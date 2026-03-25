---
title: "Field Definitions: RP Reports by Form Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form/field-definitions-rp-reports-by-form-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form/field-definitions-rp-reports-by-form-form"
---

# Field Definitions: RP Reports by Form Form

The following is a list of field descriptions for the RP
 Reports by Form form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Form

Enter the form that should be associated with
 the report. Press F4 to see a list of forms.

Related information

- [About the RP Reports by Form Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form)

## Report ID

Enter the report's ID number, or press
 F4
 to select from a list of reports.
Standard SSRS reports are available only if the Business Intelligence module is turned on.

Related information

- [About the RP Reports by Module Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-module-form)

## Active

 Select this checkbox to make the report available in the specified form’s Options menu.
 Do not select this box if you want the report to be unavailable to users.

Related information

- [About the RP Reports by Form Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form)

## Parameter Name

Specify the parameter that requires a default.
 Press F4 to view all available parameters for the form.

Related information

- [About the RP Reports by Form Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form)

## Override Default Type

Specify the default for this form’s parameter. For example, if you have a “Current Date” input, you could specify Current Date (+/-) as the Default so that if the input is blank, the report automatically pulls data associated with the current date. If a default is not specified, the default is the Crystal Report default. The following is a list of available defaults:
Fixed Value
Active PR Group

Current Date (+/-)
Active PR End Date

Current Month (+/-)
Active JB Prog Bill Month

Report Parameter
Active JB Prog Bill Number

Form Input Value
Active JB TM Bill Month

Active Company
Active JB TM Bill Number

Active Project
Report Attachment Channel

Active Contract

Note: You can also enter a specific numeric or character value as the default. For example, if you have a Y/N input, you might enter Y as the Default.

Related information

- [About the RP Reports by Form Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form)

## Override Default

Enter
 the default used for the parameter when report is run. Use this field in conjunction with
 the Default
 Type field. Enter a specific numeric or character value as the default when
 the Default Type is blank. The following table displays the values available for each
 Default Type.
Default Type
Default Value
Definition

Fixed Value

Specify a value. For example if you have a Y/N
 input, you might enter Y as the Default.

Current Date (+/-)
%D
Current Date.  To set a different value, add or
 subtract from the current date. For example, %D+1 is the current date plus
 one.

Current Month (+/-)
%M
Current Month.  To set a different value, add or
 subtract from the current month. For example, %M+1 is the current date plus
 one.

Report Parameter*
%RPxxx (xxx is equal to the other Report Parameter you are defaulting from)
For example, you might use %RP?BegJob for the
 ?EndJob parameter so that both Beginning and Ending default to the same
 value.

Form Input Value*
%FIxxx (xxx is equal to the field’s sequence number)
For example, if assigning to JC Jobs, %FI40 would be
 the Contract field’s value.

Active Company 
%C
Currently selected company

Active Project
%Project
The last company selected in PM Projects

Active Job 
%Job
The last job selected in JC Jobs

Active Contract
%Contract
The last contract selected in JC Contracts, PM
 Contracts

Active PR Group
%PR Group
The last PR Group selected in PR Pay Period Control, PR Timecard Entry

Active PR End Date
%PR End Date
The last PR End Date selected in PR Pay Period Control, PR Timecard Entry

Active JB Prog Bill Mth
%JB Prog Mth
The last progress billing month selected in JB Progress Billing

Active JB Prog Bill #
%JB Prog Bill
The last progress billing number selected in JB Progress Billing

Active JB TM Bill Mth
%JB TM Mth
The last T&M billing month selected in JB T&M Bill Edit

Active JB TM Bill #
%JB TM Bill
The last T&M billing number selected in JB T&M Bill Edit

Report Attachment Channel

Used to link record attachments on to report

Note: F4 is available when setting the default value for either report parameters or form input values.

Related information

- [About the RP Reports by Form Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form)

## Title Builder

This field is not currently in use.
