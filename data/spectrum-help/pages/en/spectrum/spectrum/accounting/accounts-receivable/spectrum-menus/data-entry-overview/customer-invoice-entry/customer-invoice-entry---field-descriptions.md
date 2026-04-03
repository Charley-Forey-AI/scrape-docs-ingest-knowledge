---
title: "Customer Invoice Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/customer-invoice-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/customer-invoice-entry---field-descriptions"
---

# Customer Invoice Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field/Button
Description

Search Transactions
Click this button to search for unposted invoices across batches. Select the invoice you wish to edit and click OK to continue.

Batch
The batch defaults to the Operator code. Enter the batch code, or double-click on this field to select from a list of available batch codes.
The Batch Summary link displays to the right of this field when an invoice is entered. Click this link to view a list of unposted A/R invoices assigned to the current batch and the total amount of displayed invoices.

Customer
Enter the customer code for whom this invoice is being prepared. If this screen was accessed from the Customer Info Bar, the selected customer code will default. If the customer's status is set to Not used, no entry is allowed.
Note: Once you enter or select the customer code, the customer's
 name and mailing address display. If there are two lines of text in the
 address, the second line displays with the city and state below the first
 line of the address and customer's name.

Job
If this invoice is for a contract, enter a valid job number. The job description will display beneath the job number. If this screen was accessed from the Customer Info Bar, the job code will default from the selected customer. If this invoice is not for a contract, press Enter to skip the job number.
When entering a new invoice, if the contract status is closed you will receive an error message and not be able to continue adding the record. When editing an existing invoice, if the contract status is closed you will receive an error message but can continue editing the record.
When entering the job, if there is an error message "RECORD NOT IN FILE
 CR.CNTR," this indicates the contract is not currently on file for this
 customer and job. To resolve this, click Cancel to
 exit the screen and then add the contract information using Contracts.
If the job status is Completed and the
 Disallow revenue entry checkbox is selected in Job
 Main Properties, you will not be able to add the invoice to the job.
If the cost centers feature is enabled, Spectrum will compare the cost center assigned to the job with cost centers in the operator's assigned scheme; if the job's cost center is not present, then invoice entry for that job will be disallowed.

Invoice #
Press Enter to display the next available invoice number. Otherwise, enter the invoice number for this transaction.
 If Multi-Currency processing is being used and [Customer Defaults](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/customers/customer-properties/customer-defaults) are configured to provide invoices in the local currency, a note will display adjacent to this field to let you know that invoice amounts will be translated to the local currency when printed.
Any entity-specific invoice numbers will default in this field if the
 Use entity-specific numbering? option is selected
 in the Accounts Receivable Installation screen. When
 adding a job invoice, the entity is derived from the cost center assigned to
 the contract. For non-job invoices, the entity associated with the cost
 center entered in the screen will be used.
While in this field, press F4 to open the Unposted A/R Invoices
 search window. This window displays a list of all unposted invoices and
 credit memos for the specified customer code (already entered in Invoice
 Entry). Here you can see the invoice details, including the invoice number,
 date, the G/L date, the invoice total and any remarks.

Invoice type
Select either Invoice or Credit memo from the drop-down menu, depending upon the transaction type.
Positive numbers will always be entered on invoices and credit memos; the Invoice or Credit memo designation indicates whether the customer's account will be increased or decreased.

G/L date
Enter the G/L date. The fiscal year and period that correspond with the G/L date display to the right of this field.
When a new date is entered, it is validated against the Minimum/Maximum date
 settings and the current processing period settings in the A/R Processing Date Change
 screen. If the Invoice date
 must be in G/L period checkbox is selected in the Accounts Receivable Installation > Properties screen, then the invoice date must be in the same fiscal
 period as the G/L date.

Invoice date
Enter the Invoice date. If the Invoice date must be in G/L period checkbox is selected in
 the Accounts Receivable Installation > Properties screen, this date will default from the G/L date.
This date is validated against the Minimum/Maximum date settings and the
 current processing period settings (both from the Processing Date
 Change screen). Please refer to the Installation topics for
 more information on setting the default invoice date.

Customer P.O.
Enter the customer's purchase order number, if applicable. When creating a contract invoice (that is, one that has both a customer and job #), this will automatically default from the Contract Defaults page.

Cost center
If the cost center feature is enabled in the Enterprise
 Installation screen, enter a cost center for the invoice in
 this field. If this is a job-related invoice, the contract's cost center
 will default in this field. If the cost center assigned to the contract is
 not present in the operator's assigned scheme, then that entry for that
 contract will not be allowed.

More Info
Click this button to open the [More Invoice Information](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/more-invoice-information) window. This window will open automatically after
 entering the Customer P.O. and Cost
 center fields.

Form Notes
Click this button to open the Notes for Customer window. Use this window to enter any invoice notes for the customer. This window will not be available for recurring invoices.
Note: When notes are added to an existing invoice, the notes will
 be committed to the invoice, regardless of whether the invoice changes are
 saved on the Invoice Entry screen.

Internal Notes
Click this button to open the Internal Invoice Notes window. Use this window to enter or edit any notes for the selected invoice. Existing notes will be displayed in chronological order of entry. When a new note is entered, select whether to copy the note to all other non-zero open items for the customer.

