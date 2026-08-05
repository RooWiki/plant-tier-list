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
    "guyana": "gy", "suriname": "sr", "french guiana": "gf",
}

# Maps each country to its continent output subfolder
COUNTRY_CONTINENT = {
    # North America
    "canada": "north_america", "usa": "north_america", "mexico": "north_america",
    "greenland": "north_america",
    # Central America
    "guatemala": "central_america", "belize": "central_america",
    "honduras": "central_america", "el salvador": "central_america",
    "nicaragua": "central_america", "costa rica": "central_america",
    "panama": "central_america",
    # Caribbean
    "cuba": "central_america", "haiti": "central_america",
    "dominican republic": "central_america", "puerto rico": "central_america",
    "jamaica": "central_america", "trinidad and tobago": "central_america",
    # South America
    "colombia": "south_america", "venezuela": "south_america",
    "guyana": "south_america", "suriname": "south_america",
    "french guiana": "south_america", "brazil": "south_america",
    "ecuador": "south_america", "peru": "south_america",
    "bolivia": "south_america", "paraguay": "south_america",
    "chile": "south_america", "argentina": "south_america",
    "uruguay": "south_america",
    # Europe
    "spain": "europe", "france": "europe", "germany": "europe",
    "italy": "europe", "portugal": "europe", "united kingdom": "europe",
    "russia": "europe", "ukraine": "europe", "poland": "europe",
    "netherlands": "europe", "belgium": "europe", "sweden": "europe",
    "norway": "europe", "finland": "europe", "denmark": "europe",
    "switzerland": "europe", "austria": "europe", "greece": "europe",
    "romania": "europe", "hungary": "europe", "czech republic": "europe",
    "slovakia": "europe", "croatia": "europe", "serbia": "europe",
    "bulgaria": "europe", "albania": "europe",
    # Middle East
    "turkey": "middle_east", "iran": "middle_east", "iraq": "middle_east",
    "saudi arabia": "middle_east", "yemen": "middle_east", "oman": "middle_east",
    "uae": "middle_east", "qatar": "middle_east", "kuwait": "middle_east",
    "jordan": "middle_east", "lebanon": "middle_east", "syria": "middle_east",
    "israel": "middle_east",
    # Africa
    "nigeria": "africa", "ethiopia": "africa", "egypt": "africa",
    "south africa": "africa", "kenya": "africa", "tanzania": "africa",
    "ghana": "africa", "cameroon": "africa", "mozambique": "africa",
    "madagascar": "africa", "angola": "africa", "zambia": "africa",
    "zimbabwe": "africa", "senegal": "africa", "mali": "africa",
    "niger": "africa", "chad": "africa", "sudan": "africa",
    "somalia": "africa", "drc": "africa", "congo": "africa",
    "ivory coast": "africa", "morocco": "africa", "algeria": "africa",
    "tunisia": "africa", "libya": "africa",
    # Asia
    "china": "asia", "india": "asia", "japan": "asia", "south korea": "asia",
    "north korea": "asia", "vietnam": "asia", "thailand": "asia",
    "indonesia": "asia", "philippines": "asia", "malaysia": "asia",
    "myanmar": "asia", "cambodia": "asia", "laos": "asia",
    "bangladesh": "asia", "pakistan": "asia", "afghanistan": "asia",
    "nepal": "asia", "sri lanka": "asia", "singapore": "asia",
    "mongolia": "asia", "kazakhstan": "asia", "uzbekistan": "asia",
    "taiwan": "asia",
    # Oceania
    "australia": "oceania", "new zealand": "oceania",
    "papua new guinea": "oceania", "fiji": "oceania",
    "solomon islands": "oceania", "vanuatu": "oceania",
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
    continent = COUNTRY_CONTINENT.get(country.lower(), "other")
    output = (
        Path(args.salida) if args.salida
        else OUTPUT_DIR / continent / f"{country.lower().replace(' ', '_')}_danger.mp4"
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
