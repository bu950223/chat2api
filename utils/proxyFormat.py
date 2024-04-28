class ProxyFormat:
    http_proxy_host: str = None
    http_proxy_port: int = 80
    proxy_type: str = "http"
    proxy_username: str = None
    proxy_password: str = None


def proxy_format(proxy_url: str):
    proxy = ProxyFormat()
    if proxy_url.startswith("http://"):
        proxy.proxy_type = "http"
        proxy_url = proxy_url.replace("http://", "")

    elif proxy_url.startswith("https://"):
        proxy.proxy_type = "https"
        proxy_url = proxy_url.replace("https://", "")

    if "@" in proxy_url:
        proxy.proxy_username, proxy.proxy_password = proxy_url.split("@")[0].split(":")
        proxy.http_proxy_host, proxy.http_proxy_port = proxy_url.split("@")[1].split(":")
    else:
        proxy.http_proxy_host, proxy.http_proxy_port = proxy_url.split(":")

    return proxy
