---
title: "Change Order Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-entry/change-order-entry/change-order-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-entry/change-order-entry/change-order-entry---cost-center-information"
---

# Change Order Entry - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, when entering a job Spectrum will allow change order log entry for the job only if the operator has permission to access the job. As the operator requests each job, Spectrum compares the cost center assigned to the job with cost centers in the operator's assigned scheme; if the cost center is not included, then entries for that job would not be allowed.
When the operator's scheme includes override settings for 'Job' entries in Cost Center Scheme Maintenance, this screen will validate the cost center assigned to the job based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned to the job with 'Job' override cost centers in the operator's assigned scheme; if the cost center is not included, then entry will not be allowed.
At the customer field, Spectrum will verify that the operator has authorization for the contract. Spectrum compares the contract's cost center with cost centers in the operator's assigned scheme; if the cost center assigned to the contract is not present, then that contract is not shown.
When the operator's scheme includes override settings for 'Contract' entries in Cost Center Scheme Maintenance, this screen will validate the cost center assigned to the contract based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned to the contract with 'Contract' override cost centers in the operator's assigned scheme; if the cost center is not included, then entry will not be allowed.
When drilling into change order detail, all information for that change order will display, even if the operator does not have permission for certain phases referenced in the Contract Pricing sub-window or subcontracts referenced in the Subcontract Pricing sub-window.
