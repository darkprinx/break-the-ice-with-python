"""Build the day cards, stage banners and Day page navigation.

Run from anywhere:  python3 scripts/build_days.py

- Writes assets/days/stage-N.svg and assets/days/day-NN.svg (used by README.md).
- Rewrites the navigation blocks between the <!-- day-nav:... --> markers in
  every Status/Day page. Safe to run as often as you like.

To change a topic, a colour or add a day, edit STAGES / DAYS below and re-run.
The README grid itself is plain HTML, so a new day also needs a card added there.
"""
import os
import re
from xml.sax.saxutils import escape

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_DIR = os.path.join(REPO, "assets", "days")
STATUS_DIR = os.path.join(REPO, "Status")

FONT = "-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"

# (name, blurb, gradient start, gradient end); each stage covers 6 days
STAGES = [
    ("Warm-up", "Loops, strings, input and your first class", "#1a7f37", "#116329"),
    ("Functions & data", "Functions, dicts, tuples, map and filter", "#0969da", "#0550ae"),
    ("Classes, errors & modules", "OOP, exceptions, regex, recursion, random", "#8250df", "#6639ba"),
    ("Challenge mode", "Bigger problems that mix everything", "#bc4c00", "#953800"),
]
DAYS_PER_STAGE = 6

# (first question, last question, topic) per day
DAYS = [
    (1, 3, "Loops, factorial & dicts"),
    (4, 9, "Input parsing & classes"),
    (10, 13, "Sorting words & binary"),
    (14, 15, "Counting letters & digits"),
    (16, 17, "Comprehensions & bank log"),
    (18, 19, "Password check & sorting"),
    (20, 21, "Generators & robot moves"),
    (22, 25, "Word frequency & docs"),
    (26, 30, "Your first functions"),
    (31, 37, "Dicts & lists in functions"),
    (38, 43, "Tuples, map & filter"),
    (44, 46, "Static methods & subclasses"),
    (47, 50, "Classes & exceptions"),
    (51, 53, "try/except & regex"),
    (54, 59, "Regex, unicode & series"),
    (60, 64, "Recursion & Fibonacci"),
    (65, 69, "assert, eval & binary search"),
    (70, 74, "The random module"),
    (75, 79, "zlib, timeit & shuffle"),
    (80, 84, "List comprehension filters"),
    (85, 89, "Sets, sorting & inheritance"),
    (90, 94, "Permutations & a puzzle"),
    (95, 99, "Rangoli, dates & sets"),
    (100, 103, "Word counts & recursion"),
]

CARD_W, CARD_H = 240, 100
BANNER_W, BANNER_H = 728, 44

# Old "go to previous/next day" links, in any of the bold/italic styles used
OLD_NAV_LINK = re.compile(r"^\[\*\*\*?_?go to (previous|next) day_?\*\*\*?\]\(.*\)\s*$")


# ---------- cards ----------

def gradient(start, end):
    return (
        '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/>'
        "</linearGradient></defs>" % (start, end)
    )


def card(day, first, last, topic, start, end):
    count = last - first + 1
    pill = "Q %d–%d" % (first, last)
    pill_w = 7 * len(pill) + 16
    return """<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  {grad}
  <rect width="{w}" height="{h}" rx="12" fill="url(#g)"/>
  <text x="{wm_x}" y="95" text-anchor="end" font-family="{font}" font-size="44" font-weight="800" fill="#ffffff" fill-opacity="0.12">{day:02d}</text>
  <text x="18" y="36" font-family="{font}" font-size="22" font-weight="700" fill="#ffffff">Day {day}</text>
  <rect x="{pill_x}" y="18" width="{pill_w}" height="22" rx="11" fill="#ffffff" fill-opacity="0.22"/>
  <text x="{pill_cx}" y="33" text-anchor="middle" font-family="{font}" font-size="11" font-weight="700" fill="#ffffff">{pill}</text>
  <text x="18" y="63" font-family="{font}" font-size="13" fill="#ffffff">{topic}</text>
  <text x="18" y="86" font-family="{font}" font-size="11" font-weight="600" fill="#ffffff" fill-opacity="0.85">{count} questions  ·  Solve →</text>
</svg>
""".format(
        w=CARD_W, h=CARD_H, grad=gradient(start, end), font=FONT, day=day,
        wm_x=CARD_W - 14, pill=pill, pill_w=pill_w, pill_x=CARD_W - 18 - pill_w,
        pill_cx=CARD_W - 18 - pill_w / 2.0, topic=escape(topic), count=count,
    )


