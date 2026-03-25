---
title: "Field Definitions: PR ETP Employee Amounts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-employee-amounts-form/field-definitions-pr-etp-employee-amounts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-employee-amounts-form/field-definitions-pr-etp-employee-amounts-form"
---

# Field Definitions: PR ETP Employee Amounts Form

The following is a list of field descriptions for the PR ETP
 Employee Amounts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Employee

Defaults from the Employee field
 on the [PR ETP Summary Process](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-summary-process-form) form > Employee ETP By Date
 tab.
To view an existing employee record, enter the
 employee number or press F4 to select from a list of employees for
 the selected tax year.
You cannot add new employees from this form. To add an employee, use the [PR ETP Generate Amounts](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-generate-amounts-form) form or [PR ETP Summary Process](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-summary-process-form) form > Employee ETP By Date tab.

## Date of Payment

Defaults from the Date of Payment
 field on the [PR ETP Summary
 Process](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-summary-process-form) form > Employee ETP By Date tab.
To view an existing record, enter the payment
 date or press F4 to select from a list of payment dates for the selected tax year and
 employee.

## DL Code

Required.
 Defaults based on the ATO categories associated with the deduction/liability codes used for payments made to this employee (set up in [PR Employee Pay Sequence Control](/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-employee-pay-sequence-control-form)).
You can also enter a new DL Code to add
 additional records. Enter a valid deduction or liability code (set up in [PR Deductions/Liabilities](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)), or press F4 to select
 one from a list.
Editing the code in this field affects the amounts shown in the ETP Summary By Payment Code section of the form.

## Payment Code

Required.
 Defaults based on the ATO categories associated with the deduction/liability codes used for payments made to this employee. (ATO categories are assigned to deduction/liability codes in the [ATO Category](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036b98--en) field of PR Deductions/Liabilities. Deduction/liability codes are associated with employees in [PR Employee Pay Sequence Control](/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-employee-pay-sequence-control-form)).
You can change the payment code here, but the system will not update other forms in the system. Use the drop-down arrow to enter a valid payment code.
Selecting a different code in this field affects the amounts shown in the ETP Summary By Payment Code section of the form.

## Total Tax Withheld

This field defaults the total tax amount withheld for ETP from [PR Employee Accumulations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accumulations-form).
You can modify the amount here, but the system will not update PR Employee Accumulations.
Editing the amount in this field affects the amounts shown in the ETP Summary By Payment Code section of the form.

## Taxable Component

This field defaults the taxable amount (eligible amount) for ETP from [PR Employee Accumulations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accumulations-form).
You can modify the amount here, but the system will not update PR Employee Accumulations.
Editing the amount in this field affects the amounts shown in the ETP Summary By Payment Code section of the form.

## Tax Free Component

This field defaults the tax-free amount (subject minus eligible amount) for ETP from [PR Employee Accumulations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accumulations-form).
You can modify the amount here, but the system will not update PR Employee Accumulations.
Editing the amount in this field affects the amounts shown in the ETP Summary By Payment Code section of the form.

## Amended Summary

Check this box if you are generating an amended ETP summary for an employee after previously submitting a summary. When you check this box, the system will generate the amended version of the PR PAYG Payment Summary - Employee Termination Payment, clearly marked as being amended.

## Include in E-File

Defaults to checked.
Uncheck this box if this payment code record should not be included in the ATO e-file.
Note: The system will also clear or set this box for this
 employee when you edit the settings in [PR ETP/PAYG E-File Set/Unset](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etppayg-e-file-unsetset-form) (accessed via Tasks > Unset/Set
 'Include in E-File' checkboxes from the [PR ETP Summary
 Process](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-etp-summary-process-form) toolbar and the [PR PAYG Summary Process](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-payg-summary-process-form) toolbar).

## E-File Amendment Indicator

Defaults to O-Original.
Set this field to A-Amended if
 this ETP payment summary record has been previously submitted to the ATO, and is now being
 resubmitted with amended values.
