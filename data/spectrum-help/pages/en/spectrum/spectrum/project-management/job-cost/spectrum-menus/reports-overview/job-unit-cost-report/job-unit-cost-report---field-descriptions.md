---
title: "Job Unit Cost Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/job-unit-cost-report/job-unit-cost-report---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/job-unit-cost-report/job-unit-cost-report---field-descriptions"
---

# Job Unit Cost Report - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Selections

Job Phase Division
Enter the job number, Phase code, and Division (applicable if you are using job divisions) to include on the report.

Project manager Estimator
Enter the project manager and estimator of jobs to include on this report.

Labor cost type(s) Material cost type(s) Subcontract cost type(s) Equipment cost type(s)
Enter the Cost type codes corresponding to the labor, material, subcontract,
 and equipment cost types to include on this report. These cost types default
 from the Job Cost Installation screen. Up to five
 codes may be entered, or press Enter to accept the system default.

Through period end date
Enter the through date, or press Enter to accept the current Job Cost processing date, or
 press F4 to
 display the Search Calendar Dates window and select
 the date. The fiscal year and period display based on the period-end
 date.

Use projected cost?
Select to include projected costs on the report. The default is controlled by
 the Show projected
 costs field on the Job Cost
 Installation screen. To include projected costs on the
 report, the period type should be job-to-date.

Include group subtotals?
Select to include group subtotals on the report. The default is controlled by
 the Show group
 subtotals checkbox on the Job Cost
 Installation screen.

Include Purchase Order quantities received but not accrued?
Select to include quantities received.
This is typically used by companies doing Unit Price Jobs, and those operations tracking quantity receipts as a separate Purchase Order function. To fully utilize this feature, the Purchase Order module must be installed and this company must be using the Two-Step Receiving Method. Quantity receipts recorded in Packing List Quantity Entry, but not yet invoiced, will be included on this report.
Note: If the 'Update packing list to jobs before invoicing' option
 is selected on the Purchase Order Installation
 screen, deselect this checkbox to avoid counting the PO quantities received
 twice.

Include Payroll in progress?
Select to include pre-time card and time card information on the report, or leave the checkbox clear to preview only fully updated transactions.
If you use this feature and post Payroll burdens to separate phases, verify that the burden phases are added to the phase detail file before any pre-time cards are entered using these phases.
For companies running multi-company payroll, if pre-time cards are included, all pertinent pre-time card entries from all companies will be included on the report.
When this checkbox is selected, Spectrum computes the total payroll cost,
 including burdens, which has been entered into Payroll > Pre-Time Card Entry but has not yet been calculated or posted. This cost is added
 to the actual cost of each job.
Note
This is only an estimate and does not reflect the actual computed costs. If
 the job uses actual burdens, the burden cost is estimated using the [Job Payroll Setup](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-payroll-setup) > Payroll burden section. In addition, if the payroll information is changed
 before the payroll is calculated and updated, the actual costs that post to
 the job will be different from what is reflected on report when it was
 previously printed. The estimated payroll costs are also included in the
 current week/month on this report.

Include A/P invoices in progress?
Select this checkbox to include all unapproved and unposted vendor invoices
 on this report.

Quantity cost type(s)

Quantities tracked in multiple cost types? Quantity cost type Labor quantity cost type Material quantity cost type Subcontract quantity cost type Equipment quantity cost type Other quantity cost type
Select to track more than one Cost type.
The quantity cost type codes default from the Job Cost Installation > Cost Types tab and are user-defined. If this checkbox is selected, then
 the Quantity cost
 type field does not display.
Boxes display when multiple quantity cost types are used, and in this case the only report format that is available is the Expanded format.

Period type

Week-to-date
Month-to-date
Year-to-date
Select the option corresponding to the time period you want to preview this
 report. The default is based on the Period typeprompt in the
 Job Cost Installation screen. Valid selections for
 this field are Week-to-date, Month-to-date, and Year-to-date. If the
 report is run to include projected costs, the period type is always
 job-to-date.

Week-to-date begin
Week-to-date end
If the Week-to-date option is selected in the Period type radio group, enter the first date to include on the report or press Enter to accept the system default, which is 6 days less than the date that displays in the Week-to-date end field.
Click the date calculator icon to add a date calculator to the report filter parameters.

Report format

Standard
Expanded
Select to preview the report in standard or expanded format.
When multiple quantity cost types are being used, only the Expanded report format is available.

Job status

Active?
Inactive?
Complete?
Enter the Job status to display on the report.
