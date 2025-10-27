# Helpful Utility Functions

A comprehensive collection of helpful utility functions for common tasks including PDF operations, image manipulation, file management, and command helpers.

## 📚 Features

### 🔴 PDF Utilities
- **Download PDF**: Download PDF files from URLs
- **Merge PDFs**: Combine multiple PDF files into one
- **Split PDF**: Split a PDF into individual pages or chunks
- **PDF to Images**: Convert PDF pages to image files

### 🔵 Image Utilities
- **Resize Image**: Resize images with aspect ratio control
- **Convert Image**: Convert between image formats (PNG, JPEG, WEBP, etc.)
- **Update Resolution**: Change image DPI/resolution metadata
- **Compress Image**: Reduce image file size
- **Create Thumbnail**: Generate thumbnails from images

### 🟢 File Utilities
- **Copy Files**: Copy multiple files to a destination
- **Move Files**: Move files between directories
- **Delete Files**: Safely delete files with confirmation
- **Compress Folder**: Create ZIP or TAR.GZ archives
- **Extract Archive**: Extract files from archives
- **Get File Size**: Get file sizes in human-readable format

### 🟡 Command Utilities
- **Common Commands List**: Organized list of useful shell commands
- **Execute Command**: Run shell commands from Python
- **System Info**: Get detailed system information
- **Print Commands**: Display commands by category

### 🟣 Text Utilities
- **Count Words/Characters**: Count words and characters in text
- **Case Conversion**: Convert to snake_case, camelCase, kebab-case, etc.
- **Extract Emails/URLs**: Extract email addresses and URLs from text
- **Truncate Text**: Truncate long text with ellipsis
- **Remove HTML Tags**: Strip HTML tags from text
- **Text Manipulation**: Reverse, replace multiple, remove extra spaces

### 🟠 Network Utilities
- **Check Connection**: Test internet connectivity
- **Get IP Address**: Get local machine IP address
- **URL Validation**: Validate and parse URLs
- **Build URLs**: Construct URLs with query parameters
- **Domain Extraction**: Extract domain from URLs
- **Port Check**: Check if a port is open

### 🔷 Data Utilities
- **JSON Operations**: Read, write, and pretty print JSON
- **CSV Operations**: Read and write CSV files
- **Format Conversion**: Convert between JSON and CSV
- **Dictionary Operations**: Flatten, merge, and filter dictionaries

### 🕐 DateTime Utilities
- **Current Date/Time**: Get current timestamps in various formats
- **Date Parsing**: Parse and format dates
- **Date Math**: Add days/hours, calculate age, days between dates
- **Date Info**: Check if weekend, get day/month names
- **Time Ago**: Human-readable time differences

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/inaiemnahid/functions.git
cd functions
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) For PDF to image conversion, install poppler:
```bash
# Ubuntu/Debian
sudo apt-get install poppler-utils

# macOS
brew install poppler

# Windows
# Download from: https://github.com/oschwartz10612/poppler-windows/releases/
```

## 🎯 Quick Demo

Run the demo script to see all available utilities:
```bash
python demo.py
```

Or run the demo with:
```bash
./demo.py  # if you made it executable
```

## 📖 Usage

### PDF Utilities

```python
from utils.pdf import download_pdf, merge_pdfs, split_pdf, pdf_to_images

# Download a PDF
download_pdf('https://example.com/file.pdf', 'output.pdf')

# Merge multiple PDFs
merge_pdfs(['file1.pdf', 'file2.pdf'], 'merged.pdf')

# Split PDF into individual pages
split_pdf('document.pdf', 'output_pages/', pages_per_file=1)

# Convert PDF pages to images
pdf_to_images('document.pdf', 'images/', dpi=300)
```

### Image Utilities

```python
from utils.image import resize_image, convert_image, compress_image, create_thumbnail

# Resize an image
resize_image('photo.jpg', 'resized.jpg', (800, 600), keep_aspect=True)

# Convert image format
convert_image('image.png', 'image.jpg', 'JPEG')

# Compress image
compress_image('large.jpg', 'compressed.jpg', quality=75)

# Create thumbnail
create_thumbnail('photo.jpg', 'thumb.jpg', (200, 200))
```

### File Utilities

