---
title: "Field Definitions: PR Employee Accums Detail Form (AU) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accums-detail-form-au/field-definitions-pr-employee-accums-detail-form-au"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accums-detail-form-au/field-definitions-pr-employee-accums-detail-form-au"
---

# Field Definitions: PR Employee Accums Detail Form (AU)

(Australia) The following is a list of field descriptions for the PR Employee Accums Detail form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Employee

(Australia) The Employee field on the PR Employee Accums Detail form.
This field defaults the current employee (that is, the employee you selected in PR Employee Accumulations).
Accept the default or enter the employee for whom to add or edit detail records. Press F4 to select from a list of valid employees; that is, employees who have records in PR Employee Accumulations.
Note: You can only add detail records for an employee/month/type/EDL code that exists in PR Employee Accumulations. If you need to add detail records for a new employee/month/type/EDL code, you must add the employee/month/type/EDL code record in PR Employee Accumulations before adding detail records here.

## Month

(Australia) The Month field on the PR Employee Accums Detail form.

This field defaults the current month (that is, the month on the record you selected in PR Employee Accumulations).
Accept the default or enter a calendar month for which there are existing records in PR Employee Accumulations for the selected employee.
All amounts are based on the payment month.
Note: You can only add detail records for an employee/month/type/EDL code that exists in PR Employee Accumulations. If you need to add detail records for a new employee/month/type/EDL code, you must add the employee/month/type/EDL code record in PR Employee Accumulations before adding detail records here.

## Type

(Australia) The Type drop-down on the PR Employee Accums Detail form.
This field defaults the current EDL type (that is, the type on the record you selected in PR Employee Accumulations).
Accept the default or press F4 to select an EDL type for which there are existing records for the selected employee and month combination in PR Employee Accumulations.

Types include: E-Earnings, D-Deduction, or L-Liability.
Note: You can only add detail records for an employee/month/type/EDL code that exists in PR Employee Accumulations. If you need to add detail records for a new employee/month/type/EDL code, you must add the employee/month/type/EDL code record in PR Employee Accumulations before adding detail records here.

## EDL Code

(Australia) The EDL Code field on the PR Employee Accums Detail form.
This field defaults the current EDL code (that is, the code on the record you selected in PR Employee Accumulations).
Accept the default or press F4 to select from a list of valid EDL codes for the specified employee, month, and EDL type combination in PR Employee Accumulations.
Note: You can only add detail records for an employee/month/type/EDL code that exists in PR Employee Accumulations. If you need to add detail records for a new employee/month/type/EDL code, you must add the employee/month/type/EDL code record in PR Employee Accumulations before adding detail records here.

## Record ID

(Australia) The Record ID field on the PR Employee Accums Detail form.
To add a new detail record, you can either double-click in this field or enter +; the system automatically assigns the next sequence number.
Note: You can only add detail records for an employee/month/type/EDL code that exists in PR Employee Accumulations. If you need to add detail records for a new employee/month/type/EDL code, you must add the employee/month/type/EDL code record in PR Employee Accumulations before adding detail records here.

## Income Stream Type

(Australia) The Income Stream Type field on the PR Employee Accums Detail form.
Defaults from the PAYG Income Type field in PR Employees (Info tab, Income Stream section).
Accept the default for this record or enter a different income stream type.

- WHM - Working holiday maker (selecting this option requires entry of an Income Stream Country)

- SAW - Salary and wages (selecting this option requires that the Income Stream Country be blank)

## Income Stream Country

(Australia) The Income Stream Country field on the PR Employee Accums Detail form.
This field is enabled and required if the Income Stream Type is WHM (Working holiday maker).
Defaults the income stream country specified for the employee in the Country Code field on the PR Employees form.
Accept the default or enter the two-letter code representing the home country of the working holiday maker. This will be the alpha-2 code defined for the country in ISO 3166-1 (cannot be AU, CC, CX, HM, or NF). Press F4 for a list of valid country codes.
Note: You will typically only change the defaulted country code for a new detail record if you are correcting the country code for an existing detail record, since edits to the country code for existing records are not allowed. In which case, once you finish entering the new detail record, you would then delete the incorrect detail record.

## Hours

The Hours field on the PR Employee Accums Detail form.
This field is available if Type is set to E-Earnings or L-Liability.

Enter the month-to-date hours for this record. These hours will be included in the total hours for the employee/month/type/EDL code in PR Employee Accumulations.
The amount entered in this field will be included in the total Subject Amount for the employee/month/type/EDL record in PR Employee Accumulations.

## Subject Amount

(Australia) The Subject Amount field on the PR Employee Accums Detail form.
This field is available if Type is set to D-Deductions or L-Liabilities.
Enter the month-to-date subject amount for this record. Subject amounts include all earnings subject to the liability or deduction, including amounts not included in the calculation basis. (e.g. earnings flagged as subject only and earnings exceeding the subject limit).

## Eligible Amount

(Australia) The Eligible Amount field on the PR Employee Accums Detail form.
This field is available if Type is set to D-Deductions or L-Liability.
Enter the month-to-date eligible amount for this liability or deduction code.
Eligible amounts include those earnings used in the calculation basis for the deduction or liability amount. If a limit is specified for the deduction or liability (PR Deductions/Liabilities), this amount will be 0.00 once the limit is reached. If no limit is specified, the subject amount and eligible amount will always be the same.
If you are loading balance forwards, the following example shows how subject and eligible amounts should be entered for an employee who has gone over the limit and an employee who has not met the limit.
The following table shows two examples of eligible amounts if the limit is $20,000.EmployeeYTDSubject AmountEligible Amount
100$50,000$50,000$20,000
200$15,000$15,000$15,000

The amount entered in this field will be included in the total Eligible Amount for the employee/month/type/EDL record in PR Employee Accumulations.

## Amount

(Australia) The Amount field on the PR Employee Accums Detail form.
Enter values as follows. When the Type field is set to:

- E-Earnings — Enter or edit the month-to-date amount for this earnings code.

-  D-Deductions — If the deduction code entered for this line has a method of Rate of Gross, the amount is calculated based on the Rate specified in PR Deductions/Liabilities. Otherwise, enter or edit the month-to-date amount for this deduction code.

- L-Liabilities — If the liability code entered for this line has a method of Rate of Gross, an amount is calculated based on the Rate specified in PR Deductions/Liabilities. Otherwise, enter or edit the month-to-date amount for this liability code.

The amount specified here will be included in the total Amount for the employee/month/type/EDL code record in PR Employee Accumulations.
