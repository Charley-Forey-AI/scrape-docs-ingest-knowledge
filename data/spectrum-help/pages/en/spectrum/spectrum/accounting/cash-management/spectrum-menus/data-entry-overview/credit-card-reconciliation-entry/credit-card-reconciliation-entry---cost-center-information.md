---
title: "Credit Card Reconciliation Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/credit-card-reconciliation-entry/credit-card-reconciliation-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/credit-card-reconciliation-entry/credit-card-reconciliation-entry---cost-center-information"
---

#  Credit Card Reconciliation Entry - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, in the Additional Transactions window Spectrum will verify authorization for the G/L account code by comparing the entry to the list of allowed cost centers for that G/L account. Spectrum compares the G/L account's list of shared cost centers with cost centers in the operator's assigned scheme; if there are no common cost centers, then that G/L account code is not allowed. Validation is also performed if the operator attempts to change or delete an existing transaction line. Spectrum provides a cost center on each detail line. Spectrum also verifies that the cost center entered is valid for the credit card account.
The G/L opening and ending balances in the header of this screen only include values for cost center(s) associated with the 'Credit card account' being reconciled.
When the operator's scheme includes override settings for 'Non-job' entries in Cost Center Scheme Maintenance, the Additional Transactions window will validate the cost center assigned to transaction lines based on these overrides. The override cost centers supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned in the entry screen detail with 'Non-job' override cost centers in the operator's assigned scheme; if the cost center is not included, then that cost center will not be allowed on the transaction line.
The additional transaction update will post to G/L using the cost center entered for both the credit G/L account entered and the debit G/L account (cash G/L account entered for that bank account). This facilitates reconcilement for operations utilizing multiple accounts (for different cost enters), tied to the same G/L 'Cash in Bank' account.
