"""
Example usage of Image utility functions
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.image import resize_image, convert_image, update_resolution, compress_image, create_thumbnail

def main():
    print("=" * 60)
    print("Image Utilities Examples")
    print("=" * 60)
    
    # Example 1: Resize image
    print("\n1. Resize an image (maintaining aspect ratio):")
    print("   resize_image('photo.jpg', 'resized.jpg', (800, 600), keep_aspect=True)")
    
    # Example 2: Convert image format
    print("\n2. Convert image from PNG to JPEG:")
    print("   convert_image('image.png', 'image.jpg', 'JPEG')")
    
    # Example 3: Update resolution
    print("\n3. Update image resolution to 300 DPI:")
    print("   update_resolution('image.png', 'high_res.png', (300, 300))")
    
    # Example 4: Compress image
    print("\n4. Compress image to reduce file size:")
    print("   compress_image('large_photo.jpg', 'compressed.jpg', quality=75)")
    
    # Example 5: Create thumbnail
    print("\n5. Create a thumbnail:")
    print("   create_thumbnail('photo.jpg', 'thumbnail.jpg', (200, 200))")
    
    print("\n" + "=" * 60)
    print("To use these functions, import them:")
    print("from utils.image import resize_image, convert_image, update_resolution")
    print("=" * 60)

if __name__ == "__main__":
    main()
