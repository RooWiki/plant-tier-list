from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from config import VIDEO_WIDTH, VIDEO_HEIGHT, FONT, FONT_BOLD

TOP_H = 900
BOT_H = VIDEO_HEIGHT - TOP_H   # 1020
NAME_H = 140
PLANT_SZ = 700
STROKE = 5  # black outline thickness for text


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if bold else FONT
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default(size)


def _fill_crop(img: Image.Image, w: int, h: int) -> Image.Image:
    iw, ih = img.size
    scale = max(w / iw, h / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    img = img.resize((nw, nh), Image.LANCZOS)
    x, y = (nw - w) // 2, (nh - h) // 2
    return img.crop((x, y, x + w, y + h))


def _square_crop(img: Image.Image, size: int) -> Image.Image:
    w, h = img.size
    m = min(w, h)
    img = img.crop(((w - m) // 2, (h - m) // 2, (w + m) // 2, (h + m) // 2))
    return img.resize((size, size), Image.LANCZOS)


def _text_with_stroke(draw: ImageDraw.ImageDraw, pos: tuple, text: str,
                      font, stroke: int = STROKE):
    x, y = pos
    for dx in range(-stroke, stroke + 1):
        for dy in range(-stroke, stroke + 1):
            if dx != 0 or dy != 0:
                draw.text((x + dx, y + dy), text, font=font,
                          fill=(0, 0, 0), anchor="mm")
    draw.text((x, y), text, font=font, fill=(255, 255, 255), anchor="mm")


def render_danger_card(
    plant_name: str,
    plant_img_path: Path | None,
    mr_img_path: Path | None,
    bg_img_path: Path | None = None,
) -> np.ndarray:
    canvas = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), (30, 30, 30))

    # ── TOP SECTION ───────────────────────────────────────────────────────────
    top = Image.new("RGB", (VIDEO_WIDTH, TOP_H), (40, 40, 40))

    if bg_img_path and Path(bg_img_path).exists():
        try:
            flag = Image.open(bg_img_path).convert("RGB")
            top = _fill_crop(flag, VIDEO_WIDTH, TOP_H)
        except Exception:
            pass

    draw_top = ImageDraw.Draw(top)

    # Plant name — UPPERCASE, white with black stroke
    name = plant_name.upper()
    font = _font(82, bold=True)
    bbox = draw_top.textbbox((0, 0), name, font=font)
    if bbox[2] - bbox[0] > VIDEO_WIDTH - 60:
        font = _font(58, bold=True)
    _text_with_stroke(draw_top, (VIDEO_WIDTH // 2, NAME_H // 2), name, font)

    # Plant image — sharp corners, centered in remaining space
    remaining = TOP_H - NAME_H
    sz = min(PLANT_SZ, remaining - 40)
    py = NAME_H + (remaining - sz) // 2
    px = (VIDEO_WIDTH - sz) // 2

    if plant_img_path and Path(plant_img_path).exists():
        try:
            plant = Image.open(plant_img_path).convert("RGB")
            plant = _square_crop(plant, sz)
            top.paste(plant, (px, py))
        except Exception:
            draw_top.rectangle([px, py, px + sz, py + sz], fill=(60, 60, 60))
    else:
        draw_top.rectangle([px, py, px + sz, py + sz], fill=(60, 60, 60))

    canvas.paste(top, (0, 0))

    # ── DIVIDER ───────────────────────────────────────────────────────────────
    ImageDraw.Draw(canvas).rectangle(
        [0, TOP_H - 3, VIDEO_WIDTH, TOP_H + 3], fill=(0, 0, 0)
    )

    # ── BOTTOM SECTION ────────────────────────────────────────────────────────
    bot = Image.new("RGB", (VIDEO_WIDTH, BOT_H), (13, 13, 13))

    if mr_img_path and Path(mr_img_path).exists():
        try:
            mr = Image.open(mr_img_path).convert("RGB")
            mw, mh = mr.size
            scale = min(VIDEO_WIDTH / mw, BOT_H / mh)
            nw, nh = int(mw * scale), int(mh * scale)
            mr = mr.resize((nw, nh), Image.LANCZOS)
            bot.paste(mr, ((VIDEO_WIDTH - nw) // 2, (BOT_H - nh) // 2))
        except Exception:
            pass

    canvas.paste(bot, (0, TOP_H))

    return np.array(canvas)
