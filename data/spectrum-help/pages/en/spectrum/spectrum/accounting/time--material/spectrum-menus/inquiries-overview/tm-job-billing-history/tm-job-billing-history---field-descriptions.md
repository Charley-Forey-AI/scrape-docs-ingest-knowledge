---
title: "T+M Job Billing History - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/spectrum-menus/inquiries-overview/tm-job-billing-history/tm-job-billing-history---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/spectrum-menus/inquiries-overview/tm-job-billing-history/tm-job-billing-history---field-descriptions"
---

# T+M Job Billing History - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Job code
Enter the job number. Based on the number entered, the full job description and other information display.

Customer
The customer code and name displays.

Billing #
Enter the number of the billing to be modified. A look-up window is available for viewing existing billing numbers. Entry of a billing number will also display invoice number, Invoice date, and the transaction thru date. If the billing number exceeds 999, the billing number will automatically be converted to the alpha equivalent (Example: A00 = 1000).

Contract # Contract type Transactions through
The contract number, job type, and billing transaction date display.

Billing summary

Billing total Add-ons Fees
The taxable, nontaxable, and total amounts for billing, add-ons, and fees display.

- Click the Add-ons button to view the [Add-on History Window](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/maintenance-overview/tm-job-billing-setup/add-on-history-window)

- Click the Fees button to view the [Fee History Window](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/maintenance-overview/tm-job-billing-setup/fee-history-window)

Subtotal
The Subtotal is the sum of the Billing total plus Add-ons plus Fees.

Tax
The total tax amount and percentage for this sales tax displays.
 Spectrum calculates the sales tax based on the invoice date.
If VAT processing is enabled, this amount is the sales tax amount plus the
 total VAT amount.
Note: If a billing has been updated to Change Request, this field will be hidden.

Invoice total
The invoice total (Billingamount plus Add-ons, Fees, and Salestax) displays.
Note: If a billing has been updated to Change Request, this field will be hidden.

Accounts receivable

Invoice/Credit memo
The field label displays based on what the invoice type is.
 Click the lookup icon to view the Accounts Receivable Invoice
 Inquiry window. You can view invoice notes by clicking the
 More info
 button in that window.
For more information on the Account Receivable Invoice
 Inquiry window, click the Spectrum Help link.

Invoice date G/L date
The Invoice date and General Ledger date display.

Status
This field displays if the A/R invoice is unposted.

Current due Retention due
The current and retention balance from Accounts Receivable Open Items displays.

Outstanding balance
The sum of the current and retention balances displays. If this invoice is not in Accounts Receivable, the Current, Retention, and Outstanding balance fields will not display.

Note: If a billing has been updated to Change Request,
 the fields in this section will be hidden and the Change request # will
 appear in their place with a link to the Change Request Entry
 screen. The link will be unavailable if the specified change request
 number does not exist in A/R, or the operator does not have security
 authorization to the Change
 Request Entry screen.

List box

Phase Ct
The phase code and job Cost type display.

Tran date
The transaction date displays.

Type Description
 The transaction type displays.

- AP = vendor name

- EQ = description of equipment used

- GL = description of journal entry

- IC = name of inventory item

- JC = description of transaction

- PR = description from Payroll setting on the Time + Material Installation > Properties tab at the time of Payroll update

Hours/qty
The total hours (or units, if applicable) display.

Billing total
 The dollar total for each line (Extension plus Markup) displays.

Message Code Reference
The message, code, and reference display.

PO# Work date Inv/check date
The purchase order number, work, and invoice/check dates display.

Pay type
The Pay type displays as Regular, Overtime, or Double.

Billing code
The billing code displays.

Billing Rate
The Billing Rate per hour (or per unit) displays.

Extension
The billing extension (total bill less markup or hours multiplied by rate) displays.

Markup
The Markup displays.

Taxable?
The column will display Yes if the transaction is taxable, or No if it's non-taxable.

From sub-job
If the selected job is a sub-job billed from a master job, the sub-job code and description will display in this column.
