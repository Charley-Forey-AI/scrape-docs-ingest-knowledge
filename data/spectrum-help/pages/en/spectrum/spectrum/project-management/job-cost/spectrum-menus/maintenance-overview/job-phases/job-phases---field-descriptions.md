---
title: "Job Phases - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/job-phases---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/job-phases---field-descriptions"
---

# Job Phases - Field Descriptions

Use the table below for reference when completing fields on this screen.
Columns/ButtonsDescriptions
NewDisplays if you have authorization to add or edit a phase. Select to open the [New Phase window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/new-phase-window) window.
SwitchSelect to choose a different job.
CopyThis button displays if you have authorization to add or edit a phase. Select to open the [Phase Copy](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/phase-copy) window.
PreferencesSelect to open the Operator Phase Display Preferences window and choose which columns you want to display in the grid.
Search
Go
Select Go to perform a search on your entry in in the Search field.
Begin Editing
Done Editing
If you have security authorization, you can select this button to edit the grid below.
Grid
PhaseEnter the phase code for the first phase of this job.
CtThe cost type entered here must have been previously defined in [Cost Type File Maintenance](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/cost-type-file-maintenance). Enter the code for a valid cost type, or select the arrow to select from a list of available cost types. This field is required.
Icons

- When editing, select the wrench icon to display the Edit Phase window.

- When viewing the screen, select the magnifying glass icon to display the View Phase window.

NotesSelect to display the Phase Summary Notes window. A blue notebook icon indicates that notes are present.
Phase descriptionEnter the description for the cost type in this required field.
Unit costThe estimated unit cost amount displays for each cost type in each phase. This and the following fields are optional.
This figure defaults based on entry in the Summary Totals window. The unit cost field tracks expected costs per unit on unit-priced phases of jobs. For example, one unit cost for a grading phase may be $12.50 per square yard (sy).

Original quantity Current quantityThe quantity for each cost type displays.
Original hours Current hoursEnter the estimated hours for this phase/cost type.
Original cost Current costDuring initial entry, enter the estimated cost for this phase/cost type in the Summary Totals window. The current estimated cost then defaults onto the main screen. Press Enter to accept the default estimated cost or specify a new cost.
The cost entered is printed on the job cost reports for comparisons with the estimated cost and actual cost.
Select the arrow to [Calculate Estimated Cost From Hours](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/calculate-estimated-cost-from-hours).

UmEnter the unit of measure associated with the "estimated qty" field. For example, if the phase is pouring 500 yards of concrete, "u/m" would be CY (cubic yards) and "estimated qty" would be 500. A lookup window is available for viewing units of measure.
The unit of measure entered here may have been previously defined in Accounts Receivable > Unit of Measure File Maintenance.

Billing item DescriptionEnter the billing item code and description.
Update projected quantities automatically?Select this checkbox if you want to use the projected contract quantities for a unit price job. This checkbox defaults to selected on new phases if the cost type is listed in Job Cost Installation > Quantity Reporting.
Once selected, this phase and cost type is linked to the corresponding billing item in the Accounts Receivable contract detail file. When the projected quantity update is performed, any flagged phases also update the corresponding projected quantity and the projected contract for the billing item in the Accounts Receivable contract detail file.

Alt phaseEnter the alternate phase to be used for the Job Comparison Report. This number may be the same or different than the number in the Phase field. Entry here does not need to fit the phase mask set for this specific job.
The system has been designed with flexible phase codes. For example, phase 10-100 on one job might be the equivalent of phase 5-10-100 on another job. This field is provided so that corresponding phases are used for the Job Comparison Report.

StateEnter the abbreviation for the work state or use the drop-down menu to select. Work state information in Time Card Entry defaults according to the following hierarchy:

- Job Phases

- Jobs

- Employees

CountyUse the drop-down menu to select the abbreviation for the work county.
LocalUse the drop-down menu to select the abbreviation for the local district.
Worker's compensation codeSelect the worker's comp code from the drop-down menu.
Payroll rate levelEnter the wage rate level number (1-9), if desired. This corresponds to the pay rate level found in the second screen of the Wage Code File Maintenance or Union File Maintenance screens. The system looks first to the wage code (when entered) for a pay rate and then to the union (when entered), and finally to the employee file (unless the Default pay rate field in the Payroll Installation screen is set to Employee pay rate or Higher of the two rates and the employee rate is higher). When adding records, the rate is determined by the wage/union code combined with the rate level. The rate level defaults from the phase file, the job file, or the employee file. To view the wage/union code default hierarchy, select [Wage/Union Code Hierarchy](/en/spectrum/spectrum/project-management/job-cost/in-depth-overview/wageunion-code-hierarchy).
If there is no wage code specified in the import file, but there is a union code, the system takes the wage code from the employee file and the union code from the import file. Additionally, if there is no wage code or union code specified in the import file, the wage code comes from the employee file and the union code from the job file.

CertifiedFrom the drop-down list, select the certified status. Options include: Yes, No, or No default. If the certified selection is set to Yes or No, this setting acts as the default for the Payroll time Card Entry screens. (Only the certified override in Payroll > Employee File Maintenance takes precedence over the selection made here in Job Cost.)
Wage codeThis column only displays if Payroll Installation is set to Wage codes.
Press F4 to open the Wage Code Phase Overrides window offered in the [New Phase window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job-phases/new-phase-window) window.

Price typeSelect the price method for this job from the list provided. Important: If a Time + Material or Cost Plus Phase is set up for a fixed bid or unit price job, it is necessary to add the job in the Time + Material module in Job Billing Maintenance. If the job is not set up there, no transactions is recorded in Time + Material files, regardless of setup here.

MarkupSelect this checkbox to set the markup flag for selected price type.Note: Markups for Time + Material and Cost Plus jobs is calculated in the Job Cost Transaction update.

Cost centerIf the phase has a different cost center than the job, enter a valid cost center or press Enter to accept the system default of blank. This field is typically left blank unless the phase is associated with a different cost center than the job. Note: This field displays only if the Enterprise Installation > Use cost centers option group is set to Yes or Pending in this company.

Est start Est endEnter the dates this phase is expected to begin and end. The start date, end date, and lead time are linked. The system calculates any one of these fields based upon entry of the other two.
DurationEnter the number of days this phase is expected to require for completion. The start date, ending date, and duration are linked. The system calculates any one of the three fields automatically based upon entry of the other two fields.
StatusIf Inactive is selected and then an attempt is made to assign a new transaction to this phase, a warning is given.
If Complete is selected, no further data entry is allowed.

CompleteEnter the expected date of the phase completion.
User-Defined fieldsThe user-defined fields display when you select them in the Operator Phase Display Preferences window. These fields may be set up in System Administration. Select the arrow to open the User-Defined Fields window.
CommentEnter any remarks about this phase, up to 250 characters.
Last revisedEnter the date the estimates were last revised. This field is for informational purposes only. It allows the user to maintain control over revisions to estimates.

Related information

- [Wage/Union Code Hierarchy](/en/spectrum/spectrum/project-management/job-cost/in-depth-overview/wageunion-code-hierarchy)
