import qrcode
import requests

from frappe.utils import cstr, get_files_path
import os
from frappe.utils.file_manager import save_file
import frappe

@frappe.whitelist()
def create_qrcode(doc, method):
    customer_name = doc.customer_name
    total = doc.grand_total

    # concatenate customer name and total with a separator
    qr_data = f"{customer_name}, {cstr(total)}"

    # set the qrcode API endpoint
    api_url = "https://api.qrserver.com/v1/create-qr-code/"

    # set the parameters for the API request
    params = {
        "data": qr_data,
        "size": "300x300",
        "margin": 4,
        "bgcolor": "ffffff",
        "color": "000000"
    }

    # make the API request to generate the QR code image
    response = requests.get(api_url, params=params)
    print(response.status_code,'kk'*100)

    # get the file name and path for the QR code image
    file_name = f"{doc.name}_qr_code.png"
    file_path = os.path.join(get_files_path(), file_name)
    print(response.content, 'kk' * 100)
    # save QR code image as a file
    with open(file_path, "wb") as f:
        f.write(response.content)

    # create a new File document to store the QR code image
    file_doc = save_file(file_name, open(file_path, "rb").read(), "Sales Invoice", doc.name)

    # create a new link between the File document and the Sales Invoice
    doc.qr_code = file_doc.file_url

