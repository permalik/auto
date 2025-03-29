import subprocess


def init_cc():
    update_apt = ["sudo", "apt", "update"]
    install_qemu_kvm = ["sudo", "apt", "install", "-y", "qemu-kvm"]
    install_libvirt = ["sudo", "apt", "install", "-y", "libvirt-bin"]
    install_bridge_utils = ["sudo", "apt", "install", "-y", "bridge-utils"]
    install_virt_manager = ["sudo", "apt", "install", "-y", "virt-manager"]

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
        subprocess.run(install_libvirt, check=True)
        print("Success: LIBVIRT Installed")
    except subprocess.CalledProcessError as e:
        print(f"Failure: LIBVIRT Not Installed\n{e}")

    try:
        subprocess.run(install_bridge_utils, check=True)
        print("Success: BRIDGE_UTILS Installed")
    except subprocess.CalledProcessError as e:
        print(f"Failure: BRIDGE_UTILS Not Installed\n{e}")

    try:
        subprocess.run(install_virt_manager, check=True)
        print("Success: VIRT_MANAGER Installed")
    except subprocess.CalledProcessError as e:
        print(f"Failure: VIRT_MANAGER Not Installed\n{e}")
