#!/usr/bin/env python3
"""Generate Spanish cat breed pages from English data."""
import json
import os

# Load English breed data (has expanded content)
with open('data/breeds.json', 'r') as f:
    breeds = json.load(f)

# Spanish translations for breed names
BREED_NAMES_ES = {
    "persian": "Persa",
    "maine-coon": "Maine Coon",
    "ragdoll": "Ragdoll",
    "british-shorthair": "Británico de Pelo Corto",
    "siamese": "Siamés",
    "abyssinian": "Abisinio",
    "bengal": "Bengalí",
    "sphynx": "Sphynx",
    "scottish-fold": "Scottish Fold",
    "russian-blue": "Azul Ruso",
    "norwegian-forest-cat": "Bosque de Noruega",
    "burmese": "Burmés",
    "oriental-shorthair": "Oriental de Pelo Corto",
    "devon-rex": "Devon Rex",
    "cornish-rex": "Cornish Rex",
    "exotic-shorthair": "Exótico de Pelo Corto",
    "himalayan": "Himalayo",
    "american-shorthair": "Americano de Pelo Corto",
    "tonkinese": "Tonkinés",
    "ragamuffin": "RagaMuffin",
    "savannah": "Savannah",
    "siberian": "Siberiano",
    "balinese": "Balinés",
    "turkish-angora": "Angora Turco",
    "turkish-van": "Van Turco",
    "somali": "Somalí",
    "chartreux": "Chartreux",
    "ocicat": "Ocicat",
    "egyptian-mau": "Mau Egipcio",
    "birman": "Birmano",
    "singapura": "Singapura",
    "manx": "Manx",
    "japanese-bobtail": "Bobtail Japonés",
    "american-curl": "Curl Americano",
    "selkirk-rex": "Selkirk Rex",
    "laperm": "LaPerm",
    "korat": "Korat",
    "bombay": "Bombay",
    "havana-brown": "Habana Marrón",
    "burmilla": "Burmilla",
    "toyger": "Toyger",
    "pixie-bob": "Pixie-Bob",
    "cymric": "Cymric",
    "american-bobtail": "Bobtail Americano",
    "nebelung": "Nebelung",
    "snowshoe": "Snowshoe",
    "chausie": "Chausie",
    "sokoke": "Sokoke",
    "australian-mist": "Mist Australiano",
    "peterbald": "Peterbald",
    "donskoy": "Donskoy",
    "kurilian-bobtail": "Bobtail de las Kuriles",
    "american-wirehair": "Americano de Pelo Áspero",
    "european-shorthair": "Europeo de Pelo Corto",
    "brazilian-shorthair": "Brasileño de Pelo Corto",
    "khao-manee": "Khao Manee",
    "lykoi": "Lykoi",
    "munchkin": "Munchkin",
    "highlander": "Highlander",
    "serengeti": "Serengeti",
    "thai": "Thai",
    "chantilly-tiffany": "Chantilly-Tiffany",
    "york-chocolate": "York Chocolate",
    "colorpoint-shorthair": "Colorpoint de Pelo Corto",
    "javanese": "Javanés",
    "oriental-longhair": "Oriental de Pelo Largo",
    "british-longhair": "Británico de Pelo Largo",
    "asian": "Asiático",
    "tiffanie": "Tiffanie",
    "california-spangled": "California Spangled",
    "dragon-li": "Dragon Li",
    "suphalak": "Suphalak",
    "aphrodite-giant": "Gigante de Afrodita",
    "cyprus": "Chipriota"
}

