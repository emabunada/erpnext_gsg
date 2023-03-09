// Copyright (c) 2023, mohammed abunada and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Working Hours"] = {
	"filters": [
			{
			"fieldname": "employee",
			"label": __("Employee"),
			"fieldtype": "Data",
			"width": "80",
		},
			{
			"fieldname": "department",
			"label": __("Department"),
			"fieldtype": "Data",
			"width": "80",
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",

		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",

		},

	]
};
