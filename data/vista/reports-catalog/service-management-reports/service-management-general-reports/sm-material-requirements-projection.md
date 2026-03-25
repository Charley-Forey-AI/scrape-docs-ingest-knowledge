---
title: "SM Material Requirements Projection | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/service-management-reports/service-management-general-reports/sm-material-requirements-projection"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/service-management-reports/service-management-general-reports/sm-material-requirements-projection"
---

# SM Material Requirements Projection

You can use the SM Material Requirements Projection report
 by selecting Service Management > Reports > SM Material Requirements
 Projection.
Special usage note: One of the last 5 group parameters must be "Material" for this report to work!
Calculated columns:

- Available: OnHand - Allocated (from IN)

- On Order: OnOrder (from IN)

- Qty Needed: Accumulated Qty from Work Order and agreement Required Materials, less any materials used on same Work Orders

- Used: Qty of Materials and Purchase Orders from Work Order Work Completed

- Surplus/(Shortage): Available + On Order - Qty Needed

- Cost Total: Accumulated Cost Total from Work Order Required Materials

The UM, Cost Rate, Cost ECM, Available, On Order, and Surplus/(Shortage) fields are only displayed at the Material group total.
Group 1-5: Use the lookup function to choose up to 5 group levels for this report. One of the group levels needs to be Material in order for the report to display properly.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Beginning Date
Enter beginning date or leave blank for all.

Ending Date
Enter ending date or leave blank for all.

Service Center
Select the Field Lookup button or press F4 to select the service center.

Division
Click the Field Lookup
 button or press F4 to select the division.

Call Type
Click the Field Lookup
 button or press F4 to select the call type.

Material Category
Click the Field Lookup
 button or press F4 to select the material category.

Material
Click the Field Lookup
 button or press F4 to select the material.

Beginning Agreement
Select the Field Lookup button or press F4 to select the beginning agreement.

Ending Agreement
Select the Field Lookup button or press F4 to select the ending agreement.

Beginning Inventory Company
Click the Field Lookup
 button or press F4 to select the beginning inventory company.

Ending Inventory Company
Click the Field Lookup
 button or press F4 to select the ending inventory company.

Beginning Inventory Location
Click the Field Lookup
 button or press F4 to select the beginning inventory location.

Ending Inventory Location
Click the Field Lookup
 button or press F4 to select the ending inventory location.

Group 1
Click the Field Lookup
 button or press F4 to select option 1 for grouping data.

Group 2
Click the Field Lookup
 button or press F4 to select option 2 for grouping data.

Group 3
Click the Field Lookup
 button or press F4 to select option 3 for grouping data.

Group 4
Click the Field Lookup
 button or press F4 to select option 4 for grouping data.

Group 5
Click the Field Lookup
 button or press F4 to select option 5 for grouping data.
