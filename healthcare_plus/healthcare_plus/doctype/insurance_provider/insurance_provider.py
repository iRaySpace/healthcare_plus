# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ivan Ray Altomera and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class InsuranceProvider(Document):

	def validate(self):
		name = frappe.get_value('Customer', self.ip_name)
		print name
		if name==None:
			cust_doc = frappe.get_doc({
				'doctype': 'Customer',
				'customer_name': self.ip_name
			})
			cust_doc.insert()
			if cust_doc:
				#print ("Customer "+self.ip_name+" is created.")
			self.customer = self.ip_name
		else:

			#print ("Customer "+self.ip_name+" already exist.")
			self.customer = self.ip_name
