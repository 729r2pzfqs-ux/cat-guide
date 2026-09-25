#!/usr/bin/env python3
"""Add 3-5 contextual internal links to the Overview/Health/Care text of every
breed page (en/de/es). Idempotent: paragraphs that already contain links are
left alone. Edits HTML in place (pages carry hand-added JSON-LD, so they must
not be regenerated)."""
import glob
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.chdir(ROOT)

LINK = '<a href="{href}" class="text-teal-600 hover:underline">{text}</a>'
MAX_LINKS = 5
MIN_LINKS = 3
# Breed names that are also places/peoples, so plain-text matches are unreliable
AMBIGUOUS = {'asian', 'cyprus', 'thai', 'serengeti'}

LANGS = {
    'en': {
        'prefix': '',
        'topics': [
            (r'hypoallergenic|allerg\w*', '/articles/hypoallergenic-cats/'),
            (r'apartments?', '/articles/best-cats-for-apartments/'),
            (r'children|kids|famil(?:y|ies)', '/articles/best-cats-for-families/'),
            (r'seniors?|older (?:people|owners|adults)', '/articles/best-cats-for-seniors/'),
            (r'low[- ]maintenance|minimal grooming', '/articles/low-maintenance-cats/'),
        ],
        'also': 'If the {name} appeals to you, also consider the {links}, or <a href="/compare/" class="text-teal-600 hover:underline">compare breeds side by side</a>.',
        'and': ' and ',
    },
    'de': {
        'prefix': '/de',
        'topics': [
            (r'hypoallergen\w*|Allergi\w*', '/de/articles/hypoallergenic-cats/'),
            (r'Wohnungs?\w*', '/de/articles/best-cats-for-apartments/'),
            (r'Kinder\w*|Familien?\w*', '/de/articles/best-cats-for-families/'),
        ],
        'also': 'Wenn Ihnen die Rasse {name} gefällt, sehen Sie sich auch {links} an oder <a href="/de/compare/" class="text-teal-600 hover:underline">vergleichen Sie Rassen direkt</a>.',
        'and': ' und ',
    },
    'es': {
        'prefix': '/es',
        'topics': [
            (r'hipoalerg\w*|alerg\w*', '/es/articles/hypoallergenic-cats/'),
            (r'apartamentos?|pisos?', '/es/articles/best-cats-for-apartments/'),
            (r'niños|familias?', '/es/articles/best-cats-for-families/'),
        ],
        'also': 'Si te gusta la raza {name}, echa un vistazo también a {links}, o <a href="/es/compare/" class="text-teal-600 hover:underline">compara razas lado a lado</a>.',
        'and': ' y ',
    },
}


def h1_name(html):
    m = re.search(r'<h1[^>]*>\s*([^<]+?)\s*<', html)
    return m.group(1).strip() if m else None


def similar_slugs(slug):
    """Similar breeds as listed on the English page's 'Similar Breeds' section."""
    html = open(f'breeds/{slug}/index.html').read()
    sec = html.split('Similar Breeds', 1)
    if len(sec) < 2:
        return []
    return re.findall(r'<a href="/breeds/([a-z-]+)/" class="block bg-white', sec[1])


def link_text_segment(text, patterns, used, budget):
    """Link first occurrence of each pattern in a plain-text segment."""
    out = text
    for pat, href in patterns:
        if budget[0] <= 0:
            break
        if href in used:
            continue
        m = re.search(r'(?<![\w-])(' + pat + r')(?![\w-])', out)
        if not m:
            continue
        # never place a link inside another link we just inserted
        before = out[:m.start()]
        if before.count('<a ') > before.count('</a>'):
            continue
        out = out[:m.start()] + LINK.format(href=href, text=m.group(1)) + out[m.end():]
        used.add(href)
        budget[0] -= 1
    return out


def main():
    slugs = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob('breeds/*/index.html'))
    stats = {}
    for lang, cfg in LANGS.items():
        pre = cfg['prefix']
        names = {}
        for s in slugs:
            n = h1_name(open(f'{pre.lstrip("/") + "/" if pre else ""}breeds/{s}/index.html').read())
            if n:
                names[s] = n
        counts = []
        for s in slugs:
            path = f'{pre.lstrip("/") + "/" if pre else ""}breeds/{s}/index.html'
            html = open(path).read()
            blocks = list(re.finditer(r'(<details.*?</summary>)(.*?)(</details>)', html, re.S))
            if not blocks or any('<a ' in b.group(2) for b in blocks):
                continue
            # candidate patterns: other breed names (longest first), then topics
            breed_pats = []
            for other, n in sorted(names.items(), key=lambda kv: -len(kv[1])):
                if other == s or other in AMBIGUOUS:
                    continue
                breed_pats.append((re.escape(n) + r'(?:s|n|es)?', f'{pre}/breeds/{other}/'))
            topic_pats = cfg['topics']
            used = {f'{pre}/breeds/{s}/'}
            budget = [MAX_LINKS]
            new_html = html
            offset = 0
            for b in blocks:
                body = b.group(2)

                def para(m):
                    segs = re.split(r'(<[^>]+>)', m.group(2))
                    for i, seg in enumerate(segs):
                        if seg.startswith('<') or not seg.strip():
                            continue
                        seg = link_text_segment(seg, breed_pats, used, budget)
                        seg = link_text_segment(seg, topic_pats, used, budget)
                        segs[i] = seg
                    return m.group(1) + ''.join(segs) + m.group(3)

                new_body = re.sub(r'(<p class="text-slate-600 leading-relaxed">)(.*?)(</p>)', para, body, flags=re.S)
                start, end = b.start(2) + offset, b.end(2) + offset
                new_html = new_html[:start] + new_body + new_html[end:]
                offset += len(new_body) - len(body)
            n_links = MAX_LINKS - budget[0]
            if n_links < MIN_LINKS:
                # append a "consider also" sentence to the last (Care) paragraph
                picks = [x for x in similar_slugs(s) if f'{pre}/breeds/{x}/' not in used and x in names]
                need = max(1, MIN_LINKS - n_links - 1)  # compare link counts as one
                picks = picks[:max(2, need)]
                if picks:
                    links = [LINK.format(href=f'{pre}/breeds/{x}/', text=names[x]) for x in picks]
                    joined = ', '.join(links[:-1]) + cfg['and'] + links[-1] if len(links) > 1 else links[0]
                    sentence = cfg['also'].format(name=names[s], links=joined)
                    last = list(re.finditer(r'</p>\s*</div>\s*</details>', new_html))[-1]
                    new_html = new_html[:last.start()] + ' ' + sentence + new_html[last.start():]
                    n_links += len(picks) + 1
            counts.append(n_links)
            if new_html != html:
                open(path, 'w').write(new_html)
        stats[lang] = (len(counts), min(counts) if counts else 0, max(counts) if counts else 0)
    for lang, (n, lo, hi) in stats.items():
        print(f'{lang}: {n} pages linked, {lo}-{hi} links each')


if __name__ == '__main__':
    main()
