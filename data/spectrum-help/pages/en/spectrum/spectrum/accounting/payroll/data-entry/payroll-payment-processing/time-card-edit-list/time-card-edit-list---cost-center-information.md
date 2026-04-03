---
title: "Time Card Edit List - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-edit-list/time-card-edit-list---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-edit-list/time-card-edit-list---cost-center-information"
---

# Time Card Edit List - Cost Center Information

If cost centers are being used in this company, when
 running the Time Card Edit List, the starting screen includes a selection for a cost group
 labeled Cost group for employee.
When a cost group or cost center is specified, then the report will show only employees
 assigned to cost centers in that group (based on the cost center assigned to the time
 card line). The cost center assigned to each time card line is shown on the edit listing
 sorted by employee and sorted by job.
The cost center selection is available for all report formats except the Time card Edit List for Quantity. The listing includes only those employees you have permission to access, but all time cards for that employee will appear, even if you do not have permission to change certain lines. For example, disallowed jobs and phases will appear on the listing if your operator is authorized to access that employee.

## Time Card Edit Listing for Quantity

When an employee is included on the Time Card Edit Listing, the Time Card Edit Listing for Quantity will print based on your operator's security authorization for the job and phase specified on the time card line. Only authorized quantity time card lines will be shown on the listing. Spectrum verifies the job is permitted. The report will only include a job on the Quantity Edit Listing if the cost center assigned to that job is valid for your operator. The job override will be used to determine valid cost centers for your operator. Spectrum will also only include phases for that job if you have cost center security for the cost centers of the phase assigned to that line.
If your operator's scheme includes override settings for job entries in Cost Center Scheme Maintenance, the Time Card Edit List for Quantity will validate the cost center assigned to direct job cost quantity detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general, and if the cost center is not included, then the quantity entry line will not be allowed.
For quantity time cards assigned to jobs in other companies, cost center validation is performed based on settings in the destination company. When the Enterprise Installation option for cost centers is set to Yes in the destination company, then your operator cost center authorization will be performed in that other company. Spectrum verifies that the cost center is valid for the job, phase, and operator in that other company. When cost centers are NOT being used in the destination company, then you will be permitted to print all quantity entries.
