---
title: "Job Productivity Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/job-productivity-report/job-productivity-report---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/job-productivity-report/job-productivity-report---field-descriptions"
---

# Job Productivity Report - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Selections

Job Phase Cost type
Enter the job number, Phase code, and Cost type to include on this report.

Division
Enter the Division to which jobs on this report should belong.

Superintendent Estimator Project manager
Enter the names of the superintendent, estimator, and project manager for this job.

- Through period end date

- Fiscal year

- Period

Enter a date to end the report with, or press Enter to accept the current Job Cost processing date.
The fiscal year and period display based on the period end date.

Use projected cost?
Select to view projected costs on this report.
The default is controlled by the Show projected costs checkbox on the [Job Cost Installation - Report Defaults](/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---report-defaults) screen.

Include group subtotals?
Select to include group subtotals on the report preview.
The default is controlled by the Show group subtotals checkbox on the [Job Cost Installation - Report Defaults](/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---report-defaults) screen.

Include Purchase Order quantities received but not accrued?
Select to include quantities received.
To use this feature to its fullest extent, the Purchase Order module must be installed and this company must be using the Two-Step Receiving method. Quantity receipts recorded in Packing List Quantity Entry, but not yet invoiced, will be included in this report. This will typically be used by companies doing Unit Price Jobs and those operations tracking quantity receipts as a separate Purchase Order function.
Note: If the 'Update packing list to jobs before invoicing' option
 is selected on the Purchase Order Installation
 screen, deselect this checkbox to avoid counting the PO quantities received
 twice.

Include Payroll in progress?
Select the checkbox to include pre-time card and time card information on the report, or leave this checkbox clear to print only fully-updated transactions.
For those running multi-company payroll, if the checkbox is selected here, all pertinent pre-time card entries for the current job will be included.
If you use this feature and if you post Payroll burdens to separate phases, verify that the burden phases are added to the phase detail file before any pre-time cards are entered using these phases.
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
Select this checkbox to include all unapproved and unposted vendor invoices on this report.

Include A/P contract labor hours with Payroll hours?
Select if you want this report to include Accounts Payable contract labor hours with Payroll hours.

Period type

- Week-to-date

- Month-to-date

- Year-to-date

The default period type is defined in the Period type section in [Job Cost Installation - Report Defaults](/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---report-defaults).

Week to date begin Week-to-date end
Selecting the Week-to-date option above activates the Week-to-date begin and Week-to-date end fields.
Enter the first and last dates you want to include on the report, or press Enter to accept the default of ALL. The 'Begin' field default date is 6 days less than the 'End' field default date.
Press F4 to select a
 different date or click the Date Calculator to
 automatically change the calculation method.

Job status

Active?
Inactive?
Complete?
Select at least one Job status to include on the report.

Calculation method

- Hours per quantity

- Quantity per hour

For example, if 2000 pounds of gravel were used in 500 hours, the report will show four if Quantity per hour is selected or .25 if Hours per quantity is selected.
You can set up the default in [Job Cost Installation - Report Defaults](/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---report-defaults) > Productivity Report ratio section.

Phase status

Active?
Inactive?
Complete?
Select at least one Phase status to include on the report.
