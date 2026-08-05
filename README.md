# 🌿 Plant Tier List Video Generator

Automatically generates short-form social media videos ranking rare plants by country using a tier list format (SS+ → F).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## What it does

1. **Scores plant rarity** using real observation data from [iNaturalist](https://www.inaturalist.org/), with Claude AI as a fallback
2. **Downloads plant photos** automatically from the iNaturalist API (organized by country/plant)
3. **Generates a 30-second video** showing each plant being placed in its tier, ending with the full tier list reveal

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

## Usage

```bash
# Built-in country presets (10 plants each)
python main.py mexico
python main.py colombia
python main.py australia

# Custom plant list
python main.py japan --plantas "Prunus serrulata" "Wisteria floribunda" "Nelumbo nucifera"

# Custom output path and duration
python main.py mexico --duracion 30 --salida ~/Videos/mexico_plants.mp4
```

### Claude AI fallback (optional)

If a plant has no iNaturalist data, the system falls back to Claude for rarity classification. To enable it, set your API key:

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

Get a key at [console.anthropic.com](https://console.anthropic.com).

## Output

Videos are saved to `output/` as `.mp4` (1080×1920, optimized for TikTok / Instagram Reels).  
Plant images are cached in `images/` by country and species, so re-runs are instant.

## Project structure

```
plant-tier-list/
├── main.py          # Entry point
├── config.py        # Tiers, colors, country plant lists
├── src/
│   ├── rarity.py    # iNaturalist scoring + Claude fallback
│   ├── searcher.py  # Image download (iNaturalist API)
│   ├── graphics.py  # Frame rendering with Pillow
│   └── video.py     # Video assembly with MoviePy
├── images/          # Auto-created, git-ignored
└── output/          # Auto-created, git-ignored
```

## Adding a new country

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

Then run `python main.py peru`.

## License

MIT
