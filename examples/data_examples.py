"""
Example usage of Data utility functions
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.data import (
    read_json, write_json, pretty_print_json, read_csv, write_csv,
    flatten_dict, merge_dicts, filter_dict
)

def main():
    print("=" * 60)
    print("Data Utilities Examples")
    print("=" * 60)
    
    # Example 1: JSON operations
    print("\n1. JSON operations:")
    data = {"name": "John", "age": 30, "city": "New York"}
    print("   data = {'name': 'John', 'age': 30, 'city': 'New York'}")
    print("   write_json(data, 'output.json')")
    print("   loaded = read_json('output.json')")
    
    # Example 2: Pretty print JSON
    print("\n2. Pretty print JSON:")
    print("   pretty_print_json(data)")
    print("   # Outputs nicely formatted JSON")
    
    # Example 3: CSV operations
    print("\n3. CSV operations:")
    print("   data = [")
    print("       {'name': 'John', 'age': 30},")
    print("       {'name': 'Jane', 'age': 25}")
    print("   ]")
    print("   write_csv(data, 'output.csv')")
    print("   loaded = read_csv('output.csv')")
    
    # Example 4: Convert between formats
    print("\n4. Convert between JSON and CSV:")
    print("   json_to_csv('data.json', 'data.csv')")
    print("   csv_to_json('data.csv', 'data.json')")
    
    # Example 5: Flatten nested dictionary
    print("\n5. Flatten nested dictionary:")
    nested = {"user": {"name": "John", "address": {"city": "NYC"}}}
    flat = flatten_dict(nested)
    print(f"   Nested: {nested}")
    print(f"   Flat: {flat}")
    
    # Example 6: Merge dictionaries
    print("\n6. Merge multiple dictionaries:")
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    merged = merge_dicts(d1, d2)
    print(f"   Dict 1: {d1}")
    print(f"   Dict 2: {d2}")
    print(f"   Merged: {merged}")
    
    # Example 7: Filter dictionary
    print("\n7. Filter dictionary by keys:")
    data = {"a": 1, "b": 2, "c": 3, "d": 4}
    filtered = filter_dict(data, ["a", "c"])
    print(f"   Original: {data}")
    print(f"   Filtered (a, c): {filtered}")
    
    print("\n" + "=" * 60)
    print("To use these functions, import them:")
    print("from utils.data import read_json, write_csv, flatten_dict")
    print("=" * 60)

if __name__ == "__main__":
    main()
