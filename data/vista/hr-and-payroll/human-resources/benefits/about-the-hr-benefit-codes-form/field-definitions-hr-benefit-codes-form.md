---
title: "Field Definitions: HR Benefit Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-benefit-codes-form/field-definitions-hr-benefit-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-benefit-codes-form/field-definitions-hr-benefit-codes-form"
---

# Field Definitions: HR Benefit Codes Form

The following is a list of field descriptions for the HR
 Benefit Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Benefit Code

 Enter a code, up to 10 characters, that
 uniquely identifies this benefit (e.g. 401K, Vac, Health Ins). Press F4 for a
 Benefit Codes Lookup form.

## Description

Description field on the HR Benefits Codes form, Benefits Options tab
Enter a description for this Benefit Code
 Option. This description provides a meaningful description in the Option
 Description fields on the Earnings Codes tab and the Deduction/Liability
 Codes tab of HR Benefit Codes.

Related information

- [Assigning Earnings, ACA, and Deduction/Liability Codes to Benefits](/en/vista/vista/hr-and-payroll/human-resources/benefits/assigning-earnings-aca-and-deductionliability-codes-to-benefits)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [Updating Resource Benefits System-Wide](/en/vista/vista/hr-and-payroll/human-resources/benefits/updating-resource-benefits-system-wide)

- [About the HR Benefit Codes Form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-benefit-codes-form)

##  Plan Name

 Enter the name of the benefit plan, up to 20 characters (e.g. Medical, Dental, Flex Spending).

##  Plan #

 Enter the plan number, up to 20 characters.

## Reporting Info

The Reporting Info text box on the HR Benefit Codes form, Info tab.
Use this text box to enter any miscellaneous notes about this
 benefit code. The space allowance is virtually unlimited.
Add a Standard NoteStandard notes allow you to insert frequently used
 text into some fields in the application. This text is created and maintained
 using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field, right click
 the mouse while focus is in the field and select Standard Notes from the shortcut menu,
 which opens the Standard Note Copy window. Then enter the standard note to copy
 (or select from F4 lookup) and click OK. The system inserts the selected note into the field.
Spelling Check Click the Spelling icon on the toolbar or select Tools Spelling  to spell check the text in this field.

##  Vendor

 Enter the vendor (from AP Vendors) that
 provides this benefit (e.g. Blue Cross, Prudential, Merrill Lynch). This is the vendor to
 which liabilities are to be paid when initialized from PR to AP.

##  Address

 Enter the address for the benefit provider (vendor) indicated above. Initially defaults the
 address specified for the vendor in AP Vendors.
 This is informational only, and is typically used as a reference when corresponding with the benefit plan administrator.
Note: If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default Country
 specified in HQ Company Setup.

##  City

 Initially defaults from the AP Vendors for the above-mentioned vendor. May be overridden.
Note: If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default Country
 specified in HQ Company Setup.

## State

Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
Note: If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default Country
 specified in HQ Company Setup.

##  Zip

 Initially defaults from the AP Vendors for the above-mentioned vendor. May be overridden.
Note: If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default Country
 specified in HQ Company Setup.

##  Country

 Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.
Note: If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default Country
 specified in HQ Company Setup.

##  Contact

 Enter the contact for the benefit provider, up to 20 characters. Typically, this will be the benefit plan administrator.

##  Phone

 Enter the contact’s phone number, up to 20 characters.

##  Fax

 Enter the contact’s fax number, up to 20 characters.

## Update PR

 Select this checkbox to update deductions, liabilities, and earnings related to this benefit to PR. May be overridden by resource in HR Resource Benefits.
 Leave this checkbox unchecked if deductions, liabilities, and earnings related to this benefit should not be updated to PR.
About Update PR
This option determines whether or not the benefit code defined for a resource (including earnings, deductions, and liabilities) will be updated to PR when running the HR Update Benefit/Salary to PR program. If this checkbox is selected, the Ready Y/N checkbox is selected in HR Resource Benefits, and both the employee and benefit code are included in the selection criteria in HR Update Benefit/Salary to PR, earnings will be updated to PR Automatic Earnings, and deductions and liabilities will be updated to PR Employee Deductions/Liabilities.
When running the HR to PR update, there are certain conditions or criteria that determine the benefits eligible for update to PR:

