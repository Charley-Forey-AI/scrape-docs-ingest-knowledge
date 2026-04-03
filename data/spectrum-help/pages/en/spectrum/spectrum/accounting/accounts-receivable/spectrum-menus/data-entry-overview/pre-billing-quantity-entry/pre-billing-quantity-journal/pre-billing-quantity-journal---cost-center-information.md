---
title: "Pre-Billing Quantity Journal - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/pre-billing-quantity-entry/pre-billing-quantity-journal/pre-billing-quantity-journal---cost-center-information"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/pre-billing-quantity-entry/pre-billing-quantity-journal/pre-billing-quantity-journal---cost-center-information"
---

# Pre-Billing Quantity Journal - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, when printing and updating the Pre-Billing Quantity Journal Spectrum will include the job only if the operator has permission to access the job. Spectrum compares the cost center assigned to the job with cost centers in the operator's assigned scheme; if the cost center is not included, then that job will not be shown.
When the operator's scheme includes override settings for 'Job' entries in Cost Center Scheme Maintenance, this report will validate the cost center assigned to the job based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned to the job with 'Job' override cost centers in the operator's assigned scheme; if the cost center is not included, then the job will not be shown on the report.
Spectrum will also verify that the operator requesting the report has permission to access the contract. Spectrum compares the contract's assigned cost center with cost centers in the operator's assigned scheme; if the cost center is not present, then quantity transaction for that contract will not be included.
When the operator's scheme includes override settings for 'Contract' entries in Cost Center Scheme Maintenance, this report will validate the cost center assigned to the contract based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned to the contract with 'Contract' override cost centers in the operator's assigned scheme; if the cost center is not included, then that contract will not be shown on the report.
When the operator is authorized to access the job and contract, all billing item transactions for that contract are included on the report and updated, including ones for disallowed cost centers.
