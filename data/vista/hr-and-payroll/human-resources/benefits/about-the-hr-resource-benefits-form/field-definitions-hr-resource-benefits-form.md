---
title: "Field Definitions: HR Resource Benefits Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-resource-benefits-form/field-definitions-hr-resource-benefits-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-resource-benefits-form/field-definitions-hr-resource-benefits-form"
---

# Field Definitions: HR Resource Benefits Form

The following is a list of field descriptions for the HR
 Resource Benefits form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Resource #

 Enter the resource (defined in HR Resources)
 for whom you are defining benefits.

## Dependent Seq #

 Enter the dependent’s sequence number. If defining benefits for the employee, this number should be 0 (zero). The description for dependent sequence number ‘0’ will be “Same as Resource Number”.If defining benefits for an employee’s dependents, this number should be the number assigned to the dependent in HR Resource Dependents.

## Benefit Code

 Enter the code (defined in HR Benefit Codes) that identifies the benefit this employee is qualified for.
Note: If you used the HR Benefit Initialization feature, all benefits defined for the associated benefit group (HR Benefit Group) will automatically be set up here.

## Benefit ID #

 Enter the employee’s identification number for this benefit, up to 20 characters.

## Smoker

Smoker checkbox on the HR Resource Benefits form, Info tab
 Select this checkbox if this employee/dependent is a smoker.
 Leave this box unselected if this employee/dependent is a non-smoker.

## Employer Cost of Benefit

Employer Cost of Benefit field on the HR Resource Benefits form, Info tab
 For resources where the Dependent Seq #
 field has a value of 0 (zero) only, specify what portion of cost of this benefit is paid by
 the employer, up to 10 digits and 2 decimals.

Related information

- [About the HR Resource Benefits form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-resource-benefits-form)

## Benefit Is Part of a Cafeteria Plan

Benefit Is Part of a Cafeteria Plan checkbox on the HR Resource Benefits form, Info tab
Select this checkbox if this benefit is part of a cafeteria plan.
Leave this checkbox unselected if this benefit is not part of a cafeteria plan.
Note: This field is informational only; the system includes this information on the HR Resource Benefits report.

## Cafeteria Plan Amount

Cafeteria Plan Amount field on the HR Resource Benefits form, Info tab
For benefits that are part of a cafeteria plan, specify the amount that the employee pays for this benefit, up to 10 digits and 2 decimals.
Note: This field is informational only; the system includes this information on the HR Resource Benefits report.

## Primary Beneficiary

 Enter the name of the primary beneficiary for this resource/benefit, up to 30 characters.

## Primary Beneficiary Relationship

 Specify how this beneficiary is related to the resource (e.g. spouse, son, daughter, etc.), up to 30 characters.

## Secondary Beneficiary

 Enter the name of the secondary beneficiary for this resource/benefit, up to 30 characters.

## Secondary Beneficiary Relationship

 Specify how this beneficiary is related to the resource (e.g. spouse, son, daughter, etc.), up to 30 characters.

## Eligibility Date

 Enter the date this employee or employee’s
 dependent is eligible for the specified benefit. Initially defaults the employee’s hire
 date (specified in HR Resources) unless the benefit code has an eligibility restriction, in
 which case, the default is based on the hire date plus the eligibility period.

## Reminder Date

 Optional. Use to enter reminder date for an important action related to this benefit for this employee/dependent.

## Active

Select this checkbox if this benefit is
 active for this employee/dependent. This checkbox will automatically be selected if you
 used the HR Benefit Initialization feature, and the ElectiveYN checkbox in HR Benefit Groups
 was left unselected.
Leave this box unchecked if this benefit is
 not active for this employee/dependent. This checkbox will automatically be left
 unselected if you used the HR Benefit Initialization feature, and the ElectiveYN
 checkbox in HR Benefit Groups was selected.
Note: This box does not control whether or not PR is updated when the HR Update Benefit/Salary to PR batch process is run. You can process updates to PR with this box unchecked.

## Effective Date

Effective Date field on the HR Resource Benefits form, Info tab
Indicate the date on which this benefit becomes active for this employee/dependent.
Note: When adding a new resource, the system compares this
 date with the effective date in HR Benefits Codes (Effective Date field, Earnings Codes or
 Deduction/Liability Codes tab). If the date in this field is prior to that in the effective
 date in HR Benefits Codes, the system uses the old rate from HR Benefits Codes. If the date
 in this field is after the date in HR Benefit Codes, but the rates have not been updated
 (you did not check the Updated YN box in HR Benefits Codes for
 either earnings or deductions/liabilities), the system uses the old rate. If you have
 checked the Updated
 YN box, the system uses the new rate.