# UI translations
UI_ES = {
    "Origin": "Origen",
    "Lifespan": "Esperanza de vida",
    "Weight": "Peso",
    "Coat": "Pelaje",
    "Breed Ratings": "Puntuaciones de la Raza",
    "Affection": "Afecto",
    "Activity Level": "Nivel de Actividad",
    "Grooming Needs": "Necesidades de Aseo",
    "Vocality": "Vocalización",
    "Independence": "Independencia",
    "Kid Friendly": "Apto para Niños",
    "Dog Friendly": "Apto para Perros",
    "Intelligence": "Inteligencia",
    "Temperament": "Temperamento",
    "Overview": "Descripción General",
    "Health": "Salud",
    "Care & Grooming": "Cuidados y Aseo",
    "Is This Breed Right for You?": "¿Es Esta Raza Adecuada para Ti?",
    "Best For": "Ideal Para",
    "Not Ideal For": "No Recomendado Para",
    "Home": "Inicio",
    "Breeds": "Razas",
    "Quiz": "Test",
    "Compare": "Comparar",
    "Search": "Buscar",
    "About": "Acerca de"
}

# Size translations
SIZE_ES = {
    "small": "Pequeño",
    "medium": "Mediano",
    "large": "Grande",
    "extra-large": "Extra Grande"
}

# Coat type translations
COAT_ES = {
    "longhair": "Pelo Largo",
    "shorthair": "Pelo Corto",
    "semi-longhair": "Pelo Semilargo",
    "hairless": "Sin Pelo",
    "rex": "Rex"
}

# Origin translations
ORIGIN_ES = {
    "United States": "Estados Unidos",
    "United Kingdom": "Reino Unido",
    "England": "Inglaterra",
    "France": "Francia",
    "Russia": "Rusia",
    "Thailand": "Tailandia",
    "Iran": "Irán",
    "Persia": "Persia",
    "Egypt": "Egipto",
    "Turkey": "Turquía",
    "Japan": "Japón",
    "Canada": "Canadá",
    "Australia": "Australia",
    "Germany": "Alemania",
    "Norway": "Noruega",
    "Burma": "Birmania",
    "Myanmar": "Myanmar",
    "Ethiopia": "Etiopía",
    "Singapore": "Singapur",
    "Isle of Man": "Isla de Man",
    "Scotland": "Escocia",
    "Kenya": "Kenia",
    "Brazil": "Brasil",
    "Cyprus": "Chipre",
    "China": "China",
    "Unknown": "Desconocido"
}

# Coat pattern translations
PATTERN_ES = {
    "various": "Varios",
    "solid": "Sólido",
    "solid black": "Negro sólido",
    "solid blue": "Azul sólido",
    "solid brown": "Marrón sólido",
    "solid white": "Blanco sólido",
    "solid chocolate/lavender": "Chocolate/Lavanda",
    "solid/tabby": "Sólido/Atigrado",
    "tabby": "Atigrado",
    "mackerel tabby": "Atigrado caballa",
    "ticked tabby": "Atigrado ticked",
    "spotted tabby": "Atigrado manchado",
    "spotted": "Manchado",
    "spotted/marbled": "Manchado/Marmoleado",
    "ticked": "Ticked",
    "ticked/solid": "Ticked/Sólido",
    "colorpoint": "Colorpoint",
    "colorpoint with white": "Colorpoint con blanco",
    "mink/colorpoint": "Mink/Colorpoint",
    "shaded/tipped": "Sombreado/Tipped",
    "van pattern": "Patrón Van",
    "roan": "Ruano"
}

