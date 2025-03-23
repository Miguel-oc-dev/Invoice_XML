import os
import xml.etree.ElementTree as ET

# The location of the folder 'Invoice_XML' must be into Documents without OneDrive folder
documents_path = os.path.join(os.path.expanduser( "~" ), "Documents")
xml_folder = os.path.join(documents_path, "XML_files") 

def process_XMLFile(xml_path):
    # Process a XML File and get the totals from the invoice into liq='0'
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        invoice_totals = []

        # Search in all invoices inside liquidacion num_liq="0"
        for liquidation in root.findall(".//liquidacion[@num_liq='0']"):
            for invoice in liquidation.findall(".//factura"):
                total = sum(
                    float(concept.find("monto_total").text)
                    for concept in invoice.findall(".//concepto")
                    if concept.find("monto_total") is not None
                )
                invoice_totals.append(total)
                
        result = [f"Processing {os.path.basename(xml_path)}\n"]
        for i, total in enumerate(invoice_totals, 1):
            result.append(f"Invoice #{i}: ${total:,.2f}")

        return "\n".join(result)
    
    except Exception as e:
        return f"Error processing {os.path.basename(xml_path)}: {str(e)}"


def process_folder(xml_folder):
    # Process all XML files in the folder
    if not os.path.exists(xml_folder):
        return f"The folder '{xml_folder}' does not exist. Add the XML files"
    
    xml_files = [f for f in os.listdir(xml_folder) if f.endswith(".xml")]
    
    if not xml_files:
        return "No XML files found in the folder"

    results = []

    for file in xml_files:
        xml_path = os.path.join(xml_folder, file)
        results.append(process_XMLFile(xml_path))

    return "\n\n".join(results)
    
print(process_folder(xml_folder))