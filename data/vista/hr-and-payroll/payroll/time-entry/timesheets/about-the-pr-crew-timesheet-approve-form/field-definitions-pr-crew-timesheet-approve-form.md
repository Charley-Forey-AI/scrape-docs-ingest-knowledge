---
title: "Field Definitions: PR Crew Timesheet Approve Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-crew-timesheet-approve-form/field-definitions-pr-crew-timesheet-approve-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-crew-timesheet-approve-form/field-definitions-pr-crew-timesheet-approve-form"
---

# Field Definitions: PR Crew Timesheet Approve Form

The following is a list of field descriptions for the PR Crew Timesheet Approve form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  PR Group

 Required.
 Specify the PR group for which to approve timesheets.

##  Select Job

 Check this box to populate the grid with timesheets for a specific company and job (specified to the right).
 Do not check this box if you want to display all timesheets, regardless of company and job.

##  JC Co

 Enabled when "Select Job" option is checked.
 Specify the JC company by which to restrict timesheet selection. Only timesheets posted to this JC company display in the grid below.

## Job

Enabled when "Select Job" option is checked.
Specify the job by which to restrict timesheet selection. Only timesheets posted to this job (for the specified JC company) display in the grid below. If left blank, all timesheets posted to the JC company specified to the left will be displayed, regardless of job.
Note:If you enter a soft- or hard-closed job, the status displays in red above this field. The system will only save the record if you allow posting to soft or hard-closed jobs (flags in JC Company Parameters).

##  Select Crew

 Check this box to populate the grid with timesheets for a specific crew (specified to the right).
 Do not check this box if you want to display all timesheets, regardless of crew.

##  Crew

 Enabled when "Select Crew" option is checked.
 Specify the crew by which to restrict timesheet selection. Only timesheets posted to this crew display in the grid below.

## Approved

The grid displays all timesheets (meeting the selection criteria) with a status of 'Awaiting Approval', 'Editable' (highlighted in red), and 'Ready to Send' (highlighted in green). However, only timesheets with a status of 'Awaiting Approval' that are not marked as 'In Use' can be approved.
You can check this box manually for each eligible timesheet or use the 'Approve All' button to automatically flag all eligible timesheets as approved. Once checked, all approved timesheets are set to a status of 'Ready to Send' and the Approved By column will be populated with the user's login.
Note:The 'Approved' box can be unchecked for any timesheet until it is sent to a PR, JC, or EM batch (in PR Timesheet Send).
