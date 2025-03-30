import subprocess


def init_cc():
    shutdown_vm = ["sudo", "virsh", "shutdown", "vm-name"]
    destroy_vm = ["sudo", "virsh", "destroy", "vm-name"]
    undefine_vm = ["sudo", "virsh", "undefine", "vm-name"]
    diskpath_vm = ["sudo", "virsh", "domblklist", "vm-name"]

    try:
        subprocess.run(shutdown_vm, check=True)
        print("Success: VM Shutdown")
    except subprocess.CalledProcessError as e:
        print(f"Failure: VM Not Shutdown\n{e}")

    try:
        subprocess.run(destroy_vm, check=True)
        print("Success: VM Destroyed")
    except subprocess.CalledProcessError as e:
        print(f"Failure: VM Not Destroyed\n{e}")

    try:
        subprocess.run(undefine_vm, check=True)
        print(f"Failure: VM Undefined")
    except subprocess.CalledProcessError as e:
        print(f"Failure: VM Not Undefined\n{e}")

    try:
        subprocess.run(diskpath_vm, check=True)
        print(f"Failure: Diskpaths Listed")
    except subprocess.CalledProcessError as e:
        print(f"Failure: Diskpaths Not Listed\n{e}")
