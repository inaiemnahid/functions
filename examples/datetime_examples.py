"""
Example usage of DateTime utility functions
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.datetime import (
    get_current_timestamp, get_current_date, get_current_time,
    parse_date, format_date, add_days, calculate_age, days_between,
    is_weekend, get_day_name, get_month_name, time_ago
)

def main():
    print("=" * 60)
    print("DateTime Utilities Examples")
    print("=" * 60)
    
    # Example 1: Get current date and time
    print("\n1. Get current date and time:")
    print(f"   Timestamp: {get_current_timestamp()}")
    print(f"   Date: {get_current_date()}")
    print(f"   Time: {get_current_time()}")
    
    # Example 2: Parse and format dates
    print("\n2. Parse and format dates:")
    print("   date = parse_date('2025-10-27')")
    print("   formatted = format_date(date, '%B %d, %Y')")
    print("   # Returns: 'October 27, 2025'")
    
    # Example 3: Add days
    print("\n3. Add/subtract days:")
    future = add_days(7)
    past = add_days(-7)
    print(f"   7 days from now: {format_date(future)}")
    print(f"   7 days ago: {format_date(past)}")
    
    # Example 4: Calculate age
    print("\n4. Calculate age from birth date:")
    print("   birth_date = parse_date('1990-01-01')")
    print("   age = calculate_age(birth_date)")
    print("   # Returns: age in years")
    
    # Example 5: Days between dates
    print("\n5. Calculate days between dates:")
    print("   d1 = parse_date('2025-01-01')")
    print("   d2 = parse_date('2025-01-10')")
    print("   days = days_between(d1, d2)")
    print("   # Returns: 9")
    
    # Example 6: Check if weekend
    print("\n6. Check if date is weekend:")
    print(f"   Today is weekend: {is_weekend()}")
    
    # Example 7: Get day and month names
    print("\n7. Get day and month names:")
    print(f"   Day: {get_day_name()}")
    print(f"   Month: {get_month_name()}")
    
    # Example 8: Time ago
    print("\n8. Human-readable time difference:")
    past_time = add_days(-2)
    print(f"   Time ago: {time_ago(past_time)}")
    
    print("\n" + "=" * 60)
    print("To use these functions, import them:")
    print("from utils.datetime import get_current_date, add_days, calculate_age")
    print("=" * 60)

if __name__ == "__main__":
    main()
