#!/usr/bin/env python3
"""
Generador de videos "plantas más peligrosas" estilo Mr. Increíble becoming uncanny.

Uso:
    python main_danger.py mexico
    python main_danger.py colombia
    python main_danger.py australia --salida ~/Videos/australia_danger.mp4
"""
import argparse
import sys
from pathlib import Path

from config import IMAGES_DIR, OUTPUT_DIR, DANGER_PLANTS, MEMES_DIR, MUSIC_PATH, BG_DIR
from src.danger_ranker import rank_dangerous_plants, get_display_name
from src.searcher import get_plant_images
from src.danger_video import create_danger_video


def get_country_bg(country: str) -> Path | None:
    BG_DIR.mkdir(parents=True, exist_ok=True)
    slug = country.lower().replace(" ", "_")
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        cached = BG_DIR / f"{slug}{ext}"
        if cached.exists():
            return cached

    try:
        import requests
        from urllib.parse import urlparse
        from ddgs import DDGS

        query = f"{country} naturaleza paisaje fotografía"
        with DDGS() as ddgs:
            results = list(ddgs.images(query, max_results=8))

        for r in results:
            url = r.get("image", "")
            if not url:
                continue
            try:
                resp = requests.get(url, timeout=10,
                                    headers={"User-Agent": "Mozilla/5.0"})
                ct = resp.headers.get("content-type", "")
                if resp.status_code == 200 and "image" in ct:
                    suffix = Path(urlparse(url).path).suffix.lower() or ".jpg"
                    dest = BG_DIR / f"{slug}{suffix}"
                    dest.write_bytes(resp.content)
                    if dest.stat().st_size > 15_000:
                        return dest
            except Exception:
                continue
    except Exception as e:
        print(f"  [aviso] Sin fondo para {country}: {e}")
    return None


def main():
    parser = argparse.ArgumentParser(description="Genera video de plantas peligrosas")
    parser.add_argument("pais", help="País (mexico, colombia, australia…)")
    parser.add_argument("--salida", default=None, help="Ruta del .mp4 de salida")
    args = parser.parse_args()

    country = args.pais.strip()
    output = (
        Path(args.salida) if args.salida
        else OUTPUT_DIR / f"{country.lower().replace(' ', '_')}_danger.mp4"
    )

    print(f"\n{'='*54}")
    print(f"  Plantas Más Peligrosas — {country.title()}")
    print(f"{'='*54}\n")

    # 1. Obtener lista de plantas
    plants_sci = DANGER_PLANTS.get(country.lower())
    if plants_sci:
        print(f"[1/4] Lista predefinida para {country} ✓")
    else:
        print("[1/4] Consultando Claude para generar lista...")
        try:
            plants_sci = rank_dangerous_plants(country)
        except Exception as e:
            print(f"[error] {e}")
            sys.exit(1)

    print("  (1=menos peligrosa → 10=más peligrosa)")
    for i, p in enumerate(plants_sci, 1):
        print(f"    {i:2d}. {p}")

    # 2. Nombres para mostrar
    print("\n[2/4] Obteniendo nombres comunes...")
    display_names = []
    for p in plants_sci:
        name = get_display_name(p)
        display_names.append(name)
        print(f"    {p} → {name}")

    # 3. Imágenes de plantas
    print("\n[3/4] Descargando imágenes...")
    plant_imgs = []
    for plant in plants_sci:
        imgs = get_plant_images(plant, country, IMAGES_DIR)
        plant_imgs.append(imgs[0] if imgs else None)
        status = "✓" if imgs else "✗ sin imagen"
        print(f"    {status} {plant}")

    # 4. Fondo del país
    print("\n[4/4] Fondo del país...")
    bg_img = get_country_bg(country)
    print(f"    {'✓ ' + bg_img.name if bg_img else '✗ usando fondo blanco'}")

    # Mr. Increíble: 1.jpg → 10.jpg
    mr_imgs = sorted(MEMES_DIR.glob("*.jpg"), key=lambda p: int(p.stem))

    plants = [
        {
            "name": display_names[i],
            "plant_img": plant_imgs[i],
            "mr_img": mr_imgs[i] if i < len(mr_imgs) else None,
        }
        for i in range(10)
    ]

    print("\n[5/4] Creando video...")
    result = create_danger_video(
        plants=plants,
        country=country.title(),
        output_path=output,
        music_path=MUSIC_PATH,
        bg_img_path=bg_img,
    )

    print(f"\n✓ Video guardado en: {result}")
    print(f"  Reproduce con: mpv '{result}'\n")


if __name__ == "__main__":
    main()
