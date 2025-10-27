"""
Example usage of Network utility functions
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.network import (
    check_internet_connection, get_ip_address, is_valid_url,
    parse_url, build_url, get_domain_from_url, get_hostname
)

def main():
    print("=" * 60)
    print("Network Utilities Examples")
    print("=" * 60)
    
    # Example 1: Check internet connection
    print("\n1. Check internet connection:")
    print("   check_internet_connection()")
    
    # Example 2: Get IP address
    print("\n2. Get local IP address:")
    print("   ip = get_ip_address()")
    print("   print(f'Local IP: {ip}')")
    
    # Example 3: Validate URLs
    print("\n3. Validate URLs:")
    urls = ["https://example.com", "not-a-url", "ftp://files.com"]
    for url in urls:
        valid = is_valid_url(url)
        print(f"   '{url}' -> {valid}")
    
    # Example 4: Parse URL
    print("\n4. Parse URL into components:")
    url = "https://example.com:8080/path?key=value#section"
    print(f"   URL: {url}")
    print("   parsed = parse_url(url)")
    print("   # Returns: {'scheme': 'https', 'netloc': 'example.com:8080', ...}")
    
    # Example 5: Build URL with parameters
    print("\n5. Build URL with query parameters:")
    base = "https://api.example.com/search"
    params = {"q": "python", "page": "1", "limit": "10"}
    print(f"   Base: {base}")
    print(f"   Params: {params}")
    result = build_url(base, params)
    print(f"   Result: {result}")
    
    # Example 6: Extract domain
    print("\n6. Extract domain from URL:")
    url = "https://www.example.com/path/to/page"
    domain = get_domain_from_url(url)
    print(f"   URL: {url}")
    print(f"   Domain: {domain}")
    
    # Example 7: Get hostname
    print("\n7. Get current machine hostname:")
    hostname = get_hostname()
    print(f"   Hostname: {hostname}")
    
    print("\n" + "=" * 60)
    print("To use these functions, import them:")
    print("from utils.network import check_internet_connection, parse_url")
    print("=" * 60)

if __name__ == "__main__":
    main()
