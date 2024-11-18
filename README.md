# Wallpaper Changer Script

This Python script changes your desktop wallpaper at a specified interval by selecting random images from a given folder. It supports **Linux**, **macOS**, and **Windows** operating systems.

## Features
- Automatically changes the desktop wallpaper from a folder of images.
- Runs in the background (daemon process) for continuous wallpaper changes.
- Customizable interval for wallpaper changes.
  
## Prerequisites
Before running the script, ensure you have the following dependencies installed based on your operating system.

### Dependencies
1. **Python 3.x**: This script requires Python 3 to run. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

2. **Linux**: 
   - `gsettings` (for GNOME desktops)
   - `feh` (fallback option for setting backgrounds in case `gsettings` fails)
   - Install using the following:
     ```bash
     sudo apt install gsettings feh
     ```

3. **macOS**: No additional dependencies required. The script uses `osascript` (built-in macOS tool) to change the wallpaper.

4. **Windows**: No additional dependencies required. The script uses `ctypes` to interact with Windows API to set the wallpaper.

### Optional: Daemon Library (Linux/macOS)
On **Linux** or **macOS**, the script uses the `daemon` library to run in the background as a daemon. Install it via `pip` if you haven't already:

```bash
pip install python-daemon
