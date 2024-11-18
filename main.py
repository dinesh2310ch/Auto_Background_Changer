
import os
import random
import time
import platform
import subprocess
import threading
import atexit


# Function to change wallpaper
def change_background(image_path):
    system = platform.system()

    if system == "Linux":
        set_linux_background(image_path)
    elif system == "Darwin":  # macOS
        set_mac_background(image_path)
    elif system == "Windows":
        set_windows_background(image_path)


def set_linux_background(image_path):
    """Set desktop background on Linux."""
    try:
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri",
                        f"file://{image_path}"], check=True)
    except subprocess.CalledProcessError:
        subprocess.run(["feh", "--bg-scale", image_path])


def set_mac_background(image_path):
    """Set desktop background on macOS."""
    applescript = f"""
    tell application "System Events"
        set desktop picture to POSIX file "{image_path}"
    end tell
    """
    subprocess.run(["osascript", "-e", applescript])


def set_windows_background(image_path):
    """Set desktop background on Windows."""
    import ctypes
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)


def get_images_from_folder(folder_path):
    """Load images from the provided folder."""
    image_list = []
    for file in os.listdir(folder_path):
        if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
            image_list.append(os.path.join(folder_path, file))
    return image_list


def run_wallpaper_changer(folder_path, interval=5):
    """Run the wallpaper changer in the background every interval seconds."""
    image_list = get_images_from_folder(folder_path)

    if not image_list:
        print("No images found in the folder.")
        return

    while True:
        random_image_path = random.choice(image_list)
        print(f"Changing background to {random_image_path}")
        change_background(random_image_path)
        time.sleep(interval)


def start_background_process(folder_path):
    """Start the wallpaper changer as a background process."""
    if platform.system() == "Windows":
        # On Windows, run as background process using threading
        wallpaper_thread = threading.Thread(target=run_wallpaper_changer, args=(folder_path,))
        wallpaper_thread.daemon = True
        wallpaper_thread.start()
    else:
        # On Linux/macOS, use daemon library to run the process in background
        import daemon
        with daemon.DaemonContext():
            atexit.register(cleanup)
            run_wallpaper_changer(folder_path)


def cleanup():
    """Function to clean up before quitting."""
    print("Cleanup before quitting")


def main():
    # Ask user for folder path
    folder_path = input("Enter the folder path containing images: ")
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    print("Starting background process...")
    start_background_process(folder_path)


if __name__ == "__main__":
    main()