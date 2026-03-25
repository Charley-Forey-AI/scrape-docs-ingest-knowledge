---
title: "Activate Arrears Calculations for Employees | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/activate-arrears-calculations-for-employees"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/activate-arrears-calculations-for-employees"
---

# Activate Arrears Calculations for Employees

Activate arrears so that the system tracks arrears for the employee when they do not have a timecard record in the current pay period.
Set any applicable deduction codes as subject to arrears. If needed, see [Set Deductions as Subject to Arrears](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/set-deductions-as-subject-to-arrears).
There are two steps to activate arrears calculations for employees:

- set deductions associated with the employee as eligible for arrears in the PR Employee Dedns/Liabs form

- activate each applicable employee record for arrears in the PR Employees form.

Once you have done both steps, the system tracks arrears for the employee when they do not have a timecard record in the current pay period. The only times you may want to adjust these settings is if the employee is taking unpaid leave (for example, FMLA) or is being terminated.
When you activate arrears calculations for an employee, the system uses the default arrears reporting threshold and payback amounts for the deduction code that are set in the PR Deductions/Liabilities form. You can choose to override those default settings in PR Employee Dedns/Liabs form.
The following information details how to activate arrears calculations for employees, as well as how to override default arrears reporting threshold and payback default settings per employee

1. In the PR Employee Dedns/Liabs form, locate the employee and the relevant deduction code.

1. Select the Arrears/Payback tab.

1. Select the Eligible for Arrears checkbox.Note: The Eligible for Arrears checkbox is only enabled when the associated deduction code has been set as subject for arrears. If needed, see [Setting Deductions as Subject to Arrears](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/set-deductions-as-subject-to-arrears).

The system enables the fields in the Reporting Arrears Threshold and Payback Per Pay Period sections.

1. Override the Reporting Arrears Threshold information, as necessary.

1. Select the Override Standard Deduction Arrears Threshold checkbox.

1. Select the option that determines the arrears reporting threshold override: Use Threshold Factor or Use Threshold Amount.

1. If you want the arrears threshold override to be determined by percentage (factor), enter the percentage amount in the Threshold Factor field.

1. If the arrears threshold override is a flat amount, enter the amount in the Threshold Amount field. Note: Arrears thresholds are used for reporting purposes only. If you are using a threshold factor, the system multiplies the standard deduction amount by the factor value. When employees reach or exceed this factor value, they will display on the PR Arrears/Payback History report.

1. Override the Payback Per Pay Period information, as necessary.

1. Select the Override Standard Deduction Payback Settings checkbox.

1. Select the option to have employees pay a percentage amount per pay period (Use Payback Factor) or a flat amount per pay period (Use Payback Amount).

1. If you want to use a payback factor, enter the percentage amount in the Payback Factor field.

1. If you want to use a flat amount, enter the amount in the Payback Amount field.

1. Save the record.

1. In the PR Employees form, select the Active for Arrears checkbox and save the record. The system will process arrears for the employee when timecard records do not exist in the current pay period.
