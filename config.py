from pathlib import Path

BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / "images"
OUTPUT_DIR = BASE_DIR / "output"

TIERS = ["SS+", "SS", "S", "A", "B", "C", "D", "F"]

# Minimalista: pasteles suaves
TIER_COLORS = {
    "SS+": "#F4A7B9",
    "SS":  "#FBBF77",
    "S":   "#FDE68A",
    "A":   "#86EFAC",
    "B":   "#93C5FD",
    "C":   "#C4B5FD",
    "D":   "#CBD5E1",
    "F":   "#D1D5DB",
}

# Umbrales de rareza según observaciones en iNaturalist
# Menos observaciones = más rara
TIER_THRESHOLDS = [
    ("SS+", 0,       200),
    ("SS",  200,     1_000),
    ("S",   1_000,   5_000),
    ("A",   5_000,   20_000),
    ("B",   20_000,  75_000),
    ("C",   75_000,  250_000),
    ("D",   250_000, 750_000),
    ("F",   750_000, float("inf")),
]

VIDEO_WIDTH  = 1080
VIDEO_HEIGHT = 1920
FPS = 24

FONT        = "/usr/share/fonts/inter/InterVariable.ttf"
FONT_BOLD   = "/usr/share/fonts/inter/InterVariable.ttf"

# Plantas de ejemplo por país
COUNTRY_PLANTS = {
    "mexico": [
        "Laelia speciosa", "Mammillaria pectinifera", "Agave parrasana",
        "Lacandonia schismatica", "Selaginella lepidophylla",
        "Beaucarnea recurvata", "Dahlia imperialis", "Vanilla planifolia",
        "Fouquieria splendens", "Echeveria elegans",
    ],
    "colombia": [
        "Espeletia grandiflora", "Cattleya trianae", "Heliconia platystachys",
        "Podocarpus oleifolius", "Magnolia colombiana",
        "Guzmania lingulata", "Victoria amazonica",
        "Catasetum macrocarpum", "Zamia encephalartoides", "Oreopanax incisus",
    ],
    "australia": [
        "Wollemia nobilis", "Sturt Desert Pea", "Banksia coccinea",
        "Anigozanthos manglesii", "Telopea speciosissima",
        "Dendrobium bigibbum", "Eucryphia lucida",
        "Boronia megastigma", "Drosera binata", "Stylidium graminifolium",
    ],
}
