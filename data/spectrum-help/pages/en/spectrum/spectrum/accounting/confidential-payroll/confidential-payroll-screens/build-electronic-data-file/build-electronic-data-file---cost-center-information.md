---
title: "Build Electronic Data File - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/confidential-payroll/confidential-payroll-screens/build-electronic-data-file/build-electronic-data-file---cost-center-information"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/confidential-payroll/confidential-payroll-screens/build-electronic-data-file/build-electronic-data-file---cost-center-information"
---

# Build Electronic Data File - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen for this company, the starting screen includes a selection for a cost group. When a cost group or cost center is specified, then the report (or file) will include only employee activity assigned to that cost group/cost center.
When the operator specifies a cost center on the starting screen, Spectrum verifies that the operator has permission to access that cost center before proceeding.
Spectrum includes employee activity on the report (or in the file) only if the operator has permission to access the employee's information. For employees in the current company, Spectrum compares the cost center assigned to the employee with cost centers in the operator's assigned scheme; if the cost center is not included, then information for that employee is omitted.
For employees in other companies, cost center validation is performed based on settings in each included company. If the cost center feature is enabled in the Enterprise Installation screen for the non-confidential company, then the cost center assigned to the employee in the non-confidential company must be included in the list of valid cost centers for the operator's scheme in the non-confidential company. If the cost center feature is enabled in the Enterprise Installation screen in the non-confidential company, then all employees from that company display on the report.
