---
title: "Material Conversion Cost/Price Calculations | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/material-setup/material-conversion-costprice-calculations"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/material-setup/material-conversion-costprice-calculations"
---

# Material Conversion Cost/Price Calculations

When you set up additional units of measure in the HQ Material Unit of Measure window, conversion units of measure will automatically be costed and priced in the same per ECM as the standard units of measure’s cost and price, based on the conversion factor.
Note: The 'bUnits' datatype has a decimal precision of three (i.e.
 .000); therefore, if this is a stocked material and you update additional UMs to
 Inventory (i.e. Insert/Update UM at IN Locations option), it is important to understand
 the effects that the conversion factor defined for these UMs may have when updating
 IN/GL with posted units. If the conversion factor has a non-zero value in the 4th
 (.0245) or 5th position (.00245), rounding may occur.
For example:
Calculation with decimal precision of 3 (.000):
Posted Units:
10.00

Unit Cost:
128.25000

 Conversion Factor:
.00245

Conversion to Std Units:
.025 (10.00 x .00245 = 0.0245, rounded to .025)

Total Cost:
3.21 (.025 x 128.25 = 3.20625, rounded to 3.21)

Calculation with decimal precision of 5 (.00000)
Posted Units:
10.00

Unit Cost:
128.25

 Conversion Factor:
.00245

Conversion to Std Units:
.0245 (10.00 x .00245 = 0.0245)

Total Cost:
3.14 (.0245 x 128.25 = 3.14212, rounded to 3.14)
