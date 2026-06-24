"""Lightweight DNS-over-HTTPS client for environments without requests library."""
import base64


def build_query(hostname):
    """Build a DNS A record query for the given hostname."""
    buf = b"\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00"
    for label in hostname.split("."):
        buf += bytes([len(label)]) + label.encode()
    buf += b"\x00\x00\x01\x00\x01"
    return buf


def encode_query(raw_query):
    """Encode a raw DNS query for DoH GET parameter."""
    return base64.urlsafe_b64encode(raw_query).rstrip(b"=").decode()


def make_doh_request(tls_conn, resolver, query_data):
    """Send a DoH query over an established TLS connection."""
    encoded = encode_query(query_data)
    request = (
        f"GET /dns-query?dns={encoded} HTTP/1.1\r\n"
        f"Host: {resolver}\r\n"
        f"Accept: application/dns-message\r\n\r\n"
    )
    tls_conn.sendall(request.encode())
    return tls_conn.recv(512)
