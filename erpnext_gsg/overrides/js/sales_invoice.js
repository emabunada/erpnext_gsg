frappe.ui.form.on('Sales Invoice',  {
    refresh: function(frm) {
    alert("asdsads")
      frappe.call({
      method: "erpnext_gsg.events.vat_tax_event.create_sales_vat_template",
      args: {},
      success: function (r) {},
    });
  },
});
