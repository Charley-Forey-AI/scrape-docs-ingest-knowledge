---
title: "Field Definitions: PR Employees Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form"
---

# Field Definitions: PR Employees Form

The following is a list of field descriptions for the PR
 Employees form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Employee

Enter a number, up to 6 digits, to uniquely identify this employee or enter ‘+’ to have the system automatically assign the next sequential number.
Note: If the system determines that the next value exceeds the maximum value allowed (999999), you will receive a message that you must manually enter a number lower than the maximum..

##  Last Name

 Enter the employee’s last name, up to 30 characters.

##  First Name

 Enter the employee’s first name, up to 30 characters.

##  Middle Name

 Enter the employee’s middle name, up to 15 characters.

##  Suffix

 Enter an alphabetic suffix (i.e. Jr., Sr., III) for this employee, if applicable, up to 4 characters.

## Sort

This field defaults to the first 15 characters of the employee’s last name. If the last name is less than 15 characters, the system adds characters from the employee’s first name, up to the 15 character limit for the field. You can change the default as necessary. Sort names can be entered in upper and/or lower case, but are always converted to uppercase letters. The system uses this sort name for alphabetical sorting, such as on reports and lookups (F4).
Note: If you change this employee's sort name, and "Name" is checked in the PR Update Options section in HR Company Parameters, the system displays a message informing you that the “Payroll employee information does not match the HR information for this employee.” Additionally, it asks “Would you like to update HR also?”. If you click Yes, the new sort name will be updated to HR. If you select No, HR will not be updated with the new sort name, and you will need to update it manually.

## Address

Enter the employee's mailing address information in the following fields:

- Address - This address is the only
 address field used on payroll checks and should therefore include apartment number,
 if applicable. It is updated to the Delivery Address in PR W-2 Employee Information
 and is the only address printed on W-2s.

- City - Enter the city.

- State - Enter a valid state (as
 defined in HQ States). The system validates the state based on the Default Country
 specified in HQ Company Setup for the active company. If not valid, an error
 displays, but entry is allowed. You must then enter a valid country for this state in
 the Country field.

- Zip Code - Enter the zip/postal
 code, up to 12 digits.

- Country - Enter the 2-character
 country code. Entry in this field is required when the address exists outside the
 Default
 Country specified in HQ Company Parameters for the active company.
 Country must be valid for the specified state (e.g. state, province, territory, etc.)
 as defined in HQ States.

- Add'l Address - Use this field to
 enter additional address information for this employee. For example, if employee
 receives his/her mail at a P.O. Box, then you might enter the P.O. Box in the
 Address field, and use this field to enter the street address.

The address information entered here is not used by any of the posting forms or on payroll checks. It will, however, be updated to the Location Address in PR W-2 Employee Information and will be used for electronic filing only. It is not used on the printed W-2.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## Email

Enter an email address. If you click the Email button () to the right of this field, the system opens Microsoft Outlook and sets up an outgoing message for you using the email address specified in this field.Note: You
 can enter multiple email addresses if applicable; however, you
 must separate them with a semi-colon. For example,
 jane.doe@email.com; johnd@email.com;
 joe.smith@email.com.

## Work Email

The Work Email field on the PR Employees form, Info tab.
If the employee has a work email address, enter it here. This field is intended as an alternative to the Email field, which is often used for employee-specific email notifications (like onboarding items, paystubs, and tax forms), that the employee may prefer to receive at a personal email account.
The Work Email field also assists in Trimble ID account registration. The registration process will look for a work email entry if the employee does not have a VA User Profile account in Vista, and will create the Trimble ID using the value in the Work Email field.
There is also a synchronization function with the Work Email field in the HR Resources form. If the company uses the HR module in Vista, then the work email in the HR Resources form is automatically updated with the new value.

##  Phone

 Enter a phone number for informational purposes only. The default for this field is blank.

## Cell

Enter the employee's cell phone number, up to 20 characters.

## SSN#

