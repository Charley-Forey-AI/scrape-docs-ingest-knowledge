---
title: "Close POs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/close-pos"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/close-pos"
---

# Close POs

You can close purchase orders and relieve the remaining committed units/dollar amounts in Job Cost and On Order quantities Inventory using the PO Close form.
In order to close a purchase order, the following must apply:

-  Received and Invoiced amounts must be equal

-  The PO cannot have any AP transactions, PO change orders, or PO receipt detail posted to it in a month later than the proposed close month.

During the close process, the system closes any PO with a complete status, any open PO that is fully invoiced, and any PO with backorders. Closing the PO removes any remaining units and dollar amounts from all items on the PO,and backorder amounts, if applicable.For detailed information about each of the fields, see the F1 Help.

1. Open the PO Close form. This is a batch process, so you will have to select an existing PO Close batch or create a new one before the form will open.

1. Select the POs that you would like to close using the fields in the Select POs to Close section.For example, to close POs for a specific vendor, select the Restrict by Vendor checkbox and enter the vendor the Vendor field.Note: If you do no select any of the options, the system selects all POs that are eligible to be closed.

1. Select the Include open standing POs checkbox to close open standing POs (non-LS POs with 0.00 units) without first marking them as complete.

1. Select the Include POs with Backorders checkbox to close purchase orders with remaining backorder units/amounts.

1. In the Close Date field, enter the close date to apply to all selected purchase orders.

1. Select the Update  button.All POs matching the selected criteria display in the grid below.

1. In the grid, remove any POs that you do not want to close by highlighting the row and pressing Delete.To clear the PO close batch, select Cancel.
The selected POs are removed from the PO Close batch only; they are not deleted.

1. Select Close POs.The PO Batch Process form opens.

1. Validate the batch, generate audit reports, and process the batch.


 The close process sets all Backordered amounts to 0.00 and relieves any Remaining Committed Units and Costs in Job Cost and On Order units in Inventory. The status is set to Close for each PO and the Month Closed is updated with the selected close date.Note: You can reopen any PO closed in the PO Close form by changing the status from "Closed" to "Open" in PO Purchase Order Entry. Be aware however, that reopening a purchase order does not reset any of the backordered units or costs, remaining committed costs, or on order units to the amounts that existed prior to closing the purchase order. Original, current, received, total, and invoiced amounts will still show pre-existing amounts.
