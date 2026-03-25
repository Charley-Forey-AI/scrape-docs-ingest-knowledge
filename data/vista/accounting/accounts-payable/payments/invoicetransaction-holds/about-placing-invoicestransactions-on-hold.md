---
title: "About Placing Invoices/Transactions on Hold | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/about-placing-invoicestransactions-on-hold"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/about-placing-invoicestransactions-on-hold"
---

# About Placing Invoices/Transactions on Hold

You can place invoices/transactions on hold to prevent them
 from being paid until you release the hold.
You can use hold codes to prevent certain invoices and/or vendors
 from being paid until you release payment. Hold codes are defined in the HQ Hold Codes form and you
 must set up at least one code to be used for retainage, but you can set up multiple codes
 to differentiate several reasons for holds. You can also assign multiple hold codes to
 vendors and transactions.
Non-retainage holds may be placed on
 invoices/transactions in many forms:

- At the time of entry in AP Transaction Entry, AP Recurring Invoices, SL
 Worksheets, and/or AP Unapproved Invoice Entry

- Using the Hold/Release tab of AP Payment Control Detail (accessed from
 within AP Payment Workfile)

- In AP Hold and Release

- For subcontracts in the SL module (SL Subcontract Entry and SL
 Worksheet)

- For purchase orders in the PO module (PO Purchase Order Entry)

- By vendor in AP Vendor Hold Codes

Transactions that are on hold are not initialized into a payment work
 file in AP Payment Posting.Note: You can only apply retainage holds
 to payable transactions during entry in AP Transaction Entry, AP Unapproved Invoice
 Entry, and AP Recurring Invoices. When you apply retainage to a transaction (invoice)
 line, the system automatically puts the retainage on hold using the hold code specified
 for retainage in AP Company Parameters (Pay Types/Discounts/ICR tab). When you are ready
 to release retainage, you must use AP Release Retainage.

Related tasks

- [Assign a Hold Code to Multiple Invoices](/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/assign-a-hold-code-to-multiple-invoices)

- [Assign Hold Codes to Specific Invoices](/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/assign-hold-codes-to-specific-invoices)

- [Release Hold Codes for Multiple Invoices](/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/release-hold-codes-for-multiple-invoices)

- [Release Hold Codes for Specific Invoices](/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/release-hold-codes-for-specific-invoices)

- [Release Hold Codes in AP Payment Workfile](/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/release-hold-codes-in-ap-payment-workfile)

Related information

- [AP Hold and Release Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-hold-and-release-form)

- [AP Payment Control Detail Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-control-detail-form)

- [HQ Hold Codes Form](/en/vista/vista/administration/headquarters/company-setup/hq-hold-codes-form)

- [AP Payment Workfile Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-workfile-form)
