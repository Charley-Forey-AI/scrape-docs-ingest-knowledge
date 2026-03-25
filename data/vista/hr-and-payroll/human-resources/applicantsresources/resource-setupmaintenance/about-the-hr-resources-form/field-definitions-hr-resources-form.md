---
title: "Field Definitions: HR Resources Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form"
---

# Field Definitions: HR Resources Form

The following is a list of field descriptions for the HR
 Resources form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  HR Resource #

 Enter a resource number, up to 6 digits, that identifies this employee/applicant or enter ‘+’ to have the system automatically assign the next sequential number.
Note: If the system determines that the next value exceeds
 the maximum value allowed (999999), you will receive a message that you must manually enter
 a number lower than the maximum.
 If accessing an employee that was initialized
 from PR, the resource number may differ from the PR Employee number, depending on
 assignment during initialization. During initialization, the system will assign the
 resource number to be the same as the PR Employee number, unless the number was found to
 exist in HR Resources for another employee/resource. In which case, the resource number
 would have been assigned using the next sequential number based on the highest existing
 resource number.
Note: This same rule applies when initializing HR resources
 to PR.
Note: If you are trying to find an employee’s record and do
 not know the employee’s number, you can enter the sort name to locate the employee. Once
 the sort name is entered, the program will find the first alphabetical occurrence of the
 entry and default that employee’s record. For example, if you have employees SMITHE,
 SMITHERS, and SMITHSON, and you enter SMITH as the sort name, the program will pull up
 employee SMITHE.

##  Name: Last

 Enter the last name of this employee/applicant, up to 30 characters. This name will print on checks, reports, and W-2s.
 If you initialized this employee from PR, this field defaults the last name specified for this employee in PR Employees. May be overridden.
Note: Changes to the employee’s last name will be updated to PR Employees automatically if the Name update option is checked in HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

##  Name: First

 Enter the first name of this employee/applicant, up to 30 characters. This name will print on checks, reports, and W-2s.
 If you initialized this employee from PR, this field defaults the first name specified for this employee in PR Employees.
Note: Changes to the employee’s first name will be updated to PR Employees automatically if the Name update option is checked in HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

##  Name: Middle

 Enter the middle name or initial of this employee/applicant, up to 15 characters. This name will print on checks, reports, and W-2s.
 If you initialized this employee from PR, this field defaults the middle name or initial specified for this employee in PR Employees.
Note: Changes to the employee’s middle name/initial will be updated to PR Employees automatically if the Name update option is checked in HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

##  Name: Suffix

 Enter the suffix (e.g. Sr., Jr., III, etc.) for this employee/applicant, up to 4 characters.
Note: Changes to the employee’s suffix will be updated to PR Employees automatically if the Name update option is checked in HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

##  Name: Sort

 This field defaults to the first 15 characters of the resources’s last name. If the last name is less than 15 characters, the system adds characters from the employee’s first name, up to the 15-character limit for the field. You can change the default as necessary. You can enter sort names in upper and/or lower case, but are always converted to uppercase letters.
Note: Changes to the employee’s sort name will be updated to PR Employees automatically if the Name update option is checked in HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

##  Marital Status

 Indicate this employee’s marital status.
 S = Single
 M = Married
 D = Divorced
 O = Other

##  Maiden Name

 For married or divorced female employees, enter the maiden name, up to 20 characters.

##  Spouse Name

 Enter the name of this employee’s spouse (if applicable), up to 30 characters.

##  Address

 Enter the address of this employee/applicant, up to 60 characters. This address will print on checks, reports, and W-2s.
 If you initialized this employee from PR, this field defaults the address specified for this employee in PR Employees.
Note: If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default Country
 specified in HQ Company Setup.
Note: Changes to the employee’s address will be updated to
 PR Employees automatically if the Address update option is checked in HR Company Parameters
 and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

##  City

 Enter the resident city of this employee/applicant, up to 30 characters. This city will print on checks, reports, and W-2s.
 If you initialized this employee from PR, this field defaults the City specified for this employee in PR Employees.
Note: If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default Country
 specified in HQ Company Setup.
Note: Changes to the employee’s address will be updated to
 PR Employees automatically if the Address update option is checked in HR Company Parameters
 and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

##  State

 Enter the resident state (as defined in HQ States) of this employee/applicant. This state prints on checks, reports, and W-2s. The system validates the state based on the Default Country specified in HQ Company Parameters for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
 If you initialized this employee from PR, this field defaults the State specified for this employee in PR Employees.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.
Note: Changes to the employee’s address will be updated to PR Employees automatically if the Address update option is checked in HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

##  Zip Code

 Enter the zip code of this employee/applicant, up to 12 digits. This zip code will print on checks, reports, and W-2s.
 If you initialized this employee from PR, this field defaults the Zip code specified for this employee in PR Employees.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.
Note: Changes to the employee’s address will be updated to PR Employees automatically if the Address update option is checked in HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

## Country

Enter the 2-character country code for this employee/applicant. This country will print on checks, reports, and W-2s. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Setup for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.
If you initialized this employee from PR, this field defaults the Country code specified for this employee in PR Employees.
Note: If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default Country
 specified in HQ Company Setup.
Note: Changes to the employee’s address will be updated to
 PR Employees automatically if the Address update option is checked in HR Company Parameters
 and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

##  Additional Address

 Use this field to enter additional address information for this employee/applicant. For example, if the employee/applicant receives his/her mail at a P.O. Box, then you might enter the P.O. Box in the Address field above, and use this field to enter the street address.
 The address information entered here is not used by any of the posting programs, but may be used on certain reports.

## Phone

Enter the employee/applicant’s phone number, up to 20 characters.
If you initialized this employee from PR, this field defaults the Phone specified for this employee in PR Employees.

##  Work

 Enter the employee/applicant’s work phone number, up to 20 characters.

##  Pager

 Enter the employee/applicant’s pager number, if applicable, up to 20 characters.

## Cell

Enter the employee/applicant’s cell phone number, if applicable, up to 20 characters.
If you initialized this employee from PR, this
 field defaults from the Cell field for this employee in PR
 Employees.

## Work Email

The Work Email field on the HR Resources form, Info
 tab.
If the resource has a work email address, enter it here. This
 field is intended as an alternative to the Email field, which is
 often used for employee-specific email notifications (like onboarding items,
 paystubs, and tax forms), that the person may prefer to receive at a
 personal email account.
There is also a synchronization option with the Work Email field in
 the PR Employees form. If the company uses the HR module and the Address box is
 checked in the PR Update
 Options section of the HR Company Parameters form, then
 the work email in the PR Employees form is automatically updated with the
 new value.

##  Race

 Required if this employee will be added (or initialized) to PR.
 Enter the race code (from PR Race Codes), that identifies this employee/applicant’s race. Used for Equal Employment Opportunity reports.
 If you initialized this employee from PR, this field defaults the Race specified for this employee in PR Employees.
Note: Changes to the employee’s race will be updated to PR Employees automatically if the Name update option is checked in HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

##  Birth Date

 Enter the employee/applicant’s birth date (e.g. 10/04/1956).
 If you initialized this employee from PR, this field defaults the Birth Date specified for this employee in PR Employees.
Note: Changes to the employee’s birth date will be updated
 to PR Employees automatically if the Name update option is checked in HR Company Parameters
 and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

