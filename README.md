# 🔍 Advanced Subdomain Finder

A fast & simple Python tool to discover subdomains of a target domain.  
This is the **free version** – good for learning and small recon tasks.

👉 For the **Pro version** (with threading, takeover detection & save results to file), check it here: [Buy Pro](https://dilkhush88.gumroad.com/l/lqwlwk)  

---

## ⚡ Features
- Brute-force subdomains using custom wordlists
- Grab HTTP status & titles
- Simple output on terminal

---

## 📌 Installation
```bash
git clone https://github.com/udaisingh00/subdomain-finder.git
cd subdomain-finder
pip install -r requirements.txt

usage
python3 subfinder.py example.com

Exmaple output
[+] Found: http://blog.example.com | Title: Blog
[+] Found: http://shop.example.com | Title: Shop
