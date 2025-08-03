# VulnScan

**VulnScan** is a lightweight Python CLI tool for detecting common web application vulnerabilities, including **Cross-Site Scripting (XSS)** and **SQL Injection (SQLi)**. It can scan URLs and HTML forms for potential weaknesses by injecting payloads and analyzing the response for reflections or error patterns.

---

---

> ⚠️ **LEGAL DISCLAIMER**  
> This tool is created strictly for **educational purposes** and **authorized testing only**.  
> You may **not use VulnScan on systems or websites without explicit permission**.  
> Unauthorized use of this tool may violate the [Computer Fraud and Abuse Act (CFAA)](https://www.justice.gov/criminal-ccips/computer-fraud-and-abuse-act), local laws, or terms of service agreements.  
> The developer is **not responsible for misuse or damage** resulting from this tool.

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

.


## ⚠️ Legal Disclaimer

> VulnScan is provided for **educational and authorized penetration testing purposes only**.  
> Do **not** use this tool on systems you do not own or have written permission to assess.  
> **Unauthorized scanning may be illegal** under national or international laws.  
> Use responsibly — you are fully liable for your own actions.
