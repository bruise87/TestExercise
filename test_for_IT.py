from urllib.parse import urlparse, parse_qs


def check():
    url = "https://google.ru/?wmid=242&clickid=92c84d0f8c034531ace41792bd8bcc05&Mookid=zoSIq0bZhDXE"
    parsed_url = urlparse(url)
    queryParams = parse_qs( parsed_url.query)
    print("clickid:", queryParams["clickid"])
