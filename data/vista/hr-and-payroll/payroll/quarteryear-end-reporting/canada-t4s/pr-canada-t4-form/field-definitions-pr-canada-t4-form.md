---
title: "Field Definitions: PR Canada T4 Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/canada-t4s/pr-canada-t4-form/field-definitions-pr-canada-t4-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/canada-t4s/pr-canada-t4-form/field-definitions-pr-canada-t4-form"
---

# Field Definitions: PR Canada T4 Form

The following is a list of field descriptions for the PR Canada T4 form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Tax Year

Enter the tax year for setting up T4 information.

## Business Number

The Business Number field on the PR Canada T4 form, Info tab.
This field defaults the Business Number defined in HQ Company Setup. If the Business Number in HQ Company Setup exceeds 9 digits, the system will only default the first 9 digits of the specified number here.
If you did not specify a Business Number in HQ Company Setup, this field defaults as blank and you must enter the 9-digit business number for your company, as provided by the Canada Revenue Agency.

Related information

- [PR Canada T4 Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/canada-t4s/pr-canada-t4-form)

## Transmitter Number

Enter the transmitter number that was assigned to you by the CRA.

## Dental Benefits Code

(Canada only) The Dental Benefit Code drop-down on the PR Canada T4 form, Info tab.

Select the Dental Benefits code (offered by the employer) that applies to most employees for the specified tax year.

- 1-Not Eligible

- 2-Payee only

- 3-Payee, spouse, children

- 6-Payee, spouse

- 5-Payee, children

When you initialize employee T4 records (by selecting Initialize Employee Slips in PR Canada T4), the system uses the dental benefits code designated for each employee in PR Employees to populate the Dental Benefits Code field on their T4 record. If no dental benefits code is designated for the employee in PR Employees, the system uses the employer's code specified here instead.
Note: If you leave this field blank and the Dental Benefits Code field for the employee (in PR Employees) is also blank, the system assigns a value of 1-Not Eligible to the employee's T4 record.

## Company Name

Enter the name of your company.

## RPP Number

Enter the Registered Pension Plan number for your company.

## Owner SIN#

Enter the Social Insurance Number for the owner of this company, if individually owned.

## Co Owner SIN#

Enter the Social Insurance Number of the co-owner of this company, if owned by individuals.

## Address

Enter the street address of your company.

## Address Cont

Enter any additional address information for your company.

## City

Enter the city associated with the address of your company.

## Province

Enter the province associated with the address of your company.

## Postal Code

Enter the postal code associated with the address of your company.

## Country

Enter the country associated with the address of your company.

## Contact Name

Enter the name of the contact person for your company.

## Phone

Enter the phone number for the contact person of your company.

## Phone Ext

Enter the extension for the contact person of your company.

## Contact Email

Enter the email address for the contact person for your company.

## Tax Year Open/Closed

The Tax Year Open/Closed option on the PR Canada T4 form, Info tab.
Specify whether the tax year is open or closed.

- Open - Select this option if the tax year is open and users can initialize or edit T4 values for the year. Note: Beginning December 2021, you must use Aatrix to create and submit T4s. You can still initialize and edit T4 values in this form prior to creating and submitting T4s; however, once you have completed processing T4s and RL Slips, any further edits must be done in Aatrix.

- Closed - Select this option once you have completed processing T4 and RL Slips for the current tax year. You can still view T4 values and run the PR Canada T4 Slip Review report from this form; however, you will be unable to re-initialize or edit existing T4 data, nor can you create and submit T4s via Aatrix.

## Box Number

The Box Number field on the PR Canada T4 form, T4 Box Items tab.

Enter the T4 box number for reporting amounts
 for the tax year. Press F4 for a list of valid box numbers.

## EDL Type

The EDL Type field on the PR Canada T4 form, T4 Box Items tab.

Select the type of code that you want to associate with this box item:

- E- Earnings - Benefit earnings type (e.g., 401(k), Cafeteria Plan, Subsistence, etc.).

- D- Deduction - Deduction type ( e.g., Canadian Pension Plan (CPP), Employment Insurance (EI), etc.).

- L- Liability - Liability type (e.g., taxes, insurance, union benefits, etc.).

