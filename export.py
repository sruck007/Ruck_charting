import csv
import json
from fpdf import FPDF

def create_export(format):
    data = {"content": "Sample transcription"}  # Example data
    if format == 'csv':
        file_path = 'transcription.csv'
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data.keys())
            writer.writerow(data.values())
        return file_path
    elif format == 'json':
        file_path = 'transcription.json'
        with open(file_path, 'w') as jsonfile:
            json.dump(data, jsonfile)
        return file_path
    elif format == 'pdf':
        file_path = 'transcription.pdf'
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, json.dumps(data, indent=2))
        pdf.output(file_path)
        return file_path
