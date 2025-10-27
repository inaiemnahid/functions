"""
PDF utility functions for downloading, merging, splitting, and converting PDFs
"""

import os
import requests
from typing import List, Optional


def download_pdf(url: str, output_path: str, timeout: int = 30) -> bool:
    """
    Download a PDF file from a URL
    
    Args:
        url: URL of the PDF file to download
        output_path: Path where the PDF should be saved
        timeout: Request timeout in seconds (default: 30)
    
    Returns:
        bool: True if download successful, False otherwise
    
    Example:
        >>> download_pdf('https://example.com/file.pdf', 'output.pdf')
        True
    """
    try:
        response = requests.get(url, timeout=timeout, stream=True)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✓ PDF downloaded successfully to {output_path}")
        return True
    except Exception as e:
        print(f"✗ Error downloading PDF: {e}")
        return False


def merge_pdfs(pdf_list: List[str], output_path: str) -> bool:
    """
    Merge multiple PDF files into one
    
    Args:
        pdf_list: List of PDF file paths to merge
        output_path: Path for the merged PDF output
    
    Returns:
        bool: True if merge successful, False otherwise
    
    Example:
        >>> merge_pdfs(['file1.pdf', 'file2.pdf'], 'merged.pdf')
        True
    """
    try:
        from PyPDF2 import PdfMerger
        
        merger = PdfMerger()
        for pdf in pdf_list:
            if os.path.exists(pdf):
                merger.append(pdf)
            else:
                print(f"Warning: {pdf} not found, skipping...")
        
        merger.write(output_path)
        merger.close()
        
        print(f"✓ PDFs merged successfully to {output_path}")
        return True
    except ImportError:
        print("✗ PyPDF2 not installed. Install with: pip install PyPDF2")
        return False
    except Exception as e:
        print(f"✗ Error merging PDFs: {e}")
        return False


def split_pdf(input_path: str, output_dir: str, pages_per_file: int = 1) -> bool:
    """
    Split a PDF file into multiple files
    
    Args:
        input_path: Path to the PDF file to split
        output_dir: Directory where split PDFs will be saved
        pages_per_file: Number of pages per output file (default: 1)
    
    Returns:
        bool: True if split successful, False otherwise
    
    Example:
        >>> split_pdf('large.pdf', 'output_dir/', pages_per_file=2)
        True
    """
    try:
        from PyPDF2 import PdfReader, PdfWriter
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        reader = PdfReader(input_path)
        total_pages = len(reader.pages)
        
        file_count = 0
        for start_page in range(0, total_pages, pages_per_file):
            writer = PdfWriter()
            end_page = min(start_page + pages_per_file, total_pages)
            
            for page_num in range(start_page, end_page):
                writer.add_page(reader.pages[page_num])
            
            output_filename = os.path.join(
                output_dir, 
                f"split_{file_count + 1}.pdf"
            )
            with open(output_filename, 'wb') as output_file:
                writer.write(output_file)
            
            file_count += 1
        
        print(f"✓ PDF split into {file_count} files in {output_dir}")
        return True
    except ImportError:
        print("✗ PyPDF2 not installed. Install with: pip install PyPDF2")
        return False
    except Exception as e:
        print(f"✗ Error splitting PDF: {e}")
        return False


def pdf_to_images(input_path: str, output_dir: str, dpi: int = 200, 
                  image_format: str = 'PNG') -> bool:
    """
    Convert PDF pages to images
    
    Args:
        input_path: Path to the PDF file
        output_dir: Directory where images will be saved
        dpi: Resolution for the output images (default: 200)
        image_format: Output image format (default: 'PNG')
    
    Returns:
        bool: True if conversion successful, False otherwise
    
    Example:
        >>> pdf_to_images('document.pdf', 'images/', dpi=300)
        True
    """
    try:
        from pdf2image import convert_from_path
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        images = convert_from_path(input_path, dpi=dpi)
        
        for i, image in enumerate(images):
            image_path = os.path.join(
                output_dir,
                f"page_{i + 1}.{image_format.lower()}"
            )
            image.save(image_path, image_format)
        
        print(f"✓ Converted {len(images)} pages to images in {output_dir}")
        return True
    except ImportError:
        print("✗ pdf2image not installed. Install with: pip install pdf2image")
        print("  Also install poppler-utils: sudo apt-get install poppler-utils")
        return False
    except Exception as e:
        print(f"✗ Error converting PDF to images: {e}")
        return False
