import requests
from bs4 import BeautifulSoup

"""BS is best for this job. We use BS for getting the form data, editing that data, and submitting that data.
#We could do this job multiple ways; this is the way I know best from research. We will consider more
advanced methods overtime if there are better results. For now,  want to keep the project simple to build momentum."""
def get_forms(url):
    """
    Fetch and parse all forms from a given URL.
    """
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find_all("form")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch forms: {e}")
        return []

def submit_form(form, base_url, payload):
    """
    Submits a form with the given payload in each input.
    Returns the respons we need.
    """
    action = form.get("action")
    method = form.get("method", "get").lower()
    full_url = requests.compat.urljoin(base_url, action)

    inputs = form.find_all("input")
    data = {}

    for input_tag in inputs:
        name = input_tag.get("name")
        if name:
            data[name] = payload  # Inject the payload into all fields

    try:
        if method == "post":
            return requests.post(full_url, data=data, timeout=5)
        else:
            return requests.get(full_url, params=data, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        return None

def scan_forms(url, payload="<script>alert(1)</script>"):
    print(f"[INFO] Scanning forms on: {url}")
    forms = get_forms(url)

    print(f"[INFO] Found {len(forms)} form(s).")

    for i, form in enumerate(forms):
        print(f"\n[>] Testing form #{i + 1}")
        response = submit_form(form, url, payload)

        if response and payload in response.text:
            print("[!!] Payload reflected! Possible XSS vulnerability.")
        else:
            print("[OK] No reflection detected.")

if __name__ == "__main__":
    target_url = input("Enter target URL (page with form): ")
    test_payload = input("Enter payload to test: ")
    scan_forms(target_url, test_payload)
