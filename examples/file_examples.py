"""
Example usage of File utility functions
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.file import copy_files, move_files, delete_files, compress_folder, extract_archive, get_file_size

def main():
    print("=" * 60)
    print("File Utilities Examples")
    print("=" * 60)
    
    # Example 1: Copy files
    print("\n1. Copy multiple files to a directory:")
    print("   copy_files(['file1.txt', 'file2.txt'], '/backup/', overwrite=True)")
    
    # Example 2: Move files
    print("\n2. Move files to another directory:")
    print("   move_files(['temp1.txt', 'temp2.txt'], '/archive/')")
    
    # Example 3: Delete files
    print("\n3. Delete files (with confirmation):")
    print("   delete_files(['old1.txt', 'old2.txt'], confirm=True)")
    
    # Example 4: Compress folder
    print("\n4. Compress a folder to ZIP:")
    print("   compress_folder('/data/myproject', 'backup.zip', format='zip')")
    
    # Example 5: Extract archive
    print("\n5. Extract a ZIP file:")
    print("   extract_archive('backup.zip', '/extracted/')")
    
    # Example 6: Get file size
    print("\n6. Get file size in human-readable format:")
    print("   size = get_file_size('document.pdf')")
    print("   # Returns: '2.5 MB'")
    
    print("\n" + "=" * 60)
    print("To use these functions, import them:")
    print("from utils.file import copy_files, move_files, compress_folder")
    print("=" * 60)

if __name__ == "__main__":
    main()
