#!/usr/bin/env python3
"""
Generador automático de videos tier list de plantas para redes sociales.

Uso:
    python main.py mexico
    python main.py colombia
    python main.py australia
    python main.py mexico --plantas "Vanilla planifolia" "Agave tequilana" "Dahlia imperialis"
    python main.py mexico --salida ~/Videos/plantas_mexico.mp4
"""
import argparse
import sys
from pathlib import Path

from config import IMAGES_DIR, OUTPUT_DIR, COUNTRY_PLANTS
from src.rarity import score_plants
from src.searcher import get_plant_images
from src.video import create_video


def main():
    parser = argparse.ArgumentParser(description="Genera un video tier list de plantas")
    parser.add_argument("pais", help="País (mexico, colombia, australia, o cualquier otro)")
    parser.add_argument("--plantas", nargs="+", metavar="PLANTA", help="Lista personalizada de plantas")
    parser.add_argument("--salida", default=None, help="Ruta del video de salida (.mp4)")
    parser.add_argument("--duracion", type=float, default=30.0, help="Duración en segundos (default: 30)")
    args = parser.parse_args()

    country = args.pais.strip()
    plants  = args.plantas or COUNTRY_PLANTS.get(country.lower(), None)

    if not plants:
        print(f"[error] No hay plantas predefinidas para '{country}'.")
        print(f"Países disponibles: {', '.join(COUNTRY_PLANTS.keys())}")
        print("Usa --plantas para especificar una lista propia.")
        sys.exit(1)

    output = Path(args.salida) if args.salida else OUTPUT_DIR / f"{country.lower().replace(' ', '_')}_tierlist.mp4"

    print(f"\n{'='*50}")
    print(f"  Tier List: Plantas Raras de {country.title()}")
    print(f"  {len(plants)} plantas | {args.duracion}s | {output.name}")
    print(f"{'='*50}\n")

    # 1. Puntuar rareza
    print("[1/3] Analizando rareza con iNaturalist + Claude...")
    scored = score_plants(plants, country)

    print(f"\n  Resultado:")
    for plant, (tier, display) in scored.items():
        print(f"    {tier:4s}  {display}")

    # 2. Descargar imágenes
    print("\n[2/3] Descargando imágenes...")
    plant_images = {}
    for plant in plants:
        imgs = get_plant_images(plant, country, IMAGES_DIR)
        plant_images[plant] = imgs
        status = f"{len(imgs)} imagen(es)" if imgs else "sin imágenes"
        print(f"    {plant}: {status}")

    # 3. Crear video
    print("\n[3/3] Creando video...")
    result = create_video(scored, plant_images, country.title(), output, args.duracion)

    print(f"\n✓ Video guardado en: {result}")
    print(f"  Abre con: mpv '{result}'\n")


if __name__ == "__main__":
    main()
