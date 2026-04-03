---
title: "Invoices Selected for Current Processing Group window | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/alternate-payee-entry/invoices-selected-for-current-processing-group-window"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/alternate-payee-entry/invoices-selected-for-current-processing-group-window"
---

# Invoices Selected for Current Processing Group window

Use this window to view invoices for the current alternate payee processing group.
Fields
Descriptions

Group
The group code displays based on the company you are working in. No entry is allowed.

Sequence
When the software generates checks, the first check to a vendor is sequence number 01 and must be for a positive dollar amount, the second is sequence number 02, and so on. No entry is allowed.

Invoice / credit memo
For check sequence number 01, all invoices/credit memos selected for payment to this vendor display. No entry is allowed. Press the Tab key to advance the cursor to the Check remarks field and press F4 to access the search for invoice/credit memos using the A/P Checks window.
When the amount due to a vendor should be paid with two or more separate checks, sequence 01 will automatically include all amounts not selected for subsequent checks. Thus, it would be possible, if check one should go to the vendor, and check two should be jointly to the vendor and an alternate, to enter only sequence 02 on this screen. Sequence 01 would then be made out to the vendor for the amount not included on the alternate's check. Discounts must be taken on sequence 01.
For all checks subsequent to sequence number 01, no invoices display. Enter an invoice/credit memo number. For checks with a sequence number higher than 01, enter the number of the invoice to be included on the check to this alternate payee window to view invoices which have already been selected.

Type
For each invoice listed, the invoice type displays: Invoice or Credit memo. No entry is allowed.

Available amount
The dollar amount due, less any discount, displays. No entry is allowed.
When partial invoice payments are made with check sequence number higher than 01, the amount which is available for payment is automatically adjusted on check sequence number 01.

Payee amount
For check sequence number 01, the available amount must be paid in full. No entry is allowed.
For checks with a sequence number higher than 01, enter the portion of the available amount which should be paid to the alternate. When partial invoice payments are made with checks having a sequence number higher than 01, the amount which is available for payment (and the corresponding payee amount) is automatically adjusted on check sequence number 01.

Check remarks
For check sequence number 01, remarks typed during Vendor Invoices Entry display. Enter any revisions to the remarks which should print on the check. Note that the first 15 characters print when standard check stock is used.

OK?
Select this checkbox if the line is acceptable and the displayed amount should be paid.
