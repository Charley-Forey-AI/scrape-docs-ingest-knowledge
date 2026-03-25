---
title: "Interfacing Split-Month Pay Periods to GL | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-with-the-general-ledger/interfacing-split-month-pay-periods-to-gl"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-with-the-general-ledger/interfacing-split-month-pay-periods-to-gl"
---

# Interfacing Split-Month Pay Periods to GL

If your pay periods are weekly or biweekly, occasionally one
 will span two months.
You may just post all of the period into one month or the other, or you may wish to split the period so that the General Ledger reflects the true picture—part of the expense applies to one month and part to the other month. You can split a pay period into two months so that the GL interface accurately depicts both months.
To activate the split month feature:

1. Set up a split-month pay period in PR Pay Period Control. For more information, see [Setting Up Split-Month Pay Periods](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/set-up-split-month-pay-periods).

1. Verify that you have
 indicated the GL Accrual Account code and the CM Account number in the PR
 Groups. These fields determine the GL cash and accrual account codes to which
 the entries are made.

1. When you are ready to interface to GL, go to PR Ledger Update, and in the Available Updates section, check the General Ledger/Cash Mgmt/Accumulations box. The program will automatically update GL Accrual and GL Cash accounts according to the following to the following tables: The system uses the date of each timecard transaction in PR Timecard Entry to determine to which month the GL entry is posted. For automatic earnings, the system uses the Posting Date entered when you process in PR Post Automatic Earnings. Remember that you can edit the automatic earnings transactions in PR Timecard Entry if you want to adjust some of the dates.
Notice that in addition to splitting the expense month, the system is also recording the Cash according to the date paid. Therefore, if some checks are paid in the first month and the rest in the second month, these are also split. For instance, layoff checks might be in a different month than the normal pay date. The employee’s accumulations are also updated according to the month paid and are on a cash basis.
