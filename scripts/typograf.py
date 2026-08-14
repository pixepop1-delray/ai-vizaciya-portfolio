# -*- coding: utf-8 -*-
"""Типограф по Ководству (§62): неразрывные пробелы после коротких предлогов
и союзов, частицы к предыдущему слову, число+слово, пробел перед тире.
Обрабатывает только текстовые узлы HTML (script/style/атрибуты не трогает)."""
import re, sys

NBSP = " "

SHORTS = ("в во и а о об у с со к ко не ни но на по за до из изо от та то те "
          "же да для при под над без про или как что").split()
SHORTS_RE = re.compile(
    r'(?:(?<=^)|(?<=[\s(«"' + NBSP + r']))(' +
    "|".join(sorted({w for w in SHORTS} | {w.capitalize() for w in SHORTS}, key=len, reverse=True)) +
    r') (?=\S)')
PARTICLES_RE = re.compile(r'(\S) (бы|ли|же|б|ль)(?=[\s.,!?…)»])')
NUM_WORD_RE = re.compile(r'(\d) (?=[А-Яа-яЁёA-Za-z$€])')
DASH_RE = re.compile(r'(\S) —')

def typo_text(t):
    if not t.strip():
        return t
    for _ in range(2):  # цепочки «и в о»
        t = SHORTS_RE.sub(lambda m: m.group(1) + NBSP, t)
    t = PARTICLES_RE.sub(lambda m: m.group(1) + NBSP + m.group(2), t)
    t = NUM_WORD_RE.sub(lambda m: m.group(1) + NBSP, t)
    t = DASH_RE.sub(lambda m: m.group(1) + NBSP + "—", t)
    return t

def typo_html(src):
    parts = re.split(r'(<[^>]+>)', src)
    out, skip = [], 0
    for p in parts:
        if p.startswith("<"):
            low = p.lower()
            if low.startswith("<script") or low.startswith("<style"):
                skip += 1
            elif low.startswith("</script") or low.startswith("</style"):
                skip = max(0, skip - 1)
            out.append(p)
        else:
            out.append(p if skip else typo_text(p))
    return "".join(out)

def typo_md(src):
    lines = src.split("\n")
    out, in_fence, in_front = [], False, False
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            in_front = True; out.append(line); continue
        if in_front:
            out.append(line)
            if line.strip() == "---":
                in_front = False
            continue
        if line.strip().startswith("```"):
            in_fence = not in_fence; out.append(line); continue
        if in_fence:
            out.append(line); continue
        # куски в бэктиках не трогаем
        segs = re.split(r'(`[^`]*`)', line)
        segs = [s if s.startswith("`") else typo_text(s) for s in segs]
        out.append("".join(segs))
    return "\n".join(out)

if __name__ == "__main__":
    import glob
    ROOT = "/Users/uliana/Desktop/VIBE CODING/ai-vizaciya-portfolio"
    html_files = [ROOT + "/index.html", ROOT + "/about/index.html", ROOT + "/privacy/index.html"] + \
                 glob.glob(ROOT + "/cases/*/index.html")
    for f in html_files:
        src = open(f, encoding="utf-8").read()
        new = typo_html(src)
        open(f, "w", encoding="utf-8").write(new)
        print(f.split("ai-vizaciya-portfolio/")[-1], "nbsp:", new.count(NBSP) - src.count(NBSP), "добавлено")
    for f in sorted(glob.glob(ROOT + "/blog-src/src/content/posts/*.md")):
        src = open(f, encoding="utf-8").read()
        new = typo_md(src)
        open(f, "w", encoding="utf-8").write(new)
        print(f.split("posts/")[-1], "nbsp:", new.count(NBSP) - src.count(NBSP), "добавлено")
