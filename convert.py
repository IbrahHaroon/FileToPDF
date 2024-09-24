from PIL import Image
from fpdf import FPDF
import os

# Convert an image to a PDF
def imageToPDF(image, output):
    try:
        with Image.open(image) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(output)
        print("Converted" + image "to" + output)
    except Exception as e:
        print("Error converting" +  image + ":" + e)