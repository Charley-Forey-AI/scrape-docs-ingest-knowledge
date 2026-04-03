---
title: "Equipment Chargeable Report Calculations | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/reports-overview/equipment-chargeable-report/equipment-chargeable-report-calculations"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/reports-overview/equipment-chargeable-report/equipment-chargeable-report-calculations"
---

# Equipment Chargeable Report Calculations

The report displays one line per selected meter type per equipment.
Column
Description

Average Meter / Period
For the monthly periods entered, the system will look both at the first meter reading and the last meter reading for the period specified, and divide the total hours used (subtracts the last meter reading from the first) by the number of periods specified. For example: If a three-month period is specified, and the first meter reading is 2500 hours and the last is 3200 hours, the average meter / period = 233.33 hours per month (3200 - 2500 / 3).

Average Usage / Period
For the monthly periods entered, the system will look at the total usage hours entered for that equipment (does not look at standby hours, just hours used on a job or non-job) divided by the number of periods specified. For example, if during the three-month period the equipment had 625 total hours used, the average usage / period (HRS) = 208.33 hours per month (625 / 3).

Chargeable % of Usage
For the monthly periods entered, this percentage would be calculated as the Average Usage per Period / Average Meter per Period. For example, the chargeable percentage for our averages above would be calculated as: 208.33 / 233.33 = 0.8929. This tells management that almost 90% of the time this equipment was run was either charged to a job or department, and there was very little downtime.
If the chargeable % was lower, management could investigate if the hours were not being reported or if the equipment had a lot of standby time reported. If that was the case, they can then run the [Equipment Utilization Report](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/reports-overview/equipment-utilization-report) to verify this explanation. If the utilization is high, the hours aren't being reported only by the employees.

Normal Usage
This is the average full usage / period.

Normal Usage / Period
This is computed based on the meter type of the line and the equipment type. If a normal value is found in either 1) the Equipment Type file, or 2) the Equipment Control Installation screen, this number is converted from a weekly to a monthly value by multiplying the value by 52 weeks and then dividing this number by 12 months.

Chargeable Percent of Normal
This is the Average Usage / Period divided by the Normal Usage / Period.

Usage hours
These hours are computed as the sum of (F)ull rate and (O)perating rate hours. (S)tandby hours are excluded.

To implement meter tracking, you should enter in the conversion balances for the meter readings in a prior year and then never run the Equipment Chargeable Report for the previous year, because it will assume they are new meters and record all the hours in the period specified. For the "through" period, you should always run the chargeable report through the last full period where there is a good meter reading.
On the last day of each month, it is recommended that an accurate meter reading be taken to ensure accuracy. If you run the Equipment Chargeable Report monthly, always run it through the last month for which you have a meter reading at the end of the month. The good thing about this report is that if a month is missed, the user can always wait and run it for the following month when there is a good meter reading available.
