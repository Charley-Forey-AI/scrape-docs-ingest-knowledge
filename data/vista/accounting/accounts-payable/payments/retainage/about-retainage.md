---
title: "About Retainage | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/retainage/about-retainage"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/retainage/about-retainage"
---

# About Retainage

Retainage is the portion of an invoice's gross amount that is withheld for payment until a later date. It remains on hold until you release it for payment.
Note: This topic uses the term "retainage" (US) to also mean retention (AU) and holdback (CA).

When you post retainage to an invoice in AP, you can specify a dollar amount or percentage for each transaction line on the invoice. The system automatically creates an additional sequence number to accommodate the retainage portion of each transaction, and assigns a Hold status to the sequence. When you are ready to pay the retainage amount, you must release it using AP Release Retainage so that it becomes available for payment.
Before you can account for retainage on payable invoices, there are initial setup steps that you must follow. Once you complete the initial setup, you can apply retainage to transactions in AP Transaction Entry, AP Unapproved Invoice Entry, or AP Recurring Invoice Entry. For information about the initial setup, see [Enable Retainage for Payable Invoices](/en/vista/vista/accounting/accounts-payable/payments/retainage/enable-retainage-for-payable-invoices#task-7933--en__task-7933).

## Applying Retainage to an Invoice

When you apply retainage to an invoice line, the system automatically splits the transaction line into two sequence numbers to accommodate the retainage portion.
For example, when entering a transaction line with a gross amount of $25,000 and a retainage amount of $2,500, the system splits the transaction into two sequences, as shown below. Seq #1 is the gross amount less retainage, Seq #2 is the retainage amount only. Note that the retainage sequence has a Hold status.
Trans #
Line #
Seq #
Amount
Pay Type
Status

100
1
1
$22,500
1 (Job)
Open

100
1
2
$2,500
9 (Retain)
Hold

The system splits the transaction internally and does not display both sequences on screen. Only the line is visible and it displays both the gross amount and the retainage amount. You can view the split transaction on specific reports, such as AP Open Payables, AP Invoices, and AP Transactions by Vendor.
The Retainage amount is included in the vendor's outstanding payable balance on reports, but the retainage is not available for payment until you release it (via AP Release Retainage). Once you release retainage, the system assigns an Open status and the retainage amount of the transaction is available for payment.

## Releasing Retainage

Retainage portions of payable transactions are automatically placed on hold when the transaction is entered. You must use AP Release Retainage to release retainage before it can be paid.
 You can release retainage using one of three options:

- Specific Amount - Release a specific amount of held retainage for the vendor based on the selection criteria.

- Percent of the Total - Release a percent of each vendor's total held retainage based on the selection criteria.

- Percent on Each Invoice - Release a percent of held retainage on each invoice based on selection criteria.

For detailed information about each of these options, along with examples of how the system releases retainage specific to each option, see the F1 help for [Specific Amount or Percent](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-release-retainageretentionholdback-form/field-definitions-ap-release-retainage-form#concept-9980--en).
For instructions on releasing retainage, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).

Related information

- [Retention Input Tax Credits: Australia](/en/vista/vista/accounting/accounts-payable/payments/retainage/retention-input-tax-credits-australia)

- [Holdback Input Tax Credits: Canada](/en/vista/vista/accounting/accounts-payable/payments/retainage/holdback-input-tax-credits-canada)

- [AP Hold and Release Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-hold-and-release-form)

- [AP Payment Control Detail Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-control-detail-form)

- [HQ Hold Codes Form](/en/vista/vista/administration/headquarters/company-setup/hq-hold-codes-form)

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)

- [AP Payable Types Form](/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/ap-pay-typescategories-forms/ap-payable-types-form)

- [AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)

- [AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)

- [AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form)
