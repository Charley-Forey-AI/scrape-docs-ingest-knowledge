---
title: "About Meter Replacements | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-meter-replacements"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-meter-replacements"
---

# About Meter Replacements

The system handles meter replacements internally by adding
 together the replaced meter reading and the current meter reading to provide a "total" meter
 reading.
If you have replaced a meter, you must
 update the Equipment Master record with the replaced meter reading.
When updating the Last Done Hours or Miles
 for a maintenance item (whether manually or via EM Work Order Update), the system
 captures and stores the replaced meter values. Replaced meter values are not included in
 the Last Done Miles or Hours values shown on the screen; however, the system does
 include the replaced meter values when determining items due for maintenance.
Note: If you manually change the Last Done values for a
 maintenance item, the system will assume the reading is for the current meter unless the
 last done date is earlier than the replaced meter date OR the last done date is the same
 as the replaced meter date, but the last done hours or miles are greater than the
 current hours or miles. In which case, it will assume the reading is for the replaced
 meter.
Tip: You can see the Total Hours or Total Miles (last done +
 replaced meter) for a maintenance item by hovering over the Last Done Miles or
 Hours fields.
When determining items due for maintenance (in EM
 Work Order Initialization), the system uses the following process:

1. Adds the Last Done Miles or Hours + Replaced Meter miles or hours + the
 SMG's interval value (i.e. Perform Service Every __ Miles/Kilometers or Hours), then
 subtracts the SMG variance (Warn when service within __ Miles/Kilometers or Hours")
 x the Variance in Advance (from EM Work Order Initialization). For ease of
 explanation, we will call this Value A.

1. Adds the current miles or hours and the replaced meter miles or hours
 defined in EM Equipment. We will call this Value B.

1. Compares Value A to Value B. If Value A is greater than Value B, the item is not
 considered due for maintenance and will not be added to the Items Due grid (in EM
 Work Order Initialization). If Value A is less than Value B, the item is considered
 due for maintenance and will be added to the Items Due grid.

Example:
Equipment 1000Equipment 2000
EMEM Current
 Odometer:8,0008,000
EMEM Replaced
 Odometer:80,00080,000
SMG "Perform Service
 Every __ Miles/Kilometers":3,0003,000
SMG "Warn when service
 within ___ Miles/Kilometers":200200
SMG Item Last Done
 Miles:7,0002,000
SMG Item's Last Done
 Replaced Miles:80,00080,000
EM Work Order Init
 "Variances in Advance":11

Equipment 1000:

- Value A: 7,000 + 80,000 + 3,000 - (200
 x 1) = 89,800

- Value B: 8,000 + 80,000 = 88,000

In this example, Equipment 1000 is not due
 for maintenance because Value A (89,800) is greater than Value B (88,000); therefore,
 the item will not be added to the Items Due grid.
Equipment 2000:

- Value A: 2,000 + 80,000 + 3,000 - (200
 x 1) = 84,800

- Value B: 8,000 + 80,000 = 88,000

In this example, Equipment 2000 is due for maintenance because
 Value A (84,800) is less than Value B (88,000); therefore, the item will be added to the
 Items Due grid.
