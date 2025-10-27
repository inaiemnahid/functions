"""
Example usage of Command utility functions
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.commands import get_common_commands, execute_command, get_system_info, print_commands_by_category

def main():
    print("=" * 60)
    print("Command Utilities Examples")
    print("=" * 60)
    
    # Example 1: Get common commands
    print("\n1. Get common commands by category:")
    print("   commands = get_common_commands()")
    print("   git_commands = commands['git']")
    
    # Example 2: Execute a command
    print("\n2. Execute a shell command:")
    print("   result = execute_command('ls -l')")
    print("   if result['success']:")
    print("       print(result['stdout'])")
    
    # Example 3: Get system information
    print("\n3. Get system information:")
    print("   info = get_system_info()")
    print("   print(f\"OS: {info['system']} {info['release']}\")")
    
    # Example 4: Print commands by category
    print("\n4. Print all Git commands:")
    print("   print_commands_by_category('git')")
    
    print("\n5. Print all available commands:")
    print("   print_commands_by_category()")
    
    print("\n" + "=" * 60)
    print("Available command categories:")
    commands = get_common_commands()
    for category in commands.keys():
        print(f"  - {category}")
    print("=" * 60)

if __name__ == "__main__":
    main()
