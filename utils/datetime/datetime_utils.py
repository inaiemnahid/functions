"""
Date and time utility functions
"""

from datetime import datetime, timedelta
from typing import Optional


def get_current_timestamp() -> str:
    """
    Get current timestamp in ISO format
    
    Returns:
        str: Current timestamp
    
    Example:
        >>> timestamp = get_current_timestamp()
        >>> print(timestamp)
        '2025-10-27T12:00:00'
    """
    return datetime.now().isoformat()


def get_current_date(format: str = "%Y-%m-%d") -> str:
    """
    Get current date in specified format
    
    Args:
        format: Date format string (default: YYYY-MM-DD)
    
    Returns:
        str: Current date
    
    Example:
        >>> get_current_date()
        '2025-10-27'
    """
    return datetime.now().strftime(format)


def get_current_time(format: str = "%H:%M:%S") -> str:
    """
    Get current time in specified format
    
    Args:
        format: Time format string (default: HH:MM:SS)
    
    Returns:
        str: Current time
    
    Example:
        >>> get_current_time()
        '12:00:00'
    """
    return datetime.now().strftime(format)


def parse_date(date_string: str, format: str = "%Y-%m-%d") -> Optional[datetime]:
    """
    Parse a date string to datetime object
    
    Args:
        date_string: Date string to parse
        format: Date format (default: YYYY-MM-DD)
    
    Returns:
        datetime or None: Parsed datetime or None if invalid
    
    Example:
        >>> dt = parse_date("2025-10-27")
        >>> print(dt)
        2025-10-27 00:00:00
    """
    try:
        return datetime.strptime(date_string, format)
    except ValueError as e:
        print(f"✗ Error parsing date: {e}")
        return None


def format_date(dt: datetime, format: str = "%Y-%m-%d") -> str:
    """
    Format a datetime object to string
    
    Args:
        dt: Datetime object
        format: Output format (default: YYYY-MM-DD)
    
    Returns:
        str: Formatted date string
    
    Example:
        >>> dt = datetime.now()
        >>> format_date(dt, "%B %d, %Y")
        'October 27, 2025'
    """
    return dt.strftime(format)


def add_days(days: int, start_date: Optional[datetime] = None) -> datetime:
    """
    Add days to a date
    
    Args:
        days: Number of days to add (can be negative)
        start_date: Starting date (default: today)
    
    Returns:
        datetime: New date
    
    Example:
        >>> future = add_days(7)
        >>> print(future)
        2025-11-03 ...
    """
    if start_date is None:
        start_date = datetime.now()
    return start_date + timedelta(days=days)


def add_hours(hours: int, start_time: Optional[datetime] = None) -> datetime:
    """
    Add hours to a datetime
    
    Args:
        hours: Number of hours to add (can be negative)
        start_time: Starting datetime (default: now)
    
    Returns:
        datetime: New datetime
    
    Example:
        >>> future = add_hours(3)
    """
    if start_time is None:
        start_time = datetime.now()
    return start_time + timedelta(hours=hours)


def calculate_age(birth_date: datetime) -> int:
    """
    Calculate age from birth date
    
    Args:
        birth_date: Birth date
    
    Returns:
        int: Age in years
    
    Example:
        >>> birth = parse_date("1990-01-01")
        >>> age = calculate_age(birth)
        >>> print(age)
        35
    """
    today = datetime.now()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age


def days_between(date1: datetime, date2: datetime) -> int:
    """
    Calculate number of days between two dates
    
    Args:
        date1: First date
        date2: Second date
    
    Returns:
        int: Number of days (absolute value)
    
    Example:
        >>> d1 = parse_date("2025-01-01")
        >>> d2 = parse_date("2025-01-10")
        >>> days_between(d1, d2)
        9
    """
    return abs((date2 - date1).days)


def is_weekend(date: Optional[datetime] = None) -> bool:
    """
    Check if a date is a weekend
    
    Args:
        date: Date to check (default: today)
    
    Returns:
        bool: True if weekend (Saturday or Sunday), False otherwise
    
    Example:
        >>> is_weekend(parse_date("2025-10-26"))  # Sunday
        True
    """
    if date is None:
        date = datetime.now()
    return date.weekday() >= 5


def get_day_name(date: Optional[datetime] = None) -> str:
    """
    Get the name of the day of the week
    
    Args:
        date: Date to check (default: today)
    
    Returns:
        str: Day name (e.g., 'Monday', 'Tuesday')
    
    Example:
        >>> get_day_name()
        'Monday'
    """
    if date is None:
        date = datetime.now()
    return date.strftime("%A")


def get_month_name(date: Optional[datetime] = None) -> str:
    """
    Get the name of the month
    
    Args:
        date: Date to check (default: today)
    
    Returns:
        str: Month name (e.g., 'January', 'February')
    
    Example:
        >>> get_month_name()
        'October'
    """
    if date is None:
        date = datetime.now()
    return date.strftime("%B")


def time_ago(past_date: datetime) -> str:
    """
    Get human-readable time difference from now
    
    Args:
        past_date: Past datetime
    
    Returns:
        str: Human-readable time difference
    
    Example:
        >>> past = add_hours(-2)
        >>> time_ago(past)
        '2 hours ago'
    """
    now = datetime.now()
    diff = now - past_date
    
    seconds = diff.total_seconds()
    
    if seconds < 60:
        return f"{int(seconds)} seconds ago"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    else:
        days = int(seconds / 86400)
        return f"{days} day{'s' if days != 1 else ''} ago"
