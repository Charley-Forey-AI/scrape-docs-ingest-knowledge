---
title: "Field Definitions: SL Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-batch-process-form/field-definitions-sl-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-batch-process-form/field-definitions-sl-batch-process-form"
---

# Field Definitions: SL Batch Process Form

The following is a list of field descriptions for the SL
 Batch Process form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Audit Reports

Prints the distribution information from the batch sorted according to updates to other modules.

- Batch List – Prints the audit list, depending on the batch being processed. Shows related information for each entry in the batch, in sequence order, with totals by batch sequence and batch number.

- Job Cost Distribution – Prints the SL JC Change Order Distribution List or SL JC Entry Distribution List, depending on the batch source.

- Error List – Displays the sequence number and error message for any entries where errors were found during validation. Errors must be corrected before posting the batch.

Note: Users who have access to batch processing forms do not automatically have access to the related audit reports. It is recommended that if they will be processing batches, you give them access to the related audit reports using VA Report Security. If users do not have access, they will receive an error message when trying to preview/print those reports to which they do not have access. In addition, if using the ‘Attach Batch Report to HQ Batch Control’ feature (assigned in SL Company Parameters), restricted access to one or more audit reports will prevent the user from posting the batch.
