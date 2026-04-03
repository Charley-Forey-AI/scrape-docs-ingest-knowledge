---
title: "More Invoice Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/more-invoice-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/more-invoice-information"
---

# More Invoice Information

The More Invoice Information window
 will open automatically after the Customer P.O. (and Cost center) field is entered in the
 Customer Invoice Entry screen. Use this window to add tax and
 payment terms to the invoice.
Field
Description

Invoice remark
Enter any remarks for this invoice, or enter an asterisk * and a message code to use a standard message. A lookup window is also available for viewing existing and selected standard remarks.
When standard messages are used, the standard message must already have been
 set up in Item Description/Message Maintenance.

Customer's job
Enter the customer's job number, if applicable.

Invoice status
This field will display the invoice status: Unposted or
 Posted, (unprinted or printed). New invoices will
 be set to (unprinted) by default.
Draw requests will display as Unposted (Draw
 request).

Tax and terms

Use online tax calculation?
If the option to use online customer payments is selected in
 Accounts Receivable Installation, this checkbox
 will be available. Select this checkbox to use the Avatax service to
 determine the appropriate jurisdiction, calculate the correct sales tax
 amount and file sales tax reports with the taxing authorities. When this
 option is selected, the Taxable, Allocate invoice to multiple tax codes and
 Sales tax
 fields will be disabled, thereby disabling the user's ability to override
 the sales tax amount.
Note: If you do not have security permission to this field, you
 will be unable to edit this field.

Taxable
Select whether or not this invoice is taxable.
If taxable, the sales tax rate based on invoice date and sales tax rate will appear to the right of this field.

- If the Override calculated tax? option was selected, the percentage-based override amount will display.

- If the Allocate invoice to multiple sales tax codes? option was selected, the composite percentage based on allocated taxable amounts and rates will display.

Allocate invoice to multiple sales tax codes?
Select this checkbox to override the sales tax and set up additional tax codes before revenue is recorded.
Note: This checkbox will not be available for recurring
 invoices.

Sales tax
The sales tax code defined for this customer displays; up to 15 characters are
 allowed. Press Enter to accept this default, or enter a different code if
 desired. The tax percentage will display. If the percentage is zero, nothing
 will display. This code defaults from the Contracts
 when this is a job invoice.
The sales tax code entered here must have been previously defined in
 Sales Tax Code Maintenance; sales tax codes may be
 up to 15 characters long. A lookup window is available for viewing valid
 sales tax codes. If an effective date falls before the first date in the
 rate history file, Spectrum will use the earliest revision.
If the Allocate invoice to multiple sales tax codes? is selected, the Tax Allocation button will display here in place of this field. Click this button to open the [Sales Tax Allocation window](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/sales-tax-allocation-window) window.

Payment terms
The normal payment terms code set up for this customer displays in this field.
 Press Enter to
 accept the default, or enter a different terms code if desired. This code
 defaults from the Customers screen. The terms code
 must have been previously defined through Terms Code File
 Maintenance.

Retention
If a job was entered on the main screen, then the
 retention percentage for this contract displays; the retention defaults from
 Contracts. If no job was entered on the main
 screen, this field is bypassed, but it is possible to left arrow back and
 record a retention percentage for the invoice.
This percentage will be used to apply any retention
 revenue, if indicated on the contract and the Use deferred retention revenue
 account checkbox on the Accounts Receivable
 Installation > G/L Codes tab is selected.

- If the Override calculated retention? checkbox is selected, the
 override percentage will be displayed in this field.

- If VAT processing is enabled for this company, select the PST on holdback? checkbox to hold back
 the retention percentage for provincial sales tax. Making changes to this
 checkbox requires all detail lines to be deleted first. This option will
 only be available when the PST on holdback? checkbox is selected in
 Sales Tax code Maintenance. This option will
 not be available if the Allocate invoice to
 multiple sales tax codes? checkbox is selected.

Other settings

Salesperson
The salesperson code for this customer displays. Press Enter to accept this
 default, or select a different code if desired. This code must already have
 been previously defined through Salesperson Code
 Maintenance.

A/R G/L account
The default Accounts Receivable General Ledger account number displays. Press Enter to accept this default; otherwise, enter a different account number if desired. This account is not normally changed by the operator unless multiple A/R accounts are used.
If the G/L code's status is set to Not used, no entry is allowed.
If the selected customer is a related party customer, the Override A/R trade
 G/L account will default in this field.

Billing address

Print alternate billing address?
Select this checkbox to print an alternate bill-to address on the invoice;
 otherwise, if this checkbox is left clear, the name and address in the
 Customers screen will print on the invoice.

Bill-to code
If you selected the Print alternate billing address checkbox, enter the bill-to code for the address that you want printed on the invoice, or double-click on this field to select from a list of available bill-to codes in the Alternate Bill-to Address window. Alternate bill-to codes can also be added or edited from this window.
If you are adding an invoice that is referencing a job, the bill-to code that
 is specified in Contracts will automatically default
 in this field.

Shipping address

Shipping address
For NON-JOB invoices, enter a shipping address in the text box.

Print job address on invoice?
For JOB invoices, select this checkbox to display the job address below. When this checkbox is not selected, enter a shipping address in the text box.
