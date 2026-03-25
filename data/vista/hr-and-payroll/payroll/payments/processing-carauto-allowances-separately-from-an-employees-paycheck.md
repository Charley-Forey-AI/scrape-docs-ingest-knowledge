---
title: "Processing Car/Auto Allowances Separately from an Employee's Paycheck | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/processing-carauto-allowances-separately-from-an-employees-paycheck"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/processing-carauto-allowances-separately-from-an-employees-paycheck"
---

# Processing Car/Auto Allowances Separately from an Employee's Paycheck

The following instructions are for setting up a car/auto
 allowance where the earnings need to be reported on the employee’s W-2’s, no Federal or
 State taxes will be withheld, and the Employee’s FICA tax obligation will be paid by the
 Employer.
Note: Before setting up the car/auto allowance, determine how
 this allowance will affect your GL. Determine what earnings type to assign to the
 earnings code, and verify that the earnings type you have assigned appears in the PR
 Departments and/or JC Departments with the proper GL accounts. Additionally, an
 appropriate GL account will need to be assigned to the deduction code.

1. In PR Earnings Codes, create an earnings code for the car/auto allowance. Select A-Amount from the Method drop-down and enter 1.00 in the Factor field. Enter the appropriate earnings type (this controls what GL account the system uses for the earnings).

1. On the Dedns/Liabs tab, add the deduction codes for all taxes that these earnings are "subject to." Generally, this would include Federal withholding, FICA, and State withholding taxes. You must also determine if additional deductions and/or liabilities are required.

1. Check the Subject Only box on those taxes that will not be withheld at this time for the car/auto allowance earnings. Often, the Federal and State taxes will not be deducted. This indicates the car/auto allowance earnings are taxable for W-2 purposes, but the taxes will not be withheld. Note: To properly calculate the FICA liability, you should not check the Subject Only box for the FICA deductions.

1. Set up a new garnishment group in PR Garnishment Group for the car/auto allowance. Add the deduction codes for FICA and the earnings code for the car/auto allowance (set up in step 1) on the Deductions/Earnings tab.

1. In PR
 Deductions/Liabilities, set up a deduction code for a reversal of the car/auto
 allowance. Enter a GL account in the GL Account field and select
 N-Rate of net from the Method drop-down. In the
 Garnishment Group field, enter the garnishment group set up in
 step 2. Enter a rate of 1.00in the Rate/Amount
 #1 and Rate/Amount #2 fields. Select
 the No
 Limitoption from the Limit section of the form. Add the earnings
 code from step 1 to the Basis Codes tab.

1. In PR Employees, add the new deduction code created in step 4 to the employee on the Dedns/Liabs tab. Check the Employee-Based box and enter the appropriate frequency code in the Frequency field (this will be used to tell the system during payroll processing that these earnings should be included). Since this deduction will be based on net pay, it should be the last item calculated. Select Override Standard Rate/Amount from the Calculations drop-down and enter a rate of 1.0 in the Rate/Amount field.

1. In PR Pay Period Control, set up a new sequence that is separate from the usual payroll run. Be sure to include the frequency code assigned to the car/auto allowance deduction in step 5 to the Active Frequency Codes tab.

1. In PR Timecard Entry create a new batch with the new sequence from step 5. Enter an employee timecard using the car/auto allowance earnings code created in step 1 with the amount for car/auto allowance. Then select File  Batch Processand post the timecard batch.

1. In PR Payroll Process, select the Employees With Changed Earnings or Overrides option, from the Processing Options section of the form, and process this pay period and payment sequence.

1. In PR Employee Pay Seq
 Control, find each employee with the car/auto allowance and select X-No
 Pay from the Payment Method drop-down.
 Update the Paid Date and Paid
 Month fields and click Process to process the
 employee.

1. Finish standard processing and closing procedures for this sequence.

Related information

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

- [PR Garnishment Groups Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-garnishment-groups-form)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [PR Pay Period Control Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-pay-period-control-form)

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [About the PR Payroll Process Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-the-pr-payroll-process-form)

- [About the PR Employee Pay Sequence Control Form](/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-employee-pay-sequence-control-form)
