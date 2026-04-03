---
title: "Packing List Quantity Entry - field descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/packing-list-quantity-entry/packing-list-quantity-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/packing-list-quantity-entry/packing-list-quantity-entry---field-descriptions"
---

# Packing List Quantity Entry - field descriptions

Use the table below for assistance when completing the fields on this screen.
Field/ButtonDescription
Purchase orderEnter the number of the purchase order being received. Vendor information is displayed based on data from initial entry of the Purchase Order Entry. If the purchase order status is set to 'Proposed' or 'Closed', or if the receiving method is set to one-step, the operator will be disallowed from proceeding.

SequencePress Enter for the default sequence number, or enter the number desired. This field is used to distinguish partial receipt of orders. For example, the first shipment is numbered 001. If the entire order were received, this would be the only sequence number. However, if some items are back-ordered, the completed portion of the order is recorded first, and then when the remaining items arrive they are recorded under sequence number 002.

Receipt dateEnter the date that the materials being recorded were received. If the Two-step with pack list update option is selected in the Purchase Order Installation screen, this date will be validated against the minimum and maximum processing dates for the Purchase Order module.
The date in this field is used as the purchase order's closed date when two-step receiving is used. If you close a purchase order during two-step receiving, the last Received date is used for the Closed date. If a previous Received date does not exist, then the Order date is used.

Pack list #Enter the vendor's packing list number.
RemarksEnter any desired remarks.
Receive in full?If a new packing list is being added, this checkbox will be available. If the checkbox is selected, the current quantity due information defaults in the This pack list qty received field on the grid. Once selected, this option cannot be un-selected.
Scheduled releaseIf a new packing list is being added and there are already scheduled dates for the selected purchase order, this field will be available. Enter the schedule release for this order.This field will be disabled in the Receive in full checkbox is selected.

StatusThe status of the purchase order displays in this field.
Job / Work Order / WarehouseThe job, work order or warehouse code will display in this field if specified in the purchase order header.
Details
Item codeThe item code and description displays.
UmThe unit of measure and description (if any) for the item displays.
Original ordered qtyThe number of items originally ordered displays.
Other receiptsThe number received on other shipments of this purchase order displays. Click the lookup icon to the right of this field to open the Receipts Inquiry window. This window is used to view detailed information regarding a purchase order for a specific job.

Current quantity dueThe quantity now due displays. This figure is calculated by Spectrum as the difference between the original quantity ordered and the quantity on prior receipts.
This pack list qty receivedNote: This warning can display only if the Warning for partial receipt in P.O. packing list checkbox is selected on the Purchase Order Installation - Properties tab.
Enter the number received in this shipment. If the amount entered here is less than the Current quantity due amount, then a warning message displays to let you know that a back order will be created. Click OK to proceed.
Additional descriptionIf the two-step receiving method was selected for this purchase order, the first line of the description from the Purchase Order details window will display in this field.
Unit costNote: These fields appear only if the Display received dollar amount in P.O. packing list entry checkbox is selected in the Purchase Order Installation screen - Properties tab.

 Displayed amounts are derived from costs given in the PO.

- Unit cost displays when you access the screen.

- Extension populates once you enter the received quantity.

Extension
