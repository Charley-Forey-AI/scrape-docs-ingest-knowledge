---
title: "Job Cost History Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-reports/job-cost-history-report/job-cost-history-report---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-reports/job-cost-history-report/job-cost-history-report---field-descriptions"
---

# Job Cost History Report - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields/ButtonsDescriptions
Buttons
Preview
Export
Select Preview to view the report.
Select Export to open the Export Report window and select the export format and other options.

My ReportsSelect to customize the Job Cost History Report.
DistributeSelect this button to create a zip file on your server, which will include a Crystal Reports format of the report and associated Document Imaging files.

- If there are errors (such as missing files), an error file will be included in the zip file.

- You will have the option of downloading the zip file or keeping it on the server. If you download the file, it will be removed from the server.

- Annotations will not display on a Distributed report.

- If you don't already have it installed, download and install the free SAP Crystal Reports Viewer.

Document Imaging Users: This report offers links (in blue) to associated images when previewed online. You will first need to unzip the file. You will not see the hyperlink if your DI security is at level 0.

Selections
Job
Phase
Cost type
Vendor
Employee
Equipment
Item
Choose which items to include in the report. The report will return all jobs that your selections were charged to for the given time frame
DivisionDivision field has a conditional window based on the Validate job division with G/L department checkbox on the Job Cost Installation screen. If the checkbox is selected, a window is available.
Note: The Validate job division with G/Ldepartment checkbox displays only if the Enterprise Installation > Use cost centers radio group is set to Yes in this company.

From date
To date
Enter the first and last transaction dates to be included on this report, or press Enter to begin with the first date on file, or end with the current job cost processing date.
For payroll transactions, this date will be the period end date if accruals are posted, and the check date if accruals are not posted. For all other transaction types, this will be the transaction date.

Include Purchase Order quantities received but not accrued?Select this checkbox to include quantities received.
To fully utilize this feature, the Purchase Order module must be installed and this company must be using the two-step receiving method. Quantity receipts recorded in Packing List Quantity Entry, but not yet invoiced, will be included on this report. This is typically used by companies doing Unit Price Jobs and those operations tracking quantity receipts as a separate P/O function.
Note: If the Update packing list to jobs before invoicing option is selected on the Purchase Order Installation screen, clear this checkbox to avoid counting the PO quantities received twice.

Include Payroll in progress?Select this checkbox if pre-time card and time card information from the Payroll module should be included.
If you use this feature and post Payroll burdens to separate phases, verify that the burden phases are added to the phase detail file before any pre-time cards are entered using these phases.
If the Use two digit day in time card entry checkbox in the Payroll Installation screen is not selected, then the pre-time card information will not appear on this report unless the from date is blank.
For those running multi-company payroll, if the checkbox is selected here, all pertinent pre-time card entries for the current job will be included from across companies. Confidential Payroll only shows the total dollars (with no name or hours displaying) on the Job Cost History Report and Job Cost History Inquiry screens. This total includes the pre-defined burden percentage from the [Job Payroll Setup](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-payroll-setup) > Payroll burden section.
When this checkbox is selected, Spectrum computes the total payroll cost (including burdens) that has been entered into Payroll > Pre-Time Card Entry but has not yet been calculated or posted. This cost is added to the actual cost of each job.
If the Post to Job Cost using standard labor rates option is selected on the Payroll Installation screen, pre-time cards and unposted time cards charged to standard cost payroll departments will appear in Job Cost at their standard cost.
Note: This is only an estimate and does not reflect the actual computed costs. If the job uses actual burdens, the burden cost is estimated using the Payroll burden section in [Job Payroll Setup](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-payroll-setup). In addition, if the payroll information is changed before the payroll is calculated and updated, the actual costs that post to the job will be different from what is reflected on the previously printed report. Estimated payroll costs are also included in the current week/month on this report.

Include A/P invoices in progress?Select this checkbox to include unapproved and unposted invoices from Vendor Invoice Entry on this report.
Include A/P contract labor hours with Payroll hours?Select this checkbox to include Accounts Payable contract labor hours with Payroll hours on this report.
Combine sub-job activity into master job?Select this checkbox to include transactions for sub-jobs if the job code specified above is a master job.
Billing period
CustomerEnter the customer to include on the report, or press F4 to select customers to include on the report.
The Job Cost History Report and the Job Cost Analysis Report provide an option to show those job cost history transactions that have been flagged for a specified billing period (customer and draw application #). The selection feature on the starting screens of this report works in conjunction with the A/R Draw Request Cost Selection system for use in tying specific job cost history transactions with each draw request billing.

Application #Enter the draw request application number that you want to include on the report, or press F4 to select application numbers to include on the report. This must be an application number for the specified customer and job.
Report format
Detail history with recaps
Detail history without recaps
Summary history
Summary history with drill-down
Select one of the Job Cost History report formats to preview and print. Note: If you choose Summary history with drill-down, you must also choose Export and view the Crystal Report. The drill-down is not available to Preview.

Detail history CSVExport as a CSV file for deeper analysis. Report headers appear only once, at the top of the CSV file.
Transaction typeChoose which transaction types to include in the report.
Job and Phase status
Active
Inactive
Complete
Records with an Active status are included by default, but you can use any combination of statuses to customize what appears in your report.
