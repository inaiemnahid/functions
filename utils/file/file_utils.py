"""
File utility functions for common file operations
"""

import os
import shutil
import zipfile
import tarfile
from typing import List, Optional


def copy_files(source_paths: List[str], destination_dir: str, overwrite: bool = False) -> bool:
    """
    Copy multiple files to a destination directory
    
    Args:
        source_paths: List of file paths to copy
        destination_dir: Destination directory
        overwrite: Whether to overwrite existing files (default: False)
    
    Returns:
        bool: True if all copies successful, False otherwise
    
    Example:
        >>> copy_files(['file1.txt', 'file2.txt'], '/destination/', overwrite=True)
        True
    """
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        
        copied_count = 0
        for source_path in source_paths:
            if not os.path.exists(source_path):
                print(f"Warning: {source_path} not found, skipping...")
                continue
            
            filename = os.path.basename(source_path)
            dest_path = os.path.join(destination_dir, filename)
            
            if os.path.exists(dest_path) and not overwrite:
                print(f"Warning: {dest_path} already exists, skipping...")
                continue
            
            shutil.copy2(source_path, dest_path)
            copied_count += 1
        
        print(f"✓ Copied {copied_count} file(s) to {destination_dir}")
        return True
    except Exception as e:
        print(f"✗ Error copying files: {e}")
        return False


def move_files(source_paths: List[str], destination_dir: str, overwrite: bool = False) -> bool:
    """
    Move multiple files to a destination directory
    
    Args:
        source_paths: List of file paths to move
        destination_dir: Destination directory
        overwrite: Whether to overwrite existing files (default: False)
    
    Returns:
        bool: True if all moves successful, False otherwise
    
    Example:
        >>> move_files(['file1.txt', 'file2.txt'], '/destination/')
        True
    """
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        
        moved_count = 0
        for source_path in source_paths:
            if not os.path.exists(source_path):
                print(f"Warning: {source_path} not found, skipping...")
                continue
            
            filename = os.path.basename(source_path)
            dest_path = os.path.join(destination_dir, filename)
            
            if os.path.exists(dest_path) and not overwrite:
                print(f"Warning: {dest_path} already exists, skipping...")
                continue
            
            shutil.move(source_path, dest_path)
            moved_count += 1
        
        print(f"✓ Moved {moved_count} file(s) to {destination_dir}")
        return True
    except Exception as e:
        print(f"✗ Error moving files: {e}")
        return False


def delete_files(file_paths: List[str], confirm: bool = True) -> bool:
    """
    Delete multiple files
    
    Args:
        file_paths: List of file paths to delete
        confirm: Whether to ask for confirmation (default: True)
    
    Returns:
        bool: True if all deletions successful, False otherwise
    
    Example:
        >>> delete_files(['temp1.txt', 'temp2.txt'], confirm=False)
        True
    """
    try:
        if confirm:
            print(f"About to delete {len(file_paths)} file(s):")
            for path in file_paths:
                print(f"  - {path}")
            response = input("Continue? (y/n): ").lower()
            if response != 'y':
                print("Deletion cancelled")
                return False
        
        deleted_count = 0
        for file_path in file_paths:
            if os.path.exists(file_path):
                os.remove(file_path)
                deleted_count += 1
            else:
                print(f"Warning: {file_path} not found, skipping...")
        
        print(f"✓ Deleted {deleted_count} file(s)")
        return True
    except Exception as e:
        print(f"✗ Error deleting files: {e}")
        return False


def compress_folder(folder_path: str, output_path: str, format: str = 'zip') -> bool:
    """
    Compress a folder to an archive
    
    Args:
        folder_path: Path to the folder to compress
        output_path: Path for the output archive
        format: Archive format ('zip' or 'tar.gz', default: 'zip')
    
    Returns:
        bool: True if compression successful, False otherwise
    
    Example:
        >>> compress_folder('/data/folder', 'backup.zip')
        True
    """
    try:
        if not os.path.exists(folder_path):
            print(f"✗ Folder {folder_path} not found")
            return False
        
        if format == 'zip':
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname)
        
        elif format == 'tar.gz':
            with tarfile.open(output_path, 'w:gz') as tarf:
                tarf.add(folder_path, arcname=os.path.basename(folder_path))
        
        else:
            print(f"✗ Unsupported format: {format}. Use 'zip' or 'tar.gz'")
            return False
        
        file_size = os.path.getsize(output_path)
        print(f"✓ Folder compressed to {output_path} ({file_size} bytes)")
        return True
    except Exception as e:
        print(f"✗ Error compressing folder: {e}")
        return False


def extract_archive(archive_path: str, destination_dir: str) -> bool:
    """
    Extract an archive (zip or tar.gz) to a destination directory
    
    Args:
        archive_path: Path to the archive file
        destination_dir: Directory where contents will be extracted
    
    Returns:
        bool: True if extraction successful, False otherwise
    
    Example:
        >>> extract_archive('backup.zip', '/extracted/')
        True
    """
    try:
        if not os.path.exists(archive_path):
            print(f"✗ Archive {archive_path} not found")
            return False
        
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        
        if archive_path.endswith('.zip'):
            with zipfile.ZipFile(archive_path, 'r') as zipf:
                zipf.extractall(destination_dir)
        
        elif archive_path.endswith(('.tar.gz', '.tgz')):
            with tarfile.open(archive_path, 'r:gz') as tarf:
                tarf.extractall(destination_dir)
        
        elif archive_path.endswith('.tar'):
            with tarfile.open(archive_path, 'r') as tarf:
                tarf.extractall(destination_dir)
        
        else:
            print(f"✗ Unsupported archive format")
            return False
        
        print(f"✓ Archive extracted to {destination_dir}")
        return True
    except Exception as e:
        print(f"✗ Error extracting archive: {e}")
        return False


def get_file_size(file_path: str, human_readable: bool = True) -> Optional[str]:
    """
    Get the size of a file
    
    Args:
        file_path: Path to the file
        human_readable: Return size in human-readable format (default: True)
    
    Returns:
        str or int: File size (human-readable string or bytes as int)
    
    Example:
        >>> get_file_size('document.pdf')
        '2.5 MB'
    """
    try:
        if not os.path.exists(file_path):
            print(f"✗ File {file_path} not found")
            return None
        
        size_bytes = os.path.getsize(file_path)
        
        if not human_readable:
            return size_bytes
        
        # Convert to human-readable format
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        
        return f"{size_bytes:.2f} PB"
    except Exception as e:
        print(f"✗ Error getting file size: {e}")
        return None
