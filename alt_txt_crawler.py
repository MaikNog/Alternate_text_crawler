import requests
from bs4 import BeautifulSoup

# Example usage
base_url = "https://hanseatictester.info/accessibility-demo-site/"
# base_url = "https://louisville.edu/faculty/cagrap01/images/img1.jpg/view"


def extract_image_alts(url):
    try:
        # Fetch content from URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        html_content = response.text

        # Parse HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract all image tags and their alt text
        images = soup.find_all('img')
        missing_alt_texts = []
        present_alt_texts = []

        for img in images:
            src_attr = img.get('src', 'No src attribute')  # Get image source attribute
            if 'alt' in img.attrs:
                alt_text = img.get('alt')
                if alt_text == "":  # If alt is present but empty
                    missing_alt_texts.append((src_attr, "Alt text is empty"))
                else:
                    present_alt_texts.append((src_attr, alt_text))
            else:
                # If 'alt' attribute is missing
                missing_alt_texts.append((src_attr, "No alt attribute"))

        return missing_alt_texts, present_alt_texts  # Return both lists separately

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return [], []


def check_image_keywords(present_alt_texts):
    # Keywords to search for in alt text or src
    keywords = ["img", ".jpg", ".png", ".gif", ".jpeg"]
    found_entries = []

    # Search for keywords in present_alt_texts
    for src_key, alt_key in present_alt_texts:
        if any(keyword in alt_key.lower() for keyword in keywords):
            found_entries.append((src_key, alt_key))

    return found_entries


# Extract the URL from the two lists
missing_alt_texts_result, present_alt_texts_result = extract_image_alts(base_url)

# Check for specific keywords in present_alt_texts
found_entries_result = check_image_keywords(present_alt_texts_result)

# Print found entries with keywords
if found_entries_result:
    print("\n#### Found entries with keywords ####")
    for idx, (src, alt) in enumerate(found_entries_result, start=1):
        print(f"Entry {idx}: alt='{alt}', src='{src}'")
    print("")
else:
    print("\nNo entries found with specified keywords.")

# Print block separator
print("#### Missing or empty alt text #####")

if missing_alt_texts_result:
    # Print missing or empty alt text entries
    for idx, (src, alt) in enumerate(missing_alt_texts_result, start=1):
        print(f"Image {idx}: alt='{alt}', src='{src}'")
    print("")
else:
    print("--------- Nothing found ------------")
    print("")

# Print block separator
print("#### Valid at text entries #####")

if present_alt_texts_result:
    # Print entries with valid alt text
    for idx, (src, alt) in enumerate(present_alt_texts_result, start=len(missing_alt_texts_result) + 1):
        print(f"Image {idx}: alt='{alt}', src='{src}'")
    print("")
else:
    print("--------- Nothing found ------------")
    print("")
