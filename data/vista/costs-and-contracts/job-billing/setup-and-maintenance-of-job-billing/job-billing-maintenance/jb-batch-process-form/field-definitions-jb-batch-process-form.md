---
title: "Field Definitions: JB Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/job-billing-maintenance/jb-batch-process-form/field-definitions-jb-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/job-billing-maintenance/jb-batch-process-form/field-definitions-jb-batch-process-form"
---

# Field Definitions: JB Batch Process Form

The following is a list of field descriptions for the JB
 Batch Process form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Month

The Month field on the JB Batch Process form.
Enter the batch process month. This field defaults the current month.

## Batch#

The Batch # field on the JB Batch Process form.
Enter a valid batch number. Press F4 for a list of valid batches for the specified batch month.
Once you have specified the batch, the screen displays information specific to this batch. Make sure this is the correct batch before proceeding.

- Created By - Display only; the name of user who created this batch.

- Created - Display only; the date and time this batch was created.

- Source - Display only; identifies the program in which the batch was created.

- Status - Display only; identifies the current status of the batch.

- Open - Batch is read for validation.

- Validated - Batch successfully validated; ready to post.

- Errors - Errors found. Must be corrected and batch revalidated before posting.

- Updated - Batch was successfully posted.

### Validate

Press this to validate. You must validate the batch before it can be updated. During the validation process, each record in the batch is checked and any errors found are noted. If there are errors, the Error List option will become available on the form and you can preview or print a list of them. You must correct all errors and revalidate the batch before it can be posted.
Note: It is recommended that you print the audit reports before you post the batch, as they are not available once you process the batch.

When you have finished printing/reviewing the audit lists, the batch is ready for posting. Selecting another batch or closing the current one before the program is run resets the status of the batch and requires it to be revalidated before posting.

### Interruptions

A batch whose posting process was interrupted for some reason cannot be revalidated. The audit and distribution lists can be reprinted, showing the remaining entries to update. Select Post and these entries will be updated.

### Clear Batch

If you need to clear the batch (for example, after discovering the entries were posted to the wrong fiscal period), you can do so using the File > Clear Batch option, as long as you have not yet posted the batch. Since the data is not updated on-line, you can clear it without affecting any modules, as though the data was never entered. If the batch includes transaction that were previously posted, they are only cleared from the batch; they are not deleted.
Note: The Clear Batch option is disabled if the batch’s status is Posting in Progress. This is done to prevent partially updated batches from being deleted should the update process be interrupted (i.e. power outage, system failure, etc.). When a batch update is interrupted, only a portion of the intended updates may occur. If the batch is subsequently cleared, there is no way to determine what was updated.

##  Audit Reports

This field prints distribution information about the batch sorted according to
 updates to other modules.
Note: If there are no entries in the batch, you cannot print the audit lists. It is recommended that you print the audit lists before posting a batch; once the batch is posted, the audit lists are no longer available.
 The following audit lists are available when processing JB batches. If a list is disabled, that particular list is not available for the current batch. To print or preview a report, select the appropriate checkbox.

- Batch List - Prints the JB AR
 Invoice Audit, showing for each billing/invoice, the units and amounts for each
 item that updates to AR. For invoices with a status of “C-Change”, the report
 shows both the old and new billing information.

- Job Cost Distribution -
 Prints the JB JC Distribution List, showing contract revenue billed (units and
 amount), retainage, and tax for each contract and item.

- General Ledger Distribution -
 Prints the JB GL Distribution List, showing the GL accounts that the interface
 updates.

- Error List - Lists the
 sequence number and the error message for any entries where errors were found in
 the validation process.

Note: Users who have access to batch processing forms do not automatically have access to the related audit reports. It is recommended that if they will be processing batches, you give them access to the related audit reports using VA Report Security. If users do not have access, they will receive an error message when trying to preview/print those reports to which they do not have access. In addition, if using the ‘Attach Batch Report to HQ Batch Control’ feature (assigned in JB Company Parameters), restricted access to one or more audit reports will prevent the user from posting the batch.

## Posting Date

The Posting Date field on the JB Batch Process form.
This field initially defaults to the current date. Accept the
 default date or enter the date to which all transactions in this batch are to be
 posted.
Click Post to
 initiate the update/posting process. The system will process each batch entry and make all
 the necessary transaction updates.
After all entries are successfully updated, they are cleared and
 the batch is closed.
