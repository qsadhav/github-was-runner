from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
import sys

def json_to_pdf(json_file, pdf_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setFont("Helvetica", 10)
    
    y_position = 750  # Adjust Y position for text placement

    for key, value in data.items():
        text = f"{key}: {value}"
        c.drawString(100, y_position, text)
        y_position -= 20  # Move down for the next line

        if y_position < 50:  # Create a new page if the text exceeds limits
            c.showPage()
            c.setFont("Helvetica", 10)
            y_position = 750

    c.save()

if __name__ == "__main__":
    json_file = sys.argv[1]
    pdf_file = sys.argv[2]
    json_to_pdf(json_file, pdf_file)
