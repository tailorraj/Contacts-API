import frappe

@frappe.whitelist()
def get_invoice_numbers(item):
    if not "Whatsapp API Caller" in frappe.get_roles(frappe.session.user):
        frappe.local.response.http_status_code = 403
        frappe.local.response.data = "User don't have sufficient role perission to get data"
        return

    warehouse = frappe.db.get_single_value('Warehouse Settings', 'default_warehouse')
    if not warehouse:
        frappe.local.response.http_status_code = 502
        frappe.local.response.data = "Please set warehouse in Warehouse Settings"
        return

    try:
        data = frappe.db.sql("""
        select
        sii.item_code,
        i.group,
        i.sub_group,
        sii.item_name,
        si.customer,
        c.customer_name,
        IF(cc.last_name is not NULL, CONCAT(cc.first_name, ' ',cc.last_name), cc.first_name) as contact_name,
        %(warehouse)s,
        (select b.actual_qty from `tabBin` b where b.item_code = sii.item_code and warehouse = %(warehouse)s) as stock,
        (select b.reserved_qty from `tabBin` b where b.item_code = sii.item_code and warehouse = %(warehouse)s) as res_stock,
        cp.phone

        from
        `tabSales Invoice Item` sii
        left join `tabItem` i on i.name = sii.item_code
        left join `tabSales Invoice` si on si.name = sii.parent
        left join `tabCustomer` c on c.name = si.customer
        left join `tabDynamic Link` cdl on cdl.link_name = c.name
        left join `tabContact` cc on cdl.parent = cc.name
        join `tabContact Phone` cp on cp.parent = cc.name 
        where
        si.docstatus = 1
        and
        cdl.link_doctype = 'Customer'
        and
        cp.is_whatsapp_no_ak = 1
        and
        sii.item_code = %(item)s
        order by si.name
        """, {"warehouse": warehouse, "item": item},as_dict = True)

        frappe.local.response.http_status_code = 200
        frappe.local.response.data = data
        return
    except Exception as ex:
        frappe.local.response.http_status_code = 502
        frappe.local.response.data = ex
        return
    # end try
# contact = frappe.db.sql(
# 			"""
# 			SELECT parent FROM `tabDynamic Link`
# 			WHERE
# 				parenttype = 'Contact' AND
# 				parentfield = 'links' AND
# 				link_doctype = 'Customer' AND
# 				link_name = %s
# 			""",
# 			(customer),
# 			as_dict=1,
# 		)
@frappe.whitelist()
def get_contact(item):
    if not "Whatsapp API Caller" in frappe.get_roles(frappe.session.user):
        frappe.local.response.http_status_code = 403
        frappe.local.response.data = "User don't have sufficient role perission to get data"
        return

    warehouse = frappe.db.get_single_value('Warehouse Settings', 'default_warehouse')
    if not warehouse:
        frappe.local.response.http_status_code = 502
        frappe.local.response.data = "Please set warehouse in Warehouse Settings"
        return
    warehouse = frappe.db.get_single_value('Warehouse Settings', 'default_warehouse')

    try:
        data = frappe.db.sql("""
        select
        i.item_name,
        i.group,
        i.sub_group,
        cp.phone,
        IF(cc.last_name is not NULL, CONCAT(cc.first_name, ' ',cc.last_name), cc.first_name) as contact_name,
        %(warehouse)s,
        (select b.actual_qty from `tabBin` b where b.item_code = %(item)s and warehouse = %(warehouse)s) as stock,
        (select b.reserved_qty from `tabBin` b where b.item_code = %(item)s and warehouse = %(warehouse)s) as res_stock,
        ci.item
        from
        `tabContact Phone` cp
        left join `tabDynamic Link` cdl on cp.parent = cdl.parent
        left join `tabContact` cc on cp.parent = cc.name
        left join `tabContact Items` ci on ci.parent = cc.name
        left join `tabItem` i on i.name = ci.item
        where
        ci.item = %(item)s
        and
        cp.is_whatsapp_no_ak = 1
        """, {"item": item, "warehouse": warehouse},as_dict = True)

        frappe.local.response.http_status_code = 200
        frappe.local.response.data = data
    except Exception as ex:
        frappe.local.response.http_status_code = 502
        frappe.local.response.data = ex
        return
    # end try

