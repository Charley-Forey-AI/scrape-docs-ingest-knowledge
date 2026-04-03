---
title: "Explanation of Journal Entries | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/explanation-of-journal-entries"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/explanation-of-journal-entries"
---

# Explanation of Journal Entries

View an example of journal entries.
In this example, the employee is currently paid weekly at
 $15.75/hour. Assume no burden for these calculations. Employee accrues 4 weeks of vacation
 per year. This translates into 3.2 hours accrued each pay cycle. At the start of this
 example, the employee has 120 hours in their vacation bank.2710
0240

Vacation Expense
Vacation Payable

1890.001
1890.001

50.403
50.403

630.004
50.405
50.405

630.006
630.006

1940.40
1360.80

Hours Bank

120.01
40.04

3.22

3.25

86.46

1. At the conversion date, the Vac/Hol/Sick G/L Accrual charges vacation expense and offsets it with vacation payable (120 hours at $15.75/hour equals 1890.00)

1. During the next pay cycle, the employee accrues an additional 3.2 hours, as shown in the Hours Bank table. (There is no impact on the General Ledger yet).

1. After the pay cycle is finished, the Vac/Hol/Sick G/L Accrual Update creates the accrual journal entry. (3.2 hours at $15.75/hour equals $50.40).

1. The next week, the employee takes 40 hours of vacation (40 hours, shown in the Hours Bank table, at $15.75/hour equals $630.00).Note: The offset to this entry is cash and other tax liabilities.

1. When the Vac/Hol/Sick G/L Accrual Update is run, it creates the accrual journal entry to accrue an additional 3.2 hours (3.2 hours as shown on the Hours Bank table and 50.40 as show in the Vacation Expense table).

1. Now it is necessary to reduce Vacation Payable by the 40 hours taken. The offset to this is the Vacation Expense account. Notice that the credit (86.4) to the expense account offsets the earlier debit taken (40.0) in the Hours Bank table.

1. After the pay cycle is complete, the employee now has 86.4 hours remaining of vacation (86.4 hrs at 15.75/hour is $1360.80).
