#!/usr/bin/env python3
"""
Demo script to showcase all utility functions
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.commands import get_common_commands, get_system_info


def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70 + "\n")


def main():
    """Main demo function"""
    
    print_header("🎉 Welcome to the Helpful Utility Functions Library!")
    
    # System Information
    print_header("📊 System Information")
    info = get_system_info()
    for key, value in info.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    
    # Available Utilities
    print_header("🔧 Available Utility Categories")
    
    utilities = {
        "📄 PDF Utilities": [
            "Download PDF from URL",
            "Merge multiple PDFs",
            "Split PDF into pages",
            "Convert PDF to images"
        ],
        "🖼️  Image Utilities": [
            "Resize images",
            "Convert image formats",
            "Update image resolution",
            "Compress images",
            "Create thumbnails"
        ],
        "📁 File Utilities": [
            "Copy files",
            "Move files",
            "Delete files",
            "Compress folders",
            "Extract archives",
            "Get file sizes"
        ],
        "💻 Command Utilities": [
            "List common commands",
            "Execute shell commands",
            "Get system information",
            "Print commands by category"
        ]
    }
    
    for category, features in utilities.items():
        print(f"{category}")
        for feature in features:
            print(f"  ✓ {feature}")
        print()
    
    # Command Categories
    print_header("📋 Available Command Categories")
    commands = get_common_commands()
    categories = list(commands.keys())
    for i, category in enumerate(categories, 1):
        cmd_count = len(commands[category])
        print(f"  {i}. {category.replace('_', ' ').title()} ({cmd_count} commands)")
    
    # Quick Start
    print_header("🚀 Quick Start")
    print("Install dependencies:")
    print("  $ pip install -r requirements.txt\n")
    print("Run examples:")
    print("  $ python examples/pdf_examples.py")
    print("  $ python examples/image_examples.py")
    print("  $ python examples/file_examples.py")
    print("  $ python examples/command_examples.py\n")
    print("Import and use:")
    print("  from utils.pdf import download_pdf")
    print("  from utils.image import resize_image")
    print("  from utils.file import compress_folder")
    print("  from utils.commands import get_system_info\n")
    
    # Documentation
    print_header("📚 Documentation")
    print("For detailed documentation and usage examples, see:")
    print("  → README.md")
    print("  → examples/ directory")
    print("  → Individual utility files in utils/\n")
    
    print("=" * 70)
    print("  Happy coding! ⭐")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
