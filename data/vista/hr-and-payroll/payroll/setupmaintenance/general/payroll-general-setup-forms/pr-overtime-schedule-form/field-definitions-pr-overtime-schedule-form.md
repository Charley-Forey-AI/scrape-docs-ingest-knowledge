---
title: "Field Definitions: PR Overtime Schedule Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-overtime-schedule-form/field-definitions-pr-overtime-schedule-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-overtime-schedule-form/field-definitions-pr-overtime-schedule-form"
---

# Field Definitions: PR Overtime Schedule Form

The following is a list of field descriptions for the PR
 Overtime Schedule form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  OT Schedule

Enter a number (0-255) to identify this
 overtime schedule.
 An overtime schedule is used to maintain daily overtime “rules” to be applied by employee, craft, or job.

##  Description

Enter a description for this overtime
 schedule, up to 30 characters.

## Level 1, 2, 3 Hours

### Level 1

Enter the maximum number of straight-time hours (0-24) that can be worked before
 overtime is calculated at this level, with this specified overtime earnings code. For
 example, if overtime is calculated after 8 hours, you would enter 8.00. If you want all
 hours worked in a day to be treated as overtime, enter 0.00. If you do not want any
 overtime calculated for a specific day, enter 24.00.Note:If you set these hours to 0.00, and Level 2 hours are greater than 0.00, all Level
 1 hours will be treated as overtime up to the number of hours specified for Level
 2, at which point they will be paid as indicated by the OT code.

### Levels 2 & 3

Typically, multiple levels are defined when more than a single premium time rate may be
 applied in a day (e.g., an employee receives time and a half after 8 hours and double
 time after 10.5 hours).
If you are using this feature, specify the maximum number hours worked before overtime
 is calculated at these levels. If you do not want any overtime calculated for a specific
 day (or you are not using this feature), you can leave the hours at 0.00 as long as no
 OT code is entered. Otherwise, you will need to enter 24.00.

## OT Code

### Level 1

Required.
Enter the earnings code (from PR Earnings Codes) that will be used when overtime is
 calculated. Initially defaults the Overtime Earnings Code assigned in PR Company
 Parameters; may be overridden.

### Levels 2 & 3

Typically, multiple levels are defined when more than a single premium time rate may be
 applied in a day (e.g. an employee receives time and a half after 8 hours and double
 time after 10.5 hours).
If you are using this feature, specify the earnings code to use when overtime is
 calculated at this level. Initially defaults as null (blank).
If you specified 0.00 hours (or you are not using this feature), this field can be left
 blank.
