import frappe




@frappe.whitelist()
def set_rate_to_settings(doc,method):
    if doc.hp_insurance_coverage == 1 and doc.party != doc.hp_insurance_provider:
        healthcare_settings = frappe.get_doc('Healthcare Plus Settings', 'Healthcare Plus Settings')
        healthcare_settings.rate = doc.paid_amount
        healthcare_settings.save()
    else:
        print ('Insurance payment')


@frappe.whitelist()
def generate_sales_invoice(doc, method):
    if doc.hp_insurance_coverage==1 and doc.party!=doc.hp_insurance_provider:

        fields = ['insurance_charge_item', 'qty', 'rate', 'insurance_credit_account','insurance_debit_account']
        from_settings = frappe.get_value('Healthcare Plus Settings', 'Healthcare Plus Settings', fields)
        sales_invoice = frappe.get_doc({
            'doctype': 'Sales Invoice',
            'customer': doc.hp_insurance_provider,
            'due_date': doc.posting_date,
            'items': [
                {
                    'item_code': from_settings[0],
                    'qty': from_settings[3],
                    'rate': from_settings[4]
                }
            ],
            'debit_to': from_settings[2],
            'party_type': 'Provider'
        })
        sales_invoice.insert()
        sales_invoice.submit()

        print 'submitted'

    else:
        print ('Patient {0} is not Insurance Covered').format(doc.party)


@frappe.whitelist()
def set_patient(doc,method):
    if doc.hp_insurance_provider:
        patient = frappe.get_value('Patient', {'customer': doc.party})
        doc.patient = patient
