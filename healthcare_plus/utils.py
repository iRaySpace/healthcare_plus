import frappe

def sample():
    item = frappe.get_value('Healthcare Plus Settings', 'Healthcare Plus Settings', ['insurance_charge_item', 'debit_to'])
    print item[0]
    print item[1]




@frappe.whitelist()
def generate_sales_invoice(doc, method):
    if doc.hp_insurance_coverage==1:
        from_settings = frappe.get_value('Healthcare Plus Settings', 'Healthcare Plus Settings', ['insurance_charge_item', 'qty'])
        sales_invoice = frappe.get_doc({
            'doctype': 'Sales Invoice',
            'customer': doc.hp_insurance_provider,
            'due_date': doc.posting_date,
            'items': [
                {
                    'item_code': from_settings[0],
                    'qty': from_settings[1]
                }
            ],
            'debit_to': doc.paid_from,
            'party_type': 'Provider'
        })
        sales_invoice.insert()
        sales_invoice.submit()
        print 'submitted'