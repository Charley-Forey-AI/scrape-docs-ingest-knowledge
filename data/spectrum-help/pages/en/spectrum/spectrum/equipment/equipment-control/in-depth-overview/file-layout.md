---
title: "File Layout | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/in-depth-overview/file-layout"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/in-depth-overview/file-layout"
---

# File Layout

The following table outlines the required file layout for
 the Equipment Transaction Import.
If no errors are found during the import, the software will add records to the Equipment
 Control Transaction Entry Table (EC_TRANSACTION_ENTRY_MC) if all of the following
 conditions are met.
Field
Type
Length
Required?
Conditions

Transaction Date
Date
8
No
Not required in the text file. Entry of this field is required on the import start screen and will be used if not submitted in the text file.

Batch Code
Alpha
10
No
Not required in the text file. Entry of this field is required on the import start screen and will be used if not submitted in the text file.

Equipment Code
Alpha
10
Yes
Must be a valid equipment code.

Cost Category
Alpha
4
Yes
Must be a valid cost category code.

- If the cost category is set to #1 or #2, then the Fuel/Oil code must be valid in the current company.

- If the cost category is set to #1, then the Fuel/Oil code must be a Fuel type.

- If the cost category is set to #2, then the Fuel/Oil code must be an Oil type.

Quantity
Numeric
11
No
Not required as this import format can be used to load meter #1 readings.

Fuel / Oil Code
Alpha
2
Optional
Only required if the Cost Category above references Fuel.

Amount
Numeric
11
No
Not required as this import format can be used to load meter #1 readings. If the import file contains a zero, the import will treat the entry as <blank>, not as an error.

G/L Debit Account
Alpha
12
Yes
Must be a direct equipment G/L code.

G/L Credit Account
Alpha
12
No
Not required in the text file. Entry of this field is required on the import start screen and will be used if not submitted in the text file.

Remarks
Alpha
30
No
Not required in the text file. Entry of this field on the import start screen will be used if not submitted in the text file.

Meter #1
Numeric
7
No
Must be positive and non-zero. The transaction will be rejected if meter 1 is not yet defined in the system and meter 1 is specified in the import file. This protection is provided for convenience when only one meter is being tracked; usually you will want to import meter readings separately using the [Import Meter Readings from Text File](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/import-meter-readings-from-text-file) feature.

Equipment Work Order
Alpha
10
Optional
Only required if the Cost Category requires the use of Equipment Work Orders.

Rate
Numeric
11
No
If blank, the rate will default in based on the Fuel/Oil code price on file.

Credit Cost Center
Alpha
10
Optional
If not entered in the text file, the system will default to the equipment's cost center.