## Gender Identity

The Gender Identity drop-down on the HR Resources form, Info tab.

Select this resource's gender identity.

- M-Male

- F-Female

- X-Non-Binary

- O-Other (enables the text box to the right for entering the gender description)

Note: Gender Identity classifications are not currently used for EEO reporting. Use the Reporting Gender field to assign this resource's gender for EEO reporting purposes.

Note: Changes to the resource’s gender information will be updated to PR Employees automatically if the Name update option is selected in HR Company Parameters and the employee’s Active PR Employee and Exists in PR checkboxes are selected in HR Resources.

## Description

The Description field (unlabeled) on the HR Resources form, Info tab.
This field is enabled only when the Gender Identity drop-down is set to O-Other.
Enter a description of the resource's gender (for example, Agender, Androgyne, Bigender, etc.).
Note: Changes to the resource’s gender information will be updated to PR Employees automatically if the Name update option is selected in HR Company Parameters and the employee’s Active PR Employee and Exists in PR checkboxes are selected in HR Resources.

##  Reporting Gender

The Reporting Gender field on the HR Resources form, Info tab.
 Indicate whether this resource/applicant will be reported as male or female on Equal Employment Opportunity reports.
 If you initialized this resource from PR, this field defaults the gender specified for the employee in PR Employees.
Note: Changes to the resource’s gender information will be updated to PR
 Employees automatically if the Name update option is selected in HR Company Parameters and
 the employee’s Active PR Employee and Exists in PR options are set to Y (selected).

##  Employment Status

 Required.
 Enter this resource’s employment status (defined in HR Status Codes).
Note: If the status entered here is flagged to ‘Update
 Employment History’ (in HR Employment Status), adding or removing the status for this
 resource will create an employment history record in HR Resource Employment History.

##  PR Co#

 Enter the Payroll company to which this resource is assigned. If the resource’s status is “Applicant”, this field should be left blank.
 If this employee was initialized from PR, this field defaults the PR company assigned to the employee in PR Employees.
Note: Although you are not required to enter a Payroll company when setting up a resource, you must assign a Payroll company before you initialize a resource to Payroll (in HR Initialize PR Employees).

## SSN#

Required if: this resource will be
 added (or initialized) to PR or if you enter a number in the PR Empl #
 field.
Enter the employee/applicant’s social security number.
If you initialized this employee from PR, this field defaults the SSN specified for this employee in PR Employees.
Note: Changes to the employee’s social security number will
 be updated to PR Employees automatically if you check the Social Security
 Number box in HR Company Parameters (PR Update Options section) and you have
 checked the Active
 PR Employee and Exists in PR boxes in HR Resources
 (Payroll Info tab).
