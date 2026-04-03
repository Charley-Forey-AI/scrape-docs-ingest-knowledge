---
title: "Contract Status Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/contract-status-report/contract-status-report---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/contract-status-report/contract-status-report---field-descriptions"
---

# Contract Status Report - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Report format

Choose one of the following format options:

> JTD contract status with YTD
The date must be in the last fiscal period of the year in order for the Link to option to create earned revenue entries checkbox to be available.

JTD contract status with MTD
The Link to option to create earned revenue entries checkbox becomes available.

JTD contract status

WIP schedule with backlog

Revenue and profit forecast
When selecting this format, the job must have an estimated complete date in order to display on the report.

Selections

Job
Division
Project manager
Contract type
Enter the job number, job division, project manager, and type of contract to include on this report.

Price type
Enter a price type:

- Fixed Price

- Time + Materials

- Cost Plus

- Unit Price

Through period end date
Fiscal year
Period
Enter a date to end the report with, or press Enter to accept the current Job Cost processing date.
The fiscal year and period display based on the period end date.

Cost group
This field displays if your company is using cost centers.
When you specify a cost group or cost center, the report only shows jobs
 assigned to cost centers in that group (based on the cost center recorded in
 the Jobs > Edit window). Spectrum verifies that you have permission to access
 that cost center before proceeding.
On the Contract Status Report preview, Spectrum includes a job only if you have security access. Spectrum compares the cost center assigned to the job with cost centers in your assigned scheme; if the cost center is not included, the job does not display.
The report includes activity for all phases of authorized jobs.

Link to option to create earned revenue entries?
Access to this option depends on a number of factors.
Spectrum observes the following hierarchy:

1. Your operator must have security access to this report, and must be able to enter transactions manually in [Earned Revenue](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/earned-revenue).

1. Your operator must have security authorization to field-level security for
 this checkbox. This setting is found in the Function Security Maintenance > Function Links Security window.

1. The Report format must be set to either the JTD contract status with YTD or JTD contract status with MTD option.

1. If the Report format is set to JTD contract status with YTD, then the date must be in the last fiscal period of the year.
Select to capture the earned revenue calculated by this report and automatically construct the necessary transactions in Earned Revenue Entry. After the unposted transactions are created, you can edit earned revenue figures as necessary, or accept the software-generated amounts and update at once.
If you select this checkbox and the Cannot Create Earned Revenue
 Entries window displays, run the Contract Status Report
 for a full year or select a Contract Status Report format that shows
 month-to-date earned revenue amounts.
If an applicable format of the report has been previewed, the Create
 Earned Revenue Entries window displays.

Include Payroll in progress?
Select to include pre-time card entry information from the Payroll module.
If you select this box and post Payroll burdens to separate phases, verify that the burden phases are added to the phase detail file before any pre-time cards are entered.
By selecting this box, Spectrum computes the total payroll cost (including
 burdens) entered into Payroll > Pre-Time Card Entry but not yet calculated or posted. This cost is added to the
 actual cost of each job.
Note: This is only an estimate and does not reflect the actual
 computed costs. If the job uses actual burdens, the burden cost is estimated
 using the [Job Payroll Setup](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-payroll-setup) > Payroll burden section. In addition, if payroll information is changed
 before the payroll is calculated and updated, the actual costs that post to
 the job will be different from what is reflected on the previously previewed
 report. Estimated payroll costs are also included in the current week/month
 on this report.

Include A/P invoices in progress?
By selecting this checkbox, Spectrum computes the total invoice amount including unposted and unapproved vendor invoices. This amount is added to the actual cost of each job.
If the invoice information is changed before the invoice is posted or updated, the actual costs that post to the job will be different from what is reflected on the report when it was previewed before. The estimated invoice costs are also included in the current week/month on this report.

Combine sub-job activity into master job?
Select to preview the report grouped by job master; otherwise the report displays by job number.
If the Exclude jobs after period-end date checkbox is also selected, Spectrum determines whether to include or exclude based on date. Spectrum evaluates the create date of the job. If the master job is included, all of its component jobs will also be included regardless of their create dates.

Use projected contract for unit price jobs?
Select to use the projected (instead of revised) contract amount for unit price jobs on the report. The original contract amount rarely reflects the true quantities used. Therefore, the projected contract amount is the more accurate contract amount billed for the job.
The projected contract amount is not date-sensitive. It equals the projected quantity times the billing rate per unit as defined in Contracts.

Show non-active jobs in summary?
Select to include non-active jobs in summary format instead of detail format .

Use projected cost?
 Select to view projected costs on this report. The default is controlled by the Show projected costs checkbox on the [Job Cost Installation - Report Defaults](/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---report-defaults) screen.

Exclude jobs created after period-end date?
Select this checkbox to exclude any jobs created after the period-end date from the report. Spectrum will compare the period-end date (from the fiscal calendar) of the date specified on the starting screen with the 'create date' of each job selected for the report. If the 'create date' is later than the fiscal period-end date, the job will be excluded. If the dates are the same, the job will be included on the report.
When the Print job master summary checkbox is also selected, Spectrum determines whether to include or exclude based on date. Spectrum evaluates the create date of the master job. If the master job is included, all of its component jobs will also be included regardless of their create dates.

Job status

Active?
Inactive?
Complete?
Select at least one Job status to display on the report.
This report determines a job's status on a date-sensitive basis. This means
 that in addition to analyzing the [Job Dates](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-dates) window
 to determine the contract's actual date of completion, Spectrum also
 analyzes the report period-end date to determine if a job should be reported
 as Active or
 Inactive for
 the selected period. When the actual date of completion in the
 Dates window is earlier or equal to the period-end
 date entered on this screen, the selected job will be tallied among the
 other Completed
 jobs.
By selecting Active,
 the report also includes jobs marked Complete that have an
 actual completion date later than this report's period-end date.
