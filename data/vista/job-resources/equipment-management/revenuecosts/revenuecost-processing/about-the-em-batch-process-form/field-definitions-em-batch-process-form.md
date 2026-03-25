---
title: "Field Definitions: EM Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-batch-process-form/field-definitions-em-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-batch-process-form/field-definitions-em-batch-process-form"
---

# Field Definitions: EM Batch Process Form

The following is a list of field descriptions for the EM
 Batch Process form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Month

 Enter the month in which to process this batch (MM/YY).

##  Batch

 Enter a valid batch number. Press F4 for a list of available batches if needed.
 Once you have specified the batch, the screen displays the information specific to the batch. Make sure this is the correct batch before proceeding.

- Created By – Name of user who added this batch control record.

- Created – Date this batch was created.

- Source – Identifies the program in which this batch was created.

- Status – Identifies the current status of the batch.

- Open—Batch is ready for validation.

- Validated—Batch successfully validated, ready to post.

- Errors—Errors found. Must be corrected and batch revalidated before posting.

- Updated—Batch was successfully posted.

Validate
Press this button to validate the batch. Batch must be validated before it can be updated. During the validation process, each record in the batch is checked and any errors found are noted. If there are errors, the Error List option will become available on the form and you can preview or print a list of them.
Once you successfully validate the batch, the related audit reports are generated and available for printing. It is recommended that you print the audit reports before you post the batch, as they are not available once you process the batch.
When you have finished printing/reviewing the audit lists, you are ready to post the batch. Selecting another batch or closing the current batch before you post it will reset the status of the batch and require that you revalidate it before posting.
Interruptions
 If there is an interruption to the update process for any reason, you will be unable to revalidate the batch. You can reprint the audit and distribution lists as needed to show the remaining entries to update. Select Post to update the entries.
Clear Batch
To clear a batch that you have not yet posted, select the Clear Batch option from the File menu. The system does not update data online; therefore, you can delete the data without affecting any modules. If you added previously posted transactions to the batch, using this function only clears them from the batch—they will not be deleted from the system. To delete a previously posted transaction, you must set the transaction’s Action to ‘Delete’ and post the batch.
Note: This option is disabled if the batch’s status is ‘4’ (Posting in Progress). This is done to prevent partially updated batches from being deleted should the update process be interrupted (i.e. power outage, system failure, etc.). If there is an interruption to the update process, only a portion of the intended updates may occur. If you subsequently clear the batch, there is no way to determine which updates did not occur.

##  Audit Reports

Audit reports are generated once you successfully validate the batch and show what information will be updated when you post the batch. The availability of each audit report is determined by the batch source (i.e., the posting form) and the information posted to entries in the batch. It is recommended that you print the audit lists prior to posting the batch since they will not be available once you have processed the batch. The following lists are available for printing:

- Batch List - Prints the entries in the batch in sequence order.

- Job Cost Distribution - Prints the EM Job Cost Distribution List showing JC company/job, equipment, revenue code, work units, work unit of measure, time units, unit cost, and total cost detail.

- Inventory Distribution - Prints the EM Inventory Distribution List, showing the equipment, cost code, cost type, material, IN location, posted unit of measure, units sold, and unit price.

- GL Acct - Prints the EM GL Distribution List showing GL account update information at either the summary or the detail level.

- Error List - Lists the sequence number and the error message for any entries where errors were found in the validation process.

Note: Users who have access to batch processing forms do not automatically have access to the related audit reports. It is recommended that if they will be processing batches, you give them access to the related audit reports using VA Report Security. If users do not have access, they will receive an error message when trying to preview/print those reports to which they do not have access. In addition, if using the ‘Attach Batch Report to HQ Batch Control’ feature (assigned in EM Company Parameters), restricted access to one or more audit reports will prevent the user from posting the batch.
Preview/Print Lists
Preview – Click this button to view the selected list(s).
Print – Click this button to print the selected list(s). You can also print these lists from the Preview screen.

##  Posting Date

Enter the date to which the transactions in this batch will be posted. Initially defaults to the current date. Press the Post button to process the batch.
