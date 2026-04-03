---
title: "Job Summary Cost Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/job-summary-cost-report/job-summary-cost-report---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/job-summary-cost-report/job-summary-cost-report---field-descriptions"
---

# Job Summary Cost Report - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Selections

Job Phase Division
Enter the job number, phase, and Division to include on this report.

Superintendent Estimator Project manager
Enter the superintendent, job estimator, and project manager for this job.

Through period end date
Fiscal year
Period
Enter a date to end the report with, or press Enter to accept the current Job Cost processing date.
The corresponding fiscal year and period display based on the period end date.

Summary by job?
Select this checkbox to summarize the report with one line for every minor and major group, followed by the job total.

Include open commitments?
Select this checkbox to include open commitments in JTD costs. The open commitment calculation will include use tax recorded on purchase orders and job requisitions.

Include Payroll in progress?
If you use this feature and post Payroll burdens to separate phases, verify that the burden phases are added to the phase detail file before any pre-time cards are entered using these phases.
When this checkbox is selected, Spectrum computes the total payroll cost
 (including burdens) that has been entered into Payroll > Pre-Time Card Entry but has not yet been calculated or posted. This cost is added
 to the actual cost of each job.
Note: This is only an estimate and does not reflect the actual
 computed costs. If the job uses actual burdens, the burden cost is estimated
 using the [Job Payroll Setup](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-payroll-setup) > Payroll burden section. In addition, if the payroll information is changed
 before the payroll is calculated and updated, the actual costs that post to
 the job will be different from what is reflected on the previously printed
 report. Estimated payroll costs are also included in the current week/month
 on this report.

Include A/P invoices in progress?
Select this checkbox to include unapproved and unposted A/P invoices; otherwise, leave the checkbox clear.
When this checkbox is selected, Spectrum computes the total invoice amount.This amount is added to the actual cost of each job. If the invoice information is changed before the invoice is posted or updated, the actual costs that post to the job will be different from what is reflected on the report when it was previously printed. The estimated invoice costs are also included in the current week/month on this report.

Cost type format

Expanded report format? Labor cost type(s) Subcontract cost types Cost types for column #4 Cost type(s) for column #5
The Expanded format includes two additional cost types (Cost types for columns #4 and #5), which can be set up in [Job Cost Installation - Cost Types](/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---cost-types). You can edit the cost types once you set them up on the installation screen.
If you do not select this checkbox, the cost type format will be standard, without the additional cost types.

Report type

Use projected costs
Non-projected week-to-date
Non-projected month-to-date
Non-projected year-to-date
Select the option corresponding to the report type you want to preview. The
 default is based on Job Cost Installation prompts for
 period type and
 Show projected
 cost.

Week-to-date begin
Week-to-date end
Selecting the Non-projected week-to-date option above activates these fields.
Enter the first and last dates you want to include on the report, or press
 Enter to accept
 the default of ALL. The Begin field default date is 6 days less than the End field default date.
Press F4 to select a
 different date or click the Date Calculator to
 automatically change the calculation method.

Group summary

Phase summary
Phase summary with subtotals
Through minor group
Minor group with subtotals
Major group only
Totals by job
Select to preview the report with one of these options. Major and minor group descriptions are set up in Job Phases.
The category-specific group description will display if a category has been designated in Jobs and the category-specific code is present.
The 'Totals by job' version of the report explains the amount of costs remaining in the WIP Report.

Phase Variance

All phases
Over variance only
Under variance only
You can select an option for the variance based on over or under, and based on a percent or a specific dollar amount. This allows a project manager to see only those phases that are over or under budget, without viewing all phases on a job.
Under variance is computed for less than or equal to the variance selected.
The Variance % and
 Variance amount
 fields become available if you select either the Over or Under variance only
 option.

Variance % Variance amount
Enter the variance percent and amount to include on the report.

Job status

Active
Inactive
Complete
Select at least one Job status to include on the report.
