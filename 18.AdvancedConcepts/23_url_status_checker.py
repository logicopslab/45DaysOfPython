# url_status_checker.py

import urllib.request
import urllib.error


def check_url(url):
    try:
        response = urllib.request.urlopen(url, timeout=5)
        return f"Status Code: {response.getcode()}"
    
    except urllib.error.HTTPError as e:
        return f"HTTP Error: {e.code}"
    
    except urllib.error.URLError:
        return "Failed to reach server"
    
    except Exception as e:
        return f"Unexpected Error: {e}"


def main():
    url = input("Enter URL (with http/https): ")
    result = check_url(url)
    print(result)


main()
