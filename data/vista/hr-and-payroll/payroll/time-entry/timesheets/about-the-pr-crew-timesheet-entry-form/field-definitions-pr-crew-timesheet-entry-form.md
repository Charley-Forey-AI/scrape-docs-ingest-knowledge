---
title: "Field Definitions: PR Crew Timesheet Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-crew-timesheet-entry-form/field-definitions-pr-crew-timesheet-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-crew-timesheet-entry-form/field-definitions-pr-crew-timesheet-entry-form"
---

# Field Definitions: PR Crew Timesheet Entry Form

The following is a list of field descriptions for the PR Crew Timesheet Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Crew

 Specify the crew to which this timesheet applies; must be a valid crew from PR Crews.

##  Date

 Enter the timecard date for this timesheet.

##  Sheet #

 Enter a unique number for this crew timesheet. Although you can enter any number between -32,768 and 32,767, this is typically '1' or '2'.

## JC Co#

Specify the JC company to which this crew timesheet applies. Initially defaults the JC company specified for this crew in PR Crews.
Note: If you enter a soft- or hard-closed job, you can only save the record if you allow posting to hard and/or soft-closed jobs (flags in JC Company Parameters). Status for hard/soft closed jobs displays in red beside the sequence.

## Job

Specify the job (JC Jobs) to which this crew timesheet applies.
 Initially defaults the job specified for this crew in PR Crews.
Note: If you enter a soft- or hard-closed job, status displays in red to the right of the job description. Record will only be saved if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters). It is important to note that although you cannot save the timesheet record, you can update a closed job to the crew setup (Update Crew button), regardless of whether you allow posting to closed jobs.

##  Shift

 Specify the shift to which this timesheet applies. Initially defaults the shift specified for this crew in PR Crews or, if no shift specified, defaults to '1'.

## Phase

Timesheet automatically defaults all phases set up for this crew in PR Crews. If you elect to 'Default Phases on Sheet #1 Only' (Options menu), phases only default for the first timesheet. All other timesheets default as null.
You can add or change phases as necessary, but you must click your cursor in another tab’s grid (or use the Save button) to save the addition/change. If you delete a phase, any entries in the Other Job Earnings tab related to that phase will be removed from the grid.
Note: If the job is locked and you enter a phase that is not set up for the job (in JC Job Phases), a warning is displayed; however, entry is allowed.
If you wish to update additional or changed phases to the crew in PR Crews, you can do so by clicking the 'Update Crew' button at the bottom of the form. However, this function is limited to Sheet #1 only. The 'Update Crew' button is disabled for all timesheets except Sheet #1.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete,’ these fields are disabled. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Progress Units

Enter the progress units for this phase. Progress units entered here are updated for this phase/cost type in JCPP (JC Progress Batch) when this timesheet is sent (in PR Timesheet Send).
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', these fields are disabled. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

##  UM

 Display only, the unit of measure for this
 phase/cost type (as defined in JC Phases or JC Job Phases).

## Cost Type

Specify the cost type to which progress units
 for this phase will be posted; must be a valid cost type for this phase (as defined in JC
 Phases or JC Job Phases).
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', these fields are disabled. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Employee Hours: Employee

Timesheet automatically defaults all employees set up for this crew (in PR Crews). Employees set up multiple times in a crew (e.g. employees assigned to multiple pieces of equipment) are set up only once in this grid.
You can add or delete employees as necessary. When adding, assign the employee to the same payroll group as is specified for this crew (in PR Crews). If deleting, and the employee is assigned to equipment in the Equipment Usage grid, the equipment usage record is left intact, but the employee is removed from the record.

- Employees added to (or deleted from) this timesheet can be updated to the standard crew setup in PR Crews by clicking the 'Update Crew' button at the bottom of the form. However, this function is limited to Sheet #1 only. The 'Update Crew' button is disabled for all timesheets except Sheet #1.

- If a timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Employee Hours: Craft

This column only displays in the grid if the 'Craft' option is checked in the Options menu.
Specify the craft under which the employee worked on this job. Initially defaults the craft assigned to this employee in PR Employees or, if a craft template is assigned to the job and an override craft is specified, from PR Craft Template.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Employee Hours: Class

Specify the class that the employee worked for
 on this job. Press F4 for a list of valid classes for the specified craft. This field
 initially defaults the class assigned to this employee in PR Employees.
Note: If this timesheet's status is 'Awaiting Approval',
 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need
 to make changes and the status is not 'Send Complete', you can do so by clicking Unlock/Edit.

## Employee Hours: Reg Hrs

Specify the number of regular hours this employee worked on this job/phase, or accept the default of 0.00 if this employee did not work on this phase.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Employee Hours: OT Hrs

This column only displays in the grid if the 'Overtime Hours' option is checked in the Options menu.
Specify the number of overtime hours this employee worked on this job/phase, if applicable. Otherwise, accept the default of 0.00.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Employee Hours: Dbl Hrs

This column only displays in the grid if the 'Doubletime Hours' option is checked in the Options menu.
Specify the number of double-time hours this employee worked on this job/phase, if applicable. Otherwise, accept the default of 0.00.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Equipment Usage: EM Co

