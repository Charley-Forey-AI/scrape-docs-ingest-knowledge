---
title: "About the IN Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/production/about-the-in-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/production/about-the-in-batch-process-form"
---

#  About the IN Batch Process Form

Uset the IN Batch Process form to validate and process batches
 created in the Inventory module.
You can access this form from the main menu or by
 selecting the Process batch option from the File menu of any posting forms in the
 Inventory module.
After the month and batch to process are specified,
 the Info section displays information about the batch (specifically, batch creator,
 creation date, batch source, and status).

## Audit Reports

The next step in batch processing is to
 validate the information in the batch. To do so, click Validate. The form runs
 through all the data in the batch and creates Audit Reports that can be previewed
 and/or printed before posting the batch. It is recommended that you print the audit
 lists before posting the batch. Once the batch is posted, the reports are no longer
 available. The following audit reports are available for this form:

- Batch List – Prints the audit
 list, depending on the batch being processed. Shows related information for
 each entry in the batch, in sequence order, with totals by batch sequence
 and batch number.

- GL Distribution - Prints the IN
 GL Distribution List, which differs based on the type of batch being
 processed (i.e. adjustment, transfer, or production). Shows the transaction,
 description, and the debit and credit amounts for each transaction.

- Job Cost Distribution – Prints
 the IN Material Order Entry JC Distributions List.

- Error List – Displays the
 sequence number and error message for any entries where errors were found
 during validation. Errors must be corrected before posting the batch.

Note:Users who have access to batch
 processing forms do not automatically have access to the related audit reports.
 It is recommended that if they will be processing batches, you give them access
 to the related audit reports using VA Report Security. If users do not have
 access, they will receive an error message when trying to preview/print those
 reports to which they do not have access. In addition, if using the ‘Attach
 Batch Report to HQ Batch Control’ feature (assigned in IN Company Parameters),
 restricted access to one or more audit reports will prevent the user from
 posting the batch.

Once the batch is ready for processing,
 enter the posting date and click Post. The entries are then cleared and the batch is
 closed.

## Clearing the Batch

When you create a batch, the system adds
 the data to a batch table and stores it until you are ready to post the batch. Data
 is not updated online; therefore, you can delete it completely without affecting any
 modules, including the module in which you created the batch. To clear a batch table
 of stored data, select ‘Clear Batch’ from the File menu. The system will
 clear/delete all data from the batch. Previously posted transactions added to the
 batch are only cleared from the batch—they are not deleted.
Note: The system creates an audit record each time you
 clear a batch. For information about cleared batches (that is, user who cleared
 batch, as well as the date and time the batch was cleared), use the VA 'Other
 Events' Statistics report.
The Clear Batch option is disabled if
 the batch’s status is 4
 (Posting in Progress). This is to prevent partially updated batches from being
 deleted should the update process be interrupted (for example, power outage,
 temporary system disconnect, and so on). When a batch update is interrupted, only a
 portion of the intended updates may occur. If a user later clears the batch, there
 is no way to determine the updated data
