---
title: "Report Calculations - Mean Time Before Failure Report | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/preventive-maintenance/spectrum-menus/reports-overview/mean-time-before-failure-report/report-calculations---mean-time-before-failure-report"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/preventive-maintenance/spectrum-menus/reports-overview/mean-time-before-failure-report/report-calculations---mean-time-before-failure-report"
---

# Report Calculations - Mean Time Before Failure Report

The following tables describe how the Mean Time Before Failure Report is calculated.
Note: Only historical meter reading information will be used
 for calculations on this report. Any unposted transactions currently in progress will be
 disregarded.
Field
Description

Equipment Code
The equipment code displays in this
 column.
Description
The equipment description displays in
 this column.
Work Order Count
The number of work orders included in
 the calculation displays in this column. If the 'Sort by' option is 'Problem
 type', this is the number of work orders assigned to this type.
Change in Meter: Total <UNITS>
The change in meter rates between the
 'From order date' and 'To order date' will display in this column. If a meter
 reading is not available as of the work ordered date, calculate using the
 latest previous meter reading before this date. The selected type of meter will
 display in place of <UNITS>.
Change in Meter: Mean Change
The total meter <UNITS> divided
 by work order count.
Days to Failure: Total Days
The total number of days between the
 'work ordered' date and the 'returned to service' date. When no earlier work
 order date exists, then the 'purchase date' is used. Note: This value is not the total number of days since the equipment was
 first placed into service, rather it omits down time (for example, the
 period from the 'order' date until the 'returned to service'
 date).

Days to Failure: Mean Days to Failure
The total days to failure divided by
 work order count will display in this column.
Failure Rate/<UNIT>
The work order count divided by the
 total meter units displays in this field. The selected type of meter will
 display in place of <UNITS>.

The following additional fields are found on the Detail format of the report.
Field
Description

Last Service Start Date
The 'Return to service' date of the next prior work order meeting the selection criteria displays in this column.

Order Date
The 'order' date of the work order displays in this column.

Work Order #
Individual work order numbers will display in this column.

Description
The work order description will display in this column.

Meter # <UNITS>
The change in meter rates between the 'From order date' and 'To order date'
 will display in this column. If a meter reading is not available as of the
 work ordered date, calculate using the latest previous meter reading before
 this date. The selected type of meter will display in place of
 <UNITS>.

Days to Failure
The total number of days between the 'work ordered' date and the 'returned to
 service' date. When no earlier work order date exists, then the 'purchase
 date' is used.Note: This value is not the total number
 of days since the equipment was first placed into service, rather it
 omits down time (for example, the period from the 'order' date until the
 'returned to service' date).
