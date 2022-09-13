import frappe



# @frappe.whitelist()
# def get_invoice_numbers(item):
#     if not "Whatsapp API Caller" in frappe.get_roles(frappe.session.user):
#         frappe.local.response.http_status_code = 403
#         frappe.local.response.data = "User don't have sufficient role perission to get data"
#         return

#     warehouse = frappe.db.get_single_value('Warehouse Settings', 'default_warehouse')
#     if not warehouse:
#         frappe.local.response.http_status_code = 502
#         frappe.local.response.data = "Please set warehouse in Warehouse Settings"
#         return

#     try:
#         data = frappe.db.sql("""
#         select
#         sii.item_code,
#         i.group,
#         i.sub_group,
#         sii.item_name,
#         si.customer,
#         c.customer_name,
#         IF(cc.last_name is not NULL, CONCAT(cc.first_name, ' ',cc.last_name), cc.first_name) as contact_name,
#         %(warehouse)s,
#         (select b.actual_qty from `tabBin` b where b.item_code = sii.item_code and warehouse = %(warehouse)s) as stock,
#         (select b.reserved_qty from `tabBin` b where b.item_code = sii.item_code and warehouse = %(warehouse)s) as res_stock,
#         cp.phone

#         from
#         `tabSales Invoice Item` sii
#         left join `tabItem` i on i.name = sii.item_code
#         left join `tabSales Invoice` si on si.name = sii.parent
#         left join `tabCustomer` c on c.name = si.customer
#         left join `tabDynamic Link` cdl on cdl.link_name = c.name
#         left join `tabContact` cc on cdl.parent = cc.name
#         join `tabContact Phone` cp on cp.parent = cc.name 
#         where
#         si.docstatus = 1
#         and
#         cdl.link_doctype = 'Customer'
#         and
#         cp.is_whatsapp_no_ak = 1
#         and
#         sii.item_code = %(item)s
#         order by si.name
#         """, {"warehouse": warehouse, "item": item},as_dict = True)

#         frappe.local.response.http_status_code = 200
#         frappe.local.response.data = data
#         return
#     except Exception as ex:
#         frappe.local.response.http_status_code = 502
#         frappe.local.response.data = ex
#         return
#     # end try
# # contact = frappe.db.sql(
# # 			"""
# # 			SELECT parent FROM `tabDynamic Link`
# # 			WHERE
# # 				parenttype = 'Contact' AND
# # 				parentfield = 'links' AND
# # 				link_doctype = 'Customer' AND
# # 				link_name = %s
# # 			""",
# # 			(customer),
# # 			as_dict=1,
# # 		)
# @frappe.whitelist()
# def get_contact(item):
#     if not "Whatsapp API Caller" in frappe.get_roles(frappe.session.user):
#         frappe.local.response.http_status_code = 403
#         frappe.local.response.data = "User don't have sufficient role perission to get data"
#         return

#     warehouse = frappe.db.get_single_value('Warehouse Settings', 'default_warehouse')
#     if not warehouse:
#         frappe.local.response.http_status_code = 502
#         frappe.local.response.data = "Please set warehouse in Warehouse Settings"
#         return
#     warehouse = frappe.db.get_single_value('Warehouse Settings', 'default_warehouse')

#     try:
#         data = frappe.db.sql("""
#         select
#         i.item_name,
#         i.group,
#         i.sub_group,
#         cp.phone,
#         IF(cc.last_name is not NULL, CONCAT(cc.first_name, ' ',cc.last_name), cc.first_name) as contact_name,
#         %(warehouse)s,
#         (select b.actual_qty from `tabBin` b where b.item_code = %(item)s and warehouse = %(warehouse)s) as stock,
#         (select b.reserved_qty from `tabBin` b where b.item_code = %(item)s and warehouse = %(warehouse)s) as res_stock,
#         ci.item
#         from
#         `tabContact Phone` cp
#         left join `tabDynamic Link` cdl on cp.parent = cdl.parent
#         left join `tabContact` cc on cp.parent = cc.name
#         left join `tabContact Items` ci on ci.parent = cc.name
#         left join `tabItem` i on i.name = ci.item
#         where
#         ci.item = %(item)s
#         and
#         cp.is_whatsapp_no_ak = 1
#         """, {"item": item, "warehouse": warehouse},as_dict = True)

#         frappe.local.response.http_status_code = 200
#         frappe.local.response.data = data
#     except Exception as ex:
#         frappe.local.response.http_status_code = 502
#         frappe.local.response.data = ex
#         return
    # end try

# @frappe.whitelist()
# def get_invoice_numbers():
#     if not "Whatsapp API Caller" in frappe.get_roles(frappe.session.user):
#         frappe.local.response.http_status_code = 403
#         frappe.local.response.data = "User don't have sufficient role perission to get data"
#         return

#     # warehouse = frappe.db.get_single_value('Warehouse Settings', 'default_warehouse')
#     # if not warehouse:
#     #     frappe.local.response.http_status_code = 502
#     #     frappe.local.response.data = "Please set warehouse in Warehouse Settings"
#     #     return

