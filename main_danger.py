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

import requests

from config import IMAGES_DIR, OUTPUT_DIR, DANGER_PLANTS, MEMES_DIR, MUSIC_PATH, BG_DIR
from src.danger_ranker import rank_dangerous_plants, get_display_name
from src.searcher import get_plant_images
from src.danger_video import create_danger_video

# ISO 3166-1 alpha-2 codes for flagcdn.com
COUNTRY_CODES = {
    "mexico": "mx", "colombia": "co", "australia": "au",
    "argentina": "ar", "brazil": "br", "canada": "ca",
    "usa": "us", "spain": "es", "france": "fr", "germany": "de",
    "japan": "jp", "china": "cn", "india": "in", "peru": "pe",
    "chile": "cl", "venezuela": "ve", "ecuador": "ec",
    "bolivia": "bo", "paraguay": "py", "uruguay": "uy",
    "costa rica": "cr", "panama": "pa", "cuba": "cu",
    "dominican republic": "do", "guatemala": "gt", "honduras": "hn",
    "el salvador": "sv", "nicaragua": "ni", "puerto rico": "pr",
}


def get_country_flag(country: str) -> Path | None:
    BG_DIR.mkdir(parents=True, exist_ok=True)
    slug = country.lower().replace(" ", "_")
    cached = BG_DIR / f"flag_{slug}.jpg"
    if cached.exists():
        return cached

    code = COUNTRY_CODES.get(country.lower())
    if not code:
        # Try pycountry as fallback
        try:
            import pycountry
            match = pycountry.countries.search_fuzzy(country)
            if match:
                code = match[0].alpha_2.lower()
        except Exception:
            pass

    if not code:
        print(f"  [aviso] Código de país no encontrado para '{country}'")
        return None

    url = f"https://flagcdn.com/w1280/{code}.jpg"
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code == 200:
            cached.write_bytes(resp.content)
            return cached
    except Exception as e:
        print(f"  [aviso] No se pudo descargar bandera: {e}")
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

    # 4. Bandera del país
    print("\n[4/4] Descargando bandera...")
    bg_img = get_country_flag(country)
    print(f"    {'✓ ' + bg_img.name if bg_img else '✗ sin bandera (fondo oscuro)'}")

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
