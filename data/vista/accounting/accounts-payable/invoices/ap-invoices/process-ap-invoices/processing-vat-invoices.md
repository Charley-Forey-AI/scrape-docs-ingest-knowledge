---
title: "Processing VAT Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/process-ap-invoices/processing-vat-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/process-ap-invoices/processing-vat-invoices"
---

# Processing VAT Invoices

Processing AP invoices with Value Added Tax (VAT) requires a slightly different process than other invoices, as VAT tax is not directly expensed.
Set up the system to track standard ITCs separately from retainage ITCs. For more information, click on one of the following links:[Tracking Retainage Input Tax Credits: Australia](/en/vista/vista/accounting/accounts-payable/payments/retainage/retention-input-tax-credits-australia)
[Tracking Retainage Input Tax Credits: Canada](/en/vista/vista/accounting/accounts-payable/payments/retainage/holdback-input-tax-credits-canada)

 Value Added Tax is paid on goods and services at each stage of production or distribution, and is based on the value added at each stage. The system tracks this tax in GL and it reduces the payment to a taxing authority through an Input Tax Credit (ITC). You do not directly expense VAT. The following instructions detail how to process VAT invoices in
 AP.

1. When you receive an invoice from the vendor, enter the invoice (in AP Transaction Entry, AP Unapproved Invoice Entry, or AP Recurring Invoices) and post the invoice.

1. Post the payment in AP
 Payment Posting.

1. Release retainage using AP
 Release Retainage. Note: If you are tracking retainage ITCs separately, the system debits the ITC retainage account ( Debit GL Retg
 Account field, HQ Tax Codes) and credits the standard ITC account ( Debit
 GL Account field, HQ Tax Codes) when you pay the release retainage transaction.

1. Create an invoice for the taxing authority. This includes two steps:

1. Create a journal entry in GL Journal Transaction Entry to debit the ITC
 amount from the tax liability account (
 Credit GL Account
 field, HQ Tax Codes) and credit the ITC amount to the standard
 ITC account (
 Debit GL Account
 field, HQ Tax Codes).

1. Create an AP expense transaction for the taxing authority. Reference the tax
 liability account (
 Credit GL Account
 field, HQ Tax Codes) in the GL account field. When you process
 the transaction, the system debits the tax liability account and credits the
 expense payable account (
 Expense
 field, AP Company Parameters, Pay Types Discounts/Report Info
 tab)

1. Use AP Payment Posting to post the payment to the taxing authority.

Related information

- [Process AP Invoices](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/process-ap-invoices)

- [Post Sales, Use, and Value Added Tax](/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/post-sales-use-and-value-added-tax)

- [AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)

- [AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)

- [AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form)

- [AP Hold and Release Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-hold-and-release-form)

- [About the GL Journal Transaction Entry Form](/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-journal-transaction-entry-form)

- [AP Payment Posting Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form)

- [About the HQ Tax Codes Form](/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form)
