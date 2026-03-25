---
title: "Company Add-Ons: Add-on Basis | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/company-add-ons-add-on-basis"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/company-add-ons-add-on-basis"
---

# Company Add-Ons: Add-on Basis

Use the Add-On Basis section in PM Company Add-Ons to specify the add-on basis; that is, the amount on which to base the add-on cost.
You can specify to use a flat amount or have the calculation based on a percentage of the overall change order or the total costs for a specific cost type.
If the add-on is for additional costs (e.g. bonds), you can redirect the costs to a specific phase/cost type and/or contract item. If you wish to distribute the add-on amount to all phases on the change order with a specific cost type, leave the phase blank and enter only the desired cost type. The system will distribute the add-on amount proportionally to all phases on the change order with that cost type, adjusting the last phase/cost type for rounding (if necessary).
Example:
Add-on:
100

Basis:
Cost Type

Basis CT:
1 (Labor)

Percent:
10.00

Redirect CT:
7 (Burden)

Redirect Phase:
(blank)

Pending CO:
Phase
CT
Amount
Add-on Amt

02210-  -
1
300.00
30.00

03310-  -
1
300.00
30.00

04410-  -
1
  400.00
40.00

Total:
$1000.00
$100.00

Approved CO:
Phase
CT
Amount

02210-  -
1
300.00

7
30.00

03310-  -
1
300.00

7
30.00

04410-  -
1
400.00

7
40.00

Total:
$1100.00

Related concepts

- [PM Company Add-ons Form](/en/vista/vista/project-management/setupmaintenance/pm-company-add-ons-form)

- [PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)
