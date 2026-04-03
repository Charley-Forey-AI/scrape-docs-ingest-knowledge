---
title: "Subcontract Change Order Log - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-financial-summary/subcontract-change-order-log/subcontract-change-order-log---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-financial-summary/subcontract-change-order-log/subcontract-change-order-log---cost-center-information"
---

# Subcontract Change Order Log - Cost Center Information

If the cost centers are being used, when accessing subcontract change orders Spectrum validates that the cost center assigned to the vendor is an authorized cost center for your operator. Spectrum compares the vendor's list of shared cost centers with cost centers in your operator's assigned cost center scheme, and if there are no common cost centers, then that vendor is disallowed. Spectrum also compares the cost center assigned to the job with cost centers in your operator's assigned scheme, and if the job's cost center is not present, then subcontract change orders will not be displayed for that job.
When your cost center scheme includes override settings for job entries in Cost Center Scheme Maintenance, the Subcontract Change Orders screen will validate the cost center assigned to associated A/R change request based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum compares the cost center assigned in the entry screen detail with job override cost centers in your operator's assigned scheme, and if the cost center is not included, then entries for the change order will not be allowed.
