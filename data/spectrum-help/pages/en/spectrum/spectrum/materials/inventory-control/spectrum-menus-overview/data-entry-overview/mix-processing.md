---
title: "Mix Processing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/mix-processing"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/mix-processing"
---

# Mix Processing

The Mix Processing screen is used to record transactions whenever a mix is produced, taking two or more inventory stock items and combining them to create a unique new stock item. "Component" items are assembled to create a "mix" item. The full cost basis of the component item is transferred to the newly mixed assortment item. In addition, during processing, quantities on hand of component items are reduced as quantities on hand of mixed items increase. No change in total inventory value occurs as a result of mix processing; but, following assembly, "cost" is associated with the mix item. This provides a simple method of building "mixes".
Think of "mix" items as the separate ingredients in a cake: eggs, flour, vanilla, and more. When these ingredients are mixed together, they create a new product: cake. Similarly, each individual mix component is entered in Mix Maintenance and used whenever a mix is produced using this screen.
The G/L entry resulting from the mix assembly is based on the G/L department stored for each component and parent item. If no G/L department is designated, the account code stored in the Inventory Installation will be used as a last resort. The mix transactions will result in a debit to inventory and a credit to mix usage for the mix item code. Entries will also be generated for each component, debiting adjustments, and crediting mix usage. When updated, transactions created using this screen will appear in inventory history as "U" (usage) type transactions.
Once you have completed this screen, click the Update button to print the [Inventory Transaction Report / Update](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-report--update).
Important: Mix components must have been previously defined in Mix Maintenance prior to recording the newly created product in this screen.

Related information

- [Mix Pick Sheet](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/mix-processing/mix-pick-sheet)
