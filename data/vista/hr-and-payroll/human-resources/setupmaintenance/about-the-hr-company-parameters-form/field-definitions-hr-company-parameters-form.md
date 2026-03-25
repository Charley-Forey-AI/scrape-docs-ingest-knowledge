---
title: "Field Definitions: HR Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-company-parameters-form/field-definitions-hr-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-company-parameters-form/field-definitions-hr-company-parameters-form"
---

# Field Definitions: HR Company Parameters Form

The following is a list of field descriptions for the HR
 Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  HR Company

 Enter the number of the HR company you want to create and maintain. Must be a valid company set up in HQ.

##  PR Company

 Required.
 Enter the Payroll company that will be used as the default when adding a resource in this HR company. This company will also be used to validate deductions and liabilities set up for a resource in the HR Benefits forms, and to determine the GL company (for batch month validation) when creating batches in HR Update Benefit/Salary to PR.

##  Employment History Event Options

 This section is used to identify which resource events you want updated to the Employment History (HREH) log. If an event is checked, you must specify the History Code (to the right of the event) under which the event will be tracked. Each time a change is made to the associated program, an entry is logged to the specified History Code in HREH.
Note: History codes are set up in HR Codes, and must be
 flagged as Type H (History).

- Dependents – Check this option if you
 want an entry logged in the HREH file each time a change is made to a resource’s
 dependent information in HR Resource Dependents.

- Benefits – Check this option if you
 want an entry logged in HREH each time a change is made to a resource’s benefits
 information in HR Resource Benefits.

- Salary - Check this option if you
 want an entry logged in the HREH file each time a change is made to a resource’s
 salary information in HR Resource Salary History.

- Reviews - Check this option if you
 want an entry logged in the HREH file each time a change is made to a resource’s
 review information in HR Resource Review.

- Training - Check this option if you
 want an entry logged in the HREH file each time a change is made to a resource’s
 training information in HR Resource Training.

- Skills - Check this option if you
 want an entry logged in the HREH file each time a change is made to a resource’s
 skill information in HR Resource Skills.

- Rewards - Check this option if you
 want an entry logged in the HREH file each time a change is made to a resource’s
 reward information in HR Resource Rewards.

- Discipline - Check this option if you
 want an entry logged in the HREH file each time a change is made to a resource’s
 discipline information in HR Resource Discipline.

- Grievances - Check this option if you
 want an entry logged in the HREH file each time a change is made to a resource’s
 grievance information in HR Resource Grievances.

- Accidents - Check this option if you
 want an entry logged in the HREH file each time a change is made to a resource’s
 accident information in HR Resource Accident.

- Drug Testing - Check this option if
 you want an entry logged in the HREH file each time a change is made to a
 resource’s drug testing information in HR Resource Drug Testing.

##  Dependent History Code

 Specify the history code (from HR Codes, Type
 H) under which to track dependent history.

##  Benefit History Code

 Specify the history code (from HR Codes, Type
 H) under which to track benefits history.

##  Salary History Code

 Specify the history code (from HR Codes, Type
 H) under which to track salary history.

##  Review History Code

 Specify the history code (from HR Codes, Type
 H) under which to track review history.

##  Training History Code

 Specify the history code (from HR Codes, Type
 H) under which to track training history.

##  Skills History Code

 Specify the history code (from HR Codes, Type
 H) under which to track skills history.

##  Rewards History Code

 Specify the history code (from HR Codes, Type
 H) under which to track rewards history.

##  Discipline History Code

 Specify the history code (from HR Codes, Type
 H) under which to track discipline history.

##  Grievance History Code

 Specify the history code (from HR Codes, Type
 H) under which to track grievance history.

##  Accident History Code

 Specify the history code (from HR Codes, Type
 H) under which to track accident history.

##  Drug Testing History Code

 Specify the history code (from HR Codes, Type
 H) under which to track drug-testing history.

## FMLA Eligibility: Number of Employed Months Required

Specify the number of month’s a resource must be employed in order to be eligible for medical leave as outlined by the Family Medical Leave Act (FMLA). The system uses the information in this field in conjunction with PR Leave Entry for reporting purposes (HR FMLA Tracking Report).
Note: The system uses the Federal requirements if they are more generous than the state requirements.

## FMLA Eligibility: Number of Hours Worked Required

Specify the number of hour’s a resource must have worked in order to be eligible for medical leave as outlined by the Family Medical Leave Act (FMLA). The system uses the information in this field in conjunction with PR Leave Entry for reporting purposes (HR FMLA Tracking Report).
Note: The system uses the Federal requirements if they are more generous than the state requirements.

## Default Status Code

Enter the default code to use in the
 Status field in HR Resource Drug Testing. Press F4 for a list of available
 status codes (set up in HR Codes).

## PR Update Options

This section controls what information set up (or changed) for a resource in Human Resources will be updated to Payroll, and what information set up (or changed) in Payroll will be updated to Human Resources.
For each option listed below, check the box to
 have PR updated online whenever the resource’s corresponding information has been changed
 in HR Resources. Resource must be assigned a valid PR employee number in order for updates
 to occur. Likewise, if checked, HR will be updated online when the employee’s corresponding
 information has been changed in PR Employees. Employee must be assigned a valid resource
 number in order for updates to occur.
If an option is left unchecked, no online updates will occur, and information will need to be changed manually.

- Name (name, birth date, race, and gender)

- Address

- Hire/Term Date

- Active Flag

- Timecard Defaults (department, craft, class, local code, earnings code, insurance code and state, tax state, and/or unemployment state).

- W-4 Info (deductions, exemptions, and filing status)

- Occupation Category (occupational category and category status)

- Social Security Number

Information related to these two options is not updated online; rather, it will be updated when HR Update Benefit/Salary to PR is run and the batch is processed.

- Salary

- Benefits

##  Audit Options

The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
The following lists and describes the audit options.

- Company - This audit option is display only, and is always checked. Any changes made to the HR Company Parameters program will be tracked in the Master Audit file.

- Resource Master – Check this box to record changes
 made to the HR Resources.

- Benefits – Check this box to record changes made in HR Resource Benefits

- Salary History – Check this box to record changes made in HR Resource Salary History.

- Review History – Check this box to record changes made in HR Resource Review.

- Skills – Check this box to record changes made in HR Resource Skills.

- Training – Check this box to record changes made in HR Resource Training.

- Rewards – Check this box to record changes made in HR Resource Rewards.

- Discipline History – Check this box to record changes made in HR Resource Discipline.

- Grievance History – Check this box to record changes made in HR Resource Grievances.

- Accidents – Check this box to record changes made in HR Resource Accident.

- Positions – Check this box to record changes made to position codes, position qualifications, and position training in HR Resource Position Codes.

- Employment History – Check this box to record changes made in HR Resource Employment History. Only changes made in this form are recorded; changes made to employment history in other forms are not recorded.

- Drug Testing – Check this box to record changes made in HR Resource Drug Testing.

- Company Assets – Check this box to record changes made in HR Company Assets, HR Company Asset Check Out, and HR Asset In/Out by Resource.

- Leave Requests – Check this box to record changes made in HR Leave Request and HR Leave Approval.

Note: When setting up a company, the entry of invalid data in certain fields will cause a warning; however, entries will be allowed and you will be able to save the record. This primarily applies to (but is not limited to) required data such as the ‘interface to’ companies and journals, since it is sometimes necessary to set up the company information before you can set up the data being requested.
