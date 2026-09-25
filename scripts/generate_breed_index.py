#!/usr/bin/env python3
"""Generate the A-Z breed index pages: /breeds/, /de/breeds/, /es/breeds/.

Names, origins, lifespans and summaries are read from the (localized) breed
pages themselves so the index always matches what each breed page shows.
Header/footer are copied from an existing breed page of the same language.
"""
import html
import json
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.chdir(ROOT)

TODAY = '2026-09-25'

COAT_GROUP = {
    'shorthair': 'short', 'shorthair (partial)': 'short',
    'semi-longhair': 'long', 'longhair': 'long',
    'shorthair/longhair': 'short long',
    'rex': 'curly', 'wirehair': 'curly',
    'hairless': 'hairless', 'hairless/shorthair': 'hairless short',
}

L = {
    'en': {
        'prefix': '', 'lifespan': 'Lifespan', 'origin': 'Origin',
        'title': 'All 74 Cat Breeds A-Z: Complete Breed List | CatFinder',
        'desc': 'All 74 cat breeds from Abyssinian to York Chocolate, with origin, lifespan and temperament for each. Filter by coat type and open any breed’s full profile.',
        'h1': 'All Cat Breeds A–Z',
        'intro': 'CatFinder covers <strong>74 cat breeds</strong>, from everyday companions like the <a href="/breeds/british-shorthair/" class="text-teal-600 hover:underline">British Shorthair</a> to rare natural breeds like the <a href="/breeds/sokoke/" class="text-teal-600 hover:underline">Sokoke</a>. Each profile rates affection, activity, grooming and kid-friendliness. Not sure where to start? <a href="/quiz/" class="text-teal-600 hover:underline">Take the breed quiz</a> or <a href="/compare/" class="text-teal-600 hover:underline">compare two breeds</a>.',
        'filter_ph': 'Filter breeds by name or origin…',
        'filters': [('all', 'All'), ('short', 'Shorthair'), ('long', 'Longhair'), ('curly', 'Curly & wirehair'), ('hairless', 'Hairless')],
        'count': 'breeds shown', 'none': 'No breeds match that filter.',
        'crumb_home': 'Home', 'crumb': 'Breeds',
        'years': 'years',
    },
    'de': {
        'prefix': '/de', 'lifespan': 'Lebenserwartung', 'origin': 'Herkunft',
        'title': 'Alle 74 Katzenrassen von A-Z: Komplette Rassenliste | CatFinder',
        'desc': 'Alle 74 Katzenrassen von Abessinier bis York Chocolate, jeweils mit Herkunft, Lebenserwartung und Charakter. Nach Fellart filtern und jedes Rassenprofil öffnen.',
        'h1': 'Alle Katzenrassen von A–Z',
        'intro': 'CatFinder stellt <strong>74 Katzenrassen</strong> vor, von beliebten Begleitern wie der <a href="/de/breeds/british-shorthair/" class="text-teal-600 hover:underline">Britisch Kurzhaar</a> bis zu seltenen Naturrassen wie der <a href="/de/breeds/sokoke/" class="text-teal-600 hover:underline">Sokoke</a>. Jedes Profil bewertet Zuneigung, Aktivität, Pflegeaufwand und Kinderfreundlichkeit. Unsicher? <a href="/de/quiz/" class="text-teal-600 hover:underline">Machen Sie das Rassen-Quiz</a> oder <a href="/de/compare/" class="text-teal-600 hover:underline">vergleichen Sie zwei Rassen</a>.',
        'filter_ph': 'Rassen nach Name oder Herkunft filtern…',
        'filters': [('all', 'Alle'), ('short', 'Kurzhaar'), ('long', 'Langhaar'), ('curly', 'Lockig & Drahthaar'), ('hairless', 'Haarlos')],
        'count': 'Rassen angezeigt', 'none': 'Keine Rasse passt zu diesem Filter.',
        'crumb_home': 'Startseite', 'crumb': 'Rassen',
        'years': 'Jahre',
    },
    'es': {
        'prefix': '/es', 'lifespan': 'Esperanza de vida', 'origin': 'Origen',
        'title': 'Las 74 razas de gatos de la A a la Z: lista completa | CatFinder',
        'desc': 'Las 74 razas de gatos, del Abisinio al York Chocolate, con origen, esperanza de vida y carácter de cada una. Filtra por tipo de pelaje y abre cualquier ficha.',
        'h1': 'Todas las razas de gatos de la A a la Z',
        'intro': 'CatFinder reúne <strong>74 razas de gatos</strong>, desde compañeros populares como el <a href="/es/breeds/british-shorthair/" class="text-teal-600 hover:underline">Británico de Pelo Corto</a> hasta razas naturales poco comunes como el <a href="/es/breeds/sokoke/" class="text-teal-600 hover:underline">Sokoke</a>. Cada ficha valora el cariño, la actividad, el aseo y la convivencia con niños. ¿No sabes por dónde empezar? <a href="/es/quiz/" class="text-teal-600 hover:underline">Haz el test de razas</a> o <a href="/es/compare/" class="text-teal-600 hover:underline">compara dos razas</a>.',
        'filter_ph': 'Filtrar razas por nombre u origen…',
        'filters': [('all', 'Todas'), ('short', 'Pelo corto'), ('long', 'Pelo largo'), ('curly', 'Rizado y duro'), ('hairless', 'Sin pelo')],
        'count': 'razas mostradas', 'none': 'Ninguna raza coincide con ese filtro.',
        'crumb_home': 'Inicio', 'crumb': 'Razas',
        'years': 'años',
    },
}


