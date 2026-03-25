---
title: "Field Definitions: PR Employee Accums Detail Form (CA) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accums-detail-form-ca/field-definitions-pr-employee-accums-detail-form-ca"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accums-detail-form-ca/field-definitions-pr-employee-accums-detail-form-ca"
---

# Field Definitions: PR Employee Accums Detail Form (CA)

(Canada) The following is a list of field descriptions for the
 PR Employee Accums Detail form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Employee

(Canada) The Employee field on the PR Employee Accums Detail form.
In this field:

- To change employees for whom to add or
 edit detail records, enter the employee number or press F4 to
 select from a list of employees who have records in PR Employee Accumulations.

- To edit the current employee's detail
 record, accept the default.

You cannot use the [PR Employee Accums Detail](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accums-detail-form-ca) form to add records for employees who do not already exist in the [PR Employee Accumulations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accumulations-form) form. To create detail records for an employee who does not already exist in the PR Employee Accumulations form, first add the employee in that form.

## Month

 (Canada) The Month field on the PR Employee Accums Detail form.
Accept the default or enter a calendar month
 for which there are existing records in PR Employee Accumulations for the selected
 employee.
All amounts are based on the payment month.

## Type

(Canada) The Type drop-down on the PR Employee Accums Detail form.
Accept the default or press F4 to select an
 EDL type for which there are existing records for the selected employee and month
 combination in PR Employee Accumulations.
Types include: E-Earnings,
 D-Deduction, or L-Liability.

## EDL Code

(Canada) The EDL Code field on the PR Employee Accums Detail form.
Accept the default, or press F4 to select an
 EDL code for which there are existing records for the selected employee, month, and EDL
 type combination in PR Employee Accumulations. The code entered here must a valid code for
 the type of accumulation selected in the Type field.

## Record ID

(Canada) The Record ID field on the PR Employee Accums Detail form.
To add a new detail record, you can either double-click in this field or enter +; the system automatically assigns the next sequence number.
Note: You can only add detail records for an employee/month/type/EDL code that exists in PR Employee Accumulations. If you need to add detail records for a new employee/month/type/EDL code, you must add the employee/month/type/EDL code record in PR Employee Accumulations before adding detail records here.

## Province

(Canada) The Province field on the PR Employee Accums Detail form.
Defaults from the Tax Prov field
 in [PR
 Employees](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form).
Accept the default for this record, or press
 F4
 to select from a list of provinces. This should be the employee's resident province for
 province-based accumulations.
Entering a province here will not update the
 Tax
 Prov field in PR Employees.

## Payroll Program Account

(Canada) The Payroll Program Account field on the PR Employee Accums Detail
 form.
Defaults from the Payroll Program
 Account field in [PR
 Employees](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form). If there is no value in PR Employees, then defaults from [PR Company Parameters](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form).
Accept the default for this record, or enter a different Canadian Business Number Payroll Program Account reference number. The number must begin with RP and be followed by four digits.
Entering a value here will not update the
 Payroll Program
 Account field in PR Employees or PR Company Parameters.

## Quebec File #

(Canada) The Quebec File # field on the PR Employee Accums Detail form.
This field is available only if the value in
 the Province field is QC (Quebec).
Defaults from the Quebec File
 Number field in [PR Company Parameters](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form).
Accept the default for this record, or enter the company's Quebec File Number. The number must begin with RS and be followed by four digits.
Entering a number here will not update the
 Quebec File
 Number field in PR Company Parameters.

## Hours

(Canada) The Hours field on the PR Employee Accums Detail form.
This field is available if Type is set to
 E-Earnings.
Enter the month-to-date hours for this record.

## Subject Amount

(Canada) The Subject Amount field on the PR Employee Accums Detail form.
This field is available if Type is set to
 D-Deductions or L-Liabilities.
Enter the month-to-date subject amount for
 this record. Subject amounts include all earnings subject to the liability or deduction,
 including amounts not included in the calculation basis. (e.g. earnings flagged as subject
 only and earnings exceeding the subject limit).

## Eligible Amount

(Canada) The Eligible Amount field on the PR Employee Accums Detail form.
This field is available if Type is set to
 D-Deductions or L-Liabilities.
Enter the month-to-date eligible amount for this liability or deduction code.
Eligible amounts include those earnings used in the calculation basis for the deduction or liability amount. If a limit is specified for the deduction or liability (PR Deductions/Liabilities), this amount will be 0.00 once the limit is reached. If no limit is specified, the subject amount and eligible amount will always be the same.
If you are loading balance forwards, the following example shows how subject and eligible amounts should be entered for an employee who has gone over the limit and an employee who has not met the limit.
The following table shows two examples of eligible amounts if the SUTA limit is $20,000.
Employee
YTD
Subject Amount
Eligible Amount

100
$50,000
$50,000
$20,000

200
$15,000
$15,000
$15,000

For more information, see [About Deductions, Subject Amounts, and Eligible Amounts](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accumulations-form).

## Amount

(Canada) The Amount field on the PR Employee Accums Detail form.
Enter values as follows. When the Type field is
 set to:

- E-Earnings — Enter or edit the month-to-date amount for this earnings code.

- D-Deductions — If the deduction code entered for this line has a method of
 Rate of Gross, the amount is calculated based on the Rate
 specified in [PR Deductions/Liabilities](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form).
 Otherwise, enter or edit the month-to-date amount for this
 deduction code.

- L-Liabilities — If the liability code entered for this line has a method of
 Rate of Gross, an amount is calculated based on the Rate
 specified in [PR Deductions/Liabilities](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form).
 Otherwise, enter or edit the month-to-date amount for this
 liability code.
