---
title: "Reconciliation Process | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/processing/reconciliation/reconciliation-process"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/processing/reconciliation/reconciliation-process"
---

# Reconciliation Process

Review the reconciliation process for CM.

1. Enter the date and balance of the statement to reconcile in the CM Statement Control program. (The last statement must be closed before you can begin processing a new statement.)

1.  Check the bank statement for charges and other adjustments that will not be reflected in this account from any of the subsidiary modules (e.g., AR, AP, and PR). Make the adjustments in CM Outstanding Entries. If the GL Interface field in CM Company Parameters is set to Summary or Detail, the entries made here will be interfaced to the appropriate GL accounts automatically.

1. Post any transfers of funds between bank accounts in CM Transfers.

1. In CM Clear Entries, select the items that have cleared the account for this statement period. You may set up this program to display any combination of items (e.g., checks, deposits, adjustments, or transfers). Because many bank statements are set up in sections, you can clear items for the statement in a similar manner (i.e., first deposits, then checks, then other adjustments, and so forth).

1. When the Working Balance equals the Statement Balance (displays on the right side of the CM Clear Entries program), your statement is reconciled.

1. Run the CM Account Statements Report specifying the statement dates and selecting cleared items only. Every check, deposit, and/or adjustment that is flagged as cleared for this statement will list on the report. The totals at the end of the report contain a recap of the account information, including the account balance and the cleared and outstanding item totals. Use these totals to finish balancing the statement. Most bank statements are subtotaled by checks cleared, deposits cleared, and miscellaneous adjustments. Therefore, you can compare the subtotals for the cleared items on the Account Statement Report with the bank’s subtotals to check for possible errors.