If this benefit code is active for this
 resource and has been defined as an ACA health plan, then a date entered here also
 automatically populates the Effective Date field on the ACA Coverage
 History tab.

Related information

- [About the HR Resource Benefits form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-resource-benefits-form)

## Expiration Date

Expiration Date field on the HR Resource Benefits form, Info tab
 Enter the date on which this benefit will expire for this employee/dependent. This date does not affect any calculation and the system uses it for warning and reporting purposes for benefit expiration.
If this benefit code is active for this
 resource and has been defined as an ACA health plan, then a date entered here also
 automatically populates the Expire Date field on the ACA Coverage
 History tab.

Related information

- [About the HR Resource Benefits form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-resource-benefits-form)

## Reinstate This Benefit

 Select this checkbox if this benefit will be reinstated for this employee/dependent. Reinstatement date is specified below.
 Leave this checkbox unselected if this benefit will not be reinstated for this employee/dependent.

##  Reinstate Date

 Enabled only when the Reinstate This Benefit option is checked.
 Indicate when this benefit will be reinstated for this employee/dependent.

## Deduction/Liability Codes: DL Code

For Dependent Seq #0 only: enter the Deduction or Liability code (from PR Deductions/Liabilities) that applies to this benefit.
This field will default any deduction and/or liability codes that were set up for the benefit code in HR Benefit Codes. Existing codes may be deleted or additional codes added as necessary.
Note: Deduction/liability codes added here will not be updated for the benefit code in HR Benefit Codes.
Tip: You can display a description field for this field by
 pressing F3 (Field Properties) from this field and selecting an option from the Description in
 Grid field. This DL Desc field does not display
 automatically.

##  Deduction/Liability Codes: DL Type

 This field is display only, indicating whether this is a Deduction (D) or Liability (L) type.

##  Deduction/Liability Codes: Option

 This field displays the benefit option that applies to this resource.
 Enter a valid benefit option (from HR Benefit Codes) for this employee.

##  Deduction/Liability Codes: Description

 Display only, the description of this deduction or liability as defined in PR Earnings Codes or PR Deductions/Liabilities.

## Deduction/Liability Codes: Employee Based? Y/N

Select this checkbox if this deduction or liability is employee-based (i.e. specific to this employee). Deduction or liability must have a Calculation Category of E (Employee) or A (Any). If this deduction or liability was assigned a frequency code (in HR Benefit Codes), this box defaults as checked. Deduction/liability will be calculated after all Federal, State, Local, Insurance, and Craft/Class based deductions and liabilities have been processed.
Leave this checkbox unselected if this deduction or liability is not employee based.

## Deduction/Liability Codes: Freq

 For employee-based deductions/liabilities only.
 Enter the frequency code (from HQ Frequency Codes) that indicates how often this employee-based deduction or liability is calculated (i.e. always, weekly, monthly, yearly, etc.). Deduction or liability must have a Calculation Category of E (Employee) or A (Any). Defaults the frequency assigned to the deduction or liability in HR Benefit Codes, if applicable.

##  Deduction/Liability Codes: Process Seq

 For employee-based deductions or liabilities only.
 Specify the processing sequence (1-9999) for this deduction/liability. This will be the order in which the deduction or liability will be calculated for this employee. Employee deductions that calculate as a rate of net should be set up last.
 If you initialized benefits (HR Benefit Initialization) or added them manually, the processing sequence defaults to 1. May be overridden.If you add deductions and/or liabilities manually, the processing sequence defaults as null. May be overridden.

## Deduction/Liability Codes: Override Calculation

If overriding the standard calculation specified for this deduction/liability (in PR Deductions/Liabilities), indicate what kind of calculation override applies:

- N-Calc Amount - Use the calculated amount

- R-Over Std Rate/ Amt - Use the standard method, but override the rate

- A-Over w/ Fixed Amt - Override the calculated amount with a fixed amount

If the deduction/liability code has a 0.00000
 value in the
 New
 Rate
 and
 Old
 Rate
 fields (in HR Benefit Codes), this field defaults to
 N-Calc
 Amount
 and the
 Rate/Amount
 field defaults as 0.00000. If there is a rate in either the
 New
 Rate
 and
 Old
 Rate
 fields in HR Benefit Codes, this field defaults
 R-Over Std Rate/
 Amt
 and the Rate/Amount field defaults based on the
 Effective
 Date
 field.

