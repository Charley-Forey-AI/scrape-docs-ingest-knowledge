---
title: "Field Definitions: PR Timecard Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form/field-definitions-pr-timecard-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form/field-definitions-pr-timecard-entry-form"
---

# Field Definitions: PR Timecard Entry Form

The following is a list of field descriptions for the PR
 Timecard Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Copy 0-2

The Copy 0-2 field on the PR Timecard Entry form.
This feature is only available in Add mode, and copies values from the previous timecard line to a new timecard line, allowing for speedier timecard entry. The options differ depending on the timecard line type (Job, Mechanic, SM Work Order).

### Job Timecards

- 0 - Adds a new entry, copying all information from the previously entered timecard up to and stopping at the Phase column. The Rate field defaults based on the earnings code, but remaining columns default as blank.

- 1 - Adds a new entry, copying all information from the previously entered timecard up to and stopping at the EC column. Rate defaults based on earnings code, but remaining columns default as blank. All remaining columns default from the previous line, with the exception of hours and usage. If there is a piece of equipment assigned to the employee in PR Employees, equipment information will also default (e.g. equipment, equip phase, revenue code, etc.).

- 2 - Adds a new entry, copying all information (except hours and amount) from the previously entered timecard up to and stopping at the Equip column. This option is generally used when an employee has operated multiple pieces of equipment at the same time for the same job and phase. In this case, you would not want to duplicate the hours and dollars, rather just record the additional equipment usage for that employee. Therefore, the hours and dollars are assumed to be 0.00.Note: This option is only available if the Enter Equipment Usage with Time Cards checkbox in PR Company Parameters (Equipment tab) is selected.

- + - Adds a new entry, copying all information from the previous line and incrementing the date (or day) by one.

Note: Each option (0-2) displays in the grid column corresponding to the copy feature. In other words, 0 displays in the Phase column, 1 displays in the EC column, and 2 displays in the Equip column. This allows for quick identification of the "copy up to" point.

### Mechanic Timecards

- 0 - Adds a new entry, copying all information from the previously entered timecard up to and stopping at the WO column. All remaining columns default from the previous line, with the exception of hours and equipment information (e.g. equipment, cost code, component, etc.).

- 1 - Adds a new entry, copying all information from the previously entered timecard up to and stopping the cursor at the Equip field/column. The Rate column defaults based on the earnings code.

- 2 - Adds a new entry, copying all information from the previously entered timecard up to and stopping at the EC column (except for the hours and amount).

- + - Adds a new entry, copying all information from the previous line and incrementing the date (day) by one.

Note: Each option (0-2) displays in the grid column corresponding to the copy feature. In other words, 0 displays in the label for the WO column, 1 displays in the label for the Equip column, and 2 displays in the label for the EC column. This allows for quick identification of the "copy up to" point.

### SM Work Order Timecards

- 0 - Adds a new entry, copying all information from the previously entered timecard up to and stopping at the Ins State column. All remaining columns default as null (with the exception of the EC, Shift, and Rate columns. See F1 help for default information).

- 1 - Adds a new entry, copying all information from the previously entered timecard up to and stopping at the SM Co column. All remaining columns default as null (with the exception of the EC, Shift, and Rate columns. See F1 help for default information).