Timesheet automatically defaults all equipment set up for this crew (in PR Crews). You can add or delete equipment as necessary.
If adding new equipment to this crew/timesheet, specify the EM company to which the equipment belongs and to which equipment usage will be posted for this job.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Equipment Usage: Equipment

Timesheet automatically defaults all equipment set up for this crew (in PR Crews). You can add or delete equipment as necessary.
If adding new equipment to this crew/timesheet, equipment must be valid for the specified EM Company. Equipment added to this timesheet can be updated to the standard crew setup in PR Crews by clicking the 'Update Crew' button at the bottom of the form. However, this function is limited to Sheet #1 only. The 'Update Crew' button is disabled for all timesheets except Sheet #1.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Equipment Usage: Employee

Specify the employee who operated this equipment on this job/phase. Initially defaults the employee who was assigned to this equipment in PR Crews.

- If you delete an employee from the Employee Hours grid, who is assigned to equipment in this grid, the employee is removed from this grid also; however, the equipment usage record will be left intact.

- If a timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Equipment Usage: Usage Units

### Automatic Entry

Click the "Initialize Usage" button to
 initialize usage for each phase based on the values entered for the employee/phase on
 the Employee Hours tab. Usage units are calculated based on the hours entered for the
 employee/phase and the Usage % specified in PR Crews. For example, if the employee
 worked 8.00 hours and the Usage % is 50.00, the usage units will be 4.00.

### Manual Entry

Specify the usage units for this
 equipment/phase.

- Deleting an employee from the
 Employee Hours grid will automatically delete the employee from any equipment
 usage record in this grid and set the usage units to zero. If you manually delete
 an employee from this grid, the usage units will be left intact.

- If this timesheet's status is
 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be
 accessed for editing. If you need to make changes and the status is not 'Send
 Complete', you can do so by clicking the Unlock/Edit button.

## Equipment Usage: Cost Type

This column only displays in the grid if the 'Cost Type' option is checked in the Options menu.
Specify a valid JC cost type for this equipment/phase. Initially defaults the usage cost type specified for this equipment in EM Equipment. This is the cost type to which usage for this job/equipment/phase will be posted.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Equipment Usage: Rev Code

This column will only display in the grid if the 'Rev Code' option is checked in the Options menu.
Specify the revenue code for this equipment/phase. Initially defaults the revenue code specified for this equipment in PR Crews. The revenue code specified here will be used to determine the rate charged to use this equipment.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Other Job Earnings: Employee

Enter the employee for which to post 'other' job earnings (e.g. subsistence, expense reimbursements, etc.). Can be an employee already set up for the crew (on Employee Hours tab) or a new employee. If a new employee, must be a valid PR employee assigned the same payroll group as is specified for the crew (in PR Crews).

- Employees entered on this tab will not updated for this crew in PR Crews when using the 'Update Crew' button. Employee must exist on the Employee Hours or Equipment Usage tabs to be updated to PR Crews.

- If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Other Job Earnings: Craft

This column will only display in the grid if the 'Craft' option is checked in the Options menu.
Specify the craft that applies to this employee's other job earnings. Initially defaults the craft assigned to this employee in PR Employees or, if a craft template is assigned to the job and an override craft is specified, from PR Craft Template.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Other Job Earnings: Class

Specify the class that applies to this employee's other job earnings. Must be a valid class for the specified craft. Initially defaults the class assigned to this employee in PR Employees.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Other Job Earnings: Earn Code

Specify a valid earnings code for this employee's other job earnings.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Other Job Earnings: Hrs/Amt

Enter the hours worked or amount earned (depending on the earnings method) on this phase that apply to 'other job earnings' for this employee.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Non-Job Earnings: Employee

Enter the employee for which to post non-job earnings (e.g. vacation, time missed, etc.). Can be an employee already set up for the crew (on Employee Hours tab) or a new employee. If a new employee, must be a valid PR employee assigned the same payroll group as is specified for the crew (in PR Crews).

- Employees entered on this tab will not updated for this crew in PR Crews when using the 'Update Crew' button. Employee must exist on the Employee Hours or Equipment Usage tabs to be updated to PR Crews.)

- If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Non-Job Earnings: Craft

This column only displays in the grid if the 'Craft' option is checked in the Options menu.
Specify the craft that applies to this employee's non-job earnings. Initially defaults the craft assigned to this employee in PR Employees or, if a craft template is assigned to the job and an override craft is specified, from PR Craft Template.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Non-Job Earnings: Class

Specify the class that applies to this employee's non-job earnings; must be a valid class for the specified craft. Initially defaults the class assigned to this employee in PR Employees.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Non-Job Earnings: Earn Code

Specify a valid earnings code for this employee's non-job earnings.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Non-Job Earnings: Hours

Enter the hours worked by this employee that apply to non-job earnings.
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.

## Non-Job Earnings: Use Std Pay Rate

Check this box to use the employee's standard pay rate (defined in PR Employees) for this non-job earnings.
Do not check this box if you do not want to use the employee's standard pay rate. Pay rate will be set to 0.00 for these non-job earnings in the timecard batch (PR Timecard Entry).
Note: If this timesheet's status is 'Awaiting Approval', 'Ready to Send', or 'Send Complete', this field cannot be accessed for editing. If you need to make changes and the status is not 'Send Complete', you can do so by clicking the Unlock/Edit button.
