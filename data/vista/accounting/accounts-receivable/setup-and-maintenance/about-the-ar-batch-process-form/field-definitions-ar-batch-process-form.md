---
title: "Field Definitions: AR Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-batch-process-form/field-definitions-ar-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-batch-process-form/field-definitions-ar-batch-process-form"
---

# Field Definitions: AR Batch Process Form

The following is a list of field descriptions for the AR Batch Process form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Audit Reports

Audit reports are generated when the batch is validated and identify the information that will be updated when the batch is posted. The availability of each audit report is determined by the batch source (i.e., the posting form) and the information posted to entries in the batch. It is recommended that you print the audit lists prior to posting the batch since they will not be available once you have processed the batch. The following lists are available for printing:

- Batch List — Prints the AR Invoice Audit
 List, AR Receipts Audit List, or AR Release Retainage Audit List, depending on the
 batch you are processing. Shows related information for each entry in the batch, in
 sequence order, with totals by batch sequence and batch. As long as entries exist in
 the batch, this report can be printed.

- Job Cost Distribution — Prints the JC
 Invoice Distribution List or JC Receipts Distribution List, depending on the batch
 you are processing. Shows billed information (invoices) or payment information
 (receipts) for each entry in the batch, with totals by item, contract, and JC
 Company.

- GL Account Distribution — Prints the AR
 GL Invoice Distribution List or AR GL Payment Distribution List, depending on the
 batch you are processing. Shows the GL account distribution information for the
 batch, sorted according to updates to other modules.

- AR JC Misc Receipts Distribution —
 Prints the AR JC Miscellaneous Receipts Distribution List, showing check number,
 units of measure, hours, units, and amount, with totals by cost type, phase, job, and
 company.

- AR EM Misc Receipts Distribution —
 Prints the AR EM Miscellaneous Receipts Distribution List, showing the equipment,
 cost code and cost type, component, unit of measure, hours, units, and amount, with
 totals by cost type, cost code, equipment, and company.

- CM Distribution — Prints the AR CM
 Distribution List, showing the bank account, customer, check number and date, deposit
 number, previous amount (if applicable), current amount, amount posted this batch,
 and total deposit amount, with totals by deposit number and company.

- AR SM Misc Receipts Distributions — Prints the AR SM Miscellaneous Receipts
 Distribution List, showing SM line type entries that AR sends to SM, including work
 order scope and cost type batch sequence, check number, date, description and amount.


- Error List — Lists the sequence number
 and the error message for any entries where errors were found in the validation
 process. Errors must be corrected before the batch can be posted.

Users who have access to batch processing forms do not automatically have access to the related audit reports. It is recommended that if they will be processing batches, you give them access to the related audit reports using VA Report Security. If users do not have access, they will receive an error message when trying to preview/print those reports to which they do not have access. In addition, if using the ‘Attach Batch Report to HQ Batch Control’ feature (assigned in AR Company Parameters), restricted access to one or more audit reports will prevent the user from posting the batch.
