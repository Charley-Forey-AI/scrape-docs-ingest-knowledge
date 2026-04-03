---
title: "Perform a Physical Inventory Using a Barcode Scanner | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/procedures-overview/tell-me-how/perform-a-physical-inventory-using-a-barcode-scanner"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/procedures-overview/tell-me-how/perform-a-physical-inventory-using-a-barcode-scanner"
---

# Perform a Physical Inventory Using a Barcode Scanner

Learn how to perform a physical inventory using a barcode
 scanner.

1. To prepare for physical inventory, make sure the
 Inventory Transaction
 Report has been printed and updated. This report shows receipts,
 transfers, and adjustments that should be posted to master files before the Physical
 Inventory is initiated. Likewise, confirm that Order Processing invoices are also
 fully posted using Invoice Register
 Report. Any purchase order quantity entries should be updated, if the
 Two step withpacking list update option is
 selected on the Purchase Order Installation > Properties tab.

1. On the Site Map screen, click Inventory Control >  Data Entry >  Physical Inventory.

1. Use the Count sheet and Set
 status buttons to set the cycle for the appropriate warehouse (for
 example, enter warehouse 1
 in both screens).

1. Using a barcode scanner, scan your physical inventory
 and enter the counts.Note: Depending on the scanner memory, you may need to divide
 up the inventory and repeat steps 4-9.

1. Download the barcode scanner data to a file with a
 unique name (for example, CCYYMDD_data.txt) and retain this file as a backup.

1. Copy the data file to another directory and convert it
 to a fixed-width format.

1. On the Site Map screen, click Equipment Tracking >  Data Entry >  Equipment Tracking and enter a new requisition.Note: The requisition transaction code will be an Issue when
 the Inventory selection is Physical.

1. Click the Import button and import the data
 file into the requisition.

1. Click the Update button and run the update to
 post the requisition. This creates the count entry in the Physical Inventory. Click
 OK to return to the main
 menu.

1. On the Site
 Map screen, click Inventory Control  >  Data Entry  >  Physical Inventory.

1. Using the Count Entry, Reports, and Update buttons, print the reports
 and process the inventory counts. Spectrum will create inventory (A)djustments equal
 to the difference of "current on hand" and the "count".

1. Click the Clear status button to clear the
 inventory cycle.
