---
title: "Set up Paid Family/Medical Leave for Washington State | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-paid-familymedical-leave-for-washington-state"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-paid-familymedical-leave-for-washington-state"
---

# Set up Paid Family/Medical Leave for Washington State

Set up Washington Paid Family / Medical Leave in Vista to enable creating and submitting paid family/medical leave reports.
 As of January 1, 2019, if you are an employer in the State of Washington you must withhold Paid Family Leave and Medical premiums from your employees' wages.The following steps detail how to set up the necessary deduction (employee) and liability (employer) codes for paid family leave for Washington State. You can set up paid family and medical leave as employee-based or state-based. Each of these methods is provided below.

1. From the main menu, select Payroll > Programs > PR Deductions/Liabilites.

1. If the unemployment state for employees is always the same as the resident state, set up state-based paid family leave deduction/liability codes as follows. Otherwise, see Step 3.

1. Set up the deduction and liability codes as follows:FieldTabDeduction CodeLiability Code
TypeInfoDeductionLiability
Calculation CategoryInfoS-StateS-State
MethodInfoG-Rate of GrossG-Rate of Gross
Rate/Amount #1Info0.002530.00147
Rate/Amount #2Info0.002530.00147
Limit TypeInfoSubject AmountSubject Amount
Limit AmountInfo132,900.00132,900.00
Limit AppliedInfoA-AnnuallyA-Annually
Aatrix Tax TypeAddl Info1161 (Paid Family Leave)1162 (Paid Family Leave - Employer)

1. Save the record.

1. From the main menu, select Payroll > Programs > PR State Information.

1. In the State field, enter WA or press F4 to select WA from the list of states

1. Click on the Add'l State Based Dedn/Liabs tab

1. In the grid, add both the deduction code and the liability code that you just created in PR Deductions/Liabilities.

1. For each of the codes, set the BasedOn field to U-Unemployment State.

1. Save the record.

1. If the unemployment state differs from the resident state (that is, follows the job state), set up employee-based paid family leave deduction/liability codes as follows.

1. Set up the deduction and liability codes as follows:FieldTabDeduction CodeLiability Code
TypeInfoDeductionLiability
Calculation CategoryInfoE-EmployeeE-Employee
MethodInfoG-Rate of GrossG-Rate of Gross
Rate/Amount #1Info0.002530.00147
Rate/Amount #2Info0.002530.00147
Limit TypeInfoSubject AmountSubject Amount
Limit AmountInfo132,900.00132,900.00
Limit AppliedInfoA-AnnuallyA-Annually
Aatrix Tax TypeAddl Info1161 (Paid Family Leave)1162 (Paid Family Leave - Employer)

1. Save the record.

1. From the main menu, select Payroll > Programs > PR Employee Dedns/Liabs.

1. For each Washington state employee, add entries for the employee-based paid family leave deduction and liability codes you created in PR Deductions/Liabilities.

1. For both codes, select the Employee-Based check box.

1. For both codes, set the Frequency field based on your standard pay period setup.

1. For both codes, set the Processing Seq # field to 1.

1. For both codes, set the Calculations method to Use Calculated Amount. Do not specify a calculation override.

1. Save the record.

 You are now set up to deduct WA Paid Family Leave premiums when processing applicable employees.For information about using Aatrix for WA Family Leave reporting, see [Create / Submit WA State Paid Family / Medical Leave Reports Using Aatrix](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aatrix-reporting/create--submit-wa-state-paid-family--medical-leave-reports-using-aatrix).

Related concepts

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [PR State Information Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-state-information-form)
