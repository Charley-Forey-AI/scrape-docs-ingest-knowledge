---
title: "Reverse Customer Invoice | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/reverse-customer-invoice"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/reverse-customer-invoice"
---

# Reverse Customer Invoice

This screen is used to reverse an open invoice, for
 instance, when all merchandise on an invoice is returned. When you enter a customer code and
 invoice number, the software automatically generates a credit memo to reverse the invoice.
Invoices created through Customer Invoice Entry (or through the Work Order or Time + Material modules) can be reversed using this screen. It is possible to reverse these invoices by simply adding a credit memo in Customer Invoice Entry, however Reverse Customer Invoice is easier to use and will automatically create the credit memo. (If appropriate, credit memos can be reversed, resulting in invoices.) If the transaction originated from a Time + Material billing, draw request or work order, you must reverse the original transaction using the reverse feature associated with the source billing process. If you have the proper security authorization, a hyperlink will be available on the error window that links to the proper screen.
When an A/R invoice originating from Service Contract > Contract Billing Processing is reversed in Accounts Receivable, the billing records in Service Contract
 are updated to reflect the reversal. Following the reversal, you can view any of the
 invoices or credit memos generated for this contract, including reversals. If the invoice
 being reversed references a service contract, the reversal will add a record to the Earned
 Revenue G/L Distribution History Table if the Earned revenue basis of the reverse contract
 billing is 'As billed'.
After creating a reversal using this screen, the transaction must be
 treated just like other credit memos; it will be included on the Invoice Entry Edit List
 and Sales Journal, and must be updated. These reversed invoices will display in Customer
 Invoice Entry along with all other invoices and credit memos. If the Must print
 invoices before posting checkbox is selected on the Accounts
 Receivable Installation screen, then the reversed item must be printed.
 There are a few possible reasons this feature would be unavailable: a credit memo already
 exists with the same number as the invoice, the invoice is no longer open, or the invoice
 history has been purged.
Warning: Invoices and work orders created through draw
 requests should not be reversed using this feature. Draw requests may be reversed using
 Reverse Last Draw Request.

## Online Tax Service Calculations

If you are using the AvaTax online tax service, when an invoice is reversed the status of the credit memo online calculation will be set to 'Pending Calculation' and the document code value cleared. This credit memo cannot be updated at this point. This newly created credit memo will display in the [Commit Online Tax Transactions](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/commit-online-tax-transactions) screen as 'Pending'. After the invoice is recalculated, this transaction will be treated like any other uncommitted transaction since it will now have a brand new document code. When online tax calculations are run on a credit memo, it will use the same invoice date that was used on the original invoice (credit memo is created with the same invoice date as the original invoice).

Related information

- [Reverse an Invoice](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/reverse-an-invoice)

- [Sales Journal / Update](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/sales-journal--update)
