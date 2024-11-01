# Image Alt Text Extractor

This Python script crawls a specified website to extract all image elements and their alternative text entries. It identifies missing, empty, and valid `alt` attributes, along with keywords related to image formats.

## Features

- Fetches and parses HTML content from a given URL.
- Extracts `src` and `alt` attributes from image tags.
- Categorizes images into:
  - Missing or empty `alt` text entries
  - Valid `alt` text entries
- Searches for specific keywords in valid `alt` text and `src` attributes.

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup4 library

## Installation

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Set the `base_url` variable to the target website URL.
2. Run the script to extract the image information.

```python
# Example usage
base_url = "https://example.com/"
```

## Output

The script prints:

- Found entries with specific keywords in `alt` text and `src`.
- Missing or empty `alt` text entries.
- Valid `alt` text entries.

If no entries are found in any category, a message "Nothing found." will be displayed.

## Example

```python
# Output Example
#### Found entries with keywords ####
Entry 1: alt='Example Image', src='https://example.com/image.jpg'

#### Missing or empty alt text #####
Nothing found.

#### Valid alt text entries #####
Image 1: alt='Valid Alt Text', src='https://example.com/valid-image.jpg'
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the GNU General Public License (GPL)  - see the [LICENSE](LICENSE) file for details.
