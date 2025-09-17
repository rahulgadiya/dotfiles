# Essential packages
sudo pacman -S hyprland kitty thunar waybar rofi-wayland mako

# Iosevka font
sudo pacman -S ttf-iosevka-nerd

# Additional fonts for better compatibility
sudo pacman -S ttf-dejavu ttf-liberation noto-fonts noto-fonts-emoji

# Icons and themes
sudo pacman -S papirus-icon-theme arc-gtk-theme

# Wayland essentials
sudo pacman -S wayland xorg-xwayland cliphist

# Screenshots and screen recording
sudo pacman -S grim slurp  wf-recorder

# Color temperature
sudo pacman -S wlsunset

sudo pacman -S pipewire pipewire-alsa pipewire-pulse pipewire-jack wireplumber
sudo pacman -S pavucontrol pamixer

bash# File manager enhancements
sudo pacman -S thunar-volman thunar-archive-plugin thunar-media-tags-plugin
sudo pacman -S gvfs gvfs-mtp gvfs-gphoto2 # for mounting drives

# Archive support
sudo pacman -S file-roller unzip unrar p7zip

# Image viewer
sudo pacman -S imv

# PDF viewer
sudo pacman -S zathura zathura-pdf-mupdf


# System info for waybar
sudo pacman -S htop 

# Brightness control
sudo pacman -S brightnessctl

# Authentication agent
sudo pacman -S polkit-gnome

# Enable essential services
#sudo systemctl enable NetworkManager
#sudo systemctl enable bluetooth
sudo systemctl enable tlp
sudo systemctl enable mbpfan
sudo systemctl enable auto-cpufreq

# User services
systemctl --user enable pipewire pipewire-pulse

