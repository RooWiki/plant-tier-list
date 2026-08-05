# 🌿 Plant Tier List Video Generator

Automatically generates short-form social media videos about plants.

Two video formats available:

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Format 1 — Rarity Tier List (`main.py`)

Ranks 10 plants from a country by rarity using iNaturalist observation data, revealing each plant into a tier list (SS+ → F). Output: 1080×1920 mp4.

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

"Mr. Incredible becoming uncanny" format: 10 dangerous plants from a country revealed one by one, synced to the iconic meme music. Output: **1080×2338** mp4 (iPhone 12 Pro full-screen ratio, 19.5:9).

**Card layout:**
- **Top half:** country flag as background, plant name in uppercase on a white strip, plant photo below
- **Bottom half:** dark background with the matching Mr. Incredible face (phase 1 = least dangerous → phase 10 = most dangerous)

**How it works:**
1. Uses a predefined list of 10 dangerous plants per country (or asks Claude AI to generate one)
2. Downloads plant photos from iNaturalist
3. Downloads the country flag from flagcdn.com as card background
4. **4-second intro card** — shows "MOST DANGEROUS PLANTS OF [COUNTRY]" with intro music + English TTS voice
5. Assembles the video synced to the Mr. Incredible becoming uncanny music, with each plant showing for its matching music segment and a 0.2s fade-in transition

### Audio

| Segment | What plays |
|---------|-----------|
| 0 – 4 s (intro) | `music/intro.m4a` + gTTS voice |
| 4 s onwards | `music/mr-incredible-becomes-uncanny-all-songs-music.mp3` |

### Music timing (relative to mr-incredible track start)

| Plant | Danger level | Segment |
|-------|-------------|---------|
| 1  | Least dangerous | 0 – 3 s   |
| 2  |                 | 3 – 6 s   |
| 3  |                 | 6 – 11 s  |
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

Videos are saved to `output/` as `.mp4`.
Plant images and country flags are cached in `images/` — re-runs are instant.

## Project structure

```
plant-tier-list/
├── main.py                 # Format 1: rarity tier list
├── main_danger.py          # Format 2: most dangerous plants
├── config.py               # Tiers, colors, plant lists, timing, paths
├── src/
│   ├── rarity.py           # iNaturalist scoring + Claude fallback
│   ├── searcher.py         # Plant image download (iNaturalist + DDGS)
│   ├── graphics.py         # Frame rendering (format 1)
│   ├── video.py            # Video assembly (format 1)
│   ├── danger_graphics.py  # Card rendering (format 2)
│   ├── danger_video.py     # Video assembly + audio mixing (format 2)
│   └── danger_ranker.py    # Claude-based danger ranking (format 2)
├── memes/
│   └── mr increible/       # Mr. Incredible phases 1–10 (jpg)
├── music/
│   ├── intro.m4a           # Intro background audio (first 4 s)
│   └── mr-incredible-becomes-uncanny-all-songs-music.mp3
├── images/                 # Auto-created, git-ignored
└── output/                 # Auto-created, git-ignored
```

## License

MIT
