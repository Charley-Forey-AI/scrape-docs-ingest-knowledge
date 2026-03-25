---
title: "Set Deductions as Subject to Arrears | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/set-deductions-as-subject-to-arrears"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/set-deductions-as-subject-to-arrears"
---

# Set Deductions as Subject to Arrears

In order for the arrears process to calculate on the proper deductions, you must set them as subject to arrears using the Arrears/Payback tab in the PR Deductions/Liabilities form.
In order to set a deduction as subject to arrears, the
 following must be true for the deduction (in PR Deductions/Liabilities):

- Calculation Category = E-Employee

- Method = A-Amount

- Rate / Amount #1 = 0.00

-  Rate / Amount #2 = 0.00

 For more information on arrears, see [Employee Arrears (Australia)](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia).
In addition, if you want arrears updated to Accounts Payable, you
 must have selected the Automatic
 Update to Accounts Payable checkbox and specified the appropriate
 Vendor, Pay Type, and Frequency.
Note: The settings on the Arrears/Payback tab can be
 overridden by employee on the PR Employee Dedns/Liabs form. For more
 information, see [Activate Arrears Calculations for Employees](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/activate-arrears-calculations-for-employees).

You can override the arrears settings defined for a deduction (in PR Deductions/Liabilities) by employee in PR Employee Dedns/Liabs. For more information, see [Activate Arrears Calculations for Employees](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/activate-arrears-calculations-for-employees)
For more information on setting up arrears for Australian employees, see [Employee Arrears (Australia)](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia).

1. Select a deduction to set as subject to arrears.Note: Arrears deductions must have a Calculation Category of E-Employee and have a Method of A-Amount. In addition, the Rate/Amount #1 and Rate/Amount #2 fields must always be set to 0.00).

 Arrears deductions must have a Calculation Category of E-Employee and have a Method of A-Amount.

1. Select the Arrears/Payback tab.

1. Select the Subject to Arrears checkbox.The system enables all other fields on the Arrears/Payback tab.

1. To include payback in the update to AP, select theSubject to Arrears checkbox. Include Payback in Auto Update to AP checkbox.When running the PR AP Update, the system automatically creates an AP transaction for arrears associated with this deduction.
The system enables the Include Payback in Auto Update to AP checkbox and all fields in the Reporting Arrears Threshold and Payback Per Pay Period sections.Note: For deductions that already have the Subject to Arrears checkbox selected, you cannot clear it if:

- There are arrears records associated with this deduction code on the PR Arrears/Payback History form.

- There is an existing Life to Date arrears balance for an employee associated with the deduction code in the PR Employee Dedns/Liabs form.

- Payback values for this deduction code exist in an open payroll.

1. To include employee payback amounts with the deduction amount (calculated or override) in the update to AP (PR AP Update), select the Include Payback in Auto Update to AP checkbox. Note: This checkbox is only enabled if you selected both the Automatic Update to Accounts Payable and Subject to Arrears checkboxes for the deduction code. For more information about this field, see the [F1 Help](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#concept-02b58d60-6883-49da-b0bf-bd284f5c3d70--en).

1. In the Reporting Arrears Threshold section, set the reporting threshold for the deduction arrears.

1. Select the option that determines the arrears reporting threshold: Use Threshold Factor or Use Threshold Amount.

1. If you want the arrears threshold to be determined by percentage (factor), enter the percentage amount in the Threshold Factor field.

1. If the arrears threshold is a flat amount, enter the amount in the Threshold Amount field.Note: Arrears thresholds are used for reporting purposes only on the PR Arrears/Payback History report.

- Factor - If you are using a threshold factor, the system multiplies the standard deduction amount by the factor value. When employees reach or exceed this factor value, their name displays on the report.

- If you are using a threshold amount, employees names display on the report when they reach or exceed the threshold amount.

- If the arrears threshold is determined by a percentage,select the Use Threshold Factor option and then enter the percentage in the Threshold Factor field.

- If the arrears threshold is a flat amount, select the Use Threshold Amount option and then enter the amount in the Threshold Amount field.

Note: Arrears thresholds are used for reporting purposes only on the PR Arrears/Payback History report. If you are using a threshold factor, the system multiplies the standard deduction amount by the factor value. When employees reach or exceed this factor value, their name displays on the report.If you are using a flat threshold amount, employees names display on the report when they reach or exceed the specified threshold amount.

1. In the Payback Per Pay Period section, set the payback amount for the arrears deduction.

1. Select to have employees pay a percentage amount per pay period (Use Payback Factor) or a flat amount per pay period (Use Payback Amount).

1. If you want to use a payback factor, enter the percentage amount in the Payback Factor field.

1. If you want to use a flat amount, enter the amount in the Payback Amount field.

- To have employees pay a percentage per pay period, select the Use Payback Factor option and then enter the payback percentage in the Payback Factor field.

- To have employees pay a flat amount per pay period, select the Use Payback Amount option and then enter the amount in the Payback Amount field.

1. Save the record.
