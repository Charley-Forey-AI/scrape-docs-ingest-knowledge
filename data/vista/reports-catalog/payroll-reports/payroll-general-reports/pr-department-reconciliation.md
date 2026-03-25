---
title: "PR Department Reconciliation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/payroll-reports/payroll-general-reports/pr-department-reconciliation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/payroll-reports/payroll-general-reports/pr-department-reconciliation"
---

# PR Department Reconciliation

You can use the PR Department Reconciliation report to
 print payroll information by department (payroll, job cost, equipment, or intercompany
 department) by selecting Payroll > Reports > PR Department Reconciliation.
The PR Department Reconciliation report prints payroll information by
 department (payroll, job cost, equipment, or intercompany department). The report breaks
 out earnings between regular and fixed and considers liability rates. Add-on earnings
 are included in the actual earnings. The JC departments use the fixed earnings unless
 the fixed rate is zero in PREH then it will use actual earnings. The JC Department
 liabilities are based on the Method, Liability Rate and Earnings Codes in the JC
 liability template currently assigned to each job. The EM departments use the fixed
 earnings unless the fixed rate is zero in PREH then it will use actual earnings. The EM
 Department liabilities are based on the Burden Type, Burden Rate and Markup Rate in EM
 Company parameters. Intercompany shows the dollars associated with earnings that posted
 to a different GL company but not to a job. The report is run for a single pay period
 end date and PR group. The report prints the payroll department information first, then
 the job/equipment/intercompany cost information. Payroll must be processed before the
 report is run to pull the correct earnings and liabilities.
This report is based on current settings, fixed rates, and liability
 rates and therefore should be run at the time of the payroll. It will only be valid on
 previous payrolls if no changes to Liability templates or fixed rates have been
 made.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

PR Group (Required)
Select the Field Lookup button or press F4 to select the PR group, or leave blank for all.

PR End Date
Click the Field
 Lookup button or press F4 to select
 the pay period end date.
