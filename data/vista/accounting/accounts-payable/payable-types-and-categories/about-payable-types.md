---
title: "About Payable Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/about-payable-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/about-payable-types"
---

# About Payable Types

Payable types determine which liability payable accounts
 are credited (when invoices are posted) and debited (when they are paid).
Each line of a transaction entered in the AP Transaction Entry and AP
 Recurring Invoices forms must be assigned one of the pay types you set up in the AP Payable Types form.
 The assigned pay type determines which liability payable account is credited when the
 invoice is posted and debited when it is paid.
If you assigned pay types in the AP Company Parameters form to the Payable
 Types for Expense, Job, Subcontract, and Retainage, then transactions entered in the AP
 Transaction Entry and AP Recurring Invoices forms automatically default to one of these assigned
 pay types, depending on the type of transaction.
For example, if you have two pay types—one for expenses and one
 for retainage—you would assign them to the four Payable Type options in the AP Company
 Parameters form as follows:
Option
Pay Type

Expense
1

Job
1

Subcontract
1

Retainage
2

Then, in the AP Transaction Entry and AP Recurring Invoices forms, the
 system will assign pay type 1 to all transactions you post for jobs, subcontracts, and
 other expenses, and pay type 2 to the retainage portions of the transactions.
Note: Pay Type defaults may be overridden by the user during
 transaction entry if the Allow Payable Type
 Override checkbox in the AP Company Parameters form is selected.

Related concepts

- [About Using Pay Types for Check Selection](/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/about-payable-types/about-using-pay-types-for-check-selection)
