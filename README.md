# Auto Wallpaper Changer

## Description
The **Auto Wallpaper Changer** is a Python tool that automatically changes your desktop wallpaper by randomly selecting images from a specified folder. It works across **Linux**, **macOS**, and **Windows**, and can run in the background at a customizable interval. Ideal for users who want a dynamic desktop experience with minimal effort.


file:///home/himan/Videos/Screencasts/Screencast%20from%2018-11-24%2004:01:44%20PM%20IST.webm


## How to Run the Script

### Clone or Download the Repository:
You can download this script as a `.zip` file or clone it using Git:

```bash
git clone https://github.com/yourusername/wallpaper-changer.git
cd wallpaper-changer


### Run the Script:
1. **Open a terminal or command prompt**.
2. Navigate to the directory where the script is located.
3. Run the script using Python:

python3 wallpaper_changer.py
pip install python-daemon


### Provide Folder Path:
When prompted, enter the full path to the folder containing your images. For example:

Enter the folder path containing images: /path/to/your/images


The script will start changing the wallpaper at a default interval of **5 seconds**. You can modify this interval by editing the script if desired.

---

## Stopping the Wallpaper Changer

The wallpaper changer script runs in the background (as a daemon process on **Linux/macOS** or using a thread on **Windows**). To stop the script, you can use the following methods based on your operating system.

### Stopping the Process via Terminal:

#### **Linux/macOS**:

1. **Find the Process ID (PID)**:
   - Open a terminal and run this command to find the PID of the running wallpaper changer script:

     ```bash
     ps aux | grep wallpaper_changer.py
     ```

   - This will list all processes related to the script. The **PID** is the number in the second column.

   Example output:
   ```bash
   user     12345  0.2  0.1  123456  7890 ?        S    10:00   0:01 python3 wallpaper_changer.py
   user     12346  0.0  0.0  123456  7890 pts/0    S+   10:00   0:00 grep --color=auto wallpaper_changer.py
   ```
   In this case, `12345` is the **PID** of the script.

2. **Kill the Process**:
   - Use the `kill` command to stop the script by its PID:

     ```bash
     kill 12345
     ```

   - Replace `12345` with the actual PID from the previous step.
   
   - If the process doesn't stop, you can forcefully kill it using:

     ```bash
     kill -9 12345
     ```

#### **Windows**:

1. **Using Task Manager**:
   - Press **Ctrl + Shift + Esc** to open **Task Manager**.
   - Look for the running Python process (either `python.exe` or `pythonw.exe`) that is running the wallpaper changer script.
   - Right-click on the Python process and select **End Task**.

2. **Using Command Prompt (if you know the PID)**:
   - If you know the PID of the Python process (e.g., `12345`), you can stop it directly from the command prompt by running:

     ```bash
     taskkill /PID 12345
     ```

   - Replace `12345` with the actual PID.

### Using `Ctrl+C` (For Non-Daemon Mode):
If the script is running in the foreground (not as a background process or daemon), you can stop it by simply pressing **Ctrl+C** in the terminal or command prompt.

Example:
- When you run the script with:

  ```bash
  python wallpaper_changer.py
  ```

  It will display output in the terminal, and you can stop it by pressing **Ctrl+C**.

---

## Notes:
- On **Linux**, you may need to install additional dependencies like **feh** or use **gsettings** (if running a GNOME desktop).
- Ensure the image folder contains only valid image formats (e.g., `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`).
- The script will loop continuously, changing wallpapers at the specified interval until it is stopped manually.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### How to Use:
1. **Download/Clone the Repository**: Users can either clone or download your repository.
2. **Run the Script**: Users are guided through running the script and providing the path to their image folder.
3. **Stop the Script**: Instructions are provided on how to stop the script on various operating systems, including methods for both background and foreground processes.

This markdown file is now complete for a `README.md` and ready to be added to your GitHub repository. It provides a comprehensive guide for installation, usage, and troubleshooting.
