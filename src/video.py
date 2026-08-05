from pathlib import Path

import numpy as np
from moviepy import ImageClip, concatenate_videoclips

from config import TIERS, FPS
from src.graphics import render_tierlist, render_plant_card


def _clip(arr: np.ndarray, duration: float) -> ImageClip:
    return ImageClip(arr, duration=duration)


def create_video(
    scored: dict[str, tuple[str, str]],
    plant_images: dict[str, list[Path]],
    country: str,
    output_path: Path,
    total_seconds: float = 30.0,
) -> Path:
    """
    scored: {planta_original: (tier, nombre_mostrar)}
    plant_images: {planta_original: [Path, ...]}
    """
    clips = []
    tiers_data: dict[str, list[tuple[str, Path | None]]] = {t: [] for t in TIERS}

    n = len(scored)
    # Distribuir tiempo: 2s intro + n*card + n*reveal + 5s final
    card_t   = max(1.5, min((total_seconds - 7) / n * 0.6, 3.5))
    reveal_t = max(0.8, min((total_seconds - 7) / n * 0.4, 2.0))

    # ── Intro (tier list vacío) ──────────────────────────────────────────────
    clips.append(_clip(render_tierlist(tiers_data, country), duration=2.0))

    # ── Una planta por turno ─────────────────────────────────────────────────
    for plant_orig, (tier, display) in scored.items():
        imgs = plant_images.get(plant_orig, [])
        img_path = imgs[0] if imgs else None

        # Tarjeta de planta
        card_arr = render_plant_card(display, tier, img_path)
        clips.append(_clip(card_arr, duration=card_t))

        # Agregar planta al tier y mostrar tier list actualizado
        tiers_data[tier].append((display, img_path))
        reveal_arr = render_tierlist(tiers_data, country)
        clips.append(_clip(reveal_arr, duration=reveal_t))

    # ── Reveal final ─────────────────────────────────────────────────────────
    clips.append(_clip(render_tierlist(tiers_data, country), duration=5.0))

    output_path.parent.mkdir(parents=True, exist_ok=True)

    video = concatenate_videoclips(clips)
    video.write_videofile(
        str(output_path),
        fps=FPS,
        codec="libx264",
        audio=False,
        logger="bar",
    )
    video.close()
    return output_path
