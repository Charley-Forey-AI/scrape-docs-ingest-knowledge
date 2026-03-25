---
title: "General Ledger Update | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update/general-ledger-update"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/run-a-ledger-update/general-ledger-update"
---

# General Ledger Update

General Ledger distributions are tracked, and values maintained, for both the current and last GL update run for each pay period.
Current values are recalculated with each update. During the update, if the current and last updated values are equal, no entries are posted to GL. If they don’t match, then a reversing entry is made to back out the old amounts and a new entry is added for the current amounts. After GL is updated, the current values are copied to the old ones, saving them as the last interface values. All entries are saved until the pay period is purged.
Dollars are always updated to GL when payroll information is updated to GL; however, payroll hours also update to GL if you have specified a “Cross Reference Memo Account” (in GL Chart of Accounts) for each account to which earnings are posted. If an account is not specified, then hours are not posted in GL. See [Cross Reference Memo Account](/en/vista/vista/accounting/general-ledger/gl-accounts/about-the-gl-chart-of-accounts-form/field-definitions-gl-chart-of-accounts-form#ID-0000e052--en) for more information.

## Split Month Distributions

If a pay period has expenses and/or payments in two different months, then the GL distributions are split according to the following tables.
Table 1. 1st MonthDebits
Credits

Labor Expense (posted date <= cutoff date)
Cash (paid month = 1st month)

Burden (posted date <= cutoff date)
Dedns (paid month = 1st month)

Liabs (paid month = 1st month)

Payroll Accrual (earnings and liabs posted <= cutoff date, but paid month = 2nd month)

Table 2. 2nd MonthDebits
Credits

Labor Expense (posted date > cutoff date)
Cash (paid month = 2nd month)

Burden (posted date > cutoff date)
Dedns (paid month = 2nd month)

Payroll Accrual (offset to credit posted in 1st month)
Liabs (paid month = 2nd month)
