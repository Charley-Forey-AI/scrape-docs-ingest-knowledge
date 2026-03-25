---
title: "Field Definitions: RP Report Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form"
---

# Field Definitions: RP Report Parameters Form

The following is a list of field descriptions for the RP
 Report Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Report ID

Select the report with the parameters you want
 to change. Press F4 to select a report from a list. Standard SSRS reports are available only
 if the Business Intelligence module is turned on.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Parameter Name

The parameter name links the report to the application, and it identifies the input fields that display when the report is launched.
Press F4 to select a parameter from a list.
Crystal Report parameters will start with a
 "?". For example, if you create a new Crystal report and then update the parameters using
 Update
 Parameters button on the Info tab of [RP Report Titles](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form), the updated parameters will all start
 with a "?".
Note: The parameter name must exactly match the name of the parameter in the application that you created the report in.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Display Sequence

Displays the sequence of the parameter. You can change this value, but you should not change the logical sequence of the parameters, especially if using F4 lookups that require the parameters to be in a specific order. For example, if a lookup requires ?Company and ?Project, the report parameters must be ?Company and then ?Project because you must select a company before a project.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Description

Use this field to enter a description of the parameter. The description can be up to 60 characters long.
The description is used as the label of the input field when the report is launched.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Datatype

This field:

- Automatically formats the input using input mask set
 up on the datatype - For example, if the parameter is phase code, select bPhase and
 the parameter will automatically be formatted using the mask on the bPhase
 datatype.

-  Allows users to press F4 in the associated input
 field.

You should use datatypes wherever
 possible.
Press F4 to select the datatype from a
 list.
If you do not select a datatype, the
 Input
 Type, Input Mask, and Input Length
 fields are enabled.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Input Type

This field is only enabled when the Datatype field
 is blank.
Select the input type of the parameter.
If you select 1-Numeric, you
 must also select a value in the Precision field.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Precision

This field is only enabled when the Datatype field
 is blank and Numeric is selected in the Input Type field.
Use this field to select the numerical precision of the parameter.

- 0=TinyInt - Input must be between 0
 and 255.

- 1=SmallInt - Input must be between
 -32,768 and 32,767.

- 2=Int - Input must be between
 -2,147,483,648 and 2,147,483,647.

- 3=Numeric - Use for decimals.
 Allows up to 38 digits, but characters before and after the decimal are determined by
 the input mask.

Note: The precision of a numeric should always be in sync with the mask and input length of the field. For example, if the input mask is #####, and the input length 5, the precision should be 1 or 2. A precision of 1 would allow entry of a number up to 32,767, whereas a precision of 2 would allow entry of a number up to 99999.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Input Mask

This field is only enabled when the Datatype field
 is blank.
Specify the input mask for this parameter,
 which formats the output of the field. Generally this applies to numeric fields, but you
 can also use them on text fields.
String
For string fields, you can enter an input mask to identify field justification.

- R - Right Justified

- L - Left Justified

- F - Fixed Length - When you select
 this option, use the Input Length field to enter the
 fixed length of the parameter.

- LUCASE - Left Justified Upper
 Case

- FUCASE - Fixed Upper Case

If an input mask is not specified, the field automatically defaults as left justified.
Numeric
For numeric fields, the input mask identifies how the numbers display (e.g. whether it is a whole number or decimal, whether to include separators or decimals, etc.). The mask should match the designated input length and precision. For example, if you want the input to be a whole number with an input length of 6, you would enter ######.
If you want the numeric to be a decimal input, and the input length is 16, you can enter in one of the following ways:
Mask
Input
Result

#,###,###,###.##
12345
 12,345.

#,###,###,##0.00
 12345
 12,345.00

For decimals requiring greater precision (such as units), you can specify up to 5 decimal places. For example, #,###,##0.00000.
Note: If your field requires a multi-part code, it is suggested you use one of the predefined datatypes (e.g. bContract, bPhase, or bJob).

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Input Length

This field is only enabled when the Datatype field
 is blank.
Enter the maximum number of characters allowed
 for entry - for example enter 30 if the field should allow up to 30
 characters.
If you are using a "Fixed" length input mask, the input must match the input length specified here exactly. For example, if the input mask is 'F' and the input length is '5', user must enter an input of five characters. Entering an input that is less than or greater than five characters will be invalid.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Default Type

This field is used in conjunction with the
 [Default Value](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003da66--en) field. Click [here](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003da66--en) for
 more information about using these fields.
