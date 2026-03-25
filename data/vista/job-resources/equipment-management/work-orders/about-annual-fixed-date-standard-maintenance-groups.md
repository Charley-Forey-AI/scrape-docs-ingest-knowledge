---
title: "About Annual Fixed Date Standard Maintenance Groups | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-annual-fixed-date-standard-maintenance-groups"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-annual-fixed-date-standard-maintenance-groups"
---

# About Annual Fixed Date Standard Maintenance
 Groups

Maintenance groups with an Annual Fixed Date basis are handled
 somewhat differently during the initialization process in EM Work Order Initialize.
Initialization uses the Create Work Order:
 ___ days prior to annual fixed date field to determine if the
 maintenance group is due for maintenance. If the due date falls within the specified
 number of days from the WO Date, it will be added to the selection grid. For
 example, if the annual fixed date is 12/15 and you specified 30 days in the
 Create
 Work Order: ___ days prior to annual fixed date field, the
 maintenance group will only be included in initialization if the WO Date is within
 30 days or less of the annual due date (e.g. the WO Date is 11/16 or later).
Some exceptions do apply:

- If the Last Done date falls within the specified
 variance (for the current year), it will not be considered due for
 maintenance. For example:  Annual Fixed Date: 6/15  Create Work Order ___
 days prior to Annual Fixed Date: 30  WO Date: 5/25/2019

- If the Last Done date is 5/20/2019, item falls
 within the 30-day variance, and is not due for maintenance.

- If the Last Done date is 4/20/2019, item falls
 outside the 30-day variance, and is due for maintenance.

- If the Create Work Order: ___ days
 prior to annual fixed date is blank, the system will
 use the Days in Advance
 field to determine if the maintenance group should be added to the
 selection grid. Items will be added to the grid when either of the
 following conditions apply:

-  the equipment has not been serviced within 45 days difference between the Last Done date of the item and the WO Date, plus the specified Days in Advance (current and following years).

- the equipment has been serviced within 45 days difference between the Last Done date of the item and the WO Date (current or prior year).

- If the Last Done Date
 field in EM Standard Maintenance Groups is blank (e.g. the equipment
 has never been serviced), the maintenance group will be added to
 selection grid, regardless of any settings.

- If the Last Done Date is 365 days or more older than the WO Date, the maintenance group will be added to selection grid, regardless of any settings.

- If the maintenance group is already on an open work order, it will not be added to the selection grid, regardless of settings.

Note: The system uses the Standard Maintenance Group Options in EM
 Company Parameters to determine how to handle maintenance items and linked
 maintenance groups that are not due for maintenance when populating the Std Maint
 Groups and Items Due grids. For more information about these options, see [About the Standard Maintenance Group
 Options](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-standard-maintenance-group-options).
