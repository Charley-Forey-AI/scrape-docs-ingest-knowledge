---
title: "SM Invoice Review Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoice-review-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoice-review-form"
---

# SM Invoice Review Form

Use the SM Invoice Review form to edit, preview, and post SM invoices for customer work orders.
Note: This form is for customer work orders only. For Job work orders, you must use Job
 Billing or Accounts Receivable; you cannot bill job work orders in Service
 Management.

You can access this form using any of the
 following methods:

- In SM Work Orders, click the
 Bill
 WO button (new invoices) or double-click an existing invoice in
 the Invoices grid.

- In SM Work Order Billing, select the Bill checkbox for the desired
 work order and click the Launch Invoice Review
 button.

- In SM Work Completed Equipment, SM Work Completed Labor, SM Work Completed Misc, SM
 Work Completed Inventory, or SM Work Completed Purchase, click the Edit
 Invoice button.

- In SM Customers or SM Service Sites, select the Invoice grid and then double-click
 on a selected Work Order invoice.

- In SM Invoices, double-click on the desired Work Order invoice in the grid.

For most customer work orders, invoices can
 only be created once you have captured work completed, since work completed lines are
 used to determine the billable amounts. However, work orders with Flat Price scopes do
 not require entry of work completed, since billable amounts are determined by the
 scope's flat price amount.

## Receivable Types

Receivable types are automatically assigned to SM invoices during the creation of the
 AR invoice batch (when you click the Process button). The system uses the Default
 Receivable Type assigned to the SM company (in SM Company Parameters). If you did
 not assign a receivable type in SM company, the system uses the receivable type
 assigned to the invoice's Bill To customer (in AR Customers) or the default
 receivable type defined in AR Company Parameters (if no receivable type is defined
 for the Bill To customer).

## No Charge Invoice Items

The No Charge checkbox allows you to flag items on an invoice that you will not
 charge the customer for, but still want shown on the invoice. Invoice lines with
 this checkbox selected will print on the invoice with all of it's values; however,
 the item's total will show as "No Charge" and will not be included in the invoice
 total.Note: You can only set this flag for an
 invoice line (not associated with a Flat Price work order scope) using the work
 completed form. If you are not charging the customer for work completed and do
 not want the information shown on the invoice, remove the line using the Remove
 Line button.

## Preview / Preview All

The Preview options allow you to view invoices before you process them. If you
 generate invoices using the SM Work Order Billing form (which allows billing
 multiple work orders at one time), use the Preview button to view the currently
 selected invoice and the Preview All button to see all invoices in the batch. If you
 are using multiple invoice formats, the system will display a different preview
 screen for each unique Custom Invoice Report. Invoice using the same custom invoice
 format will display in the same preview screen. Invoices using the standard invoice
 report will display in a separate preview screen. For invoices generated
 individually by work order (in SM Work Orders), both preview options work the
 same.Note: It is recommended that you preview
 all invoices to ensure that your invoice data is correct and that invoices are
 printing in the correct format. Once you process an invoice, you cannot change
 the invoice format.

## Processing SM Invoices

When you click the Process button, the system creates an AR Invoice Entry batch and
 displays the AR Batch Process form. You will need to validate the batch, print the
 audit reports, and process the batch in the same manner as you would for any invoice
 created directly in AR Invoice Entry. Once you process an invoice batch, the system
 updates the invoice status to "Invoiced" and each applicable work completed line to
 "Billed".Note: Invoices generated using this
 form will have a Source of SM Invoice and can only be processed via this form;
 they cannot be processed by selecting the AR Batch Process form in the Accounts
 Receivable module.

Related information

- [Generate & Process Work Order Invoices](/en/vista/vista/service-management/sm-invoices/generate--process-work-order-invoices)

- [Edit the Recipients List for SM Invoices](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/edit-the-recipients-list-for-sm-invoices)

- [Edit a Work Order Invoice](/en/vista/vista/service-management/sm-invoices/about-editingprocessing-invoices-via-sm-invoice/edit-a-work-order-invoice)

- [Use the Invoice Delivery Feature](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature)

- [Apply a Payment When Invoicing an SM Work Order - Video](/en/vista/vista/videos/service-management/apply-a-payment-when-invoicing-an-sm-work-order---video)

- [About Billing SM Job Work Orders](/en/vista/vista/service-management/sm-invoices/about-billing-sm-job-work-orders)

- [About SM Work Order Cost Adjustments](/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments)
