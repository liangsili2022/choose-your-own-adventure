# Choose Your Own Adventure: The Lost Lighthouse

A small command-line choose-your-own-adventure game written in Python (standard library only).

Stranded on a stormy island, you pick your path by number. There are two winning endings and two losing ones.

## Run it

```bash
python3 adventure.py
```

Type the number of a choice and press Enter. Type `q` to quit.

## How it works

The story lives in the `STORY` dictionary in `adventure.py`. Each scene has text and either a set of
numbered choices pointing to other scenes, or `end: True`. To add content, add new scenes and link them.

---

*Built for the MLH Global Hack Week "Build a simple application" challenge. This code was written with an AI assistant (Grok Bot), not GitHub Copilot.*
