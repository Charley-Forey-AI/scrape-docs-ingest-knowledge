---
title: "About the CM Statement Control Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-statements/about-the-cm-statement-control-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-statements/about-the-cm-statement-control-form"
---

# About the CM Statement Control Form

The CM Statement Control form stores the statement balance and status information about each account.
As items are cleared, the totals change and are reflected in this program. To reconcile or close a statement, the working balance and the statement balance must be equal.

## Processing Statements

To set up a new statement to reconcile, first make sure the last one is closed. Then,
 using the CM Statement Control program, enter a new statement date and balance. Use
 the CM Outstanding Entries program to post adjustments and CM Clear Entries program
 to clear the appropriate entries to balance the statement.

## Working Balance

When a statement is newly opened, the working balance is the same as the beginning
 balance. As you clear items, the working balance is updated. The statement is
 reconciled when the working balance again equals the statement balance. You cannot
 close a statement until the working and statement balances are equal.

## Beginning Balance Changes

There is an option in CM Company Parameters that allows you to decide whether
 beginning balances may be changed or if they should always be the ending balance of
 the last statement. Generally you will not want to allow beginning balance changes;
 however, when you initially set up the system you will need to use this feature.

## Open/Closed Statements

You may have only one statement open at a time for an account. Statements may be
 closed only when their working and statement balances are equal. To close the
 statement, change the Status to Closed in the CM Statement Control program.
A statement may be reopened (by changing the Status to Open) as long as another
 statement for that account has not already been added.
