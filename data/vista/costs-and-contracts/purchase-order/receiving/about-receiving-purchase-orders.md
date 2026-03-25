---
title: "About Receiving Purchase Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/receiving/about-receiving-purchase-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/receiving/about-receiving-purchase-orders"
---

# About Receiving Purchase Orders

Once you create a purchase order, you can receive the purchase order in the PO module or
 you can just invoice it in the AP module.

- PO Module - Receiving purchase orders
 in the PO module allows you to enter shipments received in the PO module and immediately
 update the inventory on hand in the Job Cost module. This feature is also useful if you
 want to make month-end accrual entries based on the items that you have received, but not
 invoiced.

- AP Module - You can also skip receiving
 purchase orders in the PO module. Once a PO has been entered, you can invoice it using the
 AP module. You can then close the purchase order using the [PO Close](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form) form once all
 of the units on the PO have been invoiced, or you can create a change order for the units
 that have not been invoiced.

## Receiving PO in the PO Module

Receiving POs in the PO module has four steps, which are outlined below.

1. Create the PO - When creating PO items, make sure that they are
 set up to be received in the PO module. For example when creating a PO item in PO
 Purchase Order Enter, make sure that the Receiving
  box in the lower portion of the form is checked on all PO items that should
 be received in the PO module.

1. Distribute PO Items (Optional) - You can distribute PO Items
 into multiple lines using the PO Item Distribution form. This gives you the ability to
 redirect the costs on a PO item to a different job, phase, cost type, or even line type
 when it is received. For more information, see [PO Item Distribution Overview](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-item-distribution-overview).

1. Record the Receipt - You can use the [PO Initialize
 Receipts](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-initialize-receipts-form) or [PO Receipts Entry](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form) form to receive purchase orders. You will typically use the
 initialization method when you have a large number of receipts in a single batch, and
 then use manual entry when you want to receive a small number of receipts or need to
 edit existing receipts.Note: When you enter receipt, you are entering them against the PO item lines, not the
 PO items. Changes to the units/amount received, and the backordered units/amount
 will affect the PO item line.

1. Post the Batch - After you have entered the receipts, you need
 to post the batch. You can do this by selecting File > Batch  from either PO Initialize Receipts or PO Receipts Entry, which opens the
 PO Batch Process form, allowing to validate and process the batch.

Once you post the receipts, you can invoice the received amounts using the AP module. By
 default you cannot invoice more than what has been received. However, the Audit
 Options tab on the AP Company Parameters form includes setup options that allow you to
 invoice more than what was received
When you post receipts for Inventory and Job POs, the
 Received Not Invoiced field tracks goods that have been received
 but not invoiced (in AP). Once you process the invoice in AP Transaction Entry, this field
 is relieved and transferred to the actual/invoiced field. For Inventory POs posted in PO
 Receipts Entry, the amount On Order is reduced and the Received Not Invoiced amount is
 increased. This in turn updates the On Hand quantity in Inventory.
Receipts posted to purchase orders for SM work orders
 automatically update the received units/costs for the corresponding work completed purchase
 lines in SM Work Orders (Work Completed tab). Additionally, if you elected to update
 GL/subledgers on receipt (option in PO Company Parameters), the system adds a cost entry to
 the Posted Detail grid (SM Work Orders) for each work completed purchase line.

## Invoice POs in the AP Module

If you don't want to receive a PO in the PO module, leave the Receiving checkbox cleared when creating the PO
 items. When the PO is invoiced using the AP Transaction Entry form, the Received and
 Invoiced amounts are both updated, but the Received Not Invoiced fields in JC and IN are not
 updated.
