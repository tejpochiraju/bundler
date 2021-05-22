import frappe

def get_context(context):
    params = frappe.form_dict
    name = params.get('id')
    if name:
        password = params.get('key')
        context.bundles = [frappe.get_doc('Bundle', {'name': name, 'password': password}, ignore_permissions=True)]
        return
    if frappe.session.user == 'Guest':
        return
    else:
        refs = frappe.get_list('Bundle')
        context.bundles = []
        for ref in refs:
            context.bundles.append(frappe.get_doc('Bundle', ref))