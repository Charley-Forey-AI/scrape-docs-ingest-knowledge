---
title: "Job Payroll Setup | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-payroll-setup"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-payroll-setup"
---

# Job Payroll Setup

Use this screen to enter additional properties pertaining to the job.
FieldsDescriptions
Defaults
Worker's compensationEnter a project-specific Worker's compensation code when all employees working on this project use the same code.In general, a variety of worker's compensation codes will be used on a single
 job; however, if a code is specified for the job, the code entered here must
 first be set up in Payroll > Worker's Compensation Code Maintenance. In the Payroll module, workers compensation codes are
 entered in individual employee files based on the type of work typically
 performed by the employee. During Time Card Entry, this code is provided as
 the default worker's compensation code. Occasionally, all employees working
 on a job may have a specific worker's compensation code, rather than
 their usual code.
Example: Everyone works on a waste water treatment plant. In this case, that code may be entered in this field of the job file.This code can be used as the default during Time Card Entry, overriding the code from the employee's file. (See the hierarchy in the worker's compensation definition above.)

Work stateEnter the work state tax code for this job; up to 10 characters are allowed.
Work countyEnter the work county tax code for default in Time Card Entry. This entry may not be the same as the work state code specified.
Work localEnter the local tax code for default in Time Card Entry. This entry may not be the same as the work state or work county code specified.
Rate levelThis field is used to set the pay rate level to be used in conjunction with
 the Wage Codes / Union or Pay Group features. Add or edit the wage rate
 level number (1-9). This corresponds to the pay rate level found in the Payroll > Wage Code File Maintenance - Properties tab or Union File Maintenance - Rates tab.Hierarchy:
The system first looks to the wage code for a pay rate, then to the union, and
 finally to the employee file (unless the Payroll Installation > Defaults tab's Default pay rate section is set
 to Employee pay
 rate or Higher
 of the two rates, and the employee rate is higher).
The rate is determined by the wage/union code combined with the rate level. The rate level defaults from the phase file, job file, or employee file. For more information, view the [Wage/Union Code Hierarchy](/en/spectrum/spectrum/project-management/job-cost/in-depth-overview/wageunion-code-hierarchy).
If the phase is changed for a line to one that has an applicable wage/union code combination specified, the pay rate will be adjusted automatically.

- If no wage code is specified, but there is a union code, the system takes the wage code from the employee file.

- If no wage code or union code is specified, the wage code comes from the employee file and the union code from the job file.

Pay groupThis field displays if the Pay
 group option is selected on the Payroll
 Installation screen. Select this option to copy the pay group
 information.
Certified payroll?Select this checkbox if you need certified payroll reports. To select the correct week number on the report, select this checkbox at the start of the job and select how the Payroll No. (week number) on the Certified Payroll Report should be computed for the particular job:

- From first time card date

- Work weeks only

- Calendar year (starting 01/01)

Spectrum uses this information to ensure that Time Card
 Entry is performed in the correct format so that the
 Certified Payroll Report can be printed. The certification flag in Payroll > Time Card Entry defaults based on this field unless a phase override is
 specified. This field can be overridden for individual phases in [Job Phases](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-phases).
Davis-Bacon job?
Prevailing wage job?
The Davis-Bacon job and Prevailing wage job checkboxes are designed to work specifically with Payroll deductions and add-ons.

- Select the Davis-Bacon job checkbox if the job is a federal (Davis-Bacon) job.

- Select the Prevailing wage job checkbox if the job is a State, County, or Local (prevailing wage) job.

You cannot select both checkboxes. If neither checkbox is selected, this indicates a private job.
If you select the Davis-Bacon
 job checkbox, hours and earnings from this job will be
 included in the calculation of a deduction (or add-on) that also has the
 Davis-Bacon
 jobcheckbox selected on the Payroll > Deduction / Add-on Code Maintenance > Properties tab.
If the you select the Prevailing
 wage job checkbox, hours and earnings from this job will be
 included in the calculation of a deduction (or add-on) that also has the
 Prevailing wage
 job checkbox selected on the Payroll > Deduction / Add-on Code Maintenance > Properties tab. Select the Regular wages include non-stated fringe? checkbox to track
 prevailing wage jobs with non-stated fringe. When this checkbox is
 selected, jobs created in the Add New Job window will conditionally copy
 this setting.

Certified project IDIf you are using Certified Payroll XML Electronic reporting, record the certified project ID number here. This information will be included on the XML file when using either the eCPR or AASHTOWare format.
Payroll burden
Payroll Burden assesses taxes, worker's compensation, union fringes, and so forth.During installation, this window will automatically open, allowing you to define burden information for this job.

Post actual burden to job?Actual Payroll Burden is defined as employer paid taxes, workers comp, and union fringes. Select to post actual payroll burdens to this job.
Pre-time card % Payroll %If you selected the checkbox above, then the Pre-time card % field displays. Enter the percent burden to add to Pre-time Card Labor that you want to include in Job Cost reports.If you did not select the checkbox above, the Payroll %  field displays, which is the percent burden figured on labor during a Payroll cycle.

