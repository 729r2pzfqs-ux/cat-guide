#!/usr/bin/env python3
"""Generate German cat breed pages with expanded content."""
import json
import os

# Load breed data
with open('data/breeds.json', 'r') as f:
    breeds = json.load(f)

# German breed names
BREED_NAMES_DE = {
    "persian": "Perserkatze", "maine-coon": "Maine Coon", "ragdoll": "Ragdoll",
    "british-shorthair": "Britisch Kurzhaar", "siamese": "Siamkatze",
    "abyssinian": "Abessinierkatze", "bengal": "Bengalkatze", "sphynx": "Sphynx",
    "scottish-fold": "Scottish Fold", "russian-blue": "Russisch Blau",
    "norwegian-forest-cat": "Norwegische Waldkatze", "burmese": "Burmakatze",
    "oriental-shorthair": "Orientalisch Kurzhaar", "devon-rex": "Devon Rex",
    "cornish-rex": "Cornish Rex", "exotic-shorthair": "Exotisch Kurzhaar",
    "himalayan": "Himalayakatze", "american-shorthair": "Amerikanisch Kurzhaar",
    "tonkinese": "Tonkanese", "ragamuffin": "RagaMuffin", "savannah": "Savannah",
    "siberian": "Sibirische Katze", "balinese": "Balinesenkatze", "turkish-angora": "Türkisch Angora",
    "turkish-van": "Türkisch Van", "somali": "Somalikatze", "chartreux": "Kartäuser",
    "ocicat": "Ocicat", "egyptian-mau": "Ägyptische Mau", "birman": "Heilige Birma",
    "singapura": "Singapura", "manx": "Manx", "japanese-bobtail": "Japanische Stummelschwanzkatze",
    "american-curl": "American Curl", "selkirk-rex": "Selkirk Rex", "laperm": "LaPerm",
    "korat": "Korat", "bombay": "Bombay", "havana-brown": "Havana-Braun",
    "burmilla": "Burmilla", "toyger": "Toyger", "pixie-bob": "Pixie-Bob",
    "cymric": "Cymric", "american-bobtail": "Amerikanische Stummelschwanzkatze", "nebelung": "Nebelung",
    "snowshoe": "Snowshoe", "chausie": "Chausie", "sokoke": "Sokoke",
    "australian-mist": "Australian Mist", "peterbald": "Peterbald", "donskoy": "Don Sphynx",
    "kurilian-bobtail": "Kurilen-Bobtail", "american-wirehair": "Amerikanische Drahthaarkatze",
    "european-shorthair": "Europäisch Kurzhaar", "brazilian-shorthair": "Brasilianisch Kurzhaar",
    "khao-manee": "Khao Manee", "lykoi": "Lykoi", "munchkin": "Munchkin",
    "highlander": "Highlander", "serengeti": "Serengeti", "thai": "Thaikatze",
    "chantilly-tiffany": "Chantilly-Tiffany", "york-chocolate": "York Chocolate",
    "colorpoint-shorthair": "Colorpoint Kurzhaar", "javanese": "Javanese",
    "oriental-longhair": "Orientalisch Langhaar", "british-longhair": "Britisch Langhaar",
    "asian": "Asian", "tiffanie": "Tiffanie", "california-spangled": "California Spangled",
    "dragon-li": "Dragon Li", "suphalak": "Suphalak", "aphrodite-giant": "Aphrodite-Riesenkatze",
    "cyprus": "Zypernkatze"
}

# German translations
SIZE_DE = {"small": "Klein", "medium": "Mittel", "large": "Groß", "extra-large": "Sehr groß"}
COAT_DE = {"longhair": "Langhaar", "shorthair": "Kurzhaar", "semi-longhair": "Halblanghaar", "hairless": "Haarlos", "rex": "Rex"}
ORIGIN_DE = {
    "United States": "USA", "United Kingdom": "Großbritannien", "England": "England",
    "France": "Frankreich", "Russia": "Russland", "Thailand": "Thailand", "Iran": "Iran",
    "Egypt": "Ägypten", "Turkey": "Türkei", "Japan": "Japan", "Canada": "Kanada",
    "Australia": "Australien", "Germany": "Deutschland", "Norway": "Norwegen",
    "Burma": "Burma", "Ethiopia": "Äthiopien", "Singapore": "Singapur", "Isle of Man": "Isle of Man"
}

