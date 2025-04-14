# VLAN Configuration Automation using Python 🖥️🔧

This project automates the configuration of VLANs on Cisco-like switches using Python, Netmiko, and GNS3. It’s designed for students, professionals, and network engineers who want to streamline repetitive CLI tasks and simulate enterprise networking environments.

---

## 📋 Table of Contents

1. [Features](#-features)
2. [System Requirements](#-system-requirements)
3. [Installation & Setup](#-installation--setup)
4. [Simulation Environment (GNS3 + VS Code)](#-simulation-environment-gns3--vs-code)
5. [How to Run the Script](#-how-to-run-the-script)
6. [How the Automation Works](#️-how-the-automation-works)
7. [Sample Log Output](#-sample-log-output)
8. [Project Structure](#-project-structure)
9. [Contribution](#-contribution)
10. [Author](#-author)

---

## 🚀 Features

- Automated VLAN creation (10, 20, 30...)
- Dynamic VLAN naming (`SALES`, `MARKETING`, etc.)
- Interface-to-VLAN assignment
- SSH-based configuration using Netmiko
- Saves config to startup memory
- Clean terminal output and logging
- Fully compatible with GNS3 simulation

---

## 📦 System Requirements

| Component     | Version / Recommendation |
|---------------|---------------------------|
| Python        | 3.7 or higher              |
| VS Code       | Recommended IDE           |
| GNS3          | 2.2+                       |
| Netmiko       | Latest (via pip)          |
| Paramiko      | Latest (via pip)          |
| Cisco Device  | IOSvL2 (Switch image in GNS3) |

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/azad-faizan/Network-Automation-VLAN-using-Python.git
   cd Network-Automation-VLAN-using-Python
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure Python is added to your system path.**

---

## 🖥️ Simulation Environment (GNS3 + VS Code)

### ✅ GNS3 Setup

- Add a **Cisco Switch (IOSvL2)** to your GNS3 project.
- Assign it the IP address (e.g. `192.168.1.1`) reachable from your local machine.
- Enable **SSH** on the switch:
  ```bash
  conf t
  username admin password admin
  line vty 0 4
    login local
    transport input ssh
  crypto key generate rsa
  ip domain-name local
  ```

### ✅ VS Code Setup

- Open the cloned project in **VS Code**.
- Set terminal working path:
  ```
  PS D:\Softwares\VS Code\Workspace\network-automation>
  ```

---

## ▶️ How to Run the Script

Once the environment is ready, run the script from terminal:

```bash
python vlan_automation.py
```

You will see output like:
```plaintext
Connecting to 192.168.1.1...
Username: admin
Password: ******
Creating VLAN 10...
Assigning interfaces...
Saving configuration...
Connection closed.
```

---

## 🧠️ How the Automation Works

- The script uses **Netmiko** to establish an SSH session with the switch.
- VLANs are created one by one:
  ```bash
  vlan 10
  name SALES
  interface FastEthernet0/1
  switchport access vlan 10
  ```
- Each interface is mapped to its respective VLAN.
- After configuration, the script sends `write memory` to save the running config.
- Finally, the SSH connection is closed.

This ensures repeatable and error-free setup across testbeds or live labs.

---

## 📝 Sample Log Output

```
=========================================
     VLAN CONFIGURATION LOG REPORT
=========================================

[Session Start Time]: 2025-04-14 10:52:11 AM
[Operator]: admin
[Target Device]: 192.168.1.1

--- VLAN Operation Summary ---

✔ VLAN 10 → SALES → Ports: FastEthernet0/1, FastEthernet0/2
✔ VLAN 20 → MARKETING → Ports: FastEthernet0/3, FastEthernet0/4
✔ VLAN 30 → ACCOUNTS → Ports: FastEthernet0/5, FastEthernet0/6

✔ Configuration Saved
✔ Connection Closed

[Session Duration]: 00:01:34
[Exit Status]: ✅ Completed successfully
```

---

## 📁 Project Structure

| File                | Purpose                                      |
|---------------------|----------------------------------------------|
| `vlan_automation.py`| Main automation script                       |
| `requirements.txt`  | Python packages list                         |
| `README.md`         | Complete project guide (this file)           |
| `automation_log.txt`| Sample terminal log                          |

---

## 🤝 Contribution

Pull requests are welcome! To contribute:
- Fork the repo
- Create a new branch
- Make changes and test
- Submit a pull request

If you're a student or engineer looking to add your own VLAN policies or support trunking, feel free to extend the base!

---

## 👨‍💻 Author

**Muhammad Faizan**  
Electronics Engineer | Network & Cloud Professional  
📍 Pakistan  
🔗 [GitHub](https://github.com/azad-faizan) | 🔗 [LinkedIn](#)

---