- 2 - For customer work orders, entering 2 adds a new entry, copying all information from the previously entered timecard up to and stopping at the SM Pay Type column. All remaining columns default as null (with the exception of the EC , Shift, Rate, Craft, and Class columns. See the F1 help for default information.For job-related work orders, entering 2 adds a new entry, copying all information from the previously entered timecard up to and stopping at the SM JC Cost Type column. All remaining columns default as null (with the exception of the EC , Shift, Rate, Craft, and Class columns. See the F1 help for default information.

- + - Adds a new entry, copying all information from the previous line and incrementing the date (day) by one.

Note: Each option (0-2) displays in the grid column corresponding to the copy feature. In other words, 0 displays in the label for the Ins State column, 1 displays in the label for the SM Co column, and 2 displays in the label for the SM Pay Type column. This allows for quick identification of the "copy up to" point.

## Employee

Enter the employee number for the employee or mechanic associated with this timecard entry. If you do not know the employee number, in addition to using the F4 lookup, you may enter alpha characters that will be matched to the employee sort name for the first closest match. The resulting employee number displays and the employee’s name displays below.
The employee must be active and assigned to the PR group for this batch. The default is the employee number of the previous line. If the employee has already been paid, a warning is given but entries may be made.
The employee number of an existing line may not be changed. The timecard line must be deleted and re-added with the correct employee number.
Note: This field standardly defaults the 'previous' employee (whether or not you use the Copy 0-2 function). If you have set up a user override of 'Normal' (in F3 Properties), this field defaults to a null value. If you do not enter an employee (i.e. leave null), when you tab off the field, it defaults the previous employee.

## Type

Select the type of timecard line. The following options are available:

- J - Job

- M- Mechanic

- S - SM Work Order

Note: Timecards with a type of S-SM Work Order) will
 automatically create a corresponding work completed labor line for the work order (in
 SM Work Orders).
For Australian and Canadian companies
Entry of time to a non-job SM work order will
 automatically set the Tax Type to 3-VAT for the work completed
 labor line in SM Work Orders. The tax code for the work completed line will default from
 the Service Center or Service Site (depending on the Tax Source specified for the work
 order) and must be a VAT-type code. For this function to work, the SM company's AR company
 (defined in SM Company Parameters) must be set up with a Default Country
 of AU or CA in HQ Company Setup.

## Action

When adding new entries, or when adding
 reversing timecards (Add Timecard Entry, File menu), this field defaults to A-Add and
 cannot be changed.
If adding timecards from the current payroll (Add Timecard Entry, File menu), specify the action for this entry.

- C-Change – Use this action to make
 changes to transactions that have already been processed.

- D-Delete – Use this action to
 delete the transaction from all files in Payroll (the delete functions in the toolbar
 and File menu only delete the entry from the batch).

##  Day#

The Day# field on the PR Timecard Entry form.
 This field only displays if you selected the Post by Day Number option from the Options menu.
Enter the day number of the pay period; the form automatically calculates the date of the timecard. For example, if you are entering data for the 3rd day of the pay period, then enter the number 3.
The system-calculated timecard date updates the Last Timecard Post Date field in PR Employees, as long as the date is equal to or later than the currently specified Last Timecard Post Date.

##  Date

The Date field on the PR Timecard Entry form.
 This field only displays if you did not select the Post by Day Number option from the Options menu.
Enter the date for this timecard. You do not need to enter all 6 characters of the date. If only the day number is different from the default, enter just the day and the month and year will fill in.
The date entered in this field updates the Last Timecard Post Date field in PR Employees, as long as it is equal to or later than the currently specified Last Timecard Post Date.

##  Pay Seq#

 Enter the pay sequence number (as defined for the pay period in PR Pay Period Control) to identify the group of earnings that determines pay. This number also controls how some deductions and liabilities are calculated. Defaults to the first payment sequence set up for this Pay Period, or the previous value. Existing entries cannot be changed.

##  PR Dept

 Enter a valid PR department to determine which GL Accounts are updated with these earnings and liabilities. Initially defaults the employee's assigned department from PR Employees. If this timecard is posted to a job, the JC department (assigned to the job's contract) is also used.

## Crew

The Crew field in the PR Timecard Entry form.
If applicable, enter a valid crew. Initially defaults the employee’s crew as defined in PR Employees. If crew is overridden, successive lines default from previous line.
 Entry in this field updates the Crew field in PR Employees if the timecard date is equal to or later than the Last Timecard Post Date specified in PR Employees.
Note: For Job timecards, if you have elected to include Crew in JC Detail (option in PR Company Parameters, Job Cost tab), entry in this field interfaces to Job Cost.

##  JC Co#

The JC Co # field on the PR Timecard Entry form.
Job TimecardsRequired only if timecard is charged to a job.
 Specify which JC Co# (set up in JC Company Parameters) receives the labor and equipment costs. Initially defaults the JC Co# specified in PR Employees. If overridden, successive lines default from previous line. If no JC company is entered, the Job, Phase, and Equipment Usage inputs are disabled.
Mechanics TimecardsIf you want the mechanic's time to appear on a Job Certified Payroll report, even though it was not expensed to the job, enter the JC company. New entries default to the previous value.SM Work Order TimecardsFor job-related work orders only, this field displays the JC Co to which labor costs will be posted. Defaults the JC company defined for the SM company in SM Company Parameters; cannot be changed.
Note: Entry in this field updates the JC Co # field in PR Employees if the timecard date is equal to or later than the Last Timecard Post Date specified for the employee in PR Employees.

## Job

The Job field on the PR Timecard Entry form.
Job TimecardsEnter the job number to indicate which job should receive these labor and equipment costs. If the flag to Post by Job is unchecked (Options menu), new entries will default to the job specified in PR Employees. If Post by Job is checked, it will default to the prior entry and will be skipped although you may arrow back and change.
Mechanics TimecardsIf you want the mechanic's time to appear on a Job Certified Payroll report, even though it was not expensed to the job, enter the job. New entries default to the previous value.
Note: If the job is flagged as Certified (in JC Jobs), 'Certified Job' displays in red above the grid.
If you enter a soft- or hard-closed job, status displays in red in the informational section above tab pages. Timecard will only be saved if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).
SM Work Order TimecardsFor job-related work orders only, this field displays the job to which labor costs will be posted. Defaults from the work order and cannot be changed.
Note: Entry in this field updates the Job field in PR Employees if the timecard date is equal to or later than the Last Timecard Post Date specified for the employee in PR Employees.

