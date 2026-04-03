---
title: "Reverse Customer Invoice - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/reverse-customer-invoice/reverse-customer-invoice---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/reverse-customer-invoice/reverse-customer-invoice---field-descriptions"
---

# Reverse Customer Invoice - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Transaction to be reversed

Customer
Enter the code of the customer for whom an open invoice is being reversed. The complete customer description displays, followed by the customer's address, city, state and zip. If the customer's status is set to Not used, no entry is allowed.
Note: When invoices are reversed using this screen, the bill-to
 code specified in the Customer Invoice Entry > Properties window for the original item will be transferred.

Invoice
Enter the number of the invoice you want to reverse, or double-click on this field to select an invoice from the Open A/R Items window. Use the Open A/R Items window to look up and select an invoice to be reversed.
Invoices and credit memos that display here have already been posted, and therefore may not be changed through Customer Invoice Entry; a reversing entry must be made.

Invoice type
Depending upon the type of transaction being reversed, select either Invoice or Credit memo from the drop-down menu.
If the job status is 'Completed' and the 'Disallow revenue entry' checkbox is selected in Job Main Properties, you will not be able to add the invoice to the job.

Invoice total
Once a valid invoice is selected, the invoice total will display in this field. Credit memos will display as a negative amount.
Click the View button to open the Customer Invoice Inquiry screen to view details on a specific invoice.

New credit memo/invoice

Batch Code
The batch code for this invoice defaults.

G/L date
Enter the G/L date. The fiscal year and period that correspond with the G/L date display to the right of this field.
When a new date is entered, it is validated against the Minimum/Maximum date
 settings and the current processing period settings in the A/R Processing Date Change
 screen. If the Invoice date
 must be in G/L period checkbox is selected in the Accounts Receivable Installation > Properties screen, then the invoice date must be in the same fiscal
 period as the G/L date.

Invoice date
The date for this reversal displays. If the Invoice date must be in G/L
 period? checkbox is selected in Admin > Installation > Accounts Receivable, then the invoice date must be in the same fiscal period as
 the G/L date.

Invoice remarks
Enter any remarks for this invoice, or select from one of the existing customer invoice messages.
