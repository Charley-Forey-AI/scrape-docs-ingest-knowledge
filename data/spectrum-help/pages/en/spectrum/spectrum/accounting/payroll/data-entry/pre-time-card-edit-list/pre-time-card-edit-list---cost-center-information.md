---
title: "Pre-Time Card Edit List - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/pre-time-card-edit-list/pre-time-card-edit-list---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/pre-time-card-edit-list/pre-time-card-edit-list---cost-center-information"
---

# Pre-Time Card Edit List - Cost Center Information

If cost centers are being used in this company, Spectrum
 includes the employee on the listing only if you have permission to access the employee.
Spectrum compares the cost center assigned to the employee with cost centers in your
 operator's assigned cost center scheme, and if the cost center is not included, then
 that employee is not shown on the listing.
The cost center assigned to each time card line is shown on the edit listing sorted by employee and by job.
When an employee is included on the Pre-Time Card Edit List, all time cards for that employee display, even if you do not have permission to change certain lines. For example, disallowed jobs and phases will appear on the listing if your operator is authorized to access that employee.
The Pre-Time Card Edit Listing for Quantity will print based on your operator's security authorization for the job and phase specified on the time card line. Only authorized quantity time card lines display on the listing. Spectrum verifies the job is permitted. The report will not include a job on the Quantity Edit Listing unless the cost center assigned to that job is valid for your operator.
If your operator's scheme includes override settings for job entries in Cost Center Scheme Maintenance, the Pre-Time Card Edit List for Quantity will validate the cost center assigned to direct job cost quantity detail line based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general.
For quantity time cards assigned to jobs in other companies, cost center validation is performed based on settings in the destination company:

- When Enterprise Installation option for cost centers is set to Yes in the destination company, then the operator cost center authorization will be performed in that other company. Spectrum verifies that the cost center is valid for the job, phase and operator in that other company.

- When Enterprise Installation option for cost centers is set to No in the destination company, then the operator will be permitted to print all quantity entries.
