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
        "Euphorbia antisyphilitica",     # 1 – candelilla, látex irritante leve (endémica desierto chihuahuense)
        "Argemone mexicana",             # 2 – chicalote, alcaloides isoquinolínicos hepatotóxicos (nativa México)
        "Crotalaria retusa",             # 3 – chipilillo, pirrolizidinas, adultera maíz y causa daño hepático (nativa)
        "Karwinskia humboldtiana",       # 4 – tullidora, frutos negros causan polineuropatía letal (endémica México)
        "Datura inoxia",                 # 5 – toloache, anticolinérgico potente, rituales prehispánicos (nativa México)
        "Jatropha dioica",               # 6 – sangre de drago, curcina en semillas y látex (nativa México/SW USA)
        "Taxus globosa",                 # 7 – tejo mexicano, taxina causa paro cardíaco (endémica México/C. América)
        "Ricinus communis",              # 8 – higuerilla, ricina, una semilla puede matar (naturalizada, abundante México)
        "Conium maculatum",              # 9 – cicuta (naturalizada, muy común en México), parálisis ascendente
        "Hippomane mancinella",          # 10 – manzanillo de muerte, el árbol más peligroso del mundo (costas México)
    ],
    "usa": [
        "Phytolacca americana",          # 1 – pokeweed, bayas tóxicas icónicas de Norteamérica (nativa USA)
        "Actaea pachypoda",              # 2 – white baneberry/doll's eyes, frutos blancos cardiogénicos (nativa E. USA)
        "Podophyllum peltatum",          # 3 – mayapple, podofilo-toxina potente (nativa E. USA)
        "Kalmia latifolia",              # 4 – mountain laurel, grayanotoxinas bloquean canales de sodio (nativa E. USA)
        "Ageratina altissima",           # 5 – white snakeroot, tremetona, causó "milk sickness" en pioneros (nativa)
        "Zigadenus venenosus",           # 6 – death camas, alcaloides esteroidales, mata ganado y humanos (nativa)
        "Sophora secundiflora",          # 7 – mescal bean, cytisina nicotínica, intoxicaciones rituales (nativa SW USA)
        "Aconitum uncinatum",            # 8 – eastern monkshood, aconitina, paro cardíaco en mg (nativa Apalaches)
        "Gelsemium sempervirens",        # 9 – carolina jessamine, géisemina, todas las partes letales (nativa SE USA)
        "Cicuta maculata",               # 10 – water hemlock, cicutoxina, la más violentamente tóxica de Norteamérica (nativa)
    ],
    "canada": [
        "Caltha palustris",              # 1 – marsh marigold, ranunculina en partes frescas (nativa)
        "Sanguinaria canadensis",        # 2 – bloodroot, sanguinarina alcaloide, raíz rojo sangre (nativa Canadá)
        "Sambucus racemosa",             # 3 – red elderberry, glucósidos cianogénicos en bayas crudas (nativa)
        "Actaea rubra",                  # 4 – red baneberry, frutos rojos cardiogénicos (nativa Canadá)
        "Taxus canadensis",              # 5 – tejo canadiense, taxina letal en hojas y semillas (endémica Canadá/NE USA)
        "Veratrum viride",               # 6 – false hellebore nativo Canadá/NW USA, jervina teratogénica
        "Loiseleuria procumbens",        # 7 – trailing azalea ártica nativa, grayanotoxinas cardiotóxicas
        "Aconitum delphinifolium",       # 8 – alpine monkshood ártico, aconitina, flores hermosas mortales (nativa norte Canadá)
        "Daphne mezereum",               # 9 – mezereum (naturalizada, bosques Canadá), dafnetoxina mata con pocas bayas
        "Cicuta douglasii",              # 10 – western water hemlock, cicutoxina, la más violentamente tóxica del oeste canadiense
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
    # ── Middle East ──────────────────────────────────────────────────────────
    "turkey": [
        "Euphorbia rigida",              # 1 – lechetrezna de roca, látex irritante (nativa Anatolia)
        "Ranunculus muricatus",          # 2 – botón de oro espinoso, protoanemonina (nativa)
        "Daphne pontica",                # 3 – dafne del Ponto, dafnetoxina (endémica región Ponto-Cáucaso)
        "Peganum harmala",               # 4 – harmal/ruda silvestre, beta-carbolinas psicoactivas (nativa Anatolia/Irán)
        "Hyoscyamus niger",              # 5 – beleño negro, escopolamina+atropina (nativa Turquía)
        "Digitalis ferruginea",          # 6 – dedalera oxidada, glucósidos cardíacos (nativa Turquía/Balcanes)
        "Veratrum album",                # 7 – vedegambre blanco, jervina teratogénica (nativa montañas Turquía/Irán)
        "Taxus baccata",                 # 8 – tejo, taxina letal (nativa costas del Mar Negro de Turquía)
        "Aconitum lycoctonum",           # 9 – acónito amarillo, aconitina (nativa montañas de Turquía)
        "Colchicum speciosum",           # 10 – cólchico magnífico, colchicina (endémica Turquía/Cáucaso; Turquía posee la mayor diversidad de Colchicum del mundo)
    ],
    "iran": [
        "Tribulus terrestris",           # 1 – abrojo, saponinas esteroidales hepatotóxicas (nativa estepas Irán)
        "Ferula assa-foetida",           # 2 – asafétida, furanocumarinas tóxicas (endémica Irán/Afganistán)
        "Hyoscyamus reticulatus",        # 3 – beleño reticulado, alcaloides tropanos (nativa Irán)
        "Peganum harmala",               # 4 – harmal, beta-carbolinas (nativa Irán/Turquía)
        "Sophora alopecuroides",         # 5 – sophora de estepas, matrina+citisina, parálisis (nativa estepas Irán/Asia central)
        "Datura metel",                  # 6 – estramonio asiático, alcaloides tropanos potentes (naturalizada Irán)
        "Veratrum album",                # 7 – vedegambre blanco (nativa montañas Irán/Turquía)
        "Aconitum orientale",            # 8 – acónito oriental, aconitina (nativa montañas Irán/Cáucaso)
        "Conium maculatum",              # 9 – cicuta, muy abundante en Irán (naturalizada)
        "Colchicum kotschyi",            # 10 – cólchico persa, colchicina falla multiorgánica (endémica Irán/Afganistán)
    ],
    "iraq": [
        "Solanum nigrum",                # 1 – hierba mora (naturalizada, ubicua en Irak)
        "Withania somnifera",            # 2 – ashwagandha silvestre, withanólidos somníferos (nativa Irak/Levante)
        "Tribulus terrestris",           # 3 – abrojo, saponinas (nativa Irak/Irán)
        "Papaver somniferum",            # 4 – adormidera, morfina/codeína (nativa histórica Irak/Levante)
        "Hyoscyamus muticus",            # 5 – beleño egipcio, más potente que el negro (nativa Irak/Arabia)
        "Nerium oleander",               # 6 – adelfa, glucósidos cardíacos (nativa wadis de Irak)
        "Ricinus communis",              # 7 – ricino, ricina mortal (naturalizada, muy abundante)
        "Datura stramonium",             # 8 – estramonio (naturalizada Irak)
        "Conium maculatum",              # 9 – cicuta, parálisis ascendente (naturalizada, muy común en Irak)
        "Atropa belladonna",             # 10 – belladona, en montañas kurdas del norte (nativa)
    ],
    "saudi arabia": [
        "Zygophyllum mandavillei",       # 1 – zygophyllum del Hejaz, saponinas (endémica Arabia)
        "Euphorbia larica",              # 2 – euphorbia del Golfo Pérsico, látex cáustico (nativa Arabia/Golfo)
        "Pergularia tomentosa",          # 3 – dayfah, glucósidos cardiotóxicos (nativa Arabia/N. África)
        "Rhazya stricta",               # 4 – harmal árabe, alcaloides indólicos neurotóxicos (nativa Arabia)
        "Hyoscyamus muticus",            # 5 – beleño egipcio, alcaloides tropanos (nativa Arabia)
        "Calotropis procera",            # 6 – ushur/sodom apple, látex blanco muy tóxico (nativa Arabia)
        "Citrullus colocynthis",         # 7 – coloquíntida, purgante violento letal (nativa desiertos Arabia)
        "Datura metel",                  # 8 – estramonio asiático, alcaloides (naturalizada Arabia)
        "Adenium obesum",                # 9 – rosa del desierto, glucósidos cardíacos (nativa montañas Asir)
        "Acokanthera schimperi",         # 10 – árbol veneno-flecha, ouabaína letal (nativa montañas Asir/Yemen)
    ],
    "yemen": [
        "Solanum incanum",               # 1 – berenjena silvestre, solanina (nativa Yemen/E. África)
        "Senna alexandrina",             # 2 – senna, antraquinonas tóxicas en grandes dosis (nativa Yemen/África)
        "Euphorbia ammak",               # 3 – euphorbia arbórea yemení, látex urticante (endémica SW Arabia/Yemen)
        "Pergularia tomentosa",          # 4 – dayfah, glucósidos cardiotóxicos (nativa Yemen/Arabia)
        "Calotropis procera",            # 5 – ushur, látex muy tóxico (nativa Yemen/Arabia)
        "Gloriosa superba",              # 6 – gloriosa, colchicina altamente tóxica (nativa Yemen/E. África)
        "Adenium obesum",                # 7 – rosa del desierto, glucósidos cardíacos (nativa Yemen)
        "Catha edulis",                  # 8 – khat, catinona, Yemen = mayor consumidor mundial (nativa Yemen/E. África)
        "Strophanthus sarmentosus",      # 9 – glucósidos cardiotóxicos, veneno de flecha (nativa Yemen/E. África)
        "Acokanthera schimperi",         # 10 – árbol veneno-flecha, ouabaína letal (nativa Yemen/montañas Asir)
    ],
    "oman": [
        "Sarcostemma viminale",          # 1 – viborera suculenta, látex tóxico (nativa Omán/E. África)
        "Tribulus terrestris",           # 2 – abrojo, saponinas (nativa Omán)
        "Euphorbia larica",              # 3 – euphorbia del Golfo Pérsico, látex cáustico (nativa Omán/Golfo)
        "Pergularia tomentosa",          # 4 – dayfah, glucósidos cardiotóxicos (nativa Omán/Arabia)
        "Rhazya stricta",               # 5 – harmal árabe, alcaloides neurotóxicos (nativa Omán/Arabia)
        "Calotropis procera",            # 6 – ushur, látex muy tóxico (nativa Omán/Arabia)
        "Citrullus colocynthis",         # 7 – coloquíntida, purgante violento letal (nativa desiertos Omán)
        "Datura metel",                  # 8 – estramonio asiático (naturalizada Omán)
        "Adenium obesum",                # 9 – rosa del desierto, glucósidos cardíacos (nativa Omán)
        "Euphorbia balsamifera",         # 10 – euphorbia balsámica, látex muy tóxico (nativa Omán/E. África)
    ],
    "uae": [
        "Zygophyllum qatarense",         # 1 – zygophyllum del Golfo, saponinas (nativa UAE/Qatar)
        "Leptadenia pyrotechnica",       # 2 – sarab del desierto, alcaloides cardiotóxicos (nativa UAE/Arabia)
        "Arnebia hispidissima",          # 3 – alcanetrabia espinosa, pirrolizidinas (nativa UAE/Arabia)
        "Withania somnifera",            # 4 – ashwagandha silvestre, withanólidos (nativa UAE/Levante)
        "Solanum incanum",               # 5 – berenjena silvestre (nativa UAE)
        "Euphorbia larica",              # 6 – euphorbia del Golfo, látex cáustico (nativa UAE/Omán)
        "Citrullus colocynthis",         # 7 – coloquíntida, purgante violento (nativa desiertos UAE)
        "Calotropis procera",            # 8 – ushur, látex blanco muy tóxico (nativa UAE/Arabia)
        "Rhazya stricta",               # 9 – harmal árabe, alcaloides neurotóxicos (nativa UAE/Arabia)
        "Datura metel",                  # 10 – estramonio asiático, alcaloides tropanos potentes (naturalizada UAE)
    ],
    "qatar": [
        "Zygophyllum qatarense",         # 1 – endémica Qatar/Golfo, saponinas (nativa)
        "Aerva javanica",                # 2 – lana del desierto, mildly toxic compounds (nativa Qatar)
        "Leptadenia pyrotechnica",       # 3 – sarab, alcaloides (nativa Qatar/Arabia)
        "Tribulus terrestris",           # 4 – abrojo, saponinas esteroidales (nativa Qatar)
        "Withania somnifera",            # 5 – ashwagandha, withanólidos somníferos (nativa)
        "Euphorbia larica",              # 6 – euphorbia del Golfo (nativa Qatar/Golfo)
        "Calotropis procera",            # 7 – ushur, látex blanco muy tóxico (nativa Qatar/Arabia)
        "Citrullus colocynthis",         # 8 – coloquíntida, letal en sobredosis (nativa desiertos Qatar)
        "Rhazya stricta",               # 9 – harmal árabe, neurotóxica (nativa Qatar/Arabia)
        "Hyoscyamus muticus",            # 10 – beleño egipcio, alcaloides tropanos (nativa Arabia)
    ],
    "kuwait": [
        "Zygophyllum mandavillei",       # 1 – zygophyllum (nativa Kuwait/E. Arabia)
        "Aerva javanica",                # 2 – lana del desierto (nativa Kuwait/Arabia)
        "Solanum nigrum",                # 3 – hierba mora (naturalizada)
        "Tribulus terrestris",           # 4 – abrojo, saponinas (nativa Kuwait)
        "Withania somnifera",            # 5 – ashwagandha silvestre (nativa Kuwait/Levante)
        "Euphorbia larica",              # 6 – euphorbia del Golfo (nativa Kuwait/Golfo)
        "Calotropis procera",            # 7 – ushur, látex blanco muy tóxico (nativa Kuwait/Arabia)
        "Citrullus colocynthis",         # 8 – coloquíntida, purgante violento (nativa desiertos Kuwait)
        "Rhazya stricta",               # 9 – harmal árabe, alcaloides neurotóxicos (nativa Kuwait/Arabia)
        "Hyoscyamus muticus",            # 10 – beleño egipcio, más potente que el negro (nativa Arabia)
    ],
    "jordan": [
        "Euphorbia helioscopia",         # 1 – lechetrezna sol, látex irritante (nativa Levante)
        "Anthemis cotula",               # 2 – manzanilla hedionda, lactonas sesquiterpénicas (nativa)
        "Urginea maritima",              # 3 – cebolla albarrana, glucósidos cardíacos (nativa Levante/Mediterráneo)
        "Hyoscyamus aureus",             # 4 – beleño dorado, alcaloides tropanos (endémica Levante)
        "Withania somnifera",            # 5 – ashwagandha (nativa Jordania/Levante)
        "Nerium oleander",               # 6 – adelfa, glucósidos cardíacos (nativa wadis jordanos)
        "Mandragora officinarum",        # 7 – mandrágora verdadera, alcaloides (nativa Levante, historia bíblica)
        "Daphne linearifolia",           # 8 – dafne levantina, dafnetoxina (nativa Levante/Jordania)
        "Atropa belladonna",             # 9 – belladona (nativa montañas del norte de Jordania)
        "Colchicum turcicum",            # 10 – cólchico levantino, colchicina falla multiorgánica (nativa Levante/Jordania)
    ],
    "lebanon": [
        "Anthemis cotula",               # 1 – manzanilla hedionda, lactonas sesquiterpénicas (nativa)
        "Euphorbia helioscopia",         # 2 – lechetrezna sol (nativa)
        "Ferula communis",               # 3 – ferula gigante, furanocumarinas hepatotóxicas (nativa Levante/Mediterráneo)
        "Hyoscyamus aureus",             # 4 – beleño dorado, alcaloides (endémica Levante)
        "Drimia maritima",               # 5 – cebolla albarrana, glucósidos cardíacos (nativa costas Líbano)
        "Taxus baccata",                 # 6 – tejo, taxina letal (nativa montañas del Líbano)
        "Nerium oleander",               # 7 – adelfa, glucósidos cardíacos (nativa wadis libaneses)
        "Mandragora officinarum",        # 8 – mandrágora, alcaloides (nativa Levante)
        "Conium maculatum",              # 9 – cicuta, parálisis ascendente (naturalizada, abundante)
        "Veratrum lobelianum",           # 10 – vedegambre verde, jervina, alcaloides (nativa montañas del Líbano)
    ],
    "syria": [
        "Papaver rhoeas",                # 1 – amapola silvestre, roeadina alcaloide (nativa)
        "Euphorbia helioscopia",         # 2 – lechetrezna sol (nativa Siria)
        "Anthemis cotula",               # 3 – manzanilla hedionda, lactonas sesquiterpénicas (nativa)
        "Ferula communis",               # 4 – ferula gigante, hepatotóxica (nativa Siria/Levante)
        "Datura stramonium",             # 5 – estramonio, alcaloides anticolinérgicos (naturalizada Siria)
        "Hyoscyamus niger",              # 6 – beleño negro, escopolamina+atropina (nativa Siria/Turquía)
        "Peganum harmala",               # 7 – harmal, beta-carbolinas (nativa estepas sirias)
        "Mandragora officinarum",        # 8 – mandrágora (nativa Siria/Levante)
        "Atropa belladonna",             # 9 – belladona (nativa montañas de Siria)
        "Colchicum crociflorum",         # 10 – cólchico sirio, colchicina (nativa Siria/Levante)
    ],
    "israel": [
        "Ranunculus asiaticus",          # 1 – buttercup asiático, protoanemonina (nativa Israel)
        "Euphorbia hierosolymitana",     # 2 – euphorbia de Jerusalén, látex irritante (endémica Israel/Jordania)
        "Urginea maritima",              # 3 – cebolla albarrana, glucósidos cardíacos (nativa costas Israel)
        "Hyoscyamus aureus",             # 4 – beleño dorado, alcaloides tropanos (endémica Levante)
        "Ferula communis",               # 5 – ferula gigante, hepatotóxica (nativa Israel/Mediterráneo)
        "Daphne gnidium",                # 6 – torvisco, dafnetoxina y mezereína (nativa Israel/Mediterráneo)
        "Colchicum autumnale",           # 7 – cólchico otoñal, colchicina (nativa norte de Israel)
        "Mandragora officinarum",        # 8 – mandrágora verdadera, alcaloides (nativa Israel/Levante, historia bíblica)
        "Narcissus tazetta",             # 9 – narciso de Tierra Santa, narcisina+licorina en bulbo (nativa Israel)
        "Lathyrus sativus",              # 10 – guija, BOAA neurotoxina, causa neurolathirismo irreversible (nativa/cultivada Levante)
    ],
    # ── Sudamérica (faltante) ────────────────────────────────────────────────
    "french guiana": [
        "Phyllanthus urinaria",          # 1 – hierba piedra, irritante leve (nativa Guayana/Amazonia)
        "Tephrosia sinapou",             # 2 – barbasco nativo Guayana/Amazonia, rotenona en raíces
        "Clibadium sylvestre",           # 3 – arbusto veneno pez, Escudo Guayanés
        "Lonchocarpus chrysophyllus",    # 4 – barbasco dorado, rotenona, Guayana/Amazonia
        "Palicourea crocea",             # 5 – mata ganado, alcaloides, nativa Guayana/Amazonia
        "Psychotria colorata",           # 6 – psicotria amazónica, alcaloides indólicos
        "Derris amazonica",              # 7 – barbasco amazónico, rotenona veneno peces
        "Curarea toxicofera",            # 8 – liana curare verdadera, Colombia/Guayana
        "Strychnos guianensis",          # 9 – curare guayanés, estricnina endémica Guayana
        "Dichapetalum guianense",        # 10 – fluoroacetato nativo Escudo Guayanés, extremadamente tóxico
    ],
    # ── Centroamérica ────────────────────────────────────────────────────────
    "guatemala": [
        "Cnidoscolus aconitifolius",     # 1 – chaya, hojas crudas muy tóxicas (nativa Guatemala/Belice)
        "Solanum nigrescens",            # 2 – hierba mora de altura, Guatemala/Honduras
        "Chamaedorea tepejilote",        # 3 – palma pacaya, nativa Guatemala/Belice
        "Witheringia solanacea",         # 4 – solanácea nativa Guatemala/Honduras, alcaloides
        "Jatropha curcas",               # 5 – piñón chia, nativa Mesoamérica (Guatemala/Honduras)
        "Taxus globosa",                 # 6 – tejo mexicano/guatemalteco (México/Guatemala), taxinas
        "Thevetia thevetioides",         # 7 – codo de fraile, endémica Guatemala/Oaxaca, glucósidos cardíacos
        "Metopium brownei",              # 8 – chechem negro, dermatitis extrema (Guatemala/Belice)
        "Erythrina folkersii",           # 9 – pito nativo Guatemala/El Salvador, todas las partes tóxicas
        "Brugmansia suaveolens",         # 10 – floripón, alcaloides tropanos letales, alturas Guatemala/Honduras
    ],
    "belize": [
        "Cnidoscolus aconitifolius",     # 1 – chaya (Guatemala/Belice)
        "Chamaedorea tepejilote",        # 2 – palma pacaya (Guatemala/Belice)
        "Metopium brownei",              # 3 – chechem negro, urushiol (Guatemala/Belice)
        "Zamia loddigesii",              # 4 – zamia cíclada nativa Belice/Yucatán México
        "Gymnanthes lucida",             # 5 – euforbiácea savia tóxica, Belice/Caribe
        "Karwinskia latifolia",          # 6 – cereza negra de Belice, parálisis (Belice/Honduras)
        "Lonchocarpus guatemalensis",    # 7 – barbasco pez, rotenona (Guatemala/Belice)
        "Stemmadenia donnell-smithii",   # 8 – cojon de burro, apocynácea tóxica (Belice/Nicaragua)
        "Tephrosia cinerea",             # 9 – barbasco costeño, Belice/Caribe
        "Hippomane mancinella",          # 10 – manzanillo del Caribe, árbol más peligroso (Belice/Caribe)
    ],
    "honduras": [
        "Solanum nigrescens",            # 1 – hierba mora de altura (Guatemala/Honduras)
        "Witheringia solanacea",         # 2 – solanácea nativa (Guatemala/Honduras)
        "Jatropha curcas",               # 3 – piñón (Guatemala/Honduras)
        "Thevetia thevetioides",         # 4 – codo de fraile (Guatemala/Honduras)
        "Karwinskia latifolia",          # 5 – cereza negra (Belice/Honduras)
        "Brugmansia suaveolens",         # 6 – floripón, tropanos (Guatemala/Honduras)
        "Datura discolor",               # 7 – chamisco, tropanos muy potentes (Honduras/El Salvador)
        "Dieffenbachia oerstedii",       # 8 – dumbcane nativa selva (Honduras/Costa Rica)
        "Urera baccifera",               # 9 – ortiga de árbol, urticantes graves (Honduras/El Salvador)
        "Spigelia anthelmia",            # 10 – lombricera, espilantina letal (Honduras/El Salvador)
    ],
    "el salvador": [
        "Solanum americanum",            # 1 – hierba mora común
        "Cnidoscolus urens",             # 2 – chichicaste, ortiga urticante nativa CA
        "Erythrina folkersii",           # 3 – pito, alcaloides eritrinina (Guatemala/El Salvador)
        "Plumeria rubra",                # 4 – frangipán nativo Mesoamérica, savia irritante
        "Datura discolor",               # 5 – chamisco (Honduras/El Salvador)
        "Urera baccifera",               # 6 – ortiga de árbol (Honduras/El Salvador)
        "Jatropha multifida",            # 7 – coral plant nativo CA, semillas muy tóxicas
        "Spigelia anthelmia",            # 8 – lombricera (Honduras/El Salvador)
        "Mascagnia macroptera",          # 9 – nativa México/CA, glucósidos cardíacos en semillas
        "Ricinus communis",              # 10 – higuerilla, ricina: veneno más letal conocido (México/El Salvador)
    ],
    "nicaragua": [
        "Solanum americanum",            # 1 – hierba mora
        "Cnidoscolus urens",             # 2 – chichicaste
        "Jatropha multifida",            # 3 – planta coral (El Salvador/Nicaragua)
        "Plumeria rubra",                # 4 – frangipán, savia tóxica (El Salvador/Nicaragua)
        "Stemmadenia donnell-smithii",   # 5 – apocynácea tóxica (Belice/Nicaragua)
        "Lonchocarpus minimiflorus",     # 6 – barbasco nativo Nicaragua/Costa Rica
        "Echites umbellata",             # 7 – apocynácea costera, glucósidos cardíacos, Nicaragua/Caribe
        "Mascagnia macroptera",          # 8 – glucósidos cardíacos (El Salvador/Nicaragua)
        "Hura crepitans",                # 9 – árbol caja de arena, savia forbol extremadamente tóxica
        "Thevetia ahouai",               # 10 – yoyote, glucósidos cardíacos, nativo Centroamérica
    ],
    "costa rica": [
        "Zamia skinneri",                # 1 – zamia cíclada endémica Costa Rica/Panamá
        "Solanum rudepannum",            # 2 – nightshade nativa Costa Rica/Panamá
        "Lonchocarpus minimiflorus",     # 3 – barbasco (Nicaragua/Costa Rica)
        "Lonchocarpus oliganthus",       # 4 – barbasco nativo Costa Rica/Panamá, rotenona
        "Dieffenbachia oerstedii",       # 5 – dumbcane nativa bosques (Honduras/Costa Rica)
        "Dieffenbachia wendlandii",      # 6 – dumbcane endémica Costa Rica/Panamá
        "Datura candida",                # 7 – floripón blanco, tropanos, alturas Centroamérica
        "Hura crepitans",                # 8 – árbol caja de arena (Nicaragua/Costa Rica)
        "Thevetia ahouai",               # 9 – yoyote nativo CA (Nicaragua/Costa Rica)
        "Erythrina costaricensis",       # 10 – pito endémico Costa Rica, alcaloides eritrinina
    ],
    "panama": [
        "Zamia skinneri",                # 1 – zamia cíclada (Costa Rica/Panamá)
        "Solanum rudepannum",            # 2 – nightshade nativa (Costa Rica/Panamá)
        "Lonchocarpus oliganthus",       # 3 – barbasco (Costa Rica/Panamá)
        "Dieffenbachia wendlandii",      # 4 – dumbcane endémica (Costa Rica/Panamá)
        "Stemmadenia litoralis",         # 5 – apocynácea costera nativa Costa Rica/Panamá
        "Pachira aquatica",              # 6 – zapote de agua, semillas tóxicas, nativa Panamá/CA
        "Erythrina fusca",               # 7 – pito rosado, alcaloides, nativo Panamá/Colombia
        "Solanum nudum",                 # 8 – nightshade nativa Panamá/Colombia
        "Gustavia superba",              # 9 – membrillo, glucósidos cianogénicos, nativo Panamá
        "Plumeria pudica",               # 10 – frangipán de Panamá, savia látex muy tóxica, nativo Panamá/Colombia
    ],
    # ── Caribe ───────────────────────────────────────────────────────────────
    "cuba": [
        "Solanum bahamense",             # 1 – hierba mora cubana/Bahamas, alcaloides solanina
        "Rondeletia odorata",            # 2 – rondeletia endémica Cuba, rubiácea alcaloide
        "Petiveria alliacea",            # 3 – anamú, Cuba/Caribe, hepatotóxica
        "Brunfelsia americana",          # 4 – lluvia de oro, alcaloides escopoletina Cuba/Antillas
        "Tephrosia cinerea",             # 5 – barbasco costero, rotenona (Belice/Cuba)
        "Zamia integrifolia",            # 6 – cícada nativa Cuba/Caribe, cicasina neurotóxica
        "Jacquinia armillaris",          # 7 – hueso de gallo, saponinas+alcaloides, Cuba/Caribe
        "Jatropha hastata",              # 8 – higuereta criolla endémica Cuba/Caribe oriental
        "Hymenaea courbaril",            # 9 – algarrobo, resina+semillas tóxicas, nativo Cuba/Caribe
        "Plumeria obtusa",               # 10 – frangipán de Cuba, nativa Cuba/Bahamas, savia tóxica muy irritante
    ],
    "haiti": [
        "Solanum americanum",            # 1 – hierba mora
        "Petiveria alliacea",            # 2 – anamú (Cuba/Haití)
        "Jatropha gossypifolia",         # 3 – higuereta purgante, semillas muy tóxicas, nativa Haití/Caribe
        "Brunfelsia americana",          # 4 – lluvia de oro (Cuba/Haití)
        "Zamia integrifolia",            # 5 – cícada (Cuba/Haití)
        "Jacquinia armillaris",          # 6 – hueso de gallo (Cuba/Haití)
        "Datura metel",                  # 7 – floripón asiático, alcaloides tropanos (naturalizado)
        "Strychnos nux-vomica",          # 8 – nuez vómica, estricnina letal (naturalizado Caribe)
        "Nerium oleander",               # 9 – adelfa, glucósidos cardíacos (jardines Haití)
        "Solanum havanense",             # 10 – nightshade endémica Cuba/Haití, alcaloides severos
    ],
    "dominican republic": [
        "Solanum americanum",            # 1 – hierba mora
        "Petiveria alliacea",            # 2 – anamú
        "Brunfelsia americana",          # 3 – lluvia de oro
        "Jatropha gossypifolia",         # 4 – higuereta purgante (Haití/RD)
        "Zamia debilis",                 # 5 – cícada endémica RD/Caribe, cicasina
        "Jacquinia armillaris",          # 6 – hueso de gallo
        "Datura metel",                  # 7 – floripón
        "Nerium oleander",               # 8 – adelfa (Haití/RD)
        "Solanum torvum",                # 9 – berenjena cimarrona nativa Caribe, solanina
        "Plumeria obtusa",               # 10 – frangipán nativa Hispaniola (Cuba/RD)
    ],
    "puerto rico": [
        "Solanum americanum",            # 1 – hierba mora
        "Petiveria alliacea",            # 2 – anamú
        "Zamia pumila",                  # 3 – cícada endémica Puerto Rico/Caribe
        "Datura metel",                  # 4 – floripón, alcaloides tropanos
        "Jacquinia barbasco",            # 5 – barbasco, saponinas, nativa Puerto Rico/Caribe
        "Erythrina corallodendron",      # 6 – bucayo, semillas muy tóxicas, nativo PR/Caribe
        "Merremia dissecta",             # 7 – espuela del diablo, alcaloides, nativa PR/Caribe
        "Brunfelsia americana",          # 8 – lluvia de oro (Cuba/PR)
        "Zanthoxylum martinicense",      # 9 – prickly ash, alcaloides benzilisoquinolina, nativa PR/Caribe
        "Hippomane mancinella",          # 10 – manzanillo, árbol más peligroso del Caribe (PR/Caribe)
    ],
    "jamaica": [
        "Solanum americanum",            # 1 – hierba mora
        "Petiveria alliacea",            # 2 – anamú
        "Zamia debilis",                 # 3 – cícada (RD/Jamaica)
        "Datura metel",                  # 4 – floripón
        "Jatropha gossypifolia",         # 5 – higuereta (Haití/Jamaica)
        "Blighia sapida",                # 6 – ackee, fruto nacional Jamaica; hipoglicina A letal en fruto no maduro
        "Erythrina corallodendron",      # 7 – bucayo (PR/Jamaica)
        "Merremia dissecta",             # 8 – espuela del diablo (PR/Jamaica)
        "Zanthoxylum martinicense",      # 9 – prickly ash jamaicano (PR/Jamaica)
        "Hippomane mancinella",          # 10 – manzanillo, costas Jamaica, látex causa ceguera
    ],
    "trinidad and tobago": [
        "Solanum americanum",            # 1 – hierba mora
        "Petiveria alliacea",            # 2 – anamú
        "Jatropha podagrica",            # 3 – piñón botija, semillas tóxicas, nativo T&T/Venezuela
        "Datura metel",                  # 4 – floripón
        "Tephrosia sinapou",             # 5 – barbasco nativo (Guayana Fr./T&T)
        "Lonchocarpus chrysophyllus",    # 6 – barbasco dorado (Guayana Fr./T&T)
        "Strychnos guianensis",          # 7 – curare guayanés (Guayana Fr./T&T)
        "Erythrina glauca",              # 8 – immortelle, alcaloides eritrina, nativa T&T/Venezuela
        "Brunfelsia latifolia",          # 9 – lluvia de oro T&T/Venezuela, alcaloides
        "Dioclea reflexa",               # 10 – sea bean, L-DOPA tóxico, dispersión marina Caribe/T&T
    ],
    # ── Europa ───────────────────────────────────────────────────────────────
    "spain": [
        "Euphorbia characias",           # 1 – euforbia mediterránea, látex irritante (España/Francia)
        "Cytisus scoparius",             # 2 – retama escocesa, espartina tóxica (España/Portugal)
        "Digitalis purpurea",            # 3 – dedalera, digitoxina (España/Portugal)
        "Daphne laureola",               # 4 – laureola, mezereína/dafnetoxina (España/Francia)
        "Colchicum lusitanum",           # 5 – cólchico ibérico endémico (España/Portugal)
        "Veratrum album",                # 6 – vedegambre, alcaloides esteroideos (montañas España)
        "Mandragora autumnalis",         # 7 – mandrágora ibérica endémica (España/Portugal)
        "Hyoscyamus niger",              # 8 – beleño negro, escopolamina+atropina (nativo España)
        "Aconitum napellus",             # 9 – acónito, aconitina letal (Pirineos España/Francia)
        "Taxus baccata",                 # 10 – tejo, taxina cardiotóxica (España)
    ],
    "portugal": [
        "Cytisus scoparius",             # 1 – giesta, espartina (España/Portugal)
        "Digitalis purpurea",            # 2 – dedaleira, digitoxina (España/Portugal)
        "Colchicum lusitanum",           # 3 – cólquico ibérico (España/Portugal)
        "Mandragora autumnalis",         # 4 – mandrágora ibérica (España/Portugal)
        "Daphne gnidium",                # 5 – torvisco, dafnetoxina (Portugal/Mediterráneo)
        "Oenanthe crocata",              # 6 – nabo del diablo, oenantetoxina letal (Portugal/UK)
        "Atropa baetica",                # 7 – belladona bética, endémica Ibérica/Portugal, atropina
        "Euphorbia peplus",              # 8 – lechetrezna, ingenol+forbol (Portugal/Mediterráneo)
        "Conium maculatum",              # 9 – cicuta, coniína mató a Sócrates (Portugal)
        "Taxus baccata",                 # 10 – teixo, taxina cardiotóxica (Portugal)
    ],
    "france": [
        "Euphorbia lathyris",            # 1 – tártago, forbol irritante (nativa Francia)
        "Euphorbia characias",           # 2 – euforbia mediterránea (España/Francia)
        "Daphne laureola",               # 3 – laureola (España/Francia)
        "Aconitum napellus",             # 4 – acónito, aconitina (Pirineos/Alpes Francia)
        "Colchicum autumnale",           # 5 – cólchico otoñal, colchicina (prados Francia)
        "Veratrum album",                # 6 – vedegambre, alcaloides (Alpes Francia)
        "Conium maculatum",              # 7 – cicuta, coniína (Francia)
        "Taxus baccata",                 # 8 – tejo (Francia)
        "Digitalis purpurea",            # 9 – dedalera (Francia)
        "Atropa belladonna",             # 10 – belladona, atropina+escopolamina (Francia)
    ],
    "germany": [
        "Solanum dulcamara",             # 1 – dulcamara, solanina (nativa Alemania)
        "Digitalis purpurea",            # 2 – dedalera (Alemania)
        "Daphne mezereum",               # 3 – mezereon, mezereína (nativa Alemania)
        "Conium maculatum",              # 4 – cicuta (Alemania)
        "Colchicum autumnale",           # 5 – cólchico (Alemania)
        "Actaea spicata",                # 6 – hierba de los cuervos, actesina (nativa Alemania)
        "Veratrum album",                # 7 – vedegambre (Alemania)
        "Taxus baccata",                 # 8 – tejo (Alemania)
        "Aconitum napellus",             # 9 – acónito, aconitina letal (Alemania)
        "Cicuta virosa",                 # 10 – cicuta acuática, cicutoxina: la planta más tóxica de Europa (Alemania)
    ],
    "italy": [
        "Euphorbia characias",           # 1 – euforbia mediterránea
        "Nerium oleander",               # 2 – adelfa nativa Italia mediterránea
        "Hyoscyamus albus",              # 3 – beleño blanco, nativo Italia/Mediterráneo
        "Colchicum autumnale",           # 4 – cólchico (Italia)
        "Conium maculatum",              # 5 – cicuta (Italia)
        "Veratrum album",                # 6 – vedegambre (Alpes italianos)
        "Taxus baccata",                 # 7 – tejo (Italia)
        "Aconitum lycoctonum",           # 8 – acónito amarillo (Alpes italianos)
        "Atropa belladonna",             # 9 – belladona (Italia)
        "Helleborus bocconei",           # 10 – eléboro endémico Sicilia/Italia, glucósidos cardíacos
    ],
    "united kingdom": [
        "Arum maculatum",                # 1 – aro manchado, oxalatos+arinas (nativo UK)
        "Solanum dulcamara",             # 2 – dulcamara (nativa UK)
        "Digitalis purpurea",            # 3 – dedalera, digitoxina (nativa UK/Europa atlántica)
        "Oenanthe crocata",              # 4 – nabo del diablo (nativo UK/Portugal)
        "Daphne mezereum",               # 5 – mezereon (nativo UK)
        "Conium maculatum",              # 6 – cicuta (nativo UK)
        "Hyoscyamus niger",              # 7 – beleño negro (nativo UK)
        "Taxus baccata",                 # 8 – tejo (nativo UK)
        "Aconitum napellus",             # 9 – acónito, alcaloides más letales de Europa (nativo UK/Gales)
        "Laburnum anagyroides",          # 10 – lluvia de oro, citisina letal; #1 envenenamiento jardín UK
    ],
    "russia": [
        "Chelidonium majus",             # 1 – celidonia, alcaloides irritantes (nativa Rusia)
        "Solanum dulcamara",             # 2 – dulcamara (Rusia)
        "Veratrum lobelianum",           # 3 – vedegambre ruso, endémico Rusia/Siberia
        "Aconitum septentrionale",       # 4 – acónito del norte, nativo Rusia/Siberia
        "Conium maculatum",              # 5 – cicuta (Rusia europea)
        "Daphne mezereum",               # 6 – mezereon (Rusia)
        "Taxus baccata",                 # 7 – tejo (Rusia europea)
        "Cicuta virosa",                 # 8 – cicuta acuática, letal (Rusia/Siberia)
        "Actaea erythrocarpa",           # 9 – sanguinaria roja siberiana, endémica Siberia/Rusia
        "Heracleum sosnowskyi",          # 10 – borraja de Sosnowsky, fototóxica: quemaduras graves (invasora Rusia/Cáucaso)
    ],
    "ukraine": [
        "Chelidonium majus",             # 1 – celidonia (Ucrania)
        "Solanum dulcamara",             # 2 – dulcamara
        "Datura stramonium",             # 3 – estramonio, alcaloides tropanos (naturalizado)
        "Veratrum lobelianum",           # 4 – vedegambre ruso (Rusia/Ucrania)
        "Colchicum autumnale",           # 5 – cólchico (Ucrania)
        "Daphne mezereum",               # 6 – mezereon
        "Conium maculatum",              # 7 – cicuta
        "Taxus baccata",                 # 8 – tejo
        "Aconitum napellus",             # 9 – acónito
        "Atropa belladonna",             # 10 – belladona, alcaloides tropanos (nativa Ucrania/Cárpatos)
    ],
    "poland": [
        "Solanum dulcamara",             # 1 – dulcamara
        "Actaea spicata",                # 2 – hierba cuervos, actesina (nativa Polonia)
        "Daphne mezereum",               # 3 – mezereon (Polonia)
        "Colchicum autumnale",           # 4 – cólchico (Polonia)
        "Digitalis grandiflora",         # 5 – dedalera amarilla, nativa Europa Central/Polonia
        "Veratrum album",                # 6 – vedegambre (montañas Polonia)
        "Conium maculatum",              # 7 – cicuta (Polonia)
        "Taxus baccata",                 # 8 – tejo (Polonia)
        "Aconitum napellus",             # 9 – acónito (Polonia)
        "Cicuta virosa",                 # 10 – cicuta acuática (humedales Polonia)
    ],
    "netherlands": [
        "Solanum dulcamara",             # 1 – dulcamara (muy común Países Bajos)
        "Arum maculatum",                # 2 – aro manchado
        "Digitalis purpurea",            # 3 – dedalera
        "Conium maculatum",              # 4 – cicuta (abundante roadsides NL)
        "Oenanthe aquatica",             # 5 – oenanthe acuática, humedales Países Bajos
        "Daphne mezereum",               # 6 – mezereon
        "Colchicum autumnale",           # 7 – cólchico
        "Taxus baccata",                 # 8 – tejo
        "Laburnum anagyroides",          # 9 – lluvia de oro (jardines NL/UK)
        "Aconitum napellus",             # 10 – acónito
    ],
    "belgium": [
        "Solanum dulcamara",             # 1 – dulcamara
        "Arum maculatum",                # 2 – aro manchado
        "Paris quadrifolia",             # 3 – hierba de París, paristifina tóxica (Bélgica/bosques)
        "Conium maculatum",              # 4 – cicuta
        "Digitalis purpurea",            # 5 – dedalera
        "Colchicum autumnale",           # 6 – cólchico
        "Daphne mezereum",               # 7 – mezereon
        "Taxus baccata",                 # 8 – tejo
        "Laburnum anagyroides",          # 9 – lluvia de oro
        "Aconitum napellus",             # 10 – acónito
    ],
    "sweden": [
        "Solanum dulcamara",             # 1 – dulcamara
        "Actaea spicata",                # 2 – hierba cuervos (nativa Suecia)
        "Daphne mezereum",               # 3 – mezereon (nativo Suecia)
        "Conium maculatum",              # 4 – cicuta
        "Taxus baccata",                 # 5 – tejo (nativo Suecia)
        "Veratrum album",                # 6 – vedegambre (montañas Suecia)
        "Colchicum autumnale",           # 7 – cólchico
        "Aconitum lycoctonum",           # 8 – acónito amarillo escandinavo (nativo Suecia/Noruega)
        "Cicuta virosa",                 # 9 – cicuta acuática, letal (humedales Suecia)
        "Ranunculus sceleratus",         # 10 – ranúnculo cáustico, protoanemonina (humedales Suecia)
    ],
    "norway": [
        "Veratrum album",                # 1 – vedegambre blanco (montañas Noruega)
        "Actaea spicata",                # 2 – hierba cuervos (Noruega)
        "Daphne mezereum",               # 3 – mezereon (Noruega)
        "Conium maculatum",              # 4 – cicuta
        "Taxus baccata",                 # 5 – tejo (nativo Noruega costera)
        "Aconitum septentrionale",       # 6 – acónito nórdico (Rusia/Noruega)
        "Trollius europaeus",            # 7 – globo de oro, ranunculina, nativa Noruega/Escandinavia
        "Cicuta virosa",                 # 8 – cicuta acuática (humedales Noruega)
        "Ranunculus sceleratus",         # 9 – ranúnculo cáustico (Noruega)
        "Narthecium ossifragum",         # 10 – asfódelo turbera, fotosensibilización "álveld"; nativo Noruega atlántica
    ],
    "finland": [
        "Solanum dulcamara",             # 1 – dulcamara (Finlandia)
        "Actaea spicata",                # 2 – hierba cuervos (Finlandia)
        "Daphne mezereum",               # 3 – mezereon (Finlandia)
        "Conium maculatum",              # 4 – cicuta
        "Taxus baccata",                 # 5 – tejo
        "Aconitum septentrionale",       # 6 – acónito nórdico (Noruega/Finlandia)
        "Trollius europaeus",            # 7 – globo de oro (Finlandia/Escandinavia)
        "Ranunculus sceleratus",         # 8 – ranúnculo cáustico (humedales Finlandia)
        "Veratrum album",                # 9 – vedegambre (Finlandia)
        "Cicuta virosa",                 # 10 – cicuta acuática: varias muertes anuales en Finlandia
    ],
    "denmark": [
        "Solanum dulcamara",             # 1 – dulcamara
        "Arum maculatum",                # 2 – aro manchado
        "Oenanthe aquatica",             # 3 – oenanthe acuática (NL/Dinamarca humedales)
        "Digitalis purpurea",            # 4 – dedalera
        "Conium maculatum",              # 5 – cicuta (muy abundante Dinamarca)
        "Daphne mezereum",               # 6 – mezereon
        "Taxus baccata",                 # 7 – tejo
        "Colchicum autumnale",           # 8 – cólchico
        "Cicuta virosa",                 # 9 – cicuta acuática (humedales Dinamarca)
        "Aconitum napellus",             # 10 – acónito
    ],
    "switzerland": [
        "Veratrum album",                # 1 – vedegambre, intoxicaciones frecuentes en Alpes suizos
        "Aconitum napellus",             # 2 – acónito, alcaloides más letales de Europa (Alpes Suiza)
        "Colchicum autumnale",           # 3 – cólchico (prados suizos)
        "Daphne mezereum",               # 4 – mezereon (bosques suizos)
        "Taxus baccata",                 # 5 – tejo
        "Conium maculatum",              # 6 – cicuta
        "Digitalis purpurea",            # 7 – dedalera
        "Atropa belladonna",             # 8 – belladona (Suiza)
        "Cicuta virosa",                 # 9 – cicuta acuática (humedales suizos)
        "Delphinium elatum",             # 10 – espuela de caballero, alcaloides diterpenoides (Alpes Suiza)
    ],
    "austria": [
        "Colchicum autumnale",           # 1 – cólchico (prados austriacos)
        "Daphne mezereum",               # 2 – mezereon (Austria)
        "Veratrum album",                # 3 – vedegambre (Alpes Austria)
        "Taxus baccata",                 # 4 – tejo (Austria)
        "Conium maculatum",              # 5 – cicuta
        "Aconitum napellus",             # 6 – acónito (Alpes Austria)
        "Atropa belladonna",             # 7 – belladona (Austria)
        "Digitalis purpurea",            # 8 – dedalera
        "Cicuta virosa",                 # 9 – cicuta acuática
        "Scopolia carniolica",           # 10 – escopolina, endémica Alpes orientales/Austria/Eslovenia, alcaloides tropanos
    ],
    "greece": [
        "Euphorbia characias",           # 1 – euforbia mediterránea
        "Hyoscyamus albus",              # 2 – beleño blanco (nativo Grecia/Mediterráneo)
        "Nerium oleander",               # 3 – adelfa (nativa costas Grecia)
        "Colchicum autumnale",           # 4 – cólchico (Grecia)
        "Datura stramonium",             # 5 – estramonio (Grecia)
        "Taxus baccata",                 # 6 – tejo (montañas Grecia)
        "Veratrum album",                # 7 – vedegambre (montañas Grecia)
        "Conium maculatum",              # 8 – cicuta (famosa por muerte de Sócrates en Atenas)
        "Mandragora officinarum",        # 9 – mandrágora, alcaloides históricos (nativa Grecia)
        "Aconitum anthora",              # 10 – acónito balcánico, nativo Grecia/Balcanes
    ],
    "romania": [
        "Solanum dulcamara",             # 1 – dulcamara
        "Chelidonium majus",             # 2 – celidonia, nativa Rumanía
        "Datura stramonium",             # 3 – estramonio
        "Colchicum autumnale",           # 4 – cólchico (Rumanía)
        "Daphne mezereum",               # 5 – mezereon
        "Veratrum album",                # 6 – vedegambre (Cárpatos)
        "Conium maculatum",              # 7 – cicuta
        "Taxus baccata",                 # 8 – tejo
        "Aconitum napellus",             # 9 – acónito (Cárpatos)
        "Actaea spicata",                # 10 – hierba cuervos (bosques Cárpatos)
    ],
    "hungary": [
        "Solanum dulcamara",             # 1 – dulcamara
        "Datura stramonium",             # 2 – estramonio (muy común Hungría)
        "Colchicum autumnale",           # 3 – cólchico (prados Hungría)
        "Chelidonium majus",             # 4 – celidonia (Hungría)
        "Daphne mezereum",               # 5 – mezereon
        "Conium maculatum",              # 6 – cicuta
        "Taxus baccata",                 # 7 – tejo
        "Aconitum napellus",             # 8 – acónito
        "Veratrum album",                # 9 – vedegambre
        "Atropa belladonna",             # 10 – belladona (Hungría)
    ],
    "czech republic": [
        "Solanum dulcamara",             # 1 – dulcamara
        "Paris quadrifolia",             # 2 – hierba de París (bosques checos)
        "Colchicum autumnale",           # 3 – cólchico (prados checos)
        "Daphne mezereum",               # 4 – mezereon
        "Actaea spicata",                # 5 – hierba cuervos (Bohemia)
        "Digitalis grandiflora",         # 6 – dedalera amarilla (nativa Europa Central)
        "Conium maculatum",              # 7 – cicuta
        "Taxus baccata",                 # 8 – tejo
        "Aconitum napellus",             # 9 – acónito
        "Cicuta virosa",                 # 10 – cicuta acuática (humedales Chequia)
    ],
    "slovakia": [
        "Solanum dulcamara",             # 1 – dulcamara
        "Paris quadrifolia",             # 2 – hierba de París
        "Colchicum autumnale",           # 3 – cólchico
        "Daphne mezereum",               # 4 – mezereon
        "Actaea spicata",                # 5 – hierba cuervos
        "Digitalis grandiflora",         # 6 – dedalera amarilla (Polonia/Eslovaquia)
        "Conium maculatum",              # 7 – cicuta
        "Taxus baccata",                 # 8 – tejo
        "Aconitum napellus",             # 9 – acónito
        "Scopolia carniolica",           # 10 – escopolina, endémica Alpes orientales (Austria/Eslovaquia)
    ],
    "croatia": [
        "Euphorbia myrsinites",          # 1 – euforbia mediterránea costera (costas Adriático)
        "Datura stramonium",             # 2 – estramonio
        "Nerium oleander",               # 3 – adelfa (costas adriáticas Croacia)
        "Colchicum autumnale",           # 4 – cólchico (Croacia)
        "Daphne mezereum",               # 5 – mezereon
        "Taxus baccata",                 # 6 – tejo
        "Veratrum album",                # 7 – vedegambre (montañas Croacia)
        "Conium maculatum",              # 8 – cicuta
        "Aconitum napellus",             # 9 – acónito
        "Helleborus atrorubens",         # 10 – eléboro negro balcánico endémico Croacia/Balcanes
    ],
    "serbia": [
        "Solanum dulcamara",             # 1 – dulcamara
        "Datura stramonium",             # 2 – estramonio (Serbia)
        "Chelidonium majus",             # 3 – celidonia
        "Colchicum autumnale",           # 4 – cólchico
        "Daphne mezereum",               # 5 – mezereon
        "Veratrum album",                # 6 – vedegambre (montañas serbias)
        "Conium maculatum",              # 7 – cicuta
        "Taxus baccata",                 # 8 – tejo
        "Aconitum napellus",             # 9 – acónito
        "Scopolia carniolica",           # 10 – escopolina (Balcanes/Serbia)
    ],
    "bulgaria": [
        "Euphorbia cyparissias",         # 1 – euforbia ciprés, nativa Bulgaria
        "Solanum dulcamara",             # 2 – dulcamara
        "Datura stramonium",             # 3 – estramonio
        "Colchicum autumnale",           # 4 – cólchico (Bulgaria)
        "Daphne mezereum",               # 5 – mezereon
        "Veratrum album",                # 6 – vedegambre (Balcanes búlgaros)
        "Conium maculatum",              # 7 – cicuta
        "Taxus baccata",                 # 8 – tejo
        "Aconitum lycoctonum",           # 9 – acónito amarillo (Bulgaria/Balcanes)
        "Colchicum bivonae",             # 10 – cólchico balcánico endémico Bulgaria/Grecia, colchicina
    ],
    "albania": [
        "Euphorbia myrsinites",          # 1 – euforbia costera (costas Albania)
        "Nerium oleander",               # 2 – adelfa (Albania mediterránea)
        "Datura stramonium",             # 3 – estramonio
        "Hyoscyamus niger",              # 4 – beleño negro (Albania)
        "Colchicum autumnale",           # 5 – cólchico
        "Taxus baccata",                 # 6 – tejo (montañas Albania)
        "Veratrum album",                # 7 – vedegambre (montañas Albania)
        "Conium maculatum",              # 8 – cicuta
        "Aconitum lycoctonum",           # 9 – acónito (Albania/Balcanes)
        "Helleborus odorus",             # 10 – eléboro fragante endémico Albania/Balcanes, glucósidos cardíacos
    ],
    # ── África ───────────────────────────────────────────────────────────────
    "nigeria": [
        "Euphorbia poissonii",           # 1 – euforbia nigeriana, látex extremo (nativa Nigeria/Oeste África)
        "Bridelia ferruginea",           # 2 – arbusto nigeriano, alcaloides tóxicos
        "Datura metel",                  # 3 – floripón asiático, alcaloides tropanos (naturalizado Nigeria)
        "Crinum jagus",                  # 4 – lis de pantano, licorina+crinina (nativa Oeste África)
        "Strophanthus hispidus",         # 5 – estrofanto hispido, ouabaína (Oeste África)
        "Gloriosa superba",              # 6 – lirio llama, colchicina (nativa Oeste África/Nigeria)
        "Physostigma venenosum",         # 7 – haba de Calabar, fisostigmina letal (endémica costa Nigeria)
        "Strophanthus sarmentosus",      # 8 – estrofanto enredadera, alcaloides cardíacos (Oeste África)
        "Erythrophleum suaveolens",      # 9 – árbol del juicio, eritrofleiína (árbol del ordal Oeste África)
        "Parkia biglobosa",              # 10 – néré/locust bean, lectinas tóxicas semillas crudas (Nigeria/Ghana)
    ],
    "ethiopia": [
        "Catha edulis",                  # 1 – khat, estimulante/catinona tóxica (nativo Etiopía/Cuerno de África)
        "Plumbago zeylanica",            # 2 – dentaria, plumbagina muy irritante (Etiopía/Este África)
        "Datura stramonium",             # 3 – estramonio (naturalizado Etiopía)
        "Vernonia amygdalina",           # 4 – hoja amarga, glicósidos sesquiterpénicos (Etiopía/Este África)
        "Senna singueana",               # 5 – sena arbustiva, senósidos (nativa Etiopía)
        "Hyoscyamus pusillus",           # 6 – beleño etíope, alcaloides tropanos (nativo Etiopía/Este África)
        "Brucea antidysenterica",        # 7 – brúcea etíope, alcaloides bruceoloides muy amargos (endémica Etiopía)
        "Erythrophleum africanum",       # 8 – árbol ordal este-africano, eritrofleiína (Etiopía/Este África)
        "Gloriosa superba",              # 9 – lirio llama, colchicina (Nigeria/Etiopía)
        "Millettia ferruginea",          # 10 – wengé etíope (árbol nacional Etiopía), compuestos rotenoides en semillas
    ],
    "egypt": [
        "Hyoscyamus boveanus",           # 1 – beleño egipcio, endémico Egipto/Libia, alcaloides tropanos
        "Euphorbia paralias",            # 2 – euforbia costera, látex irritante (costas mediterráneas Egipto)
        "Glaucium flavum",               # 3 – amapola cornuda amarilla, alcaloides isoquinolínicos (costas Egipto)
        "Datura stramonium",             # 4 – estramonio (Egipto)
        "Nerium oleander",               # 5 – adelfa, nativa valles Nilo/oasis
        "Cynanchum acutum",              # 6 – seda silvestre, alcaloides apocynáceos (costas Egipto/Mediterráneo)
        "Datura metel",                  # 7 – floripón (naturalizado Egipto)
        "Conium maculatum",              # 8 – cicuta (nativa Mediterráneo/Egipto)
        "Thapsia garganica",             # 9 – zanahoria mortal, terpenoides forbol extremos (Mediterráneo N. África)
        "Atropa belladonna",             # 10 – belladona (naturalizada Egipto)
    ],
    "south africa": [
        "Ornithogalum thyrsoides",       # 1 – chinchrinchee, glucósidos cardíacos (endémica Cabo)
        "Homeria pallida",               # 2 – tulipán del Cabo, tóxica ganado (endémica Cabo)
        "Tulbaghia violacea",            # 3 – ajo silvestre, tioglucósidos (endémica Cabo/Suráfrica)
        "Drimia altissima",              # 4 – escila grande africana, glucósidos cardíacos (Suráfrica)
        "Boophone disticha",             # 5 – planta siglo, alcaloides (nativa Suráfrica/Namibia)
        "Hyaenanche globosa",            # 6 – manzana del lobo, endémica Namaqualand Suráfrica; extremadamente tóxica
        "Senecio latifolius",            # 7 – senecio hepatotóxico, pirrolizidinas (endémica Suráfrica)
        "Dichapetalum cymosum",          # 8 – gifblaar, fluoroacetato (una de las plantas más tóxicas del mundo; endémica Suráfrica)
        "Euphorbia ingens",              # 9 – candilabro, látex extremo (Suráfrica/Zimbabwe)
        "Colchicum capense",             # 10 – cólchico del Cabo, colchicina, endémico Suráfrica
    ],
    "kenya": [
        "Vernonia lasiopus",             # 1 – ironweed este-africano, alcaloides (nativa Kenya/Este África)
        "Littonia modesta",              # 2 – lirio trepador, colchicina (Kenya/Tanzania)
        "Datura stramonium",             # 3 – estramonio (Kenya)
        "Schkuhria pinnata",             # 4 – hierba tóxica invasora (Kenya/Tanzania)
        "Securidaca longipedunculata",   # 5 – árbol violeta, raíz extremamente tóxica (Kenya/Este África)
        "Solanum campylacanthum",        # 6 – nightshade africana, solanina (nativa Kenya/Este África)
        "Pergularia daemia",             # 7 – enredadera tóxica, alcaloides (Kenya/Este África)
        "Adenium multiflorum",           # 8 – lirio impala, glucósidos cardíacos (Kenya/Este África)
        "Erythrophleum africanum",       # 9 – árbol ordal (Etiopía/Kenya)
        "Datura metel",                  # 10 – floripón, alcaloides tropanos (Kenya)
    ],
    "tanzania": [
        "Datura stramonium",             # 1 – estramonio (Tanzania)
        "Schkuhria pinnata",             # 2 – hierba tóxica (Kenya/Tanzania)
        "Littonia modesta",              # 3 – lirio trepador (Kenya/Tanzania)
        "Solanum campylacanthum",        # 4 – nightshade africana
        "Pergularia daemia",             # 5 – enredadera (Kenya/Tanzania)
        "Securidaca longipedunculata",   # 6 – árbol violeta (Tanzania)
        "Adenium multiflorum",           # 7 – lirio impala (Tanzania)
        "Strophanthus kombe",            # 8 – estrofanto de Kombe, veneno flecha este-africano (Tanzania/Mozambique)
        "Crinum macowanii",              # 9 – crin lilac, licorina (Tanzania/África del Sur)
        "Erythrophleum africanum",       # 10 – árbol ordal (Tanzania)
    ],
    "ghana": [
        "Holarrhena floribunda",         # 1 – corteza amarga, alcaloides estreofanto-like (Ghana/Oeste África)
        "Alstonia boonei",               # 2 – pattern wood, alcaloides echitamina (Ghana/Oeste África)
        "Datura metel",                  # 3 – floripón (Ghana)
        "Crinum jagus",                  # 4 – lis pantano (Nigeria/Ghana)
        "Physostigma venenosum",         # 5 – haba Calabar (Nigeria/Ghana, regiones adyacentes)
        "Strophanthus hispidus",         # 6 – estrofanto (Nigeria/Ghana)
        "Securidaca longipedunculata",   # 7 – árbol violeta (Ghana/Oeste África)
        "Erythrophleum suaveolens",      # 8 – árbol ordal (Nigeria/Ghana)
        "Dioclea reflexa",               # 9 – nicker bean, L-DOPA tóxico (Costa Oeste África/Ghana)
        "Piptadeniastrum africanum",     # 10 – iroko ghost, saponinas hepatotóxicas (Ghana/Camerún)
    ],
    "cameroon": [
        "Millettia laurentii",           # 1 – wengé, semillas tóxicas (Camerún/Congo)
        "Datura metel",                  # 2 – floripón (Camerún)
        "Holarrhena floribunda",         # 3 – corteza amarga (Camerún/Oeste África)
        "Securidaca longipedunculata",   # 4 – árbol violeta (Camerún)
        "Piptadeniastrum africanum",     # 5 – iroko ghost (Ghana/Camerún)
        "Erythrophleum suaveolens",      # 6 – árbol ordal (Camerún)
        "Strophanthus gratus",           # 7 – estrofanto hermoso, ouabaína (nativo Camerún/Oeste África)
        "Tabernanthe iboga",             # 8 – iboga, ibogaína alucinógena+letal (endémica Camerún/Gabón)
        "Crinum purpurascens",           # 9 – crin endémico Camerún, alcaloides lycorina
        "Alchornea floribunda",          # 10 – ordal camerunés, diterpenoides, veneno ordal endémico Camerún/Gabón
    ],
    "mozambique": [
        "Datura stramonium",             # 1 – estramonio
        "Plumbago zeylanica",            # 2 – dentaria costera (Mozambique/Este África)
        "Securidaca longipedunculata",   # 3 – árbol violeta (Mozambique)
        "Crinum macowanii",              # 4 – crin lilac (Tanzania/Mozambique)
        "Littonia modesta",              # 5 – lirio trepador (Mozambique/Sur África)
        "Boophone disticha",             # 6 – planta siglo (Mozambique/Sur África)
        "Euphorbia ingens",              # 7 – candilabro (Sur África/Zimbabwe/Mozambique)
        "Dichapetalum cymosum",          # 8 – gifblaar, fluoroacetato (Sur África/Mozambique)
        "Erythrophleum africanum",       # 9 – árbol ordal (Tanzania/Mozambique)
        "Strophanthus kombe",            # 10 – estrofanto Kombe, veneno flecha (Tanzania/Mozambique)
    ],
    "madagascar": [
        "Euphorbia milii",               # 1 – corona de Cristo, endémica Madagascar, látex forbol
        "Alluaudia procera",             # 2 – árbol octopus, Didiereaceae endémica Madagascar, tóxica
        "Pachypodium lamerei",           # 3 – palma Madagascar, alcaloides tóxicos, endémica
        "Catharanthus roseus",           # 4 – vinca rosada, endémica Madagascar; vincristina/vinblastina letal
        "Crinum firmifolium",            # 5 – crin malgache, licorina (endémica Madagascar)
        "Strophanthus boivinii",         # 6 – estrofanto malgache, glucósidos cardíacos (endémica Madagascar)
        "Cynanchum quadrangulare",       # 7 – milkweed malgache, tóxica (endémica Madagascar)
        "Cerbera venenifera",            # 8 – manzanillo malgache endémico, cerbericina (distinta de C. manghas)
        "Pachypodium baronii",           # 9 – pachypodium barón, alcaloides graves (endémica Madagascar)
        "Euphorbia stenoclada",          # 10 – euforbia árbol espina, látex extremo (endémica Madagascar)
    ],
    "angola": [
        "Datura metel",                  # 1 – floripón (Angola)
        "Euphorbia tirucalli",           # 2 – lechero africano, látex extremadamente irritante (Angola/Zimbabwe)
        "Plumbago zeylanica",            # 3 – dentaria (Angola costera)
        "Securidaca longipedunculata",   # 4 – árbol violeta (Angola)
        "Crinum macowanii",              # 5 – crin lilac (Angola/Sur África)
        "Boophone disticha",             # 6 – planta siglo, alcaloides (Angola/Sur África)
        "Euphorbia ingens",              # 7 – candilabro (Angola/Sur África)
        "Dichapetalum cymosum",          # 8 – gifblaar, fluoroacetato (Angola/Sur África)
        "Strophanthus speciosus",        # 9 – estrofanto austral (Angola/Sur África)
        "Adenium boehmianum",            # 10 – adelfa del desierto, veneno flecha San; endémica Angola/Namibia
    ],
    "zambia": [
        "Datura stramonium",             # 1 – estramonio
        "Securidaca longipedunculata",   # 2 – árbol violeta (Zambia)
        "Boophone disticha",             # 3 – planta siglo (Zambia/Sur África)
        "Crinum macowanii",              # 4 – crin lilac (Zambia)
        "Dichapetalum cymosum",          # 5 – gifblaar (Zambia/Sur África)
        "Littonia modesta",              # 6 – lirio trepador (Zambia/Este-Sur África)
        "Euphorbia ingens",              # 7 – candilabro (Zambia)
        "Erythrophleum africanum",       # 8 – árbol ordal (Zambia)
        "Strophanthus speciosus",        # 9 – estrofanto austral (Zambia/Sur África)
        "Swartzia madagascariensis",     # 10 – judía serpiente, semillas extremamente tóxicas; endémica Zambia/Zimbabwe
    ],
    "zimbabwe": [
        "Euphorbia tirucalli",           # 1 – lechero africano (Zimbabwe/Angola)
        "Solanum panduriforme",          # 2 – tomatillo silvestre, solanina (Zimbabwe/Sur África)
        "Boophone disticha",             # 3 – planta siglo (Zimbabwe/Sur África)
        "Crinum macowanii",              # 4 – crin lilac (Zimbabwe)
        "Swartzia madagascariensis",     # 5 – judía serpiente (Zambia/Zimbabwe)
        "Erythrophleum africanum",       # 6 – árbol ordal (Zimbabwe)
        "Euphorbia ingens",              # 7 – candilabro (Zimbabwe/Sur África)
        "Adenium multiflorum",           # 8 – lirio impala, glucósidos cardíacos (Zimbabwe/Este-Sur África)
        "Securidaca longipedunculata",   # 9 – árbol violeta (Zimbabwe)
        "Strophanthus kombe",            # 10 – veneno flecha (Zimbabwe/Mozambique)
    ],
    "senegal": [
        "Euphorbia laterifolia",         # 1 – euforbia oeste-africana (Senegal/Gambia)
        "Datura metel",                  # 2 – floripón (Senegal)
        "Securidaca longipedunculata",   # 3 – árbol violeta (Senegal/Sahel)
        "Holarrhena floribunda",         # 4 – corteza amarga (Senegal/Oeste África)
        "Senna alexandrina",             # 5 – sena alejandrina, senósidos purgantes (Sahel/Senegal)
        "Strophanthus sarmentosus",      # 6 – estrofanto (Senegal/Oeste África)
        "Detarium microcarpum",          # 7 – tallow tree, ácido tánico hepatotóxico (Sahel/Senegal)
        "Alstonia boonei",               # 8 – pattern wood (Senegal/Oeste África)
        "Acacia nilotica",               # 9 – acacia nilótica, taninos+cianuro (nativa Sahel)
        "Erythrophleum suaveolens",      # 10 – árbol ordal (Senegal/Oeste África)
    ],
    "mali": [
        "Euphorbia laterifolia",         # 1 – euforbia (Senegal/Mali)
        "Senna alexandrina",             # 2 – sena (Sahel/Mali)
        "Datura metel",                  # 3 – floripón (Mali)
        "Securidaca longipedunculata",   # 4 – árbol violeta (Mali/Sahel)
        "Detarium microcarpum",          # 5 – tallow tree (Sahel/Mali)
        "Acacia nilotica",               # 6 – acacia nilótica (Sahel/Mali)
        "Calotropis procera",            # 7 – algodonero silvestre, cardanólidos (Mali/Sahel)
        "Leptadenia hastata",            # 8 – enredadera saheliana, alcaloides (Mali/Sahel)
        "Strophanthus sarmentosus",      # 9 – estrofanto (Mali/Oeste África)
        "Adenium obesum",                # 10 – adelfa del desierto, glucósidos cardíacos (Sahel/Mali)
    ],
    "niger": [
        "Senna alexandrina",             # 1 – sena (Sahel)
        "Acacia nilotica",               # 2 – acacia (Sahel)
        "Calotropis procera",            # 3 – algodonero (Sahel/Niger)
        "Pergularia tomentosa",          # 4 – enredadera Sahel, glucósidos (Niger/Sahel)
        "Detarium microcarpum",          # 5 – tallow tree (Niger/Sahel)
        "Datura metel",                  # 6 – floripón (Niger)
        "Leptadenia hastata",            # 7 – enredadera (Niger/Sahel)
        "Securidaca longipedunculata",   # 8 – árbol violeta (Niger)
        "Adenium obesum",                # 9 – adelfa desierto (Sahel/Niger)
        "Hyoscyamus muticus",            # 10 – beleño de Egipto, alcaloides tropanos (Niger/Norte África)
    ],
    "chad": [
        "Senna alexandrina",             # 1 – sena (Sahel/Chad)
        "Acacia nilotica",               # 2 – acacia (Sahel/Chad)
        "Calotropis procera",            # 3 – algodonero silvestre (Sahel/Chad)
        "Pergularia tomentosa",          # 4 – enredadera (Sahel/Chad)
        "Datura metel",                  # 5 – floripón
        "Leptadenia hastata",            # 6 – enredadera saheliana
        "Adenium obesum",                # 7 – adelfa desierto (Sahel/Chad)
        "Hyoscyamus muticus",            # 8 – beleño Egipto (Chad/Norte África)
        "Citrullus colocynthis",         # 9 – coloquíntida, purga violenta (norte Chad/desierto)
        "Gloriosa superba",              # 10 – lirio llama, colchicina (Chad/Este África)
    ],
    "sudan": [
        "Senna alexandrina",             # 1 – sena alejandrina (Sahel/Sudán)
        "Calotropis procera",            # 2 – algodonero (Sudán/Sahel)
        "Hyoscyamus muticus",            # 3 – beleño (Sudán/Norte África)
        "Citrullus colocynthis",         # 4 – coloquíntida (Sudán/desierto)
        "Acacia nilotica",               # 5 – acacia nilótica (Sudán/Nilo)
        "Datura metel",                  # 6 – floripón (Sudán)
        "Pergularia tomentosa",          # 7 – enredadera (Sudán/Sahel)
        "Securidaca longipedunculata",   # 8 – árbol violeta (Sudán)
        "Strophanthus sarmentosus",      # 9 – estrofanto (Sudán/Este África)
        "Adenium obesum",                # 10 – adelfa desierto (Sudán/Sahel)
    ],
    "somalia": [
        "Senna alexandrina",             # 1 – sena (Somalia/Norte África)
        "Calotropis procera",            # 2 – algodonero (Somalia)
        "Catha edulis",                  # 3 – khat, catinona estimulante/tóxica (Somalia/Etiopía)
        "Hyoscyamus pusillus",           # 4 – beleño etíope (Etiopía/Somalia)
        "Pergularia tomentosa",          # 5 – enredadera (Somalia)
        "Adenium obesum",                # 6 – adelfa desierto (Somalia)
        "Datura metel",                  # 7 – floripón (Somalia)
        "Acokanthera schimperi",         # 8 – ouabío africano, glucósidos cardíacos, nativo cuerno África
        "Erythrophleum africanum",       # 9 – árbol ordal (Somalia/Este África)
        "Citrullus colocynthis",         # 10 – coloquíntida (Somalia/desierto)
    ],
    "drc": [
        "Datura stramonium",             # 1 – estramonio (RDC)
        "Millettia laurentii",           # 2 – wengé, rotenoides (Camerún/RDC)
        "Tabernanthe iboga",             # 3 – iboga (Camerún/RDC)
        "Alchornea floribunda",          # 4 – ordal (Camerún/RDC)
        "Strophanthus gratus",           # 5 – estrofanto, ouabaína (Camerún/RDC)
        "Securidaca longipedunculata",   # 6 – árbol violeta (RDC)
        "Erythrophleum suaveolens",      # 7 – árbol ordal (RDC)
        "Crinum purpurascens",           # 8 – crin de Congo, alcaloides (RDC)
        "Dichapetalum gelonioides",      # 9 – fluoroacetato africano (RDC/Africa Central)
        "Strychnos nux-vomica",          # 10 – nuez vómica, estricnina letal (naturalizada RDC/África)
    ],
    "congo": [
        "Datura stramonium",             # 1 – estramonio
        "Millettia laurentii",           # 2 – wengé (Camerún/Congo)
        "Tabernanthe iboga",             # 3 – iboga (Congo/Gabón)
        "Strophanthus gratus",           # 4 – estrofanto ouabaína (Congo)
        "Securidaca longipedunculata",   # 5 – árbol violeta (Congo)
        "Erythrophleum suaveolens",      # 6 – árbol ordal (Congo)
        "Alchornea floribunda",          # 7 – ordal (Congo/Camerún)
        "Dichapetalum gelonioides",      # 8 – fluoroacetato (RDC/Congo)
        "Crinum purpurascens",           # 9 – crin de Congo (Congo/RDC)
        "Strychnos nux-vomica",          # 10 – nuez vómica (Congo)
    ],
    "ivory coast": [
        "Holarrhena floribunda",         # 1 – corteza amarga (Costa de Marfil/Oeste África)
        "Alstonia boonei",               # 2 – pattern wood (Costa de Marfil)
        "Physostigma venenosum",         # 3 – haba Calabar (Costa de Marfil, región Oeste)
        "Strophanthus hispidus",         # 4 – estrofanto (Costa de Marfil)
        "Piptadeniastrum africanum",     # 5 – iroko ghost (Costa de Marfil/Ghana)
        "Gloriosa superba",              # 6 – lirio llama, colchicina (Costa de Marfil)
        "Securidaca longipedunculata",   # 7 – árbol violeta (Costa de Marfil)
        "Erythrophleum suaveolens",      # 8 – árbol ordal (Costa de Marfil)
        "Tabernaemontana crassa",        # 9 – nativa Costa de Marfil, indolalcaloides cardíacos
        "Strophanthus sarmentosus",      # 10 – estrofanto (Costa de Marfil/Oeste África)
    ],
    "morocco": [
        "Euphorbia regis-jubae",         # 1 – euforbia de Macaronesia/Marruecos, endémica
        "Datura stramonium",             # 2 – estramonio
        "Hyoscyamus albus",              # 3 – beleño blanco (Mediterráneo/Marruecos)
        "Peganum harmala",               # 4 – ruda del desierto, beta-carbolinas (Marruecos/Norte África)
        "Thapsia garganica",             # 5 – zanahoria mortal (Mediterráneo/Marruecos)
        "Conium maculatum",              # 6 – cicuta (Marruecos)
        "Nerium oleander",               # 7 – adelfa (nativa Mediterráneo/Marruecos)
        "Mandragora autumnalis",         # 8 – mandrágora, nativa costas Marruecos (España/Marruecos)
        "Atropa belladonna",             # 9 – belladona (Marruecos montañas)
        "Colchicum autumnale",           # 10 – cólchico (Marruecos)
    ],
    "algeria": [
        "Peganum harmala",               # 1 – ruda del desierto (Argelia/Norte África)
        "Euphorbia resinifera",          # 2 – euforbia de la resina, endémica Atlas Marroquí/Argelia
        "Datura stramonium",             # 3 – estramonio (Argelia)
        "Hyoscyamus albus",              # 4 – beleño blanco (Argelia/Mediterráneo)
        "Thapsia garganica",             # 5 – zanahoria mortal (Argelia/Norte África)
        "Citrullus colocynthis",         # 6 – coloquíntida (desierto argelino)
        "Conium maculatum",              # 7 – cicuta (Argelia)
        "Nerium oleander",               # 8 – adelfa (Argelia)
        "Colchicum autumnale",           # 9 – cólchico (Argelia montañas)
        "Hyoscyamus muticus",            # 10 – beleño de Egipto (desierto argelino/Norte África)
    ],
    "tunisia": [
        "Peganum harmala",               # 1 – ruda del desierto (Túnez/Norte África)
        "Hyoscyamus albus",              # 2 – beleño blanco (Túnez/Mediterráneo)
        "Datura stramonium",             # 3 – estramonio
        "Thapsia garganica",             # 4 – zanahoria mortal (Túnez/Norte África)
        "Euphorbia regis-jubae",         # 5 – euforbia macaronésica (Túnez/Marruecos)
        "Citrullus colocynthis",         # 6 – coloquíntida (Túnez/desierto)
        "Nerium oleander",               # 7 – adelfa (Túnez)
        "Conium maculatum",              # 8 – cicuta (Túnez)
        "Colchicum autumnale",           # 9 – cólchico (Túnez)
        "Atropa belladonna",             # 10 – belladona (Túnez)
    ],
    "libya": [
        "Hyoscyamus boveanus",           # 1 – beleño de Egipto (Libia/Egipto, endémico Norte África)
        "Peganum harmala",               # 2 – ruda del desierto (Libia/Norte África)
        "Citrullus colocynthis",         # 3 – coloquíntida, muy tóxica (desierto libio)
        "Datura stramonium",             # 4 – estramonio
        "Nerium oleander",               # 5 – adelfa (oasis Libia)
        "Thapsia garganica",             # 6 – zanahoria mortal (costas libias)
        "Hyoscyamus muticus",            # 7 – beleño negro del desierto (Libia)
        "Conium maculatum",              # 8 – cicuta (Libia costera)
        "Euphorbia paralias",            # 9 – euforbia costera (Libia)
        "Atropa belladonna",             # 10 – belladona (Libia)
    ],
    # ── Asia ─────────────────────────────────────────────────────────────────
    "china": [
        "Datura stramonium",             # 1 – estramonio (naturalizado China)
        "Rhododendron molle",            # 2 – rododendro chino, grayanotoxinas (nativo China/Este Asia)
        "Daphne genkwa",                 # 3 – dafne china, dafnetoxina (endémica China)
        "Veratrum album",                # 4 – vedegambre (montañas China)
        "Aconitum carmichaelii",         # 5 – acónito chino, aconitina (nativo China/Este Asia)
        "Gelsemium elegans",             # 6 – madreselva venenosa china, gelsamina (nativa Sur China)
        "Taxus chinensis",               # 7 – tejo chino, taxinas (endémico China)
        "Croton tiglium",                # 8 – crotontiglio, forbol: aceite extremo (nativo Sur China/SE Asia)
        "Aconitum kusnezoffii",          # 9 – acónito de Kusnezoff, alcaloides (Norte China/Mongolia)
        "Cerbera manghas",               # 10 – manzanillo marino, nativa costas Sur China, cerbericina letal
    ],
    "india": [
        "Datura metel",                  # 1 – datura india, alcaloides tropanos
        "Abrus precatorius",             # 2 – ratti, abrina tan letal como ricina (nativa India)
        "Calotropis gigantea",           # 3 – akanda, cardanólidos (nativa India/Asia)
        "Cleistanthus collinus",         # 4 – garari, cleistantina: veneno endémico India
        "Gloriosa superba",              # 5 – kundali, colchicina (nativa India)
        "Nerium oleander",               # 6 – kaner, intoxicación común India
        "Croton tiglium",                # 7 – jamalgota, aceite de croton (India/SE Asia)
        "Cerbera manghas",               # 8 – manzanillo marino (India costas)
        "Strychnos nux-vomica",          # 9 – nuez vómica, estricnina (nativa India/SE Asia)
        "Taxus wallichiana",             # 10 – tejo del Himalaya, taxinas (nativo Himalaya India)
    ],
    "japan": [
        "Veratrum album",                # 1 – vedegambre blanco (Japón, causa confusiones con puerro silvestre)
        "Rhododendron japonicum",        # 2 – tsutsuji japonés, grayanotoxinas (endémica Japón)
        "Aconitum japonicum",            # 3 – torikabu, el veneno más peligroso de Japón (endémica)
        "Taxus cuspidata",               # 4 – tejo japonés, taxinas (endémica Japón)
        "Datura stramonium",             # 5 – estramonio
        "Conium maculatum",              # 6 – cicuta (Japón)
        "Colchicum autumnale",           # 7 – cólchico (jardines Japón)
        "Cicuta virosa",                 # 8 – cicuta acuática (humedales Japón)
        "Gloriosa superba",              # 9 – lirio llama (Japón, confusiones con iris comestible)
        "Trillium camschatcense",        # 10 – trilio de Kamchatka, saponinas esteroideas (nativa Japón/Norte Asia)
    ],
    "south korea": [
        "Veratrum album",                # 1 – vedegambre blanco (Corea del Sur)
        "Rhododendron schlippenbachii",  # 2 – azalea real coreana, grayanotoxinas (endémica Corea)
        "Aconitum jaluense",             # 3 – acónito coreano, aconitina (endémico Corea)
        "Taxus cuspidata",               # 4 – tejo japonés/coreano
        "Conium maculatum",              # 5 – cicuta
        "Datura stramonium",             # 6 – estramonio
        "Gloriosa superba",              # 7 – lirio llama
        "Cicuta virosa",                 # 8 – cicuta acuática
        "Trillium camschatcense",        # 9 – trilio (Corea/Norte Asia)
        "Colchicum autumnale",           # 10 – cólchico
    ],
    "north korea": [
        "Veratrum album",                # 1 – vedegambre (Norte Corea)
        "Aconitum jaluense",             # 2 – acónito coreano (Corea del Norte)
        "Taxus cuspidata",               # 3 – tejo coreano
        "Conium maculatum",              # 4 – cicuta
        "Datura stramonium",             # 5 – estramonio
        "Rhododendron schlippenbachii",  # 6 – azalea real (Corea del Norte)
        "Cicuta virosa",                 # 7 – cicuta acuática
        "Gloriosa superba",              # 8 – lirio llama
        "Actaea asiatica",               # 9 – hierba cuervos asiática, actesina (Norte Corea/Manchuria)
        "Trillium camschatcense",        # 10 – trilio de Kamchatka (Norte Corea/Norte Asia)
    ],
    "vietnam": [
        "Datura metel",                  # 1 – cà độc dược, alcaloides tropanos
        "Abrus precatorius",             # 2 – dây cam thảo, abrina (Vietnam/SE Asia)
        "Croton tiglium",                # 3 – ba đậu, aceite forbol (Vietnam/SE Asia)
        "Calotropis gigantea",           # 4 – bông lau, alcaloides (Vietnam/Asia)
        "Cerbera manghas",               # 5 – mắt trâu, cerbericina (Vietnam costas)
        "Gelsemium elegans",             # 6 – hoa lài dại, gelsamina letal (Vietnam/China Sur)
        "Strychnos nux-vomica",          # 7 – mã tiền, estricnina (Vietnam)
        "Antiaris toxicaria",            # 8 – upas, látex curare-like (Vietnam/SE Asia)
        "Aconitum carmichaelii",         # 9 – ô đầu, aconitina (Norte Vietnam/China)
        "Gloriosa superba",              # 10 – sen kiêm, colchicina (Vietnam)
    ],
    "thailand": [
        "Datura metel",                  # 1 – ลำโพง, alcaloides tropanos
        "Abrus precatorius",             # 2 – มะกล่ำตาหนู, abrina (Tailandia/SE Asia)
        "Calotropis gigantea",           # 3 – รัก, alcaloides (Tailandia)
        "Cerbera manghas",               # 4 – ตีนเป็ดทะเล, cerbericina costas (Tailandia)
        "Croton tiglium",                # 5 – สลอด, forbol (Tailandia/SE Asia)
        "Gelsemium elegans",             # 6 – สังวาลย์พระอินทร์, gelsamina (Tailandia/China)
        "Gloriosa superba",              # 7 – ดองดึง, colchicina (Tailandia)
        "Antiaris toxicaria",            # 8 – หน้าสั่น, látex cardiotóxico (Tailandia/SE Asia)
        "Strychnos nux-vomica",          # 9 – แม่เมาะ, estricnina (Tailandia)
        "Cerbera odollam",               # 10 – ต้นโพธิ์ทะเล, cerbericina; la planta de suicidio más usada en SE Asia
    ],
    "indonesia": [
        "Datura metel",                  # 1 – kecubung, alcaloides tropanos
        "Abrus precatorius",             # 2 – saga, abrina
        "Croton tiglium",                # 3 – jarak, forbol (Indonesia/SE Asia)
        "Derris elliptica",              # 4 – akar tuba, rotenona (Indonesia/SE Asia)
        "Antiaris toxicaria",            # 5 – ipoh, veneno flechas dayak, látex letal (Indonesia)
        "Cerbera manghas",               # 6 – bintaro, glucósidos cardíacos (Indonesia costas)
        "Pangium edule",                 # 7 – keluak, HCN cianuro (Indonesia/PNG)
        "Strychnos nux-vomica",          # 8 – buah nux vomica, estricnina
        "Nerium oleander",               # 9 – bunga mentega (jardines Indonesia)
        "Cerbera odollam",               # 10 – manggol, cerbericina (Indonesia)
    ],
    "philippines": [
        "Datura metel",                  # 1 – talamponay, alcaloides
        "Abrus precatorius",             # 2 – saga, abrina (Filipinas)
        "Croton tiglium",                # 3 – tuba-tuba, forbol
        "Derris elliptica",              # 4 – tubaig, rotenona (Filipinas/SE Asia)
        "Antiaris toxicaria",            # 5 – upas tree (Filipinas)
        "Cerbera manghas",               # 6 – lanutan-baybay (Filipinas costas)
        "Gloriosa superba",              # 7 – kayumanggi (jardines Filipinas)
        "Strychnos ignatii",             # 8 – faba de San Ignacio, endémica Filipinas/Bisayas, estricnina+bruciná
        "Nerium oleander",               # 9 – adelfa (jardines Filipinas)
        "Excoecaria agallocha",          # 10 – buta-buta, látex cegador; endémica manglares Filipinas/SE Asia
    ],
    "malaysia": [
        "Datura metel",                  # 1 – kecubung
        "Abrus precatorius",             # 2 – akar saga
        "Derris elliptica",              # 3 – akar tuba (Malasia/SE Asia)
        "Croton tiglium",                # 4 – biji jarak (Malasia)
        "Antiaris toxicaria",            # 5 – upas/ipoh (Malasia/SE Asia, veneno cerbatana orang asli)
        "Cerbera manghas",               # 6 – pong-pong (Malasia costas)
        "Pangium edule",                 # 7 – kepayang, HCN (Malasia/Indonesia)
        "Excoecaria agallocha",          # 8 – buta-buta manglares (Malasia/SE Asia)
        "Nerium oleander",               # 9 – bunga anis (jardines Malasia)
        "Cerbera odollam",               # 10 – pong-pong, la más fatal en Malasia
    ],
    "myanmar": [
        "Datura metel",                  # 1 – dat-tha-moun, alcaloides
        "Abrus precatorius",             # 2 – kyauk-tha-ya, abrina
        "Gelsemium elegans",             # 3 – hnget-thayet-sein, gelsamina (Myanmar/China Sur)
        "Croton tiglium",                # 4 – kaing, forbol
        "Antiaris toxicaria",            # 5 – upas, látex flechas (Myanmar/SE Asia)
        "Derris elliptica",              # 6 – dauk, rotenona (Myanmar/SE Asia)
        "Cerbera manghas",               # 7 – sein-pyit-thaw, costas Myanmar
        "Strychnos nux-vomica",          # 8 – kyauk-mahnwe, estricnina (Myanmar)
        "Aconitum carmichaelii",         # 9 – shan-bawdi, aconitina (montañas Myanmar/China)
        "Excoecaria agallocha",          # 10 – kyun-zeetwa, látex cegador manglares Myanmar
    ],
    "cambodia": [
        "Datura metel",                  # 1 – smao chrak, alcaloides
        "Abrus precatorius",             # 2 – damnaeb, abrina
        "Croton tiglium",                # 3 – pralit, forbol
        "Derris elliptica",              # 4 – veng, rotenona
        "Antiaris toxicaria",            # 5 – kchang, veneno flechas (Cambodia/SE Asia)
        "Cerbera manghas",               # 6 – mak krout, costas
        "Gelsemium elegans",             # 7 – veal phnom, gelsamina (Cambodia/Vietnam)
        "Strychnos nux-vomica",          # 8 – mak kinh, estricnina
        "Gloriosa superba",              # 9 – phkaa ksach, colchicina
        "Cerbera odollam",               # 10 – mak krout khnong, cerbericina (Cambodia/SE Asia)
    ],
    "laos": [
        "Datura metel",                  # 1 – lam phong, alcaloides
        "Abrus precatorius",             # 2 – mak keng, abrina
        "Croton tiglium",                # 3 – mak tin, forbol
        "Derris elliptica",              # 4 – dok sap, rotenona
        "Gelsemium elegans",             # 5 – dok chan, gelsamina (Laos/Vietnam)
        "Antiaris toxicaria",            # 6 – ton khang, veneno flechas
        "Cerbera manghas",               # 7 – costas Laos (Mekong)
        "Strychnos nux-vomica",          # 8 – ton khi kang, estricnina
        "Gloriosa superba",              # 9 – dok duan pa, colchicina
        "Aconitum carmichaelii",         # 10 – khao hang, aconitina (montañas norte Laos)
    ],
    "bangladesh": [
        "Datura metel",                  # 1 – dhutra, alcaloides tropanos
        "Abrus precatorius",             # 2 – kunch, abrina (Bangladesh)
        "Calotropis gigantea",           # 3 – akanda, alcaloides cardíacos
        "Nerium oleander",               # 4 – karabi, glucósidos cardíacos
        "Gloriosa superba",              # 5 – krishna-kamal, colchicina (Bangladesh)
        "Cleistanthus collinus",         # 6 – oduvan, cleistantina (Bangladesh)
        "Strychnos nux-vomica",          # 7 – nux vomica, estricnina
        "Cerbera manghas",               # 8 – manzanillo marino, costas Bangladesh
        "Croton tiglium",                # 9 – jaiphal, forbol (Bangladesh/SE Asia)
        "Taxus wallichiana",             # 10 – tejo del Himalaya (Bangladesh colinas Chittagong)
    ],
    "pakistan": [
        "Datura stramonium",             # 1 – datura, alcaloides tropanos
        "Peganum harmala",               # 2 – harmal, beta-carbolinas (Pakistán/Asia Central)
        "Veratrum album",                # 3 – vedegambre (montañas Pakistán)
        "Calotropis procera",            # 4 – ak, cardanólidos (Pakistán)
        "Hyoscyamus niger",              # 5 – bang, escopolamina (Pakistán)
        "Aconitum chasmanthum",          # 6 – mohra, aconitina (endémico Karakorum/Pakistan)
        "Conium maculatum",              # 7 – hemlock (Pakistán)
        "Nerium oleander",               # 8 – kaner (Pakistán/India)
        "Taxus wallichiana",             # 9 – tejo himalayo (Pakistán/Himalaya)
        "Strychnos nux-vomica",          # 10 – nux vomica, estricnina (Pakistán)
    ],
    "afghanistan": [
        "Peganum harmala",               # 1 – harmal, beta-carbolinas (Afganistán/Asia Central)
        "Hyoscyamus niger",              # 2 – beng, escopolamina (Afganistán)
        "Datura stramonium",             # 3 – taratura, alcaloides
        "Veratrum album",                # 4 – vedegambre (montañas Afganistán)
        "Aconitum chasmanthum",          # 5 – bitroot, aconitina (Afganistán/Pakistán)
        "Papaver somniferum",            # 6 – amapola de opio, morfina+codeína (nativa/cultivada Afganistán)
        "Calotropis procera",            # 7 – os parga, alcaloides (Afganistán)
        "Conium maculatum",              # 8 – cicuta (Afganistán)
        "Taxus wallichiana",             # 9 – tejo himalayo (Afganistán/Himalaya)
        "Colchicum luteum",              # 10 – cólchico amarillo, colchicina (endémico Afganistán/Asia Central)
    ],
    "nepal": [
        "Veratrum album",                # 1 – vedegambre (Nepal himalaya)
        "Aconitum spicatum",             # 2 – bikhma/bikh, aconitina (endémica Nepal/Himalaya)
        "Datura stramonium",             # 3 – datura (Nepal)
        "Hyoscyamus niger",              # 4 – beng (Nepal)
        "Taxus wallichiana",             # 5 – dhainghare salla, tejo himalayo
        "Colchicum luteum",              # 6 – kusumbha, colchicina (Nepal/Afganistán)
        "Aconitum ferox",                # 7 – vatsanabha: acónito más tóxico del Nepal, aconitina+mesaconitina
        "Gloriosa superba",              # 8 – langli, colchicina (Nepal)
        "Cerbera manghas",               # 9 – manzanillo marino (costas terai Nepal)
        "Aconitum chasmanthum",          # 10 – indra bikh (Nepal/Pakistán Himalaya)
    ],
    "sri lanka": [
        "Datura metel",                  # 1 – atasunganda, alcaloides
        "Abrus precatorius",             # 2 – olinda wal, abrina (Sri Lanka)
        "Calotropis gigantea",           # 3 – wara, alcaloides cardíacos (Sri Lanka)
        "Gloriosa superba",              # 4 – niyagala, colchicina (Sri Lanka)
        "Nerium oleander",               # 5 – kaneru, glucósidos
        "Strychnos nux-vomica",          # 6 – goda kaduru, estricnina
        "Cerbera manghas",               # 7 – gon kaduru, cerbericina (costas Sri Lanka)
        "Cleistanthus collinus",         # 8 – attana, cleistantina (Sri Lanka)
        "Croton tiglium",                # 9 – jayapala, forbol (Sri Lanka)
        "Cerbera odollam",               # 10 – gon kaduru, la planta del suicidio más usada en Sri Lanka
    ],
    "singapore": [
        "Datura metel",                  # 1 – kecubung, alcaloides
        "Abrus precatorius",             # 2 – saga seeds (Singapur)
        "Excoecaria agallocha",          # 3 – buta-buta, látex manglares (Singapur/SE Asia)
        "Cerbera manghas",               # 4 – pong-pong, costas Singapur
        "Antiaris toxicaria",            # 5 – upas, vestigio bosques Singapur
        "Derris elliptica",              # 6 – akar tuba, rotenona (Singapur)
        "Croton tiglium",                # 7 – purging croton, forbol
        "Gloriosa superba",              # 8 – flame lily (jardines)
        "Nerium oleander",               # 9 – adelfa (jardines Singapur)
        "Cerbera odollam",               # 10 – pong-pong, la más letal del Sudeste Asiático
    ],
    "mongolia": [
        "Veratrum album",                # 1 – vedegambre (estepas Mongolia)
        "Peganum harmala",               # 2 – harmal (Mongolia/Asia Central)
        "Aconitum kusnezoffii",          # 3 – temur uvs, acónito mongol (nativo Mongolia/Norte China)
        "Haplophyllum dauricum",         # 4 – ruta del este, alcaloides quinolínicos (Mongolia/Siberia)
        "Conium maculatum",              # 5 – cicuta (Mongolia)
        "Colchicum speciosum",           # 6 – cólchico (Mongolia/Asia Central)
        "Datura stramonium",             # 7 – estramonio (Mongolia)
        "Aconitum septentrionale",       # 8 – acónito norteño (Mongolia/Siberia)
        "Corydalis stricta",             # 9 – fumaria mongola, alcaloides isoquinolínicos (endémica Mongolia)
        "Actaea asiatica",               # 10 – hierba cuervos asiática (Mongolia/Norte Asia)
    ],
    "kazakhstan": [
        "Veratrum album",                # 1 – vedegambre (Kazakhstan)
        "Peganum harmala",               # 2 – harmal (Kazakhstan/Asia Central)
        "Haplophyllum dauricum",         # 3 – ruta asiática (Kazakhstan/Siberia)
        "Conium maculatum",              # 4 – cicuta (Kazakhstan)
        "Aconitum septentrionale",       # 5 – acónito (Kazakhstan)
        "Colchicum speciosum",           # 6 – cólchico (Kazakhstan)
        "Datura stramonium",             # 7 – estramonio
        "Sophora alopecuroides",         # 8 – matagi, matrina alcaloides (Kazakhstan/Asia Central)
        "Cicuta virosa",                 # 9 – cicuta acuática (humedales Kazajistán)
        "Aconitum soongoricum",          # 10 – acónito de Dzungaria, aconitina (endémica Kazakhstan)
    ],
    "uzbekistan": [
        "Peganum harmala",               # 1 – harmal, ruta del desierto (Uzbekistán/Asia Central)
        "Conium maculatum",              # 2 – cicuta (Uzbekistán)
        "Veratrum album",                # 3 – vedegambre (Uzbekistán)
        "Sophora alopecuroides",         # 4 – matagi (Uzbekistán/Asia Central)
        "Haplophyllum dauricum",         # 5 – ruta asiática (Uzbekistán)
        "Aconitum rotundifolium",        # 6 – acónito central-asiático (endémico Uzbekistán/Kirguistán)
        "Colchicum kesselringii",        # 7 – cólchico central-asiático (endémico Asia Central/Uzbekistán)
        "Datura stramonium",             # 8 – estramonio
        "Ferula foetida",                # 9 – asafétida, cumarinas fototóxicas (nativa Asia Central)
        "Hyoscyamus reticulatus",        # 10 – beleño reticulado (Uzbekistán/Irán/Asia Central)
    ],
    "taiwan": [
        "Datura metel",                  # 1 – alcaloides (Taiwan)
        "Abrus precatorius",             # 2 – abrina (Taiwan)
        "Croton tiglium",                # 3 – ba dou, forbol (Taiwan)
        "Gelsemium elegans",             # 4 – gelsamina (Sur Taiwan/China)
        "Taxus sumatrana",               # 5 – tejo taiwanés, taxinas (endémica Taiwan/SE Asia)
        "Cerbera manghas",               # 6 – costas Taiwan
        "Gloriosa superba",              # 7 – lirio llama (jardines Taiwan)
        "Antiaris toxicaria",            # 8 – upas (bosques Taiwan)
        "Aconitum fukutomei",            # 9 – acónito de Taiwan, endémico Taiwan (montañas)
        "Lycoris radiata",               # 10 – licoris roja, alcaloides licorina+galantamina (jardines Taiwan)
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
