/**
 * Created by bai on 7/30/19.
 */
frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
	},
    insurance_covered: function (frm) {
        var is_required
        if (cur_frm.doc.insurance_covered==1){
            is_required = 1
        }else{
            is_required = 0
        }
        cur_frm.set_df_property("ref_practitioner", "reqd", is_required);
        cur_frm.set_df_property("billed_by", "reqd", is_required);
    }
});
