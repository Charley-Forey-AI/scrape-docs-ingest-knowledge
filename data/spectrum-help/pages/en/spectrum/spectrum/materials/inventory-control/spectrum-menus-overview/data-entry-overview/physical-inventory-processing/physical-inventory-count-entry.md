---
title: "Physical Inventory Count Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/physical-inventory-count-entry"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/physical-inventory-count-entry"
---

# Physical Inventory Count Entry

Use this screen to enter physical counts based on information entered in the Physical Count Sheets. This selection is only available when a physical inventory is in progress, previously initiated using the [Set Physical Inventory Status ](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/set-physical-inventory-status) screen.
When updated, transactions created using this screen will appear in Inventory History as Adjustment type transactions. To assure that all physical count transactions are fully updated, additional entries are not allowed in this screen if there are remaining unposted Adjustment entries in the Inventory Transaction file. (This can occur if Physical Inventory File Update Part I is performed, but Inventory Transaction Update Part III is not.)
The actual cost of the item may be entered in this screen, but this normally isn't necessary unless standard cost information is incorrect. The Item cost field will be blank here to protect confidential cost information; however, if an increase adjustment to the quantity is required, the standard cost from Inventory Item File Maintenance will default (and may be overwritten, if desired). If a decrease adjustment is necessary, a negative adjustment should be entered using the Shift + back tab keys to get to the Cost field. Negative adjustments with no cost entered will adjust the item's oldest positive cost layer and use its cost.
Manually entered adjustments (both positive and negative) with the same cost as the existing layer offset that layer. If a same cost layer does not exist, a new layer #1 is created.
Items that have zero in stock must be entered so that the on-hand quantity will change to zero. Items not entered on this screen will not change when the Physical Inventory is updated. This feature allows a company to do a physical inventory on a single product line.
