---
title: "Alternate Payee Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/alternate-payee-entry/alternate-payee-entry---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/alternate-payee-entry/alternate-payee-entry---field-descriptions"
---

# Alternate Payee Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Vendor
Enter the code of the vendor whose check will include an alternate payee or use the available drop-down arrow to select from a list of valid vendor codes. Vendors with a status of Not used may not be selected.
When a vendor is set to be paid electronically and an Alternate Payee is entered, the alternate payee transaction is paid with a live paper check. In this case, line 01 will be paid electronically, and lines 02-99 will be paid via live check.

Line
Enter the check number. When the software generates checks, the first check to a vendor is sequence number 01 and must be for a positive dollar amount, the second is 02, and so on (up to 99 sequences per cycle).
If a portion of the payment should go to the vendor and a portion to an alternate payee, use sequence numbers 02-99.
Alternate Payee Line '01' will use the payment method assigned during Payment Selection

- Example #1: When the vendor's 'payment method' in Vendor Payment Setup was 'Electronic payment' when invoices were selected, then invoice amounts not re-assigned to another 'Alternate Payee Line' will be paid electronically.

- Example #2: When the vendor's 'payment method' in Vendor Payment Setup was 'Comdata' when invoices were selected, then invoice amounts not re-assigned to another 'Alternate Payee Line' will be paid through Comdata.

Alternate Payee Lines '02' – '99' will always be paid using a "printed check" (that is, as if 'payment method' = 'Check'), regardless of Vendor Payment Setup or payment method assigned to items selected for payment

- Example #1 continued: Invoice amounts on Alternate Payee Lines '02-99' will be paid with 'printed checks' (not electronically).

- Example #2 continued: Invoice amounts on Alternate Payee Lines '02-99' will be paid with 'printed checks' (not through Comdata).

- Example #3: When the vendor's 'payment method' in Vendor Payment Setup was 'Print checks' (or 'Print Checks / Send electronic pre-note') when invoices were selected, then all invoice amounts (on every 'Alternate Payee Line') will be paid with a 'printed checked'.

Alternate payee name
The default is that checks are made out jointly to the vendor and an alternate payee, then mailed to the vendor. Information defaults from the Vendors screen but may be overridden.
A search window is available to select from a list of sub-tier vendors defined for the vendor in context.

Payee name
Information in this field defaults when adding a new line to the vendor name.

One time?
Select this checkbox to indicate whether the particular alternate payee for this transaction line is for one-time use only.

Invoices

- Yes displays if the sum of the values in the Payee amount column is non-zero.

- No displays if the sum of the values in the Payee amount column is zero.

Double-click in this field to open the [Invoices Selected for Current Processing Group window](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/alternate-payee-entry/invoices-selected-for-current-processing-group-window).

Address info fields
Information in these fields defaults as you tab through them.
