import os
import urllib.request

# URL of the raw file to fetch
url = "https://raw.githubusercontent.com/Akash-dev2001/OpenUniGit001/main/README.md"

# Folder name to save the fetched file
folder_name = "File"

# Ensure the folder exists
os.makedirs(folder_name, exist_ok=True)

# Extract the file name from the URL
file_name = url.split('/')[-1]
file_path = os.path.join(folder_name, file_name)

try:
    # Fetch the file from the URL and save it
    print(f"Fetching file from: {url}")
    urllib.request.urlretrieve(url, file_path)
    print(f"File successfully saved to: {file_path}")
except urllib.error.URLError as e:
    print(f"Failed to fetch the file: {e.reason}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
