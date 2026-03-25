---
title: "Delete a CM Account | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/delete-a-cm-account"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/delete-a-cm-account"
---

# Delete a CM Account

To delete a CM account that will no longer be used, you must purge all detail from all statements.
The CM Statement Purge program does not allow purging detail from the last closed statement. You can purge detail only from the statement closed prior to the last closed statement. Therefore, after reconciling and closing the last statement, you must perform the following tasks:

1. Set up a dummy statement in CM Statement Control with a beginning balance equal to the ending balance, and set the Status to Closed.

1. Purge through the last real statement.

1. In CM Statement Control, delete the dummy statement.

1. Delete the account in CM Accounts.
