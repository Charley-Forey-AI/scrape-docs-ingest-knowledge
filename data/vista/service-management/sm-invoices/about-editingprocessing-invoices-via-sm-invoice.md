---
title: "About Editing/Processing Invoices via SM Invoice | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/about-editingprocessing-invoices-via-sm-invoice"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/about-editingprocessing-invoices-via-sm-invoice"
---

# About Editing/Processing Invoices via SM Invoice

You can use the SM Invoices form to access pending invoices for editing and processing.
Using the Search Criteria in SM Invoices,
 you can filter invoices so that only those invoices you need to work on are displayed in
 the grid. Once you locate the invoice you want to edit, double-click the invoice or
 click the Open button to open the related invoice and make your edits.
For information about processing a single invoice, see [Edit and Process a Single Pending SM Invoice](/en/vista/vista/service-management/sm-invoices/about-editingprocessing-invoices-via-sm-invoice/edit-and-process-a-single-pending-sm-invoice#task-8121--en__task-8121).
For information about processing multiple invoices, see [Edit and Process Multiple Pending Invoices](/en/vista/vista/service-management/sm-invoices/about-editingprocessing-invoices-via-sm-invoice/edit-and-process-multiple-pending-invoices#task-4524--en__task-4524).

## Saving Edits Without Processing

If you edit an invoice but are not ready to process it, you can
 exit the form without losing your changes. First save the invoice, and then either
 click the Close button (below the grid) or the X button in the upper corner of the
 window. Remember that if you are editing multiple invoices in a session, exiting the
 form closes the entire invoice session. Make sure you save all invoices in the
 session before exiting.

## Canceling Invoices

You can cancel an invoice sesstion by clicking the Cancel button
 on a pending invoice (work order or agreement). Once canceled, all invoices in the
 session are deleted. When an invoice is deleted, the following occurs:

- Work Order Invoices - Work
 completed lines associated with the invoice will be flagged with a New
 status and be available for invoicing later (via SM Work Orders or SM
 Work Order Billing). This includes work completed lines associated with
 an agreement-related scope flagged as Time and Materials.

- Flat Price Work Order
 Invoices - The work order is reopened for billing and will be available
 for invoicing via SM Work Orders or SM Work Order Billing. Work
 completed lines for these invoices are not affected, as they are flagged
 as "non-billable" and are not included on the invoice.

- Agreement Invoices - The
 agreement billing is reopened and will be available for invoicing via SM
 Agreement Billings Due.

## Editing Processed Invoices

Once you process an agreement invoice, it is no longer available for editing. You
 can, however, create an adjustment to the invoice via AR Invoice Entry. For work
 order invoices, you can [edit a processed invoice](/en/vista/vista/service-management/sm-invoices/about-editingprocessing-invoices-via-sm-invoice/edit-a-work-order-invoice) at any time. However, once
 you make edits to the invoice, you must either Cancel or Process the changes. You
 cannot "save" the changes like you can for a pending invoice. If you select Cancel,
 only the changes will be canceled; the original information will be left intact. If
 you choose to process the invoice, the SM Batch Process form is displayed, allowing
 you to post the batch. Once you return to the SM Invoices form, the changes will be
 updated to the grid.

Related concepts

- [About the Search Criteria in SM Invoices](/en/vista/vista/service-management/sm-invoices/about-the-search-criteria-in-sm-invoices)

- [About Previewing, Printing, and/or Delivering Invoices](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices)

Related information

- [SM Invoices Form](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoices-form)

- [SM Invoice Review Form](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoice-review-form)

- [SM Agreement Invoice Review Form](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-agreement-invoice-review-form)
