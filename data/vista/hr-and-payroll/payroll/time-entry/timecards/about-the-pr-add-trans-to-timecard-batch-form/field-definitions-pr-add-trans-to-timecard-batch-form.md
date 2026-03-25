---
title: "Field Definitions: PR Add Trans to Timecard Batch Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-add-trans-to-timecard-batch-form/field-definitions-pr-add-trans-to-timecard-batch-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-add-trans-to-timecard-batch-form/field-definitions-pr-add-trans-to-timecard-batch-form"
---

# Field Definitions: PR Add Trans to Timecard Batch Form

The following is a list of field descriptions for the PR Add
 Trans to Timecard Batch form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Options

- Add Timecards from Current Payroll
 – Select this option to add timecards already posted within the current payroll.

- Add Reversing Timecards – Select
 this option to add timecards posted from a previous payroll.

##  Period Ending Date

 Enabled only when reversing timecards.
 Specify the pay period ending date for which to reverse timecards.

##  Post to Pay Seq

 Enabled only when reversing timecards.
 Specify the posting pay sequence for the reversing entry; must be a valid pay sequence for the current pay period.
 If this field is left blank, all reversing entries are added using their original posted payment sequence number.

## Timecard Type

Specify the timecard type to add to the batch:

- J-Job - Select this type if adding
 only job timecards to batch. (Default setting)

- M-Mechanic - Select this type if
 adding only mechanic timecards to batch.

- SM Work Orders - Select this type if adding only SM technician timecards to batch.

- Blank - Select this option to include all timecards, regardless of type.

## Last Posted Batch#

Specify the batch number to recall a group of associated timecards.
Note: Each timecard is associated with a batch number. This batch number updates whenever a timecard is pulled into a batch for editing and reposting.

##  Employee #

 Specify the employee whose timecards you want added to this batch. If left blank, all employees, that match any additional filtering criteria, are added to the batch.

##  Pay Seq

 To restrict batched timecards by pay sequence, specify a valid pay sequence. Only timecards with this pay sequence are added to the batch.

##  Post Seq

 Specify the posting sequence to restrict batched timecards by post sequence. Only timecards with this post sequence are added to the batch.

##  Beginning/Ending Timecard Date

 To restrict posted timecards to a particular date range, specify the beginning and ending posting date. Otherwise, leave blank to pull in all timecards from the pay period.

##  Craft

 This field allows you to restrict batched timecards to a specific craft.

##  Class

 This field allows you to restrict batched timecards to a specific class.

##  Earnings Code

 This field allows you to restrict batched timecards to a specific earning code.

##  Shift

 This field allows you to restrict batched timecards to a specific shift.

##  JC Co#

 This field allows you to restrict batched timecards to a specific JC Company.

## Job

This field allows you to restrict batched timecards to a specific job.
Note: The specified Job code must exactly match to restrict timecards properly.

## Phase

This field allows you to restrict batched timecards to a specific phase.
Note: The specified Phase code must exactly match to restrict timecards properly.

## SM Co #

Entry in this field is only applicable if the
 Timecard
 Type is S - SM Work Order or blank.
Enter the Service Management (SM) company by
 which to restrict timecards added to this batch. Only timecards posted to this SM company
 that meet all other restriction criteria will be added to this batch.
Note: Entry in this field is required if you will also be
 restricting timecards by SM Work Orders, SM Scope, and/or SM Pay Types.

## SM Work Order

Entry in this field is only applicable if the
 Timecard
 Type is S - SM Work Orders or blank. In addition, you must first specify a
 valid company in the SM Co # field.
Enter the work order (from SM Work Orders) by
 which to restrict timecards added to this batch. Press F4 for a list of valid work orders for
 the specified SM company. Only timecards posted to this work order that meet all other
 restriction criteria will be added to this timecard batch.

## SM Scope Seq

Entry in this field is only applicable if the
 Timecard
 Type is S - SM Work Orders or blank. In addition, you must first specify a
 valid company in the SM Co # field (above).
Enter the scope (from the specified work
 order) by which to restrict timecards added to this batch. Press F4 for a list
 of valid scopes for the specified work order. Only timecards posted to this scope that meet
 all other restriction criteria will be added to this batch.

## SM Pay Type

Entry in this field is only applicable if the
 Timecard
 Type is S - SM Work Orders or blank. In addition, you must first specify a
 valid company in the SM Co # field (above).
Enter the pay type (from SM Pay Types) by
 which to restrict timecards added to this batch. Press F4 for a list of valid pay types for the
 specified SM Co. Only timecards posted to this SM pay type that meet all other restriction
 criteria will be added to this batch.

## SM Cost Type

Entry in this field is only applicable if the
 Timecard
 Type is S - SM Work Orders or blank. In addition, you must first specify a
 valid company in the SM Co # field (above).
Enter the cost type (from SM Cost Types) by
 which to restrict timecards added to this batch. Press F4 for a list of valid cost types for the
 specified SM company. Only timecards posted to this SM cost type that meet all other
 restriction criteria will be added to this batch.

##  Exclude timecards if Employee/Pay Seq# is paid

 This checkbox is enabled only when adding timecards from a current payroll.
 Check this box to skip timecards for any employee or pay sequence that has already been paid.
 This checkbox defaults to “checked” (“yes”).

## Mark added timecards as Delete

Enabled only when adding timecards from a current payroll.
Check this box if all timecards added to batch should be marked for deletion.
Do not check this box if you do not want to delete timecards added to batch.
The checkbox defaults to “unchecked” (“no”).
