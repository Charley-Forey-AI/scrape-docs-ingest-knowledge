---
title: "About Initialize Worksheet Detail Option | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/cost-projection-detail/about-initialize-worksheet-detail-option"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/cost-projection-detail/about-initialize-worksheet-detail-option"
---

# About Initialize Worksheet Detail Option

If you are using the Projection Detail tab (JC Cost
 Projections) to build cost projections, the Initialize Worksheet Detail Option allows you to
 initialize existing projection detail into the current batch.
Note: You will only see this option if you have checked
 the Activate Projection Detail Feature box in JC Company Parameters, Projections tab.
You will typically only use this feature if
 you project detail out for the life of the job (i.e. you add a detail line for each
 month you expect the job to run) as shown in the example below.
Job: 10000-  -
Phase: 03300-100-
CT: 4 (Equip)
Seq
EMCo
Equipment
Detail Month
Number of
Units
UM
Hrs/Unit
Hours
Cost/Hour
Unit Cost
Amount

1
1
10101
6/11
1
3
HRS
1.00
160.00
50.00
50.00
8,000.00

2
1
10101
6/11
1
160.00
HRS
1.00
160.00
50.00
50.00
8,000.00

3
1
10101
6/11
1
160.00
HRS
1.00
160.00
50.00
50.00
8,000.00

4
1
10101
6/11
1
160.00
HRS
1.00
160.00
50.00
50.00
8,000.00

5
1
10101
6/11
1
160.00
HRS
1.00
160.00
50.00
50.00
8,000.00

6
1
10101
6/11
1
160.00
HRS
1.00
160.00
50.00
50.00
8,000.00

7
1
10101
6/11
1
160.00
HRS
1.00
160.00
50.00
50.00
8,000.00

For each successive month that you run cost
 projections for the job, you would set this option to initialize detail either with
 values or without values. The system will initialize detail lines for the remaining
 months based on your selection. For example, using the setup shown above, if you created
 a projections batch for 07/11 and specified to initialize detail with values,
 initialization would add sequences 3-7 to the Projections Detail grid and set all values
 to those shown for those months. It would not include Seq 1 or 2, since the batch will
 already include the actual costs for those months.
Once initialized, you can modify existing
 values or set up/delete detail lines as necessary.
