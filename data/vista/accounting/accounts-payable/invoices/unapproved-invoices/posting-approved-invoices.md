---
title: "Posting Approved Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/posting-approved-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/posting-approved-invoices"
---

# Posting Approved Invoices

To post unapproved invoices, use the AP Unapproved Invoice Posting form to start your batch. You can set filtering criteria to bring specific invoices into the batch. Although you can add invoices to the batch from any month, the system expenses them in the specified batch month.

To post unapproved invoices to an AP Transaction Entry batch:

1. Enter the month and year
 associated with the invoices you want to post in the Include Invoices
 entered for Month field, or accept the default of the current batch
 month.

1. If you want to restrict posting invoices by vendor, select the Restrict by Vendor checkbox and enter the name of the vendor in the Vendor field or press F4 for a list of vendors. If you want to restrict by sequence number, select the Restrict by Seq# checkbox and enter a range of sequence numbers.

1. If you want to restrict by pay control code, select the Restrict by Pay Control checkbox and enter the pay control code in the Pay Control field. 

1. If you want to restrict by the person responsible for the unapproved invoice, select the Restrict by Responsible Person checkbox and enter the responsible person in the Responsible Person field or press F4 to select from a list. Click Update to add invoices to the batch. The system displays all invoices meeting the filter criteria in the grid, and clears the filtering criteria fields. The system only adds invoices that all associated non-optional reviewers (and [optional reviewers](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form/field-definitions-hq-reviewer-groups-form#ID-0000f72b--en), as needed) have approved. The system also will not add invoices with missing information, or ones whose vendors are out of compliance.
There may be other reasons an approved invoice is not being updated to the batch. Run the AP Unapproved Invoice Update Check report to determine the cause, make corrections or changes, and rerun the batch update if applicable.

1. Repeat the process with other filters to add additional invoices to the batch, as necessary. Important:If you need to add addenda information to invoices with EFT pay method, stop here by pressing Cancel , but click No to clearing the batch. Open the AP Transaction Entry form, locate and open the batch you just created, and use it to add the addenda information to the appropriate invoices. Then post and process the batch as normal.

1. Click Post to post the invoices. The system displays the AP Batch Process form.

1. [Process the batch](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/ap-maintenance-forms/ap-batch-process-form) as normal. Note:

- If you do not allow transactions to exceed the total cost of subcontracts or
 purchase orders (AP Company Parameters, Audit Options tab), any transactions
 in the batch exceeding the total cost of a purchase order item/purchase
 order and/or subcontract item/subcontract will need to be corrected (in AP
 Transaction Entry) before you can process the batch.

- If more than one reviewer group is associated with an invoice, the
 responsible person for the group on the line must be used as filter
 criteria.

- If the transaction is related to a job and you do not allow posting to
 closed jobs (that is, the Allow Posting to Hard-Closed
 Jobs and/or Allow Posting to Soft-Closed
 Jobs boxes are unchecked in JC Company Parameters), you will
 be unable to post the batch. (You will be able to validate the batch, but
 the error report generated will indicate the job is closed.)
