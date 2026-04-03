---
title: "New/Edit Routing Code - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/invoice-approval-routing-maintenance/newedit-routing-code---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/invoice-approval-routing-maintenance/newedit-routing-code---field-descriptions"
---

# New/Edit Routing Code - Field Descriptions

Use this table for reference when completing the fields on this screen.
From the Invoice Approval Routing Maintenance screen, select New or choose an existing record and select Edit.
Fields/ButtonsDescriptions
DescriptionA description of the routing code.
ConfirmationThe operator that will ultimately finalize each invoice after it has completed the approval process. Confirming an invoice moves it to Invoice / Credit Memo Entry as an unposted item.
Email notification?Select this checkbox if you want an email message to be generated when an invoice is transferred to the confirming operator's during routing processing.The email address of each operator is stored in Operator Maintenance. If the system cannot find the email address there, it will use the operator's name to attempt to find the operator's email address from the current address book.

New
Edit
Insert
Delete
Use these action buttons to arrange the order of your routing list. The Insert button removes the selected record and allows you to enter a new one.
OrderThe system assigns order numbers to the routing code, and re-numbers them when needed.
Code
Reviewer name
Select the operator to reviewing the invoice, based on the order number assigned by the software.
Approval limitIf all reviewers should approve invoices routed to this code, leave this field blank.
If certain reviewers should be excused from reviewing invoices routed to this Code based on invoice amounts, insert each reviewer's assigned approval limit.

- This is the maximum approval authority the reviewer has, and invoices above this amount are routed to subsequent reviewers after the reviewer approves them.

- Within each Routing Code, if any reviewer has an approval limit, all reviewers must be given a limit. Invoices whose Total amount is over the value you enter here will be required to be approved by a reviewer with higher a limit.

E-mailSelect this checkbox if you want an email message to be generated when an invoice is ready for this reviewer to view.