def fact(page, label):
    m = re.search(re.escape(label) + r'</p>\s*<p[^>]*>([^<]+)</p>', page)
    return m.group(1).strip() if m else ''


def main():
    data = json.load(open('data/breeds.json'))
    for lang, c in L.items():
        pre = c['prefix']
        d = pre.lstrip('/') + '/' if pre else ''
        cards = []
        items = []
        for b in data:
            slug = b['id']
            page = open(f'{d}breeds/{slug}/index.html').read()
            name = html.unescape(re.search(r'<h1[^>]*>\s*([^<]+?)\s*<', page).group(1))
            desc = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', page).group(1))
            origin = fact(page, c['origin'])
            life = fact(page, c['lifespan'])
            coat = COAT_GROUP.get(b['coat']['type'], 'short')
            url = f'{pre}/breeds/{slug}/'
            items.append((name, slug, url, desc, origin, life, coat))
        items.sort(key=lambda x: x[0].lower())
        for i, (name, slug, url, desc, origin, life, coat) in enumerate(items, 1):
            cards.append(f'''            <a href="{url}" data-coat="{coat}" data-q="{html.escape((name + ' ' + origin).lower())}" class="breed-item group bg-white rounded-2xl card-shadow border border-cream-300 overflow-hidden flex gap-4 p-4 hover:border-teal-300 transition">
                <img src="/images/heads/{slug}.webp" alt="{html.escape(name)}" width="72" height="72" loading="{'eager' if i <= 9 else 'lazy'}" class="w-[72px] h-[72px] rounded-xl object-cover object-top flex-shrink-0 bg-cream-200">
                <div class="min-w-0">
                    <h2 class="text-lg font-bold text-slate-900 group-hover:text-teal-600 transition leading-tight">{html.escape(name)}</h2>
                    <p class="text-xs text-slate-500 mb-1">{html.escape(origin)} &middot; {html.escape(life)}</p>
                    <p class="text-sm text-slate-600 line-clamp-2">{html.escape(desc)}</p>
                </div>
            </a>''')
        # header/footer from the Sokoke page of this language
        src = open(f'{d}breeds/sokoke/index.html').read()
        header = re.search(r'    <header.*?</header>', src, re.S).group(0)
        header = header.replace('/breeds/sokoke/"', '/breeds/"')
        footer = re.search(r'    <footer.*?</footer>', src, re.S).group(0)
        head_ga = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-8JVFQHMFD3"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","G-8JVFQHMFD3");</script>'
        canon = f'https://catfinder.app{pre}/breeds/'
        item_list = {
            '@context': 'https://schema.org', '@type': 'CollectionPage',
            'name': c['h1'], 'description': c['desc'], 'url': canon, 'inLanguage': lang,
            'dateModified': TODAY,
            'mainEntity': {
                '@type': 'ItemList', 'numberOfItems': len(items),
                'itemListElement': [
                    {'@type': 'ListItem', 'position': i, 'name': it[0], 'url': 'https://catfinder.app' + it[2]}
                    for i, it in enumerate(items, 1)
                ],
            },
        }
        crumbs = {
            '@context': 'https://schema.org', '@type': 'BreadcrumbList',
            'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': c['crumb_home'], 'item': f'https://catfinder.app{pre}/'},
                {'@type': 'ListItem', 'position': 2, 'name': c['crumb'], 'item': canon},
            ],
        }
        filters = ''.join(
            f'<button type="button" data-f="{k}" class="filter-btn px-4 py-2 rounded-full text-sm font-medium border transition {"bg-teal-500 text-white border-teal-500" if k == "all" else "bg-white text-slate-600 border-cream-400 hover:border-teal-300"}">{v}</button>'
            for k, v in c['filters'])
        out = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
{head_ga}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{c['title']}</title>
    <meta name="description" content="{html.escape(c['desc'])}">
    <link rel="canonical" href="{canon}">
    <link rel="alternate" hreflang="en" href="https://catfinder.app/breeds/">
    <link rel="alternate" hreflang="es" href="https://catfinder.app/es/breeds/">
    <link rel="alternate" hreflang="de" href="https://catfinder.app/de/breeds/">
    <link rel="alternate" hreflang="x-default" href="https://catfinder.app/breeds/">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="CatFinder">
    <meta property="og:title" content="{html.escape(c['h1'])}">
    <meta property="og:description" content="{html.escape(c['desc'])}">
    <meta property="og:url" content="{canon}">
    <meta property="og:image" content="https://catfinder.app/images/og-default.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://catfinder.app/images/og-default.jpg">
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="stylesheet" href="/css/tailwind.css">
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; }}
        h1, h2, h3 {{ font-family: 'Instrument Serif', Georgia, serif; }}
        .card-shadow {{ box-shadow: 0 1px 3px rgba(40,37,29,0.04), 0 4px 12px rgba(40,37,29,0.03); }}
        .line-clamp-2 {{ display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }}
    </style>
    <script type="application/ld+json">
{json.dumps(item_list, ensure_ascii=False, indent=2)}
    </script>
    <script type="application/ld+json">
{json.dumps(crumbs, ensure_ascii=False, indent=2)}
    </script>
