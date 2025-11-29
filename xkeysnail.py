#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# Define macOS-like keybindings using Super (Command) key
# Smart terminal handling: Ctrl+Shift+C/V in terminals, Ctrl+C/V elsewhere

# Terminal applications (use Ctrl+Shift+C/V for copy/paste to avoid Ctrl+C killing processes)
define_keymap(re.compile("Alacritty|kitty|konsole|gnome-terminal|terminator|xterm|urxvt"), {
    K("Super-c"): K("Ctrl-Shift-c"),  # Copy in terminal
    K("Super-v"): K("Ctrl-Shift-v"),  # Paste in terminal
}, "macOS-like keybindings - terminals")

# All other applications (use regular Ctrl shortcuts)
define_keymap(lambda wm_class: wm_class not in ["Alacritty", "kitty", "konsole", "gnome-terminal", "terminator", "xterm", "urxvt"], {
    # Core macOS shortcuts - Copy, Paste, Select All, Cut
    K("Super-c"): K("Ctrl-c"),
    K("Super-v"): K("Ctrl-v"),
    K("Super-a"): K("Ctrl-a"),
    K("Super-x"): K("Ctrl-x"),

    # Additional common macOS shortcuts
    K("Super-z"): K("Ctrl-z"),        # Undo
    K("Super-Shift-z"): K("Ctrl-Shift-z"),  # Redo
    K("Super-s"): K("Ctrl-s"),        # Save
    K("Super-t"): K("Ctrl-t"),        # New tab
    K("Super-n"): K("Ctrl-n"),        # New window
    K("Super-w"): K("Ctrl-w"),        # Close tab/window
    # Super+F and Super+Q left for i3 WM (fullscreen, kill window)
}, "macOS-like keybindings - non-terminals")
