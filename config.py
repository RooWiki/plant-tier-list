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

MEMES_DIR         = BASE_DIR / "memes" / "mr increible"
MUSIC_PATH        = BASE_DIR / "music" / "mr-incredible-becomes-uncanny-all-songs-music.mp3"
INTRO_MUSIC_PATH  = BASE_DIR / "music" / "intro.m4a"
BG_DIR            = IMAGES_DIR / "backgrounds"

# Tiempos (segundos) en que la música cambia de fase — un timestamp por planta
DANGER_TIMESTAMPS = [0, 3, 6, 11, 14, 19, 21, 24, 32, 43]

# Plantas peligrosas por país, ordenadas de MENOS a MÁS peligrosa (1→10)
DANGER_PLANTS = {
    "mexico": [
        "Euphorbia milii",        # 1 – irritante cutáneo leve
        "Solanum americanum",     # 2 – tóxico si se ingiere en cantidad
        "Dieffenbachia seguine",  # 3 – cristales de oxalato, irrita boca/garganta
        "Nerium oleander",        # 4 – glucósidos cardíacos
        "Datura stramonium",      # 5 – anticolinérgico potente, alucinógeno
        "Brugmansia suaveolens",  # 6 – muy tóxico, anticolinérgico fuerte
        "Taxus globosa",          # 7 – taxina, altamente tóxico
        "Ricinus communis",       # 8 – ricina, mortal en dosis bajas
        "Conium maculatum",       # 9 – cicuta, neurotóxica, parálisis
        "Hippomane mancinella",   # 10 – el árbol más peligroso del mundo
    ],
    "colombia": [
        "Euphorbia tirucalli",    # 1
        "Jatropha curcas",        # 2
        "Solanum nigrum",         # 3
        "Nerium oleander",        # 4
        "Datura stramonium",      # 5
        "Brugmansia arborea",     # 6
        "Thevetia peruviana",     # 7
        "Ricinus communis",       # 8
        "Conium maculatum",       # 9
        "Hippomane mancinella",   # 10
    ],
    "australia": [
        "Euphorbia peplus",       # 1
        "Solanum laciniatum",     # 2
        "Lantana camara",         # 3
        "Nerium oleander",        # 4
        "Atropa belladonna",      # 5
        "Abrus precatorius",      # 6
        "Ricinus communis",       # 7
        "Conium maculatum",       # 8
        "Dendrocnide moroides",   # 9 – gympie-gympie, dolor extremo por meses
        "Cerbera manghas",        # 10
    ],
    "brazil": [
        "Caladium bicolor",       # 1 – coração-de-jesus, cristales de oxalato
        "Solanum paniculatum",    # 2 – jurubeba, nightshade nativa de Brasil
        "Jatropha mollissima",    # 3 – faveleiro, endémica de la caatinga
        "Dieffenbachia seguine",  # 4 – comigo-ninguém-pode, muy tóxica en boca
        "Thevetia peruviana",     # 5 – chapéu-de-napoleão, glucósidos cardíacos
        "Brugmansia suaveolens",  # 6 – saia-branca, anticolinérgico
        "Gloriosa superba",       # 7 – gloriosa, colchicina altamente tóxica
        "Strychnos toxifera",     # 8 – curare amazónico, usado en flechas envenenadas
        "Cerbera manghas",        # 9 – glucósidos cardíacos letales
        "Strychnos nux-vomica",   # 10 – noz-vômica, estricnina, extremadamente tóxica
    ],
}

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