PhaseThis phase code is used when the software posts a payroll burden to this job. If you enter a phase code, the burden amounts will post to this phase exclusively.If you leave this field blank, the burden posts to the same phase as the earnings specified in Time Card Entry.

Cost typeThe software prompts you for the cost type you want to use when it posts the payroll burden to Job Cost. If you enter a cost type, then the burden amounts will post to this cost type instead of the labor cost type specified in Time Card Entry.If you leave this field blank, the burden will post to the same cost type as the earnings specified in Time Card Entry.

Payroll overhead
Use payroll overhead to charge each job with an estimated administrative cost.
Example: For an overhead of 10%, if labor hours are $100 and burden is $27, then overhead is 10% of $127, or $12.70.
The information you enter here designates how payroll and job overhead data for this job is handled, and how that data is tracked in job costing. Settings in this section window default from the Job Cost Installation - Payroll tab.
When a job has overhead costs associated with Payroll, the credit side of the percent overhead posts to the same General Ledger period, even when the period end date is in a different month from the Payroll check date and the Accrue expense to field on the Payroll Installation – Properties tab is set to Work date or Period End date.
The payroll overhead feature is used for adding additional overhead to your jobs (for example, small tools expense) over and above your normal payroll burdens.

Overhead typeSelect one of the following overhead types:Percent:
Specify an additional payroll burden added to this job based on the percentage method. This would add an additional percentage amount calculated on the total burdened payroll dollars. The Percent field displays.
Amount/Hour:
Calculate the payroll overhead as an amount per hour.
Some contractors like to use hours as their basis for allocation because it is more constant and doesn't fluctuate like payroll dollars. The Rate field displays.
None:
Select to calculate the payroll without overhead.

PercentThis field is available if you selected Percent in Overhead type. Enter the payroll overhead percentage as follows:Example: 5% would be entered as 5.00 (the software converts it to a percentage for calculation).

RateThis field is available if you selected Amount / hour in Overhead type. Enter the payroll overhead amount per hour. This rate is entered as a rate per hour (for example, $1.50 per hour) and is calculated based on total payroll hours not adjusted for overtime (one overtime hour is counted as 1 overhead hour, not 1.5 hours).

PhaseEnter the phase code for the overhead amount. This phase will be used when the software posts Payroll overhead to Job Cost. The overhead amounts will post to this phase exclusively.If you leave this field clear, the software will post overhead to the same phase as the earnings specified in Time Card Entry.

Cost typeEnter the Cost type for the overhead amount. This cost type will be used when the software posts Payroll overhead to Job CostIf you leave this field blank, the Payroll Update will post overhead to the same cost type as the earnings specified in Time Card Entry.

Note:About Non-cash Add-onsPayroll Burden does not include any Non-Cash Add-ons appearing on the Properties tab of union setup. Non-Cash Add-ons burden costs are always attributed to the Labor Phase Code, regardless of the values in the Phase and Cost Type fields.

Auto-Overtime Rules buttonUse this button to open the Auto-Overtime Rules window and define the rules needed for a particular job. Fields include:

- Auto-overtime for this job? Select this checkbox if you wish to define job-specific overtime rules. When these rules are implemented, they will override Federal and State overtime rules.

- Daily overtime starts after: Specify the number of hours (per day) after which point overtime will be calculated.

- Weekly overtime starts after: Specify the number of hours (per week) after which point overtime will be calculated.

- Saturdays/Sundays: Use the available drop-down lists to select how to apply the Daily and Weekly thresholds. Options include setting the rules to the same rules used by weekdays, setting all Saturday and Sunday hours to overtime, or setting all Saturday and Sunday hours to double-time.

Wage code grid
This grid displays if you selected Wage codes in the Defaults tab of Payroll Installation. You can add or edit wage codes to a job.By entering information in this section, you determine the wage/union code
 default, which determines the employee pay rate in Payroll > Time Card Entry.
In the [Payroll Installation - Defaults](/en/spectrum/spectrum/accounting/confidential-payroll/installation-overview/payroll-installation---defaults)
 tab, if the Default pay
 rate section is set to Employee pay rate or
 Higher of the two
 rates(and the employee rate is higher), the rate field will
 default from the employee file.
If the Default rate table option group is set to Pay groups, then this grid will not display. The Pay group field in the Defaults section displays instead.
Note: Column width or sorting changes will not be saved.

Wage code UnionEnter Wage and Union codes. Up to 10 characters are allowed.
Wage description Union name CraftThese are display-only, and come from [Wage Code File Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/wage-code-file-maintenance).

Related information

- [Job % Payroll Burden vs. Actual Payroll Burden in General Ledger](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/job--payroll-burden-vs.-actual-payroll-burden-in-general-ledger)
