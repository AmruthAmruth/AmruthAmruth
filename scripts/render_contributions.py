#!/usr/bin/env python3
"""Draw the last year of contributions as a dark calendar with a vivid scale."""

import json
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

USERNAME = "AmruthAmruth"
OUT = Path(__file__).resolve().parents[1] / "assets" / "contributions.svg"

# Empty days sit in the background. Every real contribution is a clear purple.
COLORS = {
    0: "#21262d",
    1: "#6d28d9",
    2: "#8b5cf6",
    3: "#c4b5fd",
    4: "#f5d0fe",
}
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
LABEL = "#9ca3af"


def load_days():
    url = f"https://github-contributions-api.jogruber.de/v4/{USERNAME}?y=last"
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = json.load(response)
    return payload["contributions"], payload["total"]["lastYear"]


def render(contributions, total):
    by_date = {item["date"]: item for item in contributions}
    first = datetime.fromisoformat(contributions[0]["date"])
    last = datetime.fromisoformat(contributions[-1]["date"])
    start = first - timedelta(days=(first.weekday() + 1) % 7)

    columns = []
    cursor = start
    while cursor <= last:
        week = []
        for _ in range(7):
            key = cursor.strftime("%Y-%m-%d")
            week.append(by_date.get(key))
            cursor += timedelta(days=1)
        columns.append(week)

    cell = 12
    gap = 3
    step = cell + gap
    left = 32
    top = 22
    width = left + len(columns) * step + 8
    height = top + 7 * step + 28

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">',
        f"<title>{total} contributions in the last year</title>",
        f'<rect width="100%" height="100%" rx="12" fill="#0d1117"/>',
    ]

    last_month = None
    last_label_x = -999
    for index, week in enumerate(columns):
        x = left + index * step
        for row, day in enumerate(week):
            if day is None:
                continue
            current = datetime.fromisoformat(day["date"])
            if row == 0 or current.day == 1:
                if current.month != last_month and x - last_label_x > step * 2:
                    parts.append(
                        f'<text x="{x}" y="14" fill="{LABEL}" font-family="Segoe UI, sans-serif" font-size="12">{MONTHS[current.month - 1]}</text>'
                    )
                    last_month = current.month
                    last_label_x = x
            y = top + row * step
            color = COLORS[day["level"]]
            parts.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{color}">'
                f"<title>{day['date']}: {day['count']} contributions</title></rect>"
            )

    parts.append(snake_markup(columns, left, top, cell, step))

    for row, name in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        y = top + row * step + 10
        parts.append(
            f'<text x="0" y="{y}" fill="{LABEL}" font-family="Segoe UI, sans-serif" font-size="11">{name}</text>'
        )

    legend_x = width - 168
    legend_y = height - 16
    parts.append(
        f'<text x="{legend_x}" y="{legend_y}" fill="{LABEL}" font-family="Segoe UI, sans-serif" font-size="12">Less</text>'
    )
    for level in range(5):
        x = legend_x + 36 + level * (cell + 3)
        parts.append(
            f'<rect x="{x}" y="{legend_y - 10}" width="{cell}" height="{cell}" rx="2" fill="{COLORS[level]}"/>'
        )
    parts.append(
        f'<text x="{legend_x + 36 + 5 * (cell + 3) + 4}" y="{legend_y}" fill="{LABEL}" font-family="Segoe UI, sans-serif" font-size="12">More</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def snake_markup(columns, left, top, cell, step):
    """A short snake that crawls every cell of the calendar and then loops."""
    points = []
    for index, week in enumerate(columns):
        rows = range(7) if index % 2 == 0 else range(6, -1, -1)
        for row in rows:
            if week[row] is None:
                continue
            points.append((left + index * step + cell / 2, top + row * step + cell / 2))
    if len(points) < 2:
        return ""

    last = len(points) - 1
    frames = "".join(
        f"{100 * i / last:.4f}%{{transform:translate({x:.1f}px,{y:.1f}px)}}"
        for i, (x, y) in enumerate(points)
    )
    duration = 20
    gap = duration / last
    segments = 16
    rules = "".join(f".s{i}{{animation-delay:{-i * gap:.4f}s}}" for i in range(segments))
    style = (
        "<style>"
        f"@keyframes crawl{{{frames}}}"
        f".snake{{animation:crawl {duration}s linear infinite;transform-box:fill-box;transform-origin:center}}"
        f"{rules}</style>"
    )
    body = []
    for i in range(segments - 1, 0, -1):
        body.append(
            f'<circle class="snake s{i}" cx="0" cy="0" r="4.1" fill="#e0e7ff"/>'
        )
    head = (
        '<g class="snake s0">'
        '<circle cx="0" cy="0" r="5.4" fill="#ffffff"/>'
        '<circle cx="1.8" cy="-1.5" r="1.15" fill="#312e81"/>'
        '<circle cx="1.8" cy="1.5" r="1.15" fill="#312e81"/>'
        "</g>"
    )
    return style + "\n" + "\n".join(body) + "\n" + head


def main():
    contributions, total = load_days()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(contributions, total), encoding="utf-8")
    print(f"wrote {OUT} ({total} contributions)")


if __name__ == "__main__":
    main()
