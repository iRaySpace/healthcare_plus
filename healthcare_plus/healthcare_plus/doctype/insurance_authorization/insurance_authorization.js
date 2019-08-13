// Copyright (c) 2019, Ivan Ray Altomera and contributors
// For license information, please see license.txt

frappe.ui.form.on('Insurance Authorization', {
	refresh: function(frm) {
		cur_frm.doc.visit_number = Math.floor((Math.random()*100000000000)+1);
		cur_frm.set_df_property('visit_number', 'read_only', 1)
		refresh_field('visit_number')
	},
	patient_encounter: function (frm) {
		frappe.call({
			method: 'healthcare_plus.healthcare_plus.doctype.insurance_authorization.insurance_authorization.get_patient_encounter',
			args: {
				name: cur_frm.doc.patient_encounter
			},
			callback: function (r) {
				var fields = ['patient','message','authorized_by','code','description','medical_code', 'visit_date']
				var PE = r.message[0]
				var medical_code = r.message[1]
				cur_frm.doc.patient = PE[1]
				cur_frm.doc.visit_date = r.message[2]
				cur_frm.doc.message = PE[5]
				cur_frm.doc.authorized_by = PE[4]
				cur_frm.doc.code = medical_code[0]['code']
				cur_frm.doc.medical_code = medical_code[0]['medical_code']
				cur_frm.doc.description = medical_code[0]['description']
				for (var i=0; i<fields.length; i++){
					refresh_field(fields[i])
				}
            }
		})
    }
});