Click [here](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#ID-00052407--en) for the field definition for Australian users.
Click [here](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#ID-000523fa--en) for the field definition for Canadian users.

## SIN

The SIN field on the HR Resources form, Info
 tab.
This field is for Canadian users only.
Required if: this resource will be added (or
 initialized) to PR or if you enter a number in the PR Empl # field.
Enter the employee/applicant’s Social
 Insurance Number (SIN). The system will validate that the number you enter is unique and is
 a valid number. However, it is unable to verify that this is the correct number for the
 specific employee.
If you initialized this employee from PR, this field defaults the SIN specified for this employee in PR Employees.
Note: Changes to the employee’s social insurance number will be
 updated to PR Employees automatically if you check the Social Security Number box in HR Company
 Parameters (PR Update Options section) and you have checked the Active PR
 Employee and Exists in PR boxes in HR Resources
 (Payroll Info tab).

## TFN

TFN field on the HR Resources form, Info tab.
This field is for Australian users only.
Required if: this resource will be added (or
 initialized) to PR or if you enter a number in the PR Empl # field.
Enter the employee/applicant’s tax file number (TFN) in the proper format (###-###-###). If dashes are not entered, they are automatically provided.
You can also enter the following duplicate numbers, if meeting the associated criteria:

- 333-333-333 - For payees under 18 years of age and earning $122 or less per week.

- 444-444-444 - For payees who are Commonwealth Government Pensioners.

- 111-111-111 - For new payees who have not made a TFN declaration, and 28 days have not passed.

- 000-000-000 - For payees who choose not to quote a TFN and has not claimed an exemption, or does not fit into any of the other categories.

If you initialized this employee from PR, this field defaults the TFN specified for this employee in PR Employees.
Note: Changes to the employee’s tax file number will be updated to
 PR Employees automatically if you check the Social Security Number box in HR Company
 Parameters (PR Update Options section) and you have checked the Active PR
 Employee and Exists in PR boxes in HR Resources
 (Payroll Info tab).

##  PR Employee #

 Enter this resource’s PR employee number. If employee was initialized from PR, defaults the employee number assigned in PR Employees.
 If this resource does not yet exist in PR, but will be added using the “Add to PR” button, entry in this field is required. Number may be the same as the HR Resource number, as long as the number does not already exist in PR for another employee.
 If the resource’s status is ‘Applicant’, this field should be left blank.

##  Position Code

 Enter the
 code (defined in HR Position Codes) that identifies the position to which this employee is
 currently assigned or leave blank if not applicable. Changes to this code will generate an
 entry in the HR Employment History table.
Note: Changes to a resource’s position code in HR Resource
 Salary History will be updated here if you answer ‘Yes’ to the ‘Update Position Code in HR
 Resources?’ prompt.

##  Active PR Employee

 If this resource was initialized from PR and the Active flag in PR Employees is checked, this box will automatically be checked.
 Check this box if this resource is an active PR employee. Must be checked if this is a new resource and you will be adding/initializing the resource to PR.
 Do not check this box if the resource is an inactive PR employee. A bold message in red displays in the header section of this form for inactive employees.

- Changes to this resource’s ‘active’ status will be updated to PR Employees automatically if the Active Flag update option is checked in HR Company Parameters and the resource’s Exists in PR options are set to Y (checked).

- If you change this resource's status to 'inactive' and do not enter a termination date, upon saving the record, you will receive a message warning you that the resource has been changed to 'inactive' without specifying a termination date, and asking if you want to continue. Answer Yes to save the record without the termination date, no to abort the save.

- If you change this resource's status to 'Inactive' and auto earnings have been set up for the employee, a message displays indicating that the employee has been changed to inactive and asking if you want to delete the auto earnings setup for the employee. Click Yes to delete the auto earnings setup, No to leave them intact. (Note: If you elect to delete auto earnings, they will not be deleted from HR, they will only be deleted from PR.)

##  Temp Worker

The Temporary Worker checkbox on the HR Resources form,
 Payroll Info tab.

 Select this checkbox if this employee was hired on a temporary status.
 Leave this checkbox unselected if this employee is a full-time permanent employee.

##  Exists in PR

 Display only, indicating whether the resource exists as an employee in PR Employees.
 Defaults as checked if the resource was
 initialized from PR or added to PR from HR by clicking the Add to PR
 button. Otherwise, defaults as unchecked.

##  Non Resident Alien

 Check this box if this employee is a non-resident alien (i.e. an alien who does not meet either the green card test or substantial presence test as defined by the IRS).
Leave this box unchecked if this employee is a resident alien (i.e. meets the green card or substantial presence tests).

##  Overtime

 Select an
 overtime calculation option for this Employee:

- N-None – No overtime is
 calculated, employee is exempt.

- D-Daily – Always calculate
 overtime for this employee on a daily basis using the OT Schedule specified. Overtime
 also calculated if 40 hours per week is exceeded.

- W-Weekly – Calculate overtime
 on a weekly basis only (more than 40 hours per week).Note: Weekly OT is applied
 after all of the daily OT calculations are complete.

- C-Craft – Overtime is based
 on the craft and craft template that this employee works under. If the craft or craft
 template has been assigned an OT Schedule, then the daily “rules” at either of those
 levels is used. All of an employee’s time posted to the craft for the day is
 accumulated to see if overtime should be calculated. If different OT rules apply to
 the various templates that this employee has worked under, the order of timecard
 entry determines which jobs and how much OT is calculated. Weekly OT is applied after
 all of the daily OT calculations are complete.

- J-Job – Overtime is calculated
 based on the OT Schedule assigned to the job in the JC Jobs. If two jobs are assigned
 the same overtime schedule, the jobs will be combined when calculating overtime. If
 you want to process overtime independently for each job, you will need to assign
 different overtime schedules to each job.

- P-Posting Seq - This method provides another option for calculating daily overtime and applies to organizations who must adhere to both craft overtime rules and job overtime rules. Overtime is calculated only after considering all posting sequences (timecard lines) in each day and applying overtime schedule rules on a line-by-line basis, from top to bottom. The system considers overtime schedules from the job/project, the job's craft template, and the craft master.
If on a single line, the system encounters more than one overtime schedule that could apply to that line, it applies the schedule that is more generous.
Important:The order that you enter timecard lines in the PR Timecard Entry form matters.Because the system applies overtime schedule rules starting with the top timecard line and working toward to bottom line, a continuous, daily overtime calculation such as this that crosses jobs, crafts, and craft templates means the order that you enter timecard lines can affect how the system calculates wages and attributes those costs to jobs. You may encounter scenarios where if the timecard line entries are reversed, the wages are different.
Here's a brief video demonstrating the results of this setting.
Note: You must use a browser on your local computer to view this video, and not a browser in the cloud. If you are currently using a cloud-based browser, copy this page's URL and paste it into a web browser on your local computer.

Note: Changes to this field update the
 Overtime field in PR Employees form (Add’l Info tab) for this
 employee.

##  W-4 / TD1 / PAYG Completed

This field is informational only.
United States
For US companies, this field displays as W-4 Completed.
Check this box if this employee has completed their W-4 forms and/or if W-4 information has been entered for this employee on the Filing Status grid.
 Leave this box unchecked if this employee has not completed their W-4 forms and/or if W-4 information has not been entered for this employee on the Filing Status grid.
Australia
For Australian companies, this field displays as PAYG Completed.
Check this box if this employee has completed their withholding forms (NAT 3092, NAT 3093, and/or NAT 0929) and/or if withholding information has been entered for this employee on the Filing Status grid.
 Leave this box unchecked if this employee has not completed their withholding forms (NAT 3092, NAT 3093, and/or NAT 0929) and/or if withholding information has not been entered for this employee on the Filing Status grid.
Canada
For Canadian companies, this field displays as TD1 Completed.
Check this box if this employee has completed their TD1 forms and/or if TD1 overrides/claim amounts have been entered on the Filing Status grid.
Leave this box unchecked if this employee has not completed their TD1 forms and/or if TD1 overrides/claim amounts have not been entered for this employee on the Filing Status grid.
Note: If you override the claim amount for an employee, you will need to maintain the claim amount on a yearly basis, as the system does not automatically update it.

## Federal Tax Exempt (US)

(United States) The Federal Tax Exempt checkbox on the HR Resources form, Add'l Info tab.

Select this checkbox if this resource is exempt from Federal tax withholding. When processing payroll for the employee, the system calculates a zero amount for Federal withholding.
Note: Selecting this checkbox overrides any calculation override rate/amount you set up for the employee / Federal withholding deduction code in PR Employees.

Leave unselected (default) if this resource is subject to Federal tax withholding.
Note: If the W4 Info checkbox is selected in HR Company Parameters (PR Update Options section), changes to this checkbox are automatically updated to the Federal Tax Exempt checkbox in PR Employees (Add'l Info tab). If the W4 Info checkbox is not selected, you must manually update this flag in both forms.

##  Hire Date

 Enter the employee’s hire date (e.g. 01/01/99).
 If you initialized this employee from PR, this field defaults the Hire Date specified for this employee in PR Employees.
Note: Changes to the employee’s hire date will be updated to
 PR Employees automatically if the Hire/Term Date update option is checked in HR Company
 Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y
 (checked).

##  Term Date

 Enter the employee’s termination date.
Note: If you enter a termination date and the employee's "Active" flag is checked, upon saving the record, you will receive a message warning you that the 'Active' flag is Yes, and asking if you wish to continue. Answer Yes to save the record without changing the Active flag, answer N to abort the save.
Note: Changes to the employee’s termination date will be updated to PR Employees automatically if the Hire/Term Date update option is checked in HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).
Note: If a previously terminated employee is rehired, the termination date will be cleared.

##  Term Reason

 Enter the Reason Code (defined in HR Codes,
 Type N) that identifies why this employee was terminated.

## Occup Category

Enter a valid occupational category for this employee.
If you initialized this employee from PR, this field defaults the occupational category specified for this employee in PR Employees.
Note: Changes to the employee’s occupational category will be updated to PR Employees automatically if the Occup Category update option is checked in HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).

## Category Status

Category Status field on the HR Resources form, Payroll Info
 tab.
Select a category status for this resource. The standard status values are:

- A-Apprentice

- J-Journeyman

- T-Trainee

- N-Neither

The value in this field does not necessarily appear in any reports. The value found in the same-named field in the PR Employees form (Add'l Info tab), which typically matches your selection here, is used in the following reports:

- PR Department of Labor EEO-1 Report (ReportID 795)

- PR Certified Report - eMars (ReportID 1315)

When you change this employee’s category status, the system offers to update the field in the PR Employees form if the following are true:

- in the HR Company Parameters form (PR Update Options section), the Occupation Category checkbox is selected

- in the HR Resources form, the employee’s Active PR Employee and
 Exists in PR
 checkboxes are selected

If for any reason the system does not update the PR Employees form's instance of this field, and if you use either report mentioned above, you must manually update the field in the PR Employee form.
Note: Check with your state to determine the category status requirements.If you file electronically for NY DOT (PR Generate Champ-CM Exports), you must enter A, J, or T.

.

Related information

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

- [Update Employee Information](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/update-employee-information)

##  OT Schedule

 This field is accessible when you select ‘D-Daily’ in the Overtime field.
 Enter the daily overtime schedule for this employee. Press F4 for a list of valid schedules.
Note: Entry in this field updates to the OT Schedule field for this employee in PR Employees (Add’l Info tab) and vice versa.

## PR Group

Required if: this resource will be added (or
 initialized) to PR or if you enter a number in the PR Empl # field.
Specify the PR Group (from PR Groups) to which this employee is assigned. An employee’s earnings can only be posted within his/her currently assigned group.
If you initialized this employee from PR, this field defaults the PR Group specified for this employee in PR Employees.
Note: The system updates changes to this field to the corresponding record in PR Employees.

##  Department

 Required if this resource will be
 added (or initialized) to PR.
 Specify which Payroll department (PR
 Departments) this employee is assigned to. This department will be used as the default when
 entering timecards (PR Timecard Entry) to determine the GL distributions of earnings,
 unless JC departments are used.
 If you initialized this employee from PR, this field defaults the Department specified for this employee in PR Employees.
Note: Changes to this employee’s department will be updated
 to PR Employees automatically if the Timecard Defaults update option is checked in HR
 Company Parameters and the employee’s Active PR Employee and Exists in PR options are set
 to Y (checked).

##  Craft

 Specify the craft (PR Crafts) under which this employee commonly works. This craft will be
 used as the default when entering timecards (PR Timecard Entry).
 If you initialized this employee from PR, this field defaults the Craft specified for this employee in PR Employees.
Note: Changes to this employee’s craft will be updated to PR
 Employees automatically if the Timecard Defaults update option is checked in HR Company
 Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y
 (checked).

##  Class

 Specify the class under which this employee normally works. This class will be used as the default when entering timecards (PR Timecard Entry), and must be set up for the Craft (specified above) in PR Craft Classes.
 If you initialized this employee from PR, this field defaults the Class specified for this employee in PR Employees.
Note: Changes to this employee’s class will be updated to PR
 Employees automatically if the Timecard Defaults update option is checked in HR Company
 Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y
 (checked).

##  Insurance Code

 Required if this resource will be added (or initialized) to PR.
 Enter the insurance code (HQ Insurance Codes)
 that normally applies to this employee. May be used as the default when entering timecards
 (PR Timecard Entry), depending on the type of entry, the Insurance Based on Phase or
 SM Work Order Scope option in PR Company Parameters, and the Always Use Employee’s
 Standard Insurance Code option in PR Employees.
 If you initialized this employee from PR, this field defaults the Insurance Code specified for this employee in PR Employees.
Note: Changes to this employee’s insurance code will be
 updated to PR Employees automatically if the Timecard Defaults update option is checked in
 HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are
 set to Y (checked).

## Resident Tax State

Enter the employee's resident state for tax
 state based deductions and liabilities. If you initialized this employee from PR, this
 field defaults from the Resident Tax State field in PR
 Employees.
Changes to this field update PR Employees
 automatically if you checked the Timecard Defaults box in the PR Update
 Options section in HR Company Parameters, and the Active PR Employee and Exists in PR boxes
 are checked in HR Resources (Payroll Info tab).
When you are updating PR automatically, the
 system may use this state as the default for the
 Tax
 State
 field when entering timecards in PR Timecard Entry. The default for the

 Tax
 State
 field depends on the settings of the
 Work Office Tax
 State
 field on this form, the
 Always use
 Employee's Work/Resident Tax State
 checkbox in PR Employees, and the
 Use Job, SM Work
 Order or Office State for Tax State
 checkbox in PR Company Parameters (State/Local tab).
The following table displays how the

 Tax
 State
 field (PR Timecard Entry) defaults based on the settings of both
 checkboxes.
Use Job, SM WO, or Office State
Use Employee State
Tax State Default

Defaults from the
 Work Office Tax State
 field in PR Employees. If blank, the system defaults from the
 Resident Tax State
 field.

If you specify a job in the Job field
 (PR Timecard Entry), defaults from the PR State field in JC Jobs. When
 processing payroll, the system checks for reciprocity with the state specified in
 the Work
 Office Tax State or the Resident Tax State fields in PR
 Employees.
If you do not specify a job in the
 Job
 field, defaults from the
 Office State
 field in PR Company Parameters. When processing payroll, the system checks for reciprocity with the state specified in the
 Work Office Tax State
 or the
 Resident Tax State
 fields in PR Employees.
If you do not specify a job in the
 Job
 field, and the
 Office State
 field in PR Company Parameters is blank, defaults from the
 Work Office Tax State
 field in PR Employees. If that field is blank, defaults from the
 Resident Tax State
 field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR State
 field in JC Jobs.
If a customer work order, defaults from the

 PR State
 field in SM Work Orders. If you do not specify a PR State on
 the work order, defaults from the
 Work Office Tax State
 field in PR Employees. If that field is blank, defaults from
 the
 Resident Tax State
 field in PR Employees.

Defaults from the
 Work Office Tax State
 field in PR Employees. If that field is blank, defaults from the
 Resident Tax State
 field in PR Employees.

Defaults from the
 Work Office Tax State
 field in PR Employees. If that field is blank, defaults from the
 Resident Tax State
 field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Unemployment State

 Required if this resource will be added (or initialized) to PR.
 Enter the employee’s standard state for UnemploymentState based deductions and liabilities. This entry may be used as the default when entering timecards, based on the type of entry, the Use Job or SM Work Order State For Unemployment State option in PR Company Parameters, and the Always Use Employee’s Tax, Unemployment, And Insurance States option in PR Employees.
 If you initialized this employee from PR, this field defaults the UnemploymentState specified for this employee in PR Employees.
Note: Changes to this employee’s unemployment state will be updated to PR Employees automatically if the Timecard Defaults update option is checked in HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are set to Y (checked).
Note: This state must be a valid state associated with the default country set up in HQ Company Setup (Default Country field).

##  Insurance State

 Required if this resource will be added (or initialized) to PR.
Enter the employee’s standard state for
 Insurance State/Insurance Code based deductions and liabilities. This entry may be used as
 the default when entering timecards, based on the type of entry, the Use Job or SM Work Order
 State For Insurance State option in PR Company Parameters, and the Always
 Use Employee’s Tax, Unemployment, And Insurance States options in PR Employees.
If you initialized this employee from PR, this
 field defaults the InsuranceState specified for this employee in PR Employees.
Note: Changes to this employee’s insurance state will be
 updated to PR Employees automatically if the Timecard Defaults update option is checked in
 HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are
 set to Y (checked).
Note: This state must be a valid state associated with the
 default country set up in HQ Company Setup (Default Country field).

## Resident Local Code

Enter the employee's resident local code for local-based deductions and liabilities. If you initialized this employee from PR, this field defaults from the
 Resident Local Code
 field in PR Employees.
Changes to this field update PR Employees
 automatically if you checked the Timecard Defaults box in the PR Update
 Options section in HR Company Parameters, and the Active PR Employee and Exists in PR boxes
 are checked in HR Resources (Payroll Info tab).
When you are updating PR automatically, the
 system may use this state as the default for the
 Local
 field when entering timecards in PR Timecard Entry. The default for the

 Local
 field depends on the settings of the
 Work Office
 Local Code
 field on this form, the
 Always use
 Employee's Work/Resident Local Code
 checkbox in PR Employees, and the
 Use Job or
 Office Local for Local Tax
 checkbox in PR Company Parameters (State/Local tab).
The following table displays how the
 Local
 field (PR Timecard Entry) defaults based on the settings of both checkboxes.
Use Job, SM WO, or Office Local
Use Employee Local
Local Default

Defaults from the
 Work Office Local Code
 field in PR Employees. If blank, the system defaults from the
 Resident Local Code
 field.

If you specify a job in the Job field
 (PR Timecard Entry) and the PR Local Code field (JC Jobs) is not blank, defaults from the PR Local
 Code field in JC Jobs.
If you specify a job in the Job field, and the
 PR Local
 Code field (JC Jobs) is blank, the default value is the Resident Local Code field in the PR Employees form.
If you do not specify a job in the
 Job
 field, defaults from the
 Office Local
 field in the PR Company Parameters form, if it is not blank.
If you do not specify a job in the
 Job
 field, and the
 Office Local
 field in PR Company Parameters is blank, defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR Local
 Code field in the JC Jobs form, if it is not
 blank. If the job's PR Local Code field is blank, the default value is the Resident Local Code field in the
 PR Employees form
If a customer work order, defaults from the
 PR Local Code
 field in SM Work Orders. If you do not specify a PR Local Code on the work order, defaults as blank.

Defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
 If both the
 Work Office Local Code
 and the
 Resident Local Code
 fields in PR Employees are blank, defaults as blank.

Defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
 If both the
 Work Office Local Code
 and the
 Resident Local Code
 fields in PR Employees are blank, defaults as blank.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Work Office Tax State

Enter the employee's work office state for tax state based deductions and liabilities. If you initialized this employee from PR, this field defaults from the Work Office Tax State field in PR Employees.
Changes to this field update PR Employees
 automatically if you checked the Timecard Defaults box in the PR Update
 Options section in HR Company Parameters, and the Active PR Employee and Exists in PR boxes
 are checked in HR Resources (Payroll Info tab).
When you are updating PR automatically, the system may use this state as the default for the Tax State field when entering timecards in PR Timecard Entry. The default for the Tax State field depends on the settings of the
 Always use Employee's Work/Resident Tax State
 checkbox in PR Employees and the
 Use Job, SM Work Order or Office State for Tax State
 checkbox in PR Company Parameters (State/Local tab).
The following table displays how the

 Tax
 State
 field (PR Timecard Entry) defaults based on the settings of both
 checkboxes.
Use Job, SM WO, or Office State
Use Employee State
Tax State Default

Defaults from the
 Work Office Tax State
 field in PR Employees. If blank, the system defaults from the
 Resident Tax State
 field.

If you specify a job in the Job field
 (PR Timecard Entry), defaults from the PR State field in JC Jobs. When
 processing payroll, the system checks for reciprocity with the state specified in
 the Work
 Office Tax State or the Resident Tax State fields in PR
 Employees.
If you do not specify a job in the
 Job
 field, defaults from the
 Office State
 field in PR Company Parameters. When processing payroll, the system checks for reciprocity with the state specified in the
 Work Office Tax State
 or the
 Resident Tax State
 fields in PR Employees.
If you do not specify a job in the
 Job
 field, and the
 Office State
 field in PR Company Parameters is blank, defaults from the
 Work Office Tax State
 field in PR Employees. If that field is blank, defaults from the
 Resident Tax State
 field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR State
 field in JC Jobs.
If a customer work order, defaults from the
 PR
 State field in SM Work Orders. If you do not specify a PR State on the
 work order, defaults from the Work Office Tax State field in PR
 Employees. If that field is blank, defaults from the Resident Tax
 State field in PR Employees.

Defaults from the
 Work Office Tax State
 field in PR Employees. If that field is blank, defaults from the
 Resident Tax State
 field in PR Employees.

Defaults from the
 Work Office Tax State
 field in PR Employees. If that field is blank, defaults from the
 Resident Tax State
 field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Work Office Local Code

Enter the employee's work office local code for local-based deductions and liabilities. If you initialized this employee from PR, this field defaults from the
 Work Office Local Code
 field in PR Employees.
Changes to this field update PR Employees
 automatically if you checked the Timecard Defaults box in the PR Update
 Options section in HR Company Parameters, and the Active PR Employee and Exists in PR boxes
 are checked in HR Resources (Payroll Info tab).
When you are updating PR automatically, the
 system may use this code as the default for the Local field when entering timecards in PR
 Timecard Entry. The default for the Local field depends on the settings of the Always use Employee's
 Work/Resident Local Code checkbox in PR Employees and the Use Job, SM Work Order or
 Office Local for Local Tax checkbox in PR Company Parameters (State/Local
 tab).
The following table displays how the
 Local
 field (PR Timecard Entry) defaults based on the settings of both checkboxes.
Use Job, SM WO, or Office Local
Use Employee Local
Local Default

Defaults from the
 Work Office Local Code
 field in PR Employees. If blank, the system defaults from the
 Resident Local Code
 field.

If you specify a job in the Job field
 (PR Timecard Entry) and the PR Local Code field (JC Jobs) is not blank, defaults from the PR Local
 Code field in JC Jobs.
If you specify a job in the Job field, and the
 PR Local
 Code field (JC Jobs) is blank, the default value is the Resident Local Code field in the PR Employees form.
If you do not specify a job in the
 Job
 field, defaults from the
 Office Local
 field in the PR Company Parameters form, if it is not blank.
If you do not specify a job in the
 Job
 field, and the
 Office Local
 field in PR Company Parameters is blank, defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR Local Code field in the JC Jobs
 form, if it is not blank. If the job's PR Local Code field is
 blank, the default value is the Resident Local Code field in the
 PR Employees form.
If a customer work order, defaults from the
 PR Local Code
 field in SM Work Orders. If you do not specify a PR Local Code on the work order, defaults as blank.

Defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
 If both the
 Work Office Local Code
 and the
 Resident Local Code
 fields in PR Employees are blank, defaults as blank.

Defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
 If both the
 Work Office Local Code
 and the
 Resident Local Code
 fields in PR Employees are blank, defaults as blank.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

##  Earn Code

 Required if this resource will be added (or initialized) to PR.
 Enter the standard earnings code (from PR Earnings Codes) for this employee. This code may be used as the default when entering timecards in PR Timecard Entry.
 If you initialized this employee from PR, this field defaults the Earn Code specified for this employee in PR Employees.
Note: Changes to this employee’s earnings code will be
 updated to PR Employees automatically if the Timecard Defaults update option is checked in
 HR Company Parameters and the employee’s Active PR Employee and Exists in PR options are
 set to Y (checked).

##  Shift

 Enter the shift to use as a default when entering timecards (PR Timecard Entry) for this employee. You can override this value by crew in PR Crews. The crew shift only defaults if the employee is assigned to a crew and you specify the crew during timecard entry. If you do not specify a default shift here or at the crew level, shift defaults from the previously entered timecard.
 Changes to this field updates the Shift field in PR Employees for this employee.
Note: If you initialize crew timecards and you have not defined a shift for the crew, timecards default as shift ‘1’, regardless of whether you entered a default shift here.

## Employment Status

Employment Status field on the HR Resources
 form, Payroll Info tab, ACA Tracking and Classification section
Select the employee's Affordable Care Act
 (ACA) employment status. Options are:

- F - Full Time

- P - Part Time

- V - Variable

- S - Seasonal

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

- [About ACA Look Back Group Measurement Periods](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-aca-look-back-group-measurement-periods)

## Look Back Group

Look Back Group field on the HR Resources
 form, Payroll Info tab, ACA Tracking and Classification section
Enter the Look Back Group. Press F4 for a list
 of available look-back groups. Press F5 to launch the [HR ACA Look Back Group](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-look-back-group-form) form.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

- [About ACA Look Back Group Measurement Periods](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-aca-look-back-group-measurement-periods)

## Initial Measurement Start Date

Initial Measurement Start Date field on the HR
 Resources form, Payroll Info tab, ACA Tracking and Classification section
Enter the Initial Measurement Start Date in MM/DD/YY format. This is the start of the period when the hours worked are being counted for a new employee. The initial measurement period is the range of time measured for employee classification and eligibility purposes.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

## Initial Measurement End Date

Initial Measurement End Date field on the HR
 Resources form, Payroll Info tab, ACA Tracking and Classification section
Enter the initial measurement end date in MM/DD/YY format. This is the end of the period when the hours worked are being counted for a new employee. The initial measurement period is the range of time measured for employee classification and eligibility purposes.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

## Initial Administrative Start Date

Initial Administrative Start Date field on the
 HR Resources form, Payroll Info tab, ACA Tracking and Classification section
Enter the Initial Administrative Start Date in MM/DD/YY format. An initial administrative measurement period is between the initial measurement period and the associated initial stability period. This is the range of time used to collect information and make decisions about the results of the initial measurement period for a new employee.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

- [About ACA Look Back Group Measurement Periods](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-aca-look-back-group-measurement-periods)

## Initial Administrative End Date

Initial Administrative End Date field on the
 HR Resources form, Payroll Info tab, ACA Tracking and Classification section
Enter the initial administrative end Date in MM/DD/YY format. An initial administrative measurement period is between the initial measurement period and the associated initial stability period. This is the range of time used to collect information and make decisions about the results of the initial measurement period for a new employee.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

## Initial Stability Start Date

Initial Stability Start Date field on the HR
 Resources form, Payroll Info tab, ACA Tracking and Classification section
Enter the Initial Administrative Start Date in MM/DD/YY format. An initial stability period is the period of time to which the results of the initial measurement period apply.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

## Initial Stability End Date

Initial Stability End Date field on the HR Resources
 form, Payroll Info tab, ACA Tracking and Classification section
Enter the initial administrative end date in MM/DD/YY format. An initial stability period is the period of time to which the results of the initial measurement period apply.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

##  HD Amount

 The field is for Canadian users only.
 Enter the deduction amount for the purchase of approved shares of capital stock of a prescribed labour-sponsored venture capital corporation in Saskatchewan. This only applies to employees paying tax in Saskatchewan.

##  F1 Amount

 The field is for Canadian users only.
 Enter the amount for the Northern Resident Deduction (living in a prescribed zone).

##  Annual LCF stock purchase

 The field is for Canadian users only.
 Enter the deduction amount for the purchase of approved shares of capital stock of a prescribed labour-sponsored venture capital corporation.

##  Annual LCP stock purchase (Saskatchewan)

 The field is for Canadian users only.
 Enter the deduction amount for the purchase of approved shares of capital stock of a prescribed labour-sponsored venture capital corporation in Saskatchewan. This only applies to employees paying tax in Saskatchewan.

##  Do Not Allow Re-Hire of this Employee

 Check this box if this employee should not be re-hired.
 Leave this box unchecked if this employee is eligible for re-hire.

##  Relatives Working For Company

 Check this box if this employee has relatives working at this company.
 Leave this box unchecked if this employee does not have any relatives working at this company.

##  Passport

 Check this box if this employee has a passport.
 Leave this box unchecked if this employee does not have a passport.

##  Disability

 Check this box if this employee is disabled.
 Leave this box unchecked if this employee is not disabled.

##  Disability Desc

 Enabled only if Disability option is checked above.
 Enter a description of the employee’s disability, up to 30 characters.

##  License #

 Enter this employee’s driver’s license number, up to 20 characters.

##  License Type

 Indicate what type of driver’s license this employee has, up to 20 characters.

## State

Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.

##  License Country

 Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

##  License Class

 Enter the 1-character code identifying this employee's license classification.

- A = Class A. Any combination of vehicles with a GVWR of 26,001 or more pounds, provided the GVWR of the vehicle(s) being towed is in excess of 10,000 pounds.

- B = Class B. Any single vehicle with a GVWR of 26,001 or more pounds, or any such vehicle towing a vehicle not in excess of 10,000 pounds GVWR.

- C = Class C. Any single vehicle, or combination of vehicles, that does not meet the definition of Class A or Class B, but is either designed to transport 16 or more passengers, including the driver, or is placarded for hazardous materials.

- D = Class D. As defined by state.

Note: The A, B, and C license classifications require the driver's have a CDL (Commercial Drivers License). You can set up and maintain CDL endorsements/restrictions for employees in HR Employee License Endorsements (Endorsements button below).

##  Expiration Date

 Enter the expiration date of this employee’s driver’s license.

##  Approved To Operate Company Vehicles

 Check this box if this employee is approved to operate company vehicles.
 Leave this box unchecked if this employee is not approved to operate company vehicles.

##  Disabled

The Disabled checkbox on the HR Resources form, Other Info
 tab.
Select this checkbox if this resource is a
 veteran who is entitled to compensation or was discharged due to a service-related
 disability.
 Leave this box unchecked if this resource is
 not a disabled veteran.

##  Armed Forces Service Medal

The Armed Forces Service Medal checkbox on the HR Resources
 form, Other Info tab.
 Select this checkbox if this resource is a veteran who participated in an operation for which an Armed Forces service medal was awarded.

## Active Duty Wartime or Campaign Badge

The Active Duty Wartime or Campaign Badge checkbox on the HR
 Resources form, Other Info tab.
Select this checkbox if this resource is a veteran who served on active duty during a war or in a campaign for which a badge was authorized.

##  Discharge Date

Specify the date on which this Veteran (employee) was discharged from service.

##  Federal Job Category

 Required if Veteran Status (above) is Disabled, Vietnam, or Other Veteran.
 Specify the Federal job category under which this employee falls:

- 1-Executive/Senior Level Officials and Managers

- 2-First/Mid Level Officials and Managers

- 3-Professionals

- 4-Technicians

- 5-Sales Workers

- 6-Administrative Support Workers

- 7-Craft Workers

- 8-Operatives

- 9-Laborers/Helpers

- 10-Service Workers

 The information entered in this field is used for the following reports:

- HR ADA-Disabled Applicants Status

- HR Federal Contractor Veterans Report (Vets-4212)

- HR Veteran Applicants Status

- HR Work Force Analysis

## Hiring Location

Hiring Location field on the HR Resources form,
 Other Info tab
Assign the hiring location this resource was hired from. Press F4 to view and select from valid locations in the HR Hiring Location Setup form.

##  I9 Status

 Enter the I9 (immigrant) status of this employee, if applicable, up to 20 characters.

##  Citizenship

 Enter the country of citizenship for this employee, up to 20 characters.

##  Review Date

 Enter the date this employee’s immigrant status is up for review/renewal.

##  Training Budget

 Specify the yearly budget available for this employee for training.

##  Cafeteria Plan Budget

 Specify the total premium allowed for this employee under your company’s current cafeteria plan.

##  Leave Approval Group

 Enter the leave approval group for associating with this resource. Press F4 to see a list of approval groups.
 You must enter a group to enable leave request functionality for this resource. For more information, refer to Leave Requests in Related Topics below.

[](/en/vista/vista/hr-and-payroll/human-resources/leave/about-leave-requests)Leave Requests

##  High School Attended

 Indicate from which high school this employee graduated, up to 30 characters.

##  Graduation Date

 Enter the employee’s high school graduation date.

##  College Attended

 Enter the name of the college(s) this employee attended, up to 30 characters.

##  College Attended: From

 Specify the date(s) this employee began attending the specified college(s).

##  College Attended: To

 Specify the date(s) through which this employee attended the specified college(s).

##  College Attended: Degree

 Enter the college degree(s) achieved by this employee, up to 20 characters.

## Activity Date

The Activity Date field on the HR Resources form, ACA History tab.
Enter the Activity Date in MM/DD/YY format. This date represents the month and year in which the coverage offer (Series 1 Codes) or acceptance event (Series 2 Codes) are effective.
Note: If your policy year is not the calendar year, you will need to have entries for both years. For example, if your policy year is July 1, 2023 through June 30, 2024, you will need one entry for 07/01/23 through 12/31/23 and one entry for 01/01/24 through 06/30/24.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

## Code Type

Code Type field on the HR Resources form, ACA
 History tab
Select the Code Type: Series 1 Codes
 for coverage offers or Series 2 Codes for acceptance
 activities.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

## Series One Code

Series One Code field on the HR Resources form, ACA History
 tab
Available if Series 1 Codes
 is selected in the Code Type field.
The Code Series 1 indicator codes specify the type of coverage, if any, offered to an employee, the employee’s spouse, and/or the employee’s dependents.

Related concepts

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

- [About the HR ACA Coverage Offer Init Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form)

Related tasks

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

## Series Two Code

Series Two Code field on the HR Resources
 form, ACA History tab
Available if Series 2 Codes
 is selected in the Code Type field.
Select an acceptance code from the IRS Code Series 2:

- 2A - Employee not employed during the month

- 2B - Employee not a full-time employee

- 2C - Employee enrolled in coverage offered

- 2D - Employee in a section 4980H(b) Limited Non-Assessment Period

- 2E - Multi-employer interim rule relief

- 2F - Section 4980H affordability form W-2 safe harbor

- 2G - Section 4980H affordability federal poverty line safe harbor

- 2H - Section 4980H affordability rate of pay safe harbor

- 2I - Non-calendar year transition relief applies to this employee

Codes in Code Series 2 apply to employees who are in the above situations for one or more months of the calendar year.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

## Expiration Date

Expiration Date field on the HR Resources
 form, ACA History tab
Enter the Expiration Date in MM/DD/YY format. This is the date that the coverage offer or acceptance expires.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [Set Up and Process Data for ACA 1094s and 1095s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

##  Notes

Enter notes for ACA history.

##  Application Date

 Enter the date this resource applied for a position in this company.

##  Available Date

 Enter the date this applicant is available to begin working.

##  Last Contact Date

 Enter the date this applicant was last contacted.

##  Contact Phone

 Enter the phone number at which this applicant may be contacted.

##  Alternate Contact Phone

 Enter an alternate phone number at which this applicant may be contacted, if applicable.

##  Expected Salary

 Indicate what salary this applicant expects for the position he/she is applying for.

##  Referral Source

 Specify the applicant’s referral source; that is, how the applicant learned about the position. Up to 30 characters allowed.

##  Referral Cost

 Enter the cost of referral of this applicant, if applicable. Up to 10 digits before the decimal and 2 after.

##  Current Employer

 Indicate who this applicant’s current employer is (if applicable), up to 30 characters.

##  Length of Time

 Indicate how long this employee has worked for current employer, up to 20 characters.

##  Previous Employer

 Indicate who this applicant’s previous employer was (if applicable), up to 30 characters.

##  Length of Time

 Indicate how long this employee worked for his/her previous employer, up to 20 characters.

##  Do Not Contact Current Employer

 Check this box if applicant does not want his/her current employer contacted.
 Leave this box unchecked if applicant has given permission for his/her current employer to be contacted.

##  Physical

 Check this box if this employee has had a physical.
 Leave this box unchecked if this employee has not had a physical

##  Last Physical Date

 Enter the date this employee last had a physical, if applicable.

##  Physical Expiration Date

 Enter the date through which this employee’s last physical is valid. This date can be used in reports to indicate when this employee is next due for a physical.

## Physical Results

Use this box to record the results of this employee’s physical. The space allowance in this box is virtually unlimited.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.

##  Deduction

Enter each of the deduction codes (from PR
 Deductions/Liabilities) that are applicable to this employee. Deduction codes entered here
 must be assigned a Method of “Routine” (in PR Deductions/Liabilities).

## File Status

Enter the filing status for this employee.
For Federal W-4s submitted after January 1, 2020, this is the value from Step 1c of Form W-4 (2020). only the following options are valid.

- M= Married Filing Jointly

- S = Single or Married Filing Separately

- H = Head of Household

For Federal W-4s submitted prior to January 1, 2020 and state W-4s:



- S = Single

- M = Married

- H = Head of Household

- F = Married, Filing Jointly, one spouse working

- B = Married Filing Jointly, both spouses working (state only)

- W = Qualified Widow(er)

- O = No exemptions (Alabama only)

Note: It is not always necessary to define a state deduction if the filing status is the same as the employee’s federal filing status. If a state deduction has not been defined for an employee, the system automatically uses the federal filing status. If a state deduction has been defined and the filing status and exemption are left blank, a filing status of “single” with exemptions zero are assumed.
Many state routines only allow “M” or “S” as a valid filing status. Other exceptions include Connecticut, Georgia, and Puerto Rico (see the [Tax and Worker's Comp Routines ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines)Tax and Worker's Comp Routines tables for details on individual requirements).
It is very important to check for any special requirements defined for the state to determine whether a separate state deduction filing status needs to be set up.
Click [here](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#ID-0001175c--en) for the Australian field definition.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Regular Exempt's

US and Canada: The Regular Exempt's field on the HR Resources
 form, Filing Status tab. Australia: The Scale field on the HR Resources form, Filing Status
 tab.
Specify the number of regular exemptions claimed on the W-4. Initially defaults as blank.
Click [here](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#ID-00011762--en) for the Australian field definition.
Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank. Instead, use the Dependent Amount field to enter the annual dollar amount to claim as a dependent deduction. For more information, see [Dependent Amount](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#concept-43370001--en).
Pre-2020 Federal W-4s
For Federal W-4 information entered prior to January 1, 2020, this field is still applicable and indicates the number of regular exemptions claimed on the W-4. However, if the employee submits a Federal 2020 W-4, it is suggested that you clear the value in this field.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Add'l Exempt's

US and Canada: The Add'l Exempt's field on the HR Resources
 form, Filing Status tab. Australia: The Children field on the HR Resources form, Filing
 Status tab.
Most states do not require a separate allowance certificate, however follow your state guidelines for entering an employee's additional allowances/exemptions. Initially defaults as blank.
Click [here](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#ID-000117ad--en) for the Australian field definition.
Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this
 field blank. Instead, use the Dependent
 Amount field to enter the annual dollar amount to claim as a dependent
 deduction. For more information, see [Dependent Amount](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#concept-43370001--en).
Pre-2020 Federal
 W-4s
For Federal W-4 information entered prior to January 1, 2020, this
 field is still applicable. However, if the employee submits a Federal 2020 W-4, it is
 suggested that you clear the value in this field.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Scale

The Scale field on the HR Resources form, Filing Status
 tab.
For Australian users only.

### Scale Numbers for PAYG Withholding

Enter the scale number for PAYG withholding. You may enter the following numbers:

- 1 = No tax-free threshold; enter
 this if question 8 on the employee's NAT 3093 is No.

- 2 = Tax-free threshold with leave
 loading.

- 3 = Foreign resident; enter this
 if the employee is a non-resident.

- 4 = No tax file number (TFN) was provided by the employee

- 5 = Full Medicare exemption; enter
 this if the employee filed a NAT 0929 and claimed a full exemption.

- 6 = Half Medicare exemption; enter
 this if the employee filed a NAT 0929 and claimed a half exemption.

### Scale Numbers to Calculate STSL Component

If you need to calculate a Study and Training Support Loan component for an employee,
 use the following scale numbers:

- 91 = No tax-free threshold; enter
 this if question 8 on the employee's NAT 3093 is No

- 92 = Tax-free threshold with leave
 loading.

- 93 = Foreign resident; enter this
 if the employee is a non-resident.

- 95 = Full Medicare exemption;
 enter this if the employee filed a NAT 0929 and claimed a full exemption.

- 96 = Half Medicare exemption;
 enter this if the employee filed a NAT 0929 and claimed a half exemption.

Note: The STSL Component schedule applies to employees who have any of the following
 debts:

-  Higher Education Loan Program (HELP)

- VET Student Loan (VSL

- Financial Supplement (FS)

- Student Start-up Loan (SSL) / ABSTUDY SSL

- Trade Support Loan (TSL)

## Children

For Australian users only.
Enter the number of children for the employee. Enter a number here when the answer to question 12 on the employee's NAT 0929 is Yes. Otherwise, leave blank.

## Over Misc

For use with Michigan and Mississippi State Tax only.
Check this box to override the routine’s Misc Amt #1
 (usually the exemption amount) as specified in PR Routines.
Leave this box unchecked if you do not want to override the routine’s Misc Amt #1.
Click [here](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#ID-000117b2--en) for the Australian field definition.
Click [here](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#ID-0005c0b70001--en) for the Canadian field definition.
Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Over Misc

For Australian users only.
Select this checkbox if the answer to
 question 9 on the employee's NAT 3093 is Yes. When you select this checkbox, the system
 enables the Misc
 Amt 1 field, where you can enter the estimated tax offset amount from the
 NAT 3093.

## Over Misc

For Canadian users only.
Select this checkbox to apply additional tax credits to this employee. Then use the Misc Amt 1 field to record additional authorized tax credits for the employee.

Do not select this checkbox if you are not applying additional tax credits for this employee.

## Misc Amt1

The Misc Amount #1 field on the HR Resources form, Filing
 Status tab.
If you elected to override the routine’s Misc Amt #1 (i.e. you checked the Over Misc option), enter the amount to use when calculating for this employee.
If you are not overriding the routine’s Misc Amt #1, enter 0.00 in this field. (This amount must be 0.00 if Over Misc is unchecked.)
Click [here](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#ID-000117b8--en) for the Australian field definition.
Click [here](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#ID-000377eb0001--en) for the Canadian field definition.
Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Misc Amt 1

For Australian users
 only.
If you selected the Over
 Misc checkbox and the answer to
 question 9 on the employee's Nat 3093 is Yes, enter the
 estimated total tax offset amount in this field.

## Misc Amt 1

For Canadian users only.
If you are applying tax credits for this employee (you selected the Over Misc checkbox), enter the Annual Amount from line 15 of the employee's TP-1016-V form (Application for a Reduction in Source Deductions of Income Tax for an Individual or a Self-Employed Person).

## Total Claim Amount

The field displays for Canadian users
 only.
Enter the total claim amount from the
 employee’s TD1 form. The value you enter here updates the Total Claim
 Amount field on PR Employee Dedns/Liabs.

## Misc Factor

The Misc Factor field on the HR Resources form, Filing Status
 tab.
This field is for U.S. users only.
If you selected the Override Misc Amount #1 checkbox and entered an amount in the Misc Amount #1 field, enter a factor here.
Note: This factor is only used by a few routines, such as Arizona and New York City. It is used to store information needed for tax calculations.Entry here is determined by the routine being used. For information about what should be entered here for the tax state, see [About Payroll Routines](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines).

Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Multiple Jobs Checked

The Multiple Jobs Checked checkbox on the on the HR Resources
 form, Filing Status tab.
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Select this checkbox if the employee filled out Step 2 of Federal Form W-4 (2020); that is, the employee has more than one job or is married filing jointly and their spouse also works.
Leave this checkbox unselected if the employee did not fill out Step 2 of Federal Form W-4 (2020).
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Dependent Amount

The Dependent Amount field on the HR Resources form, Filing
 Status tab.
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Enter the total annual dollar amount to be claimed as a dependent deduction. This is the total amount entered by the employee in Step 3 of Federal Form W-4 (2020); that is, the amount entered on Line 3.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Other Income

The Other Income field on the on the HR Resources form, Filing
 Status tab.
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Enter the total other income as entered by the employee in Step 4a of Federal Form W-4 (2020). This amount represents the total annual income the employee expects during the year that will not have withholding (such as interest, dividends, retirement income, etc)..
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Other Deductions

The Other Deductions field on the on the HR Resources form,
 Filing Status tab.
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Enter the total other deductions entered by the employee in Step 4b of Federal Form W-4 (2020). This amount represents the total annual deductions other than the standard deduction..
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Filing Status

For Australian users only.
Select M from
 the drop-down if the employee submitted Form NAT 0929 and answered Yes to question 9 (Do you have a spouse).
 Otherwise, leave this field blank.

##  Add-On

 Used to indicate whether employee will have additional taxes withheld from their pay.
 Specify the add-on type for this deduction, to indicate how the add-on amount is calculated.

- None – No additional amount will be added.

- Amount – Add-on is a flat amount.Important: If you are entering extra withholding
 information from Federal Form W-4, you must select this type.

- Rate – Add-on is calculated as a rate of the subject amount.

Canadian users: See [Add-on Rate / Amount](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#ID-0005c0be0001--en) for additional help.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

##  Rate/Amount

Used only when an Add-On Type is specified (previous field).
Specify the additional amount or rate to withhold from this employee's pay. Add-on amounts can be any dollar value; however, if entering a rate, you will typically enter a value between 0.00 and 1.00 (e.g. .25000, .50000, etc. with 1.00000 representing 100%).
Note: The rate/amount must be 0.00 if no additional amount/rate is being withheld for this employee (i.e. the Add-On option is set to ‘None’).
For Canadian users, see [Add-on Rate / Amount](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form/field-definitions-hr-resources-form#ID-0005c0be0001--en).
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Add-on Rate / Amount

The field is for Canadian users only.
Enter the annual Add-on Amount from line 11 of
 the employee's TP-1015.3-V form (Source Deductions Return). Quebec users must enter the
 amount value only.
