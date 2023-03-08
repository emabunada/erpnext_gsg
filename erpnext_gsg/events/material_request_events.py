import frappe
from erpnext.stock.doctype.material_request.material_request import  make_stock_entry
@frappe.whitelist()
def create_stock_entry(doc, method):
    if doc.material_request_type == 'Material Issue':
        stock_entry = make_stock_entry(doc.name)
        stock_entry.save()
        stock_entry.submit()
        frappe.db.commit()


