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
    "argentina": [
        "Euphorbia selloi",       # 1 – irritante cutáneo leve, nativa del Cono Sur
        "Solanum sisymbriifolium",# 2 – revienta caballos, nativa argentina
        "Nicotiana longiflora",   # 3 – tabaquillo, endémica argentina
        "Cestrum parqui",         # 4 – palqui, hepatotóxica
        "Datura ferox",           # 5 – chamico, anticolinérgico nativo
        "Senecio grisebachii",    # 6 – yerba de la oveja, pirrolizidinas
        "Solanum glaucophyllum",  # 7 – duraznillo blanco, hipervitaminosis D
        "Baccharis coridifolia",  # 8 – mío-mío, poliacetilenos muy tóxicos
        "Brugmansia sanguinea",   # 9 – floripón rojo andino, muy tóxico
        "Veratrum album",         # 10 – cebadilla, alcaloides de veratrum letales
    ],
    "bolivia": [
        "Acnistus arborescens",   # 1 – borrachero de monte, bayas tóxicas
        "Solanum americanum",     # 2 – hierba mora
        "Nicotiana rustica",      # 3 – mapacho, tabaco nativo muy potente
        "Cestrum auriculatum",    # 4 – hierba santa, hepatotóxica
        "Datura ferox",           # 5 – chamico, anticolinérgico
        "Thevetia peruviana",     # 6 – cabalonga, glucósidos cardíacos
        "Brunfelsia grandiflora", # 7 – manacá, muy tóxica post-alucinógeno
        "Brugmansia arborea",     # 8 – floripondio, anticolinérgico potente
        "Strychnos toxifera",     # 9 – curare amazónico
        "Aconitum columbianum",   # 10 – acónito andino, aconitina, mortal en mg
    ],
    "chile": [
        "Drimys winteri",         # 1 – canelo, irritante moderado
        "Solanum nigrum",         # 2 – hierba mora
        "Cestrum parqui",         # 3 – palqui, nativa de Chile, hepatotóxica
        "Nicotiana rustica",      # 4 – tabaco silvestre
        "Datura stramonium",      # 5 – chamico
        "Senecio erraticus",      # 6 – raguay, pirrolizidinas
        "Conium maculatum",       # 7 – cicuta, neurotóxica
        "Veratrum album",         # 8 – cebadilla, alcaloides letales
        "Brugmansia sanguinea",   # 9 – floripón, anticolinérgico
        "Lobelia tupa",           # 10 – tupa, endémica chilena, lobelina muy tóxica
    ],
    "ecuador": [
        "Euphorbia cotinifolia",  # 1 – sangre de Cristo, irritante
        "Lantana camara",         # 2 – lantana, bayas tóxicas
        "Solanum quitoense",      # 3 – naranjilla, tallos y hojas tóxicos
        "Dieffenbachia seguine",  # 4 – lotería, oxalatos
        "Thevetia peruviana",     # 5 – cabalonga, glucósidos cardíacos
        "Brunfelsia grandiflora", # 6 – manacá, tóxica en todas sus partes
        "Datura stramonium",      # 7 – chamico
        "Psychotria viridis",     # 8 – chacruna, DMT, componente del ayahuasca
        "Brugmansia arborea",     # 9 – borrachero, anticolinérgico potente
        "Brugmansia candida",     # 10 – guanto, el borrachero más potente del Ecuador
    ],
    "peru": [
        "Euphorbia cotinifolia",  # 1 – sangre de toro
        "Solanum americanum",     # 2 – hierba mora
        "Nicotiana rustica",      # 3 – mapacho, tabaco ritual muy potente
        "Carapichea ipecacuanha", # 4 – ipecacuana, emetina tóxica en altas dosis
        "Thevetia peruviana",     # 5 – cabalonga
        "Brunfelsia grandiflora", # 6 – manacá
        "Psychotria viridis",     # 7 – chacruna, ayahuasca
        "Datura stramonium",      # 8 – chamico
        "Brugmansia arborea",     # 9 – toé, usado en rituales, muy peligroso
        "Clibadium sylvestre",    # 10 – barbasco amazónico, ictiotóxico, letal
    ],
    "venezuela": [
        "Euphorbia cotinifolia",  # 1 – lechero rojo, irritante
        "Lantana camara",         # 2 – venturosa, bayas tóxicas
        "Solanum torvum",         # 3 – berenjena cimarrona
        "Dieffenbachia seguine",  # 4 – lotería, oxalatos
        "Thevetia peruviana",     # 5 – cobalonga, glucósidos cardíacos
        "Brunfelsia uniflora",    # 6 – manacá venezolano
        "Gliricidia sepium",      # 7 – mata ratón, rodenticida natural
        "Brugmansia suaveolens",  # 8 – borrachero, anticolinérgico
        "Cerbera manghas",        # 9 – glucósidos cardíacos letales
        "Strychnos nux-vomica",   # 10 – nuez vómica, estricnina
    ],
    "paraguay": [
        "Euphorbia heterophylla", # 1 – lecherita del campo
        "Solanum sisymbriifolium",# 2 – tomatillo del campo
        "Nicotiana tabacum",      # 3 – tabaco, cultivado históricamente en Paraguay
        "Jatropha curcas",        # 4 – piñón, semillas altamente tóxicas
        "Datura ferox",           # 5 – chamico
        "Wedelia glauca",         # 6 – yuyo sonso, tóxica para ganado y humanos
        "Cestrum parqui",         # 7 – duraznillo negro, hepatotóxico
        "Baccharis coridifolia",  # 8 – mío-mío, poliacetilenos muy tóxicos
        "Ricinus communis",       # 9 – tártago, ricina
        "Solanum glaucophyllum",  # 10 – duraznillo blanco, calcinosis enzoótica
    ],
    "uruguay": [
        "Euphorbia peplus",       # 1 – pichoga, irritante leve
        "Solanum sisymbriifolium",# 2 – revienta caballos
        "Nicotiana tabacum",      # 3 – tabaco
        "Wedelia glauca",         # 4 – yuyo sonso, hepatotóxica
        "Cestrum parqui",         # 5 – palqui, hepatotóxica
        "Datura ferox",           # 6 – chamico, anticolinérgico
        "Senecio madagascariensis",# 7 – flor de setiembre, pirrolizidinas
        "Baccharis coridifolia",  # 8 – mío-mío
        "Conium maculatum",       # 9 – cicuta, parálisis
        "Solanum glaucophyllum",  # 10 – duraznillo blanco, hipervitaminosis D letal
    ],
    "guyana": [
        "Lantana camara",         # 1 – lantana
        "Jatropha gossypifolia",  # 2 – bellyache bush, semillas tóxicas
        "Mucuna pruriens",        # 3 – pica-pica, picazón severa + L-DOPA
        "Dieffenbachia seguine",  # 4 – dumb cane
        "Abrus precatorius",      # 5 – ojo de buey, abrina tan letal como ricina
        "Thevetia peruviana",     # 6 – glucósidos cardíacos
        "Gliricidia sepium",      # 7 – mata ratón, tóxica para mamíferos
        "Caladium bicolor",       # 8 – corazón de Jesús, oxalatos
        "Cerbera manghas",        # 9 – glucósidos cardíacos letales
        "Strychnos toxifera",     # 10 – curare, usado en flechas envenenadas
    ],
    "suriname": [
        "Euphorbia heterophylla", # 1 – irritante
        "Jatropha gossypifolia",  # 2 – bottelboom, semillas muy tóxicas
        "Mucuna pruriens",        # 3 – pica-pica, picazón intensa
        "Lantana camara",         # 4 – bayas tóxicas
        "Dieffenbachia seguine",  # 5 – oxalatos
        "Abrus precatorius",      # 6 – wegaap, abrina extremadamente tóxica
        "Thevetia peruviana",     # 7 – glucósidos cardíacos
        "Caladium bicolor",       # 8 – cristales de oxalato
        "Strychnos toxifera",     # 9 – woorali, curare
        "Physostigma venenosum",  # 10 – haba del Calabar, fisostigmina letal
    ],
    "new zealand": [
        "Euphorbia lathyris",     # 1 – tártago, irritante cutáneo leve
        "Solanum nigrum",         # 2 – hierba mora, bayas tóxicas
        "Lantana camara",         # 3 – lantana (introducida), bayas tóxicas
        "Nerium oleander",        # 4 – adelfa, glucósidos cardíacos
        "Datura stramonium",      # 5 – estramonio, anticolinérgico potente
        "Conium maculatum",       # 6 – cicuta, neurotóxica, muy abundante en NZ
        "Corynocarpus laevigatus",# 7 – karaka, endémica, semillas con karakina
        "Taxus baccata",          # 8 – tejo, taxina letal (jardines)
        "Urtica ferox",           # 9 – ongaonga, ortiga arbórea endémica, picadura fatal
        "Coriaria arborea",       # 10 – tutu, endémica, tutina causa convulsiones letales
    ],
    "papua new guinea": [
        "Euphorbia tirucalli",    # 1 – árbol de lápiz, látex irritante
        "Lantana camara",         # 2 – lantana, bayas tóxicas
        "Mucuna pruriens",        # 3 – pica-pica, picazón intensa + L-DOPA
        "Dieffenbachia seguine",  # 4 – dumb cane, cristales de oxalato
        "Abrus precatorius",      # 5 – ojo de buey, abrina tan letal como ricina
        "Gloriosa superba",       # 6 – gloriosa, colchicina altamente tóxica
        "Thevetia peruviana",     # 7 – glucósidos cardíacos
        "Cerbera manghas",        # 8 – cerbera, glucósidos cardíacos letales
        "Strychnos nux-vomica",   # 9 – nuez vómica, estricnina
        "Antiaris toxicaria",     # 10 – árbol upas, látex usado en flechas envenenadas
    ],
    "fiji": [
        "Euphorbia hirta",        # 1 – euphorbia del asma, irritante leve
        "Solanum nigrum",         # 2 – hierba mora, bayas tóxicas
        "Lantana camara",         # 3 – lantana, hepatotóxica en ganado
        "Jatropha curcas",        # 4 – piñón, semillas altamente tóxicas
        "Dieffenbachia seguine",  # 5 – dumb cane, oxalatos en boca y garganta
        "Abrus precatorius",      # 6 – ojo de buey, abrina extremadamente tóxica
        "Thevetia peruviana",     # 7 – glucósidos cardíacos
        "Barringtonia asiatica",  # 8 – vutu kana, semillas usadas como veneno de peces
        "Cerbera manghas",        # 9 – vasa, glucósidos cardíacos, común en Pacífico
        "Semecarpus vitiensis",   # 10 – endémica de Fiji, látex causa quemaduras graves
    ],
    "solomon islands": [
        "Euphorbia hirta",        # 1 – irritante leve
        "Lantana camara",         # 2 – bayas tóxicas para humanos y ganado
        "Jatropha curcas",        # 3 – semillas con curcina, altamente tóxicas
        "Mucuna pruriens",        # 4 – pica-pica, tricomas urticantes + L-DOPA
        "Dieffenbachia seguine",  # 5 – oxalatos, irrita boca y garganta
        "Abrus precatorius",      # 6 – abrina, una semilla puede ser letal
        "Thevetia peruviana",     # 7 – glucósidos cardíacos
        "Barringtonia asiatica",  # 8 – veneno de peces, saponinas tóxicas
        "Cerbera manghas",        # 9 – glucósidos cardíacos letales
        "Antiaris toxicaria",     # 10 – látex del árbol upas, usado en flechas
    ],
    "vanuatu": [
        "Euphorbia hirta",        # 1 – irritante leve
        "Lantana camara",         # 2 – bayas tóxicas
        "Jatropha curcas",        # 3 – piñón, semillas muy tóxicas
        "Dieffenbachia seguine",  # 4 – oxalatos, irrita mucosas
        "Gloriosa superba",       # 5 – gloriosa, colchicina altamente tóxica
        "Abrus precatorius",      # 6 – abrina, extremadamente tóxica
        "Thevetia peruviana",     # 7 – glucósidos cardíacos
        "Barringtonia asiatica",  # 8 – veneno tradicional de peces
        "Cerbera manghas",        # 9 – glucósidos cardíacos, común en Vanuatu
        "Excoecaria agallocha",   # 10 – mangle ciego, látex causa ceguera y ampollas
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