#     try:
#         data = frappe.db.sql("""
#         select
#         sii.item_code,
#         i.group,
#         i.sub_group,
#         sii.item_name,
#         si.customer,
#         c.customer_name,
#         IF(cc.last_name is not NULL, CONCAT(cc.first_name, ' ',cc.last_name), cc.first_name) as contact_name,
#         %(warehouse)s,
#         (select b.actual_qty from `tabBin` b where b.item_code = sii.item_code and warehouse = %(warehouse)s) as stock,
#         (select b.reserved_qty from `tabBin` b where b.item_code = sii.item_code and warehouse = %(warehouse)s) as res_stock,
#         cp.phone

#         from
#         `tabSales Invoice Item` sii
#         left join `tabItem` i on i.name = sii.item_code
#         left join `tabSales Invoice` si on si.name = sii.parent
#         left join `tabCustomer` c on c.name = si.customer
#         left join `tabDynamic Link` cdl on cdl.link_name = c.name
#         left join `tabContact` cc on cdl.parent = cc.name
#         join `tabContact Phone` cp on cp.parent = cc.name 
#         where
#         si.docstatus = 1
#         and
#         cdl.link_doctype = 'Customer'
#         and
#         cp.is_whatsapp_no_ak = 1
#         and
#         sii.item_code = %(item)s
#         order by si.name
#         """, {"warehouse": warehouse, "item": item},as_dict = True)

#         frappe.local.response.http_status_code = 200
#         frappe.local.response.data = data
#         return
#     except Exception as ex:
#         frappe.local.response.http_status_code = 502
#         frappe.local.response.data = ex
#         return
#     # end try
# # contact = frappe.db.sql(
# # 			"""
# # 			SELECT parent FROM `tabDynamic Link`
# # 			WHERE
# # 				parenttype = 'Contact' AND
# # 				parentfield = 'links' AND
# # 				link_doctype = 'Customer' AND
# # 				link_name = %s
# # 			""",
# # 			(customer),
# # 			as_dict=1,
# # 		)


# -----------------------------------Sales Invoice Contact API V1-----------------------------------------------
@frappe.whitelist()
def get_sales_contact():   
    contact_response = []
    available_items = get_available_items()    
    for item in available_items:     
        contact = get_invoiced_contact(item.item_code)      
        contact_response.append({
            "item":item,
            "invoiced_contacts":contact,
            "subgroup_contacts":get_subgroup_invoiced_contact(item.item_code)
        })
    return contact_response

def get_invoiced_contact(item):
    data = frappe.db.sql("""
        select
        sii.item_code,
        sii.item_name,
        si.customer,
        c.customer_name,        
        IF(cc.last_name is not NULL, CONCAT(cc.first_name, ' ',cc.last_name), cc.first_name) as contact_name,
        cp.phone
        from
        `tabSales Invoice Item` sii
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
        """, {"item": item},as_dict = True)
    return data


@frappe.whitelist()
def get_subgroup_invoiced_contact(item):
    data = []
    subgrp = frappe.db.get_value("Item",item,"sub_group")
    if subgrp:
        similar_item = frappe.db.sql("""
        select name from `tabItem` where sub_group = %s and name != %s
        """,(subgrp,item),as_dict=1)
        s_l = [i['name'] for i in similar_item]
        if similar_item:
            data = frappe.db.sql("""
                select
                sii.item_code,
                sii.item_name,
                si.customer,
                c.customer_name,
                
                IF(cc.last_name is not NULL, CONCAT(cc.first_name, ' ',cc.last_name), cc.first_name) as contact_name,
                cp.phone
                from
                `tabSales Invoice Item` sii
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
                sii.item_code in %(l)s
                order by si.name
                """, ({"l":tuple(s_l)}),as_dict = True)
            return data
    return data
    
# ---------------------------------------Sales Invoice API V1--------------------------------------------------------


# -----------------------------------Sales Invoice Contact API V2-----------------------------------------------
@frappe.whitelist()
def get_sales_contact_v2():   
    contact_response = []
    available_items = get_available_items()    
    for item in available_items:     
        contact_list = get_invoiced_contact_v2(item.item_code)
        for contact in contact_list:
            contact_response.append({
                "item_code": item.item_code,
                "warehouse": item.warehouse,
                "actual_qty": item.actual_qty,
                "reserved_qty": item.reserved_qty,
                "group": item.group,
                "sub_group": item.sub_group,
                "invoiced_item_code":contact.item_code,
                "invoiced_item_name":contact.item_name,
                "customer":contact.customer,
                "customer_name":contact.customer_name,
                "contact_name":contact.contact_name,
                "whatsapp_number":contact.phone
            })
    
    return contact_response

