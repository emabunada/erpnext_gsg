frappe.ui.form.on('Sales Invoice',  {
    setup: function(frm) {
      frappe.call({
      method: "erpnext_gsg.events.vat_tax_events.create_sales_vat_template",
      args: {},
      success: function (r) {},
    });
  },
});
