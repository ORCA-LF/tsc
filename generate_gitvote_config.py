#!/usr/bin/env python3
"""Generate .gitvote.yml recusal profiles from the ORCA TSC roster.

Reads tsc.yml (roster + settings) and writes .gitvote.yml containing a
default profile plus one profile per plausible recusal combination.

Usage:
    python3 generate_gitvote_config.py
    python3 generate_gitvote_config.py --check    # CI: fail if out of date
"""

import argparse
import sys
from itertools import combinations
from pathlib import Path

import yaml

ROSTER = Path("tsc.yml")
OUTPUT = Path(".gitvote.yml")

DEFAULTS = {
    "duration": "2 weeks",
    "pass_threshold": 51,
    "periodic_status_check": "5 days",
    "max_recusals": 2,
    "min_binding_voters": 3,
    "audit": True,
    "close_on_passing": False,
}


def load_roster(path):
    """Read and validate the roster file."""
    with open(path) as fh:
        data = yaml.safe_load(fh)

    members = data.get("members") or []
    if not members:
        sys.exit(f"error: {path} defines no members")

    lowered = [m.lower() for m in members]
    dupes = {m for m in lowered if lowered.count(m) > 1}
    if dupes:
        sys.exit(f"error: duplicate handles in roster: {', '.join(sorted(dupes))}")

    for m in members:
        if not m or not all(c.isalnum() or c == "-" for c in m):
            sys.exit(f"error: '{m}' is not a valid GitHub handle")

    settings = {**DEFAULTS, **(data.get("settings") or {})}
    return sorted(members, key=str.lower), settings


def profile_name(recused):
    """Deterministic profile name for a set of recused members."""
    return "recused-" + "-".join(sorted(recused, key=str.lower))


def build_profiles(members, settings):
    """Yield (name, allowed_voters, recused) for every profile to emit."""
    yield "default", members, []

    max_recusals = settings["max_recusals"]
    floor = settings["min_binding_voters"]

    for n in range(1, max_recusals + 1):
        if len(members) - n < floor:
            break
        for recused in combinations(members, n):
            allowed = [m for m in members if m not in recused]
            yield profile_name(recused), allowed, list(recused)


def render(members, settings):
    """Render the full .gitvote.yml as text."""
    profiles = list(build_profiles(members, settings))
    psc = settings["periodic_status_check"]
    psc_val = "null" if psc in (None, "null") else f'"{psc}"'

    out = [
        "---",
        "# ============================================================",
        "# GENERATED FILE — DO NOT EDIT BY HAND",
        "#",
        "# Source of truth: tsc.yml",
        "# Regenerate with: python3 generate_gitvote_config.py",
        "#",
        f"# Roster ({len(members)} members): {', '.join(members)}",
        f"# Profiles: {len(profiles)} "
        f"(1 default + {len(profiles) - 1} recusal)",
        "# ============================================================",
        "",
        f"audit:\n  enabled: {str(settings['audit']).lower()}",
        "",
        "automation:",
        "  enabled: false",
        "  rules:",
        "    - patterns: []",
        "      profile: default",
        "",
        "profiles:",
    ]

    for name, allowed, recused in profiles:
        if recused:
            header = f"Recused: {', '.join(recused)}  ->  /vote-{name}"
        else:
            header = "No conflicts, full TSC  ->  /vote"

        out += [
            f"  # {header}",
            f"  # Binding voters: {len(allowed)}",
            f"  {name}:",
            f"    duration: {settings['duration']}",
            f"    pass_threshold: {settings['pass_threshold']}",
            f"    periodic_status_check: {psc_val}",
            f"    close_on_passing: {str(settings['close_on_passing']).lower()}",
            "    allowed_voters:",
            "      users:",
        ]
        out += [f"        - {u}" for u in allowed]
        out.append("")

    return "\n".join(out).rstrip() + "\n"


def command_table(members, settings):
    """Human-readable cheat sheet of which command to run."""
    rows = ["| Conflicted members | Command | Binding voters |",
            "| --- | --- | --- |"]
    for name, allowed, recused in build_profiles(members, settings):
        who = ", ".join(recused) if recused else "none"
        cmd = "/vote" if name == "default" else f"/vote-{name}"
        rows.append(f"| {who} | `{cmd}` | {len(allowed)} |")
    return "\n".join(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--roster", default=ROSTER, type=Path)
    ap.add_argument("--output", default=OUTPUT, type=Path)
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if output is out of date")
    ap.add_argument("--table", action="store_true",
                    help="print the command cheat sheet instead")
    args = ap.parse_args()

    members, settings = load_roster(args.roster)
    rendered = render(members, settings)

    if args.table:
        print(command_table(members, settings))
        return

    if args.check:
        current = args.output.read_text() if args.output.exists() else ""
        if current != rendered:
            sys.exit(f"error: {args.output} is out of date — "
                     "run generate_gitvote_config.py and commit the result")
        print(f"{args.output} is up to date")
        return

    args.output.write_text(rendered)
    n = rendered.count("    allowed_voters:")
    print(f"wrote {args.output}: {n} profiles from {len(members)} members")


if __name__ == "__main__":
    main()
