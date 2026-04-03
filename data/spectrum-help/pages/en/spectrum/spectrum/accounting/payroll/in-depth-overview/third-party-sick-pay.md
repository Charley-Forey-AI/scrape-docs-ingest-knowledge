---
title: "Third Party Sick Pay | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/third-party-sick-pay"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/third-party-sick-pay"
---

# Third Party Sick Pay

If third-party sick pay is deemed taxable to the company
 and subject to employer paid FICA, FUTA, and SUTA limits, there are two options to record this
 information.
There may be state, county or local tax rules that will modify this procedure. Please consult with your outside CPA before continuing.
Pen and Paper Adjustment: Determine the amount of employer paid FICA,
 FUTA, and SUTA and make a manual journal entry to record these additional payroll taxes.
 Make manual adjustments to your payroll reports as needed each quarter.
Note: The Quarterly Federal Tax Report (941) would show an adjustment for "third
 party sick pay" in the amount of the employer FICA liability. This is the recommended
 method.
Enter Manual Checks into Spectrum: In this option, manual checks will
 be entered in to record the tax liabilities. The following steps outline this
 process.

1. On the Site Map
 screen, click Payroll > Maintenance > Worker's Compensation. Set up a third party sick pay worker's compensation code for any
 state involved in third party sick pay.Note: This does not
 include sick pay in the worker's compensation calculation; the tax rate for
 this workers' compensation code would be zero.

1. On the Site Map
 screen, click Payroll > Maintenance > Department Expense. Set up a third party sick pay department.

1. Navigate to Payroll > Maintenance > Tax Table Maintenance and enter the applicable state tax code, for example, WA.
 Click the Pay Type
 Exclusions tab and locate the SA pay type line (5th from the
 bottom). Select the appropriate Exempt checkboxes on this line.Note: If you
 are already using the SA pay type for another purpose, please use the 1, 2 or 3
 pay type instead.

1. If using Cash Management, in the Maintenance > Account Code File
 Maintenance screen, you can set up a bank account coded to the clearing account
 used in the third party sick pay department. If you do NOT have Cash Management,
 click System Administration > Installation > Payrollto open the Payroll
 Installation screen and change the cash G/L account code to the
 clearing account used in the Third Party Sick Pay payroll department.

1. Set up a separate pay cycle to record third party sick pay checks using the applicable period end and check dates. In the second part of this screen, enter No at the end of each deduction code line so that they will not calculate for this pay cycle. Enter Manual Check time cards for only third party sick pay in this pay cycle using the SA pay type, the third party sick pay department and entering the gross amount of the pay. If the employee belongs to a union, open the Wage field window and remove the union code.

1. Calculate the pay cycle.

1. Review the Wage and Tax
 Listing to verify that only employee paid FICA, FUTA, and SUTA have
 been accrued. All employee paid withholding must be zero. Use Check Adjustment Entry to
 correct any employer paid witholdings and deductions.

1. Continue the pay cycle as normally done through the Payroll.

1. Return to the Payroll
 Installation screen to change the cash account back to the cash G/L
 account code.

1. A journal entry will be necessary to move the total of the employer's FICA
 amount to the clearing account. An alternative to this entry is to change the
 employer FICA G/L account code in Income Tax File
 Maintenance, and then change it back after this payroll cycle is
 updated.

1. Change the Cash in bank G/L
 account code field in the Payroll
 Installation screen to the correct cash account G/L code.
