import frappe


def execute():
    print('5'*500)
    frappe.db.sql(""" update `tabSales Order` set sales_order_time = Time('12:00') where sales_order_time = null """)
