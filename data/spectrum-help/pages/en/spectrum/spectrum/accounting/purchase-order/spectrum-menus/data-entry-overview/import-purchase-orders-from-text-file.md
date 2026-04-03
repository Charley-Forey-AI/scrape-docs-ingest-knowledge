---
title: "Import Purchase Orders from Text File | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/import-purchase-orders-from-text-file"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/import-purchase-orders-from-text-file"
---

# Import Purchase Orders from Text File

This screen is used to import purchase orders from a
 comma-delimited text file, and is designed to mimic the process followed when purchase orders
 are manually entered into the software.
The import validates all required field information to ensure the imported data is
 accurate. The following date formats are accepted: MMDDYYYY, MM/DD/YY, and YYYYMMDD. If
 errors are found, the software will generate an exception report with error details before
 the data is imported.
A single import file can contain both job-specific and work order-specific purchase orders. Spectrum interprets whether a job number is recorded in the P.O. header. If it is, then the purchase order is automatically set as a 'Job' purchase. If there is no job number but the Work Order module is present, then Spectrum looks for a work order # and imports the purchase order as a 'Work order' type. If the work order number is also not present, then the purchase order type will be set to 'Job.'

## Price per factor

Import of stock and non-stock items with a price-per-factor other than 1 is supported. The import also supports lump sum purchase orders. You can also specify a sales/use tax code in the import file.
During the import update the price-per-factor will be set as follows:

- Stock
 Item: This is the price-per-factor specified in Inventory Control > Inventory File Maintenance.

- Non-stock
 Item: If the unit-of-measure is C, set the price-per-factor to 100. If
 the unit-of-measure is M, set the price-per-factor to 1000. Otherwise, set the
 price-per-factor to 1.

## Location

If there is a default purchase from location assigned to the vendor, the
 Purchase Location Code column will display this code. Likewise, if there is a default
 payment location assigned, the 'Payment location' code column will display this code.
If a Job code is specified in the import file (header record), the system will determine if an override 'ship to' address is present for that job.

## Sub-Job

If this is a sub-job transaction for a master job, Spectrum will add a new phase to the sub job if the current job is a sub-job of a valid master job, the phase lengths of both jobs match, and the Phase + Cost type combination for the current job is valid and not 'Complete'.
Watch the following videos to learn how to create a purchase order export file from Tekla EPM, and then import it into Spectrum.

Related information

- [Layout](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/import-purchase-orders-from-text-file/layout)
