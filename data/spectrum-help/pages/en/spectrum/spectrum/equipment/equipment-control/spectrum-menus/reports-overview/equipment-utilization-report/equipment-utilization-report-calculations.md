---
title: "Equipment Utilization Report Calculations | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/reports-overview/equipment-utilization-report/equipment-utilization-report-calculations"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/reports-overview/equipment-utilization-report/equipment-utilization-report-calculations"
---

# Equipment Utilization Report Calculations

The report displays one line per selected equipment code.
Column
Description

Stand-By Hours
The total stand-by hours are displayed for the period entered on the report. These are accumulated from the 'ES' entries from the Equipment data entry, or updated from the Equipment Tracking module on a regular basis while the equipment is at the job.

Usage Hours
The total hours used are displayed for the periods specified on the report. These are accumulated from the 'EU' entries from the Equipment data entry and/or from the Payroll Time Card Entry ('ER','EO','ED','EU').

Total Hours
The total hours are calculated as Stand-By Hours + Usage Hours for the periods specified on the report.

Utilization Percentage
 The utilization percentage is calculated as the Usage hours / Total hours for the period specified on the report.

Total Normal Hours
This column is only computed when the meter type = Hourly. The Total Normal Hours are computed based on the meter type of the line and the equipment type. If a normal value is found in 1) the Equipment Type file, or 2) the Equipment Control Installation screen, this number is converted from a weekly to a monthly value by multiplying the value by 52 weeks and then dividing this number by 12 months and then multiplying the number of periods included on the report.

Utilization % of Actual
This column is only computed when the meter type = Hourly and the Total Normal Hours column has a non-zero value. The calculation for this column is the Actual Usage Hours / Total Normal Hours for the period specified on the report times 100.
