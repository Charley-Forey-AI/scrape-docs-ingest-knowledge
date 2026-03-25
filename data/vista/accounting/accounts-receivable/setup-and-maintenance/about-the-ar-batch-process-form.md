---
title: "About the AR Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-batch-process-form"
---

# About the AR Batch Process Form

You can use the AR Batch Process form to post AR batches.This form can be accessed from the main menu or by selecting the Process Batch option from the File menu of any of the posting programs in AR (AR Invoice Entry, AR Cash Receipts, AR Finance Charge, and AR Release Retainage).
Once you have specified the month and batch to process, the Info section displays information about the batch (i.e. creator, creation date, source, and status).

## Validating Batch Information with Audit Reports

The next step in batch processing is to validate the information in the batch. This is done by clicking on the Validate button. The program runs through all of the data in the batch and creates Audit Reports that you can preview and/or print before you proceed with posting the batch.

-

- Batch List — Prints the AR Invoice Audit List, AR Receipts Audit List, or AR Release Retainage Audit List, depending on the batch you are processing. Shows related information for each entry in the batch, in sequence order, with totals by batch sequence and batch.

- Job Cost Distribution — Prints the JC Invoice Distribution List or JC Receipts Distribution List, depending on the batch you are processing. Shows billed information (invoices) or payment information (receipts) for each entry in the batch, with totals by item, contract, and JC Company.

- GL Account Distribution — Prints the AR GL Invoice Distribution List or AR GL Payment Distribution List, depending on the batch you are processing. Shows the GL account distribution information for the batch, sorted according to updates to other modules.

- AR JCMiscReceipts Distribution — Prints the AR JC Miscellaneous Receipts Distribution List, showing check number, units of measure, hours, units, and amount, with totals by cost type, phase, job, and company.

- AR EM MiscReceipts Distribution — Prints the AR EM Miscellaneous Receipts Distribution List, showing the equipment, cost code and cost type, component, unit of measure, hours, units, and amount, with totals by cost type, cost code, equipment, and company.

- CM Distribution — Prints the AR CM Distribution List, showing the bank account, customer, check number and date, deposit number, previous amount (if applicable), current amount, amount posted this batch, and total deposit amount, with totals by deposit number and company.

- Misc Distributions — Prints the AR Miscellaneous Distribution Audit List, showing for each sequence, the miscellaneous distribution code, description, and distribution amount, with totals by distribution code.

- AR SM Misc Recipts Distributions —
 Prints the AR Miscellaneous Distribution Audit List, showing for each sequence,
 the miscellaneous distribution code, description, and distribution amount, with
 totals by distribution code.

- Error List — Lists the sequence number and the error message for any entries where errors were found in the validation process. Errors must be corrected before the batch can be posted.

Users who have access to batch processing forms do not automatically have access to the related audit reports. It is recommended that if they will be processing batches, you give them access to the related audit reports using VA Report Security. If users do not have access, they will receive an error message when trying to preview/print those reports to which they do not have access. In addition, if using the Attach Batch Report to HQ Batch Control feature (assigned in AR Company Parameters), restricted access to one or more audit reports will prevent the user from posting the batch.
For information about setting up security for audit reports, see [VA Report Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form).

## Updating a Batch

Updating a batch is the process that takes each batch entry and makes all the necessary transaction updates. This may involve posting transactions to other modules as well as in Accounts Receivable. The following is a list of updates that occur when posting batches in AR:

- JC Interface — Indicates the update level for contract-related transactions as specified on the JC/EM tab in AR Company Parameters.

- GL Invoice Interface — Indicates the update level for invoices as specified on the Invoices tab in AR Company Parameters.

- GL Cash Interface — Indicates the update level for cash receipts as specified on the Receipts tab in AR Company Parameters.

- CM Interface — Indicates the update level for CM as specified on the CM tab in CM Company Parameters.

Once the batch is ready for processing, enter the posting date and click Post. After all of the entries have been successfully updated, the entries are cleared, and the batch is closed.

## Clearing a Batch

When you create a batch, the system adds the data to a batch table and stores it until you are ready to post the batch. Data is not updated online; therefore, you can delete it completely without affecting any modules, including the module in which you created the batch. To clear a batch table of stored data, select File > Clear Batch. The system will clear/delete all data from the batch. Previously posted transactions added to the batch are only cleared from the batch—they are not deleted.

- The system creates an audit record each time you clear a batch. For information about cleared batches (i.e. user who cleared batch, as well as the date and time the batch was cleared), use the VA 'Other Events' Statistics report.

- The Clear Batch option is disabled if the batch's status is 4 (Posting in Progress). This is to prevent partially updated batches from being deleted should the update process be interrupted (i.e. power outage, system failure, etc.). When a batch update is interrupted, only a portion of the intended updates may occur. If a user later clears the batch, there is no way to determine the updated data.
