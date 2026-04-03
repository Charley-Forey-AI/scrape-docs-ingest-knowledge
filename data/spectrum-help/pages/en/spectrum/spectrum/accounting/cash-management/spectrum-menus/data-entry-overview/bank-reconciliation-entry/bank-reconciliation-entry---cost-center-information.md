---
title: "Bank Reconciliation Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/bank-reconciliation-entry/bank-reconciliation-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/bank-reconciliation-entry/bank-reconciliation-entry---cost-center-information"
---

# Bank Reconciliation Entry - Cost Center Information

If cost centers are enabled in the current company, Spectrum will verify authorization for the G/L account code by comparing the entry to the list of allowed cost centers for that G/L account. Spectrum compares the G/L account's list of shared cost centers with cost centers in the operator's assigned scheme; if there are no common cost centers, then that G/L account code is not allowed. If the operator is allowed to access the account, all reconciled transactions will display (and can be selected) regardless of the cost center originally assigned to the original transaction.
The override cost centers supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned in the entry screen detail with 'Non-job' override cost centers in the operator's assigned scheme; if the cost center is not included, then that cost center will not be allowed on the transaction line.
In addition, the G/L opening and ending balances in the header of this screen only include values for cost center(s) associated with the 'Bank account' being reconciled. This facilitates reconcilement for operations utilizing multiple bank accounts (for different cost enters), tied to the same G/L 'Cash in Bank' account.
