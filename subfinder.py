#!/usr/bin/env python3
# Advanced Subdomain Finder Pro
# Author: YourName

import requests
import dns.resolver
import threading
import queue
from bs4 import BeautifulSoup

q = queue.Queue()
found = []

def fetch_title(url):
    try:
        r = requests.get(url, timeout=3, verify=False)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.title.string.strip() if soup.title else "No Title"
    except:
        return "No Response"

def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        dns.resolver.resolve(f"{subdomain}.{domain}", "A")
        title = fetch_title(url)
        print(f"[+] Found: {url} | Title: {title}")
        found.append(f"{url} | {title}")
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass
    except Exception:
        pass

def worker(domain):
    while not q.empty():
        sub = q.get()
        check_subdomain(domain, sub)
        q.task_done()

if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Advanced Subdomain Finder Pro")
    parser.add_argument("domain", help="Target domain (example.com)")
    parser.add_argument("-w", "--wordlist", help="Path to subdomain wordlist", required=True)
    parser.add_argument("-t", "--threads", help="Number of threads", type=int, default=10)
    parser.add_argument("-o", "--output", help="Save results to file")
    args = parser.parse_args()

    with open(args.wordlist, "r") as f:
        for line in f:
            q.put(line.strip())

    threads = []
    for i in range(args.threads):
        t = threading.Thread(target=worker, args=(args.domain,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    if args.output:
        with open(args.output, "w") as f:
            for item in found:
                f.write(item + "\n")

    print("\n[+] Scan complete.")
    if args.output:
        print(f"[+] Results saved to {args.output}")