##  Deduction/Liability Codes: PR Rate/Amt #1

 Display only, the Rate/Amount #1 specified for this deduction or liability in PR Deductions/Liabilities.

## Deduction/Liability Codes: Rate/Amount

If you elected to override the standard calculation for this deduction or liability, enter the rate or fixed amount to use for this employee.
If the deduction/liability code has a 0.00000
 value in the New
 Rate and
 Old
 Rate
 fields (in HR Benefit Codes), the Override Calculation field defaults to

 N-Calc
 Amount
 and this field defaults as 0.00000. If there is a rate in either the

 New
 Rate
 and
 Old
 Rate
 fields in HR Benefit Codes, this field defaults
 R-Over Std Rate/
 Amt
 and this field defaults the rate based on the
 Effective
 Date
 field. For more information on the
 Effective
 Date
 field, click [here](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-resource-benefits-form/field-definitions-hr-resource-benefits-form#ID-00010cf3--en).

##  Deduction/Liability Codes: Override Limit

 If overriding the standard calculation, enter the override limit here. If limit is 0.00, then when updated to PR, the Override Standard Limit option in PR Employee Deductions and Liabilities will be set to N (unchecked), and the Limit will be set to 0.00.

##  Deduction/Liability Codes: Vendor

 Enter a valid vendor for this deduction or liability. The vendor specified here will override the vendor specified for this deduction or liability in PR Deductions/Liabilities.

##  Deduction/Liability Codes: AP Trans Desc

 Enter the AP transaction header description. This entry overrides the standard deduction/liability description if a separate transaction is created for each employee.

##  Deduction/Liability Codes: GL Co#

 Initially defaults the GL company defined for the HR company’s PR company. May be overridden.
Note: If overriding this deduction/liability’s GL account (next field), this will be the GL company against which the override GL account will be validated.

##  Deduction/Liability Codes: Override GL Account

 Use only if you want to override this deduction/liability’s standard GL account.
 Enter the GL account to credit for this deduction/liability. Must be a valid account (with subledger type blank) set up in GL Chart of Accounts for the GL Co# specified to the left of this field.

## Deduction/Liability Codes: Ready? Y/N

 Select this checkbox if this deduction/liability information is ready to be updated to PR. When benefit information is updated to PR, this deduction/liability information will be updated to the PR Employee Deductions and Liabilities (PRED) table.
 Leave this checkbox unselected if this deduction/liability information is not ready to be updated to PR.
Note: Update will include all deductions and liabilities for
 this benefit that are flagged as 'ready'. Those that are not flagged as 'ready' can be
 updated at a later time.

## Earnings Code: Earnings Code

Enter the earnings code (from PR Earnings Codes) that applies to this benefit (e.g. 401(k), Cafeteria Plan, Subsistence, etc.).
This field will default any earnings codes that were set up for the benefit code in HR Benefit Codes. Existing codes may be deleted or additional codes added as necessary.
Tip: You can display a description field for this field by
 pressing F3 (Field Properties) from this field and selecting an option from the Description in
 Grid field. This Earnings Code Desc field does not display
 automatically.

## Earnings Code: Auto Earnings Seq#

 Enter the processing sequence number (0-255) for this earnings code. When running PR Post Auto Earnings, this number will be used to determine the order in which this earnings code should be calculated for this employee.

##  Earnings Code: Option

 This field displays the benefit option that applies to this resource.
 Enter a valid benefit option (from HR Benefit Codes) for this employee.

## Earnings Code: Payment Seq

Enter the payment sequence (0-255) for this earnings code.
You will only need to enter a payment sequence here if you want these earnings posted to a specific payment sequence in each pay period. Leave this field blank if all pay sequence numbers are eligible to have these earnings calculated (i.e., 401(k) earnings to be added to all subject earnings regardless of Pay Seq#).

## Earnings Code: Department

If you want to override the standard
 Payroll department assigned to this employee in HR Resources, enter the appropriate PR
 department (from PR Departments) here. This field defaults from the Department
 field in HR Resources.

## Earnings Code: Ins Code

If you want an Insurance Code posted with
 these earnings, enter the appropriate insurance code (from HR Insurance Codes) here. This
 field is typically left blank for negative 401(k) type earnings. This field defaults from
 the Ins
 Code field in HR Resources.

##  Earnings Code: GL Co#

 Initially defaults the GL company defined for the HR company’s PR company. May be overridden.

## Earnings Code: Rate/Amount

Enter the appropriate rate or amount for this
 earnings code. The system checks to see what rate (old or new) to default from the HR
 Benefit Codes form based on the Effective Date field on the Info tab of
 this form.

Note: (For United States and Canadian users) If you are using negative earnings for pre-tax deductions, enter a negative amount.
Note: While you can set up salary reductions as negative earnings, it is recommended that you set up salary reductions as pre-tax deductions. For more information, see [Setting Up Pre-Tax Deductions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions).

## Earnings Code: Annual Limit Override

Enter 0.00 if not overriding the standard annual limit established for this earnings code (in PR Earnings Codes), or enter an amount as an override annual limit for this employee. If setting up for a 401(k) or Cafeteria Plan, this amount should be negative.

## Earnings Code: Freq

 Enter a valid frequency code (from HQ Frequency Codes) to indicate which automatic earnings will be active in the pay period.

##  Earnings Code: Override Std Hours

 Check this box to override the standard pay period hours specified in PR Pay Period Control when calculating benefits based on this earnings code. Override hours are entered to the right of this field.
 Leave this box unchecked to use the standard hours specified in the PR Pay Period Control program for the group and pay period.

##  Earnings Code: Hours

 Enter the number of hours to post for this earnings code. Entry here will override the standard hours specified for the payroll group and pay period in PR Pay Period Control.

## Earnings Code: Ready? Y/N

 Select this checkbox if this earnings information is ready to be updated to PR. When benefit information is updated to PR, these earnings will be updated to the employee’s automatic earnings (PR Automatic Earnings).
 Leave this checkbox unselected if this earnings information is not ready to be updated to PR.
Note: Update will include all earnings flagged as ready. Those earnings that are not flagged as ready can be updated at a later time.

## Effective Date

Effective Date field on the HR Resource Benefits form, ACA Coverage History tab
Defaults from the Effective Date
 field on the Info tab when:

- The benefit code in the Benefit
 Code field is defined as an ACA health plan in HR Benefit Codes,

- The Active checkbox in the Important
 Date Information section of the Info tab is selected, and

- A date is entered in the Effective
 Date field in the Important Date Information section of the Info tab.

To enter a date manually, enter the date that
 ACA coverage was effective date in MM/DD/YY format. Entering or editing a date in this
 field does not update the Effective Date field on the Info tab.

Related information

- [About the HR Resource Benefits form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-resource-benefits-form)

## Expire Date

Expire Date field on the HR Resource Benefits form, ACA Coverage History tab
Defaults from the Expiration Date
 field on the Info tab when:

- The benefit code in the Benefit
 Code field is defined as an ACA health plan in HR Benefit Codes.

- The Active checkbox in the Important
 Date Information section of the Info tab is selected, and

- A date is entered in the Expiration
 Date field in the Important Date Information section of the Info tab.

To enter a date manually, enter the date that
 ACA coverage expired, in MM/DD/YY format. Entering or editing a date in this field does not
 update the Expiration Date field on the Info tab.

Related information

- [About the HR Resource Benefits form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-resource-benefits-form)

## Notes

Notes field on the HR Resource Benefits form, ACA Coverage History tab
Defaults to "System Generated" when dates
 default into the Effective Date and Expire Date fields.
You can enter or edit notes in this field as desired as it is used for informational purposes only.

Related information

- [About the HR Resource Benefits form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-resource-benefits-form)

- [Effective Date](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-resource-benefits-form/field-definitions-hr-resource-benefits-form#ID-00010de9--en)

- [Expire Date](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-resource-benefits-form/field-definitions-hr-resource-benefits-form#ID-00010dfe--en)

## Series 2 Code

Series 2 Code drop-down on the HR Resource
 Benefits form, Info tab.
Select the code that represents the acceptance
 status for this resource. Status must have applied to this resource for one or more months
 of the calendar year. For detailed information each of the listed codes, see the
 Instructions for Forms 1094-C and 1095-C available from the IRS ([www.irs.gov](http://www.irs.gov/)).

- 2A - Employee not employed during the month

- 2B - Employee not a full-time employee

- 2C - Employee enrolled in coverage offered

- 2D - Employee in a section 4980H(b) Limited Non-Assessment Period

- 2E - Multi-employer interim rule relief

- 2F - Section 4980H affordability form W-2 safe harbor

- 2G - Section 4980H affordability federal poverty line safe harbor

- 2H - Section 4980H affordability rate of pay safe harbor

- 2I - Non-calendar year transition relief applies to this employee

Note: If you selected the Active check
 box and entered dates in the Effective Date and Expiration Date
 fields, upon saving the record, the system will create a record on the ACA History tab in
 HR Resources that includes the code specified here, along with the Effective/Expiration
 Dates.
