---
title: "Cost Projection Detail | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/cost-projection-detail"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/cost-projection-detail"
---

# Cost Projection Detail

You can define the detail that makes up a cost projection using the Projection Detail tab in JC Cost Projections.
You will only need to use the Projection Detail tab if you prefer to do cost
 projections at the cost type level.
Note: In order to use this feature, you must check the
 Activate
 Projection Detail Feature box in JC Company Parameters, Projections
 tab).
For each applicable phase/cost type, you enter
 detailed cost information and then update the costs to the projections grid by clicking
 Plug
 Detail. Values will be updated to the Remaining
 column in lower grid, and the phase will be highlighted (in yellow) in phase grid to
 indicate a plugged value.
Projection detail includes (but is not
 limited to) the budget code, description, detail month, activity date range, units,
 hours, unit cost, and amount. For labor and equipment cost types (those assigned a JB
 Cost Type Category of 'L-Labor' or 'E-Equipment in JC Cost Types), additional columns
 will display for PRCo, Craft, Class, and Employee or EMCo and Equipment, respectively.
If you choose to project detail out for the
 life of the job (i.e. you add a detail line for each month you expect the job to run),
 you have the option to pull the detail in automatically each time you initialize
 projections (using Initialize Worksheet Detail Option in JC Projection Calculation). For
 example, in batch month 06/09, you set up your projection detail as follows:
SeqEMCoEquipmentDetail Mth# OfUnitsUMHrs/UnitHoursCost/HrUnit CostAmount
111010101/101160.00HRS1.00160.0050.0050.008,000.00
211010102/101160.00HRS1.00160.0050.0050.008,000.00
311010103/101160.00HRS1.00160.0050.0050.008,000.00
411010104/101160.00HRS1.00160.0050.0050.008,000.00
511010105/101160.00HRS1.00160.0050.0050.008,000.00
611010106/101160.00HRS1.00160.0050.0050.008,000.00
711010107/101160.00HRS1.00160.0050.0050.008,000.00

You then update the costs to the projections grid,
 plug values as necessary, and post the batch. In batch month 07/09, you initialize
 projection detail (with or without values). Since the system will automatically include
 the month of July in the projection calculations, it will only pull in projection detail
 sequences 3 – 7 (months 08/09 – 12/09). This process can be repeated each time you run
 projections through the life of the job, allowing you to accurately track and update
 costs as necessary.
