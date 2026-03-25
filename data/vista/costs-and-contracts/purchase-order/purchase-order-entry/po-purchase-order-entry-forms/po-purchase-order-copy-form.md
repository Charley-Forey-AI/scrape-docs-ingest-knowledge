---
title: "PO Purchase Order Copy Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-copy-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-copy-form"
---

# PO Purchase Order Copy Form

Use this form to copy existing purchase orders to new purchase orders.
Access this form via the PO Purchase Order Entry form by selecting File > Copy Purchase Order.
Copying purchase orders is particularly useful if you have one or more standard PO's that are commonly used, and want a way to streamline repetitive entries.

## Destination PO

You can specify either an existing PO or a new PO as the destination purchase order. If the destination PO is a new purchase order and you are using the 'auto generate' feature (flag in PO Company Parameters), entering 'NEW' or '+' will allow the system to auto assign the next sequential number available (based on the Last PO# in the company file). If you specify an existing PO, only POs currently in the batch are eligible.
Once you enter the destination PO, the header fields automatically default information from the source PO, such as the vendor, description, ordered by, JC Co, job, IN Co, and location. You can change the defaults as necessary.

## Destination PO Item Type

This section is only enabled if the source PO has 4-Equipment or 5-EM Work Order lines. You must specify whether to copy the work order and/or equipment lines, and if so, whether the destination PO is for the same work order and/or equipment or a different work order and/or equipment. If different, select the appropriate Override checkbox and enter the new information.
Note: If you are copying multiple work order and/or equipment items, all items will be assigned to the same work order or equipment, regardless of whether they were originally assigned to different work orders or equipment.

## Destination PO Items

This last section is used to change specific information for the PO items. Specify whether to keep the pricing from the source PO or whether to use the pricing from the appropriate sources.
The Set Quantities to one option allows you to specify whether to use the source quantities or to set each item's quantitiy to '1' on the new PO. You also have the option to copy item notes and/or user memos. If there are no user memo fields on the Memos tab (Items section), the Clear Item User Memos cleared and disabled. If you are copying to a purchase order in the current batch, these fields default from the destination purchase order and are disabled.
The Items grid displays all items from the source PO. The Incl checkbox allows you to specify which items you want copied to the new PO. Initially, all items default as selected, so you must manually deselect all items you do not want copied. This applies also to work order and/or equipment items. Although selecting the checkbox allows these items to be copied, they will only be copied if the Incl checkbox is selected.
Once you have specified the copy criteria, select the Copy button to initiate the copy process. When complete, a message informs you of what was copied, and provides the option to copy additional PO's. If you select No, you are exited from this form and returned to the Purchase Order Entry form, where you can edit and process the purchase orders as normal.
