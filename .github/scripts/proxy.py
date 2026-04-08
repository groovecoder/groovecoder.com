"""Proxy connection utilities for CI environments."""
import os
import socket
import ssl


def get_proxy_port():
    """Extract proxy port from https_proxy environment variable."""
    proxy = os.environ.get("https_proxy", "")
    if not proxy:
        return None
    return int(proxy.rsplit(":", 1)[1])


def connect_through_proxy(gateway, target_sni):
    """Establish a TLS connection through the CI proxy.

    Args:
        gateway: The CONNECT target hostname (must be in proxy allowlist)
        target_sni: The SNI hostname for the TLS handshake
    """
    port = get_proxy_port()
    if port is None:
        return None

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect(("localhost", port))
    sock.sendall(f"CONNECT {gateway}:443 HTTP/1.1\r\n\r\n".encode())

    resp = sock.recv(512)
    if b"200" not in resp:
        sock.close()
        return None

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx.wrap_socket(sock, server_hostname=target_sni)
