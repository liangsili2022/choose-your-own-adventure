#!/usr/bin/env python3
"""The Lost Lighthouse - a tiny choose-your-own-adventure game for the terminal."""

import sys

STORY = {
    "start": {
        "text": "A storm drives your boat onto a rocky island. Ahead stands a dark lighthouse; "
                "to the left, a cave glows faintly.",
        "choices": {"1": ("Climb to the lighthouse", "lighthouse"),
                    "2": ("Explore the glowing cave", "cave")},
    },
    "lighthouse": {
        "text": "The door creaks open. A spiral staircase rises into darkness, and a trapdoor sits at your feet.",
        "choices": {"1": ("Climb the stairs", "lamp_room"),
                    "2": ("Open the trapdoor", "cellar")},
    },
    "lamp_room": {
        "text": "At the top, the great lamp is cold. A box of matches lies on the floor.",
        "choices": {"1": ("Light the lamp", "win_rescue"),
                    "2": ("Pocket the matches and head back down", "cellar")},
    },
    "cellar": {
        "text": "The cellar is flooded to your knees. Something shiny rests on a shelf, and the water is rising.",
        "choices": {"1": ("Grab the shiny object", "lose_flood"),
                    "2": ("Run back up immediately", "lamp_room")},
    },
    "cave": {
        "text": "The glow comes from luminous mushrooms. A narrow tunnel continues, and an old map is pinned to the wall.",
        "choices": {"1": ("Follow the tunnel", "lose_lost"),
                    "2": ("Study the map", "map")},
    },
    "map": {
        "text": "The map marks a hidden dock on the far side of the island with a sturdy rowboat.",
        "choices": {"1": ("Head for the hidden dock", "win_dock"),
                    "2": ("Ignore it and go to the lighthouse", "lighthouse")},
    },
    "win_rescue": {"text": "The beam sweeps across the sea. By dawn a ship arrives to rescue you. YOU WIN!", "end": True},
    "win_dock": {"text": "You row away as the storm clears and reach the mainland by sunset. YOU WIN!", "end": True},
    "lose_flood": {"text": "It's just a tin can - and the stairs are now underwater. GAME OVER.", "end": True},
    "lose_lost": {"text": "The tunnel twists endlessly until your light fades. GAME OVER.", "end": True},
}


def play(input_fn=input, output_fn=print):
    """Run one playthrough. Returns the id of the ending scene."""
    scene_id = "start"
    while True:
        scene = STORY[scene_id]
        output_fn("\n" + scene["text"])
        if scene.get("end"):
            return scene_id
        for key, (label, _) in scene["choices"].items():
            output_fn(f"  {key}) {label}")
        choice = input_fn("> ").strip().lower()
        if choice in ("q", "quit"):
            output_fn("Thanks for playing!")
            return None
        if choice not in scene["choices"]:
            output_fn("Please choose one of the listed numbers (or q to quit).")
            continue
        scene_id = scene["choices"][choice][1]


def main():
    print("=== The Lost Lighthouse ===")
    try:
        while True:
            if play() is None:
                break
            if input("\nPlay again? (y/n) ").strip().lower() != "y":
                print("Thanks for playing!")
                break
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
