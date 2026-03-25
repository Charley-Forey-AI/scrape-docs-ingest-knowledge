---
title: "Payroll Interface to General Ledger | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/payroll-interface-to-general-ledger"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/payroll-interface-to-general-ledger"
---

# Payroll Interface to General Ledger

Both PR and JC have department files that define GL accounts.

Payroll departments are used to define the GL accounts for all earnings, including those charged to jobs and equipment. Job Cost departments are used to define the GL accounts for earnings that are job-costed. When timecards are entered, all earnings are posted to the GL accounts for payroll department specified on the timecard. Additional entries will be posted to the JC department accounts for earnings that are charged to jobs.

- Earnings - All earnings use the Payroll department and make GL distributions to
 earnings expense by earnings type. If earnings are job-costed, the Payroll
 department expense is offset to a JC Applied Earnings account, then expensed in
 the Job Cost department by earnings type, phase, or cost type.

- Liabilities - Burden costs also use the Payroll department,
 and make GL distributions to a burden expense by liability type. If the
 liability is associated with earnings that are job costed, the Payroll
 department expense is offset to a JC Applied Burden account, then expensed in
 the Job Cost department by liability type, phase, or cost type. The actual
 amount of liability calculated is always credited to the account set up in PR
 Deductions/Liabilities. The amount that is added to Job Cost is always debited
 to the account pulled from the JC Departments file. If you choose to calculate a
 liability on a percentage basis for Job Cost purposes, these amounts will not be
 the same. In that case, the actual amounts are debited to the Employee’s
 department account for the liability type. The percentage going to Job Cost is
 debited to the Job Cost department account and credited to the contra account,
 which is the JC Applied Burden GL Account set up in the Employee’s department.

- Fixed Rate - If using the fixed rate for some employees,
 their actual wages and liabilities will be debited to the accounts in their
 department setup (PR Departments). The value of wages when using a fixed rate
 override will be debited to the GL account for the cost type in the JC
 department file and credited to the JC Fixed Rate GL Account in the PR
 Departments for their department.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-departments-form)JC
 Departments
[](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-departments-form)PR
 Departments
