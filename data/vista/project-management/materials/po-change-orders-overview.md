---
title: "PO Change Orders Overview | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/po-change-orders-overview"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/po-change-orders-overview"
---

# PO Change Orders Overview

Purchase Order Change Orders (POCOs) are used to record changes in scope to approved
 purchase orders, such as additions/subtractions to existing items or the creation of new
 items.
In order to create a change order for a purchase
 order, the purchase order must be approved; however, it does not need to be interfaced
 to the accounting modules.
Note: Purchase orders are approved using the Approve
 checkbox on the Info tab of the PM Purchase Orders form, and they are interfaced with
 the accounting modules using the PM Interface form.
You can also create a PO change order using the PO
 Change Order Entry form in the PO module; however changes made to a purchase order in PO
 are not available in the PM module. By entering the POCO in the PM module and then
 interfacing it with the PO module, the PO change is available in both the PM and PO
 modules.
Creating and processing a POCO has four basic steps, which are almost identical to the steps for processing a subcontract change order(SCO).

## Step 1 - Create the PO Change Order

You can create PO change orders using
 one of the following methods:

- Manual
 Entry - You can manually create a POCO using PM PO Change
 Orders. You can then process it and interface it to the accounting modules
 or you can associate it with a pending change order detail item using the
 PO Change Order and PO Change Order Seq
 fields on the Estimate/Purchase Details tab of PM Pending Change Orders.

- From a
 PCO - When creating a pending change order using PM Pending
 Change Orders , you can associate a PCO detail item with an existing and
 approved PO using the PO and PO/SL
 Item fields on the Estimate/Purchase Details tab. Once a PCO
 detail item is associated with a PO, you can create a POCO in two ways:

- Automatically on Approval - When the pending change
 order is approved, the PCO detail will be used to automatically
 create a POCO. pending change orders are approved using the PM
 Approve PCOs form.

- Manually before Approval - You can also manually
 create a POCO using the detail already entered on a PCO item - for
 example if you need to create a POCO document before the pending
 change order is approved. Select Create PO Change Order in PM Pending Change Orders.
 This will open the PM PCO Items Create PCOs form.

- Using PM
 Material Detail - You can manually create a new POCO using
 the POCO Num field on the PM Material Detail form. However,
 this only applies to material detail that is associated with a purchase
 order.

- Using PM
 Purchase Orders - You can manually create a new POCO using
 the POCO Num field on the Non-Interfaced tab of the PM Purchase
 Orders form.

The line items on the PO change order
 can change an existing PO line item or create a new item on the selected PO.

## Step 2 - Create and Send the PO Change Order Document

Use the Create and Send feature to
 generate a PO change order document and email/fax it to a list of contacts. This is
 an optional step. For more information about the Create and Send feature, see [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature).

## Step 3 - Approve the PO Change Order

Before you interface a PO change order,
 it must be approved. You can either approve all items on the PO change order by
 clicking the Approve button or approve individual items by
 selecing the Interface checkbox for each applicable item,
 and then selecting the Ready for Accounting checkbox on the
 header Info tab.

## Step 4 - Interface the PO Change Order

Interface the PO change order with the
 accounting modules using the PM Interface form. You can access this form from the PM
 PO Change Orders toolbar by selecting Tasks > Open PM
 Interface.
You cannot interface the PO change order
 before the original PO has been interfaced.

Related information

- [Material Buyout Overview](/en/vista/vista/project-management/materials/material-buyout-overview)

- [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)
