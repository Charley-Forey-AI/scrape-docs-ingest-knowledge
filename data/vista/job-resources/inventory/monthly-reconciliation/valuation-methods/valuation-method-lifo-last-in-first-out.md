---
title: "Valuation Method: LIFO (Last In, First Out) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/monthly-reconciliation/valuation-methods/valuation-method-lifo-last-in-first-out"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/monthly-reconciliation/valuation-methods/valuation-method-lifo-last-in-first-out"
---

# Valuation Method: LIFO (Last In, First Out)

An example demonstrating how the ending value is calculated
 using the LIFO Valuation Method.
In addition to the standard Inventory tables, this method also uses information from the INRI (IN Reconciliation In) and INRO (IN Reconciliation Out) tables, which store the dates, unit costs, and quantities at which materials were added to and removed from stock.
First, all ‘ins’ for the month (StkUnits from INDT greater than 0.00, posted in the current month) are loaded into INRI and sorted by Location, Material, Actual Date, and Unit Cost (calculated as PostedTotalCost / StkUnits).
Note: The posted month and actual date recorded with each IN detail transaction determines its order of processing, so accurately recording the true order of inventory activity is crucial.
IN Reconciliation In (INRI)

Event
Date
Unit Cost
Units

Adjustment Entry for Beginning Balance (100 @ 1.25/ea)
10/01/10
1.25/ea
100

Buy 100 @ 1.00/ea
10/04/10
1.00/ea
100

Buy 100 @ 2.00/ea
10/07/10
2.00/ea
100

Next, the month’s total ‘out’ units (sum of StkUnits from INDT less than 0.00, posted in the current month) are calculated. If the prior month’s ending quantity is negative, then those units are added to the current month’s total 'out' units.  In our example, we have no prior month quantities, so its ending quantity is assumed to be 0.00; however, if the prior month had ended with -10 units, then 10 units would have been added to the 50 sold for a total of 60 'out' units.
After the total 'out' units have been determined, they are applied (i.e. subtracted from INRI) in ascending date order.  When an INRI entry is fully applied (Units = 0) it is removed.
Example:
Total Out Units = 50
Using the LIFO method, the system first applies the 50 ‘out’ units to the newest ‘in’ units. Therefore, 50 units are subtracted from the 100 units posted on 10/07/10. This leaves 50 remaining units in the INRI entry. The 50 'out' units are then recorded in INRO along with the Out Month, Date, Unit Cost, and In Month.
Event
Date
Unit Cost
Units

Adjustment Entry for starting Inventory level (100 @ 1.25/ea)
10/01/10
1.25/ea
100

Buy 100 @ 1.00/ea
10/04/10
1.00/ea
100

Buy 100 @ 2.00/ea
10/07/10
2.00/ea
50

If the total ‘out’ units had been equal to or greater than 100, the 10/07/10 entry would have been deleted and the entire 100 units recorded in INRO. Any remaining 'out' units would have been applied to the 10/04/10 entry. The process would continue until all ‘out’ units for the month had been applied.
After all of the 'outs' have been applied, the ending inventory’s ending value is calculated from the sum of Units * Unit Cost remaining in INRI.  In our example, we have (100 * $1.25) + (100 * $1.00) + (50 * $2.00) = $325.00.

Related information

- [Valuation Method: FIFO (First In, First Out)](/en/vista/vista/job-resources/inventory/monthly-reconciliation/valuation-methods/valuation-method-fifo-first-in-first-out)
