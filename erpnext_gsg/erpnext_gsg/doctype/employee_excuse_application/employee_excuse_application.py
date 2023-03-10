# Copyright (c) 2023, mohammed abunada and contributors
# For license information, please see license.txt
import datetime

import frappe
# import frappe
from frappe.model.document import Document


class EmployeeExcuseapplication(Document):
    def validate(self):
        self.calculate_excuse_hours()

    def calculate_excuse_hours(self):
        self.hours = frappe.utils.time_diff_in_hours(self.to_time, self.from_time)

        if self.hours <= 0:
            frappe.throw('to time must be bigger than from time')

        if self.check_if_applied_after_excuse():
            frappe.throw('apply for excuse must be before the current time ')

        max_excuse_allowed_in_month = frappe.get_doc('Department', self.department).excuse_hours_alowed
        print('* ' * 100, datetime.datetime.now().month)
        total_excuse_in_month = 0.0
        total_excuse_in_month = frappe.db.sql(f"""
        select SUM(hours)as total_hours from `tabEmployee Excuse application` where MONTH(excuse_date) = {datetime.datetime.now().month} and 
        employee = '{self.employee}' and name != '{self.name}' GROUP BY employee
        """, as_dict=1)[0].total_hours

        print('*'*100,self.hours + total_excuse_in_month )
        print('*'*100,max_excuse_allowed_in_month)

        if self.hours + total_excuse_in_month > max_excuse_allowed_in_month:
            frappe.throw('you reach your limit in excuses this month')


    def check_if_applied_after_excuse(self):
        if frappe.utils.date_diff(
                datetime.datetime.now().strftime("%m-%d-%Y"), self.excuse_date) > 0:
            return True

        if frappe.utils.date_diff(
                datetime.datetime.now().strftime("%m-%d-%Y"), self.excuse_date) == 0:
            if frappe.utils.time_diff_in_hours(str(datetime.datetime.now().time()),
                                               self.from_time) > 0:
                return True
        return False
