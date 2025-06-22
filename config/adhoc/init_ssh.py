# init_ssh.py
import subprocess


def ssh_keygen(args):
    command = ["ssh-keygen", "-t", "ed25519", "-C", args.email]
    subprocess.run(command, check=True)
