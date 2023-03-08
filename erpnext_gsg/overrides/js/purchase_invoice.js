

frappe.ui.form.on('Purchase Invoice',  {
    refresh: function(frm) {
      frappe.call({
      method: "erpnext_gsg.events.vat_tax_event.create_purchase_vat_template",
      args: {},
      success: function (r) {},
    });
  },

});
