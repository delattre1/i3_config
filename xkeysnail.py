#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# Define macOS-like keybindings using Super (Command) key for ALL applications
# Note: Some i3 WM keybindings may be overridden (like Super+Q, Super+W)
# Adjust as needed in your i3 config to use different keys for WM functions

define_keymap(None, {
    # Core macOS shortcuts - Copy, Paste, Select All, Cut
    K("Super-c"): K("Ctrl-c"),
    K("Super-v"): K("Ctrl-v"),
    K("Super-a"): K("Ctrl-a"),
    K("Super-x"): K("Ctrl-x"),

    # Additional common macOS shortcuts
    K("Super-z"): K("Ctrl-z"),        # Undo
    K("Super-Shift-z"): K("Ctrl-Shift-z"),  # Redo
    K("Super-f"): K("Ctrl-f"),        # Find
    K("Super-s"): K("Ctrl-s"),        # Save
    K("Super-t"): K("Ctrl-t"),        # New tab
    K("Super-n"): K("Ctrl-n"),        # New window
    K("Super-w"): K("Ctrl-w"),        # Close tab/window
    # Super+Q left for i3 WM (kill window)
}, "macOS-like keybindings - system wide")
