# InfraScanner
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Build-Stable-brightgreen)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

> *Red Halo's Modular Infrastructure Scanner - built for reconnaissance and service enumeration.*


**InfraScan** is a lightweight, Python-based tool designed for active port scanning, banner grabbing, and service enumeration. It sits between your recon phase and your exploitation phase - mapping the ssurface before you strike.


---

## Features

- Scan single or multiple ports

- Banner grabbing (optional)

- Modular codebase (easy to extend)

- Output results to JSON or terminal

- Built for Red Team ops and CTFs


---


## Usage 

```bash
python infrascan.py --target <IP/domain> --ports 22,80,443 --banner --output scan_results.json


---

## Available Options:

Flag | Description
--target | Target IP or domain name (Required)
--ports | Comma-separated port list (Default: 1–1024)
--banner | Enable service banner grabbing
--output | Save results to JSON file

---

### Example Output

{
  "target": "scanme.nmap.org",
  "open_ports": [
    {
      "port": 80,
      "banner": "HTTP/1.1 200 OK..."
    },
    {
      "port": 22,
      "banner": "SSH-2.0-OpenSSH_7.6p1"
    }
  ]
}


---

## Project Structure

infrascan/
├── infrascan.py
├── modules/
│   └── port_scanner.py
└── scan_reports/

---

## Part of the Red Halo Offensive Toolkit

>InfraScan is the second tool in a full-chain red team suite:

> - ReconScope-Passive & API-based recon

> - InfraScan-Active scanning & enumeration

> - RedVenom-Exploitation toolkit (Coming soon)

> - RedFang-Payload generation and delivery (coming soon)


---

## Legal Disclaimer

This tool is intended for educational and authorized security testing only. Do not use InfraScan against targets you do not have explicit permission to test.


---

## Contributions

Coming soon: If you'd like to help expand this tool, keep an eye out for contribution guidelines and roadmap tasks.

---

## License

This project is licensed under the [MIT License](LICENSE).

