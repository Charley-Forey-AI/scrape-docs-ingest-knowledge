---
title: "How the Reconciliation Process Works | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/monthly-reconciliation/how-the-reconciliation-process-works"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/monthly-reconciliation/how-the-reconciliation-process-works"
---

# How the Reconciliation Process Works

To better understand how monthly reconciliation works, you must first understand how the various Cost methods affect updates to your Inventory GL Accounts as transactions are posted.
Select the icons below for examples of how each Cost Method affects updates and the resulting value of Inventory.
[Cost Method: Average Cost](/en/vista/vista/job-resources/inventory/monthly-reconciliation/cost-methods/cost-method-average-cost)
[Cost Method: Standard Cost](/en/vista/vista/job-resources/inventory/monthly-reconciliation/cost-methods/cost-method-standard-cost)
[Cost Method: Last Cost](/en/vista/vista/job-resources/inventory/monthly-reconciliation/cost-methods/cost-method-last-cost)
The reconciliation process not only records a monthly ‘snapshot’ of your inventory, but also summarizes all ‘ins’ and ‘outs’ (i.e. purchases, sales, transfers, production, and adjustments) to recalculate an ending value based on the Valuation Method (specified in IN Company Parameters). For each stocked material, a beginning value is initialized from its prior month’s ending values. If no prior entry exists in IN Monthly Activity (INMA), the beginning value will be 0.00.
Activity is summarized by transaction type from IN Detail (INDT) posted in the reconciliation month. The sum of all activity represents the total change to Inventory GL Accounts posted throughout the month. A 'posted ending' value is determined from the material’s beginning value and its summarized activity for the month. An ending value is then calculated based on the selected Valuation Method. All values are recorded in IN Monthly Activity (INMA).
When the Update button is pressed, any difference between the ‘posted ending’ value and the calculated ending value of a material will generate a reconciliation adjustment entry.
IN Monthly Activity (INMA)

Begin Qty
0.00

Begin Value
0.00

Begin Last Unit Cost
$0.00 E

Begin Avg Unit Cost
$0.00 E

Begin Std Unit Cost
$0.00 E

Purchase Qty
200

Purchase Cost
$300.00 (Avg or Last Cost)
$250.00 (Std Cost)

Job Sales Qty
-50

Job Sales Cost
-$56.25 (Avg Cost)
-$62.50 (Std Cost)
-$50.00 (Last Cost)

Adjustment Qty
100

Adjustment Cost
$125.00

End Qty
250

End 'Posted' Cost
$368.75 (Avg Cost)
$312.50 (Std Cost)
$375.00 (Last Cost)

End Last Unit Cost
$1.50 E

End Avg Unit Cost*
$1.4167 E

End Std Unit Cost
$1.25 E

End Value**
(Based on Valuation Method)
As Posted $368.75 (Avg Cost)
As Posted $312.50 (Std Cost)
As Posted $375.00 (Last Cost)
Avg Cost $354.18
Std Cost $312.50
FIFO $362.50
LIFO $325.00

* The End Avg Unit Cost is calculated for each material as its beginning value plus the actual value of all 'ins' (i.e. purchases, production, transfers in, and adjustments), divided by the sum of the month’s beginning quantity and all ‘in’ units.
((0 x $0/ea) + ($425)) / (0 + 300) = $1.4167
Beginning Value: 0 Units x $0/ea Ins Cost: $300 + $125 = $425 Begin Qty: 0 In Qty: 300 Ending Avg Unit Cost = $1.4167
This calculation will only produce an accurate result when both the beginning quantity for the month and the sum of beginning quantity plus 'ins' are positive. If the month's beginning quantity is less than or equal to 0, the ending average cost will be calculated from 'in' units only. If neither of these conditions is met, the ending average cost will be set equal to the month's beginning average cost.
** The End Value is calculated as follows depending on the Valuation Method (using the values in the example above):

- As Posted - Beginning value plus summarized activity for the month. Result depends on the Cost Method used. No reconciliation adjustments/GL updates will be generated.

Cost Method Used
As Posted (Inventory detail value of all 'ins' and 'outs')

Average Cost
$368.75 (300 + -56.25 + 125)

Standard Cost
$312.50 (250 + -62.50 + 125)

Last Cost
$375.00 (300 + -50.00 + 125)

- Average Cost - Ending Qty x Ending Avg Unit Cost (Does not depend on Cost Method) (250 * $1.4167/ea) = $354.18

- Standard Cost - Ending Qty x Ending Std Unit Cost (Does not depend on Cost Method) (250 * $1.25/ea) = $312.50

- FIFO / LIFO - These methods require the use of two additional tables, INRI (IN Reconciliation In) and INRO (IN Reconciliation Out), to track the dates, unit costs, and quantities at which the material was added to stock and subsequently removed. For illustrations on how the End Value is is calculated using these two methods, select on the icons below:

[Valuation Method: FIFO (First In, First Out)](/en/vista/vista/job-resources/inventory/monthly-reconciliation/valuation-methods/valuation-method-fifo-first-in-first-out)
[Valuation Method: LIFO (Last In, First Out)](/en/vista/vista/job-resources/inventory/monthly-reconciliation/valuation-methods/valuation-method-lifo-last-in-first-out)
