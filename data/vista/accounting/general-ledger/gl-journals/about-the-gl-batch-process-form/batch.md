---
title: "Batch# | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-batch-process-form/batch"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-batch-process-form/batch"
---

# Batch#

Enter a valid batch number. Press F4 to look up the available batches if needed.
Note: If you are processing an SM batch and you accessed this form via SMBatches, this field will automatically default the batch number based on the batch you selected.
Once you have specified the batch, the screen displays information specific to this batch. Make sure this is the correct batch before proceeding.

- Created By - Display only; the name of user who created this batch.

- Created - Display only; the date and time this batch was created.

- Source - Display only; identifies the program in which the batch was created.

- Status - Display only; identifies the current status of the batch.

- Open - Batch is read for validation.

- Validated - Batch successfully validated; ready to post.

- Errors - Errors found. Must be corrected and batch revalidated before posting.

- Updated - Batch was successfully posted.

## Validate

Press this to validate. You must validate the batch before it can be updated. During the validation process, each record in the batch is checked and any errors found are noted. If there are errors, the Error List option will become available on the form and you can preview or print a list of them. You must correct all errors and revalidate the batch before it can be posted.
Note: It is recommended that you print the audit reports before you post the batch, as they are not available once you process the batch.

When you have finished printing/reviewing the audit lists, the batch is ready for posting. Selecting another batch or closing the current one before the program is run resets the status of the batch and requires it to be revalidated before posting.

## Interruptions

A batch whose posting process was interrupted for some reason cannot be revalidated. The audit and distribution lists can be reprinted, showing the remaining entries to update. Select Post and these entries will be updated.

## Clear Batch

If you need to clear the batch (for example, after discovering the entries were posted to the wrong fiscal period), you can do so using the File > Clear Batch option, as long as you have not yet posted the batch. Since the data is not updated on-line, you can clear it without affecting any modules, as though the data was never entered. If the batch includes transaction that were previously posted, they are only cleared from the batch; they are not deleted.
Note: The Clear Batch option is disabled if the batch’s status is Posting in Progress. This is done to prevent partially updated batches from being deleted should the update process be interrupted (i.e. power outage, system failure, etc.). When a batch update is interrupted, only a portion of the intended updates may occur. If the batch is subsequently cleared, there is no way to determine what was updated.