Enter a unique social security number in the proper format (###-##-####). If dashes are not entered, they are automatically provided.
Note: If you change this employee's social security number and the Social Security Number option is checked in HR Company Parameters (PR Update Options), a message displays indicating that the information in PR and HR does not match. Additionally it asks if you wish to update information in HR. If you click Yes, the new SSN updates to HR. If you select No, HR is not updated with the SSN and you will need to update it manually.
Click [here](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-00037c19--en) for the field definition for Australian users.
Click [here](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-00037c30--en) for the field definition for Canadian users.

## TFN

TFN field on the PR Employees form, Info tab.
This field is for Australian users only.
Enter a unique tax file number in the proper format (###-###-###). If dashes are not entered, they are automatically provided.
You can also enter the following duplicate numbers, if meeting the associated criteria:

- 333-333-333 - For payees under 18 years of age and earning $122 or less per week.

- 444-444-444 - For payees who are Commonwealth Government Pensioners.

- 111-111-111 - For new payees who have not made a TFN declaration, and 28 days have not passed.

- 000-000-000 - For payees who choose not to quote a TFN and has not claimed an exemption, or does not fit into any of the other categories.

Note: If you change this employee's tax file number and you
 checked the Social
 Security Number box in HR Company Parameters (PR Update Options section), a
 message displays indicating that the information in PR and HR does not match. Additionally
 it asks if you wish to update information in HR. If you click Yes, the new
 TFN updates to HR. If you select No, HR is not updated with the TFN and
 you will need to update it manually.

## SIN

This field is for Canadian users only.
Enter a unique Social Insurance Number (SIN) in the proper format (###-###-###). If dashes are not entered, they are automatically provided.
The system will validate that the number you enter is unique and is a valid number. However, it is unable to verify that this is the correct number for the specific employee.
Note: If you change this employee's social insurance number
 and you checked the Social Security Number box in HR Company Parameters (PR Update Options
 section), a message displays indicating that the information in PR and HR does not match.
 Additionally it asks if you wish to update information in HR. If you click Yes, the new
 SIN updates to HR. If you select No, HR is not updated with the SIN and
 you will need to update it manually.

## Race

The Race field in the PR Employees form
Enter a
 valid race code from PR Race Codes. Press F4 to select from a list of codes. If you
 are using any of the EEO reports, they will display the EEO Category assigned to this race
 code.
Important: If you are using the PR Certified Export - eMars, ReportID 1315 (U.S. only), use one-character values only to insure that your export file is compatible with the eMars system.
Non-U.S. Payroll Companies:
While race codes apply only to U.S. companies, this field still requires an entry. To meet the requirement, create a place-holder record in the PR Race Codes form and use it for this field. The entry will have no impact on any other part of the system.

Related information

- [PR Race Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-race-codes-form)

## Gender Identity

The Gender Identity drop-down on the PR Employees form, Info
 tab.
Select this employee's gender identity.

- M-Male

- F-Female

- X-Non-Binary

- O-Other (enables the text box to the right for entering the gender description)

Note: Gender Identity classifications are not currently used for EEO reporting. Use the Reporting Gender field to assign this employee's gender for EEO reporting purposes.

Note: Changes to the employee’s gender information will be updated to HR Resources automatically if the Name update option in HR Company Parameters is selected and the employee’s Active PR Employee and Exists in PR checkboxes are selected in HR Resources.


## Description

The Description field (unlabeled) on the PR Employees form,
 Info tab.
This field is enabled only when the Gender Identity drop-down is set to O-Other.
Enter a description of the employee's gender (for example, Agender, Androgyne, Bigender, etc.).
Note: Changes to the employee’s gender information will be updated to HR Resources automatically if the Name update option in HR Company Parameters is selected and the employee’s Active PR Employee and Exists in PR checkboxes are selected in HR Resources.


##  Reporting Gender

The Reporting Gender field on the PR Employees form, Info tab.
 Select the employee’s gender for EEO and other reporting.
Note: Changes to the employee’s gender information will be updated to HR Resources automatically if the Name update option in HR Company Parameters is selected and the employee’s Active PR Employee and Exists in PR checkboxes are selected in HR Resources.


##  Birth Date

 Enter the employee’s birth date for informational purposes, including slashes (e.g. 03/12/1947). If entered in a format of MM/DD/YY, the year is assumed to be in a range from 1930 – 2029.

## Hire Date

Hire Date field on the PR Employees form, Info
 tab.
Enter the employee’s hire date for
 informational purposes. If you initialized this employee from HR, this field defaults the
 Hire Date specified in HR Resources.
Note: If you change this employee’s hire date, and the “Hire/Term Date” option (PR Update Options, HR Company Parameters) is checked, the system displays the following message: “Payroll employee information does not match the HR information for this employee.” Additionally, it asks “Would you like to update HR also?” If you click Yes, the new hire date updates to HR. If you select No, HR is not updated with the new hire date and you will need to update it manually.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

- [About Initializing Employees to PR from HR](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-initializing-employees-to-pr-from-hr)

## Most Recent Rehire Date

Most Recent Rehire Date field on the PR
 Employees form, Info tab.
Enter the most recent rehire date for this
 employee. This date allows you to track the rehire date separately from the original hire
 date specified in the Hire Date field.
For new employee records, this field will
 initially default from the Hire Date field.
For Canadian Companies
You must enter a date in this field for the
 system to generate employee ROE records. For more information, see [About Setting Up Employees for ROE Reporting](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/canada-roe/about-setting-up-employees-for-roe-reporting).
For Australian Companies
Entry in this field is required for creating and maintaining period of reporting records.
Changes to this date affect the reporting
 periods (on the PAYG Reporting Periods tab) for this employee as follows:

-  If this is a new employee record, upon saving the record, the system creates a new reporting period record and sets the Period Start Date for the reporting period equal to the date entered here.

- If this is an existing employee that was previously
 terminated (Termination Date field is not blank), entry in this field will
 automatically display a message indicating that the Termination Date will be cleared.
 If you select OK, the system clears the Termination Date field, creates a
 new reporting period record, and sets the Period Start Date for the reporting period
 equal to the new rehire date.

If you select Cancel, the system cancels the change and leaves the termination date intact. No new reporting period is created.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [About PAYG Reporting Periods (Australia)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-payg-reporting-periods-australia)

##  JC Co#

The JC Co # field on the PR Employees form, Info tab.

 Enter the Job Cost company for which this employee currently works. If this is a new employee or the employee will not be working on jobs, you may leave this field blank.
 The company specified here is used as the default JC Co when entering
 timecards for this employee (in PR Timecard Entry). If a different JC company is
 entered on the timecard, the system automatically updates this field with the
 specified JC company, as long as the timecard date is equal to or later than the
 Last Timecard Post
 Date date specified (below) for the employee.
If you enter a new timecard or edit an existing timecard with a timecard date
 earlier than this date, the system will not update this field, even if the JC
 company differs from the JC company specified here.

##  Job

The Job field on the PR Employees form, Info tab.
 Enter the job this employee currently works on. If this is a new employee or the employee will not be working on jobs, you may leave this field blank.
 The job specified here is used as the default job when entering timecards for
 this employee (in PR Timecard Entry). If a different job is entered on the
 timecard, the system automatically updates this field with the specified job, as long as
 the timecard date is equal to or later than the Last Timecard Post Date specified
 (below) for the employee.
If you enter a new timecard or edit an existing timecard with a timecard date
 earlier than this date, the system will not update this field, even if the Job differs
 from the Job specified here.

##  Crew

The Crew field on the PR Employees form, Info tab.
 Enter the crew this employee currently works on. If this is a new employee or the employee will not be working on a crew, you may leave this field blank.

The crew specified here is used as the default crew when entering timecards
 for this employee (in PR Timecard Entry). If a different crew is entered on the
 timecard, the system automatically updates this field with the specified crew, as long
 as long as the timecard date is equal to or later than the Last Timecard Post Date date
 specified (below) for the employee.
If you enter a new timecard or edit an existing timecard with a timecard date
 earlier than this date, the system will not update this field, even if the crew differs
 from the crew specified here.

##  Last Timecard Post Date

The Last Timecard Post Date field on the PR Employees form,
 Info tab.
This field displays the date of the last timecard posted for this employee (in PR Timecard Entry). The system updates this field automatically when you save a timecard line, as long as the timecard date is equal to or later than the last posted date displayed in this field.
 If you enter a new timecard or edit an existing timecard with a timecard date earlier than this date, the system will not update this field, nor will it update the JC Co#, Job, or Crew fields. 

## Vendor

Vendor field on the PR Employees form.
Enter the vendor number, up to 6 digits, that corresponds to this employee, if applicable.
If one does not already exist, and if the Allow Vendors to be added from
 Payroll checkbox on the AP Company Parameters form is selected, when
 you enter a new vendor number, the system assigns it to a new vendor in the AP Vendors
 form and automatically populates certain sections:

- Name

- Address

-
Email address

- Phone

- Direct deposit info

Note: If the Allow
 Vendors to be added from Payroll checkbox on the AP Company
 Parameters form is not selected, you must use the AP Vendors form to create the
 vendor record first, then add the number to this field.

## Income Stream: PAYG Income Type

(Australia) The PAYG Income Type drop-down on the PR Employees form, Info tab.
Select the PAYG income type. The system uses the income type during payroll processing to determine tax rates and income limits for the employee, and to qualify amounts in the resulting pay sequence by income stream type.

- S - Salary or wages (default) - Select this option if this employee is a full or part-time employee receiving a regular salary or hourly wages.

- H - Working holiday maker - Select this option if this employee is a working holiday maker. Once selected, the system enables the Country Code field; entry in this field is required.

Note: If you need to change the income type for an existing employee, you must close the current reporting period and enter a new rehire date to ensure that a new reporting period is generated. For more information, see [Change an Employee's PAYG Income Type: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-payg-withholding-for-employees/change-an-employees-payg-income-type-australia).

Related information

- [Change an Employee's PAYG Income Type: Australia](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-payg-withholding-for-employees/change-an-employees-payg-income-type-australia)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Income Stream: Country Code

(Australia) The Country Code field on the PR Employees form, Info tab
For use with STP Phase 2 only.
This field is enabled and required if you selected a PAYG Income Type of H-Working holiday maker (WHM).
Enter the two-letter code representing the home country of the working holiday maker. This will be the alpha-2 code defined for the country in ISO 3166-1 (cannot be AU, CC, CX, HM, or NF).

##  PR Group

PR Group field on the PR Employees form, Info
 tab.
Enter the PR Group to which this employee is assigned or press F4 to select from a list of valid payroll groups. An employee’s earnings can only be posted within his currently assigned Group.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

##  Department

 Enter a valid department to which this employee is assigned. This department is used as the default when entering timecards and controls the GL distributions of earnings, unless JC Departments are used.

##  Craft

 Enter the valid craft that this employee commonly works under. This entry is optional and is used as the default when entering timecards.

##  Class

 Enter the valid class that this employee commonly works under. This entry is optional and is used as the default when entering timecards.

##  Ins Code

 Enter a valid insurance code as set up in HQ Insurance Codes. This includes the code only, not the state that commonly applies to this employee. This entry may be used as the default when entering timecards, based on the type of entry, the Insurance by Phase option in PR Company Parameters, and the Always Use Employee’s Standard Insurance Code option selected below. The state will be added in timecard entry based on job or resident state.

## Resident Tax State

Enter the employee's resident state for tax state
 based deductions and liabilities. The system may use this state as the default for the
 Tax
 State field when entering timecards in PR Timecard Entry. The default
 for the Tax
 State field depends on the settings of the Work Office Tax
 State field on this form, the Always use Employee's Work/Resident Tax
 State checkbox on this form, and the Use Job or Office State
 for Tax State checkbox in PR Company Parameters (State/Local tab).
The following table displays how the Tax State field (PR Timecard Entry) defaults based on the settings of both checkboxes.
Use Job, SM WO, or Office State
Use Employee State
Tax State Default

Defaults from the Work Office Tax State field in PR Employees. If blank, the system defaults from the Resident Tax State field.

If you specify a job in
 the Job field (PR
 Timecard Entry), defaults from the PR
 State field in JC Jobs. When processing payroll, the
 system checks for reciprocity with the state specified in the
 Work Office Tax
 State or the Resident Tax
 State fields in PR Employees.
If you do not specify a job in the Job field, defaults from the Office State field in PR Company Parameters. When processing payroll, the system checks for reciprocity with the state specified in the Work Office Tax State or the Resident Tax State fields in PR Employees.
If you do not specify a job in the Job field, and the Office State field in PR Company Parameters is blank, defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from theResident Tax State field in PR Employees.
SM Work Orders:
If a job work order,
 defaults from the PR State field in
 JC Jobs.
If a customer work order, defaults from the PR State field in SM Work Orders. If you do not specify a PR State on the work order, defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from the Resident Tax State field in PR Employees.

Defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from the Resident Tax State field in PR Employees.

Defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from the Resident Tax State field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Resident Unemp State

Enter the employee's state for unemployment based
 deductions and liabilities. The system may use this state as the default for the
 Unemp
 State field when entering timecards in PR Timecard Entry. The default
 for the Unemp
 State field depends upon the settings of the Always use Employee's
 Work/Resident Unemployment State checkbox on this form and the
 Use Job or
 SM Work Order State for Unemployment State checkbox in PR Company
 Parameters (State/Local tab).
The following table displays how the Unemp State field (PR Timecard Entry) defaults based on the settings of both checkboxes.
Use Job or SM WO State
Use Employee State
Ins State Default

Defaults from the Unemp State field in PR Employees.

If you specify a job in
 the Job field (PR
 Timecard Entry, defaults from PR State field in
 JC Jobs.
If you do not specify a job in the Job field, defaults from the Unemp State field in PR Employees.
SM Work Orders:
If a job work order,
 defaults from the PR State field in
 JC Jobs.
If a customer work order, defaults from the PR State field in SM Work Orders. If you do not specify a PR State on the work order, defaults from the Unemp State field in PR Employees.

Defaults from the Unemp State field in PR Employees.

Defaults from the Unemp State field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Resident Ins State

Enter the employee's state for insurance
 state/insurance code-based deductions and liabilities. The system may use this state as
 the default for the Ins State field when entering
 timecards in PR Timecard Entry. The default for the Ins State field depends upon the
 settings of the Always use Employee's Work/Resident Insurance State checkbox on this
 form and the Use
 Job or SM Work Order State for Insurance State checkbox in PR Company
 Parameters (State/Local tab).
The following table displays how the Unemp State field (PR Timecard Entry) defaults based on the settings of both checkboxes.
Use Job or SM WO State
Use Employee State
Ins State Default

Defaults from the Ins State field in PR Employees

If you specify a job in
 the Job field (PR
 Timecard Entry), defaults from PR State field in
 JC Jobs.
If you do not specify a job in the Job field, defaults from the Ins State field in PR Employees.
SM Work Orders:
If a job work order,
 defaults from the PR State field in
 JC Jobs.
If a customer work order, defaults from the PR State field in SM Work Orders. If you do not specify a PR State on the work order, defaults from the Ins State field in PR Employees.

Defaults from the Ins State field in PR Employees.

Defaults from the Ins State field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Resident Local Codes

Enter the employee's resident local code for local-based deductions and
 liabilities. The system may use this code as the default for the Local Code field when entering
 timecards in PR Timecard Entry. The default for the Local Code field depends on the
 settings of the Work Office Local
 Code field on this form, the Always use Employee's Work/Resident Local
 Code checkbox on this form, and the Use Job or Office Local for Local Tax
 checkbox in PR Company Parameters (State/Local tab).
The following table displays how the Local field (PR Timecard Entry) defaults based on the settings of both checkboxes.
Use Job, SM WO, or Office Local
Use Employee Local
Local Default

Defaults from the Work Office Local Code field in PR Employees. If blank, the system defaults from the Resident Local Code field.

If you specify a job in the Job field (PR Timecard Entry) and the PR Local Code
 field (JC Jobs) is not blank, defaults from the PR
 Local Code field in JC Jobs.
If you specify a job in the Job field, and the
 PR Local Code
 field (JC Jobs) is blank, the default value is the Resident Local Code field in the PR Employees
 form.
If you do not specify a job in the Job field, defaults from the Office Local field in the PR Company Parameters form, if it is not blank.
If you do not specify a job in the Job field, and the Office Local field in PR Company Parameters is blank, defaults from the Work Office Local Code field in PR Employees. If that field is blank, defaults from the Resident Local Code field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR
 Local Code field in the JC Jobs form, if it is not
 blank. If the job's PR Local Code
 field is blank, the default value is the Resident Local Code field in the PR Employees
 form.
If a customer work order, defaults from the PR Local Code field in SM Work Orders. If you do not specify a PR Local Code on the work order, defaults as blank.

Defaults from the Work Office Local Code field in PR Employees. If that field is blank, defaults from the Resident Local Code field in PR Employees.
 If both the Work Office Local Code and the Resident Local Code fields in PR Employees are blank, defaults as blank.

Defaults from the Work Office Local Code field in PR Employees. If that field is blank, defaults from the Resident Local Code field in PR Employees.
 If both the Work Office Local Code and the Resident Local Code fields in PR Employees are blank, defaults as blank.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Work Office Tax State

Enter the employee's work office state for tax state
 based deductions and liabilities. The system may use this state as the default for the
 Tax
 State field when entering timecards in PR Timecard Entry. The default
 for the Tax
 State field depends on the settings of the Always use Employee's
 Work/Resident Tax State checkbox on this form and the Use Job, SM Work Order
 or Office State for Tax State checkbox in PR Company Parameters
 (State/Local tab).
The following table displays how the Tax State field (in PR Timecard Entry) defaults based on the settings of both checkboxes.
Use Job, SM WO, or Office State
Use Employee State
Tax State Default

Defaults from the Work Office Tax State field in PR Employees. If blank, the system defaults from the Resident Tax State field.

If you specify a job in
 the Job field (PR
 Timecard Entry), defaults from the PR
 State field in JC Jobs. When processing payroll, the
 system checks for reciprocity with the state specified in the
 Work Office Tax
 State or the Resident Tax
 State fields in PR Employees.
If you do not specify a job in the Job field, defaults from the Office State field in PR Company Parameters. When processing payroll, the system checks for reciprocity with the state specified in the Work Office Tax State or the Resident Tax State fields in PR Employees.
If you do not specify a job in the Job field, and the Office State field in PR Company Parameters is blank, defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from the Resident Tax State field in PR Employees.
SM Work Orders:
If a job work order,
 defaults from the PR State field in
 JC Jobs.
If a customer work order, defaults from the PR State field in SM Work Orders. If you do not specify a PR State on the work order, defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from the Resident Tax State field in PR Employees.

Defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from the Resident Tax State field in PR Employees.

Defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from the Resident Tax State field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Work Office Local Code

Enter the employee's work office local code for
 local-based deductions and liabilities. The system may use this code as the default for
 the Local
 Code field when entering timecards in PR Timecard Entry. The default for
 the Local
 Code field depends on the settings of the Always use Employee's
 Work/Resident Local Code checkbox on this form and the Use Job, SM Work Order
 or Office Local for Local Tax checkbox in PR Company Parameters
 (State/Local tab).
The following table displays how the Local Code field (PR Timecard Entry) defaults based on the settings of both checkboxes.
Use Job, SM WO, or Office Local
Use Employee Local
Local Default

Defaults from the Work Office Local Code field in PR Employees. If blank, the system defaults from the Resident Local Code field.

If you specify a job in
 the Job field (PR
 Timecard Entry) and the PR Local Code field (JC Jobs) is not blank,
 defaults from the PR Local Code
 field in JC Jobs.
If you specify a job in
 the Job field, and the PR Local Code
 field (JC Jobs) is blank, the default value is the Resident Local Code field in the PR Employees
 form.
If you do not specify a job in the Job field, defaults from the Office Local field in the PR Company Parameters form, if it is not blank.
If you do not specify a job in the Job field, and the Office Local field in PR Company Parameters is blank, defaults from the Work Office Local Code field in PR Employees. If that field is blank, defaults from the Resident Local Code field in PR Employees.
SM Work Orders:
If a job work order,
 defaults from the PR Local Code
 field in the JC Jobs form, if it is not blank. If the job's
 PR Local Code
 field is blank, the default value is the Resident Local Code field in the PR Employees
 form.
If a customer work order, defaults from the PR Local Code field in SM Work Orders. If you do not specify a PR Local Code on the work order, defaults as blank.

Defaults from the Work Office Local Code field in PR Employees. If that field is blank, defaults from the Resident Local Code field in PR Employees.
 If both the Work Office Local Code and the Resident Local Code fields in PR Employees are blank, defaults as blank.

Defaults from the Work Office Local Code field in PR Employees. If that field is blank, defaults from the Resident Local Code field in PR Employees.
 If both the Work Office Local Code and the Resident Local Code fields in PR Employees are blank, defaults as blank.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

##  GL Co#

 Enter the employee’s default GL Company number, which is used for non-job timecard entries. Initially defaults the GL Company assigned in the PR Company Parameters.
 If you initialized this employee from HR, defaults the GL Company assigned in the PR Company Parameters.

## Shift

Specify the shift to use as a default when
 entering timecards (PR Timecard Entry) for this employee; may be overridden by crew (in PR
 Crews). The crew shift only defaults if the employee is assigned to a crew and the crew is
 specified during timecard entry. If no default shift is specified here or at the crew
 level, shift defaults from the previously entered timecard.
Changes to this field update the Shift field
 in HR Resources (Payroll Info tab) for this employee.
Note: If you initialize crew timecards and no shift is defined for the crew, timecards default as shift '1', regardless of whether a default shift is entered here.

## Always use Employee's Work /Resident Tax State

Check this box to have the system always default the
 employee's tax state (from PR Employees) when you enter timecard records in PR Timecard
 Entry. The system will default the tax state from the Work Office Tax
 State field. If that field is blank, the system defaults from the
 Resident Tax
 State field.
Defaults for the Tax State field in PR Timecard Entry also depend on the setting of the Use Job, SM Work Order or Office State for Tax State checkbox in PR Company Parameters (State/Local tab). The following table displays how the Tax State field defaults based on these two checkboxes.
Use Job, SM WO, or Office State
Use Employee State
Tax State Default

Defaults from the Work Office Tax State field in PR Employees. If blank, the system defaults from the Resident Tax State field.

If you specify a job in
 the Job field (PR
 Timecard Entry), defaults from the PR
 State field in JC Jobs. When processing payroll, the
 system checks for reciprocity with the state specified in the
 Work Office Tax
 State or the Resident Tax
 State fields in PR Employees.
If you do not specify a job in the Job field, defaults from the Office State field in PR Company Parameters. When processing payroll, the system checks for reciprocity with the state specified in the Work Office Tax State or the Resident Tax State fields in PR Employees.
If you do not specify a job in the Job field, and the Office State field in PR Company Parameters is blank, defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from the Resident Tax State field in PR Employees.
SM Work Orders:
If a job work order,
 defaults from the PR State field in
 JC Jobs.
If a customer work order, defaults from the PR State field in SM Work Orders. If you do not specify a PR State on the work order, defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from the Resident Tax State field in PR Employees.

Defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from the Resident Tax State field in PR Employees.

Defaults from the Work Office Tax State field in PR Employees. If that field is blank, defaults from the Resident Tax State field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Always Use Employee's Work/Resident Unemployment State

Select this checkbox to have the system always
 default the employee's unemployment state from the Unemp State field on this form when
 you enter timecard records in PR Timecard Entry.
Defaults for the Unemp State in PR Timecard Entry also depend on the setting of the Use Job or SM Work Order State for Unemployment State checkbox in PR Company Parameters (State/Local) tab. The following table displays how the Unemp State field defaults based on these two checkboxes.
Use Job or SM WO State
Use Employee State
Ins State Default

Defaults from the Unemp State field in PR Employees.

If you specify a job in
 the Job field (PR
 Timecard Entry, defaults from PR State field in
 JC Jobs.
If you do not specify a job in the Job field, defaults from the Unemp State field in PR Employees.
SM Work Orders:
If a job work order,
 defaults from the PR State field in
 JC Jobs.
If a customer work order, defaults from the PR State field in SM Work Orders. If you do not specify a PR State on the work order, defaults from the Unemp State field in PR Employees.

Defaults from the Unemp State field in PR Employees.

Defaults from the Unemp State field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Always Use Employee's Work/Resident Insurance State

Check this box to have the system always default the employee's insurance state from the Ins State field on this form when you enter timecard records in PR Timecard Entry.
Defaults for the Ins State field in PR Timecard Entry also depend on the setting of theUse Job or SM Work Order State for Insurance State checkbox in PR Company Parameters (State/Local) tab. The following table displays how the Ins State field defaults based on these two checkboxes.
Use Job or SM WO State
Use Employee State
Ins State Default

Defaults from the Ins State field in PR Employees

If you specify a job in
 the Job field (PR
 Timecard Entry), defaults from PR State field in
 JC Jobs.
If you do not specify a job in the Job field, defaults from the Ins State field in PR Employees.
SM Work Orders:
If a job work order,
 defaults from the PR State field in
 JC Jobs.
If a customer work order, defaults from the PR State field in SM Work Orders. If you do not specify a PR State on the work order, defaults from the Ins State field in PR Employees.

Defaults from the Ins State field in PR Employees.

Defaults from the Ins State field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Always use Employee's Work/Resident Local Code

Check this box to have the system always default the
 employee's local code (from PR Employees) when you enter timecard records in PR Timecard
 Entry. The system will default the tax state from the Work Office Local
 Code field. If that field is blank, the system defaults from the
 Resident
 Local Code field.
Defaults for the Local field in PR Timecard Entry also depend on the setting of the Use Job, SM Work Order or Office Local for Local Tax checkbox in PR Company Parameters (State/Local tab). The following table displays how the Local field defaults based on these two checkboxes.
Use Job, SM WO, or Office Local
Use Employee Local
Local Default

Defaults from the Work Office Local Code field in PR Employees. If blank, the system defaults from the Resident Local Code field.

If you specify a job in
 the Job field (PR
 Timecard Entry) and the PR Local Code field (JC Jobs) is not blank,
 defaults from the PR Local Code
 field in JC Jobs.
If you specify a job in
 the Job field, and the PR Local Code
 field (JC Jobs) is blank, the default value is the Resident Local Code field in the PR Employees
 form.
If you do not specify a job in the Job field, defaults from the Office Local field in the PR Company Parameters form, if it is not blank.
If you do not specify a job in the Job field, and the Office Local field in PR Company Parameters is blank, defaults from the Work Office Local Code field in PR Employees. If that field is blank, defaults from the Resident Local Code field in PR Employees.
SM Work Orders:
If a job work order,
 defaults from the PR Local Code
 field in the JC Jobs form, if it is not blank. If the job's
 PR Local Code
 field is blank, the default value is the Resident Local Code field in the PR Employees
 form.
If a customer work order, defaults from the PR Local Code field in SM Work Orders. If you do not specify a PR Local Code on the work order, defaults as blank.

Defaults from the Work Office Local Code field in PR Employees. If that field is blank, defaults from the Resident Local Code field in PR Employees.
 If both the Work Office Local Code and the Resident Local Code fields in PR Employees are blank, defaults as blank.

Defaults from the Work Office Local Code field in PR Employees. If that field is blank, defaults from the Resident Local Code field in PR Employees.
 If both the Work Office Local Code and the Resident Local Code fields in PR Employees are blank, defaults as blank.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Always use Employee's Work/Resident Standard Insurance Code

Check this box to always use the employee’s
 standard insurance code (Ins Code field) when entering timecard
 records.
Do not check this box to have the system base
 the default on the setting of the Insurance Based on Phase or SM Work Order
 Scope checkbox in PR Company Parameters.

##  Earnings Code

 Enter the earnings code that will be used as a default when entering timecards for this Employee.

## Update Auto Earnings

The Update Auto Earnings checkbox on the PR Employees form,
 Add'l Info tab.
Select this checkbox to automatically update PR Automatic
 Earnings with any changes that you make to the Salary and/or Earning Code fields. Once selected, if the earnings code specified for this employee in PR Employees is also set up for the employee in PR Automatic Earnings, the system updates the salary amount to the Rate/Amount field for the
 employee/earnings code in PR Automatic Earnings. If multiple auto earn sequences exist for the specified earnings code, the system proportionately distributes the salary amount to each applicable sequence. For more information, see [About Updating Salary Changes to Auto Earnings](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-updating-salary-changes-to-auto-earnings).
Note: If this checkbox is selected and you change an employee's salary via the HR Resource Salary History form, the system updates the earnings code sequences in PR Automatic Earnings once you run the HR Update Benefit/Salary to PR form.

If you do not select this checkbox, salary changes do not update to PR Automatic Earnings.

## Weekly Hours

Enter the number of hours that the employee
 works in a week. You must enter 0.00 or greater.
If you enter a number greater than 0.00, and the
 Salary field contains a number greater than 0.00, the system will default a
 value (Salary divided by Weekly Hours) into the Hourly Rate
 field.
Australian Users
The system uses this field in conjunction with
 the Hourly
 Rate field when calculating redundancy or "in lieu of notice" ETP payments.
 When calculating ETPs, the system multiplies this number by the number of eligible weeks to
 produce the total hours eligible for ETPs. This total hours is then multiplied by the
 Hourly
 Rate.
If you are generating ETPs for this employee,
 it is recommended that you enter the accurate hours in this field and not leave it at the
 default of 0.00 or ETP calculations will be incorrect.

##  Salary

The Salary field on the PR Employees form, Add'l Info tab.
 Enter the salary amount for this employee, if appropriate. The default is 0.00. Salaries are typically set up to be posted automatically in PR Post Auto Earnings; therefore, it is not necessary to set them up here.
Note: Alabama state withholding calculations use this field to determine
 whether an employee is subject to Alabama OT tax exemption. If an employee is set up
 with a value other than 0.00 in this field, that employee is automatically excluded
 from Alabama OT tax exemption.

## Hourly Rate

Enter the hourly rate for this employee. The PR Timecard Entry form compares this rate to the posted Craft/Class rate, if there is one, and then defaults to the higher of the two rates. The default is 0.00.
If you always pay this employee-based on the craft/template rates, it is recommended their hourly rate not be set up here. It will not be used (unless higher) and it would have to be updated manually when changed.

##  JC Fixed Rate

 Enter the JC Fixed Rate that will be used to override actual labor and burden costs when updating Job Cost for this employee. If this rate is not 0.00, then Job Cost will be charged using this rate times the hours posted on each job.

##  EM Fixed Rate

 Enter the fixed rate that will be used to override actual labor and burden costs when updating Equipment Management for this employee for mechanic’s timecards. If this rate is not 0.00, then EM will be charged using this rate times the hours posted to each piece of equipment.

## SM Fixed Rate

The SM Fixed Rate field on the PR Employees form, Add'l Info tab.
For Customer SM Work Orders only.
Enter the fixed rate to use for calculating
 override labor costs when updating customer work orders for this employee's
 labor hours.
Note: The rate you specify here is assumed to represent the fully burdened amount cost.

 When you run PR Ledger Update, the system updates the Actual Cost for the work completed labor line (in SM Work Orders) as follows:

- If the SM Pay Type specified for the work completed labor line has a Cost Method of 0 - Multiplier, the system applies the Factor defined (in SM Pay Types) for the work completed line's pay type to the rate specified here to determine the Actual Cost.Example: If the employee's SM Fixed Rate is 50.00, the pay type's Factor is 2.00, and 10 hours are posted to the work completed line, the Actual Cost will be $1,000 ((50.00 x 2.00) x 10).

-

If the SM Pay Type specified for the work completed labor line has a Cost Method of 1 - Dollar Rate, the system uses the rate defined here to calculate the Actual Cost for the work completed labor line.Example: If the employee's SM Fixed Rate is 50.00 and 10 hours are posted to the work completed line, the Actual cost will be $500 (50.00 x 10).

The fixed rate override is debited to the appropriate GL account defined
 in SM Departments; the offsetting entry is made to the SM Fixed Rate GL Account specified
 in PR Departments.
Leave this field set to 0.00 if not
 using a fixed rate to calculate override labor/burden costs when updating customer work
 orders for this employee's labor hours. Regardless of the Cost Method specified for the work completed line's SM Pay Type, if no SM Fixed Rate is specified here, the system uses the actual labor costs and burden costs from PR to update Actual Cost for the work completed labor line.

## Overtime

The Overtime field in the PR Employees form
Select how you want automatic overtime to be
 calculated for this Employee.

- N-None – No overtime is calculated, employee is exempt.

- D-Daily – Always calculate overtime for this employee on a daily basis using the OT Schedule specified. Overtime is also calculated if 40 hours per week is exceeded.

- W-Weekly – Calculate overtime on a weekly basis only
 (more than 40 hours per week).Note: Weekly OT is applied after all of the daily OT
 calculations are complete.

- C-Craft – Overtime is based on the craft and craft
 template that this employee works under. If the craft or craft template has been
 assigned an OT Schedule, then the daily “rules” at either of those levels is used.
 All of an employee’s time posted to the craft for the day is accumulated to see if
 overtime should be calculated. If different overtime rules apply to the various
 templates that this employee has worked under, the order of timecard entry determines
 which jobs or work orders (SM Work Order timecards) and how much overtime is
 calculated. Weekly overtime is applied after all of the daily overtime calculations
 are complete.

- J-Job – Overtime is calculated based on
 the OT Schedule assigned to the job in the JC Jobs. If two jobs are assigned the same
 overtime schedule, the jobs will be combined when calculating overtime. If you want
 to process overtime independently for each job, you will need to assign different
 overtime schedules to each job. Weekly overtime is applied after all of the daily
 overtime calculations are complete.

- P-Posting Seq - This method provides another option for calculating daily overtime and applies to organizations who must adhere to both craft overtime rules and job overtime rules. Overtime is calculated only after considering all posting sequences (timecard lines) in each day and applying overtime schedule rules on a line-by-line basis, from top to bottom. The system considers overtime schedules from the job/project, the job's craft template, and the craft master.
If on a single line, the system encounters more than one overtime schedule that could apply to that line, it applies the schedule that is more generous.
Important:The order that you enter timecard lines in the PR Timecard Entry form matters.Because the system applies overtime schedule rules starting with the top timecard line and working toward to bottom line, a continuous, daily overtime calculation such as this that crosses jobs, crafts, and craft templates means the order that you enter timecard lines can affect how the system calculates wages and attributes those costs to jobs. You may encounter scenarios where if the timecard line entries are reversed, the wages are different.
Here's a brief video demonstrating the results of this setting.
Note: You must use a browser on your local computer to view this video, and not a browser in the cloud. If you are currently using a cloud-based browser, copy this page's URL and paste it into a web browser on your local computer.

Note: Changes to this field update the Overtime field in the HR Resources
 form (Payroll Info tab) for this employee.

## OT Schedule

This field is accessible when you select
 ‘D-Daily’ in the Overtime field.
Specify a valid OT Schedule if this employee has been set up for daily overtime.
Note: Changes to this field update the OT Schedule field in
 HR Resources (Payroll Info tab) for this employee.

##  EM Co #

 Enter the EM company that applies to this employee. You must enter a company in this field, before assigning a piece of equipment to this employee in the Equipment Code field. When you enter a company in this field, the system defaults the company into the EM CO# field in PR Timecard Entry and the EMCo field in PR Crews (Crew Members tab).

##  Equipment Code

 Enter the piece of equipment that you want to assign to this employee. Before entering an equipment code here, you must enter a company in the EM CO # field. When you enter a piece of equipment in this field, the system defaults the company into the Equip field in PR Timecard Entry and the Equipment field in PR Crews (Crew Members tab).

## Occupational Category

The Occupational Category field in PR Employees, Add'l Info tab.
Enter a valid occupational category (as defined in PR Occupational
 Categories). For more information, see [PR Occupational Categories: Occup Category](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-occupational-categories-form/field-definitions-pr-occupational-categories-form#ID-00039879--en).
Entry in this field is required for unemployment reporting in the
 following states:
StateAffected Aatrix Unemployment
 Report
AlaskaAK TQ01C eFile Report
LouisianaLA LDOL ES4 BC/61 eFile
 Reports
South CarolinaSC UCE-120 Report
WashingtonWA 5208 A eFile Report
West VirginiaWV WVUC-A-154 eFile
 Report

## Category Status

Category Status field on the PR Employees form, Add'l Info
 tab.
Enter a category status for use on the PR Department of Labor EEO-1 Report (ReportID 795)
 and/or PR Certified Report - eMars (ReportID 1315).
When you change this employee’s category status, the system offers to
 update the same-named field in the HR Resources form (Payroll Info tab) if the Occupation
 Category checkbox is selected in the HR Company Parameters form (PR Update Options
 section).
Note: Check with your state to determine the category status requirements.If you file
 electronically for NY DOT (PR Generate Champ-CM Exports), you must enter A, J, or T.

## Geographic Code

The Geographic Code field on the PR Employees form, Addl Info tab.
Enter the geographic code for this employee that identifies where the employee is predominately working. Up to 15 characters allowed.
Typically used by states to capture census data.
Note: For Alaska, this field is required and populates the geographic code when running the Alaska Quarterly Contribution Report (AK TQ01C) via Aatrix.

## Timesheet Reviewer Group

If you are using [timesheet entry functionality](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets), enter the timesheet reviewer
 group for this employee. Press F4 for a list of active timesheet
 reviewer groups. Press F5 to connect to HQ Reviewer Group for
 reviewer-group management.
Members of this group will review and approve timesheets that are entered for this employee using PR My Timesheet Approval.

## Garnishment Allocation

Specify how garnishments will be allocated.

- Prorate– Select this option if garnishment allocations will be divided proportionally among the qualifying garnishments.

- Divide Equally – Select this option if garnishment allocations will be divided equally among the qualifying garnishments.

Note: This feature can be used with any type of garnishment allocation; however, if an employee has multiple allocations (i.e., tax levy, child support, student loan, etc.), you can only set up this up for one allocation type. For example, if an employee has both child support allocations and any other type of allocation, you would typically use this for the child support allocations.

## Withholding Limit Percentage

Specify the maximum percentage of disposable income eligible for garnishment allocations. When qualifying garnishment deductions are calculated, the garnishment amounts will be reduced so that they do not exceed the maximum amount allowable.
Note: This feature can be used with any type of garnishment allocation; however, if an employee has multiple allocations (i.e., tax levy, child support, student loan, etc.), you can only set up this up for one allocation type. For example, if an employee has both child support allocations and any other type of allocation, you would typically use this for the child support allocations.

## Garn Group

Specify which garnishment group (from PR Garnish Group) will be used to calculate this employee's disposable income for garnishment allocations.
Note: This feature can be used with any type of garnishment allocation; however, if an employee has multiple allocations (i.e., tax levy, child support, student loan, etc.), you can only set up this up for one allocation type. For example, if an employee has both child support allocations and any other type of allocation, you would typically use this for the child support allocations.

## CHAMP Trade Seq# Override

Enter the trade sequence number for this
 employee, if applicable. A list of valid trade sequence numbers can be found in the
 “Champ-CM Equal Opportunity Management Software” requirements.
Entry here will override the "Trade Seq#"
 specified at the craft level (in PR Crafts) and will be used when running "PR Generate
 CHAMP-CM Exports".
Note: This is a required field for NY DOT electronic filing. Other states may also require this information; check your state’s requirements to determine if this information is needed.

##  NAICS Code

 The NAICS Code field in the PR Employees form, Add'l Info tab
Enter the NAICS code for this employee. The system uses the this value when you generate unemployment reports in the PR Unemployment Process form.

##  Deduction for Living in Prescribed Zone

 The field is for Canadian users only.
 Enter the annual deduction amount for living in a prescribed zone from Form TD1.

##  Deductions Authorized by Tax Services Office

 The field is for Canadian users only.
 Enter the annual deductions amount for this employee as notified by a tax services office or tax center. Examples of the F1 amount include child care expenses or alimony/support payments.

##  Capital Stock Registered Federally

 The field is for Canadian users only.
 Enter the deduction amount for the purchase of approved shares of capital stock of a prescribed labour-sponsored venture capital corporation.

##  Capital Stock Registered in Saskatchewan

 The field is for Canadian users only.
 Enter the deduction amount for the purchase of approved shares of capital stock of a prescribed labour-sponsored venture capital corporation in Saskatchewan. This only applies to employees paying tax in Saskatchewan.

## Indian Tax Exempt Status

Indian Tax Exempt Status checkbox in the PR Employees form, Add'l Info tab
This checkbox displays for Canadian companies only.
Select this checkbox if this employee is a First Nations person that meets the criteria for salary or wage tax exemption.
When you process payroll, Vista omits both Federal and Provincial withholding calculations for this employee. This setting does not impact other deductions including those on the Add’l Dedn/Liab tab.
When
 you process T4s, Vista omits the amount of their exempt wages paid from Box 14 and instead places them in
 'Other information' along with Code 71.

## Additional Source Deductions

 This field is for Canadian users only, and is intended to be used by employers in Quebec.
 Enter the annual amount from line 19 of the employee's TP-1015.3-V form (Source Deductions Return).

## Authorized Source Deductions

 The field is for Canadian users only, and is intended to be used by employers in Quebec.
 Enter the annual amount from line 10 of the employee's TP-1016-V form (Application for a Reduction in Source Deductions of Income Tax for an Individual or a Self-Employed Person).

## Exempt from Additional Health Contribution

 The field is for Canadian users only, and is intended to be used by employers in Quebec.
 Unchecked by default.
Check this box for an employee who is exempt from health contributions.

## Always Calculate QPIP

 The field is displayed to Canadian users only, and is intended to be used by employers in Quebec.
 Select this checkbox for an employee who lives and works outside of Quebec. Checking this box will ensure that the system always calculates QPIP, even though the employee's tax province is not Quebec.
Note: Employees who work for a company based in Quebec but who never physically perform work in Quebec are still subject to employee and employer QPIP premiums. Reference Revenu Quebec document: RL-1 Slip_RL-1.G-V, section 3.2.2.2.
Checking this box will also ensure that the
 system properly applies the correct Reduced Employment Insurance (EI) Limit value. (This
 value can be overridden in [PR Employee Dedns/Liabs](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form) by checking the Override Standard
 Limit box and entering an amount in the Rate/Amount field.)

## Print Paycheque in French

 The field is for Canadian users only.
Defaults to unchecked.
Select this checkbox to print the pay period type and legal amount on pay cheques, pay stubs, and/or EFT remittance stubs in French for this employee. If the checkbox is selected, these items will also use French number formatting. If left unchecked, the pay period type, legal amount, and number formatting will be in English.
The following bilingual reports must be used in order to print pay cheques, pay stubs, and EFT remittance stubs in French (box checked). These reports can also be used to print in English (box unchecked):

- PR Cheque Print - CA Bilingual

- PR Cheque Print Stub - CA Bilingual

- PR Cheque Print Stub By Employee - CA Bilingual

- PR EFT Remittance - CA Bilingual

- PR EFT Remittance By Employee - CA Bilingual

Note: If this checkbox is selected, but reports other than the bilingual reports are selected in PR Company Parameters, then the pay period type, legal amount, and number formatting will be in English.
For more information on selecting bilingual reports, see [Set up Pay Cheques, Pay Stubs, and EFT Remittances to Print in Bilingual French/English](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/set-up-pay-cheques-pay-stubs-and-eft-remittances-to-print-in-bilingual-frenchenglish).

## Start Fortnight Number

The Start Fortnight Number field on the PR Employees form, Add'l Info tab.
Enter the number representing the first JobKeeper fortnightly period for which this employee received reimbursable payment. Press F4 for a list of the available fortnightly periods, along with the respective calendar dates that mark the beginning and ending of each period.
Note: The ATO requires that you not "forward date" fortnight numbers; therefore, you should not enter the Start Fortnight Number until the time period has actually started. For example, if the Start Fortnight Number is 6 (time period 08/06/2020 - 21/06/2020), do not enter it before 08 June 2020.

## Finish Fortnight Number

The Finish Fortnight Number field on the PR Employees form, Add'l Info tab.
Enter the number representing the first full JobKeeper fortnightly period after the final period for which this employee received reimbursable payment. Press F4 for a list of the available fortnightly periods, along with the respective calendar dates that mark the beginning and ending of each period.
For example, if the employee's final fortnightly period is 07/12/2020 - 20/12/2020 (Fortnight Number 19), you will enter 20 in this field.
Note: You will only need to enter a value in this field if an employee exits the program while it is still up and running.

## Tier Level Number

(Australia) The Tier Level Number field on the PR Employees form, Add'l Info tab.
Enter the tier level number for this employee.

- Tier 1 - Use this level for employees that worked 80 or more hours in the reference period.

- Tier 2 - Use this level for employees that worked less than 20 hours in the reference period.

Note: If the employee participates in the JobKeeper Payment program during the extension periods (fortnightly periods 14-26), you must enter a tier level in this field. If no tier level is specified, it may result in a delay or prevention of reimbursement from the ATO (Australian Taxation Office).

## New Hire

The New Hire drop-down on the PR Employees form, Add'l Info
 tab.

- MNM - Nominate employee — Select this option if this employee is a new hire and is participating in the JobMaker Hiring Credit (JMHC) program for the first time as your employee (that is, has no prior history of participation in the JobMaker program as your employee). When generating submission data (that includes this employee) in PR STP Generate Data, the system creates a single pseudo-allowance record representing this nomination in the employee's allowance collection for the submission.Note: You should also select this option if the employee is a rehire, but is participating in the JobMaker program for the first time as your employee (that is, has no prior history of participation in the JobMaker program as your employee).

- MNMX - Revoke prior nomination — Select this option if this employee was erroneously nominated for participation in the JobMaker program and you reported the nomination in a prior submission to the ATO. When you generate data for a new submission, the system creates a single pseudo-allowance record representing the revoked nomination in the employee's allowance collection for the submission.Note: You should revoke a prior erroneous nomination for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission or a special, out-of-cycle STP Update Event ("Fix YTD") submission.

Leave this field blank if this employee does not meet the eligibility requirements for the JobMaker program.

## Recent Rehire

The Recent Rehire drop-down on the PR Employees form, Add'l
 Info tab.

- MRM - Renominate employee — Select this option if this employee is a recent rehire and is participating in the JobMaker Hiring Credit (JMHC) program for the second time as your employee (that is, the employee was nominated for participation in the JobMaker program during a previous period of employment with your company). When generating submission data (that includes this employee) in PR STP Generate Data, the system creates a single pseudo-allowance record representing the renomination in the employee's allowance collection for the submission.

- MRMX - Revoke prior renomination — Select this option if this employee was erroneously renominated for participation in the JobMaker program and you reported the renomination in a prior submission to the ATO. When you generate data for a new submission, the system creates a single pseudo-allowance record representing the revoked renomination in the employee's allowance collection for the submission.Note: You should revoke a prior erroneous renomination for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission or a special, out-of-cycle STP Update Event ("Fix YTD") submission.

Leave this field blank if this employee does not meet the eligibility requirements for the JobMaker program.

## Period 1

The Period 1 drop-down on the PR Employees form, Add'l Info tab.

- M01 - Declare employee met
 minimum hours test — Select this option if this employee
 satisfied the minimum hours requirement for this period; that is, completed
 a minimum of 20 hours of work per week on average for the specified period
 (either the hours for which the employee is being paid or the hours the
 employee worked). When generating submission data (that includes this
 employee) in PR STP Generate Data, the system creates a single
 pseudo-allowance record representing this confirmation in the employee's
 allowance collection for the submission.Note: You must
 confirm the employee's eligibility for this period no later than the STP
 reporting due date (three days before the end of the relevant claim
 period) in order to make a claim for the employee for this period. For
 more information about reporting due dates, see the [ATO website](https://www.ato.gov.au/).

- M01X - Revoke prior declaration — Select this option if you erroneously confirmed this employee's minimum hours requirement for this period and you reported the declaration in a prior submission to the ATO. When generating submission data (that includes this employee) in PR STP Generate Data, the system creates a single pseudo-allowance record representing the revoked confirmation in the employee's allowance collection for the submission.Note: You should revoke a prior erroneous confirmation for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission, or a special, out-of-cycle STP Update Event ("Fix YTD") submission.

Leave this field blank if the employee did not meet the minimum hours requirement for this reporting period.

## Period 2

The Period 2 drop-down on the PR Employees form, Add'l Info
 tab.

- M02 -
 Declare employee met minimum hours test — Select this option
 if this employee satisfied the minimum hours requirement for this period;
 that is, completed a minimum of 20 hours of work per week on average for the
 specified period (either the hours for which the employee is being paid or
 the hours the employee worked). When generating submission data (that
 includes this employee) in PR STP Generate Data, the system
 creates a single pseudo-allowance record representing this confirmation in
 the employee's allowance collection for the submission.Note: You must confirm the employee's eligibility for
 this period no later than the STP reporting due date (three days before
 the end of the relevant claim period) in order to make a claim for the
 employee for this period. For more information about reporting due
 dates, see the [ATO website](https://www.ato.gov.au/).

- M02X - Revoke prior declaration — Select this option if you erroneously confirmed this employee's minimum hours requirement for this period and you reported the declaration in a prior submission to the ATO. When generating submission data (that includes this employee) in PR STP Generate Data, the system creates a single pseudo-allowance record representing the revoked confirmation in the employee's allowance collection for the submission.Note: You should revoke a prior erroneous confirmation for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission, or a special, out-of-cycle STP Update Event ("Fix YTD") submission.

Leave this field blank if the employee did not meet the minimum hours requirement for this reporting period.

## Period 3

The Period 3 drop-down on the PR Employees form, Add'l Info
 tab.

- M03 -
 Declare employee met minimum hours test — Select this option
 if this employee satisfied the minimum hours requirement for this period;
 that is, completed a minimum of 20 hours of work per week on average for the
 specified period (either the hours for which the employee is being paid or
 the hours the employee worked). When generating submission data (that
 includes this employee) in PR STP Generate Data, the system
 creates a single pseudo-allowance record representing this confirmation in
 the employee's allowance collection for the submission.Note: You must confirm the employee's eligibility for
 this period no later than the STP reporting due date (three days before
 the end of the relevant claim period) in order to make a claim for the
 employee for this period. For more information about reporting due
 dates, see the [ATO website](https://www.ato.gov.au/).

- M03X - Revoke prior declaration — Select this option if you erroneously confirmed this employee's minimum hours requirement for this period and you reported the declaration in a prior submission to the ATO. When generating submission data (that includes this employee) in PR STP Generate Data, the system creates a single pseudo-allowance record representing the revoked confirmation in the employee's allowance collection for the submission.Note: You should revoke a prior erroneous confirmation for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission, or a special, out-of-cycle STP Update Event ("Fix YTD") submission.

Leave this field blank if the employee did not meet the minimum hours requirement for this reporting period.

## Period 4

The Period 4 drop-down on the PR Employees form, Add'l Info
 tab.

- M04 -
 Declare employee met minimum hours test — Select this option
 if this employee satisfied the minimum hours requirement for this period;
 that is, completed a minimum of 20 hours of work per week on average for the
 specified period (either the hours for which the employee is being paid or
 the hours the employee worked). When generating submission data (that
 includes this employee) in PR STP Generate Data, the system
 creates a single pseudo-allowance record representing this confirmation in
 the employee's allowance collection for the submission.Note: You must confirm the employee's eligibility for
 this period no later than the STP reporting due date (three days before
 the end of the relevant claim period) in order to make a claim for the
 employee for this period. For more information about reporting due
 dates, see the [ATO website](https://www.ato.gov.au/).

- M04X - Revoke prior declaration — Select this option if you erroneously confirmed this employee's minimum hours requirement for this period and you reported the declaration in a prior submission to the ATO. When generating submission data (that includes this employee) in PR STP Generate Data, the system creates a single pseudo-allowance record representing the revoked confirmation in the employee's allowance collection for the submission.Note: You should revoke a prior erroneous confirmation for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission, or a special, out-of-cycle STP Update Event ("Fix YTD") submission.

Leave this field blank if the employee did not meet the minimum hours requirement for this reporting period.

## Period 5

The Period 5 drop-down on the PR Employees form, Add'l Info
 tab.

- M05 -
 Declare employee met minimum hours test — Select this option
 if this employee satisfied the minimum hours requirement for this period;
 that is, completed a minimum of 20 hours of work per week on average for the
 specified period (either the hours for which the employee is being paid or
 the hours the employee worked). When generating submission data (that
 includes this employee) in PR STP Generate Data, the system
 creates a single pseudo-allowance record representing this confirmation in
 the employee's allowance collection for the submission.Note: You must confirm the employee's eligibility for
 this period no later than the STP reporting due date (three days before
 the end of the relevant claim period) in order to make a claim for the
 employee for this period. For more information about reporting due
 dates, see the [ATO website](https://www.ato.gov.au/).

- M05X - Revoke prior declaration — Select this option if you erroneously confirmed this employee's minimum hours requirement for this period and you reported the declaration in a prior submission to the ATO. When generating submission data (that includes this employee) in PR STP Generate Data, the system creates a single pseudo-allowance record representing the revoked confirmation in the employee's allowance collection for the submission.Note: You should revoke a prior erroneous confirmation for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission, or a special, out-of-cycle STP Update Event ("Fix YTD") submission.

Leave this field blank if the employee did not meet the minimum hours requirement for this reporting period.

## Period 6

The Period 6 drop-down on the PR Employees form, Add'l Info
 tab.

- M06 -
 Declare employee met minimum hours test — Select this option
 if this employee satisfied the minimum hours requirement for this period;
 that is, completed a minimum of 20 hours of work per week on average for the
 specified period (either the hours for which the employee is being paid or
 the hours the employee worked). When generating submission data (that
 includes this employee) in PR STP Generate Data, the system
 creates a single pseudo-allowance record representing this confirmation in
 the employee's allowance collection for the submission.Note: You must confirm the employee's eligibility for
 this period no later than the STP reporting due date (three days before
 the end of the relevant claim period) in order to make a claim for the
 employee for this period. For more information about reporting due
 dates, see the [ATO website](https://www.ato.gov.au/).

- M06X - Revoke prior declaration — Select this option if you erroneously confirmed this employee's minimum hours requirement for this period and you reported the declaration in a prior submission to the ATO. When generating submission data (that includes this employee) in PR STP Generate Data, the system creates a single pseudo-allowance record representing the revoked confirmation in the employee's allowance collection for the submission.Note: You should revoke a prior erroneous confirmation for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission, or a special, out-of-cycle STP Update Event ("Fix YTD") submission.

Leave this field blank if the employee did not meet the minimum hours requirement for this reporting period.

## Period 7

The Period 7 drop-down on the PR Employees form, Add'l Info tab.

- M07 -
 Declare employee met minimum hours test — Select this option
 if this employee satisfied the minimum hours requirement for this period;
 that is, completed a minimum of 20 hours of work per week on average for the
 specified period (either the hours for which the employee is being paid or
 the hours the employee worked). When generating submission data (that
 includes this employee) in PR STP Generate Data, the system
 creates a single pseudo-allowance record representing this confirmation in
 the employee's allowance collection for the submission.Note: You must confirm the employee's eligibility for
 this period no later than the STP reporting due date (three days before
 the end of the relevant claim period) in order to make a claim for the
 employee for this period. For more information about reporting due
 dates, see the [ATO website](https://www.ato.gov.au/).

- M07X - Revoke prior declaration — Select this option if you erroneously confirmed this employee's minimum hours requirement for this period and you reported the declaration in a prior submission to the ATO. When generating submission data (that includes this employee) in PR STP Generate Data, the system creates a single pseudo-allowance record representing the revoked confirmation in the employee's allowance collection for the submission.Note: You should revoke a prior erroneous confirmation for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission, or a special, out-of-cycle STP Update Event ("Fix YTD") submission.

Leave this field blank if the employee did not meet the minimum hours requirement for this reporting period.

## Period 8

The Period 8 drop-down on the PR Employees form, Add'l Info
 tab.

- M08 -
 Declare employee met minimum hours test — Select this option
 if this employee satisfied the minimum hours requirement for this period;
 that is, completed a minimum of 20 hours of work per week on average for the
 specified period (either the hours for which the employee is being paid or
 the hours the employee worked). When generating submission data (that
 includes this employee) in PR STP Generate Data, the system
 creates a single pseudo-allowance record representing this confirmation in
 the employee's allowance collection for the submission.Note: You must confirm the employee's eligibility for
 this period no later than the STP reporting due date (three days before
 the end of the relevant claim period) in order to make a claim for the
 employee for this period. For more information about reporting due
 dates, see the [ATO website](https://www.ato.gov.au/).

- M08X - Revoke prior declaration — Select this option if you erroneously confirmed this employee's minimum hours requirement for this period and you reported the declaration in a prior submission to the ATO. When generating submission data (that includes this employee) in PR STP Generate Data, the system creates a single pseudo-allowance record representing the revoked confirmation in the employee's allowance collection for the submission.Note: You should revoke a prior erroneous confirmation for an employee at your earliest opportunity after you have discovered the error, using either a regular, recurring STP Pay Event submission, or a special, out-of-cycle STP Update Event ("Fix YTD") submission.

Leave this field blank if the employee did not meet the minimum hours requirement for this reporting period.

## Active

Check this box if this employee is an active employee who is still posting timecards and receiving payments.
Do not check this box if this employee is not an active employee. “Inactive Employee” displays in red at the top of the screen.
Note: If you have terminated this employee and entered a
 termination date in the Term Date field, the system will display
 a warning if you re-check this box asking if you want to clear the Term Date
 field. Click Yes to clear the Term Date field or click No to leave the
 date in the field.
Note: If you change this employee's status to inactive by checking
 this box, and auto earnings have been set up for the employee, a message displays
 indicating that the employee has been changed to inactive and asks if you want to delete
 the auto earnings setup for the employee. Click Yes to delete the auto earnings setup or
 No
 to leave them intact. If you elect to delete auto earnings, they will only be deleted from
 PR. The auto earnings setup in HR Resource Benefits is left intact. Additionally, if employee has active leave codes with a balance, the system displays a
 message and prompts you to deactivate the employee's leave codes. Once you select OK,
 the Active checkbox is deselected for each applicable leave code in PR Employee Leave,
 and you can no longer edit the leave code records.

## Termination Date

Termination Date field on the PR Employees
 form, Add'l Info tab.
Enter the termination date for this employee.
Note: If an employee is rehired, once you check the
 Active box, the system will ask if you want to clear the Term Date
 field. Click Yes to clear the Term Date field or click No to leave the
 date in the field.

### For Australian Companies

When you enter a date in this field, the
 system automatically updates the Period End Date for the current reporting period (on the
 PAYG Reporting Periods tab) for an employee.
If this field is blank, the date entered here must be greater than the Most Recent Rehire Date and must be later than the Period Start Date of the current reporting period. You cannot enter a termination date if the Most Recent Rehire Date is blank.
If this field is not blank, changes to the termination date will only be allowed if both of the following conditions are met:

- The last reporting period record for the employee
 has both a Period Start Date and Period End Date matching the rehire date and
 existing termination date (respectively), and no INB Summary exists with those dates.

- The new termination date is earlier than the Final Pay Period Date of the last reporting period record.

Note: If you terminate an employee that is associated with active leave
 codes, a message displays indicating there are active leave codes with a balance, and
 asking if you want to continue and deactivate the employee's leave codes.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [About PAYG Reporting Periods (Australia)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-payg-reporting-periods-australia)

## Cessation Reason

(Australia) The Cessation Reason drop-down on the PR Employees form, Addl Info tab.
For use with STP Phase 2 only.
This drop-down is enabled only for inactive employees (that is; the Active checkbox is deselected).
Select the reason employment has ceased for this employee.

- V - Voluntary Cessation

- I - Ill Health

- D - Deceased

- R - Redundancy

- F - Dismissal

- C - Contract Cessation

- T - Transfer

## Separation Date

Australian Users
When you are making an Employment Termination
 Payment or an unused leave payment to an employee, you must enter their
 termination/separation date in this field prior to processing the payments. Once you enter
 a date in this field, the system enables the Separation for Reason of Redundancy or Early
 Retirement box. Check that box if the employee has been terminated due to
 redundancy or early retirement.
For more information, see [Automatic Payments for Terminated Employees: Australia](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia).
Canadian Users
When an employee has an interruption of earnings (for whatever reason), you must enter the last day for which the employee was paid to enable the system to create Record of Employment (ROE) records. If you do not enter a date here, the system will not create an ROE record for this employee during ROE initialization.
If the employee returns to work, you should
 clear this field and update the Most Recent Rehire Date field.
For more information, see [About Setting Up Employees for ROE Reporting](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/canada-roe/about-setting-up-employees-for-roe-reporting).

## Separation Reason

The system enables this drop-down when you
 enter a date in the Separation Date field.
Select the option that best describes the reason that this employee has been terminated.
If you select R-Redundancy,
 the system enables the Pay Redundancy checkbox on the PR Auto
 Termination Pay form which allows you to pay this employee an ETP for redundancy.
If you select P-Unsatisfactory Work
 Performance, M-Misconduct, Q-Resignation, or O-Other, the system enables the Reason
 Explanation field.
For more information, see [Employment Termination Payments: Australia](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia).

## Reason Explanation

If you select P-Unsatisfactory Work
 Performance, M-Misconduct, Q-Resignation,
 or O-Other from the Separation Reason drop-down, the system
 enables this field. Enter any additional information that explains the reason for the
 employee's termination.

## Employment Termination Payments Posted

When posting automatic ETPs for this employee, the system will automatically check this box. Once the box is checked, you will be unable to generate any additional ETPs. You can uncheck this box to process additional automatic ETPs, if necessary.
You can also check this box independent of the automatic ETP process if you do not want to process ETPs for the employee.
Additional Information
[Employment Termination Payments: Australia](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia)
[Generating Employee ETPs](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/generate-payments-for-terminated-employees)

## Active for Arrears

Check this box to activate this employee for arrears. In addition to this, you will need to associate this employee with deduction codes that are subject to arrears before the system will calculate for arrears. For more information, see [Activating Arrears Calculations for Employees](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/activate-arrears-calculations-for-employees).

##  Pension Plan

The Pension Plan checkbox on the PR Employees form, Add'l Info tab.
 Select this checkbox if this employee is covered by a qualified pension plan (prints on W-2s).


 Leave this checkbox unselected if this employee is not covered by a qualified pension plan.

## Posting to All

Check this box if this employee’s earnings are to cover the entire period. This is necessary to calculate rate per day earnings, deductions, and liabilities when earnings are not posted daily. If checked, when posting time for this employee in either PR Timecard Entry or when processing PR Automatic Earnings, the Post To Date must match the payroll ending date for the correct Payroll Period. Posting to all will calculate based on the craft/class add-on setup only.
Do not check this box if this employee’s earnings will not cover the entire period.

## Include on Certified Reports

The Include on Certified Reports checkbox on the PR Employees form, Add'l Info tab.
Select this checkbox if this employee's earnings should be included on standard
 Certified Payroll reports. This will also be used as the default when
 entering timecards for the employee. Default may be overridden in PR
 Timecard Entry.

If you do not select this checkbox, the employee's earnings will not be included in the earnings break down in Certified Reports. However, all earnings will be included in weekly totals so that the report accurately reflects what an employee was paid.
Note: If you initialized this employee from HR, this box defaults as selected.

## Nonresident Alien

Check this box if the employee is a
 nonresident alien (NRA). When checked, the system adds an additional amount to the subject
 wages (as defined in IRS Publication 15), depending on the employee’s pay period (e.g.
 weekly, bi-weekly, semi-monthly, or monthly); tax is computed for a filing status of
 “Single/1 exemption,” as required by federal law. It is recommended that your NRA employees
 indicate their filing status as “Single/1” on their W-4s.

## Federal Tax Exempt (US)

(United States) The Federal Tax Exempt checkbox on the PR Employees form, Add'l Info tab.
Select this checkbox if this employee is exempt from Federal tax withholding. During payroll processing, the system calculates a zero amount for Federal withholding for the employee.
Note: If you have set up a calculation override for the Federal Withholding deduction in PR Employee Dedns/Liabs, selecting this checkbox overrides the rate/amount you specified for the employee/deduction code.

Leave unselected (default) if this employee is subject to Federal tax withholding.
Note: If the W4 Info checkbox is selected in HR Company Parameters (PR Update Options section), changes to this checkbox are automatically updated to the Federal Tax Exempt checkbox in HR Resources (Payroll Info tab). If the W4 Info checkbox is not selected, you must manually update this flag in both forms.

## W-2 Email Consent

(United States only) The W-2 Email Consent checkbox on the PR Employees form, Add'l Info tab.
Select this checkbox if this employee has consented to receive W-2s electronically (via email). This requires that you enter an email address for the employee in the Email field (Info tab).
Leave this checkbox unselected if the employee has not consented to receive W-2s electronically. Instead, the employee will receive printed W-2s.
When generating W-2 data in PR W-2 Process, the setting defined here defaults for the employee record (in PR W-2 Employee Edit) and may be overridden as needed for the specified Tax Year.

## 1095 Email Consent

(United States only) The 1095 Email Consent checkbox on the PR Employees form, Add'l Info tab.
Select this checkbox if this employee has consented to receive 1095s electronically (via email). This requires that you enter an email address for the employee in the Email field (Info tab).
Leave this checkbox unselected if the employee has not consented to receive 1095s electronically. Instead, the employee will receive printed 1095s.
When generating 1095 data in PR ACA Process, the setting defined here defaults for the employee record (in PR ACA 1095-C Employee) and may be overridden as needed for the specified Tax Year.

## FLSA Exempt

The FLSA Exempt checkbox on the PR Employees form, Add'l Info tab.
Select this checkbox if this employee is exempt under the Fair Labor Standards Act (FLSA).
Leave this checkbox unselected if this employee is not exempt under the Fair Labor Standards Act (FLSA).
Note: This field defaults as unselected when adding new employees.

The system will use this field when validating timecard batches for certain compliance discrepancies (for example, those defined in HQ State Compliance). For more information, see [PR Timecard Validation Rules Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-validation-rules-form).

## Check Print Order

This is an optional sort field that may be used when printing checks. For example, you might use this field to enter a supervisor’s name or initials to allow sorting checks by supervisor.
Note: This field is case-sensitive (i.e. 'JOHNSON' will sort before 'James').

## Method of Pay Stub Delivery

The Method of Pay Stub Delivery drop-down on the PR Employees form, Add'l Info tab.
Select the method of delivery to use for sending payment information (check stubs or direct deposit information) to the employee (using PR Pay Stub Notify). Options are:

- N-None – The employee will not receive an email when you print checks or download electronic funds transfers (EFTs).

- A-Email with attachment – The Employee will receive an email with the payment information report attached. The type of payment report depends on the Report Title for Check Attachment and Report Title for EFT Attachment fields in PR Company Parameters. For more information, see [Set up Payment Report Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information).
If you select this option, you must enter an email address in the Email Address field on the Info tab of this form. Additionally, you must be attaching payment information to employee pay sequences. For more information, see [Set Pay Stub Attachment Options](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/set-pay-stub-attachment-options).

- E-Email as notification – The employee will receive an email notification of payment, but it will not include an attachment. If you select this option, you must enter an email address in the Email Address field on the Info tab of this form.

Related information

- [Set up an Employee to Receive Pay Stubs via Email](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-an-employee-to-receive-pay-stubs-via-email)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## PAYG INB Summary

PAYG
 INB Summary checkbox on the PR Employees form, Add'l Info tab.
This
 field is enabled only if you selected the PAYG INB Summary checkbox in PR Company
 Parameters.
Select
 this checkbox if this employee has opted to received their PAYG payment summaries via
 email. Employee must have a valid email defined on the Info tab in PR Employees to enable
 this functionality.
Note: This checkbox defaults as selected if:

-  when enabling PAYG summary attachments in PR
 Company Parameters, you elected to automatically update employees with valid email
 addresses to receive PAYG payment summaries via email (answered Yes to the prompt
 displayed when saving the record).

- you entered a valid email address for a new or
 existing employee after enabling PAYG summary attachments in PR Company
 Parameters.

Do not select this checkbox if this employee opted out of receiving their PAYG payment summaries via email.

Related information

- [Set up an Employee to Receive PAYG Summaries via Email (Australia)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-an-employee-to-receive-payg-summaries-via-email-australia)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

## Payroll Program Account

This field displays for Canadian companies only.
Enter the Canadian Business Number Payroll Program Account reference number for this employee. The number must begin with RP and be followed by four digits.
This field overrides the value in the
 Payroll Program
 Account field in PR Company Parameters for this employee. The value in this
 field would be used if a reduced Employment Insurance (EI) program has been implemented for
 this employee, or the employee has been enrolled in more than one qualified reduced EI
 program.

## Quebec File Number

Enter your company's six-character Quebec File Number. Vista uses this number when you report employee deductions and contributions under separate payroll program accounts for an employee who meets both these requirements in a calendar year:

- performed work in Quebec

- participated in two or more Employee Insurance (EI) programs
Tip: Correct entries begin with RS and are followed by four digits.

## Dental Benefits Code

(Canada only) The Dental Benefits Code drop-down on the PR Employees form, Addl Info tab.
Select the dental benefit offered by the employer to this employee.

- 1-Not Eligible

- 2-Payee only

- 3-Payee, spouse, children

- 6-Payee, spouse

- 5-Payee, children

When generating employee records in PR Canada T4, the system uses the value entered here to populate the Dental Benefits Code field in PR Canada T4 Employees (the T4 Employees tab on the PR Canada T4 form). If you leave this field blank, the system will use the dental benefits code defined for the employer in PR Canada T4 (Info tab) instead.
The system uses the Dental Benefits Code assigned to the employee T4 record (in PR Canada T4 Employee) to populate Box 45 on the employee's T4 Slip.

## CPP-QPP Exempt

(CA only) The CPP-QPP Exempt checkbox on the PR Employees form, Add'l Info tab.
Select this checkbox if the employee is exempt from the Canada Pension Plan (CPP and CPP2) or the Quebec Pension Plan (QPP and QPP2). During payroll processing, the system refrains from calculating deductions and liabilities for CPP, CPP2, QPP, and QPP2.
 This checkbox also affects the T4 report, where it is used to determine whether the employee should be listed as exempt from CPP or QPP.

## EI Exempt

(CA only) The EI Exempt checkbox on the PR Employees form, Add'l Info tab.
Select this checkbox if the employee is exempt from Employment Insurance.

## PPIP Exempt

(CA only) The PPIP Exempt checkbox on the PR Employees form, Add'l Info tab.
Select this checkbox if the employee is exempt from the Provincial Parental Insurance Plan.

## Employment Basis

 (Australia) The Employment Basis drop-down on the PR Employees form, Add'l Info tab.
For use with STP Phase 2 only.
Enter the employment basis for this employee.

- F - Full Time (default)

- P - Part Time

- C - Casual

## Additional Withholding for Medicare Levy Surcharge

(Australia) The Additional Withholding for Medicare Levy Surcharge checkbox on the PR Employees form, Add'l Info tab.
For use with STP Phase 2 only.
Select this checkbox if the employee requested additional withholding for the Medicare Levy Surcharge. When selected, the Withholding Tier Level drop-down is enabled to indicate the withholding rate for the employee.
Note: This setting is used during STP Phase 2 data generation as part of the computation to determine the employee's Tax Treatment Code, and has no bearing on the actual calculation of PAYG withholding amounts during payroll processing. Additional withholding, if needed, should be configured for the employee as a rate-based add-on for the PAYG Tax deduction code in PR Employee Dedns/Liabs.

Leave this checkbox unselected if:

- the employee is fully or partially exempt from the Medicare Levy Surcharge; that is, the employee is assigned a Scale of 5, 95, 6, or 96 on the Filing Status tab in PR Employees.

-  the employee did not request additional withholding for the Medicare Levy Surcharge.

- the employee claimed a Medicare Levy Reduction (the Claim for Medicare Levy Reduction checkbox is selected).

## Withholding Tier Level

 (Australia) The Withholding Tier Level drop-down on the PR Employees form, Addl Info tab.
For use with STP Phase 2 only.
This drop-down is enabled and required if you selected the Additional Withholding for Medicare Levy Surcharge checkbox.
Note: This setting is used during STP Phase 2 data generation as part of the computation to determine the employee's Tax Treatment Code, and has no bearing on the actual calculation of PAYG withholding amounts during payroll processing. Additional withholding, if needed, should be configured for the employee as a rate-based add-on for the PAYG Tax deduction code in PR Employee Dedns/Liabs.

Select the tier level representing the withholding rate requested by this employee for the Medicare Levy Surcharge.

- Tier 1 (1.00 %)

- Tier 2 (1.25 %)

- Tier 3 (1.50 %)

## Claim for Medicare Levy Reduction

(Australia) The Claim for Medicare Levy Reduction checkbox on the PR Employees form, Add'l Info tab.
For use with STP Phase 2 only.
Select this checkbox if this employee claimed a Medicare Levy Reduction.
Leave this checkbox unselected if:

- the employee is fully exempt from the Medicare Levy; that is, the employee is assigned a Scale of 5 or 95 on the Filing Status tab in PR Employees.

- the employee requested additional withholding for the Medicare Levy Surcharge (the Additional Withholding for Medicare Levy Surcharge checkbox is selected).

- the employee did not claim a Medicare Levy Reduction.

## Direct Deposit

Direct Deposit section on the PR Employees
 form, Direct Deposit tab.
Select whether the employee uses direct deposit for payment from one of the following:

- Not Used - Select this option if this employee will be paid by check.

- Pre-Note - Select this option if this is a test run for direct deposit for this employee. The employee will still be paid by check.

- Active - Select this option if this employee will be paid by direct deposit.

Related information

- [Set up an Employee for Direct Deposit](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-an-employee-for-direct-deposit)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Routing Transit # / BSB #

US & Canada: Routing Transit # field on the PR
 Employees form, Direct Deposit tab.
Australia: BSB # field on the PR Employees form,
 Direct Deposit tab.
For US & Canada:
 Enter the routing transit number of the of the bank accepting the direct deposit for this employee.
For Australia:
Enter the enter the bank state branch number of the bank accepting the direct deposit for this employee.

Related information

- [Set up an Employee for Direct Deposit](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-an-employee-for-direct-deposit)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Bank Account #

Bank Account # field on the PR Employees form,
 Direct Deposit tab.
This field is enabled only for direct deposit status of Prenote or Active.
 Enter the bank account number provided by the bank accepting the direct deposit for this employee. Up to 17 characters allowed (alpha, numeric (0-9), and hyphens only).
 This number identifies the specific account
 receiving the funds. All net pay will be deposited into this account unless additional
 distributions are set up on the Add'l Direct Deposits tab in PR Employees.

Related information

- [Set up an Employee for Direct Deposit](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-an-employee-for-direct-deposit)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Account Type

Account Type section on the PR Employees form,
 Direct Deposit tab.
This field is enabled only for direct deposit status of Prenote or Active.
Indicate to what type of bank account this employee’s direct deposit will be made.

- Checking – Check this option if this employee’s bank
 account is a checking account.
Note: This account type will appear as code '22' in the EFT file.

- Savings - Check this option if this vendor’s bank
 account is a savings account.
Note: This account type will appear as code '32' in the EFT file.

Note: The system defaults the Checking radio
 button when you select the Active option from the EFT Info
 field.

Related information

- [Set up an Employee for Direct Deposit](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-an-employee-for-direct-deposit)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Direct Deposit Applies to Only One Pay Sequence

Direct Deposit Applies to Only One Pay Sequence checkbox on the PR Employees form, Direct Deposit tab.
This field is enabled only for direct deposit status of Prenote or Active.
Select this checkbox if this employee's
 direct deposit applies to only one pay sequence (specified in the Pay Seq field).
 Direct deposit payment will default for the specified pay sequence for all pay periods;
 however, you may override the default in PR Employee Pay Seq Control.
Do not select this checkbox if this employee's direct deposit applies to all pay sequences.

Related information

- [Set up an Employee for Direct Deposit](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-an-employee-for-direct-deposit)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [About the PR Employee Pay Sequence Control Form](/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-employee-pay-sequence-control-form)

## Pay Seq

Pay Seq field on the PR Employees form, Direct
 Deposit tab.
This field is enabled only when you select the
 Direct Deposit
 Applies to Only One Pay Sequence checkbox.
Specify which pay sequence for this employee
 will be paid by direct deposit. This applies to all pay periods for this employee except
 when the OverrideDirDeposit checkbox is selected in PR Pay Period Control for the
 pay sequence in a specific pay period.

Related information

- [Set up an Employee for Direct Deposit](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-an-employee-for-direct-deposit)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Seq

Seq field on the PR Employees form, Add'l
 Direct Deposits tab.
 This number controls the order of processing
 (ascending). Amounts will be distributed according to sequence up to the amounts specified,
 with any remaining net pay distributed to the account set up in PR Employees. Distributions
 only need to be set up here if an employee wants his net pay deposited to more than one
 account.
Enter the sequence number to identify the
 order in which this distribution should be processed. For example, if this distribution
 should be processed first, enter 1.

Related information

- [Set up Additional Direct Deposits for an Employee](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-additional-direct-deposits-for-an-employee)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Routing Transit # / BSB #

 US & Canada: Routing Transit # field on the PR
 Employees form, Add'l Direct Deposits tab.
Australia: BSB # field on the PR Employees form,
 Add'l Direct Deposits tab.
For US & Canada:
 Enter the routing transit number of the of the bank accepting the direct deposit for this employee.
For Australia:
Enter the enter the bank state branch number of the bank accepting the direct deposit for this employee.

Related information

- [Set up Additional Direct Deposits for an Employee](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-additional-direct-deposits-for-an-employee)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Bank Account #

Bank Account # field on the PR Employees form,
 Add'l Direct Deposits tab.
 Enter the bank account number to which the pay is to be deposited.

Related information

- [Set up Additional Direct Deposits for an Employee](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-additional-direct-deposits-for-an-employee)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Type

Acct Type drop-down on the PR Employees form,
 Add'l Direct Deposits tab.
Indicate to what type of bank account this employee’s direct deposit will be made.

- C-Checking

- S-Savings

Related information

- [Set up Additional Direct Deposits for an Employee](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-additional-direct-deposits-for-an-employee)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Status

Enter the status of this deposit distribution, selecting from one of the following:

- A-Active

- I-Inactive

- P-Prenote - If this status is selected, it must be changed to “Active” once testing has been completed so that depositing can occur.

## Frequency

Frequency field on the PR Employees form,
 Add'l Direct Deposits tab.
Enter a valid frequency code to control how often this distribution is to be made. Press F4 to select from a list of valid frequency codes.

Related information

- [Set up Additional Direct Deposits for an Employee](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-additional-direct-deposits-for-an-employee)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Method

Method drop-down on the PR Employees form,
 Add'l Direct Deposits tab.
Specify the method used to calculate the amount of the deposit.

- A-Amount

- P-Percentage

Related information

- [Set up Additional Direct Deposits for an Employee](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-additional-direct-deposits-for-an-employee)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Percent

Percent field on the PR Employees form, Add'l
 Direct Deposits tab.
This field is enabled when the Method field is
 set to P-Percentage.
Enter the percent of net pay to be deposited. Enter as a percentage and not a rate.

Related information

- [Set up Additional Direct Deposits for an Employee](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-additional-direct-deposits-for-an-employee)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Amount

Amount field on the PR Employees form, Add'l
 Direct Deposits tab.
This field is enabled when the Method field is
 set to A-Amount.
Enter the amount of net pay to be deposited.

Related information

- [Set up Additional Direct Deposits for an Employee](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-additional-direct-deposits-for-an-employee)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Deduction Code

Enter a deduction code for withholding federal or state tax. Press F4 for a list of deduction codes.

## Filing Status (US)

The Filing Status field on the PR Employees form, Filing Status tab.
Enter the filing status for this employee.
For Federal W-4s submitted after January 1, 2020, this is the value from Step 1c of Form W-4 (2020). Only the following options are valid:

- S = Single or Married filing separately

- M = Married filing jointly or Qualifying surviving spouse

- H = Head of Household

For Federal W-4s submitted prior to January 1, 2020 and state W-4s:

- S = Single

- M = Married Filing Separately

- H = Head of Household

- F = Married Filing Jointly, one spouse working

- B = Married Filing Jointly, both spouses working (state only)

- W = Qualified Widow(er)

- O = No exemptions (Alabama only)

Note: It is not always necessary to define a state deduction if the filing status is the same as the employee’s federal filing status. If a state deduction has not been defined for an employee, the system automatically uses the federal filing status. If a state deduction has been defined and the filing status and exemption are left blank, a filing status of “single” with exemptions zero are assumed.
Many state routines only allow “M” or “S” as a valid filing status. Other exceptions include Connecticut, Georgia, and Puerto Rico (see the [Tax and Worker's Comp Routines ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines)Tax and Worker's Comp Routines tables for details on individual requirements).
It is very important to check for any special requirements defined for the state to determine whether a separate state deduction filing status needs to be set up.
For the Australian field definition, see [Filing Status (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-00038406--en).
Note: For the U.S. only, the value specified in this field will
 print on selected payroll check print/EFT remittance reports (for example, PR Check
 Print, PR Check Print Stub, and PR EFT Remittance).

Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Filing Status (AU)

Select M from the drop-down if the employee
 submitted Form NAT 0929 and answered Yes to question 9 (Do you have a
 spouse). Otherwise, leave this field blank.

## Regular Exempt's

US and Canada: The Regular Exempt's field on the PR Employees form, Filing Status tab. Australia: The Scale field on the PR Employees form, Filing Status tab.
Enter the number of regular exemptions claimed on the W-4.
Australian users: See the field definition for [Scale](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-0003844c--en).
Federal 2020 W-4sIf you are entering information from a Federal 2020 W-4, leave this field blank. Instead, use the Dependent Amount field to enter the annual dollar amount to claim as a dependent deduction. For more information, see [Dependent Amount](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#concept-43370002--en).
Pre-2020 Federal W-4sFor Federal W-4 information entered prior to January 1, 2020, this field is still applicable and indicates the number of regular exemptions claimed on the W-4. However, if the employee submits a Federal 2020 W-4, it is suggested that you clear the value in this field.Note: For the U.S. only, the value specified in this field will print on
 selected payroll check print/EFT remittance reports (for example, PR
 Check Print, PR Check Print Stub, and PR EFT Remittance).

Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Add'l Exempt's

US and Canada: The Add'l Exempt's field on the PR Employees form, Filing Status tab. Australia: The Children field on the PR Employees form, Filing Status tab.
Most states do not require a separate allowance certificate, however follow your state guidelines for entering an employee's additional allowances/exemptions.
Australian users: See the field definition for [Children](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-00038497--en).
Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank. Instead, use the Dependent Amount field to enter the annual dollar amount to claim as a dependent deduction. For more information, see [Dependent Amount](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#concept-43370002--en).
Pre-2020 Federal W-4s
For Federal W-4 information entered prior to January 1, 2020, this field is still applicable. However, if the employee submits a Federal 2020 W-4, it is suggested that you clear the value in this field.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Apply Tax Credits

The Apply Tax Credits checkbox on the PR Employees form, Filing Status tab
Select this checkbox to apply additional tax
 credits to this employee. Once selected, the Authorized Tax Credits field is enabled
 for recording additional authorized tax credits for the employee.
Do not select this checkbox if you are not applying additional tax credits for this employee.

## Authorized Tax Credits

This field is enabled only if the Apply Tax
 Credits checkbox is selected.
Enter the Annual Amount from line 15 of the employee's TP-1016-V form (Application for a Reduction in Source Deductions of Income Tax for an Individual or a Self-Employed Person).

## Override Misc Amount #1

US: The Override Misc Amount #1 checkbox on the PR Employees
 form, Filing Status tab. Australia: The Apply Tax Offset checkbox on the PR
 Employees form, Filing Status tab. Canada: The Apply Tax Credits checkbox on the PR
 Employees form, Filing Status tab.
United States users: This field is currently used
 for Colorado, Mississippi, and Michigan State Tax only. Select this check
 box to override the routine’s Misc Amount #1 field
 in PR Routines (usually the exemption amount).
Note:For Colorado
 users: You should only select this checkbox (for
 the Colorado deduction) if the employee has filed a Colorado DR
 0004.

Australian users: See the field definition for [Apply Tax Offset](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-0003849c--en).
Canadian users: See the field definition for [Apply Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-0005c200--en).
Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

##  Misc Amount #1

US: The Misc Amount #1 field on the PR Employees form, Filing Status tab. Australia: The Tax Offset field on the PR Employees form, Filing Status tab. Canada: The Authorized Tax Credits field on the PR Employees form, Filing Status tab.
United States users: If you selected the Override Misc Amount #1 checkbox, use this field to enter the amount to use when calculating for this Employee.
Note: For Colorado users: Enter the amount from Line 2 of the
 employee's Form DR 0004.

Australian users: See the field definition for [Tax Offset](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-000384a7--en).
Canadian users: See the field definition for [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-0005c20b--en).
Federal 2020 W-4s
If you are entering information from a Federal 2020 W-4, leave this field blank.
Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Misc Factor

The Misc Factor field on the PR Employees form, Filing Status tab.
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

The Multiple Jobs Checked checkbox on the on the PR Employees form, Filing Status tab.
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Select this checkbox if the employee filled out Step 2 of Federal Form W-4 (2020); that is, the employee has more than one job or is married filing jointly and their spouse also works.
Leave this checkbox unselected if the employee did not fill out Step 2 of Federal Form W-4 (2020).
Note: The value specified in this field will print on selected payroll check
 print/EFT remittance reports (for example, PR Check Print, PR Check Print Stub, and
 PR EFT Remittance).

Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Dependent Amount

The Dependent Amount field on the PR Employees form, Filing Status tab.
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Enter the total annual dollar amount to be claimed as a dependent deduction. This is the total amount entered by the employee in Step 3 of Federal Form W-4 (2020); that is, the amount entered on Line 3.
Note: The value specified in this field will print on selected payroll check
 print/EFT remittance reports (for example, PR Check Print, PR Check Print Stub, and
 PR EFT Remittance).

Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Other Income

The Other Income field on the on the PR Employees form, Filing Status tab.
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Enter the total other income as entered by the employee in Step 4a of Federal Form W-4 (2020). This amount represents the total annual income the employee expects during the year that will not have withholding (such as interest, dividends, retirement income, etc).
Note: The value specified in this field will print on selected payroll check
 print/EFT remittance reports (for example, PR Check Print, PR Check Print Stub, and
 PR EFT Remittance).

Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Other Deductions

The Other Deductions field on the on the PR Employees form, Filing Status tab.
This field is for U.S. users only, and applies to 2020 W-4s (effective January 1, 2020).
Enter the total other deductions entered by the employee in Step 4b of Federal Form W-4 (2020). This amount represents the total annual deductions other than the standard deduction.
Note: The value specified in this field will print on selected payroll check
 print/EFT remittance reports (for example, PR Check Print, PR Check Print Stub, and
 PR EFT Remittance).

Note: If you selected the W-4 Info checkbox in the PR Update Options section of the HR Company Parameters form, the system automatically synchronizes the employee and resource records when additions or changes are made to this field in either HR or PR. However, in order for auto-updates to occur:

- you must assign a valid resource number to the employee in the PR Employees form;

- you must assign a valid employee number to the resource in the HR Resources form; and

- you must select the Active PR Employee and Exists in PR checkboxes for the resource in the HR Resources form.

 If you do not select the W-4 Info checkbox, you must update this field manually in each of the HR Resources, PR Employees, and PR Employee Dedns/Liabs forms as applicable.

## Scale

(Australia) The Scale field on the PR Employees form, Filing Status tab.

###
Scale Numbers for PAYG Withholding

Enter the scale number for PAYG withholding. You may enter the following numbers:

- 1 = No tax-free threshold; enter this if question 8 on the employee's NAT 3093 is No.

- 2 = Tax-free threshold with leave loading.

- 3 = Foreign resident; enter this if the employee is a non-resident.

- 4 = No tax file number (TFN) was provided by the employee

- 5 = Full Medicare exemption; enter this if the employee filed a NAT 0929 and claimed a full exemption.

- 6 = Half Medicare exemption; enter this if the employee filed a NAT 0929 and claimed a half exemption.

### Scale Numbers to Calculate STSL Component

If you need to calculate a Study and Training Support Loan component for an employee, use the following scale numbers:

- 91 = No tax-free threshold; enter this if question 8 on the employee's NAT 3093 is No.

- 92 = Tax-free threshold with leave loading.

- 93 = Foreign resident; enter this if the employee is a non-resident.

- 95 = Full Medicare exemption; enter this if the employee filed a NAT 0929 and claimed a full exemption.

- 96 = Half Medicare exemption; enter this if the employee filed a NAT 0929 and claimed a half exemption.

Note: The STSL Component schedule applies to employees who have any of the following debts:

- Higher Education Loan Program (HELP)

- VET Student Loan (VSL)

- Financial Supplement (FS)

- Student Start-up Loan (SSL) / ABSTUDY SSL

- Trade Support Loan (TSL)

## Children

Enter the number of children for the employee. Enter a number here when the answer to question 12 on the employee's NAT 0929 is Yes. Otherwise, leave blank.

## Apply Tax Offset

The Apply Tax Offset checkbox on the PR
 Employees form, Filing Status tab.
Select this checkbox if the answer to
 question 9 on the employee's NAT 3093 is Yes. When you select this checkbox, the system
 enables the Tax
 Offset field, where you can enter the estimated tax offset amount from the
 NAT 3093.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Tax Offset

The system enables this box when you check the
 Apply tax
 offset box.
If the answer to question 9 on the employee's Nat 3093 is Yes, enter the estimated total tax offset amount in this field.

## Total Claim Amount

The field displays for Canadian users only.
If overriding the standard claim amount, enter
 the amount here. Otherwise, leave this field blank. The value you enter here updates the
 Total Claim
 Amount field in PR Employee Dedns/Liabs.
Note: You will only need to enter a value here if the
 Employee is not claiming the Basic Personal Exemption on the TD1-Federal/TD1-Provincial.
 The routines for Federal and Provincial taxes (defined in PR Routines) will automatically
 realize the current annual personal exemption.

## Period Start Date

Period Start Date field on the PR Employees
 form, PAYG Reporting Periods tab.
The system will automatically create and update reporting periods based on changes to the Most Recent Rehire Date and Termination Date for an employee. You should not need to manually add records, but it is allowed.
For reporting periods added by the system, this date is set as follows (and cannot be changed):

- If this reporting period was created because you
 added a new employee and entered a hire date for the first time, the Most Recent Rehire
 Date field will automatically default from the Hire Date (one time
 only) and this field is set equal to the Most Recent Rehire Date field.

- If this reporting period was created because you
 rehired the employee and entered a new rehire date, this field is set equal to the
 date specified in the Most Recent Hire Date field.

- If this reporting period was automatically created because you generated year-end summaries for all employees and the Period End Date for the previous reporting period record was set to 6/30/YY (by the system), this field is set to 7/1/YY.

- If this reporting period was created because you generated an on-demand summary for an employee that was not terminated (no Termination Date exists), this field is set equal to one day after the Period End Date entered (manually or by the system) for the previous reporting period record.

If you are manually adding a reporting period
 record, enter the period start date. If there are existing reporting periods and summaries
 for this employee, this date must fall after the previous reporting period's Period End
 Date, and cannot conflict with the Begin Date / End Date range of any existing reporting
 periods or INB summaries.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [About PAYG Reporting Periods (Australia)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-payg-reporting-periods-australia)

## Period End Date

Period End Date field on the PR Employees
 form, PAYG Reporting Periods tab.
The system will automatically create and update reporting periods based on changes to the Most Recent Rehire Date and Termination Date for an employee. You should not need to manually add records, but it is allowed.
For existing reporting periods, the system will automatically set this date as follows (and cannot be changed):

- If you entered a termination date for the employee
 and this is the most recent reporting period record, this field is set equal to the
 date specified in the Termination Date field (Add'l Info
 tab) .

- If you generated year-end summaries for all employees and this is the most recent reporting period record, this field is automatically set to 6/30/YY.

- If you generated a part-year summary for an employee
 that was not terminated (no Termination Date) and this is the most recent reporting
 period, if you did not manually enter a period end date, this field is set equal to
 the Process Through Date specified when generating amounts in PR PAYG Employee
 Generate Amts.

You will typically only need to manually enter a date here if you will be generating a part-year summary for the employee.
Enter the period end date for this reporting period. Date must be equal to or later than the Period Start Date for the current reporting period and equal to or earlier than 6/30/YY of the current fiscal year. For part-year summaries, this date should be the end date for the pay period that most closely matches the exact day of the employee's request.
Note: If the employee has been terminated, this date must be equal to or earlier than the Final Pay Period Date (if one is entered) for the current reporting period.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [About PAYG Reporting Periods (Australia)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-payg-reporting-periods-australia)

## Final Pay Period Date

Final Pay Period Date field on the PR
 Employees form, PAYG Reporting Periods tab.
The system will automatically create and update reporting periods based on changes to the Most Recent Rehire Date and Termination Date for an employee. You should not need to manually add records, but it is allowed.
You will only need to enter a date in this field if the employee has been terminated and received (or will receive) their final payment after the termination pay period.
Enter the final pay period date for this reporting period. Date entered here must be equal to or later than the Period End Date of the current reporting period.
Note: If the date entered here falls after 6/30/YY, the system will create a new reporting period with a Period Start Date and a Period End Date of 7/1/YY. It will then set the Final Pay Period Date for the new reporting period equal to the Final Pay Period Date entered here, and clear the Final Pay Period Date from the previous reporting period record.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [About PAYG Reporting Periods (Australia)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-payg-reporting-periods-australia)

## Income Type

Income Type drop-down on the PR Employees form, PAYG Reporting Periods tab.
Income Type drop-down on the PR Employees form, PAYG Reporting Periods tab.
When a new reporting period is created (by hiring or rehiring an employee), this field automatically defaults the PAYG Income Type specified for the employee on the Info tab (in PR Employees). You should not need to change the default.
Income types are as follows:

- S - Salary or wages (default) - Select this option if this employee is a full or part-time employee receiving a regular salary or hourly wages.

- H - Working holiday maker - Select this option if this employee is a working holiday maker.

Note: If an employee's PAYG Income Type changes after a reporting period is created, do not change the Income Type for the reporting period. Instead, follow the steps for [changing an employee's PAYG income type](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-payg-withholding-for-employees/change-an-employees-payg-income-type-australia) to enable the system to create a new reporting period for the employee that reflects the new income type. This ensures each reporting period and its associated summary reflects the correct income type.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Tax Year

Tax Year field on the PR Employees form, PAYG
 Reporting Periods tab.
Display-only field showing the tax year to
 which this reporting period applies. The system automatically populates this field once you
 generate a summary for this reporting period (via PR Employee Generate Amts) using the Tax
 Year you specified in PR PAYG Summary Process prior to generating amounts.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [About PAYG Reporting Periods (Australia)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-payg-reporting-periods-australia)

## Notes

Notes field on PR Employees form, PAYG
 Reporting Periods tab.
Enter any miscellaneous notes about this reporting period. The space allowance is virtually unlimited.
Note: If you are accessing this field from a grid and you need additional space for your notes, double-click in the field to access the Grid Notes form.
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

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

## Summary #

Summary # field on the PR Employees form, PAYG
 Reporting Periods tab.
Display-only field showing the summary number
 for this reporting period. The system automatically populates this field once you generate
 a summary for this reporting period (via PR Employee Generate Amts) using the Summary #
 assigned to the related summary record in PR Employee PAYG Summaries.

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [About PAYG Reporting Periods (Australia)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-payg-reporting-periods-australia)

## Aatrix ID

The Aatrix ID field on the PR Employees form, Aatrix ID Values tab.
Enter a valid Aatrix ID to identify the value being reported. Press F4 for a list of valid Aatrix IDs.
Note: Aatrix IDs are used to identify employee data that is unique to various state regulatory reports; therefore, you may need to set up multiple IDs to meet all of your company's reporting needs. When running regulatory reports via the PR Aatrix Report Selection form, the system passes the applicable IDs defined for each employee to Aatrix based on the state and report selected.

## Value

The Value field on the PR Employees form, Aatrix ID Values tab.
Enter the value that applies to the specified Aatrix ID. The description displayed for the specified Aatrix ID indicates what value to enter. For example, if you enter Aatrix ID "4005 (CA Wage Plan Code)", the applicable values are shown after the hyphen in the code description (S, U, J, L, R, A, or P).
When running regulatory reports via the PR Aatrix Report Selection form, the system passes this value to Aatrix for the applicable report.

## Memo

The Memo field on the PR Employees form, Aatrix ID Values tab.
Enter a memo about this employee / Aatrix ID entry, up to 500 characters.
The memo entered here is informational only. It is not passed to Aatrix during regulatory reporting.
