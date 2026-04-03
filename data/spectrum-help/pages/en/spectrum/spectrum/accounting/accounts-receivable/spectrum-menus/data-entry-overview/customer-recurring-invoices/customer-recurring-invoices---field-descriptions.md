---
title: "Customer Recurring Invoices - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-recurring-invoices/customer-recurring-invoices---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-recurring-invoices/customer-recurring-invoices---field-descriptions"
---

# Customer Recurring Invoices - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field/Button
Description

Recurring invoice heading

Customer
Enter the customer code for whom this recurring invoice is being prepared. A lookup window is available for viewing existing customer codes or adding a new customer. If the customer's status is set to Not used, no entry is allowed.
Note: Once you enter or select the customer code, the customer's name and mailing address display. If there are two lines of text in the address, the second line displays with the city and state below the first line of the address and customer's name.

Job
If this recurring invoice is for a contract, enter a valid job number. The job description will display beneath the job number. A search window is available for viewing valid job numbers. If this recurring invoice is not for a contract, press Enter to skip the job number.
When entering the job, if there is an error message "RECORD NOT IN FILE CR.CNTR," this indicates the contract is not currently on file for this customer and job. To resolve this, click Cancel to exit the screen and then add the contract information using Contracts.
If the cost centers feature is enabled, Spectrum will compare the cost center assigned to the job with cost centers in the operator's assigned scheme; if the job's cost center is not present, then invoice entry for that job will be disallowed.

Recurring #
Press Enter to display the next available recurring invoice number. Otherwise, enter the recurring invoice number for this transaction.
While in this field, press F4 to open the Unposted A/R Invoices search window. This window displays a list of all unposted invoices and credit memos for the specified customer code (already entered in Invoice Entry). Here you can see the invoice details, including the invoice number, date, the G/L date, the invoice total and any remarks.

Invoice type
Select either Invoice or Credit memo from the drop-down menu, depending upon the transaction type.
Positive numbers will always be entered on invoices and credit memos; the Invoice or Credit memo designation indicates whether the customer's account will be increased or decreased.

Frequency code
Enter the frequency code; for example, M for (M)onthly, Q for (Q)uarterly, or other batch frequencies, as desired.

Customer P.O.
Enter the customer's purchase order number, if applicable.

Must print invoice form prior to update?
Select this checkbox to give the invoice a status of unprinted. If this checkbox is selected, the invoice should be printed in AR Invoice Entry.

Cost center
If the cost center feature is enabled in the Enterprise
 Installation screen, enter a cost center for the recurring
 invoice in this field. Spectrum compares the entered cost center with cost
 centers in the operator's assigned scheme. If the cost center assigned to
 the contract is not present, then that entry for that contract will not be
 allowed.

More Info
Click this button to open the [More Invoice Information](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/more-invoice-information) window. This window will open automatically after
 entering the Customer P.O. and Cost
 center fields.

Internal Notes
Click this button to add an internal invoice note, or edit an existing note.

User-Defined
Click this button to select a user-defined field for use with this invoice.

Financials

Non-taxable
The non-table amount from the invoice entry is displayed in this field.
Note: All values in this section will be updated as detail lines
 are added or changed.

Taxable
The taxable amount from the invoice entry is displayed in this field.

Subtotal
The sum of the non-taxable and taxable line transactions for this invoice are displayed in this field.

Sales tax
The sales tax amount from the invoice entry screen displays in this field.
If the Override calculated tax checkbox is selected, enter a new sales tax amount. No tax calculation will occur if additional lines are added or the invoice date is changed to another date with a different tax rate.

Invoice total
The sum of the Subtotal and Sales tax amounts are displayed in this field.

Override calculated retention?
Select this checkbox to enter a new retention amount.

Override calculated
 holdback?If the PST code is set up for holdback in PST Tax Maintenance
 and the Allocate PST on holdback? option is selected on the More Invoice
 Information window, select this option to enter a PST holdback amount.
