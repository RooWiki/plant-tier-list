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
        "Solanum esuriale",              # 1 – quena, nightshade árida nativa (endémica)
        "Pimelea trichostachya",         # 2 – lino del monte, ésteres diterpénicos, "mal de San Jorge" (endémica)
        "Macrozamia communis",           # 3 – burrawang, cycada nativa, cycasina cancerígena y neurotóxica (endémica)
        "Duboisia hopwoodii",            # 4 – pituri, tabaco sagrado aborigen, 10× más nicotina (endémica)
        "Cerbera manghas",               # 5 – suicide apple, glucósidos cardíacos (costas tropicales QLD)
        "Erythrophleum chlorostachys",   # 6 – Cooktown ironwood, eritrofleína causa paro cardíaco (endémica)
        "Gastrolobium bilobum",          # 7 – heart-leaf poison bush, fluoroacetato natural (endémica WA)
        "Acacia georginae",              # 8 – georgina gidgee, fluoroacetato (endémica Australia central)
        "Gastrolobium grandiflorum",     # 9 – poison bush del norte, fluoroacetato en toda la planta (endémica NT/QLD)
        "Dendrocnide moroides",          # 10 – gympie-gympie, tricomas silíceos, dolor extremo por meses (endémica NE QLD)
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
        "Euphorbia glauca",              # 1 – shore spurge endémica NZ, látex irritante en costas
        "Ranunculus insignis",           # 2 – buttercup alpino nativo NZ, protoanemonina vesicante (endémica)
        "Clematis paniculata",           # 3 – puawhananga nativa NZ, ranunculina en partes frescas (endémica)
        "Pimelea prostrata",             # 4 – strathmore weed nativa NZ/Australia, diterpenoides hepatotóxicos
        "Solanum laciniatum",            # 5 – poroporo, nightshade nativa de NZ y SE Australia
        "Corynocarpus laevigatus",       # 6 – karaka, endémica NZ, karakina en semilla neurotóxica
        "Taxus baccata",                 # 7 – tejo (en jardines NZ), taxina, paro cardíaco con 50 g de hoja
        "Conium maculatum",              # 8 – cicuta (naturalizada, ubicua en NZ), parálisis ascendente
        "Urtica ferox",                  # 9 – ongaonga, ortiga arbórea endémica NZ, picadura ha matado personas y caballos
        "Coriaria arborea",              # 10 – tutu, endémica NZ, tutina bloquea receptores GABA, convulsiones letales
    ],
    "papua new guinea": [
        "Solanum torvum",                # 1 – turkey berry silvestre, alcaloides esteroidales (silvestre Melanesia)
        "Calophyllum inophyllum",        # 2 – tamanu, xantonas tóxicas en frutos inmaduros (costas PNG/Fiji)
        "Brucea javanica",               # 3 – kosam, bruceolides citotóxicos (SE Asia/Melanesia)
        "Croton tiglium",                # 4 – purging croton, ésteres de forbol extremadamente irritantes (Melanesia)
        "Abrus precatorius",             # 5 – ojo de buey, abrina igual de letal que ricina (Melanesia tropical)
        "Derris elliptica",              # 6 – tuba root, rotenona, veneno de pesca tradicional melanesio
        "Pangium edule",                 # 7 – kepayang, ácido prúsico (HCN) en frutos crudos (endémico Melanesia)
        "Dichapetalum gelonioides",      # 8 – fluoroacetato sódico natural, endémica Melanesia/SE Asia
        "Antiaris toxicaria",            # 9 – árbol upas, antiarina cardiotóxica en látex, flechas envenenadas
        "Cerbera manghas",               # 10 – cerbera, glucósidos cardíacos letales (costas PNG)
    ],
    "fiji": [
        "Derris trifoliata",             # 1 – tuba marino nativo, rotenona, veneno de pesca (costas Pacífico)
        "Gnetum gnemon",                 # 2 – bago, semillas y hojas con glucósidos tóxicos en crudo (Pacífico occidental)
        "Mucuna gigantea",               # 3 – sea bean, tricomas urticantes y L-DOPA en semillas (costas Pacífico)
        "Inocarpus fagifer",             # 4 – ivi, castaño de Tahití, glucósidos cianogénicos en crudo (Pacífico)
        "Colubrina asiatica",            # 5 – lather leaf, saponinas hemolíticas (costas Pacífico Fiji/Vanuatu)
        "Barringtonia asiatica",         # 6 – vutu kana, saponinas, veneno de pesca sagrado en Fiji (Fiji/Vanuatu)
        "Excoecaria agallocha",          # 7 – mangle ciego, látex causa ceguera y quemaduras (Fiji/Vanuatu)
        "Calophyllum inophyllum",        # 8 – tamanu, xantonas y látex tóxicos en frutos inmaduros (PNG/Fiji)
        "Cycas seemannii",               # 9 – cycada endémica Pacífico Sur, cycasina neurotóxica y cancerígena (Fiji/Vanuatu)
        "Semecarpus vitiensis",          # 10 – marking nut endémica FIJI, análogo de urushiol, quemaduras químicas severas
    ],
    "solomon islands": [
        "Piper methysticum",             # 1 – kava, hepatotóxico en abuso prolongado (Salomón/Vanuatu)
        "Erythrina variegata",           # 2 – árbol del coral, eritralina alcaloide en semillas (Salomón/Vanuatu)
        "Barringtonia racemosa",         # 3 – barringtonia de río, saponinas, veneno de pesca tradicional
        "Brucea javanica",               # 4 – kosam, bruceolides citotóxicos (Melanesia, PNG/Salomón)
        "Croton tiglium",                # 5 – purging croton, ésteres de forbol (Melanesia, PNG/Salomón)
        "Derris elliptica",              # 6 – tuba, rotenona, veneno de pesca (Melanesia, PNG/Salomón)
        "Inocarpus fagifer",             # 7 – ivi, glucósidos cianogénicos en semillas crudas (Fiji/Salomón)
        "Pangium edule",                 # 8 – kepayang, HCN letal en frutos crudos (Melanesia, PNG/Salomón)
        "Dendrocnide latifolia",         # 9 – stinging tree melanesio, tricomas urticantes (Salomón/Vanuatu)
        "Dichapetalum gelonioides",      # 10 – fluoroacetato sódico natural, endémica Melanesia (PNG/Salomón)
    ],
    "vanuatu": [
        "Tephrosia purpurea",            # 1 – veneno de pesca tradicional, rotenona (Vanuatu/Pacífico)
        "Piper methysticum",             # 2 – kava, mayor consumidor mundial, hepatotóxico crónico (Salomón/Vanuatu)
        "Gyrocarpus americanus",         # 3 – árbol helicóptero, alcaloides tóxicos en frutos (Pacífico)
        "Erythrina variegata",           # 4 – árbol del coral, eritralina en semillas (Salomón/Vanuatu)
        "Mucuna gigantea",               # 5 – sea bean, tricomas urticantes y L-DOPA (Fiji/Vanuatu)
        "Colubrina asiatica",            # 6 – lather leaf, saponinas hemolíticas (Fiji/Vanuatu)
        "Barringtonia asiatica",         # 7 – vutu, saponinas, veneno de pesca sagrado (Fiji/Vanuatu)
        "Excoecaria agallocha",          # 8 – mangle ciego, látex causa ceguera temporal (Fiji/Vanuatu)
        "Cycas seemannii",               # 9 – cycada endémica Pacífico Sur, cycasina cancerígena y neurotóxica (Fiji/Vanuatu)
        "Dendrocnide latifolia",         # 10 – stinging tree melanesio, pariente del gympie-gympie (Salomón/Vanuatu)
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
