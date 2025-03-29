# main.py
"""
auto
"""

import argparse

from config.adhoc import init_ssh


def main():
    # Initialize Parser and Subparser
    parser = argparse.ArgumentParser(description="auto CLI")
    subparsers = parser.add_subparsers(
        dest="category", required=True, help="Select a Category"
    )

    # Category Selection
    # Configuration
    config_parser = subparsers.add_parser("cfg", help="Configuration Programs")
    config_subparsers = config_parser.add_subparsers(dest="program", required=True)

    # Adhoc: : Init SSH
    init_ssh_parser = config_subparsers.add_parser(
        "init_ssh", help="Create Local SSH Key"
    )
    init_ssh_parser.add_argument(
        "-e", "--email", type=int, help="Email for SSH Key", required=True
    )
    init_ssh_parser.set_defaults(func=init_ssh)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
