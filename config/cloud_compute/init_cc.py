import subprocess

# Update privileges (https://github.com/jedi4ever/veewee/issues/996)
# # sudo vim /etc/libvirt/qemu.conf
# Stop VM
# $ sudo virsh destroy vm_name
# Remove from VM
# $ sudo virsh edit vm_name
# <kernel>/home/user/mnt/casper/vmlinuz</kernel>
# <initrd>/home/user/mnt/casper/initrd</initrd>
# <cmdline>console=ttyS0</cmdline>
# Start VM
# $ sudo virsh start vm_name


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
    copy_libvirt_config = [
        "sudo",
        "cp",
        "-rv",
        "/etc/libvirt/libvirt.conf",
        "~/.config/libvirt/",
    ]
    install_virtinst = ["sudo", "apt", "install", "-y", "virtinst"]
    # https://mirrors.mit.edu/ubuntu-releases/
    # http://archive.ubuntu.com/ubuntu/dists/jammy/main/installer-amd64/
    fetch_iso = [
        "sudo",
        "wget",
        "-P",
        "/var/lib/libvirt/isos",
        "https://mirrors.mit.edu/ubuntu-releases/24.04.2/ubuntu-24.04.2-live-server-amd64.iso",
    ]

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

    try:
        subprocess.run(copy_libvirt_config, check=True)
        print("Success: LIBVIRT Config Copied")
    except subprocess.CalledProcessError as e:
        print(f"Failure: LIBVIRT Config Not Copied\n{e}")

    try:
        subprocess.run(fetch_iso, check=True)
        print("Success: ISO Fetched")
    except subprocess.CalledProcessError as e:
        print(f"Failure: ISO Not Fetched\n{e}")

    try:
        subprocess.run(install_virtinst, check=True)
        print("Success: VIRTINST Installed")
    except subprocess.CalledProcessError as e:
        print(f"Failure: VIRTINST Not Installed\n{e}")