TEMPERAMENT_DE = {
    "calm": "Ruhig", "gentle": "Sanft", "affectionate": "Liebevoll", "quiet": "Leise",
    "playful": "Verspielt", "intelligent": "Intelligent", "curious": "Neugierig",
    "active": "Aktiv", "social": "Sozial", "loyal": "Treu", "shy": "Schüchtern",
    "independent": "Unabhängig", "friendly": "Freundlich", "vocal": "Gesprächig",
    "energetic": "Energisch", "adaptable": "Anpassungsfähig", "sweet": "Süß",
    "devoted": "Ergeben", "sensitive": "Sensibel", "mischievous": "Schelmisch",
    "bold": "Mutig", "athletic": "Athletisch", "reserved": "Zurückhaltend",
    "docile": "Fügsam", "patient": "Geduldig", "alert": "Aufmerksam",
    "loving": "Liebend", "easygoing": "Entspannt", "outgoing": "Kontaktfreudig"
}

# German overview/health/care translations (AI-generated for common breeds)
CONTENT_DE = {
    "persian": {
        "overview": "Die Perserkatze ist eine der ältesten und bekanntesten Katzenrassen der Welt. Mit ihrem charakteristischen flachen Gesicht, den runden Augen und dem fließenden Fell sind sie seit Jahrhunderten geschätzte Begleiter. Perser sind der Inbegriff einer Schoßkatze – ruhig, sanftmütig und zufrieden damit, bequem zu faulenzen.",
        "health": "Perser sind anfällig für Polyzystische Nierenerkrankung (PKD), Atemprobleme aufgrund ihres flachen Gesichts (brachyzephales Syndrom) und Augenerkrankungen wie übermäßiges Tränen. Regelmäßige Tierarztuntersuchungen und Gentests werden empfohlen. Ihr flaches Gesicht kann auch zu Zahnproblemen führen.",
        "care": "Tägliche Fellpflege ist unerlässlich, um Verfilzungen im langen Fell zu verhindern. Ihre Augen müssen regelmäßig gereinigt werden, da sie zu Tränenflecken neigen. Halten Sie sie drinnen, da ihr Fell und flaches Gesicht sie anfällig machen. Füttern Sie hochwertiges Futter und überwachen Sie das Gewicht, da sie zu Übergewicht neigen."
    },
    "maine-coon": {
        "overview": "Die Maine Coon ist Amerikas einheimische Langhaarkatze und eine der größten domestizierten Rassen. Als 'sanfte Riesen' bekannt, verbinden sie beeindruckende Größe mit einer freundlichen, hundeähnlichen Persönlichkeit. Sie sind ausgezeichnete Mäusejäger mit einem robusten Aussehen, das für die harten Winter Neuenglands geeignet ist.",
        "health": "Maine Coons können anfällig für Hypertrophe Kardiomyopathie (HCM), Hüftdysplasie und Spinale Muskelatrophie (SMA) sein. Regelmäßige Herzuntersuchungen werden empfohlen. Trotz ihrer Größe sind sie bei richtiger Pflege generell gesunde Katzen und können 12-15 Jahre alt werden.",
        "care": "Ihr halblanges Fell muss 2-3 mal wöchentlich gebürstet werden, um Verfilzungen zu verhindern. Sie genießen interaktives Spielen und brauchen Platz zum Klettern und Erkunden. Stellen Sie stabile Kratzbäume bereit, die ihr Gewicht tragen können. Sie mögen oft Wasser und 'helfen' gerne beim Abwaschen!"
    },
    "ragdoll": {
        "overview": "Die Ragdoll erhielt ihren Namen von ihrer Tendenz, beim Hochheben schlaff zu werden wie eine Stoffpuppe. Diese sanften Riesen sind für ihr ruhiges Temperament und ihre wunderschönen blauen Augen bekannt. Sie folgen ihren Besitzern oft von Raum zu Raum und sind bemerkenswert gutmütig.",
        "health": "Ragdolls können anfällig für Hypertrophe Kardiomyopathie (HCM) und Blasensteine sein. Regelmäßige Herzuntersuchungen werden empfohlen. Sie sind im Allgemeinen gesund und leben typischerweise 12-17 Jahre bei richtiger Pflege.",
        "care": "Ihr seidiges Fell verfilzt weniger als bei anderen Langhaarkatzen, aber wöchentliches Bürsten wird empfohlen. Halten Sie sie drinnen, da sie sehr vertrauensvoll und schlecht auf der Straße sind. Bieten Sie interaktives Spielzeug und Klettermöglichkeiten."
    },
    "british-shorthair": {
        "overview": "Die Britisch Kurzhaar ist eine der ältesten englischen Katzenrassen mit einem robusten, muskulösen Körperbau und einem dichten, plüschigen Fell. Sie sind für ihr ruhiges, ausgeglichenes Temperament bekannt und werden oft als 'Teddy-Bär-Katzen' bezeichnet.",
        "health": "Britisch Kurzhaar können anfällig für Hypertrophe Kardiomyopathie (HCM) und Polyzystische Nierenerkrankung (PKD) sein. Regelmäßige Gesundheitsuntersuchungen werden empfohlen. Sie neigen zu Übergewicht, daher ist eine kontrollierte Ernährung wichtig.",
        "care": "Wöchentliches Bürsten reicht aus, um ihr dichtes Fell in gutem Zustand zu halten. Sie sind relativ pflegeleicht, brauchen aber regelmäßige Bewegung, um ein gesundes Gewicht zu halten. Bieten Sie interaktives Spielzeug und Kratzmöglichkeiten."
    },
    "siamese": {
        "overview": "Die Siamkatze ist eine der ältesten und bekanntesten Katzenrassen, berühmt für ihre auffälligen blauen Augen, ihr Points-Muster und ihre gesprächige Natur. Sie sind äußerst sozial und bilden starke Bindungen zu ihren Menschen.",
        "health": "Siamesen können anfällig für Amyloidose, Asthma und bestimmte Herzerkrankungen sein. Regelmäßige Tierarztbesuche sind wichtig. Sie sind im Allgemeinen langlebig und können 15-20 Jahre alt werden.",
        "care": "Ihr kurzes Fell braucht minimale Pflege – wöchentliches Bürsten reicht aus. Sie brauchen viel geistige Stimulation und soziale Interaktion. Einsamkeit tolerieren sie schlecht, daher ist ein Spielkamerad oder viel menschliche Gesellschaft ideal."
    }
}

