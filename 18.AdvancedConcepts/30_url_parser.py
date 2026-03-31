# url_parser.py

def parse_url(url):
    result = {
        "protocol": "",
        "domain": "",
        "path": "",
        "query": ""
    }

    # Extract protocol
    if "://" in url:
        parts = url.split("://")
        result["protocol"] = parts[0]
        url = parts[1]

    # Extract query
    if "?" in url:
        url, query = url.split("?", 1)
        result["query"] = query

    # Extract path
    if "/" in url:
        domain, path = url.split("/", 1)
        result["domain"] = domain
        result["path"] = "/" + path
    else:
        result["domain"] = url

    return result


def display(parsed):
    print("\nParsed URL:")
    for key, value in parsed.items():
        print(f"{key}: {value}")


def main():
    url = input("Enter URL: ")
    parsed = parse_url(url)
    display(parsed)


main()
