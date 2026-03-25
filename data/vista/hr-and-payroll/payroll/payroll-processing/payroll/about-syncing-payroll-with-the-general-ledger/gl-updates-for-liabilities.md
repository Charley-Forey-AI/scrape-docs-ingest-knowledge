---
title: "GL Updates for Liabilities | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-with-the-general-ledger/gl-updates-for-liabilities"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-syncing-payroll-with-the-general-ledger/gl-updates-for-liabilities"
---

# GL Updates for Liabilities

All payroll liabilities are debited to the accounts set up by
 liability type in the PR Departments.

If the timecard entries are not posted to a job, are
 not mechanics’ timecards, and/or the Use JC or EM Department or Payroll options are
 not chosen, the accounts in the PR Departments will be the only ones used. Each
 liability code is set up in PR Deductions/Liabilities with a liability type, and the
 liability types are assigned GL codes in the PR Departments.
Additional GL entries for liabilities will be made if the JC or EM Department for Payroll options are used. If you are using the “exact” method for charging Job Cost, or the “actual” method for charging EM (on mechanics), the setup may make it seem the PR Department was not used. The entries made are as follows:
Debit
Credit

Liability Type (PR Department)
GL Account (PR Deductions/Liabilities)

Cost Type (JC or EM Department) with overrides by Liability Type or Cost Code
JC/EM Applied Burden (PR Department)

If you are using the “exact” method for costing and
 you use the same GL account for the Liability Type and the Applied Burden accounts
 in the PR Departments (1 & 4 above), these will offset each other with equal
 amounts and will not in fact make an entry to the General Ledger.
If you are using a percentage rate for costing and the same accounts are used, the difference between actual and the rate will be charged to the account. If using separate accounts, all four entries will be made.
