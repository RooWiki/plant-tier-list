import time
from pathlib import Path
from urllib.parse import urlparse

import requests

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"}


def _download(url: str, dest: Path) -> bool:
    try:
        r = requests.get(url, headers=HEADERS, timeout=15, stream=True)
        ct = r.headers.get("content-type", "")
        if r.status_code == 200 and "image" in ct:
            dest.write_bytes(r.content)
            return dest.stat().st_size > 5_000
    except Exception:
        pass
    return False


def _ext(url: str) -> str:
    suffix = Path(urlparse(url).path).suffix.lower()
    return suffix if suffix in (".jpg", ".jpeg", ".png", ".webp") else ".jpg"


def _from_inaturalist(plant_name: str, save_dir: Path, n: int = 2) -> list[Path]:
    """Descarga fotos directamente desde la API de iNaturalist (sin rate limit)."""
    downloaded: list[Path] = []
    try:
        # Buscar el taxón
        r = requests.get(
            "https://api.inaturalist.org/v1/taxa",
            params={"q": plant_name, "rank": "species", "per_page": 1},
            timeout=12,
        )
        results = r.json().get("results", [])
        if not results:
            return []

        taxon = results[0]
        taxon_id = taxon["id"]

        # Foto principal del taxón
        default_photo = taxon.get("default_photo", {})
        if default_photo:
            url = default_photo.get("medium_url") or default_photo.get("url", "")
            if url:
                dest = save_dir / f"00{_ext(url)}"
                if _download(url, dest):
                    downloaded.append(dest)

        if len(downloaded) >= n:
            return downloaded

        # Fotos adicionales del taxón
        r2 = requests.get(
            f"https://api.inaturalist.org/v1/taxa/{taxon_id}/map_layers",
            timeout=10,
        )
        # Observaciones recientes con fotos
        r3 = requests.get(
            "https://api.inaturalist.org/v1/observations",
            params={
                "taxon_id": taxon_id,
                "photos": "true",
                "quality_grade": "research",
                "per_page": 5,
                "order_by": "votes",
            },
            timeout=12,
        )
        obs = r3.json().get("results", [])
        for i, ob in enumerate(obs):
            if len(downloaded) >= n:
                break
            photos = ob.get("photos", [])
            if photos:
                url = photos[0].get("url", "").replace("square", "medium")
                if url:
                    dest = save_dir / f"{i+1:02d}{_ext(url)}"
                    if _download(url, dest) and dest not in downloaded:
                        downloaded.append(dest)
                        time.sleep(0.2)

    except Exception as e:
        print(f"    [iNaturalist fotos] {plant_name}: {e}")

    return downloaded


def _from_ddgs(plant_name: str, country: str, save_dir: Path, n: int = 2) -> list[Path]:
    """Fallback: DuckDuckGo/DDGS."""
    downloaded: list[Path] = []
    try:
        from ddgs import DDGS
        query = f"{plant_name} plant {country}"
        with DDGS() as ddgs:
            results = list(ddgs.images(query, max_results=n + 8))
        for i, r in enumerate(results):
            if len(downloaded) >= n:
                break
            url = r.get("image", "")
            if not url:
                continue
            dest = save_dir / f"ddg_{i:02d}{_ext(url)}"
            if _download(url, dest):
                downloaded.append(dest)
                time.sleep(0.5)
    except Exception as e:
        print(f"    [DDGS] {plant_name}: {e}")
    return downloaded


def get_plant_images(plant_name: str, country: str, images_root: Path) -> list[Path]:
    """Retorna imágenes del caché o las descarga. Prioridad: iNaturalist → DDGS."""
    plant_dir = (
        images_root
        / country.lower().replace(" ", "_")
        / plant_name.lower().replace(" ", "_")
    )

    if plant_dir.exists():
        cached = sorted(
            p for p in plant_dir.iterdir()
            if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")
        )
        if cached:
            return cached

    plant_dir.mkdir(parents=True, exist_ok=True)
    print(f"    Descargando: {plant_name}...")

    imgs = _from_inaturalist(plant_name, plant_dir, n=2)
    if not imgs:
        imgs = _from_ddgs(plant_name, country, plant_dir, n=2)

    return imgs
