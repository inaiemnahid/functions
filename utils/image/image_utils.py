"""
Image utility functions for resizing, converting, and manipulating images
"""

import os
from typing import Tuple, Optional


def resize_image(input_path: str, output_path: str, size: Tuple[int, int], 
                 keep_aspect: bool = True) -> bool:
    """
    Resize an image to specified dimensions
    
    Args:
        input_path: Path to the input image
        output_path: Path for the output image
        size: Tuple of (width, height) in pixels
        keep_aspect: Whether to maintain aspect ratio (default: True)
    
    Returns:
        bool: True if resize successful, False otherwise
    
    Example:
        >>> resize_image('photo.jpg', 'resized.jpg', (800, 600))
        True
    """
    try:
        from PIL import Image
        
        with Image.open(input_path) as img:
            if keep_aspect:
                img.thumbnail(size, Image.Resampling.LANCZOS)
            else:
                img = img.resize(size, Image.Resampling.LANCZOS)
            
            img.save(output_path)
        
        print(f"✓ Image resized successfully to {output_path}")
        return True
    except ImportError:
        print("✗ Pillow not installed. Install with: pip install Pillow")
        return False
    except Exception as e:
        print(f"✗ Error resizing image: {e}")
        return False


def convert_image(input_path: str, output_path: str, output_format: Optional[str] = None) -> bool:
    """
    Convert an image from one format to another
    
    Args:
        input_path: Path to the input image
        output_path: Path for the output image
        output_format: Output format (e.g., 'PNG', 'JPEG', 'WEBP'). 
                       If None, inferred from output_path extension
    
    Returns:
        bool: True if conversion successful, False otherwise
    
    Example:
        >>> convert_image('photo.png', 'photo.jpg', 'JPEG')
        True
    """
    try:
        from PIL import Image
        
        with Image.open(input_path) as img:
            # Convert RGBA to RGB for formats that don't support transparency
            if output_format in ['JPEG', 'JPG'] or output_path.lower().endswith(('.jpg', '.jpeg')):
                if img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
            
            if output_format:
                img.save(output_path, format=output_format)
            else:
                img.save(output_path)
        
        print(f"✓ Image converted successfully to {output_path}")
        return True
    except ImportError:
        print("✗ Pillow not installed. Install with: pip install Pillow")
        return False
    except Exception as e:
        print(f"✗ Error converting image: {e}")
        return False


def update_resolution(input_path: str, output_path: str, dpi: Tuple[int, int]) -> bool:
    """
    Update the DPI (resolution) metadata of an image
    
    Args:
        input_path: Path to the input image
        output_path: Path for the output image
        dpi: Tuple of (horizontal_dpi, vertical_dpi)
    
    Returns:
        bool: True if update successful, False otherwise
    
    Example:
        >>> update_resolution('image.png', 'high_res.png', (300, 300))
        True
    """
    try:
        from PIL import Image
        
        with Image.open(input_path) as img:
            img.save(output_path, dpi=dpi)
        
        print(f"✓ Image resolution updated to {dpi} DPI at {output_path}")
        return True
    except ImportError:
        print("✗ Pillow not installed. Install with: pip install Pillow")
        return False
    except Exception as e:
        print(f"✗ Error updating resolution: {e}")
        return False


def compress_image(input_path: str, output_path: str, quality: int = 85) -> bool:
    """
    Compress an image by reducing quality
    
    Args:
        input_path: Path to the input image
        output_path: Path for the output image
        quality: Quality level (1-100, higher is better quality but larger file)
    
    Returns:
        bool: True if compression successful, False otherwise
    
    Example:
        >>> compress_image('large_photo.jpg', 'compressed.jpg', quality=75)
        True
    """
    try:
        from PIL import Image
        
        if not 1 <= quality <= 100:
            print("✗ Quality must be between 1 and 100")
            return False
        
        with Image.open(input_path) as img:
            # Get original file size
            original_size = os.path.getsize(input_path)
            
            # Convert RGBA to RGB for JPEG
            if output_path.lower().endswith(('.jpg', '.jpeg')) and img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            img.save(output_path, quality=quality, optimize=True)
            
            # Get new file size
            new_size = os.path.getsize(output_path)
            reduction = ((original_size - new_size) / original_size) * 100
            
            print(f"✓ Image compressed successfully to {output_path}")
            print(f"  Size reduced by {reduction:.1f}% ({original_size} → {new_size} bytes)")
        
        return True
    except ImportError:
        print("✗ Pillow not installed. Install with: pip install Pillow")
        return False
    except Exception as e:
        print(f"✗ Error compressing image: {e}")
        return False


def create_thumbnail(input_path: str, output_path: str, size: Tuple[int, int] = (128, 128)) -> bool:
    """
    Create a thumbnail of an image
    
    Args:
        input_path: Path to the input image
        output_path: Path for the thumbnail
        size: Maximum size for the thumbnail (default: 128x128)
    
    Returns:
        bool: True if thumbnail creation successful, False otherwise
    
    Example:
        >>> create_thumbnail('photo.jpg', 'thumb.jpg', (200, 200))
        True
    """
    try:
        from PIL import Image
        
        with Image.open(input_path) as img:
            img.thumbnail(size, Image.Resampling.LANCZOS)
            img.save(output_path)
        
        print(f"✓ Thumbnail created successfully at {output_path}")
        return True
    except ImportError:
        print("✗ Pillow not installed. Install with: pip install Pillow")
        return False
    except Exception as e:
        print(f"✗ Error creating thumbnail: {e}")
        return False