def banner(n, name, blurb, first_day, last_day, start, end):
    return """<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  {grad}
  <rect width="{w}" height="{h}" rx="10" fill="url(#g)"/>
  <text x="18" y="28" font-family="{font}" font-size="15" font-weight="800" fill="#ffffff">STAGE {n}  ·  {name}</text>
  <text x="{rx}" y="28" text-anchor="end" font-family="{font}" font-size="12" fill="#ffffff" fill-opacity="0.9">{blurb}  ·  Days {a}–{b}</text>
</svg>
""".format(
        w=BANNER_W, h=BANNER_H, grad=gradient(start, end), font=FONT, n=n,
        name=escape(name.upper()), blurb=escape(blurb), a=first_day, b=last_day,
        rx=BANNER_W - 18,
    )


def build_cards():
    os.makedirs(CARDS_DIR, exist_ok=True)
    for i, (name, blurb, start, end) in enumerate(STAGES):
        first_day = i * DAYS_PER_STAGE + 1
        last_day = first_day + DAYS_PER_STAGE - 1
        write_text(os.path.join(CARDS_DIR, "stage-%d.svg" % (i + 1)),
                   banner(i + 1, name, blurb, first_day, last_day, start, end))
        for day in range(first_day, last_day + 1):
            first, last, topic = DAYS[day - 1]
            write_text(os.path.join(CARDS_DIR, "day-%02d.svg" % day),
                       card(day, first, last, topic, start, end))


# ---------- Day page navigation ----------

def page_file(day):
    return "Day %d.md" % day if day < 10 else "Day_%d.md" % day


def page_link(day):
    return page_file(day).replace(" ", "%20")


def top_nav(day):
    parts = []
    if day > 1:
        parts.append('<a href="%s">← Day %d</a>' % (page_link(day - 1), day - 1))
    parts.append('<a href="../README.md#days">All 24 days</a>')
    if day < len(DAYS):
        parts.append('<a href="%s">Day %d →</a>' % (page_link(day + 1), day + 1))
    return ['<p align="center">%s</p>' % " &nbsp;·&nbsp; ".join(parts)]


def bottom_nav(day):
    lines = ['<p align="center">']
    if day < len(DAYS):
        first, last, topic = DAYS[day]
        lines += [
            "<sub><b>UP NEXT</b></sub><br>",
            '<a href="%s"><img src="../assets/days/day-%02d.svg" width="240" alt="Day %d, questions %d to %d: %s"></a><br>'
            % (page_link(day + 1), day + 1, day + 1, first, last, escape(topic)),
        ]
    else:
        lines.append("🎉 <b>You finished all %d days!</b> Share your own solutions in the discussion below.<br>" % len(DAYS))
    links = []
    if day > 1:
        links.append('<a href="%s">← Day %d</a>' % (page_link(day - 1), day - 1))
    links.append('<a href="../README.md#days">All 24 days</a>')
    lines += [" &nbsp;·&nbsp; ".join(links), "</p>"]
    return lines


def set_block(lines, name, block, default_at):
    """Replace the lines between <!-- day-nav:name --> markers, or insert them at default_at."""
    start, end = "<!-- day-nav:%s -->" % name, "<!-- /day-nav:%s -->" % name
    wrapped = [start] + block + [end]
    if start in lines:
        i, j = lines.index(start), lines.index(end)
        return lines[:i] + wrapped + lines[j + 1:]
    return lines[:default_at] + wrapped + [""] + lines[default_at:]


def drop_old_links(lines):
    """Remove the old previous/next links (and the blank line after each). Returns (lines, first index)."""
    out, first = [], None
    skip_blank = False
    for line in lines:
        if OLD_NAV_LINK.match(line):
            if first is None:
                first = len(out)
            skip_blank = True
            continue
        if skip_blank and line.strip() == "":
            skip_blank = False
            continue
        skip_blank = False
        out.append(line)
    return out, first


def build_nav():
    for day in range(1, len(DAYS) + 1):
        path = os.path.join(STATUS_DIR, page_file(day))
        with open(path, "rb") as f:
            raw = f.read().decode("utf-8")
        newline = "\r\n" if "\r\n" in raw else "\n"
        lines = raw.split(newline)

        # Top: below the sponsor slot comment, and below the sponsor line if the slot is sold
        if "<!-- day-nav:top -->" in lines:
            at = 0
        else:
            at = next(i for i, l in enumerate(lines) if l.rstrip().endswith("-->")) + 1
            if lines[at].startswith('<p align="right">'):
                at += 1
            while lines[at].strip() == "":
                at += 1
        lines = set_block(lines, "top", top_nav(day), at)

        # Bottom: where the old previous/next links were, else before the Discussion link
        lines, at = drop_old_links(lines)
        if at is None and "<!-- day-nav:bottom -->" not in lines:
            at = next(i for i, l in enumerate(lines) if "Discussion" in l and l.startswith("["))
        lines = set_block(lines, "bottom", bottom_nav(day), at or 0)

        with open(path, "wb") as f:
            f.write(newline.join(lines).encode("utf-8"))


def write_text(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    build_cards()
    build_nav()
    print("Built %d cards, %d banners and navigation for %d Day pages."
          % (len(DAYS), len(STAGES), len(DAYS)))
