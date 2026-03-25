---
title: "Processing Car/Auto Allowances with an Employee's Paycheck | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/processing-carauto-allowances-with-an-employees-paycheck"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/processing-carauto-allowances-with-an-employees-paycheck"
---

# Processing Car/Auto Allowances with an Employee's Paycheck

The following instructions detail how to set up car/auto
 allowance earnings where taxes will be deducted from the employee’s current paycheck.

At a minimum, the FICA portion of the car/auto allowance earnings will be withheld, but other taxes can also be withheld at this time. The car/auto allowance earnings will be reported on the employee’s W-2, as will any taxes deducted from the employee’s current paycheck.
Note: Before setting up the car/auto allowance, determine how this
 allowance will affect your GL. Determine what earnings type to assign to the
 earnings code, and verify that the earnings type you have assigned appears in the PR
 Departments and/or JC Departments with the proper GL Accounts. Additionally, an
 appropriate GL Account will need to be assigned to the Deduction Code.

1. In PR Earnings Codes, create an earnings code for the car/auto allowance. Select A-Amount from the Method drop-down and enter 1.00 in the Factor field. Enter the appropriate earnings type (this controls what GL account the system uses for the earnings).

1. On the Dedns/Liabs tab, add the deduction codes for all taxes that these earnings are "subject to." Generally, this would include Federal withholding, FICA, and State withholding taxes. You will also need to add the FICA liability codes. You must also determine if additional deductions and/or liabilities are required.

1. Check the Subject Only box for those deductions/liabilities that will not be withheld at this time for the car/auto allowance earnings. Often, the Federal and State taxes will not be deducted. This indicates the car/auto allowance earnings are taxable for W-2 purposes, but the taxes will not be withheld. Note: To properly calculate the FICA liability, you should not check the Subject Only box for the FICA deductions.

1. In PR Deductions/Liabilities, set up a deduction code for a reversal of the car/auto allowance. Enter the GL account in the GL Account field and select G-Rate of Gross from the Method drop-down. Enter a rate of 1.00 in the Rate/Amount #1 and Rate/Amount #2 fields. Select the No Limit option from the Limit section of the form. Add the car/auto allowance earnings code from step 1 to the Basis Codes tab.

1. In PR Employees, add the new deduction code created in step 2 to the employee on the Dedns/Liabs tab. Check the Employee Based box and enter the appropriate frequency code in the Frequency field (this will be used to tell the system during payroll processing that these earnings should be included). The Processing Seq# field can be left blank. Select Override standard Rate/Amount from the Calculations drop-down and enter a rate of 1.0 in the Rate/Amount field.

1. For those pay periods where the car/auto allowance earnings will be added to the employee’s paycheck, add the frequency code assigned to the car/auto allowance deduction (in Step 3) to the Active Frequency Codes tab in PR Pay Period Control.

1. In PR Timecard Entry, post the car/auto allowance earnings by entering an employee timecard line using the earnings code created in Step 1 with the amount for the car/auto allowance. Post the remaining regular time card entries for the employee.

1. Continue [processing your payroll](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll) as you would normally. Verify the car/auto allowance is correct prior to printing checks. You will see the allowance amount appear in both earnings and deductions.

Related information

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [PR Pay Period Control Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-pay-period-control-form)

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)
