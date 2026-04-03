---
title: "Purchase Order Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry"
---

# Purchase Order Entry

The Purchase Order Entry screen is
 used to record purchase orders.
Purchase orders may be recorded for negative quantity when material is being returned to
 the vendor. When negative purchase orders are received, a credit memo results in Accounts
 Payable.
The Purchase Order and Work Order modules enable material purchases to
 transfer from the purchase order into the work order material file. As items are received
 on purchase order, the associated work order can be modified automatically. Based on the
 Auto-set dispatch status and priority of fully received Work Orders setting in the Work Order Installation > Dispatch tab, if you are receiving or closing a purchase order and the corresponding
 work order is fully received, then the dispatch status and priority will automatically be
 updated. This eliminates the need to rely on material information already recorded in
 Purchase Order Entry. (The lines do not actually transfer until
 the Work Order Material Entry page is accessed for the given work
 order.)
Watch the following video to learn more about the Purchase Order Entry and Receiving process:

The Payment Terms fields and Terms Discount column is 'display only' if the operator doesn't have the correct security authorization for PO Entry - Payment Terms.

## Note regarding Lump Sum Purchase Orders

If the purchase order pricing type is set to lump sum, the quantity ordered is always '1' (display only), and users are only allowed to record non-stock items. The quantity received column will be hidden, as it is not applicable to lump sum purchase orders.

## Note regarding P.O. Receiving Report

On the Detail format of the P.O. Receiving Report, when From/To delivery date range is entered, the report is pulling the information from the estimated Delivery Date entered on this screen. If the date field is blank, then the purchase order will not be included on the report.

## Note regarding Proposed Purchase Orders

If the Workflow module is installed and active in this company, proposed purchase orders will display on the Workflow info bar. The Currently Assigned To You section will show all proposed purchase orders that are assigned to you and require action. Click the tooltip icon to search current workflow assignments and switch to a different proposed purchase order.
The info bar will display the assignment, due date, instructions, notes & history, and action buttons specific to the purchase order (Completed and Back buttons for steps marked FOR COMPLETION, and Approve and Reject buttons for steps marked FOR APPROVAL). The action buttons will only display if the current operator is assigned to this step, or is an override operator for this workflow. After the operator clicks an action button, the system will open the next pending workflow assignment (if applicable). Proposed purchase orders awaiting further action will display on the My Current Workflow Assignments dashboard app until completed.

## Spectrum Financial Controls

If you have access to this screen through Spectrum Financial Controls, use this [cheat sheet](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/93196e10-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiI5MzE5NmUxMC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjY4NTUsImp0aSI6IjhjNjI3Yzg3YzViYjRiMTg4YTUyZWU5MTI4NTExMjY1IiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.bsNNHeKV9kx-zSPsQkB1OdHPGP6OsJFBpbQG7XfLeE8&response-content-disposition=filename%3D%22Spectrum_Purchase_Order_Entry.pdf%22) to learn the basics of Purchase Order Entry.

Related information

- [Creating Purchase Order Revisions](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/creating-purchase-order-revisions)

- [Integrating Purchases with a Work Order](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/integrating-purchases-with-a-work-order)

- [Issuing a Lump Sum Purchase Order](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/issuing-a-lump-sum-purchase-order)

- [Reopen a Closed Purchase Order](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/reopen-a-closed-purchase-order)

- [Accruing Job Purchase Orders](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/accruing-job-purchase-orders)

- [Purchase Order Entry - Cost Center Field Hierarchy](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/purchase-order-entry---cost-center-field-hierarchy)
