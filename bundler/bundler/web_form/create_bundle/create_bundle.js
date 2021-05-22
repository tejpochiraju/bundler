frappe.ready(function() {
	frappe.web_form.after_load = () => {
		$("button:contains('Add Row')" ).addClass('btn-primary');
	}	
	frappe.web_form.after_save = () => {
		window.location.href = '/view';
	}
	frappe.web_form.on_delete = () => {
		window.location.href = '/view';
	}
})