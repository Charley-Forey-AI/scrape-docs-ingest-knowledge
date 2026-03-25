---
title: "How System Count Quantities Are Determined | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/monthly-reconciliation/initialize-the-physical-count-worksheet/how-system-count-quantities-are-determined"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/monthly-reconciliation/initialize-the-physical-count-worksheet/how-system-count-quantities-are-determined"
---

# How System Count Quantities Are Determined

System count quantities are determined by ‘on hand’
 quantities (IN Materials) minus any “ins” and “outs” with an Actual Date equal to or greater
 than the Count Date (On Hand – [Units In + Units Out]).
However, you can specify to include activity
 posted on the count date in the system count by checking the Include Count Date Activity
 box. If the option is unchecked, the system will subtract these quantities from the ‘on
 hand’ quantities when calculating the system count.
An example of some posted adjustments for a
 specific material:
Trans #
Units
ActDate

1
10.000
10/30/08

2
-5.000
10/30/08

3
-15.000
10/31/08

4
-25.000
11/01/08

If the worksheet for this example is
 initialized, and the Count Date is 10/31/08, the system treats each of the posted
 transactions as follows (assuming that the original on hand amount for the material is
 500.000):
Trans #
Units
ActDate
On Hand
System Count

1
10.000
10/30/05
510.000
510.000 (units are
 added)

2
-5.000
10/30/05
505.000
505.000 (subtracts the
 units)

3
-15.000
10/31/05
490.000
490.000 (subtracts the
 units)

4
-25.000
11/01/05
465.000
490.000 (backs the
 transaction out of INDT and adds the units back into the count.

Note: Any discrepancies found between the physical count and the
 system count are recorded in the Adj Units column for each material.