Several T4 Box Items are restricted to entry of a specific EDL type. For example, in Box 16 (Employee's CPP Contributions), you must enter an EDL type of D-Deduction. If you enter an invalid EDL Type, a warning is displayed and you must enter the appropriate EDL type before you can save the record.
For more information, select the links below.
[Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)
[Set up an EI Deduction Code: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-an-ei-deduction-code-canada)
[Set up QPP / QPP2 Deductions: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-qpp--qpp2-deductions-canada)
[Set up CPP / CPP2 Deductions: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-cpp--cpp2-deductions-canada)
[Associate Deductions and Liabilities with Earnings Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/associate-deductions-and-liabilities-with-earnings-codes)

Related information

- [Set T4 Information for the Current Tax Year](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/canada-t4s/process-canadian-t4s/set-t4-information-for-the-current-tax-year)

- [PR Canada T4 Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/canada-t4s/pr-canada-t4-form)

## EDL Code

The EDL Code field on the PR Canada T4 form, T4 Box Items tab.

Enter the deduction or liability code for the type of code associated with this box item or press F4 to select from a list of valid codes.
Several of the T4 Box Items require entry of deduction or liability codes that are defined in PR Federal Info. For example, in Box 16 (Employee's CPP Contributions), you must enter the deduction code you specified in the CPP Deduction field in PR Federal Info. If you enter a deduction code that does not match what is defined in PR Federal Info, a warning is displayed and you must enter the appropriate code before you can save the record.
Tip: You can press F5 to set up an associated EDL Code in PR Deductions/Liabilities if needed.

## Amount Type

The Amount Type field on the PR Canada T4 form, T4 Box Items tab.

Select an amount type for the box item:

- A-Amount – A - Amount – Select this option for an earnings code to report the earnings amount, or for a deduction code or liability code to report the calculated amount of the deduction or liability. This option is appropriate for liabilities that are treated like earnings. If the box item requires reporting both earnings and liabilities, select this option for the relevant earnings codes and liability codes so that the amounts will be added together

- E-Eligible Amount – Include only those earnings used in the calculation basis for the deduction amount.

- S-Subject Amount – Wages that are subject to a certain deduction or liability.

Tip: For Box Item 14, be sure to set the Amount Type field for earnings or liabilities to A-Amount.

Several T4 Box Items are restricted to entry of a specific Amount Type. For example, in Box 16 (Employee's CPP Contributions), the Amount Type field must be left empty. If you enter an Amount Type, a warning is displayed and you must clear the field before you can save the record.

## Code Number

The Code Number field on the PR Canada T4 form, T4 Other Codes tab.

Once you select Initialize Employer T4 Items/Codes, the system defaults either the default code numbers or the code numbers that you specified for the previous tax year.
Enter the code number for an amount that relates to employment commissions, taxable allowances and benefits, deductible amounts, etc. Press F4 for a list of valid box numbers.

## EDL Type

The EDL Type field on the PR Canada T4 form, T4 Other Codes tab.

Select the type of code that you want to associate with this box item:

- E- Earnings - Benefit earnings type (e.g., 401(k), Cafeteria Plan, Subsistence, etc.).

- D- Deduction - Deduction type ( e.g., Canadian Pension Plan (CPP), Employment Insurance (EI), etc.).

- L- Liability - Liability type (e.g., taxes, insurance, union benefits, etc.).

Related information

- [Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)

- [Set up an EI Deduction Code: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-an-ei-deduction-code-canada)

- [Set up CPP / CPP2 Deductions: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-cpp--cpp2-deductions-canada)

- [Set up QPP / QPP2 Deductions: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-qpp--qpp2-deductions-canada)

- [Associate Deductions and Liabilities with Earnings Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/associate-deductions-and-liabilities-with-earnings-codes)

- [Set T4 Information for the Current Tax Year](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/canada-t4s/process-canadian-t4s/set-t4-information-for-the-current-tax-year)

- [PR Canada T4 Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/canada-t4s/pr-canada-t4-form)

## EDL Code

The EDL Code field on the PR Canada T4 form, T4 Other Codes tab.

Enter the specific code number for the type of code associated with this box item. Press F4 for a list of codes.

## Amount Type

The Amount Type field on the PR Canada T4 form, T4 Other Codes tab.

Select an amount type for the code:

- A-Amount – Liabilities that are treated like earnings. Select this option when you have to set up both earnings and liabilities so that the amounts will be added together.

- E-Eligible Amount – Include only those earnings used in the calculation basis for the deduction amount.

- S-Subject Amount – Wages that are subject to a certain deduction or liability.

## Employee

Enter the number for the employee that you are
 reporting T4s for. Press F4 for a list of valid employees.
Once you enter the employee number here, the rest of the fields on the Info tab default information from the employee record in PR Employees.

## SIN Number

This field defaults from the SIN Number field in
 PR Employees after you enter an employee number in the Employee field. The system will validate
 that the number you enter is unique and is a valid number. However, it is unable to verify
 that this is the correct number for the specific employee.
You may override the default here, but changes here do not update the employee record in PR Employees.

## RPPNumber

This field
 defaults from the RPPNumber field in PR Crafts (Add'l Info tab). If that field is blank, this
 field defaults from the RPP Number field in PR Canada T4.
Accept the default or enter another RPP (Registered Pension Plan) number for this employee.

## Dental Benefits Code

(Canada only) The Dental Benefits Code drop-down on the PR Canada T4 form, T4 Employees tab.

Select the Dental Benefits code (offered by the employer) that applies to this employee for the specified tax year.

- 1-Not Eligible

- 2-Payee only

- 3-Payee, spouse, children

- 6-Payee, spouse

- 5-Payee, children

When you initialize employee slips, the system assigns a dental benefits code to each employee's T4 record as follows:

- If a dental benefits code is designated for the employee in PR Employees, that code defaults here.

-  If no dental benefits code is designated in PR Employees, this field defaults the dental benefits code specified for the employer on the Info tab in PR Canada T4.

- If no dental benefits code is designated for the employee or the employer, this field defaults to 1-Not Eligible.

The system uses the Dental Benefits Code assigned here to populate Box 45 on the employee's T4 Slip.

## First Name

This field defaults from the First field in
 PR Employees after you enter an employee number in the Employee field.
You may override the default here, but changes here do not update the employee record in PR Employees.

## Mid Name

This field defaults from the Middle field in
 PR Employees after you enter an employee number in the Employee field.
You may override the default here, but changes here do not update the employee record in PR Employees.

## Last Name

This field defaults from the Last field in
 PR Employees after you enter an employee number in the Employee field.
You may override the default here, but changes here do not update the employee record in PR Employees.

## Address 1

This field defaults from the Address field
 in PR Employees after you enter an employee number in the Employee
 field.
You may override the default here, but changes here do not update the employee record in PR Employees.

## Address 2

This field defaults from the Add'l Address
 field in PR Employees after you enter an employee number in the Employee
 field.
You may override the default here, but changes here do not update the employee record in PR Employees.

## City

This field defaults from the City field in
 PR Employees after you enter an employee number in the Employee field.
You may override the default here, but changes here do not update the employee record in PR Employees.

## Province

This field defaults from the Province field
 in PR Employees after you enter an employee number in the Employee
 field.
You may override the default here, but changes here do not update the employee record in PR Employees.

## Postal Code

This field defaults from the Postal Code
 field in PR Employees after you enter an employee number in the Employee
 field.
You may override the default here, but changes here do not update the employee record in PR Employees.

## Country

This field defaults from the Country field
 in PR Employees after you enter an employee number in the Employee
 field.
You may override the default here, but changes here do not update the employee record in PR Employees.

## Exempt

The CPPQPP Exempt, EI Exempt, and PPIP Exempt checkboxes on the PR Canada T4 form, T4 Employees tab.
These checkboxes default from the CPP-QPP Exempt, EI Exempt, and PPIP Exempt fields in PR Employees after you enter an employee number in the Employee field.
You may override the default here, but changes here do not update the employee record in PR Employees.
Select a checkbox to mark the employee as exempt from the Canadian Pension Plan, Employment Insurance, or Provincial Parental Insurance Plan.
