import frappe


@frappe.whitelist()
def create_purchase_vat_template():
    accounts = frappe.get_list("Account", filters={"root_type": 'Expense' or ''})
    parent_account = accounts[0].name
    account_name = 'Purchase Vat Account'
    if not check_if_account_exist(account=account_name):
        create_account(account_name=account_name, parent_account=parent_account, account_type='Chargeable')
    vat_account_name = frappe.get_list("Account", filters={"account_name": account_name})[0].name
    vat_title = "Purchase Tax 16%"
    if not check_if_vat_exist(vat_title):
        create_tax(vat_title, vat_account_name, vat_type="Purchase Taxes and Charges Template")


@frappe.whitelist()
def create_sales_vat_template():
    accounts = frappe.get_list("Account", filters={"root_type": 'Income' or ''})
    parent_account = accounts[0].name
    account_name = 'Sales Vat Account'
    if not check_if_account_exist(account=account_name):
        create_account(account_name=account_name, parent_account=parent_account, account_type='Chargeable')
    vat_account_name = check_if_account_exist(account=account_name)[0].name
    vat_title = "Sales Tax 16%"
    if not check_if_vat_exist(vat_title):
        create_tax(vat_title, vat_account_name, vat_type="Sales Taxes and Charges Template")


def create_account(account_name, parent_account, account_type):
    company_global = frappe.get_doc('Global Defaults')
    new_account = frappe.new_doc('Account')
    new_account.account_name = account_name
    new_account.account_type = account_type
    new_account.account_currency = company_global.default_currency
    new_account.company = company_global.default_company
    new_account.parent_account = parent_account
    new_account.insert(ignore_permissions=1)
    frappe.db.commit()


def check_if_account_exist(account):
    accounts = frappe.get_list("Account", filters={"account_name": account})
    print(accounts)
    return accounts


def check_if_vat_exist(vat_name):
    taxes = frappe.get_list("Purchase Taxes and Charges Template", filters={"title": vat_name})
    print(taxes)
    return taxes


def create_tax(vat_title, vat_account_name, vat_type):
    tax_template = frappe.new_doc(vat_type)
    tax_template.title = vat_title

    tax_template.is_default = 1
    tax_template.append("taxes", {
        "type": "On Net Total",
        'charge_type': "On Net Total",
        "account_head": vat_account_name,
        "description": f"{vat_type} Tax 16%",
        "rate": 16
    })

    # tax_template.tax_type = "On Net Total"
    tax_template.insert()
