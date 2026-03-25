---
title: "Field Definitions: PR State Information Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-state-information-form/field-definitions-pr-state-information-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-state-information-form/field-definitions-pr-state-information-form"
---

# Field Definitions: PR State Information Form

The following is a list of field descriptions for the PR
 State Information form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  State

 Enter a valid state code (HQ States).

## Tax ID#

The Tax ID# field on the PR State Information form, Info tab.
Enter the Tax Identification Number, up to 20 characters (including dashes).
When running the W-2 programs, the Tax ID#, by requirement, is entered without the dashes.
 The system will put them in automatically, but since the placement of numbers and dashes
 may vary for each state, the system does not know where to put the dashes unless specified
 here in this form.
Note: (For the State of Georgia) Use this field to enter the 9-digit State Control Number-Withholding Number.

##  Tax Dedn

The Tax Dedn field on the PR State Information form, Info tab.
Enter a state income tax deduction code.
If there is no income tax for the state, you may leave this field blank.

## Calculate Tax Option

The Calculate Tax Option field on the PR State Information form, Info tab.
This option controls state income tax calculations and applies to the state income tax deduction only.

- Posted Only - Calculate tax for the posted state only, regardless of the employee's resident state. If the posted state and resident state are different, the posted state will be the work state when no reciprocal agreement (defined in HQ States) exists between the work and resident states. Otherwise it will be the resident state.

- Full Tax for Both Posted and
 Resident when No Reciprocity - Calculate tax for both the posted
 and resident state, but only when no reciprocal agreement exists between the
 states. If a reciprocal agreement exists, calculate only the resident state
 tax.Note: This option is not valid for the state of
 Alabama. Alabama does not require withholding of income tax from a resident
 working out of state when the employer is withholding tax for the state in
 which the employee is working.

- Both with Difference to Resident - Calculate tax for both the posted state and resident state, if the posted and resident states are different. If the resident state tax is higher than the posted state tax, the full amount of the posted tax is deducted, but only the difference is deducted for the resident state. For example, if the posted state tax = $100 and the resident state tax = $125, $100 is deducted for the posted state and $25 is deducted for the resident state.Note: With this option, the resident state deduction Subject and Eligible amounts are set to 0.00.
If the posted state tax is higher than the resident state tax, then deduct the full amount of posted tax, but do not deduct resident state tax. Using the example above, if the posted state tax = $125 and the resident state tax = $100, $125 is deducted for the posted state and 0.00 tax is deducted for the resident state

## Accumulate Subject Earnings in Resident State

The Accumulate Subject Earnings in Resident State checkbox on the PR State Information form, Info tab.
The system enables this checkbox when you select the Both with Difference to Resident calculate tax option.
Select this checkbox to include amounts earned in a non-resident state in the subject amount for the employee's resident state.
If this checkbox is not selected, the system excludes amounts earned in a non-resident state in the subject amount for the employee's resident state.

## Unemployment ID#

 Displays for United States users only
 (Default
 Country field set to US in HQ Company Setup).
This field initially defaults to the Tax ID# (specified above). If a separate ID# is required for reporting unemployment information, enter the ID#, up to 20 characters. Check with your state to determine what format to use when entering the ID #.

### Florida Users

The Unemployment ID for Florida is a seven
 digit number. When entering the number, omit any check digits that may have been added.
 For example, the “-2” in 2113652-2.

##  SUTA Liability

 Displays for United States users only
 (Default
 Country field set to US in HQ Company Setup).
 Enter the liability code for State Unemployment. This must be a valid liability code set up in PR Deductions/Liabilities.

## Accumulate with SUTA Liability

 Displays for United States users only
 (Default
 Country field set to US in HQ Company Setup).
Select how accumulations should be made for State Unemployment from the following choices:

- Hours Worked

- Weeks Worked

- None

Note: If you select the Weeks Worked option, weeks will accrue only for employees posted to Pay Seq #1. If tracking SUTA based on 'weeks worked', subject weeks will be reported only for employees accruing under Pay Seq #1.

## Exclude Out-of-State SUTA Wages

Displays for United States users only
 (Default
 Country set to US in [HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)).
Select this checkbox to exclude out-of-state wages from SUTA eligible wages during payroll processing.

## Contact

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
Enter the name or title, up to 30 characters, of the individual in your company responsible for preparing Unemployment/Wage reports, up. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.
Note: Florida requires this field when generating electronic unemployment files.

## Phone/Ext.

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 Enter the phone number (up to 15 digits) and extension number (up to 5 digits), at which the contact specified above can be reached. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.
Note: Florida requires this field when generating electronic unemployment files.

## Email

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
Required for the state of Florida.
Enter the contact’s email address.
Note: Florida requires this field when generating electronic unemployment files.

