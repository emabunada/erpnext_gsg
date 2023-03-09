# Copyright (c) 2023, mohammed abunada and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    # if not filters:
    #     return [], []

    columns, data = [], []
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns(filters=None):
    columns = [
        {"label": _("Employee"), "fieldname": "employee", "fieldtype": "Data"},
        {"label": _("Employee Name"), "fieldname": "employee_name", "fieldtype": "Data"},
        {"label": _("Department"), "fieldname": "department", "fieldtype": "Data"},
        {"label": _("Attendance Date"), "fieldname": "attendance_date", "fieldtype": "Date"},
        {"label": _("Working Hours"), "fieldname": "working_hours", "fieldtype": "Float"},
        {
            "label": _("Check In"),
            "fieldname": "check_in",
            "fieldtype": "Time",
            "width": 80,

        },
        {
            "label": _("Check Out"),
            "fieldname": "check_out",
            "fieldtype": "Time",
            "width": 80,

        },
    ]
    return columns


def get_data(filters):
    new_filters = {}

    if not filters:
        new_filters = {}
    if filters.employee:
        new_filters = {
            "employee": filters.get("employee"),
        }
    if filters.department:
        new_filters = {
            "department": filters.get("department"),
        }
    if filters.from_date and filters.to_date:
        new_filters = {
            "attendance_date": ("between", [filters.get("from_date"), filters.get("to_date")])
        }
    fields = {'employee', 'employee_name', 'department', 'attendance_date', 'check_in', 'check_out'}
    data = frappe.db.get_all('Attendance', fields, filters=new_filters)
    add_working_hours(data)
    return data


def add_working_hours(data):
    for row in data:
        if row.check_in and row.check_out:
            working_hours = frappe.utils.time_diff_in_hours(row.check_out, row.check_in)

            row.working_hours = working_hours
        else:
            working_hours = 0.0
            row.working_hours = working_hours

# "{party_type}:Link/{party_type}".format(party_type=party_type),
# "{party_value_type}::150".format(party_value_type=frappe.unscrub(str(party_type_value))),