# Verdict translations (Best For / Not Ideal)
VERDICT_ES = {
    # Best For
    "Active families": "Familias activas",
    "Active households": "Hogares activos",
    "Allergy sufferers": "Personas con alergias",
    "Any household": "Cualquier hogar",
    "Apartment living": "Vida en apartamento",
    "Apartments": "Apartamentos",
    "Cold climates": "Climas fríos",
    "Couples": "Parejas",
    "Elderly owners": "Dueños mayores",
    "Experienced cat owners": "Dueños con experiencia",
    "Experienced owners": "Dueños experimentados",
    "Families": "Familias",
    "Families with children": "Familias con niños",
    "Families with older children": "Familias con niños mayores",
    "Farms": "Granjas",
    "First-time cat owners": "Dueños primerizos",
    "First-time owners": "Dueños primerizos",
    "Homes with dogs": "Hogares con perros",
    "Homes with outdoor access": "Hogares con acceso exterior",
    "Indoor living": "Vida interior",
    "Interactive households": "Hogares interactivos",
    "Lap cat seekers": "Buscadores de gatos de regazo",
    "Large homes": "Casas grandes",
    "Multi-pet homes": "Hogares con varias mascotas",
    "Quiet households": "Hogares tranquilos",
    "Rural homes": "Casas rurales",
    "Seniors": "Personas mayores",
    "Single-pet homes": "Hogares con una sola mascota",
    "Singles": "Solteros",
    "Therapy situations": "Situaciones de terapia",
    "Those appreciating beauty": "Quienes aprecian la belleza",
    "Those appreciating elegance": "Quienes aprecian la elegancia",
    "Those home often": "Quienes están en casa frecuentemente",
    "Those wanting a companion": "Quienes buscan compañía",
    "Those wanting a talkative cat": "Quienes quieren un gato conversador",
    "Those wanting affection": "Quienes buscan afecto",
    "Those wanting beautiful cats": "Quienes quieren gatos hermosos",
    "Those wanting black cats": "Quienes quieren gatos negros",
    "Those wanting companionship": "Quienes buscan compañerismo",
    "Those wanting cuddles": "Quienes quieren mimos",
    "Those wanting dog-like cats": "Quienes quieren gatos como perros",
    "Those wanting entertainment": "Quienes buscan entretenimiento",
    "Those wanting hairless cats": "Quienes quieren gatos sin pelo",
    "Those wanting healthy breeds": "Quienes quieren razas saludables",
    "Those wanting interaction": "Quienes buscan interacción",
    "Those wanting large cats": "Quienes quieren gatos grandes",
    "Those wanting loyal cats": "Quienes quieren gatos leales",
    "Those wanting playful cats": "Quienes quieren gatos juguetones",
    "Those wanting rare breeds": "Quienes quieren razas raras",
    "Those wanting small cats": "Quienes quieren gatos pequeños",
    "Those wanting talkative cats": "Quienes quieren gatos conversadores",
    "Those wanting tiger-looks": "Quienes quieren aspecto de tigre",
    "Those wanting unique cats": "Quienes quieren gatos únicos",
    "Those wanting unique looks": "Quienes quieren apariencia única",
    "Those wanting unusual breeds": "Quienes quieren razas inusuales",
    "Those wanting unusual cats": "Quienes quieren gatos inusuales",
    "Those wanting unusual coats": "Quienes quieren pelajes inusuales",
    "Those wanting vocal cats": "Quienes quieren gatos vocales",
    "Those wanting wild looks": "Quienes quieren aspecto salvaje",
    "Those who love Persians but not grooming": "Quienes aman los Persas pero no el aseo",
    "Those who love Siamese": "Quienes aman los Siameses",
    "Those with grooming time": "Quienes tienen tiempo para el aseo",
    "Those with pools/water": "Quienes tienen piscina/agua",
    "Those with time to play": "Quienes tienen tiempo para jugar",
    "Travel (adaptable)": "Viajes (adaptable)",
    "Working professionals": "Profesionales que trabajan",
    "Those wanting Burmese-type": "Quienes quieren tipo Burmés",
    
    # Not Ideal
    "Budget-conscious (extremely rare)": "Presupuesto limitado (extremadamente raro)",
    "Budget-conscious (very rare)": "Presupuesto limitado (muy raro)",
    "Budget-conscious owners (rare breed)": "Dueños con presupuesto limitado (raza rara)",
    "Busy families": "Familias ocupadas",
    "Busy households": "Hogares ocupados",
    "Busy households with children": "Hogares ocupados con niños",
    "Busy households with many visitors": "Hogares ocupados con muchas visitas",
    "Busy households with visitors": "Hogares ocupados con visitas",
    "Cold climates without heating": "Climas fríos sin calefacción",
    "Cold environments": "Ambientes fríos",
    "Cold homes": "Casas frías",
    "Families with young children": "Familias con niños pequeños",
    "Hot climates": "Climas cálidos",
    "Outdoor cat seekers": "Buscadores de gatos de exterior",
    "Quiet seekers": "Buscadores de tranquilidad",
    "Small apartments": "Apartamentos pequeños",
    "Small spaces": "Espacios pequeños",
    "Those away often": "Quienes se ausentan frecuentemente",
    "Those concerned about genetic health issues": "Preocupados por problemas genéticos de salud",
    "Those concerned about genetic issues": "Preocupados por problemas genéticos",
    "Those concerned about health issues": "Preocupados por problemas de salud",
    "Those disliking grooming": "Quienes no les gusta el aseo",
    "Those disliking unusual features": "Quienes no les gustan características inusuales",
    "Those wanting a calm cat": "Quienes quieren un gato tranquilo",
    "Those wanting a calm lap cat": "Quienes quieren un gato de regazo tranquilo",
    "Those wanting a cuddly cat": "Quienes quieren un gato mimoso",
    "Those wanting a lap cat": "Quienes quieren un gato de regazo",
    "Those wanting a quiet cat": "Quienes quieren un gato silencioso",
    "Those wanting a very active cat": "Quienes quieren un gato muy activo",
    "Those wanting a vocal cat": "Quienes quieren un gato vocal",
    "Those wanting an active cat": "Quienes quieren un gato activo",
    "Those wanting calm cats": "Quienes quieren gatos tranquilos",
    "Those wanting exotic breeds": "Quienes quieren razas exóticas",
    "Those wanting exotic looks": "Quienes quieren aspecto exótico",
    "Those wanting fluffy cats": "Quienes quieren gatos peludos",
    "Those wanting low grooming": "Quienes quieren poco aseo",
    "Those wanting quiet": "Quienes buscan tranquilidad",
    "Those wanting rare/exotic breeds": "Quienes quieren razas raras/exóticas",
    "Those wanting very active cats": "Quienes quieren gatos muy activos",
    "Those wanting very affectionate cats": "Quienes quieren gatos muy cariñosos",
    "Those who dislike grooming": "Quienes no les gusta el aseo",
}

