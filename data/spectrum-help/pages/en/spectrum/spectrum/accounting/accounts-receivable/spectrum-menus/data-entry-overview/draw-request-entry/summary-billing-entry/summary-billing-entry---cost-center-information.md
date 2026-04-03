---
title: "Summary Billing Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/summary-billing-entry/summary-billing-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/summary-billing-entry/summary-billing-entry---cost-center-information"
---

# Summary Billing Entry - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, when accessing a draw a draw request Spectrum will display the draw only if the operator has permission to access the job. As the operator requests each job, Spectrum compares the cost center assigned to the job with cost centers in the operator's assigned scheme; if the cost center is not included, then draw requests for that job will not be shown.
When the operator's scheme includes override settings for 'Job' entries in Cost Center Scheme Maintenance, this screen will validate the cost center assigned to the job based on these overrides. The override cost centers(s) supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned to the job with 'Job' override cost centers in the operator's assigned scheme; if the cost center is not included, then draw request for that job will not be shown.
Spectrum also compares the contract's cost center with cost centers in the operator's assigned scheme; if the cost center assigned to the contract is not present, then draw request for that contract will not be shown.
When the operator's scheme includes override settings for 'Contract' entries in Cost Center Scheme Maintenance, this screen will validate the cost center assigned to the contract based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned to the contract with 'Contract' override cost centers in the operator's assigned scheme; if the cost center is not included, then draw requests for that contract will not be shown.
