---
title: "Job Quantity Complete Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-quantity-complete-entry/job-quantity-complete-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/job-quantity-complete-entry/job-quantity-complete-entry---cost-center-information"
---

# Job Quantity Complete Entry - Cost Center Information

When Enterprise Installation option for cost centers is set to Yes in this company, when entering quantities, Spectrum verifies the job is permitted, and you will not be able to enter a job unless the cost center assigned to that job is valid for your operator, and Spectrum only displays phases for that job if you have cost center security for the cost centers of the phase assigned to that line. The job override is used to determine valid cost centers for your operator.
Spectrum also ensures that you have permission for the cost center specified in the phase file, if any. If the cost center is not specified in the phase file, the cost center assigned to the job is used, provided you have permission for that cost center.
If your scheme includes override settings for job entries in Cost Center Scheme Maintenance, this screen validates the cost center assigned to direct job cost quantity detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general.
If the Company field is changed to another company, cost center validation is performed based on settings in the destination company. If the Enterprise Installation option for cost centers is set to Yes in the destination company, then you must have cost center authorization in that other company. Spectrum verifies that the cost center is valid for the job, phase, and operator in that other company.
No changes are allowed to the cost center assigned to the line in Time Card Entry by Quantity. This defaults from the phase, and if not set in the phase it defaults from the job.
