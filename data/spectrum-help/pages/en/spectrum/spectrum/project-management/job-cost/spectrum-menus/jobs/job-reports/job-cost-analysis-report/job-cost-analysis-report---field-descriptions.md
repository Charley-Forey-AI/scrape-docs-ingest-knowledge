---
title: "Job Cost Analysis Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-reports/job-cost-analysis-report/job-cost-analysis-report---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-reports/job-cost-analysis-report/job-cost-analysis-report---field-descriptions"
---

# Job Cost Analysis Report - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Selections

- Job

- Phase

- Cost type

- Division

- Superintendent

- Estimator

- Project manager

Enter the job number, phase number, Cost type, Division, superintendent, estimator, and project manager to include on this report. Press Enter to include ALL.
Entering a single job in the Job field activates the Billing option in the Period type section.

- Through period end date

- Fiscal year

- Period

Enter the period end date, or press Enter for the current Job Cost processing date.
Click the date calculator icon to add a calculation method to the report filter parameters.
The fiscal year and period display based on the period end date.

Use projected cost?
Select to include projected costs on the report. The default is controlled by
 the Show projected
 cost checkbox on the Job Cost
 Installation screen.

Include open commitments?
Select to include open commitments in JTD costs. The open commitment calculation will include use tax recorded on purchase orders and job requisitions.

Include A/P contract labor hours with Payroll
 hours?
This checkbox only applies to the Labor analysis (projected) format. The Summary and Detail formats do not display this data.

Include Payroll in progress?
If you use this feature and post payroll burdens to separate phases, verify that the burden phases are added to the phase detail file before any pre-time cards that use these phases are entered.
When this checkbox is selected, Spectrum computes the total payroll cost
 (including burdens) entered into Payroll > Pre-Time Card Entry and Time Card Entry but not yet
 calculated or posted. This cost is added to the actual cost of each job.
If the 'Post to Job Cost using standard labor rates' option is selected on the
 Payroll Installation screen, pre-time cards and
 unposted time cards charged to standard cost payroll departments will appear
 in Job Cost at their standard cost.
If the option to 'Include A/P invoices in progress?' is also selected, then unposted contract labor amounts will also be computed during the report compilation.
Note: This is only an estimate and does not reflect the actual
 computed costs. If the job uses actual burdens, the burden cost is estimated
 using the [Job Payroll Setup](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-payroll-setup) > Payroll burden section. In addition, if the payroll information is changed
 before the payroll is calculated, the actual costs that post to the job will
 be different from what is reflected on the previously viewed report.
 Estimated payroll costs are also included in the current week/month on this
 report.

Include A/P invoices in progress?
When you select this checkbox, Spectrum computes the total invoice amount including unposted and unapproved invoices. This amount is added to the actual cost of each job. If the invoice information is changed before the invoice is posted or updated, the actual costs that post to the job will be different from what is reflected on the report when it was previously viewed. The estimated invoice costs on this report are also included in the current week/month.

Combine sub-job activity into master job?
Select this checkbox to include transactions for sub-jobs if the job code specified above is a master job.

Display graphs?
Select to include graphs on the Job Cost Analysis report that show variance by group.

Group summary
Select from one of the following options:

- Phase summary

- Phase summary with subtotals

- Through minor group

- Through minor group with subtotals

- Major group only
The category-specific group description displays if a category has been designated in Jobs and the category-specific code is present.
The field default is set during [Installation Overview](/en/spectrum/spectrum/project-management/job-cost/installation-overview).
Major and minor group descriptions are set up in [Phase Category Maintenance](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/maintenance-overview/phase-category-maintenance).

Report format

Detail Job Cost Analysis
Summary Job Cost Analysis
Labor Analysis (projected)
Select one of the analysis report options to preview.
If you selected Include A/P contract labor hours with Payroll hours?above, then select Labor Analysis (projected) to view the associated data.

Job status

Active
Inactive
Complete
Select to view jobs with the status of Active, Inactive, and/or Complete.

Period type

Week-to-date
Month-to-date
Year-to-date
Billing
The default period type is defined in the Period type section in [Job Cost Installation - Report Defaults](/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---report-defaults).
Week-to-date Begin and End fields
Selecting the Week-to-date option activates the Week-to-date begin and Week-to-date end fields.
Enter the first and last dates you want to include on the report, or press Enter to accept the default of ALL. The 'Begin' field default date is 6 days less than the 'End' field default date.
Press F4 to select a
 different date or click the Date Calculator to
 automatically change the calculation method.
Billing
This option becomes available when you specify a single job in the Job field. An additional Billing information section displays.
This report and the [Job Cost History Report](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-reports/job-cost-history-report) show job cost history transactions that have been flagged for a specified billing period (customer and application #).
The selection feature on the starting screens of these two reports work in conjunction with the A/R Draw Request Cost Selection system. You can use the system to tie specific job cost history transactions with each draw request billing.

Billing information

Customer
These fields become available when you select Billing as the period type. Enter the Customer code.

Application #
Enter the application number for this draw request, or select from a list of valid application numbers and corresponding dates.

Include memo billings?
Select this checkbox to include memo billings on the report.

Phase status

Active
Inactive
Complete
Select the Phase status you want to display on the report.

Phase variance

All phases
Over variance only
Under variance only
Select an option to determine which phases to include on the report.
You can select an option for the variance based on over or under, and based on a percent or a specific dollar amount. This allows a project manager to see only those phases that are over or under budget, without viewing all the phases on a job.
Under variance is computed for less than or equal to the variance selected.
The Variance % and Variance amount fields below become available if you select either the Over variance only or Under variance option.

Variance %
Variance amount
Enter the variance percent and amount to include on the report.
This allows a project manager to view only jobs or phases that are over or under budget, instead of viewing all phases for the selected job(s).
