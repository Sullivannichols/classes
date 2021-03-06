# ArchLinux Installation on Netbook


## Base Install
### Setup LiveInstall USB/CD
* Download the ArchLinux ISO from a verified source and verify the image sig
* Install the ISO to the boot device (USB or CD) using Rufus or DD
* Boot machine from the new boot device

### Setup Partitions
* Once booted into the ArchLinux LiveInstall, create the partitions on the
destination system.
* View the connected storage devices with `lsblk`
* Run parted on the harddrive associated with the system.
  * `parted /dev/sdX` where X is the letter of the block device
* Create a partition table with msdos
  * `mklabel msdos`
* Now create partitions as needed
  * Syntax: `mkpart part-type fs-type start end`
  * Swap: `mkpart primary linux-swap 1MiB 4GiB`
  * Root: `mkpart primary ext4 4GiB 30GiB`
  * Home: `mkpart primary ext4 30GiB 100%`
* Set boot flag for root partition
  * `set 1 boot on`
* Exit parted with `quit`, then format, setup, and mount partitions
  * `mkswap /dev/sdxY` where x = block device, y = swap partition
  * 'swapon /dev/sdxY` where x = block device, y = swap partition
  * `mkfs.ext4 /dev/sdxY` where x = block device, y = root partition
  * `mkfs.ext4 /dev/sdxY` where x = block device, y = home partition
  * `mount /dev/sdxY /mnt` where x = block device, y = root partition
  * `mkdir /mnt/home`
  * `mount /dev/sdxY /mnt/home` where x = block device, y = home partition

### Connect to the internet
* Simply plug in ethernet cable and test connection with `ping`
* If using wireless...
  * Use `ip link` to get devices
  * Use `wifi-menu -o <devicename>` to open network selector

### Install the System
* Select the closest mirror for downloads
  * `vi /etc/pacman.d/mirrorlist`
  * Move the closest mirror to the top of the file
* Begin installation
  * `pacstrap -i /mnt base`
* Once all packages are installed, generate the fstab file.
  * `genfstab -U /mnt > /mnt/etc/fstab`
  * Run this ONLY ONCE.
* Root into the new system and edit configuration files.
  * `arch-chroot /mnt /bin/bash`
  * Select language
    * `vi /etc/locale/gen`
    * Uncomment entries for US English
    * `locale-gen`
    * `echo LANG=en_US.UTF-8 > /etc/locale.conf`
    * `export LANG=en_US.UTF-8`
  * Select timezone & clock
    * View available zones: `ls /usr/share/zoneinfo`
    * View subzones: `ls /usr/share/zoneinfo/America`
    * Select a zone: `ln -s /usr/share/zoneinfo/<zone>/<subzone>
    * Set clock with `hwclock --systohc --utc`

### Setup the Network
* For wifi, install the necessary packages with pacman.
  * `pacman -S wireless_tools wpa_supplicant wpa_actiond dialog`
  * Now to connect to network, simply use `wifi-menu`

### Configure Package Manager
* If necessary, add repos to pacman by editing /etc/pacman.conf
* After changing this config, reload with `pacman -Sy`

### Setup Users
* Change root password
  * `passwd`
* Create user account
  * `useradd -m -g users -G wheel,storage,power -s /bin/bash <username>`
  * `passwd <username>`
* Install sudo
  * `pacman -S sudo`
  * `EDITOR=vi visudo`
  * Uncomment `%wheel ALL=(ALL) ALL`

### Install Bootloader (GRUB)
* Install GRUB
  * `pacman -S grub-bios`
  * `grub-install --target=i386-pc --recheck /dev/sdX` where x = block device
  * `grub-mkconfig -o /boot/grub/grub.cfg`

### Setup Hostname
* `echo <hostname> > /etc/hostname`

### Exit LiveInstall
* Exit chroot environment: `exit`
* Umount the partitions
  * `umount -R /mnt`
* Shutdown: `shutdown now`
* Remove boot device, boot into new system, and begin system configuration.

## Configuration
### Environment Setup
* Remove unecessary packages
  * `sudo pacman -Rs nano vi s-nail`
* Install desired packages
  * `sudo pacman -S git vim acpi python3 pip`
* Install python libraries with pip
  * `sudo pip3 install pyyaml`
* Get environment settings
  * `git clone https://github.com/brandonrandle/.env ~/.env`
  * Run `~/.env/setup.sh` to setup basic settings
  * Run `~/.env/net_setup.sh` to setup netbook specific settings
* Fix keybindings
  * Use `sudo loadkeys ./ctrl-caps-swap.map` to fix control key (add this to the
 setup script)
  * Also add to setup script the xorg keybindings

### Xorg Setup
* Install required packages
  * `sudo pacman -S xorg-server xorg-init xterm <xif86stuff>`
* Create .xinitrc and add necessary commands
  * `exec xterm -geometry 170x46+0+0`
