# WiFi Password Recovery Tool (Windows)

A small Python script that retrieves the passwords of WiFi networks your Windows laptop has previously connected to and saved. It uses Windows' built-in `netsh` command under the hood, so it only works on Windows and only for networks whose credentials are already stored on that machine.

## What it does

The script:
1. Lists every saved WiFi profile on the computer (`netsh wlan show profiles`)
2. Loops through each profile and pulls its stored password in plain text (`netsh wlan show profile <name> key=clear`)
3. Prints out each network name alongside its password

## Why this is useful

- **Recovering a forgotten password** — if you know a device is already connected to a WiFi network but you don't remember the password (e.g. to share it with a guest or set up a new device), this pulls it straight from Windows' saved profile.
- **Migrating to a new device** — quickly get a list of all your saved networks and their passwords before switching laptops.
- **Auditing your own saved networks** — see exactly which networks your machine remembers and has stored credentials for, which is useful for general digital hygiene (e.g. removing old/unused networks).
- **Learning project** — it's a good beginner-friendly example of using Python's `subprocess` module to interact with system command-line tools and `re` to parse their output.

## Project Structure

```
wifi-password-tool/
├── wifi_password.py      # main script
├── wifi_password.spec    # PyInstaller build config
├── dist/                 # contains the built .exe (after building)
├── build/                # PyInstaller intermediate files
└── .venv/                # local virtual environment
```

> **Note:** The `dist/` folder is kept in this repo so the `.exe` is available to download and run directly — no Python installation required. `build/` and `.venv/` are excluded via `.gitignore` since they're just local build cache and environment files with no use to anyone else.

Suggested `.gitignore`:
```
.venv/
build/
__pycache__/
*.pyc
```

## Requirements

- Windows OS (relies on `netsh`, which is Windows-only)
- Python 3.x
- The script must be run from an account with sufficient privileges — some profiles may return "Access Denied" otherwise

## Usage

**Option 1 — Run the Python script directly**

```bash
python wifi_password.py
```

**Option 2 — Run the standalone executable**

A pre-built `.exe` is included in this repo at `dist/wifi_password.exe` (built using [PyInstaller](https://pyinstaller.org/)), so you can download and run it on a Windows machine without needing Python installed at all. Just download `dist/wifi_password.exe`, then double-click it, or run it from a terminal:

```bash
dist\wifi_password.exe
```

Either way, the program will print each saved network name and its password, then wait for you to press Enter before closing.

> **Heads up:** Because this tool extracts saved WiFi passwords, some browsers and antivirus programs may flag `wifi_password.exe` as suspicious or block the download. This is a common false positive for PyInstaller-built executables that read credentials — not a sign the file is unsafe. If you're cautious, you can run the Python script directly instead (Option 1), or inspect `wifi_password.py` yourself before building/running it.

### Building the executable yourself

If you want to rebuild the `.exe` from source:

```bash
pip install pyinstaller
pyinstaller wifi_password.spec
```

The output will be placed in the `dist/` folder.

## ⚠️ Responsible Use — Please Read

This tool only reveals WiFi passwords that are **already saved on the computer it's run on** — it does not hack, crack, or intercept anything, and it cannot retrieve passwords for networks you haven't connected to.

That said, please use it responsibly:

- **Only run this on your own computer**, or on a device you have explicit permission to access.
- **Do not use this to access someone else's saved WiFi credentials without their consent.** Running this on a shared, work, school, or borrowed computer to extract passwords that aren't yours is a violation of privacy and, depending on your location, may be illegal.
- **Do not use this to gain unauthorized access to networks.**

This project is shared **for educational purposes only** — to demonstrate how Windows stores network credentials and how Python can interact with system utilities. The author is not responsible for any misuse of this script.

## Disclaimer

This software is provided "as is", without warranty of any kind. Use it at your own risk and in accordance with all applicable laws.
