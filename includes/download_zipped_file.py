import requests


# Step 3: Python function to download a zip file
def download_zipped_file(url, save_path):
    # Note: You don't need to reassign these parameters since they'll be passed through op_kwargs
    zipped_files = requests.get(url)
    # Use the save_path parameter directly, not as a string
    with open(save_path, "wb") as f:
        f.write(zipped_files.content)
    print(f"File downloaded successfully and saved to: {save_path}")
