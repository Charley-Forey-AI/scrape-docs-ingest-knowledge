---
title: "Cost Method: Standard Cost | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/monthly-reconciliation/cost-methods/cost-method-standard-cost"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/monthly-reconciliation/cost-methods/cost-method-standard-cost"
---

# Cost Method: Standard Cost

An example of a single material added to inventory with 0.00
 units on hand and an initial per unit cost of $1.25.
An adjustment is made to establish the material’s beginning balance, followed by a purchase, sale, and finally another purchase.
This table displays the quantity on hand and unit costs resulting from each event.
IN Materials (INMT)

Event
Date
Qty on Hand
Last Unit Cost
Avg Unit Cost
Std Unit Cost

Beginning Balance

0
1.25/ea
1.25/ea
1.25/ea

Adjustment Entry for Beginning Balance (100 @ 1.25/ea)
10/01/10
100
1.25/ea
1.25/ea
1.25/ea

Buy 100 @ 1.00/ea
10/04/10
200
1.00/ea
1.125/ea
1.25/ea

Sell 50
10/06/10
150
1.00/ea
1.125/ea
1.25/ea

Buy 100 @ 2.00/ea
10/07/10
250
2.00/ea
1.475/ea
1.25/ea

This table illustrates how the Standard Cost method affects updates and the resulting value of Inventory. The Posted Total Cost represents the actual cost associated with each transaction, and the Change to Inventory represents the debit or credit posted to your GL Inventory Accounts. These two values may differ when using this cost method.
Event
Posted Total Cost
Change to Inventory
Ending Inventory
Variance*

Adjustment Entry for Beginning Balance (100 @ 1.25/ea)
125.00
(100 * $1.25/ea) = $125.00
125.00
0.00

Buy 100 @ 1.00/ea
100.00
(100 * $1.25/ea) = $125.00
250.00
-25.00

Sell 50
-62.50
(-50 * $1.25/ea) = -$62.50
187.50
0.00

Buy 100 @ 2.00/ea
200.00
(100 * $1.25/ea) = $125.00
312.50
75.00

362.50

50.00

* The 'Posted Total Cost' value less the 'Change to
 Inventory' value is captured in the Cost Variance account specified for the
 location in IN Locations, or in the override Cost Variance account specified
 for the location/category in IN Location Category Override.

Related information

- [Cost Method: Average Cost](/en/vista/vista/job-resources/inventory/monthly-reconciliation/cost-methods/cost-method-average-cost)

- [Cost Method: Last Cost](/en/vista/vista/job-resources/inventory/monthly-reconciliation/cost-methods/cost-method-last-cost)