- The HR company equals the active company (specifically, the company you are working in). The update includes only resources/benefit codes for the currently active HR company.

- The update only includes benefits for the resource
 (the Dependent Seq#field is set to zero); dependent benefits are not
 updated.

- The effective date specified for the resource (Effective Date field) is less than or equal to the date specified in HR Update Benefit/Salary to PR (Effective Date field).

- The benefit has not been updated to PR; that is, the Updated Y/N box is unchecked (HR Benefit Codes, Earnings Codes or Deduction/Liability Codes tabs).

Note: The system checks this box once the benefit is updated to PR; however, if subsequent changes are made to the benefit, the system will uncheck this box.

- The Exists in PR display box is
 checked and an employee number is specified in PR Empl
 # (HR Resources, Payroll Info tab).

- The resource/benefit does not exist in another batch.

Note: If a benefit is determined eligible, the update of earnings, deductions, and liabilities is determined as follows:

- If the deduction or liability is employee based, it must have a processing sequence in order to be updated. Deductions and liabilities that are not employee-based do not require a processing sequence.

- Earnings, deductions, and liabilities must be flagged as 'ready' for update. If the Ready flag is set to N, the earnings code, deduction, or liability will be skipped.

##  Eligibility Basis

 Indicate the time basis applicable to the Eligibility Period. This will be used in conjunction with the Eligibility Period to indicate how long an employee has to work before being qualified for the benefit.

- Days – Select this option if employees must work a specified number of days (indicated to the right) to be eligible for the benefit.

- Months – Select this option if employees must work a specified number of months (indicated to the right) to be eligible for this benefit.

- Years – Select this option if employees must work a specified number of years (indicated to the right) to be eligible for this benefit.

- Blank – There are no eligibility requirements for this benefit plan.

##  Eligibility Period

 Disabled if Eligibility Basis is blank.
 Specify the number of Days, Months, or Years (depending on the Eligibility Basis specified above) that an employee must work before they become eligible for this benefit plan.

## Health Plan

Health Plan field on the HR Benefits Codes form, ACA section
Select this checkbox to designate this benefit code as an Affordable Care Act (ACA) health plan.

Related information

- [Assigning Earnings, ACA, and Deduction/Liability Codes to Benefits](/en/vista/vista/hr-and-payroll/human-resources/benefits/assigning-earnings-aca-and-deductionliability-codes-to-benefits)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [Updating Resource Benefits System-Wide](/en/vista/vista/hr-and-payroll/human-resources/benefits/updating-resource-benefits-system-wide)

- [About the HR Benefit Codes Form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-benefit-codes-form)

## Minimum Essential Coverage

Minimal Essential Coverage field on the HR Benefits Codes form, ACA section
Available if the Health Plan
 checkbox is selected.
Select this checkbox to designate that this benefit code refers to a health plan that conforms to minimum essential coverage (MEC), as per the Affordable Care Act (ACA).

Related information

- [Assigning Earnings, ACA, and Deduction/Liability Codes to Benefits](/en/vista/vista/hr-and-payroll/human-resources/benefits/assigning-earnings-aca-and-deductionliability-codes-to-benefits)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [Updating Resource Benefits System-Wide](/en/vista/vista/hr-and-payroll/human-resources/benefits/updating-resource-benefits-system-wide)

- [About the HR Benefit Codes Form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-benefit-codes-form)

## Self Insured

Self-Insured checkbox on the HR Benefits Codes form, ACA section
Available if the Health Plan
 checkbox is selected.
Select this checkbox to designate this health
 plan as self-insured, as per Affordable Care Act (ACA) definitions.

Related information

- [Assigning Earnings, ACA, and Deduction/Liability Codes to Benefits](/en/vista/vista/hr-and-payroll/human-resources/benefits/assigning-earnings-aca-and-deductionliability-codes-to-benefits)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [Updating Resource Benefits System-Wide](/en/vista/vista/hr-and-payroll/human-resources/benefits/updating-resource-benefits-system-wide)

- [About the HR Benefit Codes Form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-benefit-codes-form)

## Option

Option field on the HR Benefits Codes form, Benefits Options tab
Enter a Benefit Code Option number to uniquely identify this benefit option.

Related information

- [Assigning Earnings, ACA, and Deduction/Liability Codes to Benefits](/en/vista/vista/hr-and-payroll/human-resources/benefits/assigning-earnings-aca-and-deductionliability-codes-to-benefits)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [Updating Resource Benefits System-Wide](/en/vista/vista/hr-and-payroll/human-resources/benefits/updating-resource-benefits-system-wide)

- [About the HR Benefit Codes Form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-benefit-codes-form)

##  Description

 Enter a description of the benefit code, up to 30 characters.

## ACA Coverage

ACA Coverage field on the HR Benefits Codes form, Benefits Options tab
Select an ACA coverage type: Self,
 Self + Spouse, Self + Dependents, or Self + Family.

Related information

- [Assigning Earnings, ACA, and Deduction/Liability Codes to Benefits](/en/vista/vista/hr-and-payroll/human-resources/benefits/assigning-earnings-aca-and-deductionliability-codes-to-benefits)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [Updating Resource Benefits System-Wide](/en/vista/vista/hr-and-payroll/human-resources/benefits/updating-resource-benefits-system-wide)

- [About the HR Benefit Codes Form](/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-benefit-codes-form)

## Benefit Options: Notes

Enter notes for the Benefit Code option.

##  Earnings Codes: Earning Code

 Enter a valid earnings code to associate with this benefit.

##  Earnings Codes: Option

 Required field.
 Enter a benefit code option. This value must be numeric. You can apply multiple options to a benefit code to define multiple rates. For example, you might define a three-tiered 401(k) plan, each level having a different rate.

##  Earnings Codes: Frequency

 Required field.
 Specify a valid frequency code (from HQ Frequency Codes) to identify the processing frequency for this earnings code (e.g., always, weekly, monthly, yearly, etc.).

##  Earnings Codes: Old Rate

 If this is a new benefit, this rate defaults to 0.00.
 Enter the rate that was in effect prior to the New Rate and Effective Date.

##  Earnings Codes: New Rate

 If this is a new benefit, this rate defaults to 0.00.
 Enter the new rate.

##  Earnings Codes: Effective Date

 Enter the date the New Rate takes effect.

## Updated YN

This checkbox defaults to blank when entering a new earnings code. Once you update the benefit code to HR Resource Benefits, the system selects this checkbox.
If you are making change to an existing code, uncheck this box to have the system update HR Resource Benefits when you process HR Benefit Update.
Check this box to prevent the system from updating HR Resource Benefits with this benefit.

##  Deduction/Liability Codes: DL Code

 Enter a valid deduction and/or liability code to associate with this benefit.

##  Deduction/Liability Codes: Option

 Required field.
 Enter a benefit code option. This value must be numeric. You can apply multiple options to a benefit code to define multiple rates. For example, you might define a medical plan with three coverage levels, each one having a different rate.

## Deduction/Liability Codes: Frequency

Optional field.
Specify a valid frequency code (from HQ Frequency Codes) to identify the frequency at which this deduction or liability will be processed (i.e. always, weekly, monthly, yearly, etc.). You must assign the deduction or liability a Calculation Category of ‘E-Employee’ or ‘A-Any’ in PR Deductions/Liabilities.
Note: When you add a benefit for a resource in HR Resource
 Benefits (either manually or via initialization), the system will check the Employee-Based
 box for all deductions and liabilities.

##  Deduction/Liability Codes: Old Rate

 If this is a new benefit, this rate defaults to 0.00.
 Enter the rate that was in effect prior to the New Rate and Effective Date.

##  Deduction/Liability Codes: New Rate

 If this is a new benefit, this rate defaults to 0.00.
 Enter the new rate.

##  Deduction/Liability Codes: Effective Date

 Enter the date the New Rate takes effect.

## Deduction Liability: Updated YN

This checkbox defaults to blank when entering a new deduction/liability code. Once you update the benefit code to HR Resource Benefits, the system selects this checkbox.
If you are making change to an existing code, uncheck this box to have the system update HR Resource Benefits when you process HR Benefit Update.
Check this box to prevent the system from updating HR Resource Benefits with this benefit.
