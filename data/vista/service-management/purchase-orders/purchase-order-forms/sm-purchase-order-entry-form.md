---
title: "SM Purchase Order Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form"
---

# SM Purchase Order Entry
 Form

Use the SM Purchase Order Entry form to enter purchase
 orders for an SM work order.
You can access the SM Purchase Order Entry
 form by selecting the Create PO button in SM Work Orders.
Note: The Create PO button is enabled only if work
 order has not been closed or canceled.
When you need to purchase materials for a
 work order, using this form allows you to get a purchase order in the system with minimal
 information, and without leaving the work order. Information not initially entered on the
 PO can be entered later when more details about the purchase are available.
Once you finish entering a purchase order
 and save the record, the system automatically creates a PO entry batch. If you assigned a
 vendor to the purchase order, the system posts the batch and generates a work completed
 purchase line (in SM Work Orders, Work Completed tab). If you did not assign a vendor, the
 batch remains open and flagged with a status of 'Reserved'. You can access the purchase
 order in either SM Purchase Order Entry or PO Purchase Order Entry for editing. The work
 completed purchase line will not be generated until you assign a vendor and post the
 batch.
Note: If you did not assign a rate template to the work
 order scope specified for the PO Item you can still save the work order; however, you must
 assign a rate template in order to invoice the purchase order (in AP Transaction
 Entry).
You can edit purchase orders (either using this form or PO Purchase
 Order Entry), as long as you have not received or invoiced the PO. All changes are updated
 to the related work completed purchase line. Once you receive or invoice the purchase
 order, only the Description, Units, Req Date, Pay Category, and Pay Type fields may be
 modified.Note: If you selected the Receiving checkbox for a PO item, you
 can receive the PO using PO Receipts Entry. If you did not select the Receiving
 checkbox, the system will auto-receive the PO during invoicing in AP Transaction Entry.


You can see cost information for each purchase order item using the Cost tab; however,
 values are not populated until you close and reopen the form. Once you receive a purchase
 order item (via PO Receipts Entry, PO Initialize Receipts, or AP Transaction Entry), the
 system updates the received, back ordered, invoiced, and remaining values accordingly.
Select the links below for more information.
[Enter POs in SM Purchase Order Entry](/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/enter-pos-in-sm-purchase-order-entry)
[About Tracking Compliance](/en/vista/vista/service-management/purchase-orders/about-tracking-compliance#concept-9592--en__concept-9592)
[About Purchase Orders for Job Work Orders](/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/about-purchase-orders-for-job-work-orders#concept-8838--en__concept-8838)
[About PO Item Distribution](/en/vista/vista/service-management/purchase-orders/about-po-item-distribution)

Related information

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)

- [PO Company Parameters Form](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)

- [PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

- [PO Vendor Materials Form](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-vendor-materials-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
