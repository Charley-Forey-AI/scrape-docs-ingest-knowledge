---
title: "Field Definitions: PR Employee DednsLiabs Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form"
---

# Field Definitions: PR Employee DednsLiabs Form

The following is a list of field descriptions for the PR Employee DednsLiabs form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Employee

 Enter the employee number.

##  Deduction/Liability Code

 Enter a valid deduction or liability code.

## Employee-Based

Check this box to indicate whether this deduction/liability is to be calculated after all Federal, State, Local, Insurance, and Craft/Class based deductions and liabilities have been processed.
Do not check this box for federal and state tax routines (unless specifically instructed to in the Tax & Worker’s Comp Routines table in the Overview section). Checking it for tax routines will give an error (#8162) when processing payroll (PR Payroll Process).

Related information

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [Set Up a Roth 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction)

- [Set Up a Catch-Up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction)

## Frequency

Enter the valid frequency code to establish how often this employee-based deduction or liability is calculated.
The Frequency code controls the processing of the employee-based deductions/liabilities. For example, if the frequency code is Monthly, the deduction/liability is only processed once a month when the code is set as “Active” in PR Pay Period Control.
Note: This field is disabled if the deduction or liability is not employee-based.

## Processing Seq#

The Processing Seq# field on the PR Employee Dedns / Liabs form, Info tab.
This field is only enabled when the Employee-Based checkbox is selected.
Enter the processing sequence number for this deduction or liability.
This field controls the order in which an employee-based deduction or liability is calculated (ascending). Deductions and liabilities set up without a processing sequence number are processed first, in order by deduction/liability code.
Note: Employee deductions that calculate as a rate of net should be set up last.

### 401(k) / Roth Deductions

If an employee has both 401(k) and Roth deductions, it is recommended that you assign different processing sequences to each. This ensures proper limit application, since both the 401(k) and Roth deductions are subject to the same limit for the same employee.
 You will also need to make sure you assign the appropriate processing sequence for the 401(k) and Roth catch-up deductions. Since the catch-up deductions kick in once the standard limit is met (depending on the age range), they should be set up with the same processing sequence as the 401(k) or Roth deduction.
For example:
DeductionProcessing Seq#
401(k)1
Roth2
401(k) Catch-up Contribution1
Roth Catch-up Contribution2

Important: The Secure 2.0 Act allows for an increased catch-up limit for employees meeting the minimum / maximum age range defined in the pre-tax deduction group; however, no additional deduction setup is required. The system automatically applies the higher limit when an employee reaches the minimum age and reverts to the standard limit when they reach the maximum age. Eligibility for the increased limit is based on the employee's age by December 31st of the tax year. If they reach the minimum age by that date, the higher limit applies from January 1st of that year. If they exceed the maximum age by December 31st of the tax year, the standard limit applies beginning January 1st of that year.

Important: Be mindful that the processing sequence chosen can affect, or be affected by, other deductions like garnishments.

## Filing Status (US)

The Filing Status drop-down on the PR Employee Dedns/Liabs form, Info tab, Routine Info section.
Enter the filing status for this employee.
For Federal W-4s submitted after January 1, 2020, this is the value from Step 1c of Form
 W-4 (2020). only the following options are valid.

- M = Married Filing Jointly

- S = Single or Married Filing Separately

- H = Head of Household

For Federal W-4s submitted prior to January
 1, 2020 and state W-4s:

- S = Single

- M = Married, Filing Separately

- H = Head of Household

- F = Married Filing Jointly, one
 spouse working

- B = Married Filing Jointly, both spouses working (state only)

- W = Qualified Widow(er)

- O = No exemptions (Alabama only)

Important: It is very important that you check for any special requirements defined for the state to determine whether you must set up a separate state deduction filing status.
It is not always necessary to define a state deduction if the filing status is the same as the employee’s federal filing status. In general, if a state deduction has not been defined for an employee, the system automatically uses the federal filing status. If a state deduction has been defined and the filing status and exemption are left blank, a filing status of 'S' with exemptions of zero is assumed.
For employees residing in Ohio and paying Ohio School District tax, the Ohio state tax deduction must be defined. The school district tax computation relies on the regular exemptions specified for Ohio state tax.
Many state routines allow only 'M' or 'S' as a valid filing status. Other exceptions to filing status include Connecticut, Georgia, and Puerto Rico. See [United States Tax and Worker's Comp Routines](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states) for more information.

Australian Users: See [Filing Status](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-0005c055--en) for information on this field.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Filing Status (AUS)

Select M from the drop-down if the employee
 submitted Form NAT 0929 and answered Yes to question 9 (Do you have a
 spouse). Otherwise, leave this field blank.

## Scale

(Australia) The Scale field on the PR Employees form, Filing Status tab.
Scale Numbers for PAYG WithholdingEnter the scale number for PAYG Withholding. Available numbers are as follows:

- 1 = No tax-free threshold; enter this if question 8 on the employee's NAT 3093 is No

- 2 = Tax-free threshold with leave loading

- 3 = Foreign resident; enter this if the employee is a non-resident

- 4 = No tax file number (TFN) was provided by the employee

- 5 = Full Medicare exemption; enter this if the employee filed a NAT 0929 and claimed a full exemption

- 6 = Half Medicare exemption; enter this if the employee filed a NAT 0929 and claimed a half exemption

Scale Numbers to Calculate STSL ComponentIf you need to calculate a Study and Training Support Loan component for an employee, use the following scale numbers:

- 91 = No tax-free threshold; enter this if question 8 on the employee's NAT 3093 is No

- 92 = Tax-free threshold with leave loading

- 93 = Foreign resident; enter this if the employee is a non-resident

- 95 = Full Medicare exemption; enter this if the employee filed a NAT 0929 and claimed a full exemption

- 96 = Half Medicare exemption; enter this if the employee filed a NAT 0929 and claimed a half exemption

Note: The STSL Component schedule applies to employees who have any of the following debts:

- Higher Education Loan Program (HELP)

-
VET Student Loan (VSL)

-
Financial Supplement (FS)

-
Student Start-up Loan (SSL) / ABSTUDY SSL

-
Trade Support Loan (TSL)

## Children

Enter the number of children for the employee. Enter a number here when the answer to question 12 on the employee's NAT 0929 is Yes. Otherwise, leave blank.

## Apply tax offset

Select this checkbox if the answer to
 question 7 on the employee's NAT 3093 is Yes. When you select this checkbox, the system
 enables the Tax
 Offset field, where you can enter the estimated tax offset amount from the
 NAT 3093.

## Tax offset

The system enables this box when you check the
 Apply tax
 offset box.
If the answer to question 7 on the employee's Nat 3093 is Yes, enter the estimated total tax offset amount in this field.

## Regular Exempt's

The Regular Exempt's field on the PR Employee Dedns/Liabs form, Info tab, Routine Info section.
Enter the number of regular exemptions claimed on the W-4. This field is not used for every state. For more information on how this field is used, see [United States Tax and Worker's Comp Routines ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states)and locate your state.
Australian users: See [Scale](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-0005c05c--en) for the field definition for this field.
2020 Federal W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank. Instead, use the Dependent Amount field to enter the annual dollar amount to claim as a dependent deduction. For more information, see [Dependent Amount](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#concept-4337--en).
Pre-2020 Federal W-4s
For Federal W-4 information entered prior to January 1, 2020, this field is still applicable. However, if the employee submits a Federal 2020 W-4, it is suggested that you clear the value in this field.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Add'l Exempt's

The Add'l Exempt's field on the PR Employee Dedns/Liabs form, Info tab, Routine Info section.
Enter the number of additional exemptions claimed on the W-4.
Australian users: See [Children](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-0005c04f--en) for the field definition for this field.
Candian users: Enter the number of additional exemptions claimed on the T4.
Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank. Instead, use the Dependent Amount field to enter the annual dollar amount to claim as a dependent deduction. For more information, see [Dependent Amount](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#concept-4337--en).
Pre-2020 Federal W-4s
For Federal W-4 information entered prior to January 1, 2020, this field is still applicable. However, if the employee submits a Federal 2020 W-4, it is suggested that you clear the value in this field.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Apply Tax Credits

This field displays for Canadian users only.
Check this box to enable the Authorized Tax
 Credits field, where you can record additional tax credits for the
 employee.

## Override Misc Amount #1

This checkbox is currently used for Mississippi and Michigan State Tax only.
Select this checkbox to override the routine’s Misc Amount #1 (usually the exemption amount). You will need to enter a new miscellaneous amount in the Misc Amount #1 field.
Australian users: See [Apply tax offset](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-0005c048--en) for the field definition for this field.
Canadian users: See [Apply tax credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-0005c0b7--en) for the field definition for this field.
Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Misc Amount #1

This field is enabled only if you selected the Override Misc Amount #1 checkbox.
Enter the amount to use when calculating for this employee.
Australian users: See the field definition for [Tax offset](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-0005c0a8--en).
Canadian users: See the field definition for [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en).
Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Authorized Tax Credits

 The field is for Canadian users only.
Available if the Apply tax
 credits checkbox is checked.
Enter the Annual Amount from line 15 of the employee's TP-1016-V form (Application for a Reduction in Source Deductions of Income Tax for an Individual or a Self-Employed Person).

## Misc Factor

This field is for U.S. users only.
If you selected the Override Misc Amount #1 checkbox and entered an amount in the Misc Amount #1 field, enter a factor here. Factors are currently only used by a few tax routines (e.g., Arizona state tax).
Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Total Claim Amount

This field displays for Canadian users only.
 Enter the total claim amount from the
 employee’s TD1 form. The value you enter here updates the Total Claim
 Amount field on the Filing Status tab on PR Employees.
Note: You only need to enter a value here if the Employee is not
 claiming the Basic Personal Exemption on the TD1-Federal/TD1-Provincial. The routines for
 Federal and Provincial taxes (defined in PR Routines) will automatically realize the
 current annual personal exemption.

## Multiple Jobs Checked

The Multiple Jobs Checked checkbox on the PR Employee Dedns/Liabs form, Info tab, Routine Info section.
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Select this checkbox if the employee filled out Step 2 of Federal Form W-4 (2020); that is, the employee has more than one job or is married filing jointly and their spouse also works).
Leave this checkbox unselected if the employee did not fill out Step 2 of Federal Form W-4 (2020).
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Dependent Amount

The Dependent Amount field on the PR Employee Dedns/Liabs form, Info tab, Routine Info section.
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Enter the total annual dollar amount to be claimed as a dependent deduction. This is the total amount entered by the employee in Step 3 of Federal Form W-4 (2020); that is, the amount entered on Line 3.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Other Income

The Other Income field on the PR Employee Dedns/Liabs form, Info tab, Routine Info section
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Enter the total other income as entered by the employee in Step 4a of Federal Form W-4 (2020). This amount represents the total annual income the employee expects during the year that will not have withholding (such as interest, dividends, retirement income, etc).
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Other Deductions

The Other Deductions field on the PR Employee Dedns/Liabs form, Info tab, Routine Info section.
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Enter the total other deductions entered by the employee in Step 4b of of Federal Form W-4 (2020). This amount represents the total annual deductions other than the standard deduction.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Total Claim Amount

 The field is for Canadian users only.
 Enter the total claim amount from the
 employee’s TD1 form. The value you enter here updates the Total Claim
 Amount field on the Filing Status tab on PR Employees.

## Calculations

Indicate what kind of calculation override applies (if any) to the deduction/liability.

- Use Calculated Amount — No override, use the amount as calculated.

- Override Method - Use Rate Of Gross — Override the
 standard method and calculate as a rate of gross. Useful for those employees who want
 their Federal Tax calculated as a rate of earnings instead of based on the Federal
 Tax routine. Selecting this option enables the Rate/Amount field below.

- Override Standard Rate/Amount — Use the standard
 calculation method, but override the rate or amount. Use this option to establish an
 employee rate or amount that is subject to limits. Selecting this option enables
 the
 Rate/Amount field below.

- Override With A Fixed Amount — Override the
 calculated amount with a fixed amount (no limit). Use this option when you want a
 specific result each time the deduction or liability is calculated, regardless of
 limits. If greater than 0.00, add-on amounts will be added to this value. Selecting
 this option enables the Rate/Amount field below.

Note: Limits are applied when the deduction code is set up with a [Method ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-000369dd--en) of Rate of Net. Limits are also applied when the deduction code uses a [ Pre-Tax Group](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036acc--en). In both of these cases, the system always apply limit checks even when a fixed amount override is entered.
A typical use of this option is for garnishments. Garnishments should be set up in PR Deductions/Liabilities with a Method of N-Rate of Net. If the garnishment is flat amount with a minimum net pay, the method can be overridden here. This option may also be used on federal and state withholding routines to override the tax with 0.00 for exempt employees.
Another typical use of this option is setting up 401(k) deductions, when the deduction is set up as Rate of gross and an employee wants his or her deduction set at a flat amount. You can use the Override With a Fixed Amount option as long as the 401(k) deduction uses Pre-Tax Groups to control limits.

Related information

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [Set Up a Roth 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction)

- [Set Up a Catch-Up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction)

## Rate/Amount

Enter the employee’s rate, if overriding the method or standard rate, or enter the Employee’s amount, if overriding with a fixed amount.
Note: If an override rate or amount is not entered here, the standard rate or amount specified for this deduction in PR Deductions/Liabilities is used.

Related information

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [Set Up a Roth 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction)

- [Set Up a Catch-Up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction)

- [Set Up a 401(k) Employer Match](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-401k-employer-match)

- [Set Up a Multi-Tiered 401(k) Employer Match](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-multi-tiered-401k-employer-match)

## Override Standard Limit

Select this checkbox to override the standard limit for this deduction/liability (as defined in PR Deductions/Liabilities).
Note: Checking this box does not override the limit basis or how it is applied. It is only used to override the limit amount or rate.
Do not select this checkbox if using the standard limit defined for this deduction/liability in PR Deductions/Liabilities.

Related information

- [Set Up a Standard 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-standard-401k-deduction)

- [Set Up a Roth 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-roth-401k-deduction)

- [Set Up a Catch-Up 401(k) Deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/set-up-a-catch-up-401k-deduction)

## Rate/Amount

 Used only when the Override Standard
 Limit checkbox is checked.
 Specify the override limit amount or rate for this employee and deduction/liability.
Note: Rate of Earnings limits apply to liabilities only.

## Minimum Net Pay

Indicate if a minimum net pay value should be used to limit the amount of a deduction (disabled for liabilities). This field is typically used for garnishments. Select from the following options:

- No Minimum

- Based on Percent of Net Pay

- Based on Amount of Net Pay

The amount of the deductions will be reduced as needed to leave the minimum net pay indicated. If a garnishment group has been assigned to the deduction in PR Deductions/Liabilities, then only those earnings and deductions are included as “net pay”. If no garnishment group has been assigned, all earnings and deductions are included (deductions with a lower processing sequence than the garnishment).

## Percent/Amount

 Enter the percent (for example, enter 25% as 25.00) or amount (positive), which is dependent upon selection in the Minimum Net Pay field.

## Add-on

Add-ons allow you to calculate an additional amount to the normal calculation of a deduction or liability. A typical example is an additional amount or percentage of earnings to be withheld for federal or state income taxes.
Specify the add-on type for this deduction, to indicate how the add-on amount is to be calculated.

- None — No additional amount is to be calculated.

- Amount — Add-on is a flat amount. Selecting this option enables the Rate/Amount field.Important: If you are entering extra withholding information from Federal Form W-4, you must select this type.

- Rate — Add-on is calculated as a rate of the subject amount. Selecting this option enables the Rate/Amount field.

Canadian users: See [Add-on Rate / Amount](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-0005c0be--en) for additional help.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Rate / Amount

The Rate/Amount field on the PR Employee Dedns/Liabs form, Info tab, Add-On section.
Used only when an Add-on type is specified (previous field).
Specify the additional amount or rate to withhold from the employee's pay for each pay period. Add-on amounts can be any dollar value; however, if entering a rate, you will typically enter a value between 0.00 and 1.00 (e.g. .25000, .50000, etc. with 1.00000 representing 100%).
Canadian users: See [Add-on Rate / Amount](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-0005c0be--en) for the field definition for this field.Note: If you are entering extra withholding information from Federal Form W-4, this is a dollar amount, not a rate; therefore, you must set the Add-On type to Amount.

Federal 2020 W-4s
If you are entering information from from Federal Form W-4 (2020), enter the dollar amount specified in Step 4c. This is the additional amount per pay period to withhold.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Add-on Rate / Amount

 The field is for Canadian users only.
 Enter the annual Add-on Amount from line 11 of the employee's TP-1015.3-V form (Source Deductions Return). Quebec users must enter the amount value only.

## Auto AP Overrides: Vendor

Enabled only for employee-based deductions or
 liabilities for which the “Automatic Update to Accounts Payable” option in PR
 Deductions/Liabilities is checked.
Specify the vendor to create AP transactions for paying this employee-based deduction/liability. Vendor specified here override the vendor specified for the DL code in PR Deductions/Liabilities.
This may be used for garnishments. The same deduction code can be used for multiple garnishments, but allows the AP transactions to be separate vendors.
Note: An override vendor must be specified here in order to
 enter EFT Child Support information below and the vendor must be set up for EFT payments
 and Child Support addenda information (in AP Vendors).

##  Auto AP Overrides: Trans Description

 Enabled only for employee-based deductions or liabilities for which the “Automatic Update to Accounts Payable” option in PR Deductions/Liabilities is checked.
 Enter a description, up to 30 characters. If this is a garnishment-type deduction, you might use this field to enter the case number. This description is used as the AP transaction header description and overrides the standard description for the deduction/liability code if a separate transaction is created for each employee.

##  EFT Child Support Info: Case ID#

Required.
 Enabled only for employee-based deductions or
 liabilities for which the "Automatic Update to Accounts Payable” option in PR
 Deductions/Liabilities is checked, and if the override vendor (specified above) is set up
 for EFT payments and Child Support addenda information (in AP Vendors, Add’l Info tab).
 Enter the employee’s assigned case identification number, up to 20 characters.

##  EFT Child Support Info: Fips Code

Optional.
 Enabled only for employee-based deductions or
 liabilities for which the "Automatic Update to Accounts Payable” option in PR
 Deductions/Liabilities is checked, and if the override vendor (specified above) is set up
 for EFT payments and Child Support addenda information (in AP Vendors, Add’l Info tab).
 Enter the FIPS (Federal Information Process Standard) code for the child support entity receiving the transaction.

## EFT Child Support Info: Health Insurance Available

Required.
 Enabled only for employee-based deductions or
 liabilities for which the "Automatic Update to Accounts Payable” option in PR
 Deductions/Liabilities is checked, and if the override vendor (specified above) is set up
 for EFT payments and Child Support addenda information (in AP Vendors, Add’l Info tab).
 Check this box if the non-custodial parent has family medical insurance available through his/her employer.
 Do not check this box if the non-custodial parent does not have family medical insurance available through his/her employer.

## Override GL Account

Enabled only if the Employee-Based
 box (above) is checked for the deduction/liability code.
Enter a valid GL Account (with a blank subledger type) if you want to override the standard (credit) GL Account for this deduction/liability.

## EIC Status

No longer used. Vista does not take any action on this field.
Enabled only if the Employee-Based checkbox (above) is selected for the deduction/liability code.

- S-Single or Head of Household

- M-Married w/o spouse filing certificate

- B-Married, both spouses filing certificates

Leave blank if the employee is not eligible for EIC benefits.

## Subject to Garnishment Allocations

Check this box if this deduction is subject to garnishment allocations (i.e. allocated based on the garnishment allocation setup defined in PR Employees, Add'l Info tab).
Note: The garnishment allocations feature can be used for any type of garnishment allocation; however, if an employee has both child support allocations and some other type of allocation (i.e., tax levy, student loan, etc.), you can only check this option for one allocation type (typically child support). If the employee has multiple child support orders, check this option for each child support deduction.
Additionally, if you check this option for a deduction, you must have Withholding Limit Percentage specified (PR Employees, Add'l Info tab); otherwise, no allocations occur.

##  Garnishment Allocations Group

 Enabled only if 'Subject to Garnishment Allocations' is checked.
 Specify the garnishment allocation group (0-255) for this deduction. Initially defaults to '1'.
 Garnishment allocation groups can be used to separate current support orders from arrears payments and to specify the order in which to process the groups. Typically, only one group for current support and one for arrears needs to be set up; however, you can designate more groups as necessary.

## Membership #

Note: The system displays this field when the
 Default Country
 field (HQ Company Setup) has been set to
 AU
 for Australia.
Enter the employee's superannuation fund
 number for this deduction/liability code. The system enables this field only for
 deduction/liability codes where the ATO Category field (PR Deductions/Liabilities
 Addl Info tab) has been set to Superannuation or Superannuation-Extra.
