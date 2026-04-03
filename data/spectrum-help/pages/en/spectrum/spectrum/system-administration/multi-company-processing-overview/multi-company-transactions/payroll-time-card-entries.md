---
title: "Payroll Time Card Entries | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-transactions/payroll-time-card-entries"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/multi-company-processing-overview/multi-company-transactions/payroll-time-card-entries"
---

# Payroll Time Card Entries

When entering multi-company transactions, always log in to the company that will be issuing checks.
When using Time Card Entry, after the page header is complete, the cursor is positioned in the pay type column of the line transaction portion of the page. Enter the appropriate pay type (regular, overtime, and so on), and enter the company to which this employee's hours should be charged. The payroll department must be in the company being charged.
The transaction will be recorded like this:

## COMPANY PAYING PAYROLL

DebitCredit
Intercompany AccountCash & Liabilities

## COMPANY INCURRING EXPENSE

DebitCredit
Labor ExpenseIntercompany Account
