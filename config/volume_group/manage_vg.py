import subprocess

view_size = ["sudo", "vgdisplay"]
extend_lv_by_gb = ["sudo", "lvextend", "-L", "+5G", "/dev/mapper/ubuntu--vg-ubuntu--lv"]
extend_lv_max = [
    "sudo",
    "lvextend",
    "-L",
    "+100%FREE",
    "/dev/mapper/ubuntu--vg-ubuntu--lv",
]
ext4_resize = ["sudo", "resize2fs", "/dev/mapper/ubuntu--vg-ubuntu--lv"]
xfs_resize = ["sudo", "xfs_growfs", "/"]
