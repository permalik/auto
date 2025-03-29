import subprocess


def init_cc():
    update_apt = ["sudo", "apt-get", "update"]
    install_qemu_kvm = ["sudo", "apt-get", "install", "-y", "qemu-kvm"]
    install_libvirt_system = [
        "sudo",
        "apt-get",
        "install",
        "-y",
        "libvirt-daemon-system",
    ]
    install_libvirt_clients = ["sudo", "apt-get", "install", "-y", "libvirt-clients"]
    install_bridge_utils = ["sudo", "apt-get", "install", "-y", "bridge-utils"]

    try:
        subprocess.run(update_apt, check=True)
        print("Success: APT Updated")
    except subprocess.CalledProcessError as e:
        print(f"Failure: APT Not Updated\n{e}")

    try:
        subprocess.run(install_qemu_kvm, check=True)
        print("Success: QEMU Installed")
    except subprocess.CalledProcessError as e:
        print(f"Failure: QEMU Not Installe\n{e}")

    try:
        subprocess.run(install_libvirt_system, check=True)
        print("Success: LIBVIRT System Installed")
    except subprocess.CalledProcessError as e:
        print(f"Failure: LIBVIRT System Not Installed\n{e}")

    try:
        subprocess.run(install_libvirt_clients, check=True)
        print("Success: LIBVIRT Clients Installed")
    except subprocess.CalledProcessError as e:
        print(f"Failure: LIBVIRT Clients Not Installed\n{e}")

    try:
        subprocess.run(install_bridge_utils, check=True)
        print("Success: BRIDGE_UTILS Installed")
    except subprocess.CalledProcessError as e:
        print(f"Failure: BRIDGE_UTILS Not Installed\n{e}")
