---
title: "Accounts Payable Entries | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-transactions/accounts-payable-entries"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-transactions/accounts-payable-entries"
---

# Accounts Payable Entries

When entering multi-company transactions, always log in to the company that will be issuing checks.
When using Vendors Invoice Entry, after the page header is complete, the cursor is positioned in the account code column of the line transaction portion of the page. Enter the company to which this invoice should be charged; the G/L account code should be from the company that is incurring the expense. Continue completing the page.
In booking the invoice, the transaction will be recorded like this:

## COMPANY PAYING BILLS

DebitCredit
Intercompany AccountAccounts Payable
(from installation page)(from invoice header)

## COMPANY INCURRING EXPENSE

DebitCredit
Expense AccountIntercompany Account
(from invoice detail)(from installation page)

In paying the invoice, the transaction will be recorded:

## COMPANY PAYING BILLS

DebitCredit
Accounts PayableCash

Related information

- [Multi-Company Transactions](/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-transactions)
