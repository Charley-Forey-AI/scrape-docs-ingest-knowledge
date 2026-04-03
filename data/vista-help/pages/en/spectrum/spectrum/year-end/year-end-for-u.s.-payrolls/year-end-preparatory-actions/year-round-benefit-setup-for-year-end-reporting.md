---
title: "Year Round Benefit Setup for Year-End Reporting | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/year-end-preparatory-actions/year-round-benefit-setup-for-year-end-reporting"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/year-end-preparatory-actions/year-round-benefit-setup-for-year-end-reporting"
---

# Year Round Benefit Setup for Year-End Reporting

The various employee benefits provided to employees throughout the year need to be included in year-end reporting in state, local, and federal jurisdictions. This section looks at common ways that Spectrum is configured to help you track, maintain, and report these benefits.
Please contact your accountant for information regarding your company's specific reporting responsibility.
The example benefits we will use to illustrate benefit accrual methods are:

- employee health care benefits

- personal use of company vehicles

- life insurance in excess of $50,000

There are various methods for accurately accruing these benefits all year for accurate reporting at year-end:

- (Recommended) During the course of the year, use Add-on and Deduction codes to record the benefit paid to the employee. The add-on code expenses the employer payment of the benefit and accrues its liability (if the benefit is taxable, the add-on would be set for taxability). The deduction code reduces the pay of the employee for their allotted portion of the benefit (if the employee portion is deducted pre-tax, the deduction code is set accordingly).

- Use a pay type. Choose between these two options:

- If using pay type 1, 2, or 3, set these up in System Administration > Installation > Payroll.

- If using an add-on code used as a pay type, set this up in Payroll > Maintenance > Add-on/Deduction.

- In either case and specifically for the benefit, do both the following:

- Set up a department expense code in Payroll > Maintenance > Department Expense.

- Set up a deduction code in Payroll > Maintenance > Add-on/Deduction.

- (Not recommended) During the course of year-end processing, manually adjust employee W-2s to reflect benefits, and then manually modify the relevant tax reports and GL accounts. This method will under-state income paid out to the employee over the year, and your year-end reports will not tie to the W-2.

## Reporting Employee Health Care Benefits on Form W-2

Employers must display the cost of health care paid by the employer and the employee on the W-2 form in Box 12, using code 'DD'.

## Add-on and Deduction code setup to record Non-Cash Benefits

Step 1: Create Code to Track Employer Portion of Health Care
Create an add-on to record the cost of employer-paid health care benefits.
Properties Tab

1. Set the Type to Add-on.

1. Calculation method depends on whether the benefit is a fixed amount or a rate per hour.

1. Enter the benefit expense G/L account code. This is the debit side of the transaction. In our example, we would set this as an indirect GL account code.

1. Select the Clear employee balance at year end checkbox.

Tax Effects Tab
Employees are not taxed on health care benefits, so nothing would be entered on the tax effects tab.
Note: Other benefits may result in increasing the employee tax obligation, and in those cases, the taxability would be set on this screen.
Add-ons Tab

1. (Optional) Set the direct cost flag to non-direct cost.

1. Clear the Paid to employee on paycheck checkbox, since this is a non-cash benefit.

1. (Optional) Clear the Print on paycheck checkbox.

1. Enter the benefit liability account code in the 'Non-cash G/L account' field. This is the credit side of the transaction.

Step 2: Create Code to Track Employee Portion of Health Care
Create a deduction code to deduct the cost of the employee's portion of health care.
Properties Tab

1. Set the Type to Deduction.

1. Calculation method depends on whether the benefit is a fixed amount or a rate per hour.

1. Enter the employee liability G/L account code on the Properties tab. This is the debit side of the transaction.

1. Select the Clear employee balance at year end checkbox.

Tax Effects Tab
Since employee health contributions are usually collected pre-tax, the income tax and FICA boxes would be selected for the US tax jurisdiction.Important: Consult with your tax advisor for your specific situation.

Step 3: Enter Codes on Employee Recurring Deduction/Add-on Maintenance
The last step is to set up the add-on and deduction codes on the employee. Go to Payroll > Maintenance > Recurring Deduction/Add-on > Recurring Deduction/Add-on Maintenance. In this manner, these amounts will accrue automatically during each pay cycle.
Tip: If the add-on code was not set up at the beginning of the year, use the Adjust Non-Cash Add-on Balances screen to bring the YTD amounts up to date. When you perform the Build W-2s process, enter both add-on and deduction codes into Box 12, code 'DD'. The system automatically sums these amounts together.

## Personal Use of Company Vehicles

If your company provides personal use of company-owned vehicles as an employee benefit, it may be necessary to include an amount in the employee's year-to-date earnings to reflect taxable income for personal use of company vehicles.

## Life Insurance in Excess of $50,000

If your company provides life insurance as an employee benefit, it may be necessary to include an amount in the employee's year-to-date earnings to reflect taxable income for life insurance in excess of $50,000. This amount must also be included in box 12 of the W-2, code C.
The IRS publishes a table detailing the amount of earnings to be applied.
Payroll Installation Screen pay type

1. Navigate to Payroll > Maintenance > Deduction/Add-on Code, and select New to add a new Add-on Code.

1. In the Properties tab:

- enter a fixed amount Calculation method,

- enter a non-direct expense GL account, and

- select the Clear employee balance at year end checkbox.

1. In the Tax Effects tab, enter all the tax codes for US, state, county, and local.

1. In the Add-ons tab:

- clear the Pay the employee on the paycheck checkbox,

- select the Print on paycheck checkbox, and

- enter the same GL account in the Non-cash GL account field as you did in the Properties tab.

Note: These lines should be added to the last regular paycheck.

## Adjusting W-2 Forms Prior to Printing

Once you process a payroll for the next/new year, it is too late to add additional earnings to the previous year payroll reports. However, you can make adjustments to the W-2 forms prior to printing.
The following process adjusts only the W-2 forms being produced. It doesn't affect employee earnings or update the quarterly or yearly payroll reports.
The life insurance may be recorded directly into the employee's W-2 record. Use the W-2 Form Maintenance screen to adjust the employee's W-2 wage and tax statement. Consult with your accountant for specific instructions on which figures to adjust:

- Wages tips and other compensation (box 1)

- Federal income tax withheld (box 2)

- Social Security wages (box 3)

- Social Security tax withheld (box 4)

- Medicare wages (box 5)

- Medicare tax withheld (box 6)

- State/local information (boxes 15-20)

Entry in this screen is reflected only on the W-2 paper and electronic filing reports. This procedure does not result in any changes to the Payroll period end reports, nor does it change recognition of expense in the General Ledger for employer FICA. Be sure to manually adjust your Quarterly Federal Tax Report and other fourth-quarter tax filings if necessary.
Please contact your accountant for information regarding your company's specific reporting responsibility.
