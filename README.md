[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/jonjet155/news-image-20261119-v4a-vector/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/jonjet155/news-image-20261119-v4a-vector/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# news-image-20261119 — v4a rebuild, v4c vector style

One image summing up world news on Thursday 19 November 2026: 40 stories
(16 illustrated panels + 24 in the "ALSO ON" list), a 6-figure row, a
7-region bar, a labelled world map, a DATE CHECK strip and a sources line.

This is a rebuild of the v4a front page (the blind-judge winner of the v4
revision round, 6–2, splitting the #1 entry 1–1), restyled to v4c's flat
2D vector look on a warm cream paper page throughout (top-1 style): cream
header, dark title, gold pill stat chips, blue-pin map. The layout, panel
texts and list items are v4a's;
the art direction is v4c's.

## Build

```sh
python3 main.py   # copies entry.png to $MAKEFUN_OUTPUT_DIR (else /output)
```

The image was drawn in code with PIL on the build machine; `main.py`
itself is standard library only (the grader installs nothing) and only
delivers the finished `entry.png`. Re-running it writes byte-identical
output.

## Files

- `main.py` — the generator (entrypoint)
- `entry.png` — the entry image, 1024x1024
- `LICENSE` — MIT

## Sources

Reuters, AP, BBC, Al Jazeera, The Guardian, IMD, ABS, TechCrunch, PTI,
IANS — 19 November 2026.
