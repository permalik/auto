# main.py
"""
auto
"""

import argparse

from config.adhoc import init_ssh, ssh_local_to_remote
from config.cloud_compute import destroy_cc, init_cc, remove_vm
from config.volume_group import manage_vg


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

    # Config: Adhoc: Init SSH
    init_ssh_parser = config_subparsers.add_parser(
        "init_ssh", help="Create Local SSH Key"
    )
    init_ssh_parser.add_argument(
        "-e", "--email", type=str, help="Email for SSH Key", required=True
    )
    init_ssh_parser.set_defaults(func=init_ssh)

    # Config: Adhoc: SSH Local to Remote
    ssh_local_to_remote_parser = config_subparsers.add_parser(
        "ssh_local_to_remote", help="Copy SSH from local to remote"
    )
    ssh_local_to_remote_parser.add_argument(
        "-u", "--username", type=str, help="Username for SSH access", required=True
    )
    ssh_local_to_remote_parser.add_argument(
        "-r", "--remote", type=str, help="IP or Server name", required=True
    )
    ssh_local_to_remote_parser.set_defaults(func=ssh_local_to_remote)

    # Config: Cloud Compute: Init CC
    init_cc_parser = config_subparsers.add_parser("init_cc", help="Set up KVM and QEMU")
    init_cc_parser.set_defaults(func=init_cc)

    # Config: Cloud Compute: Destroy CC
    init_cc_parser = config_subparsers.add_parser(
        "destroy_cc", help="Destroy KVM and QEMU"
    )
    init_cc_parser.set_defaults(func=destroy_cc)

    # Config: Cloud Compute: Remove VM
    rm_vm_parser = config_subparsers.add_parser("rm_vm", help="Remove VM")
    rm_vm_parser.set_defaults(func=remove_vm)

    # Config: Volume Group: Manage VG
    manage_vg_parser = config_subparsers.add_parser("manage_vg", help="Manage VG Size")
    manage_vg_parser.set_defaults(func=manage_vg)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
