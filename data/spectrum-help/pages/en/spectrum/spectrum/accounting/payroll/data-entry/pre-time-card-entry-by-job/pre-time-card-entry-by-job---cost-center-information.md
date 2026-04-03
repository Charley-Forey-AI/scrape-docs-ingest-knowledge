---
title: "Pre-Time Card Entry by Job - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/pre-time-card-entry-by-job/pre-time-card-entry-by-job---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/pre-time-card-entry-by-job/pre-time-card-entry-by-job---cost-center-information"
---

# Pre-Time Card Entry by Job - Cost Center Information

When Enterprise Installation option for cost centers is set
 to Yes in this company, when
 entering pre-time cards for a job, Spectrum allows entry only if you have permission to access
 that job.
As you request each job, Spectrum compares the cost center assigned to the job with cost
 centers in your operator's assigned cost center scheme, and if the cost center is not
 included, then time card entries for that job will not be allowed.
If the operator's scheme includes override settings for job entries in Cost Center Scheme Maintenance, this update will validate the cost center assigned to the job based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general.
Spectrum displays time card lines for the job only if you are authorized to view the employee.
When entering time card lines for a job in another company, cost center validation is performed based on settings in the destination company. If the Enterprise Installation option for cost centers is set to Yes in the destination company, then the cost center designated on the distribution line must be valid in that other company. Spectrum also verifies that the cost center is valid for the job and phase.
In the Pre-Time Card Entry window, Spectrum allows entry of a payroll department code only if the cost center for the job and phase is valid for that department. Spectrum will use the cost center assigned to the phase, and if this is blank then the cost center assigned to the job is used. If this cost center is not setup for the department, then the phase is shown as invalid, and you must correct either the phase or department to continue.
In the Pre-Time Card Entry window, when adding, editing, or deleting a deduction or add-on time card line, Spectrum verifies that you have permission to access the deduction/add-on code. All deductions and add-ons assigned to the employee display in the maintenance screen, but changes will not be allowed if you are not authorized for that code.
When adding, editing, or deleting a deduction or add-on code, Spectrum also verifies that the employee has permission for the deduction/add-on code.
