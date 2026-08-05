from pathlib import Path

from moviepy import AudioFileClip, ImageClip, concatenate_audioclips, concatenate_videoclips

from config import DANGER_TIMESTAMPS, FPS
from src.danger_graphics import render_danger_card, render_intro_card

INTRO_DURATION = 3.0  # seconds the intro card is shown before the plants


def create_danger_video(
    plants: list[dict],
    country: str,
    output_path: Path,
    music_path: Path,
    bg_img_path: Path | None = None,
) -> Path:
    """
    plants: list of 10 dicts (ordered least → most dangerous):
        { 'name': str, 'plant_img': Path|None, 'mr_img': Path|None }
    """
    audio = AudioFileClip(str(music_path))
    music_dur = audio.duration

    timestamps = DANGER_TIMESTAMPS + [music_dur]
    durations = [timestamps[i + 1] - timestamps[i] for i in range(10)]

    # Intro card — plays with the first INTRO_DURATION seconds of music
    intro_frame = render_intro_card(country, bg_img_path)
    clips = [ImageClip(intro_frame, duration=INTRO_DURATION)]

    for i, plant in enumerate(plants):
        frame = render_danger_card(
            plant_name=plant["name"],
            plant_img_path=plant.get("plant_img"),
            mr_img_path=plant.get("mr_img"),
            bg_img_path=bg_img_path,
        )
        clips.append(ImageClip(frame, duration=durations[i]))

    video = concatenate_videoclips(clips)

    # Intro plays in silence; music starts after INTRO_DURATION seconds
    silence = audio.subclipped(0, INTRO_DURATION).with_volume_scaled(0)
    music   = audio.subclipped(0, min(video.duration - INTRO_DURATION, music_dur))
    video   = video.with_audio(concatenate_audioclips([silence, music]))

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
    return output_path
