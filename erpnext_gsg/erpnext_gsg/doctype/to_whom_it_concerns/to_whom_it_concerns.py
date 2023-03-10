# Copyright (c) 2023, mohammed abunada and contributors
# For license information, please see license.txt
import frappe
# import frappe
from frappe.model.document import Document


class ToWhomItConcerns(Document):
    pass


@frappe.whitelist()
def get_salary(employee):
    print('*' * 100, employee)
    salaries = frappe.db.sql(f"""
	select net_pay , end_date from	`tabSalary Slip` where employee = '{employee}' ORDER BY end_date DESC
""", as_dict=1)
    if salaries:
        return salaries[0].net_pay
    else:
        return 0.0
