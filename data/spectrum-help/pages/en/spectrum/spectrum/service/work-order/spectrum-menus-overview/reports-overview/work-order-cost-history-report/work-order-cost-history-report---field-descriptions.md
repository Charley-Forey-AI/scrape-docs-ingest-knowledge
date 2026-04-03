---
title: "Work Order Cost History Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/reports-overview/work-order-cost-history-report/work-order-cost-history-report---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/reports-overview/work-order-cost-history-report/work-order-cost-history-report---field-descriptions"
---

# Work Order Cost History Report - Field Descriptions

Use the table below for reference when completing the fields on this screen.

Work order Site Customer Task Work order type Work order zone Contract
Enter the work order number, site code,
 customer code, task code, work order type, work order zone, and contract number
 to print on the report, or press Enter to include all work orders.
G/L date
The software will compare the selected
 date range with the G/L date associated with each cost history record. When the
 report includes unposted labor costs, then all such transactions with a work
 date on or before the 'To G/L Date' will be included. When the report includes unposted material costs, then all such
 transactions will be included, regardless of date. These transactions will
 appear undated at the end of lists sorted by date.

Include historical costs
If the Detail format is selected ,
 select this checkbox to include historical costs, and select one or more
 transaction types to display on the report:

- Labor
 (Work Order source)

- Labor
 (Payroll source), including time cards with direct work
 order cost add-ons

- Material (Work Order source)

- Material (A/P source)

- Other charges (Work Order source)

- Other charges (G/L source)

Include unposted costs
Select this checkbox to include
 unposted costs, and then select whether to include labor and/or material
 transactions on the report.

- When the 'Include unposted labor costs' option is
 selected, the cost totals will include all payroll cost transactions,
 available for billing pre-time entries and time card entries, and
 unposted labor transactions.

- When the 'Include unposted material costs' option is
 selected, the cost totals will include invoice cost transactions,
 available for billing AP invoice entries and unapproved invoice entries,
 and estimated and unposted material transactions. Note: If both 'Include unposted labor costs' and
 'Include unposted material costs' options are selected, unposted other
 charge transactions will also be included on the report.

Format
Select a report format:

- Detail

- Summary

 If Detail is selected, the options to include
 historical costs are enabled.

Sort by
Click to specify the sequence in which
 work orders are to be printed. This report can be grouped by work order number,
 by technician (lead technician), by ordered date, or by the estimated
 completion date. Sorting by lead technician is particularly useful if open work
 orders are being scheduled and techs have been entered in the technician field
 on the Work Order Entry screen; this report can show which work is assigned for
 every technician.
Work order status
By default this report will print all
 three work order status types. When one or more of these checkboxes is
 selected, the software filters work orders for inclusion on this report based
 on the current status of the work order.
