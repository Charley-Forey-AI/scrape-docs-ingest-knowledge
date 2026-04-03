---
title: "Perform a Physical Inventory | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/procedures-overview/tell-me-how/perform-a-physical-inventory"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/procedures-overview/tell-me-how/perform-a-physical-inventory"
---

# Perform a Physical Inventory

Learn how to perform a physical inventory.

1. To prepare for physical inventory, make sure the
 Inventory Transaction
 Report has been printed and updated. This report shows receipts,
 transfers, and adjustments that should be posted to master files before the Physical
 Inventory is initiated.

1. Confirm that the following transactions are updated if
 the stock has been removed from the warehouse shelf and therefore will not be
 counted:

- Inventory Control Job Requisitions Transaction Update

-  Work Order Create AR Invoices and AR Data Entry
 Invoice/Credit memo Sales Journal update

- Order Processing Invoices

1. To provide current quantity information for all items,
 print a summary Items-On-Hand Valuation
 Report.

1. To set the warehouse status where the Physical
 Inventory will be taken, you must temporarily cease inventory transactions using the
 Physical Inventory Status
 Update. Once
 this step has been performed, inventory item information in the computer files may
 not be changed until Physical Inventory
 Clear has been performed.

1. To create the necessary forms with the appropriate
 warehouse codes, use Physical Count
 Sheet Printing.

1. To enter inventory date to the software after the
 count sheets have been completed, use Physical Count Data Entry. As each item is entered, the status flag
 for each is changed from (C)leared to (E)ntered.

1. When the physical counts have been entered, the
 following three reports should be printed using the Physical Inventory Reports
 screen:

- Physical
 Count Transaction Listing to ensure that all information has
 been entered correctly.

- Physical
 Inventory Exception Listing to review a listing of all items
 for which there is no physical count entered.

- Physical
 Inventory Variance Report to compare the computer total for
 each item with the physical count for each item (only those items that do
 not properly reconcile will print).
Note: All items that appear on the Physical Inventory
 Variance Report should be verified.

1. Correct all items that were either missing or improperly accounted for. [Reconciling Inventory Discrepancies after an Inventory
 Count](/en/spectrum/spectrum/materials/inventory-control/procedures-overview/tell-me-how/reconciling-inventory-discrepancies-after-an-inventory-count)

1.  If there are still un-updated transactions in job
 requisition, Work Order and/or Order Processing that should be included in the count,
 add these quantities to the entered count.

1. Confirm your Inventory Control current processing date
 is set to the desired date. For example, if today is 1/3 and you are updating counts
 effective 12/31, it's necessary to change the current processing date to 12/31. IC
 Data Entry Processing Date Change.

1. To update the Inventory Item Detail File
 Maintenance to reflect the physical counts and to create inventory
 adjustment entries for all items entered that had a variance between the on-hand
 quantity and the physical count, run the Physical Inventory File
 Update.

1. To isolate any discrepancies still existing between
 system records and the actual physical count, print the Item History Report.

1. To return the Inventory Control to normal operations,
 perform the Physical Inventory
 Clear.

1. To reflect current inventory quantities after physical
 inventory completion, print a final copy of the summary Items-On-Hand Valuation
 Report.

1.  If you changed your current processing date in step
 11, correct your processing date to the current date now.
