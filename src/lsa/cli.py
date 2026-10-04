"""Command-line entry point: `uv run lsa <command>`."""

from __future__ import annotations

import argparse


def _not_implemented(_args: argparse.Namespace) -> None:
    print("not implemented")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="lsa")
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name in ("count", "estimate"):
        sub.add_parser(name).set_defaults(func=_not_implemented)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
