---
title: "About Using Pay Types for Check Selection | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/about-payable-types/about-using-pay-types-for-check-selection"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/about-payable-types/about-using-pay-types-for-check-selection"
---

# About Using Pay Types for Check Selection

 You can use Pay Types as a way of segregating payables you are preparing to
 pay.
When initializing payments to a payment batch in the
 AP Payment Posting form, you can specify which pay type transactions to add to the work
 file in preparation for the check run.
For instance, by using the Restrict by Payable Type
 option, you could set up the payment batch to only pay retainage payables or only pay job payables.
 Many contractors pay their subcontractors on a different payment schedule than material
 suppliers. This is an excellent reason to use a different pay type for subcontract
 payables.
Taking into consideration this selection capability, you may want
 to set up additional pay types (even if you assign several with the same GL liability
 account) so that you will be able to select categories of transactions for check
 processing.
For example, you might set up the following four Pay Types:
Payable Type
GL Account

1 (job payables)
2100

2 (subcontract payables)
2100

3 (misc. payables)
2100

4 (retainage payables)
2200

You can then assign the four pay types to the four Payable Type
 options in AP Company Parameters.
Option
Pay Type

Expense
3

Job
1

Subcontract
2

Retainage
4
