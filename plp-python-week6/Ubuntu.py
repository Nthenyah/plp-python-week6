import requests
import os
from urllib.parse import urlparse

def fetch_image(url, downloaded_files):
    try:
        # Fetch the image with headers
        headers = {"User-Agent": "Ubuntu-Image-Fetcher/1.0"}
        response = requests.get(url, headers=headers, timeout=10, stream=True)
        response.raise_for_status()

        # Check important headers
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > 5_000_000:  # 5 MB limit
            print(f"✗ Skipped (too large): {url}")
            return

        # Extract filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

        # Avoid duplicates
        if filename in downloaded_files:
            print(f"✗ Skipped (duplicate): {filename}")
            return

        # Save image
        filepath = os.path.join("Fetched_Images", filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        downloaded_files.add(filename)
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory if it doesn’t exist
    os.makedirs("Fetched_Images", exist_ok=True)

    # Get multiple URLs
    urls = input("Please enter image URLs separated by commas: ").split(",")

    downloaded_files = set()

    for url in urls:
        url = url.strip()
        if url:
            fetch_image(url, downloaded_files)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
