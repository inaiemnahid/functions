"""
Example usage of PDF utility functions
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.pdf import download_pdf, merge_pdfs, split_pdf, pdf_to_images

def main():
    print("=" * 60)
    print("PDF Utilities Examples")
    print("=" * 60)
    
    # Example 1: Download a PDF
    print("\n1. Download PDF from URL:")
    print("   download_pdf('https://example.com/sample.pdf', 'downloaded.pdf')")
    
    # Example 2: Merge PDFs
    print("\n2. Merge multiple PDFs:")
    print("   merge_pdfs(['file1.pdf', 'file2.pdf', 'file3.pdf'], 'merged.pdf')")
    
    # Example 3: Split PDF
    print("\n3. Split PDF into separate pages:")
    print("   split_pdf('document.pdf', 'output_pages/', pages_per_file=1)")
    
    # Example 4: Convert PDF to images
    print("\n4. Convert PDF pages to images:")
    print("   pdf_to_images('document.pdf', 'images/', dpi=300)")
    
    print("\n" + "=" * 60)
    print("To use these functions, import them:")
    print("from utils.pdf import download_pdf, merge_pdfs, split_pdf, pdf_to_images")
    print("=" * 60)

if __name__ == "__main__":
    main()
