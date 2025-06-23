import subprocess


def ssh_local_to_remote(args):
    command = [
        "ssh-copy-id",
        "-i",
        "~/.ssh/id_ed25519.pub",
        f"{args.username}@{args.remote}",
    ]
    try:
        subprocess.run(command, check=True)
        print("Success: SSH copied")
    except subprocess.CalledProcessError as e:
        print(f"Failed: SSH not copied\n{e}")
