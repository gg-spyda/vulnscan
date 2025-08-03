#Program starts here. We want to build a very basic CLI for fun and development of our skills. Every day we should
#learning and making updates.

import argparse
from vulnscan.scanners import xss, sqli

#This will create our CLI and we will add color later.
def main():
    parser = argparse.ArgumentParser(
        description="VulnScan - Lightweight Web Vulnerability Scanner"
    )

    parser.add_argument(
        "--url",
        required=True,
        help="Target URL (e.g., https://example.com/search?q=test)"
    )

    parser.add_argument(
        "--xss",
        action="store_true",
        help="Run XSS vulnerability tests"
    )

    parser.add_argument(
        "--sqli",
        action="store_true",
        help="Run SQL Injection vulnerability tests"
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all vulnerability tests"
    )

    args = parser.parse_args()

    #We can run our scans here.
    if args.all or args.xss:
        print("[*] Running XSS tests...")
        xss.scan(args.url)

    if args.all or args.sqli:
        print("[*] Running SQLi tests...")
        sqli.scan(args.url)

if __name__ == "__main__":
    main()

