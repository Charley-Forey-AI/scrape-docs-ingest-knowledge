---
title: "Retention Input Tax Credits: Australia | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/retainage/retention-input-tax-credits-australia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/retainage/retention-input-tax-credits-australia"
---

# Retention Input Tax Credits: Australia

Options for tracing retention Input Tax Credits
 (ITCs) for Australia.
When tracking retention ITCs, you can include the retention in the
 tax basis, or you can calculate the tax basis without retention. Both options are discussed
 below.
Note: For instances where the word retainage is used, it
 refers to retention.

## Tax Basis of Net Retention

This section discusses how to track standard ITCs separately from retention ITCs. This ensures that retention tax is not expensed until you release and pay the retention amount.
To withhold retention from the tax basis, you must
 first select the Tax basis is net of retention checkbox in the AP Company Parameters form. When
 selected, the system calculates the tax basis as the line amount minus retention for
 transactions with an associated Value Added Tax (VAT) code.
When setting up tax codes for withholding retention
 from the tax basis (in the HQ Tax Codes form), you need to specify a GL account for
 tracking standard ITCs, tracking retention ITC payables, and a contra GL account to hold
 the ITC retention amount until retention is released and paid. For more information on
 creating tax codes, see [About the HQ Tax Codes Form](/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form).
As you create AP transactions associated with the
 tax code (in AP Transaction Entry, AP Unapproved Invoice Entry, and AP Recurring
 Invoices), the system will track the ITCs in the appropriate accounts. The system will
 not expense the retention ITC amount until you release and pay retention. Once you [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice) (using the AP Release Retainage), the system
 moves the retention ITC amount from the ITC retention account to the standard ITC
 account.
Note:If you release retention and split it for payment, but you only want to make a partial payment, you should pay the portion of the split with the retention tax *first*. This is because if the taxed remainder of the retention is put back on hold, you will most likely see an incorrect tax amount.

Tables 1, 2, and 3 display how the system process a $1,000 AP transaction with a retention amount of $100 and a 5% tax rate when the tax basis is net of retention.
Table 1. Table 1: Transaction Posting GL
 DistributionsDebit
Credit

Job Expense Account
$1,000
AP Account
$945

Standard ITC Account
$45
Retainage AP Account
$105

Retention ITC Contra Account
$5
Retention ITC AP Account
$5

Table 2. Table 2: Payment Posting GL Distributions -
 Paying Open PayablesDebit
Credit

AP Account
$945
Cash
$945

Table 3. Table 3: Payment Posting GL Distributions -
 Paying Released RetentionDebit
Credit

AP Account
$100
Cash
$105

## Including Retention in Tax Basis

When you include the retention in the tax basis, you can either track the retention ITCs in a separate GL account from standard ITCs, or you can track both types of ITCs in the same account.
Tracking ITCs Separately
When setting up VAT tax codes for including
 retention in the tax basis (in the HQ Tax Codes form), but tracking ITCs separately, you will
 need to specify a GL account for tracking standard ITCs and one for tracking retention
 ITC payables. For more information on creating tax codes, see [About the HQ Tax Codes Form](/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form).
As you create transactions associated with the tax
 code, the system tracks the ITCs in two accounts. Once you release the retention (using the AP
 Release Retainage form), the system moves the retention ITC amount from the ITC retention
 account to the standard ITC account.
Tables 4, 5, and 6 display how the system processes a $1,000 AP transaction with a retention amount of $100 and a 5% tax rate when retention is included in the tax basis.
Table 4. Table 4: Transaction Posting GL
 DistributionsDebit
Credit

Job Expense Account
$1,000
AP Account
$945

Standard ITC Account
$45
Retainage AP Account
$105

Retainage ITC Account
$5

Table 5. Table 5: Payment Posting GL Distributions -
 Paying Open PayablesDebit
Credit

AP Account
$945
Cash
$945

Table 6. Table 6: Payment Posting GL Distributions -
 Paying Released RetentionDebit
Credit

AP Account
$100
Cash
$100

Tracking ITCs Together
When you include the retention in the tax basis (in
 HQ Tax Codes) and you are tracking retention and standard ITCs together, you only need to
 specify a single ITC-tracking GL account. When tracking ITCs together, you can manually
 exclude retention from the tax basis. When doing so, enter the transaction as normal,
 but manually decrease the amount in the Basis field by the retention amount
 and process the transaction.
Table 7 displays how the system processes a $1,000 AP transaction with a retention amount of $100 and a 5% tax rate.
Table 7. Table 7: Transaction Posting GL
 DistributionsDebit
Credit

Job Expense Account
$1,000
AP Account
$945

ITC Account
$45
Retainage AP Account
$100

When you manually exclude the retention from the tax basis, you must create an
 additional transaction for the retention tax amount (after you have released retention).
 To do this, enter a transaction for the retention amount in the Tax Basis
 field. Using the scenario from Table 7, you would enter $100 in the Tax Basis
 field. The system would then automatically calculate $5 as the tax amount, displaying it
 in the Tax Amt field. Process the transaction as normal and complete any additional
 steps to complete the transaction. For more information, see [Processing VAT Transactions ](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/process-ap-invoices/processing-vat-invoices).

Related information

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)

- [AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)

- [AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)

- [AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form)

- [AP Hold and Release Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-hold-and-release-form)
