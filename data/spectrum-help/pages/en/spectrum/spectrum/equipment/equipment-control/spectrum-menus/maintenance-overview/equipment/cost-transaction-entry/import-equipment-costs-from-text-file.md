---
title: "Import Equipment Costs from Text File | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/import-equipment-costs-from-text-file"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/import-equipment-costs-from-text-file"
---

# Import Equipment Costs from Text File

This update creates unposted equipment transactions from a
 comma-delimited text file.
The Default settings (transaction
 date, batch code, credit G/L account and remarks) will only be used if the import file does
 not contain this information.

- If a meter value is specified in the import file, it will be assigned to meter # 1. If meter # 1 is not yet defined in the system and a meter # 1 reading is specified in the import file, the transaction will be rejected and you will need to manually import the meter reading using [Import Meter Readings from Text File](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/import-meter-readings-from-text-file).

- If the import file does not include a rate or amount, then the rate will default from the Fuel/Oil code price on file.The Fuel/Oil price may be imported if the cost category is #1 or #2.

- If errors are encountered, the Import Equipment Cost Error Listing will display showing error details. After making any error corrections to the import file data, you will then be able to re-import the text file.

Related information

- [File Layout](/en/spectrum/spectrum/equipment/equipment-control/in-depth-overview/file-layout)
