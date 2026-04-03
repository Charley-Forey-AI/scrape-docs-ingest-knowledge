---
title: "Pre-Time Card Entry Window - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/pre-time-card-entry-window/pre-time-card-entry-window---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/pre-time-card-entry-window/pre-time-card-entry-window---cost-center-information"
---

# Pre-Time Card Entry Window - Cost Center Information

In the Pre-Time Card Entry window, Spectrum allows entry of a payroll department code only if the cost center assigned to the time card line is valid for that department. If the cost center is NOT set up for that department:

- For a non-direct cost department, the cost center is shown as invalid and you must change either the department code or cost center to continue.

- For a job cost department, the phase is shown as invalid, you must correct the phase, job, or department to continue.

- For an equipment cost department, the equipment cost category is shown as invalid and you must change the cost category, equipment code, or the department.
If the Operator changes the 'Work order' in this screen, the software will automatically adjust the cost center assigned to the time card line based on the cost center in the Work Order Header Table. Security authorization for the new work order and cost center will be re-evaluated, and entry of the new work order will be disallowed if the Operator does not have permission to the new cost center.
The following table shows how the Pre-Time Card Entry window handles different entry types when cost centers are being used and you are adding, editing, or deleting entries.
Entry type
Cost center validation
If overrides are used...

Direct Job Cost
Spectrum verifies the job and phase code of a time card line are permitted. Spectrum first verifies that you have permission for cost center specified in the phase file, if any. If the cost center is not specified in the phase file, the cost center assigned to the job will be assigned, provided the operator has permission for that cost center. Spectrum also verifies that the cost center assigned to the line based on the job or phase is valid for the G/L account code associated with the department specified on that line.
If your assigned cost center scheme includes override settings for job entries in Cost Center Scheme Maintenance, this screen validates the cost center assigned to direct job cost time card lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general.

Direct Equipment Cost
Spectrum verifies that the equipment and cost category code of a time card line are permitted. Spectrum first verifies that you have permission for the cost center specified in the cost category file, if any. If the cost center is not specified in the cost category file, the cost center assigned to the equipment will be assigned, provided you have permission for that cost center. Spectrum also ensures that the cost center assigned to the line based on the equipment or cost category is valid for the G/L account code associated with the department specified on that line. Entry of that equipment code will not be permitted if the cost centers in both the equipment and cost category files are disallowed.
If you assigned cost center scheme includes override settings for equipment entries in Cost Center Scheme Maintenance, this screen will validate the cost center assigned to direct equipment cost time card lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general.

Non-Direct Cost
If your assigned cost center scheme includes override settings for non-job entries in Cost Center Scheme Maintenance, this screen validates the cost center assigned to non-direct time card lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general.

Deduction or Add-on
Spectrum verifies that you have permission to access the deduction/add-on code. Spectrum compares the deduction's list of shared cost centers with cost centers in your operator's assigned cost center scheme, and if there are no common cost centers, then entry of that deduction/add-on code is disallowed. All deductions and add-ons assigned to the employee will appear in the maintenance screen, but changes will not be allowed if your operator is not authorized for that code.

Multi-Company
Cost center validation is performed based on settings in the destination company. When Enterprise Installation option for cost centers is set to Yes in the destination company, then the cost center designated on the distribution line must be valid in that other company. Job, phase, equipment, and cost category authorization is validated with the operator settings in the destination company. When Enterprise Installation option for cost centers is set to No in the destination company, then the cost center field will not appear in the window for that time card.
