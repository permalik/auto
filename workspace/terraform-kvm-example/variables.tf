variable "libvirt_disk_path" {
	description = "path for libvirt pool"
	default = "/opt/kvm/pool1"
}

variable "ubuntu_24_img_url" {
	description = "ubuntu 24.04 image"
	default = "http://cloud-images.ubuntu.com/releases/noble/release-20250327/ubuntu-24.04-server-cloudimg-amd64.img"
}

variable "vm_hostname" {
	description = "vm hostname"
	default = "terraform-kvm-ansible"
}

variable "ssh_username" {
	description = "the ssh user"
	default = "permalik"
}

variable "ssh_private_key" {
	description = "the private key"
	default = "/home/permalik/.ssh/id_rsa"
}
