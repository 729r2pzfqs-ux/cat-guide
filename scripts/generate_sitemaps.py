#!/usr/bin/env python3
"""Build per-language sitemaps (sitemap-en/es/de.xml) plus a sitemap index at
sitemap.xml. lastmod = date of the last git commit touching the page, or today
if the page has uncommitted changes. Skips noindex pages and redirect stubs."""
import datetime
import os
import re
import subprocess

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.chdir(ROOT)
BASE = 'https://catfinder.app'
TODAY = datetime.date.today().isoformat()

dirty = set(subprocess.check_output(['git', 'diff', '--name-only', 'HEAD']).decode().split())
dirty |= set(subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard']).decode().split())


def main_text(html):
    """Visible text of <main> (tags stripped), so header/nav-only edits
    such as a new language switcher don't count as content changes."""
    m = re.search(r'<main.*?</main>', html, re.S)
    t = re.sub(r'<script.*?</script>', '', m.group(0) if m else html, flags=re.S)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t)).strip()


def lastmod(path):
    if path in dirty:
        try:
            old = subprocess.check_output(['git', 'show', f'HEAD:{path}'], stderr=subprocess.DEVNULL).decode()
        except subprocess.CalledProcessError:
            return TODAY
        if main_text(old) != main_text(open(path, encoding='utf-8').read()):
            return TODAY
    out = subprocess.check_output(['git', 'log', '-1', '--format=%cs', '--', path]).decode().strip()
    return out or TODAY


pages = []
for dirpath, _, files in os.walk('.'):
    if '/.git' in dirpath or '/scripts' in dirpath:
        continue
    if 'index.html' not in files:
        continue
    path = os.path.join(dirpath, 'index.html')[2:]
    html = open(path, encoding='utf-8').read()
    if 'http-equiv="refresh"' in html or re.search(r'<meta name="robots" content="[^"]*noindex', html):
        continue
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    if not canon or not canon.group(1).startswith(BASE):
        continue
    lang = re.search(r'<html lang="(\w+)"', html).group(1)
    alts = re.findall(r'<link rel="alternate" hreflang="([\w-]+)" href="([^"]+)"', html)
    pages.append((lang, canon.group(1), lastmod(path), alts))

index = []
for lang in ('en', 'es', 'de'):
    rows = sorted(p for p in pages if p[0] == lang)
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for _, loc, mod, alts in rows:
        out.append('  <url>')
        out.append(f'    <loc>{loc}</loc>')
        out.append(f'    <lastmod>{mod}</lastmod>')
        if len(alts) > 1:
            for hl, href in alts:
                out.append(f'    <xhtml:link rel="alternate" hreflang="{hl}" href="{href}"/>')
        out.append('  </url>')
    out.append('</urlset>')
    fn = f'sitemap-{lang}.xml'
    open(fn, 'w').write('\n'.join(out) + '\n')
    index.append((fn, max(r[2] for r in rows)))
    print(fn, len(rows))

out = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for fn, mod in index:
    out += ['  <sitemap>', f'    <loc>{BASE}/{fn}</loc>', f'    <lastmod>{mod}</lastmod>', '  </sitemap>']
out.append('</sitemapindex>')
open('sitemap.xml', 'w').write('\n'.join(out) + '\n')