## Transmitter ID#

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 Enter the media transmitter or authorization number, up to 10 characters, assigned to you by the State. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.
Iowa Users - Use this field to enter the Iowa Business eFile Number (BEN).

##  Establishment ID#

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 Enter the establishment identification number, up to 4 characters. This ID# may be used to designate various store or factory locations or types of payroll when a file contains multiple records with the same EIN#. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.

## C-3 Data

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
Enter the 1 character defined by the states requiring this information. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.

## Suffix Code

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 Enter the 5 characters that have been defined by the states requiring this information. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.

##  Tax Type

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 Enter the 1 character defined by the states requiring this information. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.

## Taxing Entity

This field is available only when the Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
Enter the 10 characters defined by the states
 requiring this information. This information is used by the ICESA (Interstate Conference
 of Employment Security Agencies) format.

##  Document Control ID#

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
Enter the 10 characters defined by the states requiring this information. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.

## Plant #

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 If applicable, specify the plant code (up to 2 characters) as defined by state.

## Branch

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 If applicable, specify the branch code (up to 3 characters) as defined by state.

## Private Disability Plan ID #

The Private Disability Plan ID # field on the PR State Information form, Unemployment/Wage Reporting tab.
 This field is available only when the Default Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
Currently used for New Jersey only.
Enter the private disability plan number, as defined by the NJ Department of Labor.
Entry in this field is informational only; this number is not included in the efile generated via PR Generate W-2 eFile. If you are using Aatrix to electronically file W-2s, you must manually enter this number in the Aatrix wizard; it is not passed from Vista. For more information, see [File W-2s Using Aatrix](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/file-w-2s-using-aatrix#task-4096--en__NJ_PrivateDis_PrivateFamLeave).
Note: Private Disability amounts will print in the Box 14 sections of the Vista PR W2 Preview Report and PR W2 Employee Copies report (Copy 2 section). However, the Private Disability Plan ID # is not included these reports.

## State Control #

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 The input needed for this 7-character field is defined by the states requiring this information. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.

## State ID#

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 Enter the 2-digit Federal postal code assigned to the State specified above. This is NOT the 2-character postal abbreviation.

## Unit ID#

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 The input needed for this 5-character field is defined by the states requiring this information. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.

## County

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 The input needed for this 3-character field is defined by the states requiring this information. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.

## Out of County

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 The input needed for this 7-character field is defined by the states requiring this information. Used by the ICESA (Interstate Conference of Employment Security Agencies) format.

## Local Code 1

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 Currently used only for New York City unemployment wage reporting.
 Enter the local code assigned for the New York City tax (in [PR Local Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-local-codes-form)). The description for this local code will be used as the field label for the corresponding tax withholding field in the PR Unemployment Employees form.

## Local Code 2

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 Currently used only for the City of Yonkers unemployment wage reporting.
 Enter the local code assigned for the Yonkers city tax (in [PR Local Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-local-codes-form)). The description for this local code will be used as the field label for the corresponding tax withholding field in the [PR Unemployment Employees](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/unemployment/about-the-pr-unemployment-employees-form) form.

## Local Code 3

 Unused at this time.

## DL Code 1 & 2

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
Currently used only for New Mexico workers compensation reporting.

- In DL Code 1, enter the deduction for
 workers compensation.

- In DL Code 2, enter the liability for
 workers compensation.

- If workers compensation is not applicable for a particular employee, enter zero (0) into both fields.

You must also add these codes to the
 DL
 Code field on the Add’l State Based Dedns/Liabs tab.
Note: These fields need to be set at the end of the month.

## Wage Plan

 This field is available only when the
 Default
 Country ([HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)) is set to US.
 Enter the 1-character wage plan code. This
 field automatically updates the Wage Plan Code field on [PR Unemployment Employees](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/unemployment/about-the-pr-unemployment-employees-form).

## DL Code

 Enter any additional deductions and liabilities that need to be calculated for the state. The type, description, and method display in the grid to the right.
New Mexico Users - If you entered a code for workers compensation reporting in the DL Code 1 and DL Code 2 fields, you must also add the codes to this grid.

## Based On

Determines whether the subject amount for the deduction or liability is calculated the same as the Income Tax or Unemployment.

- T - Earnings on all timecards subject to withholding
 tax for this state will also be subject to this deduction/liability.

- U - Earnings on all timecards subject to unemployment for this state will also be subject to this deduction/liability.

## Always calc for resident

The Always calc for resident checkbox on the PR State
 Information form, Add'l State Based Dedn/Liabs tab.
Enabled only for state-based deduction codes.

Select this checkbox to always calculate this deduction for state residents, even when they work in another state.
Note: For the state of Oregon, selection of this checkbox is required for Oregon statewide transit tax deduction codes.

Related concepts

- [PR State Information Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-state-information-form)
