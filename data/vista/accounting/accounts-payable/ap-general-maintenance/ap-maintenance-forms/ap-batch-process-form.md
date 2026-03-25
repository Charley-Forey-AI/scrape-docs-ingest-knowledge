---
title: "AP Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/ap-maintenance-forms/ap-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/ap-maintenance-forms/ap-batch-process-form"
---

# AP Batch Process Form

Use the AP Batch Process form to process (post) Accounts Payable batches.
You can access this form from the main menu or by selecting File > Batch Process in the AP posting or batch processing form.
Once you specify the month and batch to process, the Info
 section of the screen displays information about the batch.

- Created By - the name of user who created this batch.

- Created - the date and time this batch was created.

- Source - the form in which this batch was created. Source is hard-coded and
 cannot be changed by users.

- Status - the current status of the batch.

- Open - ready for validation

- Validated - successfully validated and ready to post

- Errors - errors must be corrected and the batch
 re-validated before posting

- Updated - successfully posted

## Available Audit Reports

Each batch type will have its own set of audit reports. The
 following audit reports are available for this module:

- Batch List — Prints the AP Entry Audit List (invoice entry batch), AP
 Release Retainage Audit List (released retainage batch), or AP Payment Audit List
 (payment batch), showing details of each entry in the batch. Entries are displayed in
 batch sequence order.

- Job Cost Distribution – Prints the AP JC Entry Distribution List, showing
 the invoices that will be interfaced to JC. Information shown includes the phase,
 cost type, unit of measure, and unit.

- Equipment Distribution – Prints the AP EM Entry Distribution List, showing
 the invoices that will be interfaced to EM. Information shown includes the vendor, AP
 reference (invoice) number, material, equipment unit of measure, and units. May also
 include PO/PO Item or Work Order/Work Order Item, if applicable.

- Inventory Distribution – Prints the AP IN Entry Distribution List, showing
 the invoices that will be interfaced to IN. Information includes the GL account,
 sales unit of measure and units, and the standard unit of measure and units for each
 transaction.

- GL Account Distribution – Prints the AP GL Entry Distribution List or AP GL
 Payments Distribution list (depending on batch type), showing the debit and credit
 amounts for each transaction.

- Error List – Lists the sequence number and the error message for any entries
 containing errors. You must correct the errors before you post the batch.

Note: Users who have access to batch processing forms do not automatically
 have access to the related audit reports. It is recommended that if they will be
 processing batches, you give them access to the related audit reports using the [VA Report Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form) form. If users do not have access to each report, they
 will receive an error message when trying to preview/print them, but they will be able
 to post.
Important: If you selected the Attach Batch Report to
 HQ Batch Control checkbox in the AP Company Parameters form (Audit
 Options tab), restricted access to one or more audit reports will prevent the user from
 posting the batch.

Select the links below for more information about using this form.
[Process a Batch](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/batch-processing/process-a-batch)
[About Clearing a Batch](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/batch-processing/about-clearing-a-batch)
