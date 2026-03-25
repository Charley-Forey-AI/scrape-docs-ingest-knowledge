---
title: "Enter Start and Stop Time on Timecards | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-start-and-stop-time-on-timecards"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-start-and-stop-time-on-timecards"
---

# Enter Start and Stop Time on Timecards

When entering timecards in PR Timecard Entry, you may enter the start, stop, and break time for the employee.
Once you enter this information, the system will automatically default the hours worked to the Hours field for the timecard record.
Note: Prior to entering start, stop, and break time you must initially do the following:

- The Start Time, Stop Time, and Break Hours fields do not automatically display in the PR Timecard Entry grid. To add them to the grid, select Options  Customize Grids to display the PR User Grid Options form. Select Field in grid from the Start/Stop field on each of the applicable tabs (Job Timecards, Mechanics Timecards, Service Timecards). Save the record, close the form and the fields will display in the timecard grid. For more information, see [PR User Grid Options](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-user-grid-options-form).

- Verify that the setting of the Timecard Stop Time must be greater than Start Time checkbox in PR Company Parameters is correct. For more information, see [Timecard Stop Time must be greater than Start Time](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form/field-definitions-pr-company-parameters-form#ID-000358ed--en).

The following details how to enter start, stop, and break time on timecard records. All of the steps are optional.

1. Enter the starting time (24-hour format) in the Start Time field.

1. Enter the stop time (24-hour format) in the Stop Time field. If you checked the Timecard Stop Time must be greater than Start Time box in PR Company Parameters, the time you enter here cannot be less than the Start Time value. If the Timecard Stop Time must be greater than Start Time box is not checked, all time after 24 hours will be considered the next day.Note: If you leave either the Start
 Time or Stop
 Time field blank, the system will not record a start/stop time
 period.

1. Enter the number of hours that the employee took for a break in the Break Hours field. The Hours field will now default the start/stop time minus the specified break time.

1. Enter the rest of the timecard information and save the record.

1. Enter any additional timecard records. If you enter another record for the same employee and date, and the start/stop time periods overlap, the system will not let you save the new record.

Related information

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [Posting Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/posting-timecards)
