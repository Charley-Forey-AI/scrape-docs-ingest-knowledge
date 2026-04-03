---
title: "Create A/R Invoice - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-order-financial-summary/create-ar-invoice/create-ar-invoice---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-order-financial-summary/create-ar-invoice/create-ar-invoice---field-descriptions"
---

# Create A/R Invoice - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field
Description

Work order #
The work order number displays. This is
 the work order that was selected on the Work Order Entry
 screen.
Accounts receivable invoice

A/R invoice #
The A/R invoice number displays. The
 invoice number is based on the setting in Work Order
 Installation.
Customer
The customer displays from the work
 order.
Invoice date
Enter the desired invoice date, or
 press Enter to accept
 the entered date as the default invoice date.If the
 Invoice date must be in G/L period' option was selected in
 Accounts Receivable Installation, the date entered
 in this field must be within the same fiscal period as the G/L
 date.

G/L date
Enter the desired general ledger date
 for this invoice, or press Enter to accept the default of the current Accounts Receivable
 processing as the invoice date. If the Invoice date must
 be in G/L period' option was selected in Accounts Receivable
 Installation, any date within the Work Order minimum/maximum
 date range can be entered in this field.

Invoice batch code
Enter the batch code to be assigned to
 this Accounts Receivable invoice, or press Enter to accept the default.
Terms code
The terms code will default from the
 current setting for this work order, but can be changed to a different
 code.
Sales tax code
The sales tax code will default from
 the current setting for this work order, but can be changed to a different
 code. The Sales tax
 amount will immediately re-calculate if this code is changed.
Bill through date
By default, this update will include
 transactions through the maximum Work Order processing date, but you can enter
 a different date in this field to shift the most recent transactions onto
 future billings. During the update, Spectrum will select labor transactions
 based on the work order date, and material transactions based on the date added
 to the work order.Note: This option will be
 hidden if you are creating an invoice for a Job work order.

Preview customer invoice now?
Select this checkbox to print and
 email the customer invoice. When this option is selected and the Operator
 clicks OK to initiate
 the update, the Mail Customer Invoice window will
 automatically open. Note: This field will be
 disabled if the Operator does not have access to the Accounts Receivable > Invoice Print screen.

Invoice totals

Manufacturer subtotal
The manufacturer subtotal for this
 invoice displays.
Customer subtotal
The customer subtotal for this invoice
 displays.  The invoice calculations will be based on all
 unbilled Labor, Material, Other charges and Flat rate tasks, excluding task
 transactions that are not complete.

Sales tax
The sales tax calculated by the
 software displays in this field. Spectrum calculates the sales tax amount based
 on the invoice date. If you override the tax amount, the amount entered will be
 recorded in Accounts Receivable.
Invoice total
The invoice total displays as the sum
 of the above subtotal and sales tax. The invoice
 calculations will be based on all unbilled Labor, Material, Other charges
 and Flat rate tasks, excluding task transactions that are not complete.


Work order

Set work order to complete?
Select this checkbox to set the site
 work order status to complete. Site work orders cannot be set to complete if
 any incomplete tasks are present. When the status is set
 to complete during this update, the 'Complete date' will be set to the G/L
 date specified on the starting screen. If the work order is not set to
 complete, the 'Complete date' column will remain clear during this update.
 This checkbox will not appear for job work orders.

New dispatch status
If the work order is not set to
 complete, enter a dispatch status code in this field. Codes with a status of
 'Proposed' will not be allowed.
New priority
If the work order is not set to
 complete, enter a priority code in this field.
