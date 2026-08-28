# 💱 Daily Exchange Rate Email Bot

A simple Python automation that fetches live USD exchange rates every morning and emails them straight to your inbox — no manual effort required.

Built as a hands-on foundations project for learning **APIs, environment variables, email automation, error handling, and task scheduling** — the core skills behind most real-world automation and AI-engineering pipelines.

---

## ✨ Features

- 🌍 Fetches **live exchange rates** (USD → GHS, EUR, GBP) via [exchangerate-api.com](https://www.exchangerate-api.com)
- 📧 Sends a clean daily summary email automatically via Gmail SMTP
- 🔐 Keeps API keys and passwords out of source code using environment variables
- 🛡️ Handles API and network failures gracefully instead of crashing
- ⏰ Runs fully unattended every morning via Windows Task Scheduler

---

## 🛠️ Tech Stack

- **Python 3.13**
- [`requests`](https://pypi.org/project/requests/) — API calls
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) — environment variable management
- `smtplib` / `email.message` — built-in Python email sending
- **Windows Task Scheduler** — daily automation trigger

---

## 📁 Project Structure

This project sits inside my broader `Python-Projects` repo:

```
Python-Projects/
├── .gitignore                   # Root-level, applies to all projects
├── LICENSE                      # Root-level, applies to all projects
├── README.md                    # Overview of all projects in this repo
├── Beginner - Password Generator.../
└── exchange-rate-script/        # ← You are here
    ├── test_api.py               # Main script: fetch rates + send email
    ├── .env                       # Local secrets (NOT committed — ignored via root .gitignore)
    └── README.md                  # This file
```

---

## 🚀 Getting Started

> 📂 This project lives as a subfolder inside my [Python-Projects](https://github.com/PkayAddison/Python-Projects) repo, alongside my other beginner projects.

### 1. Clone the repo and navigate to this project
```bash
git clone https://github.com/PkayAddison/Python-Projects.git
cd Python-Projects/exchange-rate-script
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.\.venv\Scripts\activate.ps1      # Windows PowerShell
```

### 3. Install dependencies
```bash
pip install requests python-dotenv
```

### 4. Get your API key
Sign up for a free key at [exchangerate-api.com](https://www.exchangerate-api.com).

### 5. Set up your Gmail App Password
This script sends email via Gmail SMTP, which requires an **App Password** (not your regular Gmail password):
1. Enable **2-Step Verification** on your Google Account.
2. Generate an App Password at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

### 6. Configure your environment variables
Create a `.env` file in the project root:

```env
EXCHANGE_API_KEY=your_exchangerate_api_key
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_APP_PASSWORD=your_16_char_app_password
```

> ⚠️ Never commit your `.env` file. It's already listed in `.gitignore`.

### 7. Run it
```bash
python test_api.py
```
You should receive an email with the current exchange rates within a few seconds.

---

## ⏰ Automating It (Windows Task Scheduler)

To have this run automatically every morning:

1. Open **Task Scheduler** → **Create Basic Task**.
2. Set a **Daily** trigger at your preferred time.
3. Action: **Start a program**, with:
   - **Program/script:** full path to your `.venv`'s `python.exe`, wrapped in quotes:
     ```
     "C:\path\to\project\.venv\Scripts\python.exe"
     ```
   - **Add arguments:** `test_api.py`
   - **Start in:** the project folder path, **without** quotes:
     ```
     C:\path\to\project
     ```

> 💡 **Note:** The `Start in` field must NOT be wrapped in quotes, even though `Program/script` must be. Adding quotes there will cause a `0x8007010B` ("directory name is invalid") error. This one tripped me up — worth knowing if you're setting this up yourself.

---

## 🧯 Error Handling

The script catches and reports two categories of failure instead of crashing silently:
- **API/network issues** (`requests.exceptions.RequestException`)
- **Email/connection issues** (`smtplib.SMTPException`, `OSError`)

If something fails, you'll get a clear console message indicating which part broke.

---

## 🗺️ Roadmap

- [x] Fetch live exchange rates via API
- [x] Parse and extract specific currencies
- [x] Secure secrets with environment variables
- [x] Send results via email
- [x] Add error handling
- [x] Automate with Task Scheduler
- [ ] **Stretch goal:** Add an LLM-generated commentary line summarizing the day's rate movement

---

## 📄 License

This project is part of the `Python-Projects` repo and is covered under the [MIT License](../LICENSE) at the repo root.

---

## 🙋 About

Built by Paa Kwesi as a foundations project on the path to AI engineering — learning how APIs, automation, and secure credential handling work together in a real, end-to-end pipeline.
