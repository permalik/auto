import subprocess


def init_cc():
    install_qemu_kvm = ["sudo", "apt-get", "install", "-y", "qemu-kvm"]
    install_libvirt_system = [
        "sudo",
        "apt-get",
        "purge",
        "libvirt-daemon-system",
    ]
    install_libvirt_clients = ["sudo", "apt-get", "purge", "libvirt-clients"]
    install_bridge_utils = ["sudo", "apt-get", "purge", "bridge-utils"]
    update_apt = ["sudo", "apt-get", "update"]

    try:
        subprocess.run(install_qemu_kvm, check=True)
        print("Success: QEMU Purged")
    except subprocess.CalledProcessError as e:
        print(f"Failure: QEMU Not Purged\n{e}")

    try:
        subprocess.run(install_libvirt_system, check=True)
        print("Success: LIBVIRT System Purged")
    except subprocess.CalledProcessError as e:
        print(f"Failure: LIBVIRT System Not Purged\n{e}")

    try:
        subprocess.run(install_libvirt_clients, check=True)
        print("Success: LIBVIRT Clients Purged")
    except subprocess.CalledProcessError as e:
        print(f"Failure: LIBVIRT Clients Not Purged\n{e}")

    try:
        subprocess.run(install_bridge_utils, check=True)
        print("Success: BRIDGE_UTILS Purged")
    except subprocess.CalledProcessError as e:
        print(f"Failure: BRIDGE_UTILS Not Purged\n{e}")

    try:
        subprocess.run(update_apt, check=True)
        print("Success: APT Updated")
    except subprocess.CalledProcessError as e:
        print(f"Failure: APT Not Updated\n{e}")
