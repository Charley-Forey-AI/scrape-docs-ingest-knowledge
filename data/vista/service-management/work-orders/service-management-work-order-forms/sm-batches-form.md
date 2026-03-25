---
title: "SM Batches Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-batches-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-batches-form"
---

# SM Batches Form

Use the SM Batches form to select SM batches for processing.

You will only need to use this form for batches that are in an "unposted" status due to validation errors or interruptions during the validation or posting process (for example, batch processing was interrupted by power failure and batch is stuck at a status of 4-Processing).
Once you select a batch, the upper grid displays all existing unprocessed batches. If you want to see only those batches you created, select the Include My Batches Only checkbox.
For each batch, the grid shows the batch month, ID, and status, as well as who created the batch, whether the batch is in use and by whom, and the batch source. Once you click on a batch, the lower grid shows all transactions within the batch. In many cases, this grid may be empty, meaning there are no transactions in the batch.
 You cannot remove transactions from the batch using this form. If you need to remove transactions from a batch and the batch is not in a "Posting" status, you can remove the transactions by clearing the batch in SM Batch Process. For more information, see [SM Batch Process Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-batch-process-form).

## In Use By

This column indicates whether a batch is currently in use and by whom. If a batch is in use, it does not necessarily mean that a user is currently in the batch entering data. In some cases, a batch can be flagged as 'in use' because of an interrupted validation process or a program error. You can unlock a batch by selecting the batch in the grid, right-clicking your mouse, and selecting the Unlock Batch option. However, you can only use the Unlock Batch option for batches you created. Batches that are 'in use by' other logins must be unlocked by that user or via HQ Batch Control (if security allows you access).

## Batch Status

The Status column identifies the processing status of each batch to help determine at what level the batch was interrupted.

- Open - You will typically only see this status if a batch was stuck in an unposted state and someone manually changed the batch's status to Open via HQ Batch Control.

- Valid - This status indicates the batch process was interrupted during or just after the validation process.

- Errors - This status indicates errors occurred during validation that need to be corrected before you can post the batch.

- Posting - This status indicates the batch process was interrupted during posting.

You can post batches with a status of Open, Valid, or Posting by selecting them from the Batches list and clicking the Post button. This will access the SM Batch Process form, where you can process as normal.
If a batch has an Errors status, you will need to correct the errors before you can post the batch. You can identify the errors by clicking the Post button to access SM Batch Process, and then clicking Preview or Print to see the Error Report.

## Refresh

Some batches cannot be posted from this form and will require that you post them directly in the related batch form. For example, to process a batch with an 'SM Invoice' source, you must post that batch directly in the AR Batch Process form. Once you post the AR batch, clicking the Refresh button in this form updates the grid, removing the posted batch from the list.

Related tasks

- [Post a Batch Using SM Batches](/en/vista/vista/service-management/work-orders/about-posting-work-completed-batches/post-a-batch-using-sm-batches)

Related information

- [SM Batch Process Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-batch-process-form)