# Temperament translations
TEMPERAMENT_ES = {
    "calm": "Tranquilo",
    "gentle": "Gentil",
    "affectionate": "Cariñoso",
    "quiet": "Silencioso",
    "friendly": "Amigable",
    "playful": "Juguetón",
    "intelligent": "Inteligente",
    "docile": "Dócil",
    "easygoing": "Relajado",
    "loyal": "Leal",
    "independent": "Independiente",
    "vocal": "Vocal",
    "social": "Social",
    "active": "Activo",
    "curious": "Curioso",
    "confident": "Seguro",
    "energetic": "Enérgico",
    "reserved": "Reservado",
    "devoted": "Devoto",
    "mischievous": "Travieso",
    "outgoing": "Extrovertido"
}

def generate_es_breed_page(breed):
    """Generate Spanish breed page."""
    breed_id = breed['id']
    name_en = breed['name']
    name_es = BREED_NAMES_ES.get(breed_id, name_en)
    
    origin_en = breed.get('origin', 'Unknown')
    origin = ORIGIN_ES.get(origin_en, origin_en)
    lifespan_en = breed.get('lifespan', '12-15 years')
    lifespan = lifespan_en.replace(' years', ' años').replace(' year', ' año')
    weight = breed['size'].get('weight_kg', '4-6')
    size_cat = breed['size']['category']
    size_es = SIZE_ES.get(size_cat, size_cat.capitalize())
    coat_type = breed['coat']['type']
    coat_es = COAT_ES.get(coat_type, coat_type.capitalize())
    coat_pattern_en = breed['coat']['pattern']
    coat_pattern = PATTERN_ES.get(coat_pattern_en, coat_pattern_en)
    
    description_en = breed.get('description', '')
    
    # Load Spanish translations
    breed_id = breed['id']
    try:
        with open('data/breeds_es.json', 'r') as f:
            es_translations = json.load(f)
        es_content = es_translations.get(breed_id, {})
        overview = es_content.get('overview', description_en)
        health = es_content.get('health', 'Se recomiendan chequeos veterinarios regulares para esta raza.')
        care = es_content.get('care', 'El aseo regular y una dieta equilibrada son importantes para esta raza.')
        # Use first sentence of overview as short description
        description = overview.split('.')[0] + '.' if overview else description_en
    except:
        overview = description_en
        description = description_en
        health = 'Se recomiendan chequeos veterinarios regulares para esta raza.'
        care = 'El aseo regular y una dieta equilibrada son importantes para esta raza.'
    
    ratings = breed.get('ratings', {})
    temperament = breed.get('temperament', [])
    verdict = breed.get('verdict', {})
    best_for = verdict.get('best_for', [])
    not_ideal = verdict.get('not_ideal', [])
    
    # Generate ratings HTML
    rating_labels = {
        'affection': 'Afecto',
        'activity': 'Nivel de Actividad',
        'grooming': 'Necesidades de Aseo',
        'vocality': 'Vocalización',
        'independence': 'Independencia',
        'kid_friendly': 'Apto para Niños',
        'dog_friendly': 'Apto para Perros',
        'intelligence': 'Inteligencia'
    }
    
    ratings_html = ''
    for key, label in rating_labels.items():
        value = ratings.get(key, 3)
        ratings_html += f'''
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">{label}</span><span class="font-medium">{value}/5</span></div>
                    <div class="rating-bar rating-{value}"></div>
                </div>'''
    
    # Temperament HTML
    temp_html = ''.join([f'<span class="bg-gradient-to-r from-fuchsia-100 to-purple-100 text-slate-700 px-4 py-2 rounded-full text-sm font-medium">{TEMPERAMENT_ES.get(t, t.capitalize())}</span>' for t in temperament[:6]])
    
    # Best for / Not ideal HTML
    best_for_html = ''.join([f'<li class="flex items-start gap-2"><svg class="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg><span>{VERDICT_ES.get(item, item)}</span></li>' for item in best_for])
    not_ideal_html = ''.join([f'<li class="flex items-start gap-2"><svg class="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg><span>{VERDICT_ES.get(item, item)}</span></li>' for item in not_ideal])
    
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-8JVFQHMFD3"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-8JVFQHMFD3');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name_es} - Guía de Raza | CatFinder</title>
    <meta name="description" content="Guía completa del {name_es}: temperamento, cuidados, salud y más. Descubre si esta raza es adecuada para ti.">
    <link rel="canonical" href="https://catfinder.app/es/breeds/{breed_id}/">
    <link rel="alternate" hreflang="en" href="https://catfinder.app/breeds/{breed_id}/">
    <link rel="alternate" hreflang="es" href="https://catfinder.app/es/breeds/{breed_id}/">
    <link rel="alternate" hreflang="de" href="https://catfinder.app/de/breeds/{breed_id}/">
    <link rel="alternate" hreflang="x-default" href="https://catfinder.app/breeds/{breed_id}/">
    <meta property="og:title" content="{name_es} - Guía de Raza | CatFinder">
    <meta property="og:description" content="Todo sobre el {name_es}: personalidad, cuidados, necesidades de aseo y más.">
    <meta property="og:image" content="https://catfinder.app/images/breeds/{breed_id}.webp">
    <meta property="og:url" content="https://catfinder.app/es/breeds/{breed_id}/">
    <meta property="og:type" content="article">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .rating-bar {{ height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden; }}
        .rating-bar::after {{ content: ''; display: block; height: 100%; border-radius: 4px; background: linear-gradient(90deg, #d946ef, #a855f7); }}
        .rating-1::after {{ width: 20%; }}
        .rating-2::after {{ width: 40%; }}
        .rating-3::after {{ width: 60%; }}
        .rating-4::after {{ width: 80%; }}
        .rating-5::after {{ width: 100%; }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800">
    <nav class="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4">
            <div class="flex items-center justify-between">
                <a href="/es/" class="flex items-center gap-2">
                    <div class="w-10 h-10 bg-gradient-to-br from-fuchsia-500 to-purple-600 rounded-xl flex items-center justify-center text-white shadow-lg shadow-fuchsia-500/20">
                        <i data-lucide="cat" class="w-6 h-6"></i>
                    </div>
                    <span class="font-bold text-xl bg-gradient-to-r from-fuchsia-600 to-purple-600 bg-clip-text text-transparent">CatFinder</span>
                </a>
                <div class="flex items-center gap-6">
                    <a href="/es/search/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Razas</a>
                    <a href="/es/quiz/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Test</a>
                    <a href="/es/compare/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Comparar</a>
                    <a href="/es/search/" class="text-slate-600 hover:text-slate-900 font-medium">Buscar</a>
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-6xl mx-auto px-4 py-8">
        <nav class="text-sm text-slate-600 mb-6">
            <a href="/es/" class="hover:text-fuchsia-600">Inicio</a>
            <span class="mx-2">/</span>
            <a href="/es/search/" class="hover:text-fuchsia-600">Razas</a>
            <span class="mx-2">/</span>
            <span class="text-slate-700">{name_es}</span>
        </nav>

        <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden mb-8">
            <div class="md:flex">
                <div class="md:w-2/5">
                    <img src="/images/breeds/{breed_id}.webp" alt="{name_es}" class="w-full h-full object-cover">
                </div>
                <div class="md:w-3/5 p-6 md:p-8">
                    <div class="flex flex-wrap gap-2 mb-4">
                        <span class="bg-fuchsia-100 text-fuchsia-700 px-3 py-1 rounded-full text-sm font-medium">{coat_es}</span>
                        <span class="bg-purple-100 text-purple-700 px-3 py-1 rounded-full text-sm font-medium">{size_es}</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-bold text-slate-900 mb-4">{name_es}</h1>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                            <div>
                                <p class="text-xs text-slate-500">Origen</p>
                                <p class="font-semibold text-slate-700">{origin}</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                            <div>
                                <p class="text-xs text-slate-500">Esperanza de vida</p>
                                <p class="font-semibold text-slate-700">{lifespan}</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg>
                            <div>
                                <p class="text-xs text-slate-500">Peso</p>
                                <p class="font-semibold text-slate-700">{weight} kg</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"></path></svg>
                            <div>
                                <p class="text-xs text-slate-500">Pelaje</p>
                                <p class="font-semibold text-slate-700">{coat_pattern}</p>
                            </div>
                        </div>
                    </div>
                    <p class="mt-4 text-slate-600 leading-relaxed">{description}</p>
                </div>
            </div>
        </div>

        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-6">Puntuaciones de la Raza</h2>
            <div class="grid md:grid-cols-2 gap-x-12 gap-y-4">
                {ratings_html}
            </div>
        </section>

        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-4">Temperamento</h2>
            <div class="flex flex-wrap gap-2">
                {temp_html}
            </div>
        </section>

        <!-- Accordion Sections -->
        <div class="space-y-4 mb-8">
            <details class="bg-white rounded-2xl shadow-sm border border-slate-200 group" open>
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-3">
                        <svg class="w-5 h-5 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                        Descripción General
                    </h2>
                    <svg class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </summary>
                <div class="px-6 pb-6">
                    <p class="text-slate-600 leading-relaxed">{overview}</p>
                </div>
            </details>

            <details class="bg-white rounded-2xl shadow-sm border border-slate-200 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-3">
                        <svg class="w-5 h-5 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
                        Salud
                    </h2>
                    <svg class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </summary>
                <div class="px-6 pb-6">
                    <p class="text-slate-600 leading-relaxed">{health}</p>
                </div>
            </details>

            <details class="bg-white rounded-2xl shadow-sm border border-slate-200 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-3">
                        <svg class="w-5 h-5 text-fuchsia-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"></path></svg>
                        Cuidados y Aseo
                    </h2>
                    <svg class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </summary>
                <div class="px-6 pb-6">
                    <p class="text-slate-600 leading-relaxed">{care}</p>
                </div>
            </details>
        </div>

        <section class="bg-gradient-to-br from-fuchsia-50 via-purple-50 to-pink-50 rounded-2xl p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-6">¿Es Esta Raza Adecuada para Ti?</h2>
            <div class="grid md:grid-cols-2 gap-6 mb-6">
                <div class="bg-white rounded-xl p-5 shadow-sm">
                    <h3 class="font-semibold text-green-700 mb-3 flex items-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        Ideal Para
                    </h3>
                    <ul class="space-y-2 text-slate-600">
                        {best_for_html}
                    </ul>
                </div>
                <div class="bg-white rounded-xl p-5 shadow-sm">
                    <h3 class="font-semibold text-red-700 mb-3 flex items-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        No Recomendado Para
                    </h3>
                    <ul class="space-y-2 text-slate-600">
                        {not_ideal_html}
                    </ul>
                </div>
            </div>
        </section>
    </main>

    <footer class="bg-slate-900 text-slate-400 py-12">
        <div class="max-w-6xl mx-auto px-4">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                <div class="flex items-center gap-2">
                    <svg class="w-6 h-6 text-fuchsia-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5c.67 0 1.35.09 2 .26 1.78-2 5.03-2.84 6.42-2.26 1.4.58-.42 7-.42 7 .57 1.07 1 2.24 1 3.44C21 17.9 16.97 21 12 21s-9-3-9-7.56c0-1.25.5-2.4 1-3.44 0 0-1.89-6.42-.5-7 1.39-.58 4.72.23 6.5 2.23A9.04 9.04 0 0 1 12 5Z"/><path d="M8 14v.5"/><path d="M16 14v.5"/><path d="M11.25 16.25h1.5L12 17l-.75-.75Z"/></svg>
                    <span class="font-bold text-white">CatFinder</span>
                </div>
                <div class="flex gap-6 text-sm">
                    <a href="/es/search/" class="hover:text-white">Razas</a>
                    <a href="/es/quiz/" class="hover:text-white">Test</a>
                    <a href="/es/compare/" class="hover:text-white">Comparar</a>
                    <a href="/es/about/" class="hover:text-white">Acerca de</a>
                </div>
                <p class="text-sm">&copy; 2026 CatFinder</p>
            </div>
        </div>
    </footer>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script>lucide.createIcons();</script>
</body>
</html>'''
    
    return html

# Generate all Spanish breed pages
os.makedirs('es/breeds', exist_ok=True)

print("Generating Spanish breed pages...")
for breed in breeds:
    breed_id = breed['id']
    html = generate_es_breed_page(breed)
    
    # Create breed directory
    breed_dir = f'es/breeds/{breed_id}'
    os.makedirs(breed_dir, exist_ok=True)
    
    # Write HTML file
    with open(f'{breed_dir}/index.html', 'w') as f:
        f.write(html)
    
    print(f"  ✓ {BREED_NAMES_ES.get(breed_id, breed['name'])}")

print(f"\n✅ Generated {len(breeds)} Spanish breed pages")
