---
title: "New Phase window | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/new-phase-window"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/new-phase-window"
---

# New Phase window

Use this window to add phases to the job.
Fields/Buttons
Descriptions

Job
The job code and description display. This is view only unless you add a single new phase from the Search Phases window.

Phase
Enter the phase code for the first phase of this job.
Each job can have an unlimited number of phase breakdowns. The phase codes can be set to correspond to bidding categories or to the logical breakdown of cost centers. The CSI Standard phase codes are another possibility of a phase breakdown that can be used.
The phase code format is very flexible, allowing major and minor grouping for subtotaling on the Analysis and Productivity reports. The mask specified in Jobs controls the format for the phase code.
When a new phase is added, and the Set projected costs, quantity, and
 hours to current estimate when adding a phase checkbox is
 selected on Job Cost Installation, the projected
 costs and hours are set to equal the current estimated costs and hours.
In addition to setting projected cost and hours in this screen, when a new
 phase is added, the projected figures are also initialized during the Project Setup > Job Setup Update based on the installation option.

Cost type
The cost type entered here must have been previously defined in
 Cost Type File Maintenance. Enter the code for a
 valid cost type, or click the arrow to select from a list of available cost
 types. This field is required.

Cost center
If the phase has a different cost center than the job, enter a valid cost center or press Enter to accept the system default of blank. This field is typically left blank unless the phase is associated with a different cost center than the job.
Note: This field displays only if the Enterprise Installation
 Use cost centers option group is set to Yes or
 Pending in this company.

Status

Active
Inactive
Complete
Complete date
If you select Inactive or Complete, then an attempt is made to assign a new transaction to this phase

Properties

Unit of measure
Enter the unit of measure associated with the "estimated qty" field. For example, if the phase is pouring 500 yards of concrete, "u/m" would be CY (cubic yards) and "estimated qty" would be 500. A lookup window is available for viewing units of measure.
The unit of measure entered here may have been previously defined in Accounts Receivable > Unit of Measure File Maintenance.

Billing item
Enter the billing item code and description.

Update projected contract quantity?
Select this checkbox if you want to use the projected contract quantities for a unit price job. Once selected, this phase and cost type will be linked to the corresponding billing item in the Accounts Receivable contract detail file. When the projected quantity update is performed, any phases that are flagged will also update the corresponding projected quantity and the projected contract for the billing item in the Accounts Receivable contract detail file.

Alternate phase
Enter the alternate phase to be used for the Job Comparison Report. This number may be the same or different than the number in the Phase field. Entry here does not need to fit the phase mask set for this specific job.
The system has been designed with flexible phase codes. For example, phase 10-100 on one job might be the equivalent of phase 5-10-100 on another job. This field is provided so that corresponding phases are used for the Job Comparison Report.

Unit cost
The estimated unit cost amount will display for each cost type in each phase. This and the following fields are optional.
This figure defaults based on entry in the Summary Totals window. The unit cost field tracks expected costs per unit on unit-priced phases of jobs. For example, one unit cost for a grading phase may be $12.50 per square yard (sy).

Override price type

Use job default?

Price type
Select the price method for this job from the list provided: Fixed price, Time + Material, Cost plus, Unit price, or Job default.
Important:If a T+M or cost plus phase is set up for a fixed bid or unit price job, it is necessary to add the job in the Time + Material module in Job Billing Maintenance. If the job is not set up there, no transactions will be recorded in T+M files, regardless of setup here.

Markup?
Select this checkbox to set the markup flag for selected price type.
Note: Markups for Time + Material and Cost Plus jobs will be calculated in the Job Cost Transaction update.

Estimated dates

Start date
End date
Duration
Enter the dates this phase is expected to begin and end. The start date, end date, and lead time are linked. The system will calculate any one of these fields based upon entry of the other two.

Original estimate

Original quantity
The quantity for each cost type displays.

Original hours
Enter the estimated hours for this phase/cost type.

Original cost
During initial entry, enter the estimated cost for this phase/cost type in the Summary Totals window.

Current estimate

Current quantity
The quantity for each cost type displays.

Current hours
Enter the estimated hours for this phase/cost type.

Current cost
The current estimated cost will then default onto the main screen. Press Enter to accept the default estimated cost or specify a new cost.
The cost entered is printed on the job cost reports for comparisons with the estimated cost and actual cost.
Click the arrow to [Calculate Estimated Cost From Hours](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/calculate-estimated-cost-from-hours).

Override payroll setup

Work state
Enter the abbreviation for the work state or use the drop-down menu to select. Work state information in Time Card Entry defaults according to the following hierarchy:

- Job Phases

- Jobs

- Employees

Work county
Use the drop-down menu to select the abbreviation for the work county.

Work local
Use the drop-down menu to select the abbreviation for the local district.

Worker's compensation
Select the worker's comp code from the drop-down menu.

Rate level
Enter the wage rate level number (1-9), if desired. This corresponds to the
 pay rate level found in the second screen of the Wage Code File
 Maintenance or Union File Maintenance
 screens. The system looks first to the wage code (when entered) for a pay
 rate and then to the union (when entered), and finally to the employee file
 (unless the Default pay
 rate field in the Payroll Installation
 screen is set to Employee pay
 rate or Higher
 of the two rates and the employee rate is higher). When
 adding records, the rate is determined by the wage/union code combined with
 the rate level. The rate level defaults from the phase file, the job file,
 or the employee file.
In Change mode, if the phase is changed for a line to one that has an applicable wage/union code combination specified, the pay rate will be adjusted automatically using the same hierarchy used in Add mode.
If there is no wage code specified in the import file, but there is a union code, the system takes the wage code from the employee file and the union code from the import file. Additionally, if there is no wage code or union code specified in the import file, the wage code will come from the employee file and the union code from the job file.

Certified
From the drop-down list, select the certified status. Options include:
 Yes, No, or No default. If the
 certified selection is set to Yes or No, this setting will act as the default for the Payroll > Time Card Entry screens. (Only the certified override in Payroll > Employee File Maintenance will take precedence over the selection made here in Job
 Cost.)

Wage codes
This option only displays if Payroll Installation is
 set to 'Wage codes'.
Press F4 to open the Wage Code Phase
 Overrides window offered in the [New Phase window](#ID-00005dbe--en__ID-00005dbe) window.

Last revised
Enter the date the estimates were last revised. This field is for informational purposes only. It allows the user to maintain control over revisions to estimates.

Comment
Enter any remarks about this phase. You can enter up to 250 characters.

User-Defined
The user-defined fields display when you select them in the
 Operator Phase Display Preferences window. These
 fields may be set up in System Administration. Click
 the arrow to open the User-Defined Fields window.

Phase Notes
Click to enter a note in the [Phase Summary Notes](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/phase-summary-notes) window.

Related information

- [Wage/Union Code Hierarchy](/en/spectrum/spectrum/project-management/job-cost/in-depth-overview/wageunion-code-hierarchy)
