from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from config import TIERS, TIER_COLORS, VIDEO_WIDTH, VIDEO_HEIGHT, FONT, FONT_BOLD

BG         = "#F8F9FA"
TEXT_DARK  = "#1C1C2E"
TEXT_GRAY  = "#6B7280"
GRID       = "#E5E7EB"
WHITE      = "#FFFFFF"

HEADER_H   = 200
TIER_H     = int((VIDEO_HEIGHT - HEADER_H - 40) / len(TIERS))
LABEL_W    = 170
CELL       = 140
IMG_SZ     = 110
PAD        = 16


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_BOLD if bold else FONT
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default(size)


def _hex(color: str) -> tuple[int, int, int]:
    h = color.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _rounded_paste(canvas: Image.Image, src: Image.Image, pos: tuple[int, int], radius: int = 14):
    mask = Image.new("L", src.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, *src.size], radius=radius, fill=255)
    canvas.paste(src, pos, mask)


def _load_plant_img(path: Path | None, size: int) -> Image.Image | None:
    if not path or not path.exists():
        return None
    try:
        img = Image.open(path).convert("RGB")
        # Crop cuadrado desde el centro
        w, h = img.size
        m = min(w, h)
        img = img.crop(((w - m) // 2, (h - m) // 2, (w + m) // 2, (h + m) // 2))
        return img.resize((size, size), Image.LANCZOS)
    except Exception:
        return None


# ─── Tier list ──────────────────────────────────────────────────────────────

def render_tierlist(
    tiers_data: dict[str, list[tuple[str, Path | None]]],
    country: str,
) -> np.ndarray:
    img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    # Header
    draw.rectangle([0, 0, VIDEO_WIDTH, HEADER_H], fill=WHITE)
    draw.text((VIDEO_WIDTH // 2, 70),  "Plantas Raras",         font=_font(60, bold=True),  fill=TEXT_DARK, anchor="mm")
    draw.text((VIDEO_WIDTH // 2, 140), country.upper(),         font=_font(34),              fill=TEXT_GRAY, anchor="mm")
    draw.line([0, HEADER_H, VIDEO_WIDTH, HEADER_H], fill=GRID, width=2)

    for i, tier in enumerate(TIERS):
        y = HEADER_H + 20 + i * TIER_H
        color = _hex(TIER_COLORS[tier])

        # Label
        draw.rectangle([0, y, LABEL_W, y + TIER_H], fill=color)
        brightness = sum(color) / 3
        label_fg = TEXT_DARK if brightness > 160 else WHITE
        draw.text((LABEL_W // 2, y + TIER_H // 2), tier, font=_font(40, bold=True), fill=label_fg, anchor="mm")

        # Row background alternado
        row_bg = (248, 249, 250) if i % 2 == 0 else (255, 255, 255)
        draw.rectangle([LABEL_W, y, VIDEO_WIDTH, y + TIER_H], fill=row_bg)
        draw.line([0, y, VIDEO_WIDTH, y], fill=GRID, width=1)

        # Plantas en esta fila
        plants = tiers_data.get(tier, [])
        max_cols = (VIDEO_WIDTH - LABEL_W - PAD) // (CELL + PAD)

        for j, (name, img_path) in enumerate(plants[:max_cols]):
            x = LABEL_W + PAD + j * (CELL + PAD)
            cy = y + (TIER_H - IMG_SZ - 24) // 2

            plant_img = _load_plant_img(img_path, IMG_SZ)
            if plant_img:
                _rounded_paste(img, plant_img, (x, cy))
            else:
                draw.rounded_rectangle([x, cy, x + IMG_SZ, cy + IMG_SZ], radius=10, fill=GRID)

            short = name if len(name) <= 10 else name[:9] + "…"
            draw.text((x + IMG_SZ // 2, cy + IMG_SZ + 12), short, font=_font(18), fill=TEXT_DARK, anchor="mm")

    return np.array(img)


# ─── Plant card (pantalla completa antes de revelar el tier) ─────────────────

def render_plant_card(
    display_name: str,
    tier: str,
    img_path: Path | None,
) -> np.ndarray:
    img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    color = _hex(TIER_COLORS[tier])

    # Banda superior de color
    band_h = 420
    draw.rectangle([0, 0, VIDEO_WIDTH, band_h], fill=color)

    # Tier label grande
    draw.text((VIDEO_WIDTH // 2, band_h // 2), tier, font=_font(140, bold=True), fill=TEXT_DARK, anchor="mm")

    # Imagen de la planta
    img_y = band_h + 60
    img_sz = 680
    plant_img = _load_plant_img(img_path, img_sz)
    if plant_img:
        # Sombra suave
        shadow = Image.new("RGBA", (img_sz + 20, img_sz + 20), (0, 0, 0, 0))
        shadow_d = ImageDraw.Draw(shadow)
        shadow_d.rounded_rectangle([10, 10, img_sz + 10, img_sz + 10], radius=30, fill=(0, 0, 0, 60))
        shadow = shadow.filter(ImageFilter.GaussianBlur(12))
        img.paste(shadow, ((VIDEO_WIDTH - img_sz - 20) // 2, img_y - 10), shadow)
        _rounded_paste(img, plant_img, ((VIDEO_WIDTH - img_sz) // 2, img_y), radius=28)

    else:
        x0 = (VIDEO_WIDTH - img_sz) // 2
        draw.rounded_rectangle([x0, img_y, x0 + img_sz, img_y + img_sz], radius=28, fill=GRID)

    img_bottom = img_y + img_sz

    # Nombre
    draw.text((VIDEO_WIDTH // 2, img_bottom + 70),  display_name, font=_font(54, bold=True), fill=TEXT_DARK, anchor="mm")
    draw.text((VIDEO_WIDTH // 2, img_bottom + 140), f"Tier → {tier}",   font=_font(36),             fill=TEXT_GRAY, anchor="mm")

    return np.array(img)
