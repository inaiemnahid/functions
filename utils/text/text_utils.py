"""
Text and string manipulation utility functions
"""

import re
from typing import List, Optional, Dict


def count_words(text: str) -> int:
    """
    Count the number of words in a text
    
    Args:
        text: Input text string
    
    Returns:
        int: Number of words
    
    Example:
        >>> count_words("Hello world, this is a test")
        6
    """
    return len(text.split())


def count_characters(text: str, include_spaces: bool = True) -> int:
    """
    Count the number of characters in a text
    
    Args:
        text: Input text string
        include_spaces: Whether to include spaces in count (default: True)
    
    Returns:
        int: Number of characters
    
    Example:
        >>> count_characters("Hello world", include_spaces=False)
        10
    """
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def reverse_text(text: str) -> str:
    """
    Reverse a text string
    
    Args:
        text: Input text string
    
    Returns:
        str: Reversed text
    
    Example:
        >>> reverse_text("Hello")
        'olleH'
    """
    return text[::-1]


def to_title_case(text: str) -> str:
    """
    Convert text to title case
    
    Args:
        text: Input text string
    
    Returns:
        str: Text in title case
    
    Example:
        >>> to_title_case("hello world")
        'Hello World'
    """
    return text.title()


def to_snake_case(text: str) -> str:
    """
    Convert text to snake_case
    
    Args:
        text: Input text string
    
    Returns:
        str: Text in snake_case
    
    Example:
        >>> to_snake_case("Hello World Example")
        'hello_world_example'
    """
    # Replace spaces and special characters with underscores
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', '_', text)
    return text.lower()


def to_camel_case(text: str) -> str:
    """
    Convert text to camelCase
    
    Args:
        text: Input text string
    
    Returns:
        str: Text in camelCase
    
    Example:
        >>> to_camel_case("hello world example")
        'helloWorldExample'
    """
    words = text.split()
    if not words:
        return text
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


def to_kebab_case(text: str) -> str:
    """
    Convert text to kebab-case
    
    Args:
        text: Input text string
    
    Returns:
        str: Text in kebab-case
    
    Example:
        >>> to_kebab_case("Hello World Example")
        'hello-world-example'
    """
    # Replace spaces and special characters with hyphens
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text.lower()


def remove_extra_spaces(text: str) -> str:
    """
    Remove extra spaces from text (multiple spaces become single space)
    
    Args:
        text: Input text string
    
    Returns:
        str: Text with single spaces only
    
    Example:
        >>> remove_extra_spaces("Hello    world   test")
        'Hello world test'
    """
    return ' '.join(text.split())


def extract_emails(text: str) -> List[str]:
    """
    Extract email addresses from text
    
    Args:
        text: Input text string
    
    Returns:
        list: List of email addresses found
    
    Example:
        >>> extract_emails("Contact us at info@example.com or support@test.org")
        ['info@example.com', 'support@test.org']
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)


def extract_urls(text: str) -> List[str]:
    """
    Extract URLs from text
    
    Args:
        text: Input text string
    
    Returns:
        list: List of URLs found
    
    Example:
        >>> extract_urls("Visit https://example.com or http://test.org")
        ['https://example.com', 'http://test.org']
    """
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(url_pattern, text)


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length
    
    Args:
        text: Input text string
        max_length: Maximum length of the output
        suffix: Suffix to add when truncating (default: "...")
    
    Returns:
        str: Truncated text
    
    Example:
        >>> truncate_text("This is a very long text", 10)
        'This is...'
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def remove_html_tags(text: str) -> str:
    """
    Remove HTML tags from text
    
    Args:
        text: Input text with HTML tags
    
    Returns:
        str: Text without HTML tags
    
    Example:
        >>> remove_html_tags("<p>Hello <b>world</b></p>")
        'Hello world'
    """
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def count_occurrences(text: str, substring: str, case_sensitive: bool = True) -> int:
    """
    Count occurrences of a substring in text
    
    Args:
        text: Input text string
        substring: Substring to count
        case_sensitive: Whether to be case sensitive (default: True)
    
    Returns:
        int: Number of occurrences
    
    Example:
        >>> count_occurrences("Hello hello HELLO", "hello", case_sensitive=False)
        3
    """
    if not case_sensitive:
        text = text.lower()
        substring = substring.lower()
    return text.count(substring)


def replace_multiple(text: str, replacements: Dict[str, str]) -> str:
    """
    Replace multiple substrings in text
    
    Args:
        text: Input text string
        replacements: Dictionary of {old: new} replacements
    
    Returns:
        str: Text with replacements made
    
    Example:
        >>> replace_multiple("Hello world", {"Hello": "Hi", "world": "there"})
        'Hi there'
    """
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text
