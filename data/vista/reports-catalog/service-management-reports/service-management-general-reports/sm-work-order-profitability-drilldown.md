---
title: "SM Work Order Profitability Drilldown | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/service-management-reports/service-management-general-reports/sm-work-order-profitability-drilldown"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/service-management-reports/service-management-general-reports/sm-work-order-profitability-drilldown"
---

# SM Work Order Profitability Drilldown

You can use the SM Work Order Profitability Drilldown
 report to see profitably data at various grouping levels of the Work Order by selecting
 Service Management > Reports > SM Work Order Profitability
 Drilldown.
The goal of this report is to give the user the ability to see profitably data at various grouping levels of the Work Order. Users have the ability to drill down into these various levels to see more granular details. From a high level down to the actual work completed lines the totals of Price, Billed, Cost (Projected or Actual), Gross Profit, and Gross Profit Percent are calculated. At the work completed line the report will also show the Batch Month, Completed Date, Quantity, and Unit of Measure for each line. Gross Profit Percentage is calculated right to left and is not a vertical sum.
This report has five levels of data groupings:

1. Either Customer, Call Type, Service Center, Service Site, Technician, or Work Order Status

1. Work Order

1. Scope

1. Either Line Type or Cost Type

1. Work Completed Line

The first and forth grouping levels are user choice driven via the launcher.
Display\Parameter Restrictions:
Landscape report.
Drilldown report, this means that if a user would like to print/export the report they have to first drilldown to the level they want to print and then print from that level. Drilldown functionality will not work in PDF format.
'Work Order' parameter values are filtered on Company if no Customer value is provided, or on Company/Customer combo if Customer value is provided. 'Group by' parameter options are currently hard coded into the report. Any addition to the options in this parameter will need to be added to the report as well.
Cost values will look to Actual Cost first and if no value is found (or value is = 0) then it will use Projected Cost regardless of value (returns 0 if blank). Formula is:
If Actual = 0 then Projected else Actual
The report will note which Cost values are based (fully or partially) off of Projected via a '*' after each value. Lines that are flagged as No Charge in the Work Completed form will show as '**" and have a billed amount as 0.
Data Sources:

- SMWorkOrder

- SMServiceSite

- SMWorkOrderScope

- HQCO

- SMWorkCompleted

- SMWorkScope

- SMLineType

- SMWorkOrderStatus

- SMCostType

- SMCustomer

- ARCM

Related Reports:

- SM Work Order Profitability Summary

- SM Work Order Profitability Detail

Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Customer
Press F4 to select the Customer

From Date
Enter from date.

To Date
Enter to Date.

Date Range Field
Click the Field Lookup
 button or press F4 to select the scope date field.

Beginning Work Order Number
Enter or select the applicable beginning work order.

Ending Work Order Number
Enter or select the applicable ending work
 order.
Work Order Status
Click the Field Lookup
 button or press F4 to select the work order status.

Work Scope
Click the Field Lookup
 button or press F4 to select the work scope.

Service Site
Select the Field Lookup button or press F4 to select the service site.

Service Center
Select the Field Lookup button or press F4 to select the service center.

Call Type
Click the Field Lookup
 button or press F4 to select the call type..

Technician
Select the Field Lookup button or press F4 to select the technician.

Group By
Click the Field Lookup
 button or press F4 to select option for grouping data.

Group by (L)ine or (C)ost Type
Enter L or C.

(M)arkup or Gross (P)rofit %
Enter M or P.

Profit Based on (P)rice or (B)illed Amount
Enter P or B.
