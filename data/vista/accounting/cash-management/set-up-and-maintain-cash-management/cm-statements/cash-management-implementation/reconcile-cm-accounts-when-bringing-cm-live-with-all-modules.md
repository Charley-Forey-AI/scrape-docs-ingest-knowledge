---
title: "Reconcile CM Accounts When Bringing CM Live with All Modules | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-statements/cash-management-implementation/reconcile-cm-accounts-when-bringing-cm-live-with-all-modules"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-statements/cash-management-implementation/reconcile-cm-accounts-when-bringing-cm-live-with-all-modules"
---

# Reconcile CM Accounts When Bringing CM Live with All Modules

You can reconcile CM Accounts while bringing CM live alongside all other modules.

1. Set the GL Interface Level to No Update and check the Allow Changes to Statement Beginning Balance box in the CM Company Parameters program.

1. Enter the beginning and ending balances from your current statement in the CM Statement Control form.

1. Post outstanding entries to the CM Outstanding Entries form. For entries that were not processed in the Vista™ system, you need to make one lump sum check entry (C) to record the total of all checks cleared; make an adjustment entry (A) to record the total of all adjustments cleared; make one lump sum deposit entry (D) to record the total of all deposits cleared; and make individual entries for transactions that have not cleared the bank (as shown on the statement).

1. Enter any transfers that affect the current statement in the CM Transfers form.

1. Clear the lump sum entries made in Step 3 in the CM Clear Entries form. For checks and deposits that were processed in the Vista system, clear all that show as cleared on the current bank or brokerage statement. When finished, print the batch distribution list and post the batch.

1. Using the CM Account Statement Report, print the report and balance to the statement provided by your bank or brokerage firm.

1. Close the statement in CM Statement Control.

1. In the CM Company Parameters form, review all settings and make any necessary changes for live processing. In particular, set the GL Update Level to the desired level with the appropriate journal indicated, and uncheck the Allow Changes to Statement Beginning Balance box.

1. If you implemented AP, AR, and/or PR before CM, review each Company Parameters form to ensure that the CM flags have been set up properly.