@frappe.whitelist()
def get_invoiced_contact_v2(item):
    data = []
    subgrp = frappe.db.get_value("Item",item,"sub_group")
    if subgrp:
        similar_item = frappe.db.sql("""
        select name from `tabItem` where sub_group = %s
        """,(subgrp),as_dict=1)
        s_l = [i['name'] for i in similar_item]
        if similar_item:
            data = frappe.db.sql("""
                select
                sii.item_code,
                sii.item_name,
                si.customer,
                c.customer_name,                
                IF(cc.last_name is not NULL, CONCAT(cc.first_name, ' ',cc.last_name), cc.first_name) as contact_name,
                cp.phone
                from
                `tabSales Invoice Item` sii
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
                sii.item_code in %(l)s group by cp.phone,sii.item_code
                order by si.name
                """, ({"l":tuple(s_l)}),as_dict = True)
            return data
    return data
    
# ---------------------------------------Sales Invoice API V2--------------------------------------------------------


# ---------------------------------------Contact API V1--------------------------------------------------------
@frappe.whitelist()
def get_contacts_item():
    contact_response = []
    available_items = get_available_items()
    for item in available_items:     
        contact = get_standalone_contact(item.item_code)      
        contact_response.append({
            "item":item,
            "direct_contacts":contact,
            "subgroup_contacts":get_subgroup_contact(item.item_code)
        })
    return contact_response

@frappe.whitelist()
def get_subgroup_contact(item):
    data = []
    subgrp = frappe.db.get_value("Item",item,"sub_group")
    if subgrp:
        similar_item = frappe.db.sql("""
        select name from `tabItem` where sub_group = %s and name != %s
        """,(subgrp,item),as_dict=1)
        s_l = [i['name'] for i in similar_item]
        if similar_item:
            data = frappe.db.sql("""
                select
                cp.phone,
                IF(cc.last_name is not NULL, CONCAT(cc.first_name, ' ',cc.last_name), cc.first_name) as contact_name
                from
                `tabContact Phone` cp
                left join `tabDynamic Link` cdl on cp.parent = cdl.parent
                left join `tabContact` cc on cp.parent = cc.name
                left join `tabContact Items` ci on ci.parent = cc.name
                left join `tabItem` i on i.name = ci.item
                where
                ci.item in %(item)s
                and
                cp.is_whatsapp_no_ak = 1
                """, {"item": tuple(s_l)},as_dict = True)
    return data

def get_standalone_contact(item):
    data = frappe.db.sql("""
        select
        cp.phone,
        IF(cc.last_name is not NULL, CONCAT(cc.first_name,' ',cc.last_name), cc.first_name) as contact_name
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
        """, {"item": item},as_dict = True)
    return data

# ---------------------------------------Contact API V1--------------------------------------------------------

# ---------------------------------------Contact API V2--------------------------------------------------------
@frappe.whitelist()
def get_contacts_item_v2():
    contact_response = []
    available_items = get_available_items()
    for item in available_items:     
    #     {
    #     "item": {
    #         "item_code": "AppleScreen",
    #         "warehouse": "Finished Goods - E",
    #         "actual_qty": 99.0,
    #         "reserved_qty": 0.0,
    #         "group": "",
    #         "sub_group": "PC",
    #     },
    #     "subgroup_contacts": [{"phone": "4579647897", "contact_name": "Rock"}],
    # }
        contact_list = get_subgroup_contact_v2(item.item_code)
        for contact in contact_list:    
                contact_response.append({
                    "item_code":item.item_code,
                    "item_name":item.item_name,
                    "warehouse":item.warehouse,
                    "actual_qty":item.actual_qty,
                    "reserved_qty":item.reserved_qty,
                    "group":item.group,
                    "sub_group":item.sub_group,
                    "contact_name":contact.contact_name,
                    "whatsapp_number":contact.phone
                })
    return contact_response


def get_subgroup_contact_v2(item):
    data = []
    subgrp = frappe.db.get_value("Item",item,"sub_group") 
    if subgrp:        
        data = frappe.db.sql("""
            select
            cp.phone,
            IF(cc.last_name is not NULL, CONCAT(cc.first_name, ' ',cc.last_name), cc.first_name) as contact_name
            from
            `tabContact Phone` cp
            left join `tabDynamic Link` cdl on cp.parent = cdl.parent
            left join `tabContact` cc on cp.parent = cc.name
            left join `tabContact Sub Group` ccsg on ccsg.parent = cc.name
            where
            ccsg.sub_group = %s
            and
            cp.is_whatsapp_no_ak = 1
            """,(subgrp),as_dict = True)
    return data

# ---------------------------------------Contact API V2--------------------------------------------------------





# ---------------------support function-------------------------------
def get_available_items():
    available_item = frappe.db.sql("""
    select bn.item_code,it.item_name,bn.warehouse,bn.actual_qty,bn.reserved_qty,it.group,it.sub_group from `tabBin` bn inner join `tabItem` it on it.name = bn.item_code where bn.actual_qty > 0
    """,as_dict=1)
    return available_item

# ---------------------support function-------------------------------