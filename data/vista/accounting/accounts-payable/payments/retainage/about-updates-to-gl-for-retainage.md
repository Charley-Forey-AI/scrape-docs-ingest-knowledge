---
title: "About Updates to GL for Retainage | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/retainage/about-updates-to-gl-for-retainage"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/retainage/about-updates-to-gl-for-retainage"
---

# About Updates to GL for Retainage

When you apply retainage to an invoice, release retainage that has been held, or
 place released retainage back on hold, the system updates the General Ledger accounts
 accordingly.
 When you post an AP transaction to which you have applied retainage (US),
 retention (AU) or holdback (CA), the system automatically creates entries in General
 Ledger for the retainage/retention/holdback portion of each transaction. Once you
 release retainage/retention/holdback or when you place released
 retainage/retention/holdback back on hold, the system updates the appropriate
 GL accounts. This includes the ITC Contra accounts used for GST/PST (for companies in Australia and
 Canada).
 The following details the General Ledger distributions for retainage transactions.

## United States

Example: You enter an Expense
 transaction for $1000, with 10% retention and 7% sales tax (calculated on the
 invoice total).
Line Gross:$1000
Retainage:$100
Tax Basis:$1000
Tax Amount:$70
Invoice Total:$1070

Once you process the batch, the system creates the GL entries as follows:DebitCredit
Job Expense Account$1070
AP Account$970

Retention Payable Account$100

When you release the retainage, the system updates GL as shown below. This
 example shows a full release of $100.
DebitCredit
Retention Payable Account$100
AP Account$100

If you place the released retainage back on hold, the system updates GL as
 follows:
DebitCredit
AP Account$100
Retention Payable Account$100

## Australia

Example: You enter an Expense transaction for $1000, with 10% retention and 10% GST/PST (net
 of retention).
Line Gross:$1000
Retainage:$100
Tax Basis:$900
Tax Amount:$90
Invoice Total:$900

Once you process the batch, the system creates the GL entries as follows:
DebitCredit
Job Expense Account$1000
AP Account$990

Standard ITC Account$90
Retention Payable Account$100

Retention ITC Contra Account$10
Retention ITC Payable Account$10

When you release the retention, the system updates GL as shown below. This
 example shows a full release of $100 with $10 GST.Note: The system applies the
 current tax rate to VAT tax for before releasing retention.

DebitCredit
Retention Payble Account$100
AP Account$110

Standard ITC Account$10

Retention ITC AP Account$10
Retention ITC Contra Account$10

If you place the released retention back on hold, the system updates GL as
 follows:
DebitCredit
AP Account$110
Retention Payable Account$100

Standard ITC Account$10

Retention ITC Contra Account$10
Retention ITC Payable Account$10

Note:If you release retainage and split it for payment, but you put the retainage back on hold without paying any of the split, the batch posting action to put the retainage back on hold will automatically remove the split.

For detailed information about tracking Retention ITCs, see [Retention Input Tax Credits: Australia](/en/vista/vista/accounting/accounts-payable/payments/retainage/retention-input-tax-credits-australia).

## Canada

Example: You enter an Expense transaction for $1000, with 5% holdback and
 10% GST/PST (net of holdback).
Line Gross:$1000
Retainage:$100
Tax Basis:$900
Tax Amount:$92.16
Invoice Total:$992.16

DebitCredit
Job Expense Account$1042.40
AP Account$992.16

Standard ITC Account$54
Holdback Payable Account$100

Holdback ITC Contra Account$6
Holdback ITC AP Account$6

Credit GL Ret/Hbk Account$4.24

When you release the holdback, the system updates GL as shown below. This
 example shows a full release of $100 with $10 GST.Note: The
 system applies the current tax rate to VAT tax for before releasing
 holdback.

DebitCredit
Holdback Payable Account$100
AP Account$110.24

Standard ITC Account$6

Holdback ITC AP Account$6
Holdback ITC Contra Account$6

Credit GL Ret/Hbk Account$4.24

If you place the released holdback back on hold, the system updates GL as
 follows:
DebitCredit
AP Account$110.24
Holdback Payable Account$100

Standard ITC Account$6

Holdback ITC Contra Account$6
Holdback ITC AP Account$6

Credit GL Ret/Hbk$4.24

Note:If you release retainage and split it for payment, but you put the retainage back on hold without paying any of the split, the batch posting action to put the retainage back on hold will automatically remove the split.

For detailed information about tracking Holdback ITCs, see [Holdback Input Tax Credits: Canada](/en/vista/vista/accounting/accounts-payable/payments/retainage/holdback-input-tax-credits-canada).

Related concepts

- [AP Release Retainage/Retention/Holdback Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-release-retainageretentionholdback-form)

- [About Retainage](/en/vista/vista/accounting/accounts-payable/payments/retainage/about-retainage)

Related tasks

- [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice)

- [Place Released Retainage Back on Hold](/en/vista/vista/accounting/accounts-payable/payments/retainage/place-released-retainage-back-on-hold)
