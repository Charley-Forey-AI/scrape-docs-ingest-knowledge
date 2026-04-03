---
title: "Invalid Billing Items Report - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-cost-selection/invalid-billing-items-report/invalid-billing-items-report---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-cost-selection/invalid-billing-items-report/invalid-billing-items-report---cost-center-information"
---

# Invalid Billing Items Report - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, when printing the Invalid Billing Items Report Spectrum will include the job only if the operator has permission to access the job's information. Spectrum compares the cost center assigned to the job with cost centers in the operator's assigned scheme; if the cost center is not included, then that job will not be shown.
When the operator's scheme includes override settings for 'Job' entries in Cost Center Scheme Maintenance, this report will validate the cost center assigned to the job based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned to the job with 'Job' override cost centers in the operator's assigned scheme; if the cost center is not included, then the job will not be shown on the report.
Spectrum will also verify that the operator requesting the report has permission to access the contract. Spectrum compares the contract's assigned cost center with cost centers in the operator's assigned scheme; if the cost center is not present, then quantity transactions for that contract will not be included.
When the operator's scheme includes override settings for 'Contract' entries in Cost Center Scheme Maintenance, this report will validate the cost center assigned to the contract based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned to the contract with 'Contract' override cost centers in the operator's assigned scheme; if the cost center is not included, then that contact will not be shown on the report.
All detail lines are included on the report when the operator has authorization to access that job and contract, regardless of phase and billing item cost center security.
