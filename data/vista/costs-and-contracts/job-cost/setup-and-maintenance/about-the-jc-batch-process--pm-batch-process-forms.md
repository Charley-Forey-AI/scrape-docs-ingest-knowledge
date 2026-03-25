---
title: "About the JC Batch Process / PM Batch Process Forms | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-batch-process--pm-batch-process-forms"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-batch-process--pm-batch-process-forms"
---

# About the JC Batch Process / PM Batch Process Forms

Use this form to process batches created in Job Cost, or cost projections created in the PM module.

- Month and batch# - Generally the Month
 and Batch# fields are disabled.

- Info section

- Created By - The user creating the batch.

- Created - The date and time the batch was created.

- Source - The process/program that created the
 batch.

- Status - The current status of the batch. Open - The
 batch is ready for validation. Validated - The batch has been successfully
 validated and is ready to post. Errors - The batch failed validation. Print
 an Error List, correct the errors, and then validate and post the batch.
 Updated - The batch was successfully posted.

- Validate button - Click on the Validate button to validate the transactions in the batch. If
 there are errors, generate an Error List report to review the list of
 errors.

- Audit Reports section - Once the batch has been validated
 (Validate button), use the Audit Reports section to select the
 audit reports to review before posting the batch.

- Batch List - Prints the JC Material Use Audit List,
 showing entries in the batch in sequence order.

- Show Full Projection Detail - This box applies to JC
 Cost Projection batches, but not PM Cost Projection batches. Check this
 box if you want the JC Projections Audit List to show full projection
 detail by phase/cost type.

- GL Account Distribution - Prints the JC GL Material
 Distribution List, showing the GL account distribution for the batch,
 sorted according to updates to other modules.

- Inventory Distribution – Prints the JC IN Cost Adj
 Distribution List, showing the updates to Inventory for the batch.
 Information includes job, phase, cost type, material, location, units,
 unit cost, unit price, total price, and total cost, with totals by
 company and batch.

- Error List - Lists the sequence number and the error
 message for any entries where errors were found in the validation
 process. Errors must be corrected before the batch can be posted.

- Printing / saving audit reports - You should print or save
 the audit reports before posting the batch. If the Attach Batch
 Report to HQ Batch Control box is checked (JC Company
 Parameters> info tab), the audit reports are automatically saved and attached
 to the batch record that is created in the [HQ Batch Control ](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form) form.

- Clear Batch - Select File > Clear Batch to clear a batch that has not yet been posted. For example, you
 might delete a batch after discovering the entries were posted to the wrong
 fiscal period. Since the data is not updated on-line, it can be deleted without
 affecting any modules, as though the data was never entered. Transactions that
 were previously posted and added to the batch are only cleared from the batch;
 they are not deleted. The Clear Batch option is disabled if the batch’s status
 is Posting in Progress. This is done to prevent partially updated batches from
 being deleted should the update process be interrupted (i.e. power outage,
 system failure, etc.). When a batch update is interrupted, only a portion of the
 intended updates may occur. If the batch is subsequently cleared, there is no
 way to determine what was updated.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters
