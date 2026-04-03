---
title: "Inventory Transaction Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-entry"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-entry"
---

# Inventory Transaction Entry

The Inventory Transaction Entry is used to enter different
 transaction types: adjustments, transfers, cost adjustments, and receipts.
Once you have completed this screen,
 click the Update button to print
 the [Inventory Transaction Report / Update](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-report--update).
Learn more about each of the transaction types:
 Adjustments Adjustments can be positive or negative, but the negative adjustments may not exceed the quantity on hand. A reason must be provided for each adjustment, for example, "spoilage", "broken", "not usable", "theft", and so forth. In addition to direct entry of adjustments, entries to this file can be made from Physical Inventory File Update and Mix Assembly Transaction Update. Use adjustments to make credit returns, by entering a negative adjustment to one account code and a positive adjustment to a different account code.
 Transfers Record transfers of stock from one warehouse to another. The "oldest" item on hand is removed from the source warehouse when using First-In-First-Out costing method. The "newest" item is transferred when using Last-In-Last-Out costing. In either case, the transferred item becomes the "newest" item in the destination warehouse. You are prevented from transferring more stock than is on hand at the source warehouse; items may not be transferred to a warehouse if the particular item is not yet set up in that warehouse. Protection assures that if multiple G/L inventory account codes are used, the appropriate inventory setup has been performed. In the case where the category code for the item does not contain a G/L account code for the departments specified in the Warehouse File Maintenance screen the software makes sure the codes are valid and not direct cost for Job or Equipment. If the transaction line entered would result in an invalid General Ledger entry, the system will issue an error message and disallow the user to continue until the setup has been corrected.
 Cost Adjustments Cost adjustments are a way to add a dollar amount to an inventory item after it has been updated into Item Detail File Maintenance. A good example is adding a freight amount to an inventory item after it has been posted with the quantity received. A cost adjustment can be entered, which will add a fixed dollar amount to the value of a specific inventory item and therefore increasing the unit cost of that item. The Miscellaneous adjustment does not adjust the quantity in the warehouse; rather, it resets the unit cost for the quantity on hand to reflect the cost adjustment.
 Receipts Record receipt of inventory to the specified warehouse. When updated, transactions created using this screen will appear in Inventory History as Receipts type transactions. If the Purchase Order module is in use and items received have been included on purchase orders, entry here is not necessary. Receipt through the Purchase Order Receiving replaces inventory receipt through this screen.
