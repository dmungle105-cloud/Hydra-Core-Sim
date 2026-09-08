# Hydra-Core-Sim: Automated Credential Auditing Simulator

A high-performance, multi-threaded credential stuffing and authentication simulation utility built in Python. Designed to demonstrate how automated dictionary attacks exploit weak password policies, this tool serves as a local security auditor to stress-test target SSH endpoints safely.

## 🚀 Key Features
* **Hybrid Execution Modes:** Supports seamless command-line execution or an interactive, menu-driven step-by-step user prompt interface.
* **Throttled Concurrency Control:** Employs a `BoundedSemaphore` constraint layer to cap active authentication threads to 20 maximum concurrent connections. This prevents socket exhaustion or crash loops on target devices.
* **Dynamic IO Validation:** Integrates strict file checking utilizing `os.path` hooks to verify wordlist presence before firing threads.
* **Native Protocol Handling:** Leverages the robust `paramiko` library to mimic true SSH handshake exchanges (Port 22).

## 🛠️ Requirements & Setup
* Python 3.x
* Required module: `paramiko`

To install dependencies within your environment, execute:
```bash
pip install paramiko
```

## 💻 How to Use

Ensure you have a password list file (e.g., `common_passwords.txt`) located within your target workspace.

### 1. Interactive Launch Mode (Play Button friendly)
Simply run the script. The engine will guide you through setup prompts directly in the console:
```bash
python Untitled-1.py
```
**Console Prompts View:**
```text
=== Hydra-Core-Sim: Interactive Mode ===
┌─ Enter Target IP (e.g., 127.0.0.1): 127.0.0.1
├─ Enter Username to audit (e.g., admin): root
└─ Enter Wordlist file path (e.g., common_passwords.txt): common_passwords.txt
```

### 2. Fast Command Line Mode
Pass arguments dynamically directly when initializing:
```bash
python Untitled-1.py <Target-IP> <Username> <Wordlist-Path>
```

## 📊 Sample Output Execution
```text
[*] Initializing password audit against 127.0.0.1 for user 'root'...
[*] Reading wordlist data...
[-] Failed attempt: root:password123
[-] Failed attempt: root:qwerty

[+] SUCCESS: Weak credentials found! -> root:admin123

[*] Audit complete. Target verified as VULNERABLE.
```

## ⚠️ Legal Disclaimer
This software is developed strictly for educational purposes, authorized systems testing, and defensive engineering research. Running brute-force simulations against environments without unambiguous, explicit written authorization from the system owner is unlawful.

---
*Maintained as a module exploration project under core security simulation frameworks.*
