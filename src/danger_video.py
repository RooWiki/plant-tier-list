import tempfile
from pathlib import Path

import numpy as np
from moviepy import (
    AudioFileClip, CompositeAudioClip, ImageClip,
    concatenate_audioclips, concatenate_videoclips,
    vfx,
)

from config import DANGER_TIMESTAMPS, FPS, INTRO_MUSIC_PATH
from src.danger_graphics import render_danger_card, render_intro_card

INTRO_DURATION = 4.0

# iPhone 12 Pro: 2532×1170px → at 1080 width → height = 1080*(2532/1170) ≈ 2337
CANVAS_W  = 1080
CANVAS_H  = 2338
CONTENT_H = 1920                         # existing layout height
CONTENT_Y = (CANVAS_H - CONTENT_H) // 2  # 209px black bar top & bottom


def _to_canvas(frame: np.ndarray) -> np.ndarray:
    """Centers a 1080×1920 frame inside a 1080×2338 black canvas."""
    canvas = np.zeros((CANVAS_H, CANVAS_W, 3), dtype=np.uint8)
    canvas[CONTENT_Y:CONTENT_Y + CONTENT_H] = frame
    return canvas


def _generate_tts(text: str) -> Path:
    from gtts import gTTS
    path = Path(tempfile.mktemp(suffix=".mp3"))
    gTTS(text=text, lang="en", slow=False).save(str(path))
    return path


def create_danger_video(
    plants: list[dict],
    country: str,
    output_path: Path,
    music_path: Path,
    bg_img_path: Path | None = None,
) -> Path:
    """
    plants: list of 10 dicts (least → most dangerous):
        { 'name': str, 'plant_img': Path|None, 'mr_img': Path|None }
    """
    audio     = AudioFileClip(str(music_path))
    music_dur = audio.duration

    timestamps = DANGER_TIMESTAMPS + [music_dur]
    durations  = [timestamps[i + 1] - timestamps[i] for i in range(10)]

    # ── Intro clip ────────────────────────────────────────────────────────────
    intro_frame = render_intro_card(country, bg_img_path)
    clips = [ImageClip(_to_canvas(intro_frame), duration=INTRO_DURATION)]

    # ── Plant clips with fade-in for smooth sync ──────────────────────────────
    for i, plant in enumerate(plants):
        frame = render_danger_card(
            plant_name=plant["name"],
            plant_img_path=plant.get("plant_img"),
            mr_img_path=plant.get("mr_img"),
            bg_img_path=bg_img_path,
        )
        fade = min(0.2, durations[i] / 4)
        clip = (
            ImageClip(_to_canvas(frame), duration=durations[i])
            .with_effects([vfx.FadeIn(fade)])
        )
        clips.append(clip)

    video = concatenate_videoclips(clips)

    # ── Audio: intro music + TTS during intro, mr-incredible after ───────────
    print("  Generando voz TTS...")
    tts_path    = _generate_tts(f"Most dangerous plants of {country}")
    tts_audio   = AudioFileClip(str(tts_path))
    intro_music = AudioFileClip(str(INTRO_MUSIC_PATH)).subclipped(0, INTRO_DURATION)

    silence       = audio.subclipped(0, INTRO_DURATION).with_volume_scaled(0)
    music_portion = audio.subclipped(0, min(video.duration - INTRO_DURATION, music_dur))
    delayed_music = concatenate_audioclips([silence, music_portion])

    final_audio = CompositeAudioClip([delayed_music, intro_music, tts_audio])
    final_audio = final_audio.with_duration(video.duration)
    video = video.with_audio(final_audio)

    # ── Render ────────────────────────────────────────────────────────────────
    output_path.parent.mkdir(parents=True, exist_ok=True)
    video.write_videofile(
        str(output_path),
        fps=FPS,
        codec="libx264",
        audio_codec="aac",
        logger="bar",
    )
    video.close()
    audio.close()
    tts_audio.close()
    tts_path.unlink(missing_ok=True)
    return output_path