##  Phase

Job Timecards
 Specify which phase of the job should receive the labor and equipment costs. This entry may only be skipped if the Allow Job Timecards Without a Phase flag option is checked in PR Company Parameters; if a phase is not specified, earnings on this timecard are not interfaced to JC). New entries default to the previous entry.
 If you use the F4 lookup feature at this
 field, and the job is set up for Locked Phases, you will only be shown phases on the job
 (as defined in JC Job Phases). If the job is not set up for Locked Phases, all phases (in
 JC Phases) are shown.
SM Work Order Timecards
For job-related work orders only, this field displays the phase to which labor costs will be posted. Defaults from the work order scope and cannot be changed.
Note: If the work order scope has not been assigned a phase,
 the phase will default as blank and you will be unable to save the record. Since this field
 is disabled for SM work order timecards, you cannot assign a phase here; however, you can
 assign a phase to the work order scope by pressing F5 from the SM Wo or
 SM
 Scope fields. Once you assign a phase to the scope, you will be able to save
 the timecard record.

## Ticket

The Ticket field on the PR Timecard Entry form.
If applicable, enter the Field Ticket associated with this timecard line or press F4 to select from a list of valid field tickets for the associated contract/job.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to job timecards is only useful if the job's contract/contract item has a bill type of T&M or Both.

For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Ins State

Enter a
 valid insurance state, or accept the default. This state, plus the insurance code in the
 Ins Code
 field, must be set up in PR State Insurance Codes.
This field defaults based on the job state (
 PR State
 field, JC Jobs), work order state ( PR State field, SM Work Orders), or the
 employee's insurance state ( Ins State field, PR Employees). The system
 determines the default depending on the settings for the Use Job or SM Work Order State for Insurance
 State box in PR Company Parameters and the Always use Employee's Work/Resident Insurance
 State box in PR Employees.
 The following table displays how this field defaults based on the settings for these two checkboxes.
Use Job or SM WO State
Use Employee State
Ins State Default

Defaults from the
 Ins State
 field in PR Employees

If you specify a job in the Job field
 (PR Timecard Entry), defaults from PR State field in JC Jobs.
If you do not specify a job in the
 Job
 field, defaults from the
 Ins State
 field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR State
 field in JC Jobs.
If a customer work order, defaults from the
 PR State
 field in SM Work Orders. If you do not specify a PR State on the work order, defaults from the
 Ins State
 field in PR Employees.

Defaults from the
 Ins State
 field in PR Employees.

Defaults from the
 Ins State
 field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Tax State

Enter the
 state for applying tax deduction and liabilities. This field defaults based on the job state (
 PR State
 field, JC Jobs), work order state ( PR State field, SM Work Orders), your
 company's office state ( Office State field, PR Company Parameters),
 or the employee's tax state (either the Resident Tax State or the Work Office Tax
 State fields, PR Employees). The system determines the default depending on the
 settings for the Use
 Job, SM Work Order or Office State for Tax State box in PR Company Parameters
 and the Always use
 Employee's Work/Resident Tax State box in PR Employees.
The following table displays how this field defaults based on the settings for the
 Use Job, SM Work Order or Office State for Tax State
 and
 Always use Employee's Work/Resident Tax State
 checkboxes.
Use Job, SM WO, or Office State
Use Employee State
Tax State Default

Defaults from the
 Work Office Tax State
 field in PR Employees. If blank, the system defaults from the
 Resident Tax State
 field.

If you specify a job in the Job field
 (PR Timecard Entry), defaults from the PR State field in JC Jobs. When
 processing payroll, the system checks for reciprocity with the state specified in
 the Work
 Office Tax State or the Resident Tax State fields in PR
 Employees.
If you do not specify a job in the
 Job
 field, defaults from the
 Office State
 field in PR Company Parameters. When processing payroll, the system checks for reciprocity with the state specified in the
 Work Office Tax State
 or the
 Resident Tax State
 fields in PR Employees.
If you do not specify a job in the
 Job
 field, and the
 Office State
 field in PR Company Parameters is blank, defaults from the
 Work Office Tax State
 field in PR Employees. If that field is blank, defaults from the
 Resident Tax State
 field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR State
 field in JC Jobs.
If a customer work order, defaults from the
 PR State
 field in SM Work Orders. If you do not specify a PR State on the work order, defaults from the
 Work Office Tax State
 field in PR Employees. If that field is blank, defaults from the
 Resident Tax State
 field in PR Employees.

Defaults from the
 Work Office Tax State
 field in PR Employees. If that field is blank, defaults from the
 Resident Tax State
 field in PR Employees.

Defaults from the
 Work Office Tax State
 field in PR Employees. If that field is blank, defaults from the
 Resident Tax State
 field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Local