User-Defined
Click this button to open the Invoice User-Defined Fields window. Use this window to enter
 or edit any user-defined fields for the invoice.

Financials

Non-taxable
The non-table amount from the invoice entry is displayed in this field.
Note: All values in this section will be updated as detail lines
 are added or changed.

Taxable
The taxable amount from the invoice entry is displayed in this field.

Subtotal
The sum of the non-taxable and taxable line transactions for this invoice are displayed in this field.

Sales tax will be calculated using Online Tax
 Service
If the Use online tax calculation service checkbox is selected in the [More Invoice Information](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/more-invoice-information) window, click the Online Tax Calculation button to perform the tax calculation and display the calculated invoice total in this field. The online tax code will display in the grid below, and the listing report will indicate 'Sales tax calculated using online tax service'.
Note: This feature will only be available to hosted and SaaS customers.

Override calculated tax?
Select this checkbox to enter a new sales tax or VAT tax amount.
If the Allocate invoice to multiple sales tax codes? checkbox is selected in the More Invoice Information window, the Tax Allocation button will display in place of this field. Click this button to open the [Sales Tax Allocation window](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/sales-tax-allocation-window) window.

Sales tax
The sales tax amount from the invoice entry screen displays in this field.
If the Override calculated tax checkbox is selected, enter a new sales tax amount. No tax calculation will occur if additional lines are added or the invoice date is changed to another date with a different tax rate.

VAT code
This field only displays when the Utilize value added tax (VAT)
 tracking? checkbox in General Ledger
 Installation is selected. Click the available drop-down and
 select the Value Added Tax Code you want to use (for
 example, GST).

VAT tax amount
If VAT processing is being used, the system automatically calculates the tax amount shown here.
Note: The VAT tax calculation does NOT include the provincial sales
 tax.

Invoice total
The sum of the Subtotal and Sales tax amounts are displayed in this field.
Note: This amount includes the VAT tax amount, when VAT processing
 is being used.

Override calculated retention?
Select this checkbox to enter a new retention amount.

Override calculated
 holdback?If the PST code is set up for holdback in PST Tax Maintenance
 and the Allocate PST on holdback? option is selected on the More Invoice
 Information window, select this option to enter a PST holdback amount.
RetentionThe retention amount from the invoice entry displays in
 this field.

- If the Override calculated retention checkbox is selected, enter
 a new retention amount. No retention calculation will occur if additional
 lines are added.

- If the Override calculated holdback checkbox is selected, the
 holdback percentage of the taxable amount displays in this field instead.


Retention
 VATThis field only displays when the Utilize value added tax (VAT)
 tracking? checkbox in General Ledger
 Installation is selected. This amount will recalculate
 anytime the retention percent is changed.
Retention VAT = 'VAT tax amount' x <retention
 percentage> / 100
The Sales tax amount is included
 in its entirety in the Current portion.
 VAT tax is split between
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

Online tax status/code
If the online tax service calculation is in use, this read-only field will display the transaction status and code.

Detail Lines

Type
Select an invoice type:

- Detail

- Message

- Equipment

The invoice type selected here will determine the field and navigation options for this line.

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
 entered, the equipment name from Equipment File
 Maintenance defaults.

- If a 'Message' invoice type was selected, enter a description of up to 250 characters, or search for customer invoice messages. The rest of the columns will be disabled for Message invoice types.

- You can also click in this field to access the Search Unit Price Billings window. The billing items and where the price defaulted from will display in this window. Unit price billing items will only appear in this window if the job is set to 'Unit price'. To use the standard descriptions, enter * plus the code, or click the Standard Descriptions button. For more information on Master Job and Sub-Job Unit Price Billings, view the [Set Up Unit Price Billing Items](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/set-up-unit-price-billing-items) topic.

Um
If a quantity was entered, enter the unit of measure for this invoice line item. For example, include EA, LB, and so forth. If no quantity was entered, this field will be skipped.

Unit price
If a quantity was entered, enter a unit price for this line item. If no quantity was entered, this field will be skipped. If an equipment code was entered, the unit price defaults from the rental rate of the equipment from Equipment File Maintenance.

Extension
If the quantity and unit price were entered, this field will be calculated and displayed automatically; no entry is required. If no quantity was entered, enter the total dollar amount for this line.

G/L account
Enter the G/L account code. If the G/L code's status is set to Not used, no entry is allowed.
At the G/L account
 field in the Invoice Detail portion of the screen,
 Spectrum will verify the cost center assigned to the G/L account code by
 comparing the entry to the list of allowed cost centers for that G/L
 account. Spectrum compares the G/L account's list of shared cost centers
 with cost centers in the operator's assigned scheme; if there are no common
 cost centers, then that G/L account code is not allowed. Validation is also
 performed if the operator attempts to change or delete an existing
 distribution line. In addition, the cost center assigned to the detail line
 must be valid for the G/L account code assigned to that line.

Tax?
Select this checkbox if this invoice is taxable. Otherwise, leave this checkbox clear if the invoice is not taxable. This information defaults from the Contracts if this is a job invoice.

Cost center
The cost center for the detail line will default from the header, but can be overridden if the cost center is in the Operator's assigned scheme. If an equipment related invoice is entered, the equipment's cost center will default in this field.

G/L description
The G/L account code description displays in this field.

Message
If Message invoice type was selected above, enter a message here.
