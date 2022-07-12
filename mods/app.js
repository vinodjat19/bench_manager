// Copyright (c) 2017, Frappé and contributors
// For license information, please see license.txt

frappe.ui.form.on('App', {
	refresh: function(frm) {

		if (frm.doc.is_git_repo != true) {
			// Do nothing
		} else {
			frm.add_custom_button(__('Push'), function(){
				let key = frappe.datetime.get_datetime_as_string();
				console_dialog(key);
				frappe.call("bench_manager.mods.bench_command_mod.console_command", {
                    doc: frm.doc,
					key: key,
					caller: "push"
				});
			});
		}
	}
});