Enter a
 valid local code (set up in [PR
 Local Codes ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-local-codes-form)) for applying local/city deductions and liabilities, or accept the
 default.
This field defaults based on either the job
 state ( PR
 State field, JC Jobs), the work order state ( PR State field, SM
 Work Orders), your company's office state ( Office Local field, PR Company Parameters),
 or the employee's tax state (either the Resident Local Code or the Work Office Local
 Code fields, PR Employees).
The system determines the default depending on the settings for the
 Use Job, SM Work Order or Office Local for Local Tax
 box in PR Company Parameters and the
 Always use Employee's Work/Resident Local Code
 box in PR Employees.
The following table displays how this field defaults based on the settings for the
 Use Job, SM Work Order or Office Local for Local Tax
 and
 Always use Employee's Work/Resident Local Code
 checkboxes.
Use Job, SM WO, or Office Local
Use Employee Local
Local Default

Defaults from the
 Work Office Local Code
 field in PR Employees. If blank, the system defaults from the
 Resident Local Code
 field.

If you specify a job in the Job field
 (PR Timecard Entry) and the PR Local Code
 field (JC Jobs) is not blank, defaults from the PR Local
 Code field in JC Jobs.
If you specify a job in the Job field, and the
 PR Local
 Code field (JC Jobs) is blank, the default value is the Resident Local Code field in the PR Employees form.
If you do not specify a job in the
 Job
 field, defaults from the
 Office Local
 field in the PR Company Parameters form, if it is not blank.
If you do not specify a job in the
 Job
 field, and the
 Office Local
 field in PR Company Parameters is blank, defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR Local Code field in the JC Jobs
 form, if it is not blank. If the job's PR Local Code field is
 blank, the default value is the Resident Local Code field in
 the PR Employees form.
If a customer work order, defaults from the
 PR Local Code
 field in SM Work Orders. If you do not specify a PR Local Code on the work order, defaults as blank.

Defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
 If both the
 Work Office Local Code
 and the
 Resident Local Code
 fields in PR Employees are blank, defaults as blank.

Defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
 If both the
 Work Office Local Code
 and the
 Resident Local Code
 fields in PR Employees are blank, defaults as blank.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Unemp State

Enter the
 state for applying unemployment deductions and liabilities.
This field defaults based on the job state
 (PR
 State field, JC Jobs), work order state (PR State field, SM Work Orders), or the
 employee's unemployment state (Unemp State field, PR Employees). The system
 determines the default depending on the settings for the Use Job or SM Work Order State for Unemployment
 State box in PR Company Parameters and the Always use Employee's Work/Resident Unemployment
 State box in PR Employees.
The following table displays how this field defaults based on the settings for the
 Use Job or SM Work Order State for Unemployment State
 and
 Always use Employee's Work/Resident Unemployment State
 checkboxes.
Use Job or SM WO State
Use Employee State
Ins State Default

Defaults from the
 Unemp State
 field in PR Employees.

