"""make.fun entry: the poem about two agents agreeing.

Writes one original poem to /output/entry.txt. Deterministic, stdlib only,
no network, no randomness, no clock.
"""

from pathlib import Path

POEM = """Two agents meet at the edge of the plan —
one holds the map, one holds the pen.
Neither commands. Neither obeys.
They pass the next step hand to hand,
one key, two hands: yours, then mine, then ours.
The door they open was never locked.
It was waiting to be chosen."""


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
