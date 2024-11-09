import os
import re

# Path to the folder containing your scanned images
image_directory = './Listings 09:2024 copy 8'

# List all files in the directory and ensure they are in the natural order
all_files = sorted(
    [f for f in os.listdir(image_directory) if f.lower().startswith('scan')],
    key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0
)

# Move 'Scan.jpeg' to the start if it exists
if 'Scan.jpeg' in all_files:
    all_files.remove('Scan.jpeg')
    all_files.insert(0, 'Scan.jpeg')

# Initialize card number
card_number = 1001

# Rename images
for i in range(0, len(all_files), 8):
    # Rename the first 4 images in the batch as fronts
    for j in range(4):
        if i + j < len(all_files):  # Ensure we don't go out of range
            old_path = os.path.join(image_directory, all_files[i + j])
            new_name = f'card{card_number + j}f.jpg'
            new_path = os.path.join(image_directory, new_name)
            os.rename(old_path, new_path)
            print(f'Renamed {all_files[i + j]} to {new_name}')
    
    # Rename the next 4 images in the batch as backs
    for j in range(4):
        if i + 4 + j < len(all_files):  # Ensure we don't go out of range
            old_path = os.path.join(image_directory, all_files[i + 4 + j])
            new_name = f'card{card_number + j}b.jpg'
            new_path = os.path.join(image_directory, new_name)
            os.rename(old_path, new_path)
            print(f'Renamed {all_files[i + 4 + j]} to {new_name}')
    
    # Increment card number by 4 for the next batch
    card_number += 4
