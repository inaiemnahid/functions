"""
Example usage of Text utility functions
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.text import (
    count_words, count_characters, reverse_text, to_snake_case,
    to_camel_case, to_kebab_case, extract_emails, extract_urls,
    truncate_text, remove_html_tags
)

def main():
    print("=" * 60)
    print("Text Utilities Examples")
    print("=" * 60)
    
    # Example 1: Count words and characters
    print("\n1. Count words and characters:")
    text = "Hello world, this is a test"
    print(f"   Text: '{text}'")
    print(f"   Words: {count_words(text)}")
    print(f"   Characters: {count_characters(text)}")
    
    # Example 2: Case conversions
    print("\n2. Convert to different cases:")
    text = "Hello World Example"
    print(f"   Original: '{text}'")
    print(f"   snake_case: '{to_snake_case(text)}'")
    print(f"   camelCase: '{to_camel_case(text)}'")
    print(f"   kebab-case: '{to_kebab_case(text)}'")
    
    # Example 3: Extract emails and URLs
    print("\n3. Extract emails and URLs from text:")
    text = "Contact us at info@example.com or visit https://example.com"
    print(f"   Text: '{text}'")
    print(f"   Emails: {extract_emails(text)}")
    print(f"   URLs: {extract_urls(text)}")
    
    # Example 4: Truncate text
    print("\n4. Truncate long text:")
    long_text = "This is a very long text that needs to be truncated"
    print(f"   Original: '{long_text}'")
    print(f"   Truncated: '{truncate_text(long_text, 20)}'")
    
    # Example 5: Remove HTML tags
    print("\n5. Remove HTML tags:")
    html = "<p>Hello <b>world</b>, this is <em>HTML</em></p>"
    print(f"   Original: '{html}'")
    print(f"   Clean: '{remove_html_tags(html)}'")
    
    print("\n" + "=" * 60)
    print("To use these functions, import them:")
    print("from utils.text import count_words, to_snake_case, extract_emails")
    print("=" * 60)

if __name__ == "__main__":
    main()
