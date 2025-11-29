# i3 Window Manager Configuration

Personal i3WM configuration with macOS-like keyboard shortcuts for Arch Linux.

## Features

- **i3 Window Manager** configuration with autotiling
- **macOS-like keyboard shortcuts** (Command/Super key mappings)
- **Centralized configuration** - everything in one place
- **Rofi** launcher integration
- **Custom gaps** and smart borders

## Keyboard Shortcuts

### macOS-style Shortcuts (via xkeysnail)
- `Super+C` - Copy (Ctrl+C)
- `Super+V` - Paste (Ctrl+V)
- `Super+A` - Select All (Ctrl+A)
- `Super+X` - Cut (Ctrl+X)
- `Super+Z` - Undo
- `Super+Shift+Z` - Redo
- `Super+F` - Find
- `Super+S` - Save
- `Super+T` - New Tab
- `Super+N` - New Window
- `Super+W` - Close Tab/Window

### i3 Window Management
- `Super+Enter` - Open terminal (Alacritty)
- `Super+Q` - Kill focused window
- `Super+Space` - Rofi launcher
- `Super+h/j/k/l` - Vim-style navigation
- `Super+1-9` - Switch workspaces
- `Super+Shift+1-9` - Move window to workspace
- `Super+Shift+R` - Restart i3

## Installation

### Prerequisites

```bash
# Install required packages
sudo pacman -S i3-wm alacritty rofi autotiling-rs python-evdev python-xlib

# Install xkeysnail from AUR
paru -S xkeysnail
```

### Setup

1. **Clone this repository:**
   ```bash
   git clone git@github.com:delattre1/i3_config.git ~/.config/i3
   ```

2. **Set up sudo permissions for xkeysnail:**
   ```bash
   echo "$(whoami) ALL=(ALL) NOPASSWD: /usr/bin/xkeysnail" | sudo tee /etc/sudoers.d/xkeysnail
   sudo chmod 440 /etc/sudoers.d/xkeysnail
   ```

3. **Reload i3 configuration:**
   ```bash
   i3-msg reload
   # or restart i3
   i3-msg restart
   ```

4. **Verify xkeysnail is running:**
   ```bash
   ps aux | grep xkeysnail
   ```

## File Structure

```
~/.config/i3/
├── config          # i3 window manager configuration
├── xkeysnail.py    # macOS-like keyboard shortcuts
└── README.md       # This file
```

## Making Changes

### Update i3 Configuration

Edit `~/.config/i3/config` and reload i3:
```bash
# Edit config
vim ~/.config/i3/config

# Reload i3 (Super+Shift+R or)
i3-msg reload
```

### Update Keyboard Shortcuts

Edit `~/.config/i3/xkeysnail.py` and restart xkeysnail:
```bash
# Edit xkeysnail config
vim ~/.config/i3/xkeysnail.py

# Restart xkeysnail
sudo pkill -f xkeysnail
sudo xkeysnail ~/.config/i3/xkeysnail.py &
```

### Commit and Push Changes

```bash
cd ~/.config/i3
git add .
git commit -m "Description of changes"
git push
```

## Syncing to Another Machine

1. **Clone the repository:**
   ```bash
   git clone git@github.com:delattre1/i3_config.git ~/.config/i3
   ```

2. **Follow the setup steps above** (prerequisites and sudo permissions)

3. **Pull updates:**
   ```bash
   cd ~/.config/i3
   git pull
   i3-msg reload
   ```

## Customization

### Add More macOS-style Shortcuts

Edit `~/.config/i3/xkeysnail.py`:
```python
K("Super-r"): K("Ctrl-r"),  # Add reload shortcut
```

### Exclude Specific Apps from Remapping

Change `define_keymap(None, {` to:
```python
define_keymap(re.compile("App1|App2"), {
```

### Change i3 Keybindings

Edit `~/.config/i3/config` and modify the `bindsym` lines.

## Troubleshooting

### xkeysnail not working
```bash
# Check if running
ps aux | grep xkeysnail

# Check logs
tail -f /tmp/xkeysnail.log

# Restart manually
sudo pkill -f xkeysnail
sudo xkeysnail ~/.config/i3/xkeysnail.py &
```

### Shortcuts conflicting with i3
Edit `xkeysnail.py` and comment out conflicting shortcuts, or change i3 keybindings.

## System Info

- **OS:** Garuda Linux (Arch-based)
- **WM:** i3
- **Terminal:** Alacritty
- **Launcher:** Rofi
- **Font:** Inter

## License

Personal configuration - feel free to use and modify.
