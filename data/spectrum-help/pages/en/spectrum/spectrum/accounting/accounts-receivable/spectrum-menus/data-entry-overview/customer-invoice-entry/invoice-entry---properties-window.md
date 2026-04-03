---
title: "Invoice Entry - Properties Window | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/invoice-entry---properties-window"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/invoice-entry---properties-window"
---

# Invoice Entry - Properties Window

Use this window to view invoice properties including billing and shipping addresses, and modify G/L account number, terms code, salesperson code and sales tax information.
Field
Description

PrintedDuring initial entry of an invoice, the screen displays Yes if
 the Printing tab on the Accounts Receivable Installation screen
 indicates that invoices should be entered as already
 printed.
If the invoice was generated as a draw request, then transferred
 to Invoice Entry, an X displays in this field.

Print alternate
 address?Select this checkbox to print an alternate bill-to address on the
 invoice.

Billing
 AddressIf the Print alternate address checkbox is
 selected, the company name associated with the selected
 alternate bill-to address code displays. Otherwise, the name
 maintained for the customer in the Customers screen will
 display.

Print job
 address?Select this checkbox if the job address should normally appear on
 the printed invoice.Do not select the checkbox for non-job
 invoices.
If a job invoice should show a ship-to address other than the one
 specified in the Jobs screen, do not select the checkbox and
 then record the alternate address below.

A/R G/L
 account The default Accounts Receivable General Ledger account number
 displays in this field. This account is not normally changed by
 the operator unless multiple A/R accounts are used. If this G/L
 account should be different than specified by default, use the
 up-arrow key at the Terms field to access
 this field for changes. If the G/L code's status is set to 'Not
 used', no entry is allowed.

Terms The normal terms code set up for this customer displays in this
 field. The terms code must have been previously defined through
 Terms Code File Maintenance.

Salesperson The salesperson code for this customer displays in this field.
 This code must already have been previously defined through
 Salesperson Code Maintenance.

Sales
 taxThe sales tax code defined for this customer displays in this
 field. Press Enter to accept this default, or enter a different
 code if desired. The tax rate will display to the right of this
 field; if the percentage is zero, nothing will display. This
 code defaults from the Contracts when
 this is a job invoice.
The sales tax code entered here must have been previously defined
 in Sales Tax Code Maintenance; sales tax codes may be up to 15
 characters long. If an effective date falls before the first
 date in the rate history file, Spectrum will use the earliest
 revision.
If there are different tax rates on different portions of the
 invoice, enter an asterisk (*) in this field. Then, after all
 detail lines have been entered, it will be possible to enter the
 appropriate tax code for each line using the Sales Tax
 Allocation in the summary portion of the screen.

Taxable?Select whether or not this invoice entry is taxable, or press
 Enter to accept the software default.

RetentionIf a job was entered on the main screen, then the retention
 percentage for this contract displays. The retention defaults
 from Contracts. If no job was entered on
 the main screen, this field is bypassed, but it is possible to
 left arrow back and record a retention percentage for the
 invoice.
This percentage will be used to apply any
 retention revenue, if indicated on the contract and Use deferred
 retention revenue account checkboxes on the Accounts Receivable Installation > G/L Codes tab is selected.

Remarks Enter any remarks for this invoice, or enter an asterisk * and a
 message code to use a standard message. When standard messages
 are used, the standard message must already have been set up in
 Item Description/Message
 Maintenance.
