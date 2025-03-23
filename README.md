# XML Invoice Processor

## Overview
This script works with XML files that have invoices and gets the total amount for each invoice where `num_liq='0'`. It shows the extracted data in terminal

## Features
- Reads XML files that are in the Invoice_XML folder inside the Documents folder.
- Extracts the total amount of invoices where num_liq='0'.
- Shows processed invoices and their totals.
- Handles missing or wrong data carefully.

## Requirements
- Python 3.x
- No extra libraries required (uses built-in `os` and `xml.etree.ElementTree`).

## Installation
1. Make sure you have Python 3 installed.
2. Copy the script to your desired location.

## Usage
1. Place your XML invoice files in the `Documents/Invoice_XML` folder.
2. Run the script:
   ```sh
   python ecd.py
   ```
3. The script will show the processed invoices and their totals.

## Example Output
```
Processing: 20211216_X009PM2.xml
Invoice #1: $30,897.26
Invoice #2: $69,916.79
```

## Error Handling
- If the folder is missing, the script will show a message telling you to create it.
- If no XML files are found, the script will inform you.
- If an XML file is not correct, an error message will be shown.

## Folder Structure
```
Documents/
│── XML_files/
│   ├── invoice1.xml
│   ├── invoice2.xml
│   ├── ...
```

## Notes
- Make sure your XML files have the correct structure with <liquidacion num_liq='0'> and <monto_total> fields.
- The script will only process invoices with valid <monto_total> values.


