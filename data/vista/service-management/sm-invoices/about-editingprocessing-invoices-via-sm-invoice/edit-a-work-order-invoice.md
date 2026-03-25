---
title: "Edit a Work Order Invoice | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/about-editingprocessing-invoices-via-sm-invoice/edit-a-work-order-invoice"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/about-editingprocessing-invoices-via-sm-invoice/edit-a-work-order-invoice"
---

# Edit a Work Order Invoice

You can edit both pending and processed work order invoices using SM Invoice Review.
 Once you [generate a work order invoice](/en/vista/vista/service-management/sm-invoices/generate--process-work-order-invoices) (via SM Work Orders or SM Work Order Billing), you can edit the invoice as needed before you process it. Using the SM Invoice Review form, you can edit the header information for an invoice, remove invoice lines you are not ready to invoice, and access the appropriate form to make changes to the information on an invoice line.After you process an invoice, which sends it Accounts Receivable, edits are limited. In addition, because AR does not update SM, edits to the invoice must be made using the SM Invoice Review form (rather than in AR Invoice Entry).

1. Open the invoice to edit in SM Invoice Review using one of the following methods:

- From SM Invoices, by double-clicking on the desired Work Order invoice in the grid

- From SM Customers, by selecting the Invoices tab and double-clicking on the desired Work Order invoice

- From SM Service Sites, by selecting the Invoices tab and double-clicking on the desired Work Order invoice

- From SM Work Orders, by selecting the Invoices tab and double-clicking on the desired Work Order invoice

1. Edit the header information as applicable.Note: If you are editing a processed invoice and the original posting month has been closed, you will need to enter a new post month (must be an open month) before you can process the invoice.

1. To edit an invoice line for a non-flat price work order:

1. In the Lines grid, select the invoice line sequence to edit.

1. Click Edit Record. The applicable Work Completed form opens (e.g. if you selected a Labor line, the SM Work Completed Labor form opens).

1. Edit the work completed record as needed.The edits allowed will depend on the work completed line type. See the F1 help for more information.

1. Save the work completed record and close the form.You are returned to the SM Invoice Review form.

1. To edit an invoice line for a flat-price work order:

1. In the Lines grid, select the invoice line sequence to edit.

1. Click Edit Record. The applicable Work Completed form opens (e.g. if you selected a Labor line, the SM Work Completed Labor form opens). The SM Invoice Flat Price Change form opens.

1. Edit the Description or Billing Amount as needed. See the work completed record as needed.The edits allowed will depend on the work completed line type. See the [F1 help](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoice-flat-price-change-form) for more information.

1. Save the work completed record and close the form.You are returned to the SM Invoice Review form.

1. To delete an invoice line:

1. In the Lines grid, select the invoice line sequence to delete.

1. Click Remove Line. This removes the line from the invoice, but leaves it available for invoicing later.

1. [Edit the Recipients list](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/edit-the-recipients-list-for-sm-invoices) (optional).

1. Click Process.

 The invoice is posted and sent to Accounts Receivable.Note: If you edited an invoice that was already processed, reprocessing the invoice creates an AR adjustment transaction (negative or positive) and applies it against the original invoice, the same as if you entered an adjustment directly in AR Invoice Entry.If you changed the tax information for a work completed invoice line, the update process will back out the last record created in ARTL (AR Transaction Lines) for the work completed line, netting the record to 0.00. It will then create a new record with the updated tax code information. If you changed the tax information for a flat price line, changes to the tax amount will occur automatically when you change the billing amount.
