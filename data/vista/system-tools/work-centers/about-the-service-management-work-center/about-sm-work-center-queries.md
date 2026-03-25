---
title: "About SM Work Center Queries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-centers/about-the-service-management-work-center/about-sm-work-center-queries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-centers/about-the-service-management-work-center/about-sm-work-center-queries"
---

# About SM Work Center Queries

Work center queries allow you to view specific Service Management data, such as work orders, customer and service site information, trip scheduling, and so forth.

## Query Security

Query security is set up using [VA Inquiry Security](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form). The security defined on this form determines which queries (standard or custom) display in the SM Work Center menu, and which queries users can add. Query security is discussed in the Work Center Setup help. Click [here](/en/vista/vista/system-tools/work-centers/about-work-center-setup) for more information.

## Configuring Hot Lists

The Hot List menu folder in the SM Work Center displays a list of high priority items (e.g. Overdue Work Orders). Hot List items are queries (standard or custom) that you can customize directly from the SM Work Center or using [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form).
Changes made to Hot List queries from the SM Work Center will only affect how the Hot List query displays in the selected SM Work Center for the active user. Changes made to Hot List queries using [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form) will affect how the Hot List queries display for all users everywhere in the application, including Dashboard, PM, and SM work centers.

## Adding Dashboard Queries to the SM Work Center Menu

You can add additional Dashboard queries to the SM Work Center as menu items and then customize those queries using the Grid Query form.
Note: Changes made to the menu will only affect how it displays on the selected SM Work Center on your user account. It will not affect other user accounts or the other SM Work Center tabs on your application window.
Although you can add any Dashboard query to an SM work center, not all queries support all functions of the SM work center.

- Company Filter - The Company drop-down filter at the top of the SM Work Center will only work with queries that include a company filter parameter. You can only add parameters to custom queries; therefore, if a standard Dashboard query does not contain a company parameter and you want to add one, you must copy the query and then add the company parameter to the new query. For more information, see [VA My VP Queries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form).

- Service Center / Division Filters - The Service Center and Division drop-down filters at the top of the SM module Work Center will only work with queries that were specifically designed to use them—they will be disabled for all other queries. However, if you make a copy of the query, the Service Center and Division drop-down filters will still be enabled.

Note: Unlike the company filter parameter, only very advanced users will be able to add this functionality to a custom query. If you would like to create a custom query that includes this functionality, contact Viewpoint Technical Services.

- Double-click to open a record - You can double-click on a record that displays in the SM Work Center to open that record. Queries that were specifically designed for the SM Work Center will also include this functionality. Other Dashboard queries added to your SM work center may also have this functionality. However, if you want to add this functionality to a custom query, you must add KEYID and FormName columns to the query. For an example of these columns, open the VA Inquiries form, select the "SMWorkOrdersOverdue" query, and then open the Columns tab.

## About Inquiries

An inquiry is two or more queries that are linked together. For example if you have a query that displays a list of purchase orders and a query that displays detailed information about PO items, you can link these two queries together so that from a Work Center you can drill-through a PO and see detailed information about the PO items.
Click the links below for more information.
[Creating Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/creating-inquiries)
[Add a Query to an SM Work Center](/en/vista/vista/system-tools/work-centers/about-the-service-management-work-center/add-a-query-to-an-sm-work-center)
[Customize a Hot List Query in a PM or SM Work Center](/en/vista/vista/system-tools/work-centers/about-work-center-setup/customize-a-hot-list-query-in-a-pm-or-sm-work-center)
