---
title: "PM Project Budgets Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form"
---

# PM Project Budgets Form

Use this form to create and maintain project budgets, which allow you further breakdown the revenue or costs associated with a change order.

You can define budget detail using [budget IDs](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form), by manually entering costs and markups, or a combination of both. For example, you can assign budget codes to those sequences that define the breakdown of revenue or costs, and then enter sequences without budget IDs that will be used to provide details, subtotals, and/or totals of the cost or revenue.
Example:
SeqGroupLineLevelCodeDescription
111D - DetailL1Laborer Type 1
212D - DetailL1Laborer Type 1
313D - DetailL2Laborer Type 2
414S - SubtotalTotal labor
521D - DetailFill
622D - DetailDisposal Fees
723S - SubtotalTotal Material
831D - DetailJD 410 Excavator
932D - Detail10 CY Dump Truck
1033S - SubtotalTotal Equipment
1141D - DetailBurden
1242S - SubtotalBurden Subtotal
1354T - TotalTotal

Each sequence must be assigned a group number. The group number is used to combine all lines within the group for subtotaling purposes. However, the group number is not used in Total calculations.
Note: The Seq number assigned to each entry (automatically) only represents the order in which the entry was added to the grid; it does not control the order in which detail appears on budget reports, nor is it used in subtotals or total calculations.

A Line number must also be assigned to each entry. You can have multiple lines within a group (as shown in the example above) or use the line number as a sequential list of all entries. In the example above, this would mean assigning line number of 1 thru 13.
The line number controls the order in which the detail appears on budget reports, and is used in the subtotal and total calculations. When calculating subtotals, all sequences within a group where the line number is less than the subtotal line number will be included in the subtotal. In the example above, the subtotal for Labor (Seq 4) will include Lines 1, 2, and 3 (of Group 1), the subtotal for Material (Seq 7) will include Lines 1 and 2 (of Group 2), and the subtotal for Equipment (Seq 10) will include Lines 1 and 2 (of Group 3). When calculating totals, all lines to be included in the total must have a line number equal to or less than the total line number. In our example, each group has its own set of line numbers. So in order to ensure that all lines will be included, the total line number (Seq 13) must be equal to or greater than the highest line number of all groups; in this case, 4.
Once set up here, you can assign project budgets to change order items in PM Pending Change Orders or PM Approved Change Orders.
