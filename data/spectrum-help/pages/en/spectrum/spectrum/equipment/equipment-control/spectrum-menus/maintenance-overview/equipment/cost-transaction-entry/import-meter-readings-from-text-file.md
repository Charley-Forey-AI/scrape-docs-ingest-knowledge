---
title: "Import Meter Readings from Text File | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/import-meter-readings-from-text-file"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/import-meter-readings-from-text-file"
---

# Import Meter Readings from Text File

This update creates unposted meter reading transactions
 from a comma-delimited text file.
The Default settings (meter reading date, batch code, and remarks) will only be used if the
 import file does not contain this information. The Meter # is not a required entry in the
 import file; the software will assume that the reading is for the first meter if not
 specified.
If errors are encountered, the Import Meter Reading Error Listing will display following the import of valid records. This import will be safe to repeat after making any error corrections to the import file data, as long as the transaction update has not been performed. The import will simply overwrite existing transaction records if found in the meter transaction table.

Related information

- [File Layout](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/import-meter-readings-from-text-file/file-layout)
