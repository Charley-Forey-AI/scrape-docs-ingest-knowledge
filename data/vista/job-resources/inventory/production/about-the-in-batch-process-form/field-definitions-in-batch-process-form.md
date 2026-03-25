---
title: "Field Definitions: IN Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/production/about-the-in-batch-process-form/field-definitions-in-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/production/about-the-in-batch-process-form/field-definitions-in-batch-process-form"
---

# Field Definitions: IN Batch Process Form

The following is a list of field descriptions for the IN
 Batch Process form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Audit Reports

 Prints the distribution information from the batch sorted according to updates to other modules.
Note: If there are no entries in the batch, the audit lists cannot be printed. Also, it is recommended that you print the audit lists before you post a batch because once the batch is posted, the audit lists are no longer available.
 The following audit lists are available when processing IN batches. If a list is grayed out, it means that particular list is not available for the current batch. Additionally, only those lists with the checkbox marked can be previewed or printed.

- Batch List – Prints the audit list, depending on the batch being processed. Shows related information for each entry in the batch, in sequence order, with totals by batch sequence and batch number.

- GL Distribution - Prints the IN GL Distribution List, which differs based on the type of batch being processed (i.e. adjustment, transfer, or production). Shows the transaction, description, and the debit and credit amounts for each transaction.

- Job Cost Distribution – Prints the IN Material Order Entry JC Distributions List.

- Error List – Displays the sequence number and error message for any entries where errors were found during validation. Errors must be corrected before posting the batch.

Note: Users who have access to batch processing forms do not automatically have access to the related audit reports. It is recommended that if they will be processing batches, you give them access to the related audit reports using VA Report Security. If users do not have access, they will receive an error message when trying to preview/print those reports to which they do not have access. In addition, if using the ‘Attach Batch Report to HQ Batch Control’ feature (assigned in IN Company Parameters), restricted access to one or more audit reports will prevent the user from posting the batch.
