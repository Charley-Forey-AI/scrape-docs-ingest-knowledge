---
title: "Pre-Time Card Quantity Import Errors - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/pre-time-card-import-errors/pre-time-card-quantity-import-errors/pre-time-card-quantity-import-errors---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/pre-time-card-import-errors/pre-time-card-quantity-import-errors/pre-time-card-quantity-import-errors---cost-center-information"
---

# Pre-Time Card Quantity Import Errors - Cost Center Information

For records sent to the error screen due to the import operator having insufficient security for the job or phase, the Quantity Import screen lists the error as "Cost center invalid for import."
When rechecking a time card entry, you must have security for the cost center (from the job or phase override). When rechecking, if any records that would be updated are flagged as having an import operator cost center security error, the following prompt displays: "Update record(s) with errors due to import operator's cost center security settings now?"
When Enterprise Installation option for cost centers is set to Yes in this company, when entering quantities, Spectrum verifies that the job and phase are permitted. The cost center for the line will be display only from the phase (or job if no cost center is assigned to the phase), and must be valid for your operator. The job override from the cost center scheme will be used to determine if the cost center is valid for your operator.
If the Company field is changed to another company, cost center validation is performed based on settings in the destination company. If the Enterprise Installation option for cost centers is set to Yes in the destination company, then you must have cost center authorization in that other company. When Enterprise Installation option for cost centers is set to No in the destination company, then you will be permitted to proceed.