Retention
The retention amount from the invoice entry displays in this field. If the
 Override calculated retention checkbox is selected, enter a new
 retention amount. No retention calculation will occur if additional lines
 are added.

- If the Override calculated retention checkbox is selected, enter
 a new retention amount. No retention calculation will occur if additional
 lines are added.

- If the Override calculated holdback checkbox is selected, the
 holdback percentage of the taxable amount displays in this field
 instead.

Retention
 VATThis field only displays when the Utilize
 value added tax (VAT) tracking? checkbox in
 General Ledger Installation is selected. This
 amount will recalculate any time the retention percent is changed.
Retention VAT = 'VAT tax amount' x <retention percentage> / 100
The Sales tax amount is included in its entirety in the
 Current portion. VAT tax is split between
 Current and Retention using
 the 'retention percentage' assigned to the invoice.
If the Override calculated holdback checkbox is selected, the
 Holdback VAT amount displays in this field instead.

Holdback
 PSTIf the PST code is set up for holdback in PST Tax Maintenance
 and the Override calculated holdback checkbox is selected, this field
 will display the holdback percentage amounts for PST.
Current
The Invoice total minus the retention/holdback amount(s) displays in this
 field.

Detail Lines

Type
Select an invoice type:

- Detail

- Message

- Equipment

Equipment
If an Equipment invoice type was selected, enter the
 equipment code for the invoice in this field. Entry of a retired equipment
 code will be disallowed.
If a Detail or Message invoice
 type was selected, this field will be skipped.
This column will be hidden if the Equipment Control module is not present, the
 Enter equipment on non-job
 invoices? option is not selected in Accounts
 Receivable Installation, or this is a contract invoice.

Rate type
If an Equipment invoice type was selected, enter the
 rate type for the invoice in this field.
If a Detail or Message invoice
 type was selected, this field will be skipped.
This column will be hidden if the Equipment Control module is not present, the
 Enter equipment on non-job
 invoices? option is not selected in Accounts
 Receivable Installation, or this is a contract invoice.

Quantity
If applicable, enter the quantity for this line item. If a quantity is entered, the extension is calculated as the quantity multiplied by the unit price. If no quantity is entered, then the extension is entered by the operator.

Description
Enter the description for this invoice line item.

- If a Detail or Equipment invoice
 type was selected, enter a description of up to 30 characters, or
 search for customer invoice messages. If an equipment code has been
 entered, the equipment name from Equipment File Maintenance
 defaults.

- If a Message invoice type was selected, enter a
 description of up to 250 characters, or search for customer invoice
 messages. The rest of the columns will be disabled for Message invoice
 types.

Um
If a quantity was entered, enter the unit of measure for this invoice line item. For example, include EA, LB, and so forth. If no quantity was entered, this field will be skipped.

Unit price
If a quantity was entered, enter a unit price for this line item. If no quantity was entered, this field will be skipped. If an equipment code was entered, the unit price defaults from the rental rate of the equipment from Equipment File Maintenance.

Extension
If the quantity and unit price were entered, this field will be calculated and displayed automatically; no entry is required. If no quantity was entered, enter the total dollar amount for this line.

G/L account
Enter the G/L account code. If the G/L code's status is set to Not used, no entry is allowed.
At the G/L account field in the Invoice Detail portion of the screen, Spectrum will verify the cost center assigned to the G/L account code by comparing the entry to the list of allowed cost centers for that G/L account. Spectrum compares the G/L account's list of shared cost centers with cost centers in the operator's assigned scheme; if there are no common cost centers, then that G/L account code is not allowed. Validation is also performed if the operator attempts to change or delete an existing distribution line. In addition, the cost center assigned to the detail line must be valid for the G/L account code assigned to that line.

Tax
Select this checkbox if this invoice is taxable. Otherwise, leave this checkbox clear if the invoice is not taxable. This information defaults from the Contracts if this is a job invoice.

Expand
Click the Expand button to show the G/L account code description and Cost center description for each detail line, as applicable.
