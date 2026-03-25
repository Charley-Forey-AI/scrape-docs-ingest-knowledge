---
title: "About PM Work Center Queries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-centers/about-the-project-management-work-center/about-pm-work-center-queries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-centers/about-the-project-management-work-center/about-pm-work-center-queries"
---

# About PM Work Center Queries

Work center queries allow you to view specific Project Management data, such as change orders, document control/tracking, projections, field logs, and so forth.
There are several queries that display as menu items on the standard PM Work Center - for example, the Projects, Contracts, and Hot List queries. Each of these queries displays a list of records, and they are created and maintained using the VA Inquiries form.

## Query Security

Query security is set up using VA Inquiry Security. The security defined on this form determines which queries (standard or custom) display in the PM Work Center menu, and which queries users can add. Query security is discussed in the Work Center Setup help. For more information, see [About Work Center Setup](/en/vista/vista/system-tools/work-centers/about-work-center-setup).

## Configuring Hot Lists

The Hot List is a query in the PM Work Center that displays a list of high priority items, and you can customize it either directly from the PM Work Center or from VA Inquiries.
Changes made to the Hot List in the PM Work Center only affect how the Hot List displays in the selected PM Work Center on your user account. Changes made to the Hot List using VA Inquiries affect how the Hot List displays everywhere in the application, including on a Dashboard Work Center, and how it displays for other users.

## Adding Inquiries to a PM Work Center

The Hot List menu option in the PM Work Center is a query. You can add additional queries to the PM Work Center as menu items and then customize those queries using the Inquiry Settings form.
Changes made to the menu will only affect how it displays on the selected PM Work Center for your user account. Any changes that you make will not affect other user accounts, or the other PM Work Center tabs on your application window. This also applies to customizing the query using the Inquiry Settings form; changes only affect how that query displays on the selected PM Work Center tab on your user account.
Note: If you want to make changes to a query and have it affect all users, you can create and modify queries using VA Inquiries. If you want to create PM Work Centers that you can apply to multiple user accounts, see [About the VA Work Center Profile Form](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-profile-form) for more information.

You can add any query to a PM module Work Center, but only some queries support all of the PM module Work Center functionality.

- Company Filter - The Company drop down filter at the top of the PM Work Center will only work with queries that include a company filter parameter. For an example of a company filter parameter, open the VA Inquiries form, select the JC Budget Analysis By Cost Type query, and then open the Parameters tab. You can use this example to add a company filter parameter to a custom query.

- Project/Status Filter - The Project and Project Status drop down filters at the top of the PM module Work Center only work with queries that were specifically designed to use them. Generally the Project and Project Status fields will be disabled for queries.

## Linking Inquiries

An inquiry is two or more queries that are linked together. For example if you have a query that displays a list of purchase orders and a query that displays detailed information about PO items, you can link these two queries together so that from a Work Center you can drill-through a PO and see detailed information about the PO items.

## Unapproved Invoice Review Query

The Unproved Invoice Review query (which is a standard query) is in the Document Review folder and displays all of the unapproved invoices created in AP Unapproved Invoice Entry to which you are assigned as a reviewer. If you are not set up as a reviewer, this menu item does not display any information.
You can view this query using the VA Inquiries form.

## Process Workflow Queries

If you have the Workflow module and are using the Process Workflow feature for PO and Subcontract review/approval, you will use the My Documents to Review query to see all documents that have been submitted for approval and are ready for you to review/approve. Using this query, you can approve or reject each purchase order or subcontract, as well as edit documents, add attachments, and enter comments.
There are also several other queries related to the Process Workflow feature that you can assign to a PM Work Center:

- My Items to Review

- My Documents in Workflow

- My Workflow Documents to Process

- My Notifications

- All Documents in Workflow

- All Workflow Documents to Process

- Workflow Comments

You can find more information about these inquiries in the VA Inquiries form.
Note: If you have Viewpoint Field Management or Viewpoint Financial Controls, you can also approve purchase orders and subcontracts using the Pending PO / Subcontract Review approval page, which you can access:

- from Project Management by selecting Programs > PM Pending PO / SL Review;

- from Purchase Order by selecting Programs > PO Pending PO Review; or

- from Subcontract Ledger by selecting Programs >  SL Subcontract Review.

Select the links below for more information.
[Creating Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/creating-inquiries)
[Add a Query to a PM Work Center](/en/vista/vista/system-tools/work-centers/about-the-project-management-work-center/add-a-query-to-a-pm-work-center)
[Customize a Hot List Query in a PM or SM Work Center](/en/vista/vista/system-tools/work-centers/about-work-center-setup/customize-a-hot-list-query-in-a-pm-or-sm-work-center)
[VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)
