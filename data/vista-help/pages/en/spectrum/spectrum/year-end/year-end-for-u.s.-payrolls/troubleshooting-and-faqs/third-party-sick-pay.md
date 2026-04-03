---
title: "Third-Party Sick Pay | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/troubleshooting-and-faqs/third-party-sick-pay"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/troubleshooting-and-faqs/third-party-sick-pay"
---

# Third-Party Sick Pay

If third-party sick pay is deemed taxable to the company and subject to employer paid FICA, FUTA, and SUTA limits, there are two options to record this information.Note: There may be state, county, or local tax rules that should prompt modifications to this procedure. Please consult with your CPA before continuing.

## Pen and Paper Adjustment

Determine the amount of employer paid FICA, FUTA, and SUTA and make a manual journal entry to record these additional payroll taxes. Make manual adjustments to your payroll reports as needed each quarter.Note: The Quarterly Federal Tax Report (941) would show an adjustment for "third-party sick pay" in the amount of the employer FICA liability. This is the recommended method.

## Enter Manual Checks into Spectrum

Use payroll checks to record the tax liabilities:

1. Select Payroll > Maintenance > Worker's Compensation.

1. Set up a third-party sick pay worker's compensation code for any state involved in third-party sick pay.Note: This does not include sick pay in the workers' compensation calculation; the tax rate for this workers' compensation code would be zero.

1. Select Payroll > Maintenance > Department Expense.

1. Set up a third-party sick pay department.

1. Select System Administration > Installation > Payroll, select the G/L Codes tab and change the cash G/L account code to the clearing account used in the Third-Party Sick Pay payroll department.

1. If Cash Management module is present, on the System Administration > Installation > Cash Management screen, select Bank Accounts and deselect the option to post payroll transactions.

1. Set up a separate pay cycle to record third-party sick pay checks using the applicable period end and check dates. Make sure the Automatic cycle and accrue hourly banks are cleared, select Turn off auto deposit payments.

1. Select the Suppress all in the Recurring deductions and add-ons checkbox.

1. Enter Manual Check time cards for only third-party sick pay in this pay cycle using the 'SA' pay type, the Third-Party Sick Pay Department and entering the gross amount of the pay. If the employee belongs to a union, remove the wage code and union from the time card file.Note: If you are already using the SA pay type for another purpose, please use the Other 1, 2, or 3 pay type instead. To see the Description setup for these, go to System Administration > Installation > Payroll > Properties tab.

1. Calculate the pay cycle.

1. Use Check Adjustment Entry to zero out employee-paid withholdings and deductions and select Save.

1. Return to Calculation Reports and review the State Wage and Tax Listing to verify that only employer-paid FICA, FUTA, SUTA, and other local taxes that are subject to sick leave have been accrued and that all employee-paid withholding is zero. Archive reports for your records.

1. Update the pay cycle as you normally would.

1. Return to the Payroll Installation screen to change the cash account back to the cash G/L account code.

1. Turn the Cash Management module back on (if you turned it off in step 6).

1. Enter a journal entry to move the total of the employers' FICA amount to the clearing account. An alternative to this entry is to change the employer FICA G/L account code in Tax Table File Maintenance, and then change it back after this payroll cycle is updated.

## How do I produce a separate W-2 for third-party sick pay?

Important: The IRS doesn't require a separate W-2 for third-party sick pay. It is optional.
You can use the existing W-2 to report the third-party sick pay by editing the existing W-2 for this employee in the W-2 Form Maintenance screen and adding the amounts to the appropriate boxes to report the third-party sick pay.
If you want to create a new W-2 for third-party sick pay, note that it will be vital to follow the instructions below to ensure the extra W-2 will be included on the W-2 electronic filing for the SSA:

1. Add the additional W-2 to report third-part sick pay separately from regular wages in the W-2 Form Maintenance screen with an employee code that *is different from the existing Spectrum employee code*.

1. Leave the Form ID field blank.

1. Continue entering amounts in the applicable boxes of the W-2 to report the third-party sick pay. By using a different employee code, the blank Form ID field will allow this extra W-2 to be written to the W2REPORT file, which is created when you select the Electronic button.
