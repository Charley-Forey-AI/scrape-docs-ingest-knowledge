---
title: "Generate & Process Work Order Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/generate--process-work-order-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/generate--process-work-order-invoices"
---

# Generate & Process Work Order Invoices

When you are ready to bill work orders, you can generate an invoice directly from the SM Work Orders form or generate invoices for multiple work orders using the SM Work Order Billing form.
Most invoices for customer work order are generated based on the equipment, labor, material, and/or miscellaneous work completed lines entered for the work order. Other work orders, such as those generated from an agreement or those with flat price scopes, do not require that you enter work completed in order to create invoices. For these work orders, billable amounts are determined by the agreement, agreement service, or the price specified for the work order scope (flat price work orders).Note: For information about how to create and process invoices for agreement-related work orders, see [Generate and Process Agreement Billings](/en/vista/vista/service-management/sm-invoices/generate--process-agreement-billings). For information about how to bill job work orders, see [Billing SM Job Work Orders](/en/vista/vista/service-management/sm-invoices/about-billing-sm-job-work-orders)..

If you selected the Use Review Process checkbox in SM Company Parameters, the following applies:

-  If generating invoices via the SM Work Order Billing form, only items that are ready-to-bill appear in the work orders grid.

- Flat price items are not editable in the Work Order Detail grid at the bottom of SM Work Order Billing

- When authorized reviewers click the Bill WO button to bill a work order, the system asks whether to "Bill all work or only work marked Ready to Bill?"

The following steps detail how to create an invoice session and process invoices for customer and T&M agreement work order scopes.

1. Create an invoice session using one of the following methods:OptionDescription
Using SM Work Orders

1. From the main menu, select Service Management > Programs > SM Work Orders.

1. In the Work Order field, enter the work order for which to create an invoice.

1. Click Bill WO.
The SM Invoice Review form displays.Note: If you selected the Use Review Process checkbox in SM Company Parameters and you are not authorized as a reviewer on the work order, the Bill WO button does not appear.

Using SM Work Order Billing

1. From the main menu, select Service Management > Programs > SM Work Order Billing.

1. In the Work Order Filter section, use any combination of the fields to create a work order filter. Refer to the F1 help for how each field functions.

1. Click Refresh to populate the grid based on selected filter options.

1. Select work orders to bill by clicking Select All or by selecting the Bill checkbox for individual work orders/lines.

Using the SM Work Center

1. From the main menu, click on the desired Service Management work center tab.

1. From the Items menu (left pane), select Work Order Management  >  Billable Work Orders. The Billable Work Orders grid displays.

1. If you are billing a single work order, select the work order line in the grid and select Tasks > Bill Work Order.The SM Invoice Review form displays.

1. The header fields default values based on the customer's setup (in AR Customers). You should not need to change these values; however, with the exception of the Seq field, you can change the default values as needed. For more information about these fields, see the F1 help.Note: If you have an alternate billing address, enter the Alternate Billing Address Sequence number (created in [ AR Customers](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)) into the Alt. Addr: field. Press F4 for an Accounts Receivable Alt Billing Address Lookup form. Press F5 to connect to the AR Customers form where alternate billing addresses are maintained.

1. If you want to apply a miscellaneous cash receipt to the work order, do the following:

1. From the Payment Type drop-down list, select the payment type: A-On Account, C-Cash, or X-Credit Card.

1. In the Payment Amount field, enter the payment amount. This can be a partial payment or a full payment; however, the payment amount cannot exceed the invoice amount.

1. If the Ref Number field, enter the payment reference number, if applicable.

1. Save the invoice header.

1. Review and [edit the invoice lines](/en/vista/vista/service-management/sm-invoices/about-editingprocessing-invoices-via-sm-invoice/edit-a-work-order-invoice) as needed.

1. If you billed multiple work orders with this session, repeat Steps 2-5 for each invoice sequence in the session. If this is a single invoice session, skip to Step 7.

1.  Preview the invoices.You can click the Preview button (to the right of the Invoice Summary Level field to preview the selected invoice or click the Preview All button (bottom of screen) to preview all invoices in the session.

1. Process the invoice(s).

1. Click the Process button. The AR Batch Process form displays.

1. Click Validate. The system validates the information and generates the applicable batch reports.

1. Review and print batch reports (recommended).

1. In the Posting Date field, enter the date to which invoices are to be posted. Initially defaults to the current date.

1. Click Post to initiate the posting process. The system will process each batch entry and make all the necessary transaction updates. In addition, each invoice is updated to a status of Invoiced (from Pending) and any related work completed lines are updated with a status of Billed.

1. [Edit the Recipients list for invoice delivery](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/edit-the-recipients-list-for-sm-invoices) (optional).

1. [Add attachments for invoice delivery via email (optional).](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/addselect-attachments-for-sm-invoice-delivery)

1. Click the Deliver button.Note: If you are not ready to deliver the invoice, you can do so later via the [SM Invoices](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoices-form) form.

 Once you post an invoice, it is available for payment using AR Cash Receipts. You can reprint invoices at any time using the custom reports you chose for each invoice, the SM Invoice report (if no custom report was used), or the AR Invoice report (this option only available for processed invoices)

Related information

- [About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)

- [About the AR Invoice Entry Form](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-invoice-entry-form)

- [About the AR Batch Process Form](/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-batch-process-form)

- [About the AR Cash Receipts Form](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form)

- [About the Ready To Bill Flag](/en/vista/vista/service-management/work-orders/work-order-review-process/about-the-ready-to-bill-flag)