</head>
<body class="bg-cream-100 min-h-screen text-slate-800">
{header}

    <main class="max-w-6xl mx-auto px-4 py-8">
        <nav class="text-sm text-slate-500 mb-6">
            <a href="{pre}/" class="hover:text-teal-600">{c['crumb_home']}</a>
            <span class="mx-2">/</span>
            <span class="text-slate-700">{c['crumb']}</span>
        </nav>

        <div class="mb-8 max-w-3xl">
            <h1 class="text-4xl md:text-5xl font-display text-slate-900 mb-4">{c['h1']}</h1>
            <p class="text-slate-600 leading-relaxed">{c['intro']}</p>
        </div>

        <div class="flex flex-col md:flex-row md:items-center gap-4 mb-6">
            <input id="breed-filter" type="search" placeholder="{c['filter_ph']}" aria-label="{c['filter_ph']}" class="w-full md:w-80 bg-white border border-cream-400 rounded-xl px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-teal-500/20 focus:border-teal-400">
            <div class="flex flex-wrap gap-2">{filters}</div>
        </div>
        <p class="text-sm text-slate-500 mb-4"><span id="breed-count">{len(items)}</span> {c['count']}</p>

        <div id="breed-grid" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-12">
{chr(10).join(cards)}
        </div>
        <p id="breed-none" class="hidden text-center text-slate-500 py-8">{c['none']}</p>
    </main>

{footer}
    <script>
        lucide.createIcons();
        (function () {{
            var input = document.getElementById('breed-filter');
            var btns = document.querySelectorAll('.filter-btn');
            var items = document.querySelectorAll('.breed-item');
            var coat = 'all';
            function apply() {{
                var q = input.value.trim().toLowerCase();
                var n = 0;
                items.forEach(function (el) {{
                    var ok = (coat === 'all' || el.dataset.coat.split(' ').indexOf(coat) > -1) && (!q || el.dataset.q.indexOf(q) > -1);
                    el.style.display = ok ? '' : 'none';
                    if (ok) n++;
                }});
                document.getElementById('breed-count').textContent = n;
                document.getElementById('breed-none').classList.toggle('hidden', n > 0);
            }}
            input.addEventListener('input', apply);
            btns.forEach(function (b) {{
                b.addEventListener('click', function () {{
                    coat = b.dataset.f;
                    btns.forEach(function (x) {{
                        var on = x === b;
                        x.classList.toggle('bg-teal-500', on); x.classList.toggle('text-white', on); x.classList.toggle('border-teal-500', on);
                        x.classList.toggle('bg-white', !on); x.classList.toggle('text-slate-600', !on); x.classList.toggle('border-cream-400', !on);
                    }});
                    apply();
                }});
            }});
        }})();
    </script>
</body>
</html>
'''
        os.makedirs(f'{d}breeds', exist_ok=True)
        open(f'{d}breeds/index.html', 'w').write(out)
        print(f'{d}breeds/index.html', len(items))


if __name__ == '__main__':
    main()
