---
title: "Void Check Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/void-check-entry/void-check-entry---cost-center-information"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/void-check-entry/void-check-entry---cost-center-information"
---

# Void Check Entry - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, when voiding a check Spectrum will allow entry only if the operator has permission to access the vendor and invoice. Spectrum compares the vendor's list of shared cost centers with cost centers in the operator's assigned scheme, and if there are no common cost centers, then checks for that vendor are not allowed. Spectrum also compares the cost center assigned to the payment transaction with cost centers in the operator's assigned scheme, and if the check's cost center is not included, then that check cannot be voided.
Note: For void checks, the cost center defaults from the original check, not the check cycle's cost center.
If multi-cost center or mutli-entity transactions, this update will reverse payments using the same inter-post G/L account hierarchy as when originally paid.
