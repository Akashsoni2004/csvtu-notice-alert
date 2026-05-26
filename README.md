# CSVTU Notice Alert

An automated GitHub Actions bot that monitors the [CSVTU (Chhattisgarh Swami Vivekanand Technical University)](https://csvtu.ac.in/ew/notices/) notices page and sends an email alert whenever a new notice is published.

---

## Features

- Automatically scrapes the CSVTU notices page
- Sends email alerts to multiple recipients (To + CC)
- Runs on a scheduled interval via GitHub Actions
- Tracks the last seen notice to avoid duplicate alerts
- Credentials stored securely as GitHub Secrets

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core scripting language |
| `requests` | Fetching the notices webpage |
| `BeautifulSoup4` | Parsing HTML to extract notices |
| `smtplib` | Sending emails via Gmail SMTP |
| GitHub Actions | Scheduling and automation |

---

## Project Structure

```
csvtu-notice-alert/
│
├── main.py              # Main script — scrapes notices and sends email
├── last_notice.txt      # Stores the ID of the last seen notice (auto-generated)
└── .github/
    └── workflows/
        └── notice.yml   # GitHub Actions workflow file
```

---

## Setup & Configuration

### 1. Fork or Clone the Repository

```bash
git clone https://github.com/your-username/csvtu-notice-alert.git
cd csvtu-notice-alert
```

### 2. Set Up Gmail App Password

> Regular Gmail passwords won't work. You need a Google App Password.

1. Enable **2-Step Verification** on your Google account
2. Go to **Google Account → Security → App Passwords**
3. Generate a new App Password for "Mail"
4. Copy the 16-character password (**without spaces**)

### 3. Add GitHub Secrets

Go to your repository → **Settings → Secrets and variables → Actions → New repository secret**

| Secret Name | Value |
|-------------|-------|
| `EMAIL` | Your Gmail address (e.g. `yourname@gmail.com`) |
| `PASSWORD` | Your 16-character App Password (**no spaces**) |

### 4. Configure Recipients

Edit `main.py` to update the email recipients:

```python
to_email = ["your-email@gmail.com"]
cc_email = [
    "friend1@gmail.com",
    "friend2@gmail.com"
]
```

---

## GitHub Actions Workflow

The workflow is defined in `.github/workflows/notice.yml` and runs automatically on a schedule.

> You can adjust the `cron` schedule to check more or less frequently.

---

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│                   GitHub Actions (Cron)                 │
└──────────────────────────┬──────────────────────────────┘
                           │ Triggers on schedule
                           ▼
┌─────────────────────────────────────────────────────────┐
│              Fetch CSVTU Notices Page                   │
│         https://csvtu.ac.in/ew/notices/                 │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│         Parse HTML → Extract Latest Notice ID           │
└──────────────────────────┬──────────────────────────────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
     Same as last_notice.txt?     New notice found!
              │                         │
     No email sent               Send email alert
     Print "No new notice."      Update last_notice.txt
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## Author

Made by **Akash Kumar Soni**  
📧 akashkrsoni2004@gmail.com  
🎓 CSVTU Student Project
