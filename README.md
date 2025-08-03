# VulnScan

**VulnScan** is a lightweight Python CLI tool for detecting common web application vulnerabilities, including **Cross-Site Scripting (XSS)** and **SQL Injection (SQLi)**. It can scan URLs and HTML forms for potential weaknesses by injecting payloads and analyzing the response for reflections or error patterns.

---

## 🚀 Features

- ✅ Detects reflected **XSS** vulnerabilities
- ✅ Detects basic **SQLi** via error-based responses
- ✅ Automatically scans and injects into HTML **forms**
- ✅ Clear and colorized CLI output
- ✅ Modular and easily extensible code structure
- ✅ Built with Python 3 (`requests`, `bs4`, `colorama`)

---

## 📋 Requirements

VulnScan requires Python **3.6 or higher** and the following packages:

- [`requests`](https://pypi.org/project/requests/)
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/)
- [`colorama`](https://pypi.org/project/colorama/)

To install all dependencies:

```bash
pip install -r requirements.txt
