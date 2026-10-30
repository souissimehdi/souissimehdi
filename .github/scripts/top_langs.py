"""Generate top-langs.svg from the public repos of a GitHub user (stdlib only)."""
import json
import os
import sys
import urllib.request

USER = sys.argv[1] if len(sys.argv) > 1 else "souissimehdi"
OUT = sys.argv[2] if len(sys.argv) > 2 else "top-langs.svg"
TOP = 6
COLORS = {"Java": "#b07219", "HTML": "#e34c26", "Python": "#3572A5", "JavaScript": "#f1e05a",
          "TypeScript": "#3178c6", "Shell": "#89e051", "Dockerfile": "#384d54", "CSS": "#563d7c"}


def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


totals = {}
for repo in get(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner"):
    if repo["fork"]:
        continue
    for lang, size in get(repo["languages_url"]).items():
        totals[lang] = totals.get(lang, 0) + size

langs = sorted(totals.items(), key=lambda kv: -kv[1])[:TOP]
total = sum(s for _, s in langs) or 1
W, BAR_X, BAR_W = 300, 25, 250
H = 55 + 25 + 20 * ((len(langs) + 1) // 2) + 15
p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
     "font-family=\"'Segoe UI',Ubuntu,Sans-Serif\">",
     f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="4.5" fill="#0d1117"/>',
     '<text x="25" y="35" font-size="18" font-weight="600" fill="#6DB33F">Most Used Languages</text>',
     f'<clipPath id="c"><rect x="{BAR_X}" y="55" width="{BAR_W}" height="8" rx="4"/></clipPath><g clip-path="url(#c)">']
x = BAR_X
for lang, size in langs:
    w = BAR_W * size / total
    p.append(f'<rect x="{x:.2f}" y="55" width="{w:.2f}" height="8" fill="{COLORS.get(lang, "#8b949e")}"/>')
    x += w
p.append("</g>")
for i, (lang, size) in enumerate(langs):
    cx, cy = 25 + (i % 2) * 130, 88 + (i // 2) * 20
    p.append(f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{COLORS.get(lang, "#8b949e")}"/>'
             f'<text x="{cx + 15}" y="{cy}" font-size="11" fill="#c3d1d9">{lang} {100 * size / total:.2f}%</text>')
p.append("</svg>")
open(OUT, "w", encoding="utf-8").write(chr(10).join(p))
print(f"wrote {OUT}: " + ", ".join(f"{l} {100 * s / total:.1f}%" for l, s in langs))
