---
title: "A/R Invoice Form - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/ar-invoice-form/ar-invoice-form---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/ar-invoice-form/ar-invoice-form---field-descriptions"
---

# A/R Invoice Form - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Invoice source
Select one or more of the invoice sources to include on the report:

- Accounts receivable

- Draw request

- Time + material

- Service contract

- Work order

The Accounts receivable source includes invoices and credit memos added in Invoice Entry, plus ones originating in Recurring Invoice Entry and from Materials Management.
Note: If the Time + Material, Service Contracts or Work Order modules are not present, the respective checkboxes will be hidden. If the Print status is set to First print only, the Draw request checkbox will be hidden.

Invoice format
Select the invoice format you want to print:

- Mailer

- Standard

- Retention

- Work order

If the Work Order format is selected and the extension is zero, then the material will not show up on Time + Material type work orders.
An option is available to produce a retention invoice for a contract. The Retention format provides an itemized list of retention balances due on open invoices for the contract and prints on both the pre-printed and plain-paper invoice formats. Use of this format does not result in any change to the customer or G/L balances, since the revenue and receivable amounts have already been recognized at the time the original invoice was processed, but allows you to create a "memo invoice" for the customer.

Print status
Select the print status for this batch.
Note: Draw requests are not included when the First print status is selected since the print status of draw request invoices are automatically treated as printed from the time they are first created. To print a draw request invoice, select Reprint and select the Draw request checkbox in Invoice source.

Job
Enter the job number for which to print an invoice, or press Enter to print ALL jobs.

Customer
Enter the customer code for which to print an invoice, or press Enter to print ALL customers.
If the invoice form is launched from the Customer Open Items or Customer Payment History screens, the customer code will default in this field.

Batch
Enter the batch code, or press Enter to accept the default of ALL batch codes.
Note: This field will be hidden if the Retention invoice format is selected.

Invoice
Enter the invoice number, or press Enter to accept the default of ALL invoices.
If the invoice form is launched from the Customer Open Items or Customer Payment History screens, the invoice number will default in this field.
Note: This field will be hidden if the Retention invoice format is selected.

Invoice date
Enter the first and last invoice dates for which to print an invoice, or press Enter to begin with the earliest date and end with the current A/R processing date.

Retention terms
Enter the retention terms code, or leave this field blank to use the customer default.
Note: This field is only available when the Retention option is selected in the Invoice format box.

Include all posted A/R invoices with an outstanding balance?
Select this checkbox to include invoices and credit memos with a non-zero balance, including ones with retention-only balances.
Note: This option should only be selected when the Print status is set to Reprint only or All, as all open invoices have already been printed.

Print detail for flat rate Work Order invoices?
When this option is selected the invoice will include information stored in certain Work Order history tables. This option will show transactions associated with the Bill # of the current invoice, and exclude transactions for other billings.
This option applies to the Mailer, Standard and Work order invoice formats. This field will be hidden if the Work Order module is unavailable.

- On the Mailer and Standard invoice formats, when flat rate invoices originating from the Work Order module are printed, if this box is clear but the invoice includes a non-zero extension T+M detail, these amounts will be grouped on the invoice as "Other."

- On the Work Order invoice format, when flat rate invoices originating from the Work Order module are printed, if this box is selected then the invoice form may include detail lines with a zero-dollar extension.
Tip: Work orders may be specified as flat rate in the Price field in the New/Edit Work Order - Properties window.

Message
Enter the message to print on this group of invoices, if desired. To print a standard message, enter an asterisk (*) and a valid message code to print a standard message on this group of invoices. Otherwise, press Enter to leave this field blank.
