---
title: "Build Finance Charge Transactions - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/finance-charge-entry/build-finance-charge-transactions/build-finance-charge-transactions---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/finance-charge-entry/build-finance-charge-transactions/build-finance-charge-transactions---cost-center-information"
---

# Build Finance Charge Transactions - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, calculating finance charges will be performed only when the operator has permission to access all of the customers with open items. When the update is initiated, Spectrum compares the customers' lists of shared cost centers with cost centers in the operator's assigned scheme. If there are no common cost centers for any customer, then the finance charge calculation is not performed.
After verifying the operator is allowed to perform the build, Spectrum will calculate finance charges based on overdue balances.

1. Overdue balances are stored by cost center, based on the cost center assigned to each open item.

1. Calculate the finance charge using the assigned percentage for each cost center's overdue balance (positive or negative).

1. Test for minimum charge across cost centers:

- If the total overdue balance across all cost centers for the customer would result in a minimum charge, allocate the minimum charge as detailed below. Each cost center's finance charge allocation is rounded to the nearest penny.

- If the overdue balance across all cost centers for the customer exceeds the minimum charge, save the finance charge calculated from each cost center's overdue balance (even if it is negative or below the minimum charge if calculated alone).
