# Ethical-Hacking-Journal

This is a journal to keep track of overall progress and new topics I learn about Ethical Hacking / Hacking in general

here are some key concepts im aware of, but might need to brush up on: 
# Reconnaissance
I'm aware that there are two different types: active and passive.

Active is when you are actively interacting with the target, less hidden, more risk of being found out and making "noise".

Passive recon: not directly interacting with the target. this is done by looking at any social media post, gaining info that way. looking to see if any info has been uploaded to the internet about this company, looking at layouts of the building for security if doing an internal pentest etc. 

# Enumeration

Enumeration is the act of then going further, starting to dig deeper, identifing active host, open ports, any available services on the network/system. basically trying to identify a point of entry, or multiple points of entry. Enumeration is a great way to find out service versions that might be outdated and have vulns that can be exploited, shared resources, and config data. 

# Exploitation

This is when the fun happens. During this stage of the hacking methodology, you try to exploit any identified vulns to gain some form of access or control of a system. this can be a workers computer, maybe a network etc. 

# Post-Exploitation 

After Exploitation, this is when you would try to maintain access aka gaining "Persistance". You could even try to escalate your own privs by trying to reach a position of more power/control like admin, or any other position that has more privileges. This is also the chance to gather more info if needed, but also it's a good things to do so in general. 


# Tools

some great tools to use during the process include, Nmap for port scanning, this is a great way to discover open ports and services. Enum4Linux to gather info for window machines. Nessus and OpenVAS are used for vuln scanning. Nikto scans for any security issues. 

The Metasploit Framework itself is a pretty handy tool that provides a myriad of payloads and exploits for various systems, with Meterpreter being an advanced payload for post-exploitation, burp suite is also great for web application testing, used to find exploits like sql-injection and XSS. John the Ripper and Hashcat are great for password cracking.