```python
from utils.file import copy_files, compress_folder, extract_archive, get_file_size

# Copy multiple files
copy_files(['file1.txt', 'file2.txt'], '/backup/', overwrite=True)

# Compress a folder
compress_folder('/data/myproject', 'backup.zip', format='zip')

# Extract archive
extract_archive('backup.zip', '/extracted/')

# Get file size
size = get_file_size('document.pdf')  # Returns: '2.5 MB'
```

### Command Utilities

```python
from utils.commands import get_common_commands, execute_command, get_system_info

# Get common commands by category
commands = get_common_commands()
git_commands = commands['git']

# Execute a shell command
result = execute_command('ls -l')
if result['success']:
    print(result['stdout'])

# Get system information
info = get_system_info()
print(f"OS: {info['system']} {info['release']}")
```

### Text Utilities

```python
from utils.text import count_words, to_snake_case, extract_emails, truncate_text

# Count words in text
word_count = count_words("Hello world, this is a test")

# Convert to snake_case
snake = to_snake_case("Hello World Example")  # 'hello_world_example'

# Extract emails from text
emails = extract_emails("Contact: info@example.com or support@test.org")

# Truncate long text
short = truncate_text("This is a very long text", 10)  # 'This is...'
```

### Network Utilities

```python
from utils.network import check_internet_connection, parse_url, build_url

# Check internet connection
is_online = check_internet_connection()

# Parse URL
components = parse_url("https://example.com:8080/path?key=value")

# Build URL with parameters
url = build_url("https://api.example.com", {"q": "search", "page": "1"})
```

### Data Utilities

```python
from utils.data import read_json, write_csv, flatten_dict, merge_dicts

# Read and write JSON
data = read_json('data.json')
write_json(data, 'output.json')

# CSV operations
csv_data = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
write_csv(csv_data, 'output.csv')

# Flatten nested dictionary
flat = flatten_dict({'user': {'name': 'John', 'city': 'NYC'}})

# Merge dictionaries
merged = merge_dicts({'a': 1}, {'b': 2}, {'c': 3})
```

### DateTime Utilities

```python
from utils.datetime import get_current_date, add_days, calculate_age, time_ago

# Get current date
today = get_current_date()  # '2025-10-27'

# Add days to date
future = add_days(7)  # 7 days from now

# Calculate age
from utils.datetime import parse_date
birth = parse_date('1990-01-01')
age = calculate_age(birth)

# Human-readable time difference
past = add_days(-2)
ago = time_ago(past)  # '2 days ago'
```

## 🔍 Examples

Check out the `examples/` directory for detailed usage examples:
- `examples/pdf_examples.py` - PDF utility examples
- `examples/image_examples.py` - Image utility examples
- `examples/file_examples.py` - File utility examples
- `examples/command_examples.py` - Command utility examples
- `examples/text_examples.py` - Text utility examples
- `examples/network_examples.py` - Network utility examples
- `examples/data_examples.py` - Data utility examples
- `examples/datetime_examples.py` - DateTime utility examples
- `examples/command_examples.py` - Command utility examples

Run examples:
```bash
python examples/pdf_examples.py
python examples/image_examples.py
python examples/file_examples.py
python examples/command_examples.py
```

## 📋 Requirements

- Python 3.7+
- requests
- Pillow
- PyPDF2
- pdf2image
- poppler-utils (system package, for PDF to image conversion)

## 🛠️ Project Structure

```
functions/
├── utils/
│   ├── __init__.py
│   ├── pdf/
│   │   ├── __init__.py
│   │   └── pdf_utils.py
│   ├── image/
│   │   ├── __init__.py
│   │   └── image_utils.py
│   ├── file/
│   │   ├── __init__.py
│   │   └── file_utils.py
│   └── commands/
│       ├── __init__.py
│       └── command_utils.py
├── examples/
│   ├── pdf_examples.py
│   ├── image_examples.py
│   ├── file_examples.py
│   └── command_examples.py
├── requirements.txt
├── README.md
└── LICENSE
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new utility functions
- Improve existing functions
- Fix bugs
- Add more examples
- Improve documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

MD. Naiem Islam Nahid

## ⭐ Support

If you find this repository helpful, please give it a star ⭐