If you specify a job in the Job field
 (PR Timecard Entry, defaults from PR State field in JC Jobs.
If you do not specify a job in the
 Job
 field, defaults from the
 Unemp State
 field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR State
 field in JC Jobs.
If a customer work order, defaults from the
 PR State
 field in SM Work Orders. If you do not specify a PR State on the work order, defaults from the
 Unemp State
 field in PR Employees.

Defaults from the
 Unemp State
 field in PR Employees.

Defaults from the
 Unemp State
 field in PR Employees.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Ins Code

Enter an existing insurance code to indicate which workers compensation deductions and liabilities apply. The insurance state/insurance code combination must exist in the PR State Insurance Codes form.
This field initially defaults based on the
 Insurance Based on Phase or SM Work Order Scope
 flag in PR Company Parameters and the
 Always use Employee's Work/Resident Insurance State
 checkbox in PR Employees.
 The following table displays how this field defaults based on the settings for these two checkboxes.
Insurance based on Phase/SMWO
Use Employee Insurance Code
Ins Code Default

Defaults from the
 Ins State
 field in PR Employees.

If you specify a job in the
 Job
 field (PR Timecard Entry), defaults from the
 Insurance Code
 field in JC Job Phases (if phase is an exact match). If no insurance code is specified for the phase in JC Job Phases, defaults from the
 Insurance Code
 field in JC Insurance Template. If no insurance code is specified for the phase in JC Insurance Template, or no insurance template is specified for the job, defaults from the
 Ins Code
 field in PR Employees.
If you do not specify a job in the
 Job
 field, defaults from the
 Ins Code
 field in PR Employees.
SM Work Orders:
If a job work order, defaults from the
 Insurance Code
 field in JC Job Phases. If no insurance code is specified in JC Job Phases, defaults from the
 Insurance Code
 field in JC Insurance Template. If no insurance code is specified for the phase in JC Insurance Template, or no insurance template is specified for the job, defaults from the
 Ins Code
 field in PR Employees.
If a customer work order, defaults from the
 Insurance Code
 field in SM Work Orders. If you do not specify an insurance code on the work order, defaults from the
 Ins State
 field in PR Employees.

Defaults from the
 Ins Code
 field in PR Employees.

Defaults from the
 Ins Code
 field in PR Employees.

Note: These defaults may be overridden if the Use Override Code When Pay Rate
 Exceeds Threshold Rate checkbox is selected in PR State Insurance Codes and the
 employee's combined pay rate and applicable add-on earnings are equal to or greater than the
 specified threshold rate. For more information, see [About Override Insurance Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-california-override-insurance-codes).
Important: If you need to manually override the insurance code on any line, you must first allow the
 Rate
 field value to set; then you can go back and enter the new insurance code. If you change the insurance code before the rate is set, rate threshold overrides can change your code selection.

##  GL Co#

 This field applies to Job timecards only.
 Enter the GL company to indicate which General Ledger should receive these payroll expenses. Must be a valid GL company, and the batch month must be open for its subledgers.
 If posting to a job, the GL company defaults from JC Company Parameters and cannot be changed.
 If not posting to a job, defaults the GL company specified for the employee in PR Employees.

##  EM Co

Enter the EM Company for this timecard line. Initially defaults the EM Co# specified in PR Company Parameters or the previous value. If blank, then Equipment may not be entered.
 Job Timecards
 This is the EM company that will receive the revenue for the use of its equipment.
The
 EM Co#
 and
 Equip
 fields display either before or after the
 Class
 field, depending on how you have set the Equipment Class Override option in PR Timecard Entry (Options menu). If the option is selected, both fields display before the
 Class
 field, and the Class defaults from the equipment’s category (i.e., employee’s pay rate is based on the type of equipment he was operating). If the option is not selected, both fields display after the
 Class
 field and are used only to record equipment usage.
 Mechanic Timecards
 This is the EM company that will receive the costs for this mechanic’s time. This entry is used to qualify the equipment, work order, component, and cost codes.
Service Timecards
For non-job work orders only.
This is the EM company that will receive the revenue for the use of its equipment.
The
 EM Co#
 and
 Equip
 fields display either before or after the
 Class
 field, depending on how you have set the Equipment Class Override option in PR Timecard Entry (Options menu). If the option is selected, both fields display before the
 Class
 field, and the Class defaults from the equipment’s category (i.e., employee’s pay rate is based on the type of equipment he was operating). If the option is not selected, both fields display after the
 Class
 field and are used only to record equipment usage.

##  Equip

Enter the equipment for this timecard or press
 F4
 to select from a list of valid equipment for the specified EM company. Equipment must be flagged as Active or Down.
 Job Timecards
This equipment will be credited with revenue for its use at a specified usage rate, and the job will be debited for the use of the equipment at the same rate.
The
 EM Co#
 and
 Equip
 fields display either before or after the
 Class
 field, depending on how you have set the Equipment Class Override option in PR Timecard Entry (Options menu). If the option is selected, both fields display before the
 Class
 field, and the Class defaults from the equipment’s category (i.e., employee’s pay rate is based on the type of equipment he was operating). If the option is not selected, both fields display after the
 Class
 field and are used only to record equipment usage.
 Mechanic Timecards
 This is the equipment to which labor costs will be posted. If you entered a work order for this timecard, this field defaults the equipment from the work order and cannot be changed.
Service Timecards
 This is the equipment used to perform the work for the specified work order and to which revenue will be posted. The cost for the use of the equipment cost will be posted to the work order.
The
 EM Co#
 and
 Equip
 fields display either before or after the
 Class
 field, depending on how you have set the Equipment Class Override option in PR Timecard Entry (Options menu). If the option is selected, both fields display before the
 Class
 field, and the Class defaults from the equipment’s category (i.e., employee’s pay rate is based on the type of equipment he was operating). If the option is not selected, both fields display after the
 Class
 field and are used only to record equipment usage.

##  WO

 This field applies to Mechanic timecards only.
 Specify which maintenance work order was being worked on. Entry in this field is optional, but if entered, the work order must have previously been set up. New entries default to the previous value.

##  WO Item

 This field applies to Mechanic timecards only.
 If you entered a work order in the previous field (WO), specify a valid open work order item for the work order.

##  Cost Code

 This field applies to Mechanic timecards only.
 Specify the cost code for this equipment that will receive the labor costs. If a work order and item have been entered, then a cost code must be used unless the Allow Cost Code Change option is checked on the Work Orders tab in EM Company Parameters. New entries not posted to work order items default to the previous value. The cost type is assigned in the EM Company Parameters form and cannot be overridden.

##  Comp Type

 This field applies to Mechanics timecards only.
 If you entered an equipment number, and you want to post costs at the component level, enter the component type. Entry in this field is optional, but if one is entered, the first component of this type defaults in the following field. If a work order and item are entered, then only the assigned component and component type are valid.

##  Component

 This field applies to Mechanics timecards only.
 If you entered an equipment number, and you want to post costs at the component level, enter the equipment component. Entry in this field is optional, but if one is entered, it must be an existing component set up for the equipment. If a work order and item have been entered, then only the assigned component is valid.

## SM Co

This field applies to technician timecards
 only (i.e. Type is S-SM Work Order).
Enter the SM Co for which the specified
 technician worked when completing the specified work order. Press F4 for a list
 of valid SM companies. Initially defaults the SM company defined for this PR company in PR
 Company Parameters (SM Co # field, Job Cost / Service Mgmt tab).
This field is disabled for existing records when the specified work order/scope is closed.

## SM WO

This field applies to technician timecards
 only (i.e. Type is S-SM Work Order).
Enter the SM work order that applies to this
 timecard line. Press F4 for a list of valid work orders.
Note: If posting to closed jobs in not allowed (i.e. the
 Allow Posting to
 Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs boxes
 are not selected in JC Company Parameters), you cannot specify a work order that is
 associated with a closed job.

## SM Scope Seq

This field applies to technician timecards
 only (i.e. Type is S-SM Work Order).
Enter the work order scope that applies to
 this timecard line. Press F4 for a list of valid scopes for the
 work order.

- If you select a scope that has been closed, a warning displays and you will be unable to save the record. You must either reopen the scope in SM Work Orders or select an open scope.

Note: If the scope is closed for an existing timecard, you will be able to process the timecard. If you elect to change the scope, you must enter an open scope.

- For job-related work orders:
Note:

- If the scope is not assigned a phase, a warning displays and you be unable to save the record. You can press F5 from this field to access SM Work Orders and assign a phase to the scope. Once you assign a phase to the scope, you can save the record.

- If the Costing Method is Markup
 and the scope does not have a rate template assigned, you will be able to
 post the timecard batch; however, you will be unable to run PR Ledger Update
 until you assign a rate template to the scope.

## SM Pay Type

This field applies to technician timecards
 only (i.e. Type is S-SM Work Order).
Enter the pay type that applies to this timecard line. The pay type determines the default earnings code for the technician, as well as the Cost Rate for the work completed labor line created (in SM Work Order, Work Completed grid) when this record is saved.
Note: Once the work order/scope specified for this entry is closed, you will be unable to change the pay type.

## SM Cost Type

This field applies to technician timecards
 only (i.e. Type is S-SM Work Order).
Enter the SM cost type that applies to this
 timecard line. Press F4 for a list of valid SM cost types.
Note: Once the work order/scope specified for this entry is closed, you will be unable to change the SM cost type.

## SM JC Cost Type

This field is only displayed if the line Type is S-SM
 Work Order and the selected SM work order is for a job.
Required.
Enter the JC cost type (from JC Cost Types) for the work performed. Initially defaults as follows:

- If you entered an SM cost type for the line, defaults the JC cost type assigned to the SM cost type (in SM Cost Types). Default may be overridden.

- If you did not enter an SM cost type or if you entered an SM cost type, but no JC cost type is assigned to the SM cost type, this field will default the JC Cost Type from the earnings code entered for this line.

The system will use this cost type, in conjunction with the phase specified for the work order sequence, to post the costs to Job Cost (via the JC Cost Detail table).
Note: If the work order scope specified for this invoice line has not been assigned a phase, you will receive a message indicating the phase is missing; you will be unable to save the record until you assign a phase to the work order scope in SM Work Orders.
Note: If no phase override exists in JC Departments (Phase
 Overrides tab) for the phase specified on the work order scope, the cost type entered here
 must be set up with the appropriate GL accounts in JC Departments (Cost Types tab) based on
 the following:

- If the phase exists on the job
 (locked and non-locked jobs), the cost type must be set up for the department
 assigned to the phase's contract item.

- If the phase does not exist for the
 job (non-locked jobs only), the cost type must be set up for the department
 assigned to the first contract item associated with the job.

- If the phase does not exist for the
 job (non-locked jobs only), but the phase matches the "number of valid characters"
 of a phase that does exist on the job, the cost type must exist for the contract
 item assigned to the valid job phase.

Note: If the cost type is not found in JC Departments, you
 will be allowed to post the timecard batch; however, you will need to set the cost type up
 in JC Departments before running PR Ledger Update. This applies regardless of how you set
 the JC
 interface checkbox in SM Company Parameters.
Locked Phases vs. Non-Locked Phases
If the Phases on this job are locked box is checked
 for the job in JC Jobs, the cost type specified here must be set up for the job/phase in JC
 Job Phases. If it is not, you will receive a warning and be unable to save the line until you
 specify a valid job/phase cost type.
Tip: You can add the cost type to the job phase by pressing
 F5
 from this field to access JC Job Phases. Once you set up the cost type and exit JC Job Phases, you can enter the cost type here.
If the Phases on this job are locked box is not
 checked in JC Jobs, you can use any cost type defined for the phase in JC Job Phases or JC
 Phases. If the cost type is not set up for the phase, you will receive a warning and be
 unable to save the line until you specify a valid phase cost type.

##  Craft

 Optional.
Enter a valid craft for this employee or press
 F4
 to select from a list of valid crafts.
The following table displays how this field defaults the craft.
Line Type
Uses Craft Template From
Reciprocal Agreement set to Override
Use Job Craft
Use Employee Craft

Job (with Job specified)
Job
Y
Y
N

N
N
Y

Job (no Job specified)
N/A
N/A
N/A
Y

Mechanic (with Job specified)
Job
Y
Y
N

N
N
Y

Mechanic (no Job specified)
N/A
N/A
N/A
Y

SM Work Order (Job WO)
Job
Y
Y
N

N
N
Y
N

SM Work Order (Customer WO)
Work Order
Y
Y
N

N
N
Y

Note: For SM-related timecards that originated from SM Work Orders, this field defaults the craft designated for the technician on the work completed labor line.
The craft is used in conjunction with the class and templates to determine pay rates, add-on earnings, and deductions and liabilities.

##  Class

 If you specified a craft for this employee (previous field), enter the craft
 classification. Must be an existing class set up for the craft in the PR Crafts form.
 Initially defaults the employee's standard class from PR Employees.
 If you selected the Equipment Class Override option (Options menu), and an equipment has been entered for this timecard line, this field defaults the PR Class specified for the equipment's category (in EM Categories). The combination of craft and class, if entered, determines the pay rate default.
If the craft template associated with the Job (job, mechanic, and SM job work order timecards) or SM Work Order (customer work order timecards) has a reciprocal agreement with a type of Override, the system will override the employee's standard craft with the Job Craft specified on the craft template (in PR Craft Template). If the employee's standard class or equipment class (if Equipment Class Override option is in use and an equipment was entered) does not exist for the Job Craft, you must either set up the class for the Job Craft in PR Craft Classes and in PR Craft Class Templates (for the job's craft template) or select a valid class already set up for the Job Craft.
Note: Service timecards (type S-SM Work Order) originating from Service Management will default the class specified for the labor line in SM Work Orders (Work Completed tab) or in SM Work Completed Labor.

## Earn Codes

Earnings codes define the type of earnings such
 as regular hourly, overtime, double time, salary, and so forth. Enter a valid earnings code
 (from PR Earnings Codes) to indicate the type of earnings to be posted and, in part, to
 determine pay rate, JC Cost Type, GL Expense Account, and the subject amounts of deduction
 and liability calculations. New entries default to the employee’s standard earnings code in
 the PR Employees form.

- If entering technician timecards (Type of S
 - SM Work Order), this field will initially default from PR Employees; however, once
 you enter the SM Pay Type, this field defaults the Earn Code defined for the pay type
 in SM Pay Types.

- When saving job and mechanic timecard lines, the
 cost type specified for the earnings code (in PR Earnings Codes) is validated against
 the cost types assigned to the line’s phase. If the job’s phases are locked, the
 earnings code’s cost type must be valid for the phase in JC Job Phases. If not using
 locked phases, the cost type must be valid for the phase in the JC Phases. If no
 valid match found, an error message displays and the line cannot be saved.

## Shift

Enter a shift, which determines (with the craft and class) the default pay rate. Initially defaults a shift as follows:

- If the employee is assigned to a crew and the crew is specified on the timecard, defaults the shift specified for the crew (in PR Crews).

- If no default shift is specified for the crew, or no crew is specified for the timecard, defaults the shift specified for the employee (in PR Employees).

- If no default shift is defined for the employee, defaults the shift from the previously entered timecard.

- If no default shift is defined for the employee, and it is the first timecard entry in the batch, defaults as '1'.

Note: If you initialized crew timecards and the crew does not have a shift defined, timecards default as shift '1', regardless of whether a default shift is defined for the employee in PR Employees.

## Rate

This field is displayed only if the Display Earnings Rates in
 PR Timecard Entry box is checked for your user login in VA User Profile and
 you have specified to show the Hourly Rate in the grid for the
 applicable timecard type in PR User Grid Options.
Enter the hourly rate of pay posted with these earnings. If the earnings code is rate based, then the rate defaults to the greater of the employee’s standard hourly rate in the PR Employees form or the rate assigned to the posted craft/class and shift, which may be overridden by the Job Craft Template. If the earnings code is amount based, then the amount defaults to the salary from PR Employees and the rate defaults to the amount divided by the standard hours for the pay period.
If the salaried employee worked other than the standard hours for the week and you want to calculate a different rate in order to distribute their earnings over the hours worked, then use the PR Salary Distribution form.
SM Work Order Timecards
For rate-based earnings codes, the rate defaults to the greater of the employee’s standard hourly rate in the PR Employees form or the rate assigned to the posted craft/class and shift, which may be overridden by the Craft Template assigned to the work order in SM Work Orders (customer work orders) or the Job Craft Template (job work orders). If the earnings code is amount based, then the amount defaults to the salary from PR Employees and the rate defaults to the amount divided by the standard hours for the pay period.
The rate specified here will only be used for payroll purposes; it will not be updated to the work completed labor line generated (during batch processing) for the work order. The system will use the rate specified for the technician (in SM Technicians) as the Cost Rate for the work completed line. Once you process the payroll and run PR Ledger Update, the system will update the amount paid to the employee as "actual cost" for the work completed labor line.

##  Hours

 Enter the number of hours the employee worked
 and will be paid for. If you entered time in the Start Time, Stop Time, and
 Break
 Hours fields, the system will automatically default a value in this field.
 For more information, see [Entering Start and Stop Time
 on Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-start-and-stop-time-on-timecards).

## Amount

This field is displayed only if the Display Earnings Rates in
 PR Timecard Entry box is checked for your user login in VA User Profile and
 you have specified to show the Amount in the grid for the applicable
 timecard type in PR User Grid Options.
Defaults the total calculated earnings amount for this time entry based on the Rate and Hours (add-on earnings are applied during Payroll processing and are not displayed here). If the method for the specified earnings code is Amount, new entries default to the employee’s standard salary amount (from PR Employees); may be overridden.
SM Work Order Timecards
The amount specified here will only be used for payroll purposes; it will not be updated to the work completed labor line generated (during batch processing) for the work order. The system will calculate the projected cost for the work completed line based on the hours specified for this timecard and the rate specified for the technician in SM Technician. Once you process the payroll and run PR Ledger Update, the system will update the amount paid to the employee as "actual cost" for the work completed labor line.

## Equip Phase

This field applies to Job timecards only.
Specify the posting phase for this line's equipment usage. Initially defaults the specified labor phase; may be overridden.
If attachments exist for the equipment to which you are posting usage, the override equipment phase and cost type is also updated for the attachment. In addition, if you override the equipment phase, the timecard audit list report (PR Timecard Entry Audit List) shows the equipment phase below the job phase line. However, if you do not override the equipment phase, it is excluded from the report, as it is the same as the job phase.

## Equip SM CT

For SM Work Order timecards only.
Enter the equipment cost type for this timecard. Cost type must be set up in SM Cost Types with an E-Equipment cost type category.

##  CT

 This field applies to Job timecards only
 Specify the posting JC cost type for this
 line's equipment usage. Initially defaults the JC cost type specified for the equipment in
 EM Equipment; may be overridden.

##  Revenue Code

For Job and Service timecards only.
If you entered an EM Company and equipment number for this timecard entry, enter the revenue code to which equipment usage will be posted. Initially defaults the revenue code assigned to the equipment (in EM Equipment). If no revenue code is assigned to the equipment, defaults as blank.
The revenue code entered here determines the rate of revenue generated for the specified equipment.

##  Usage

 This field applies to Job and Service timecards only.
 Enter the usage units (e.g., hours, days, weeks, etc.) to indicate the amount of time this equipment was used. The revenue code specified for the timecard line determines the Time UM that the usage units represent.
 This field defaults the hours posted to the timecard; however, depending on the Time UM specified for the revenue code, this may or may not accurately reflect the usage units. For example, if this field defaults as 40.00, but the Time UM for the revenue code is DAYS, this may not be an accurate representation of the actual usage units. Therefore, you would need to update the Usage units accordingly.

## Cert

The Cert checkbox on the PR Timecard Entry form.
This flag allows timecard level control of earnings included on Certified Payroll reports, and defaults to the setting specified for the employee in PR Employees (Include on Certified Reports box, Add'l Info tab). You may override this field.
Select this checkbox to include the employee's earnings indicated by this timecard entry when running Certified Reports.
 If this checkbox is not selected, these earnings are not included in the earnings break down in Certified Reports. However, all earnings will be included in weekly totals so that the report accurately reflects what an employee was paid.

##  Memo

 Use this field to enter a memo about this timecard entry. For additional space, double-click this field. A Notes window displays, allowing you virtually unlimited space for your notes and information; there is a maximum allowance of 8k.
 If you wish to add standard notes (set up in HQ Standard Note), make sure focus is in the field, then move to any gray area on the screen and right-click. From the displayed list, select the Add Std Note option; the Standard Note Copy window displays. Enter the note you wish to copy (use F4 for a list of standard notes) and click OK to add the note to this field.
