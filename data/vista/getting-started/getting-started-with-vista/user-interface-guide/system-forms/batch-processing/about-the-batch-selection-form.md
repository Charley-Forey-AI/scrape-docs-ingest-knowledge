---
title: "About the Batch Selection Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/batch-processing/about-the-batch-selection-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/batch-processing/about-the-batch-selection-form"
---

# About the Batch Selection Form

Posting programs in the system use batches to record data. You can use the Batch
 Selection form to either create a new batch or find an existing batch to use.
Batch entry forms are those forms that require you to create or
 open a batch in order to add, change, or delete records, and then process the batch in order
 to update the appropriate database tables. Records in batches are only recognized after the
 batch is posted.

## About the In Use By column

The In Use By
 column indicates whether a batch is currently in use and by whom. To help you prevent
 inadvertent errors, if the batch is in use by another user, no other user can access the
 batch.
Occasionally, the ‘in use’ indicator remains even when a user is
 not actually using the batch. This is usually due to a system error/interruption.

- If you see your username in the In Use By column, unlock the batch by selecting
 the batch in the grid, right-clicking your mouse, and selecting Unlock Batch.
Note: The unlock action from within the batch selection form only works when
 your username appears in the In Use By
 field, regardless of who created the batch.

- If you need access to a batch displaying another username in
 the In Use By column, and if you have
 access to the HQ Batch Control form, clear the In
 Use By field in that form.

## About the Restricted column

Only the user who created a restricted batch can open it. If you
 need to remove a batch’s restriction (for example, the originating user is unavailable and
 you need to post the batch), you can do so using the HQ Batch Control form (if security
 allows you access).
Note: Once the restriction is removed, the batch can be opened by any user with
 access to the batch selection form.
Note: Regardless of who applies a restriction to a batch, the user who created it
 is the only one who can open it.

Related information

- [About the HQ Batch Control Form](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form)
