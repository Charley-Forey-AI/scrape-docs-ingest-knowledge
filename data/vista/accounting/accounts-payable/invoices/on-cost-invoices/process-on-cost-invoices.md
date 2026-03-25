---
title: "Process On-Cost Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/process-on-cost-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/process-on-cost-invoices"
---

# Process On-Cost Invoices

A high-level overview of processing on-cost invoices with
 links to more detailed information.
Once you have set up on-cost invoicing, the system generates on-cost invoices based on the original invoice that you paid to the subcontractor for their work.

1. Enter an invoice for the subcontractor in the AP Transaction Entry form (see [Entering Accounts Payable Invoices](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/enter-accounts-payable-invoices)). You can also review [recurring](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices) or [unapproved](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-unapproved-ap-invoices) invoices that are ready to be processed.Note: If you have set the subcontractor as subject to on-cost (you
 checked the Subject to
 On-Cost box in AP Vendors, Add'l Info tab), the
 system will check the Subject to
 On-Cost box for each invoice line in AP
 Transaction Entry. If you have specified a specific JC cost type
 for on-cost invoice job line associated with the subcontractor
 (JC Cost Type
 field in AP Vendors, Add'l Info tab), the system will compare the
 line's cost type with AP Vendors. If the cost types match, the
 Subject to
 On-Cost box for the invoice line will remain
 checked. If they do not match, the system will uncheck the box
 for the job invoice line. This means that on-cost invoices will
 not be generated for the line.

1. [Process and post the invoice batch](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/ap-maintenance-forms/ap-batch-process-form) as
 normal. All invoices with lines that were set to subject as on-cost will be
 available for review in the AP On-Cost Workfile form, and will be set to an on-cost
 status of Awaiting Process (On-Cost Status field).

1. [Add invoices](/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/add-multiple-invoices-to-the-on-cost-workfile) to the AP On-Cost Workfile form and [review each invoice line](/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/review-invoice-lines-in-the-on-cost-workfile).Tip: You can also run the AP On Cost Pending Invoices report to view invoice/transaction lines that are subject to on-cost processing prior to processing on-cost invoices.

1. Set the on-cost action for each invoice line appropriately using the

 On-Cost Action drop-down in the AP On-Cost Workfile form. For more information on this field, click [here](/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/ap-on-cost-invoice-forms/ap-on-cost-workfile-form/field-definitions-ap-on-workfile-form#ID-0000611a--en).

1. From the AP On-Cost Workfile form, create an on-cost batch by clicking Create On-Cost Batch.The Batch Selection form displays.

1. [Select the batch](/en/vista/vista/system-tools/user-interface-guide/system-forms/batch-processing/about-the-batch-selection-form) you wish to use and
 click OK. The AP Transaction
 Entry form displays. The system groups all payments to an on-cost
 vendor onto a single invoice, regardless of the original invoice's vendor.

1. From the AP Transaction Entry form, run the AP On-Cost
 Reconciliation by Batch report by selecting Options > Reports > AP On-Cost Reconciliation by
 Batch. This report displays the on-cost invoice along with the
 associated original subcontractor invoices; the data for this report is
 similar to the data shown in the AP On-Cost Workfile form prior to creating the On-Cost
 batch.Note: Since the report relies on batch
 data that will no longer available after the batch has been posted, it
 is recommended that you print the report, or export it to a file, for
 later reference.

1. Modify the invoices/transactions as necessary and then [process and post the batch](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/ap-maintenance-forms/ap-batch-process-form) as normal.

1. Continue with the normal [payment posting process](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/process-ap-invoices).Note: If you have set the subcontractor
 as subject to on-cost (you selected the Subject to On-Cost checkbox in the AP Vendors form,
 Add'l Info tab), the system selects the Subject to On-Cost checkbox for each invoice line
 in the AP Transaction Entry form. If you have specified a specific JC
 cost type for on-cost invoice job line associated with the
 subcontractor (JC Cost Type field
 in the AP Vendors form, Add'l Info tab), the system will compare the
 line's cost type with AP Vendors. If the cost types match, the
 Subject to On-Cost
 checkbox for the invoice line remains selected. If they do not match,
 the system clears the checkbox for the job invoice line. This means
 that on-cost invoices will not be generated for the line.
