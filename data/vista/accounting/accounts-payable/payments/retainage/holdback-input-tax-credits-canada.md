---
title: "Holdback Input Tax Credits: Canada | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/retainage/holdback-input-tax-credits-canada"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/retainage/holdback-input-tax-credits-canada"
---

# Holdback Input Tax Credits: Canada

You can track holdback Input Tax Credits (ITCs) for
 Canada.
If you release holdback and split it for payment, but you only want to make a partial payment, you should pay the portion of the split with the holdback tax *first*. This is because if the taxed remainder of the holdback is put back on hold, you will most likely see an incorrect tax amount.
When tracking holdback ITCs, you can include the
 holdback in the tax basis, or you can calculate the tax basis without holdback. Both
 options are discussed below.

## Tax Basis Net of Holdback

This section discusses how to track
 standard ITCs separately from holdback ITCs. Tracking them separately ensures that holdback tax is not
 expensed until you release and pay the holdback amount.
To withhold holdback from the tax basis,
 you must first select the Tax basis is net of holdback checkbox in the AP
 Company Parameters form. When you select this checkbox, the system calculates the tax basis as line
 amount minus holdback for transactions with an associated Value Added Tax (VAT)
 code.
When setting up tax codes for withholding
 holdback from the tax basis (in the HQ Tax Codes form), you must specify a GL account for
 tracking standard ITCs, tracking holdback ITC payables, and a contra GL account that
 will hold the ITC holdback amount until holdback is released and paid. For more
 information, see [Set Up Tax Codes: Canada](/en/vista/vista/administration/headquarters/tax-code-setup/set-up-tax-codes-canada).
As you create AP transactions associated
 with the tax code (in the AP Transaction Entry, AP Unapproved Invoice Entry, and AP
 Recurring Invoices forms), the system tracks the ITCs in the appropriate accounts. The system
 does not expense the holdback ITC amount until you release and pay holdback. Once you
 [release the holdback](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice) (in the AP Release Retainage form), the
 system moves the holdback ITC amount from the ITC holdback account to the standard ITC
 account.
Single Level Tax Code
 Example
Tables 1, 2, and 3 display how the system
 processes a $1,000 AP transaction with a holdback amount of $100 and a 15% HST
 (Harmonized Sales Tax) rate.
Table 1. Table 1: Transaction Posting GL DistributionsDebit
Credit

Job Expense Account
$1,000
AP Account
$1,035

Standard ITC Account
$135
Holdback AP Account
$100

Holdback ITC Contra
 Account
$15
Holdback ITC AP Account
$15

Table 2. Table 2: Payment Posting GL Distributions - Paying Open PayablesDebit
Credit

AP Account
$1,035
Cash
$1,035

Table 3. Table 3: Payment Posting GL Distributions - Paying Released HoldbackDebit
Credit

AP Account
$100
Cash
$115

Multi-Level Tax Code
 Example
If you are using a multi-level code
 tracking both GST and Provincial Sales Tax (PST), the system includes the PST amount in
 the job expense total; the PST amount is directly expensed.
Tables 4, 5, and 6 display how the system
 processes a $1,000 AP transaction with a holdback amount of $100, a 5% GST rate, and a
 10% PST rate.
Table 4. Table 4: Transaction Posting GL DistributionsDebit
Credit

Job Expense
 Account (including PST)
$1,100
AP Account
$1,035

Standard ITC Account
$45
Holdback AP Account
$110

Holdback ITC Contra
 Account
$5
Holdback ITC AP Account
$5

Table 5. Table 5: Payment Posting GL Distributions - Paying Open PayablesDebit
Credit

AP Account
$1,035
Cash
$1,035

Table 6. Table 6: Payment Posting GL Distributions - Paying Released HoldbackDebit
Credit

AP Account
$100
Cash
$115

## Include Holdback in Tax
 Basis

When you include the
 holdback in the tax basis, you can either track the retainage ITCs in a separate GL
 account from standard ITCs, or you can track both types of ITCs in the same
 account.
Tracking ITCs
 Separately
When
 setting up VAT tax codes for including holdback in the tax basis (in HQ Tax Codes), but
 tracking ITCs separately, you must specify a GL account for tracking standard
 ITCs and one for tracking holdback ITC payables. For more information on creating tax
 codes, see [About the HQ Tax Codes Form](/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form).
As you create transactions associated with the tax code, the system
 tracks the ITCs in two accounts. Once you release the holdback (AP Release Retainage form),
 the system moves the holdback ITC amount from the ITC holdback account to the standard
 ITC account.
Tables 7, 8, and 9
 display how the system processes a $1,000 AP transaction with a holdback amount of $100
 and a 15% HST rate.
Table 7. Table 7: Transaction Posting GL
 DistributionsDebit
Credit

Job Expense Account
$1,000
AP Account
$1,035

Standard ITC Account
$135
Holdback AP Account
$115

Holdback ITC Account
$15

Table 8. Table 8: Payment Posting GL Distributions - Paying
 Open PayablesDebit
Credit

AP Account
$1,035
Cash
$1,035

Table 9. Table 9: Payment Posting GL Distributions - Paying
 Released HoldbackDebit
Credit

AP Account
$100
Cash
$100

Note: If you are using a multi-level code
 tracking both GST and Provincial Sales Tax (PST), the system includes the PST amount in
 the job expense total; the PST amount is directly expensed.
Tracking ITCs
 Together
When you include the
 holdback in the tax basis (in the HQ Tax Codes form) and you are tracking holdback and standard
 ITCs togther, you only need to specify a single ITC-tracking GL account. When tracking
 ITCs together, you can manually exclude holdback from the tax basis. When doing so,
 enter the transaction as normal, but manually decrease the amount in the Basis field
 by the holdback amount and process the transaction.
Table 10 displays how the system processes a $1,000 AP transaction
 with a holdback amount of $100 and a 15% HST rate.
Table 10. Table 10: Transaction Posting GL DistributionsDebit
Credit

Job Expense Account
$1,000
AP Account
$1,035

ITC Account
$135
Holdback AP Account
$100

When you manually exclude the
 holdback from the tax basis, you must create an additional transaction for the holdback
 tax amount (after you have released holdback). To do this, enter a transaction for the
 holdback amount in the Tax Basis field. Using the scenario
 from Table 7, you would enter $100 in the Tax Basis field. The system would then
 automatically calculate $5 as the tax amount, displaying it in the Tax Amt field.
 Process the transaction as normal and complete any additional steps to complete the
 transaction. For more information, see [Processing VAT Invoices](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/process-ap-invoices/processing-vat-invoices).
Note: If you are using a multi-level code
 tracking both GST and Provincial Sales Tax (PST), the system includes the PST amount in
 the job expense total; the PST amount is directly expensed.

Related information

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)

- [AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)

- [AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)

- [AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form)

- [AP Hold and Release Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-hold-and-release-form)
