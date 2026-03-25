---
title: "Reconcile CM Accounts When Bringing CM Live After Other Modules | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-statements/cash-management-implementation/reconcile-cm-accounts-when-bringing-cm-live-after-other-modules"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-statements/cash-management-implementation/reconcile-cm-accounts-when-bringing-cm-live-after-other-modules"
---

# Reconcile CM Accounts When Bringing CM Live After Other Modules

You can reconcile CM Accounts while bringing CM live after
 other modules have been implemented.
If you are implementing CM several months after the
 other modules, then you have probably been updating checks and deposits and reconciling
 bank statements manually. Unless you want to reconcile all of these bank statements
 again in CM, you need to complete the following steps to reconcile each CM bank account.
 To reconcile CM accounts after the
 other Vista modules have been implemented:

1. Set the GL Interface
 Level to ‘No Update’ and check the Allow Changes to Statement Beginning Balance
 box in the CM Company Parameters form.

1. Enter a dummy first
 statement with a beginning balance of zero and an ending balance that is equal
 to the beginning balance of your first live statement in the CM Statement
 Control form.

1. Using the dummy
 statement, clear all entries that have cleared the bank (on any statement before
 your first live statement) in the CM Clear Entries form.

1. In the CM Outstanding
 Entries program, determine the amount of the variance on the dummy statement and
 post the amount as a single adjustment using the dummy statement.

1. Using the dummy
 statement, clear the adjustment entry posted in Step 4 in the CM Clear Entries
 form. The working balance and the statement balance should balance at this
 point.

1. In CM Statement Control,
 close the dummy statement. See “Reconciliation Process” in this help file or the
 CM Processing log for instructions on how to reconcile your first live
 statement.

1. In the CM Company
 Parameters form, review all settings and make any necessary changes for live
 processing. In particular, set the GL Update Level to the desired level with the
 appropriate journal indicated, and uncheck the Allow Changes to Statement
 Beginning Balance box.

1. Review the AP, AR,
 and/or PR Company Parameters forms to ensure that the CM flags have been set up
 properly.
