---
title: "Time Card Quantity Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/time-card-quantity-entry/time-card-quantity-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/time-card-quantity-entry/time-card-quantity-entry---cost-center-information"
---

# Time Card Quantity Entry - Cost Center Information

If cost centers are being used in this company, when
 entering quantities, Spectrum verifies the job is permitted.
You will not be able to enter a job unless the cost center assigned to that job is valid
 for your operator, and Spectrum only displays phase information the cost centers
 assigned to the phases that are valid for your operator. The cost center assigned to the
 quantity line is display only. The job override is used to determine valid cost centers
 for your operator.
Spectrum also assures that you have permission for cost center specified in the phase file, if any. If the cost center is not specified in the phase file, the cost center assigned to the job will be assigned, provided you have permission for that cost center.
If your scheme includes override settings for job entries in Cost Center Scheme Maintenance, this screen will validate the cost center assigned to direct job cost quantity detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general.
If the Company field is changed to another company, cost center validation is performed based on settings in the destination company. When the Enterprise Installation option for cost centers is set to Yes in the destination company, then you must have cost center authorization in that other company. Spectrum verifies that the cost center is valid for the job, phase, and your operator in that other company. When the Enterprise Installation option for cost centers is set to No in the destination company, then you will be permitted to proceed.