def get_de_name(breed_id):
    return BREED_NAMES_DE.get(breed_id, breed_id.replace('-', ' ').title())

def get_de_temperament(temps):
    return [TEMPERAMENT_DE.get(t.lower(), t) for t in temps]

def get_de_content(breed_id, field, default):
    if breed_id in CONTENT_DE and field in CONTENT_DE[breed_id]:
        return CONTENT_DE[breed_id][field]
    # Fallback to English
    return default

def generate_breed_page(breed):
    breed_id = breed['id']
    de_name = get_de_name(breed_id)
    
    # Get content
    overview = get_de_content(breed_id, 'overview', breed.get('overview', ''))
    health = get_de_content(breed_id, 'health', breed.get('health', ''))
    care = get_de_content(breed_id, 'care', breed.get('care', ''))
    
    # Translate temperament
    temps = get_de_temperament(breed.get('temperament', []))
    temp_tags = ''.join([f'<span class="bg-gradient-to-r from-fuchsia-100 to-purple-100 text-slate-700 px-4 py-2 rounded-full text-sm font-medium">{t}</span>' for t in temps])
    
    # Translate other fields
    origin = ORIGIN_DE.get(breed.get('origin', ''), breed.get('origin', ''))
    size = SIZE_DE.get(breed.get('size', {}).get('category', ''), breed.get('size', {}).get('category', ''))
    coat = COAT_DE.get(breed.get('coat', {}).get('type', ''), breed.get('coat', {}).get('type', ''))
    
    # Best for / Not ideal for
    best_for = breed.get('best_for', ['Familien', 'Wohnungsleben'])
    not_ideal = breed.get('not_ideal_for', ['Sehr beschäftigte Menschen'])
    
    best_for_html = ''.join([f'''<li class="flex items-start gap-2"><svg class="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg><span>{item}</span></li>''' for item in best_for[:3]])
    not_ideal_html = ''.join([f'''<li class="flex items-start gap-2"><svg class="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg><span>{item}</span></li>''' for item in not_ideal[:2]])
    
    ratings = breed.get('ratings', {})
    
    html = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{de_name} - Rasseführer | CatFinder</title>
    <meta name="description" content="{de_name}: Erfahren Sie alles über Temperament, Pflege und Eigenschaften dieser wunderbaren Katzenrasse.">
    <link rel="canonical" href="https://catfinder.app/de/breeds/{breed_id}/">
    <link rel="alternate" hreflang="en" href="https://catfinder.app/breeds/{breed_id}/">
    <link rel="alternate" hreflang="de" href="https://catfinder.app/de/breeds/{breed_id}/">
    <link rel="alternate" hreflang="es" href="https://catfinder.app/es/breeds/{breed_id}/">
    <link rel="icon" href="/favicon.ico">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .rating-bar {{ height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden; }}
        .rating-bar::after {{ content: ''; display: block; height: 100%; border-radius: 4px; }}
        .rating-1::after {{ width: 20%; background: linear-gradient(90deg, #f472b6, #c084fc); }}
        .rating-2::after {{ width: 40%; background: linear-gradient(90deg, #f472b6, #c084fc); }}
        .rating-3::after {{ width: 60%; background: linear-gradient(90deg, #f472b6, #c084fc); }}
        .rating-4::after {{ width: 80%; background: linear-gradient(90deg, #f472b6, #c084fc); }}
        .rating-5::after {{ width: 100%; background: linear-gradient(90deg, #f472b6, #c084fc); }}
    </style>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-8JVFQHMFD3"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-8JVFQHMFD3');</script>
</head>
<body class="bg-gradient-to-br from-fuchsia-50 via-white to-purple-50 min-h-screen">
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="/de/" class="flex items-center gap-3">
                <div class="w-10 h-10 bg-gradient-to-br from-fuchsia-500 to-purple-600 rounded-xl flex items-center justify-center text-white">
                    <i data-lucide="cat" class="w-6 h-6"></i>
                </div>
                <span class="text-xl font-bold text-slate-800">CatFinder</span>
            </a>
            <nav class="flex items-center gap-6 text-sm font-medium">
                <a href="/de/search/" class="text-slate-600 hover:text-fuchsia-600">Rassen</a>
                <a href="/de/quiz/" class="bg-gradient-to-r from-fuchsia-500 to-purple-600 text-white px-5 py-2.5 rounded-xl font-semibold">Quiz</a>
            </nav>
        </div>
    </header>

    <main class="max-w-4xl mx-auto px-4 py-8">
        <nav class="text-sm mb-6">
            <ol class="flex items-center gap-2 text-slate-600">
                <li><a href="/de/" class="hover:text-fuchsia-600">Startseite</a></li>
                <li>/</li>
                <li><a href="/de/search/" class="hover:text-fuchsia-600">Rassen</a></li>
                <li>/</li>
                <li class="text-slate-900 font-medium">{de_name}</li>
            </ol>
        </nav>

        <div class="bg-white rounded-3xl shadow-xl overflow-hidden mb-8">
            <div class="md:flex">
                <div class="md:w-2/5">
                    <img src="/images/breeds/{breed_id}.webp" alt="{de_name}" class="w-full h-80 md:h-full object-cover object-top" onerror="this.src='/images/breeds/placeholder.webp'">
                </div>
                <div class="p-6 md:p-8 md:w-3/5">
                    <h1 class="text-3xl md:text-4xl font-bold text-slate-900 mb-2">{de_name}</h1>
                    <div class="grid grid-cols-2 gap-3 mt-4">
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path></svg>
                            <div><p class="text-xs text-slate-500">Herkunft</p><p class="font-semibold text-slate-700">{origin}</p></div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                            <div><p class="text-xs text-slate-500">Lebenserwartung</p><p class="font-semibold text-slate-700">{breed.get('lifespan', '12-15 Jahre')}</p></div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg>
                            <div><p class="text-xs text-slate-500">Größe</p><p class="font-semibold text-slate-700">{size}</p></div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"></path></svg>
                            <div><p class="text-xs text-slate-500">Fell</p><p class="font-semibold text-slate-700">{coat}</p></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-6">Rassenbewertungen</h2>
            <div class="grid md:grid-cols-2 gap-x-12 gap-y-4">
                <div><div class="flex justify-between mb-2"><span class="text-slate-600">Zuneigung</span><span class="font-medium">{ratings.get('affection', 3)}/5</span></div><div class="rating-bar rating-{ratings.get('affection', 3)}"></div></div>
                <div><div class="flex justify-between mb-2"><span class="text-slate-600">Aktivität</span><span class="font-medium">{ratings.get('activity', 3)}/5</span></div><div class="rating-bar rating-{ratings.get('activity', 3)}"></div></div>
                <div><div class="flex justify-between mb-2"><span class="text-slate-600">Pflege</span><span class="font-medium">{ratings.get('grooming', 3)}/5</span></div><div class="rating-bar rating-{ratings.get('grooming', 3)}"></div></div>
                <div><div class="flex justify-between mb-2"><span class="text-slate-600">Lautstärke</span><span class="font-medium">{ratings.get('vocality', 3)}/5</span></div><div class="rating-bar rating-{ratings.get('vocality', 3)}"></div></div>
                <div><div class="flex justify-between mb-2"><span class="text-slate-600">Unabhängigkeit</span><span class="font-medium">{ratings.get('independence', 3)}/5</span></div><div class="rating-bar rating-{ratings.get('independence', 3)}"></div></div>
                <div><div class="flex justify-between mb-2"><span class="text-slate-600">Kinderfreundlich</span><span class="font-medium">{ratings.get('kid_friendly', 3)}/5</span></div><div class="rating-bar rating-{ratings.get('kid_friendly', 3)}"></div></div>
            </div>
        </section>

        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-4">Temperament</h2>
            <div class="flex flex-wrap gap-2">{temp_tags}</div>
        </section>

        <!-- Accordion Sections -->
        <div class="space-y-4 mb-8">
            <details class="bg-white rounded-2xl shadow-sm border border-slate-200 group" open>
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-3">
                        <svg class="w-5 h-5 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                        Übersicht
                    </h2>
                    <svg class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </summary>
                <div class="px-6 pb-6"><p class="text-slate-600 leading-relaxed">{overview}</p></div>
            </details>

            <details class="bg-white rounded-2xl shadow-sm border border-slate-200 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-3">
                        <svg class="w-5 h-5 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
                        Gesundheit
                    </h2>
                    <svg class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </summary>
                <div class="px-6 pb-6"><p class="text-slate-600 leading-relaxed">{health}</p></div>
            </details>

            <details class="bg-white rounded-2xl shadow-sm border border-slate-200 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-3">
                        <svg class="w-5 h-5 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"></path></svg>
                        Pflege & Haltung
                    </h2>
                    <svg class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </summary>
                <div class="px-6 pb-6"><p class="text-slate-600 leading-relaxed">{care}</p></div>
            </details>
        </div>

        <section class="bg-gradient-to-br from-fuchsia-50 via-purple-50 to-pink-50 rounded-2xl p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-6">Ist diese Rasse die richtige für Sie?</h2>
            <div class="grid md:grid-cols-2 gap-6">
                <div class="bg-white rounded-xl p-5 shadow-sm">
                    <h3 class="font-semibold text-green-700 mb-3 flex items-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        Ideal für
                    </h3>
                    <ul class="space-y-2 text-slate-600">{best_for_html}</ul>
                </div>
                <div class="bg-white rounded-xl p-5 shadow-sm">
                    <h3 class="font-semibold text-red-700 mb-3 flex items-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        Nicht ideal für
                    </h3>
                    <ul class="space-y-2 text-slate-600">{not_ideal_html}</ul>
                </div>
            </div>
        </section>
    </main>

    <footer class="bg-slate-900 text-slate-400 py-12">
        <div class="max-w-6xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-4">
            <div class="flex items-center gap-2"><i data-lucide="cat" class="w-6 h-6 text-fuchsia-400"></i><span class="font-bold text-white">CatFinder</span></div>
            <div class="flex gap-6 text-sm">
                <a href="/de/search/" class="hover:text-white">Rassen</a>
                <a href="/de/quiz/" class="hover:text-white">Quiz</a>
                <a href="/de/compare/" class="hover:text-white">Vergleichen</a>
                <a href="/de/about/" class="hover:text-white">Über uns</a>
            </div>
            <p class="text-sm">&copy; 2026 CatFinder</p>
        </div>
    </footer>
    <script>lucide.createIcons();</script>
</body>
</html>'''
    
    return html

# Generate all breed pages
os.makedirs('de/breeds', exist_ok=True)

for breed in breeds:
    breed_id = breed['id']
    html = generate_breed_page(breed)
    
    os.makedirs(f'de/breeds/{breed_id}', exist_ok=True)
    with open(f'de/breeds/{breed_id}/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Generated: de/breeds/{breed_id}/")

print(f"\nDone! Generated {len(breeds)} German breed pages.")
