# 🛡️ OminiShell

### Multi-Format Windows Remote Access & Security Research Framework

<p align="center">
  <b>OminiShell</b> is a cybersecurity research project focused on studying file-based delivery mechanisms, remote-access concepts, and security detection challenges across multiple Windows file formats.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Kali%20Linux-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Category-Cybersecurity-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Use-Authorized%20Testing-green?style=for-the-badge">
</p>

---

## 📌 Overview

**OminiShell** is a command-line based cybersecurity research tool designed to explore how different Windows file formats can be incorporated into remote-access and security-testing workflows.

The project supports multiple output/file-format research options, allowing security researchers to study different delivery mechanisms in a controlled laboratory environment.

### Supported Research Formats

* 🦇 **BAT File**
* 🖼️ **Image File**
* 📄 **PDF File**
* 📊 **Office File — Word / Excel**
* ❓ **Help**
* 🚪 **Exit**

---

## 🔥 FUD / Evasion Research

OminiShell includes a **FUD (Fully Undetectable) / evasion-oriented research concept** as part of its security-testing focus.

The purpose of this functionality is to allow researchers to study the challenges faced by antivirus, endpoint-security, and malware-detection solutions when analyzing dynamically generated or modified file-based artifacts.

> ⚠️ **Important:** “FUD” is used in this project as a security-research concept and should **not** be interpreted as a guarantee that generated artifacts will remain undetected by every antivirus, EDR, sandbox, or security product.

Detection capabilities continuously change between security vendors and product versions. Therefore, no artifact should be considered permanently or universally “undetectable.”

### Research Areas

FUD/evasion research can be used to investigate:

* 🛡️ Antivirus detection
* 🔎 EDR telemetry
* 🧬 Static vs. behavioral detection
* 🧪 Sandbox analysis
* 📡 Network-based detection
* ⚙️ Endpoint monitoring
* 🚨 Detection-rule development

The recommended approach is to perform such research only against **isolated test systems that you own or are explicitly authorized to assess**.

---

## ✨ Features

| Feature              | Description                                     |
| -------------------- | ----------------------------------------------- |
| 🖥️ CLI Interface    | Interactive terminal-based interface            |
| 🦇 BAT Module        | BAT-file security research                      |
| 🖼️ Image Module     | Image-file delivery research                    |
| 📄 PDF Module        | PDF-based attack-chain research                 |
| 📊 Office Module     | Word/Excel security research                    |
| 🔥 FUD Research      | Study of detection and evasion challenges       |
| ⚙️ Automated Setup   | Setup through the included script               |
| 🔬 Security Research | Designed for controlled laboratory environments |

---

## 🖥️ Interface

OminiShell provides an interactive menu:

```text
╔══════════════════════════════════════╗
║              OminiShell              ║
║               [v1.0]                 ║
║          [By Shailesh-ZX]             ║
╚══════════════════════════════════════╝

[1] Bat File
[2] Image File
[3] PDF File
[4] Office File (Word, Office)
[5] Help
[6] Exit

Select an option >
```

---

## ⚙️ Requirements

* Kali Linux / Linux environment
* Python 3
* Bash
* Dedicated Windows testing VM
* Isolated laboratory network


## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/shailesh-zx/ominishell
```

Enter the project directory:

```bash
cd ominishell
```

Run the setup script:

```bash
bash setup.sh
```

Start OminiShell:

```bash
python3 ominishell.py
```

After launching the program, the interactive menu can be used to select the desired research module.

---

## 🔬 Security Research Applications

OminiShell can be used for controlled research involving:

* File-based attack vectors
* Windows security mechanisms
* Malware-analysis concepts
* Red-team training
* Endpoint detection
* EDR research
* SIEM monitoring
* Threat hunting
* Incident-response training
* Detection engineering
* Security-awareness demonstrations

---

## 🛡️ Defensive Research

OminiShell can also be useful from a defensive perspective.

Security teams can use controlled laboratory experiments to investigate:

### Endpoint Telemetry

* Suspicious process creation
* Parent/child process relationships
* Command-line activity
* Temporary-file execution
* Unusual application behavior

### Network Telemetry

* Unexpected outbound connections
* Suspicious destinations
* Long-lived connections
* Unusual DNS activity
* Abnormal network patterns

### Detection Engineering

Research results can be used to develop:

* EDR detection rules
* SIEM queries
* Threat-hunting techniques
* Incident-response procedures
* Endpoint monitoring policies

---

## 🧪 Recommended Laboratory

For safe testing, use a disposable virtual environment.

### Best Practices

* Use a dedicated Windows VM.
* Keep the testing network isolated.
* Create VM snapshots before experiments.
* Never use real credentials.
* Never place sensitive information inside the test VM.
* Restore the VM after testing.
* Do not test against production infrastructure.

---

## ⚠️ Disclaimer

> **OminiShell is intended strictly for educational purposes, cybersecurity research, malware analysis, red-team laboratories, and authorized penetration testing.**

The author does **not** authorize or encourage:

* Unauthorized computer access
* Credential theft
* Malware distribution
* Unauthorized persistence
* Antivirus/EDR bypass against third-party systems
* Attacks against systems without permission
* Deployment against third-party infrastructure
* Any activity that violates applicable laws

You are solely responsible for obtaining proper authorization before performing security testing.

**Never use OminiShell against a system you do not own or have explicit permission to test.**

---

## 📜 Legal Notice

OminiShell is a **dual-use security research project**.

The presence of FUD/evasion-oriented research functionality does not imply that the project guarantees detection bypass or authorization to deploy generated artifacts against third-party systems.

Security products evolve continuously, and detection results can vary between environments and versions.

The maintainers are not responsible for damage, misuse, unauthorized access, or illegal activity resulting from this project.

---

## 🤝 Contributing

Contributions related to legitimate security research are welcome.

Areas of interest include:

* Security research
* Defensive detection
* Malware analysis
* Documentation
* Bug fixes
* Code quality
* Laboratory safety
* Threat research

Contributions intended primarily for unauthorized access or abuse are not encouraged.

---

## 👨‍💻 Author

### Shailesh-ZX

**Cybersecurity Researcher & Developer**

GitHub: **shailesh-zx**

---

## ⭐ Support

If you find **OminiShell** useful for authorized cybersecurity research or education, consider giving the repository a ⭐.

---

## 📄 License

See the repository's `LICENSE` file for the applicable licensing terms.

---

<div align="center">

### 🛡️ Research • Analyze • Detect • Defend

**OminiShell — Cybersecurity Research Project**

</div>
