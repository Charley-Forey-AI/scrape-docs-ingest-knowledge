---
title: "Field Definitions: PR Crews Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-crews-form/field-definitions-pr-crews-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-crews-form/field-definitions-pr-crews-form"
---

# Field Definitions: PR Crews Form

The following is a list of field descriptions for the PR Crews form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Crew

Enter a unique code, up to 10 characters, to
 identify a group of employees and/or equipment that commonly work together. Crews can be
 used in PR Timecard Entry to automatically post one line of earnings to each member of the
 crew.

##  Description

Enter a description for this crew, which will
 be used for reports.

##  JC Co#

Enter the default JC company for this crew.
 Entry in this field is required if you are initializing timesheets for this crew in PR Crew
 Timesheet Entry.

## Job

Enter the default job for this crew. Entry in this field is required if you are initializing timesheets for this crew in PR Crew Timesheet Entry.
Note: If you enter a soft- or hard-closed job, the status
 displays in red to the right of the job description. The system will only save the record
 if you allow posting to soft- or hard-closed jobs (you checked the Allow Posting to
 Soft-Closed Jobs and Allow Posting to Hard-Closed Jobs boxes
 in JC Company Parameters).

## Timesheet Phases

Enter up to eight valid phases for this crew/job. The phases entered here default into the timesheet grid when you initialize timesheets for this crew (in PR Timesheet Entry). They are also used for posting progress units to job cost.
If you require more than eight phases, you can manually add them to subsequent timesheets for the crew (in PR Timesheet Entry).

## Timesheet Earnings Codes Overrides: Regular

Specify the override earnings code for regular
 hours for this crew. This earnings code is used when sending timesheets to a payroll
 timecard batch. If this is left blank, the earnings code for regular hours specified in PR
 Company Parameters (Regular field) is used.

## Timesheet Earnings Codes Overrides: Overtime

Specify the override earnings code for
 overtime hours for this crew. This earnings code is used when sending timesheets to a
 payroll timecard batch. If this is left blank, the earnings code for overtime hours
 specified in PR Company Parameters (Overtime field) is used.

## Timesheet Earnings Codes Overrides: Doubletime

Specify the override earnings code for
 double-time hours for this crew. This earnings code is used when sending timesheets to a
 payroll timecard batch. If this is left blank, the earning code for double-time hours
 specified in PR Company Parameters (Doubletime field) is used.

## PR Group

Enter the payroll group for this crew. Press
 F4
 for a list of valid payroll groups. The employees you [add to this
 crew](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payroll-crews/add-employees-to-payroll-crews) (on the Crew Members tab) must have the same payroll group assigned in their
 employee record (PR
 Group field in PR Employees).

## Shift

Enter the shift for this crew. The shift that you specify here defaults on timesheets and/or timecards initialized for this crew. You may override the default.
Note: If you initialize crew timecards (PR Initialize Crew Timecards), and have not specified a shift for the crew, timecards default as shift 1, regardless of whether you entered a default shift here.

## Timesheets Require Approval

Check this box if crew timesheets must be approved (PR Timesheet Approve) before they are sent to a payroll, job cost, or equipment usage batch (in PR Timesheet Send).
Do not check this box if crew timesheets can be sent to payroll, job cost, or equipment usage batches without approval.

## Seq#

Enter a number between 1 and 999 to identify a unique entry within the crew. This allows an employee to be referenced more than once within a crew.

## Employee

Required for timecards, optional for timesheets.
Enter the number or sort name of the employee
 you want to assign to this crew. Press F4 for a list of employees. The employee’s last and
 first name display in the Name field to the right.
Note: You can add employees to a crew multiple times as necessary (e.g., employees assigned to multiple pieces of equipment). If initializing crew timecards (PR Initialize Crew Timecards), one timecard entry is generated for each employee entry here. If initializing crew timesheets (PR Crew Timesheet Entry), one entry is generated per employee in the Employee Hours grid, and one equipment usage entry generated for each employee/equipment entry.

## Use Std Hrs

Check this box if timecards will be initialized with the labor hours entered, and earnings will be calculated using the standard rate default. All new entries initially default as checked.
Do not check this box if timecards will not be initialized with labor hours entered. Hours and earnings will be set to 0.00. Only equipment usage is included on timecards.
Note: This field does not apply to crew timesheets.

## Add-on Hrs

Enter the number of additional hours to post when a timecard is generated for the Employee, if desired. The default for this field is 0.00. This field is typically used for foremen.
Note: This field does not apply to crew timesheets.

## EM Co#

The system displays this field when you check
 the Enter Equipment
 Usage with Time Cards box in PR Company Parameters.
Enter the EM company to use when posting
 equipment usage. This field initially defaults from the EM Co # field
 in PR Employees. If that field is blank, this field defaults from the EM Co# field in
 PR Company Parameters (Equipment tab).

## Equipment

The system displays this field when you check
 the Enter Equipment
 Usage with Time Cards box in PR Company Parameters.
Enter a valid equipment code to identify the
 equipment used by this employee, if you are posting usage. This field defaults from the
 Equipment
 Code field in PR Employees (Add'l Info tab).
Note: Timecards cannot be posted to equipment-only sequences. If you will be using this crew to initialize timecards, you must specify an employee for this equipment.

## RevCode

The system displays this field when you check
 the Enter Equipment
 Usage with Time Cards box in PR Company Parameters.
Enter the revenue code to use when posting
 usage to this equipment. Press F4 to see a list of valid revenue codes.
 This code is used to identify the type and rate charged to use the equipment you specified
 in the Equipment field.

## UsagePct

Enter the percent of posted hours that will default for usage units (e.g., when initializing timecards for a Crew and entering standard hours of 8.00, if this percent was 50%, then 4.00 hours of equipment usage will be posted). If equipment has been entered, the default is 100%.
