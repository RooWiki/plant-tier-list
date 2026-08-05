# 🌿 Plant Tier List Video Generator

Automatically generates short-form social media videos about plants, optimized for TikTok / Instagram Reels (1080×1920).

Two video formats available:

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Format 1 — Rarity Tier List (`main.py`)

Ranks 10 plants from a country by rarity using iNaturalist observation data, revealing each plant into a tier list (SS+ → F).

**How it works:**
1. Scores plant rarity from real [iNaturalist](https://www.inaturalist.org/) observation counts
2. Downloads plant photos from the iNaturalist API
3. Generates a 30-second video placing each plant into its tier, ending with the full reveal

### Tiers

| Tier | Rarity |
|------|--------|
| SS+  | Critically rare / near extinct |
| SS   | Very rare, few known populations |
| S    | Rare, hard to find |
| A    | Uncommon |
| B    | Moderately common |
| C    | Fairly common |
| D    | Very common |
| F    | Widespread / invasive |

### Usage

```bash
# Built-in country presets
python main.py mexico
python main.py colombia
python main.py australia

# Custom plant list
python main.py japan --plantas "Prunus serrulata" "Wisteria floribunda" "Nelumbo nucifera"

# Custom output path and duration
python main.py mexico --duracion 30 --salida ~/Videos/mexico_plants.mp4
```

### Adding a new country

Edit `config.py` and add an entry to `COUNTRY_PLANTS`:

```python
COUNTRY_PLANTS = {
    "peru": [
        "Puya raimondii",
        "Cinchona officinalis",
        # ...
    ],
}
```

---

## Format 2 — Most Dangerous Plants (`main_danger.py`)

"Mr. Incredible becoming uncanny" format: 10 dangerous plants from a country revealed one by one, synced to the iconic meme music. Each plant gets a card with the plant photo on top and the corresponding Mr. Incredible face below — from calm (plant 1, least dangerous) to fully uncanny (plant 10, most dangerous).

**How it works:**
1. Uses a predefined list of 10 dangerous plants per country (or asks Claude AI to generate one)
2. Downloads plant photos from iNaturalist
3. Downloads a country landscape photo as background
4. Assembles a video synced to the music, with each plant showing for its matching music segment

### Music timing

| Plant | Danger level | Music segment |
|-------|-------------|---------------|
| 1  | Least dangerous | 0 – 3 s  |
| 2  |                 | 3 – 6 s  |
| 3  |                 | 6 – 11 s |
| 4  |                 | 11 – 14 s |
| 5  |                 | 14 – 19 s |
| 6  |                 | 19 – 21 s |
| 7  |                 | 21 – 24 s |
| 8  |                 | 24 – 32 s |
| 9  |                 | 32 – 43 s |
| 10 | Most dangerous  | 43 s – end |

### Usage

```bash
# Built-in country presets (mexico, colombia, australia)
python main_danger.py mexico
python main_danger.py colombia

# Custom output path
python main_danger.py australia --salida ~/Videos/australia_danger.mp4
```

### Adding a new country

Edit `config.py` and add an entry to `DANGER_PLANTS` ordered from least to most dangerous:

```python
DANGER_PLANTS = {
    "peru": [
        "Euphorbia milii",       # 1 – least dangerous
        "Solanum americanum",    # 2
        # ...
        "Hippomane mancinella",  # 10 – most dangerous
    ],
}
```

If the country is not in `DANGER_PLANTS`, the script automatically asks Claude AI to generate the list (requires `ANTHROPIC_API_KEY`).

---

## Requirements

- Python 3.10+
- FFmpeg (`sudo pacman -S ffmpeg` or `sudo apt install ffmpeg`)

## Installation

```bash
git clone https://github.com/RooWiki/plant-tier-list.git
cd plant-tier-list

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

### Claude AI (optional)

Used as fallback for rarity scoring (format 1) and to generate dangerous plant lists for unlisted countries (format 2):

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

Get a key at [console.anthropic.com](https://console.anthropic.com).

## Output

Videos are saved to `output/` as `.mp4` (1080×1920).
Plant images are cached in `images/` by country and species — re-runs are instant.

## Project structure

```
plant-tier-list/
├── main.py               # Format 1: rarity tier list
├── main_danger.py        # Format 2: most dangerous plants
├── config.py             # Tiers, colors, plant lists, timing config
├── src/
│   ├── rarity.py         # iNaturalist scoring + Claude fallback
│   ├── searcher.py       # Image download (iNaturalist API + DDGS fallback)
│   ├── graphics.py       # Frame rendering (format 1)
│   ├── video.py          # Video assembly (format 1)
│   ├── danger_graphics.py  # Card rendering (format 2)
│   ├── danger_video.py     # Video assembly with music sync (format 2)
│   └── danger_ranker.py    # Claude-based plant danger ranking (format 2)
├── memes/
│   └── mr increible/     # Mr. Incredible phases 1–10 (jpg)
├── music/                # Background music for format 2
├── images/               # Auto-created, git-ignored
└── output/               # Auto-created, git-ignored
```

## License

MIT
