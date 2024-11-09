import pytesseract
from PIL import Image
import os

# Full absolute path to the folder within your project directory
image_directory = '/Users/brendancarnill/Desktop/OCR_NLP_Project/Listings 09:2024 copy 8' 

# Initialize a dictionary to store the extracted text for each card
ocr_results = {}

# Get a sorted list of all image files
all_files = sorted([f for f in os.listdir(image_directory) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

# Process each card in pairs (back followed by front)
for i in range(0, len(all_files), 2):
    card_number = 1001 + (i // 2)
    back_image_path = os.path.join(image_directory, all_files[i])
    front_image_path = os.path.join(image_directory, all_files[i + 1])

    # Perform OCR on the back image
    back_text = pytesseract.image_to_string(Image.open(back_image_path))
    
    # Perform OCR on the front image
    front_text = pytesseract.image_to_string(Image.open(front_image_path))

    # Store results in the dictionary
    ocr_results[f'card{card_number}'] = {
        'back_text': back_text,
        'front_text': front_text
    }

    # Print the extracted text for verification
    print(f'Card {card_number} Back Text:\n{back_text}\n')
    print(f'Card {card_number} Front Text:\n{front_text}\n')

# Optional: Save the OCR results to a text file
with open('ocr_results.txt', 'w') as file:
    for card, texts in ocr_results.items():
        file.write(f'{card}:\nBack Text:\n{texts["back_text"]}\n\nFront Text:\n{texts["front_text"]}\n\n')
