"""
Data manipulation utility functions (JSON, CSV, etc.)
"""

import json
import csv
from typing import Any, List, Dict, Optional


def read_json(file_path: str) -> Any:
    """
    Read JSON data from a file
    
    Args:
        file_path: Path to JSON file
    
    Returns:
        Parsed JSON data
    
    Example:
        >>> data = read_json('data.json')
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"✗ Error reading JSON: {e}")
        return None


def write_json(data: Any, file_path: str, indent: int = 2) -> bool:
    """
    Write data to a JSON file
    
    Args:
        data: Data to write
        file_path: Path to output JSON file
        indent: Indentation level (default: 2)
    
    Returns:
        bool: True if successful, False otherwise
    
    Example:
        >>> write_json({'name': 'John', 'age': 30}, 'output.json')
        True
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        print(f"✓ JSON written to {file_path}")
        return True
    except Exception as e:
        print(f"✗ Error writing JSON: {e}")
        return False


def pretty_print_json(data: Any, indent: int = 2) -> None:
    """
    Pretty print JSON data to console
    
    Args:
        data: Data to print
        indent: Indentation level (default: 2)
    
    Example:
        >>> pretty_print_json({'name': 'John', 'age': 30})
        {
          "name": "John",
          "age": 30
        }
    """
    print(json.dumps(data, indent=indent, ensure_ascii=False))


def read_csv(file_path: str, has_header: bool = True) -> List[Dict[str, str]]:
    """
    Read CSV data from a file
    
    Args:
        file_path: Path to CSV file
        has_header: Whether CSV has header row (default: True)
    
    Returns:
        list: List of dictionaries (if has_header) or list of lists
    
    Example:
        >>> data = read_csv('data.csv')
        >>> print(data[0])
        {'name': 'John', 'age': '30'}
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            if has_header:
                reader = csv.DictReader(f)
                return list(reader)
            else:
                reader = csv.reader(f)
                return list(reader)
    except Exception as e:
        print(f"✗ Error reading CSV: {e}")
        return []


def write_csv(data: List[Dict[str, Any]], file_path: str, fieldnames: Optional[List[str]] = None) -> bool:
    """
    Write data to a CSV file
    
    Args:
        data: List of dictionaries to write
        file_path: Path to output CSV file
        fieldnames: List of field names (auto-detected if None)
    
    Returns:
        bool: True if successful, False otherwise
    
    Example:
        >>> data = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
        >>> write_csv(data, 'output.csv')
        True
    """
    try:
        if not data:
            print("✗ No data to write")
            return False
        
        if fieldnames is None:
            fieldnames = list(data[0].keys())
        
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"✓ CSV written to {file_path}")
        return True
    except Exception as e:
        print(f"✗ Error writing CSV: {e}")
        return False


def json_to_csv(json_file: str, csv_file: str) -> bool:
    """
    Convert JSON file to CSV
    
    Args:
        json_file: Path to input JSON file
        csv_file: Path to output CSV file
    
    Returns:
        bool: True if successful, False otherwise
    
    Example:
        >>> json_to_csv('data.json', 'data.csv')
        True
    """
    data = read_json(json_file)
    if data is None:
        return False
    
    if isinstance(data, list):
        return write_csv(data, csv_file)
    else:
        print("✗ JSON data must be a list of objects")
        return False


def csv_to_json(csv_file: str, json_file: str) -> bool:
    """
    Convert CSV file to JSON
    
    Args:
        csv_file: Path to input CSV file
        json_file: Path to output JSON file
    
    Returns:
        bool: True if successful, False otherwise
    
    Example:
        >>> csv_to_json('data.csv', 'data.json')
        True
    """
    data = read_csv(csv_file)
    if not data:
        return False
    
    return write_json(data, json_file)


def flatten_dict(d: Dict, parent_key: str = '', sep: str = '.') -> Dict:
    """
    Flatten a nested dictionary
    
    Args:
        d: Dictionary to flatten
        parent_key: Parent key for recursion
        sep: Separator for keys (default: '.')
    
    Returns:
        dict: Flattened dictionary
    
    Example:
        >>> flatten_dict({'a': {'b': 1, 'c': 2}})
        {'a.b': 1, 'a.c': 2}
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def merge_dicts(*dicts: Dict) -> Dict:
    """
    Merge multiple dictionaries
    
    Args:
        *dicts: Dictionaries to merge
    
    Returns:
        dict: Merged dictionary
    
    Example:
        >>> merge_dicts({'a': 1}, {'b': 2}, {'c': 3})
        {'a': 1, 'b': 2, 'c': 3}
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result


def filter_dict(d: Dict, keys: List[str]) -> Dict:
    """
    Filter dictionary by keys
    
    Args:
        d: Dictionary to filter
        keys: List of keys to keep
    
    Returns:
        dict: Filtered dictionary
    
    Example:
        >>> filter_dict({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])
        {'a': 1, 'c': 3}
    """
    return {k: v for k, v in d.items() if k in keys}
