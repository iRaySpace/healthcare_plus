# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ivan Ray Altomera and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta

class InsuranceAuthorization(Document):
	pass




@frappe.whitelist()
def get_patient_encounter(name):

	PE_fields = ["name", "patient", "encounter_date", "encounter_time", "practitioner", 'encounter_comment']
	PE = frappe.get_value('Patient Encounter', name, PE_fields)

	code_fields = ['medical_code', 'code', 'description']
	code = frappe.get_all('Codification Table', {'parent': PE[0]}, code_fields)

	return PE, code, to_datetime(PE[2],PE[3])



def to_datetime(d,t):
	date = d.strftime('%Y-%m-%d')
	time = str(t)
	d = date+" "+time
	return datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
