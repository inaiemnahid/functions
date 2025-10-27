"""
Network and web utility functions
"""

import socket
import urllib.parse
from typing import Optional, Dict


def check_internet_connection(host: str = "8.8.8.8", port: int = 53, timeout: int = 3) -> bool:
    """
    Check if internet connection is available
    
    Args:
        host: Host to check (default: Google DNS)
        port: Port to check (default: 53)
        timeout: Timeout in seconds (default: 3)
    
    Returns:
        bool: True if connection available, False otherwise
    
    Example:
        >>> check_internet_connection()
        True
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False


def get_ip_address() -> Optional[str]:
    """
    Get the local IP address
    
    Returns:
        str or None: Local IP address or None if unable to determine
    
    Example:
        >>> ip = get_ip_address()
        >>> print(ip)
        '192.168.1.100'
    """
    try:
        # Connect to external host to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return None


def is_valid_url(url: str) -> bool:
    """
    Check if a URL is valid
    
    Args:
        url: URL to validate
    
    Returns:
        bool: True if valid URL, False otherwise
    
    Example:
        >>> is_valid_url("https://example.com")
        True
    """
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def parse_url(url: str) -> Dict[str, str]:
    """
    Parse a URL into its components
    
    Args:
        url: URL to parse
    
    Returns:
        dict: Dictionary with URL components
    
    Example:
        >>> parse_url("https://example.com:8080/path?key=value#section")
        {'scheme': 'https', 'netloc': 'example.com:8080', 'path': '/path', ...}
    """
    parsed = urllib.parse.urlparse(url)
    return {
        'scheme': parsed.scheme,
        'netloc': parsed.netloc,
        'path': parsed.path,
        'params': parsed.params,
        'query': parsed.query,
        'fragment': parsed.fragment
    }


def build_url(base_url: str, params: Dict[str, str]) -> str:
    """
    Build a URL with query parameters
    
    Args:
        base_url: Base URL
        params: Dictionary of query parameters
    
    Returns:
        str: URL with query parameters
    
    Example:
        >>> build_url("https://example.com", {"key": "value", "page": "1"})
        'https://example.com?key=value&page=1'
    """
    if not params:
        return base_url
    query_string = urllib.parse.urlencode(params)
    separator = '&' if '?' in base_url else '?'
    return f"{base_url}{separator}{query_string}"


def get_domain_from_url(url: str) -> Optional[str]:
    """
    Extract domain from URL
    
    Args:
        url: URL to extract domain from
    
    Returns:
        str or None: Domain name or None if invalid
    
    Example:
        >>> get_domain_from_url("https://www.example.com/path")
        'www.example.com'
    """
    try:
        parsed = urllib.parse.urlparse(url)
        return parsed.netloc
    except:
        return None


def encode_url(url: str) -> str:
    """
    URL encode a string
    
    Args:
        url: String to encode
    
    Returns:
        str: URL encoded string
    
    Example:
        >>> encode_url("hello world & test")
        'hello%20world%20%26%20test'
    """
    return urllib.parse.quote(url)


def decode_url(url: str) -> str:
    """
    URL decode a string
    
    Args:
        url: String to decode
    
    Returns:
        str: URL decoded string
    
    Example:
        >>> decode_url("hello%20world%20%26%20test")
        'hello world & test'
    """
    return urllib.parse.unquote(url)


def get_hostname() -> str:
    """
    Get the hostname of the current machine
    
    Returns:
        str: Hostname
    
    Example:
        >>> hostname = get_hostname()
        >>> print(hostname)
        'my-computer'
    """
    return socket.gethostname()


def is_port_open(host: str, port: int, timeout: int = 2) -> bool:
    """
    Check if a port is open on a host
    
    Args:
        host: Host to check
        port: Port number to check
        timeout: Timeout in seconds (default: 2)
    
    Returns:
        bool: True if port is open, False otherwise
    
    Example:
        >>> is_port_open("localhost", 80)
        False
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False
