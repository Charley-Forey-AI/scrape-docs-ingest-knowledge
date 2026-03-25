---
title: "Field Definitions: PR User Grid Options Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-user-grid-options-form/field-definitions-pr-user-grid-options-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-user-grid-options-form/field-definitions-pr-user-grid-options-form"
---

# Field Definitions: PR User Grid Options Form

The following is a list of field descriptions for the PR User
 Grid Options form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Job Timecards

For each field listed below, specify the display option for Job timecard lines and, if applicable, set the field to be skipped (by checking the corresponding
 Grid Input Skip
 box) when information is entered into the grid (users can still manually select the field and enter values).
The following table groups the fields into three separate columns. The first column indicates fields that are required/cannot be skipped and are always available on a Job timecard line. The second column lists optional fields. The third column also lists optional fields, but these have associated description fields that can be displayed.
Required Fields
Optional Fields
Optional Fields w/Description Fields

Employee
Type
PR Dept

Equipment**
Pay Seq
Crew

Job
Ins State
Local Code

Phase
Tax State
Ins Code

Unemp State
Equipment**

GL Co#
Craft

EM Co#**
Class

Shift
Equip Phase**

Hourly Rate*
Cost Type

Amount*
Rev Code**

Certified

Memo

Note: Fields with an asterisk (*) will display in the grid
 when the
 Display Earnings
 Rates in Timecard Entry
 checkbox is selected in VA User Profile for the user who is entering
 timecards. Otherwise, the fields are disabled and do not display in the grid.
Fields with a double-asterisk (**) will display in
 the grid when you check the Enter Equipment Usage with Timecards box (PR
 Company Parameters, Equipment tab) and you select Options  > Post Equipment
 Usage in PR Timecard Entry.
For required fields, there are three options available for display:

- No Description - the description associated with this field is not
 displayed.

- Description in Grid - the description associated with this field displays in
 the grid.

- Description Above Grid - the description associated with this field displays
 above the grid. For both types of optional
 fields, the following options are available:

- No Grid Input - the field does not display in the grid; typically fields are
 removed to speed up data entry or if the default value is seldom overridden.

- No Grid Input / Field Value Above the Grid - the field does not display in
 the grid, although it does display above the grid (informational only).

- Field in Grid - the field displays in the grid and users can enter values.
 For optional fields that have associated
 description fields, the following options are also available:

- No Grid Input / Description Above Grid - the field does not display in the
 grid, although its description displays above the grid.

- Field and Description in Grid - the field and its description appear in the
 grid.

- Field in Grid / Description Above Grid - the field displays in the grid,
 while the description displays above the grid.

## Mechanics Timecards

For each field listed below, specify the
 display option for Mechanics timecard lines and, if applicable, set the field to be skipped
 (by checking the corresponding Grid Input Skip box) when information is
 entered into the grid (users can still manually select the field and enter values).
The following table groups the fields into three separate columns. The first column indicates fields that are required/cannot be skipped and are always available on a Mechanics timecard line. The second column lists optional fields. The third column also lists optional fields, but these have associated description fields that can be displayed.
Required Fields
Optional Fields
Optional Fields w/Description Fields

Employee
Type
PR Dept

Equipment
Pay Seq
Crew

Cost Code
JC Co#
Job

Ins State
Local Code

Tax State
Ins Code

Unemp State
Work Order

EM Co#
WO Item

Shift
Comp Type

Hourly Rate
Component

Amount
Craft

Certified
Class

Memo

Note: Fields with an asterisk (*) will display in the grid
 when the Display
 Earnings Rates in Timecard Entry checkbox is selected in VA User Profile
 for the user who is entering timecards. Otherwise, the fields are disabled and do not
 display in the grid.
For required fields, there are three options available for display:

- No Description - the description associated with this field is not displayed.

- Description in Grid - the description associated with this field displays in the grid.

- Description Above Grid - the description associated with this field displays above the grid.
For both types of optional fields, the following options are available:

- No Grid Input - the field does not display in the grid; typically fields are removed to speed up data entry or if the default value is seldom overridden.

- No Grid Input / Field Value Above the Grid - the field does not display in the grid, although it does display above the grid (informational only).

- Field in Grid - the field displays in the grid and users can enter values.
For optional fields that have associated description fields, the following options are also available:

- No Grid Input / Description Above Grid - the field does not display in the grid, although its description displays above the grid.

- Field and Description in Grid - the field and its description appear in the grid.

- Field in Grid / Description Above Grid - the field displays in the grid, while the description displays above the grid.

## Service Timecards

For each field listed below, specify the display option for SM Work Order timecard lines and, if applicable, set the field to be skipped (by checking the corresponding Grid Input Skip box) when information is entered into the grid (users can still manually select the field and enter values).
The following table groups the fields into three separate columns. The first column indicates fields that are required/cannot be skipped and are always available on an SM Work Order timecard line. The second column lists optional fields. The third column also lists optional fields, but these have associated description fields that can be displayed.
Required Fields
Optional Fields
Optional Fields w/Description Fields

Employee
Type
PR Dept

SM WO
Pay Seq
Local Code

SM Scope Seq
Ins State
Ins Code

SM Pay Type
Tax State
SM Cost Type

SM JC Cost Type**
Unemp State
Craft

SM Co
Class

GL Co#
Equipment

Shift
Equip SM Cost Type

Hourly Rate*

Amount*

Certified

Memo

Start/Stop

EM Co#

Equip Phase***

Equip JC Cost Type***

Rev Code

Note: Fields with an asterisk (*) will display in the grid when the Display Earnings Rates in Timecard Entry checkbox is selected in VA User Profile for the user who is entering timecards. Otherwise, the fields are disabled and do not display in the grid.

**
The SM JC Cost Type field is a required field for timecards posted to job-related work orders; however, because the system will always default a JC cost type (from the SM Cost Type or from the earnings code assigned to the SM Pay Type), the system allows you to set this field to be skipped for input. You will only need access to this field if you need to change the default value.

***
The Equip Phase and Equip JC Cost Type fields are enabled in this form, but are not currently functional and will be disabled in the timecard entry grid. They were put in place for a future release.

For required fields, there are three options available for display:

- No Description - the description associated with this field is not displayed.

- Description in Grid - the description associated with this field displays in the grid.

- Description Above Grid - the description associated with this field displays above the grid.
For both types of optional fields, the following options are available:

- No Grid Input - the field does not display in the grid; typically fields are removed to speed up data entry or if the default value is seldom overridden.

- No Grid Input / Field Value Above the Grid - the field does not display in the grid, although it does display above the grid (informational only).

- Field in Grid - the field displays in the grid and users can enter values.
For optional fields that have associated description fields, the following options are also available:

- No Grid Input / Description Above Grid - the field does not display in the grid, although its description displays above the grid.

- Field and Description in Grid - the field and its description appear in the grid.

- Field in Grid / Description Above Grid - the field displays in the grid, while the description displays above the grid.

## Grid Input Skip

Check this box if this field is being displayed in the grid, but you want the cursor to skip this field during data entry.
Leave this box unchecked if you do not want the cursor to skip this field during data entry.
