# OminiShell

![Security Research](https://img.shields.io/badge/Focus-Security%20Research-red.svg)
![Python 3](https://img.shields.io/badge/Python-3.x-blue.svg)
![Linux](https://img.shields.io/badge/Platform-Linux-000000?logo=linux)
![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

> **OminiShell** is an advanced cybersecurity research and authorized penetration-testing framework designed to study how seemingly benign Windows file formats can be analyzed and tested as delivery mechanisms for remote-access functionality.

---

> [!WARNING]
> **AUTHORIZED USE ONLY**  
> This project is strictly intended for educational purposes, defensive security research, and authorized red-team testing in controlled, isolated laboratory environments.

---

## 📌 Project Overview

OminiShell provides an interactive command-line interface (CLI) for security researchers and detection engineers to experiment with file-based payload delivery formats. By understanding how attackers manipulate common document types, defensive teams can craft better detections and strengthen endpoint security posture.

### Key Research Vectors
* **Batch Files (`.bat`):** Analyzing command execution and script obfuscation.
* **Image Files (`.png`, `.jpg`):** Testing steganography and polyglot file delivery mechanics.
* **PDF Documents (`.pdf`):** Investigating embedded script execution and dynamic triggers.
* **Microsoft Office Formats (`.docx`, `.xlsx`):** Examining macro-based vectors and object embedding.

---

## 🛠️ Key Features

* **Interactive CLI Interface:** Intuitive menu-driven system for quick module selection.
* **Modular Architecture:** Dedicated research components tailored for specific file formats.
* **Automated Environment Setup:** Built-in bash automation for seamless dependency management.
* **Telemetry & Detection Testing:** Helps analyze process trees, child process creation, and network telemetry.

---

## 📋 System Requirements & Lab Setup

### Prerequisites
* **Operating System:** Linux Environment (Kali Linux, Ubuntu, or Parrot OS recommended)
* **Runtime:** Python 3.x
* **Shell:** Bash

* **Target System:** Disposable Windows Virtual Machine in a Host-Only network layout.
* **Monitoring:** Enable Sysmon and Windows Event Logging to capture behavior.
* **Protection:** Ensure frequent VM snapshots to reset the environment post-testing.

---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/shailesh-zx/ominishell](https://github.com/shailesh-zx/ominishell)
cd ominishell

2. Run Automated Setup
Bash

bash setup.sh

3. Launch OminiShell
Bash

python3 ominishell.py

🖥️ Terminal Interface Preview
Plaintext

====================================================
                OMINISHELL FRAMEWORK                
          File Delivery & Research Module           
====================================================

  [1] Bat File Research
  [2] Image File Delivery Module
  [3] PDF File Delivery Module
  [4] Office File Module (Word / Excel)
  [5] Help & Documentation
  [6] Exit Framework

Select a module [1-6]: 

🛡️ Use Cases for Security Teams

    Red Team Operations: Emulate realistic adversary file-delivery techniques.

    Detection Engineering: Develop and validate YARA rules, Sigma rules, and EDR detections.

    Incident Response: Analyze attack artifacts and child process spawning behavior.

    Malware Analysis Training: Understand the anatomy of file-based attack chains.

⚖️ Legal & Ethical Disclaimer

OminiShell is provided AS-IS for legitimate research and educational usage only.

    Do NOT test this project against systems, networks, or devices without explicit, written authorization.

    The developer (Shailesh-ZX) assumes no liability and is not responsible for any misuse, unauthorized access, or damage caused by this utility.

    Users are required to comply with all applicable local, national, and international cybersecurity laws.

🤝 Responsible Disclosure & Author

If you identify security vulnerabilities or issues within the framework itself, please report them directly via GitHub Issues or contact the maintainer.

    Author: Shailesh-ZX

    GitHub: @shailesh-zx

    License:MIT
