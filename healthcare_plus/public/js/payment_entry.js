/**
 * Created by bai on 7/30/19.
 */
cur_frm.cscript.hp_insurance_coverage= function (frm) {
	if (cur_frm.doc.hp_insurance_coverage==1){
		cur_frm.set_df_property("hp_insurance_provider", "reqd", 1);
		console.log("test")
	}else{
		cur_frm.set_df_property("hp_insurance_provider", "reqd", 0);
	}
}