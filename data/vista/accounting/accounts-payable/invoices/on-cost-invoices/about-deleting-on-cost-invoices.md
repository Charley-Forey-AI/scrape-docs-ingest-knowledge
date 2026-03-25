---
title: "About Deleting On-Cost Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/about-deleting-on-cost-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/on-cost-invoices/about-deleting-on-cost-invoices"
---

# About Deleting On-Cost Invoices

You can delete on-cost invoices in the AP Transaction Entry form. This article applies only to users in Australia.
To delete on-cost invoices, add them to an
 AP Transaction Entry batch just like a regular invoice, select D-Delete
 from the Action drop-down, and process the batch. However, because on-cost
 invoices are based on an original subcontractor/vendor invoice there are some
 differences in the process.
If you attempt to delete the original subcontractor invoice, and there are associated on-cost invoices that have not been posted yet, the system will not allow you to delete the original invoice. You must first delete the associated on-cost invoices before deleting the original invoice. However, you must first add the on-cost invoices into a batch and delete them prior to adding the original invoice into a batch for deletion. You cannot delete the original invoice and all of its associated on-cost invoices in the same batch.
Tip: Run the AP On-Cost Invoices report to identify the on-cost
 invoices that are associated with the original subcontractor
 invoice.
If you add an original subcontractor invoice back into a batch, and it has associated on-cost invoices that have been posted, the system will display red text warnings in AP Transaction Entry. In this case, you should not delete the invoices.
When deleting an on-cost invoice, the system will
 automatically reset the on-cost processing status on the original subcontractor invoice
 to "waiting." This means that the original invoice will be available for review when
 adding invoices to AP On-Cost Workfile.
If there are multiple on-cost invoices associated
 with the original invoice, the original invoice's on-cost processing status will remain
 as "processed" and will not display in AP On-Cost Workfile.
