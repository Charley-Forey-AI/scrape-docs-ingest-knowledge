---
title: "Import Pre-Time Card - Cost Center information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/import-pre-time-card---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/import-pre-time-card---cost-center-information"
---

# Import Pre-Time Card - Cost Center information

When Enterprise Installation option for cost centers is set
 to Yes in this company, then when importing time cards for an employee, Spectrum will record
 the line in Pre-Time Card Entry only if you have permission to access that employee.
Spectrum compares the cost center assigned to the employee with cost
 centers in your operator's assigned cost center scheme, and if the cost center is not
 included, then the time card entries for the employee will be imported into Pre-Time Card
 Import Errors instead of Pre-Time Card Entry.
Cost center is an optional 10-character alphanumeric variable in the import file, positioned directly following the Crew code.

- For direct job cost time card lines, the cost center assigned to the job will override the cost center specified in the import file.

- For direct equipment cost time card lines, the cost center assigned to the piece of equipment will override the cost center specified in the import file.

- If a cost center is specified in the import file, that cost center will be assigned to the time card line.

- If no cost center is specified during the import, the employee's cost center will be assigned to the line.

During the import, Spectrum will validate the cost center associated with the time card line to assure that it is an active code, and that it is allowed for your operator. If not, the time card line will be imported to Pre-Time Card Import Errors instead of Pre-Time Card Entry.
When multi-company time cards are included in the import, Spectrum will determine whether the Enterprise Installation option for cost centers is set to Yes in the other company, and cost center validation will be performed based on settings in that company.
If your scheme includes override settings for employee entries in Cost Center Scheme Maintenance, this screen will validate the cost center assigned to the employee based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general.
During the import of Quantity records, Spectrum will record the line in Quantity Complete Entry only if you have permission to access that job. If your scheme includes override settings for job entries in Cost Center Scheme Maintenance, this screen validates the cost center assigned to the job based on these overrides.
Note: Regarding Deductions: In the case of deduction cost center
 assignment, even though this import will assign the cost center first from the import file
 and secondarily from the employee, the Payroll Update will reset the cost center of all
 deductions to the cost center assigned to that particular pay cycle. The cost center
 assigned by the import update is used for security purposes until the pre-time card line is
 ultimately updated.

Related information

- [File Layout Specifics](/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/file-layout-specifics)

- [Pre-Time Card Import Errors](/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/pre-time-card-import-errors)