Select the default type in this field and then
 use the Default
 Value field to enter the specific default value.
For example if this is a date parameter that
 should default to 1 day in the future, select 1-Current Date (+/-) if this field and then change the Default Value
 field to %D+1.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Default Value

Use this field in conjunction with the [Default
 Type](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003da56--en) field.
Select a default type and then use this field to define the default value.
Default Type
Default Value
Definition

BLANK

Enter a fixed default value.

Fixed Value

Specify a value. For example if you have a Y/N input, you might enter Y as the Default.

Current Date (+/-)
%D
Current Date.  To set a different value, add or subtract from the current date. For example, %D+1 is the current date plus one.

Current Month (+/-)
%M
Current Month.  To set a different value, add or
 subtract from the current month. For example, %M+1 is the current date plus
 one.

Report Parameter
%RPxxx (xxx is equal to the Report Parameter that you are defaulting from)
For example, you might use %RP?BegJob for the ?EndJob parameter so that both Beginning
 and Ending default to the same value.
When using this option, the parameter selected in
 the Default Value field must have a lower Load
 Sequence# than the current parameter.

Form Input Value
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
The last PR Group selected in PR Pay Period Control,
 PR Timecard Entry

Active PR End Date
%PR End Date
The last PR End Date selected in PR Pay Period
 Control, PR Timecard Entry

Active JB Prog Bill Mth
%JB Prog Mth
The last progress billing month selected in JB
 Progress Billing

Active JB Prog Bill #
%JB Prog Bill
The last progress billing number selected in JB
 Progress Billing

Active JB TM Bill Mth
%JB TM Mth
The last T&M billing month selected in JB
 T&M Bill Edit

Active JB TM Bill #
%JB TM Bill
The last T&M billing number selected in JB
 T&M Bill Edit

Report Attachment Channel

Use this default type to link record attachments to report.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Required

Select this checkbox if the parameter is required.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Multi Value

Multi Value checkbox in the RP Report Parameters form
Select this checkbox if the report launcher's entry field for this parameter should accept more than a single value.Note: Selecting this checkbox for any parameter only has an effect in the report's launcher when both the following apply to the same parameter record:

- the Report Lookup field (read-only) is not null, AND

- the Lookup is Active checkbox is selected.

Important: This is an advanced setting. In order for this functionality to work, the Crystal Reports file or the stored procedure must be modified for the report. If you have knowledge of Crystal Reports software or are able to modify a stored procedure, you may opt to proceed.

## Lookup is Active

Select this checkbox to activate this lookup. When selected, this lookup will be activated when F4 is pressed at the report input. If multiple lookups are assigned, those that are marked as ‘Active’ will appear as radio button options in the lookup window.
Note: All lookups, when added to the grid, automatically default to Active.
If unselected, this lookup will become ‘inactive’ (i.e. will not be activated when F4 is pressed at the report input). If multiple lookups are assigned, those that are marked as ‘inactive’ will not appear as radio button options in the lookup window.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Load Sequence #

This field is only applies to Crystal Reports.
This field controls the order of the datatype lookup and all additional lookups. The lookup with the lowest load sequence number is the default lookup.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Lookup Parameters

For Crystal applications only.
Specify the additional lookup parameters required for this F4 Lookup.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

- [Additional Lookups](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/additional-lookups)

## Add'l Lookups: Lookup

 Specify the lookup you want assigned to the report parameter indicated above (Parameter Name). Press F4 for a list of valid lookups (standard and custom). Once the lookup is specified, the grid is populated with the lookup’s status (Standard or Custom) and Lookup Query information.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

- [Additional Lookups](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/additional-lookups)

## Add'l Lookups: Lookup Parameters

For Crystal applications only.
Specify the additional lookup parameters required for this F4 Lookup.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

- [Additional Lookups](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/additional-lookups)

## Add'l Lookups: Load Sequence

For Crystal applications only.
This field controls the order of the datatype lookup and all additional lookups. The lookup with the lowest load sequence number is the default lookup.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)

## Add'l Lookups: Active

Check this box to activate this lookup. When checked, this lookup will be activated when F4 is pressed at the report input. If multiple lookups are assigned, those that are marked as ‘Active’ will appear as radio button options in the lookup window.
Note: All lookups, when added to the grid, automatically default to Active.
If unchecked, this lookup will become ‘inactive’ (i.e. will not be activated when F4 is pressed at the report input). If multiple lookups are assigned, those that are marked as ‘inactive’ will not appear as radio button options in the lookup window.

Related information

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters)
