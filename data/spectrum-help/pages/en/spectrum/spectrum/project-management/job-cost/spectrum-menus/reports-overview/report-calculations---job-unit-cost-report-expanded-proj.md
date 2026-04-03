---
title: "Report Calculations - Job Unit Cost Report (Expanded, Proj. Cost = Yes) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/report-calculations---job-unit-cost-report-expanded-proj.-cost--yes"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/report-calculations---job-unit-cost-report-expanded-proj.-cost--yes"
---

# Report Calculations - Job Unit Cost Report (Expanded, Proj. Cost = Yes)

The calculation of projected costs is based on the unit price projection method assigned to the individual phase code / cost type. This is located in JC_PHASE_MASTER_MC.Projected_Cost_Code.
This value can be E ( = estimated), A ( = actual), or P (= projected).

- If the projected unit price method is 'E', projected cost = estimated cost * (projected qty / estimated qty)

- If the projected unit price method is 'A', projected cost = actual cost * (projected qty / actual qty)

- If the projected unit price method is 'P', projected cost = projected cost from the projected cost history

These calculations are only applicable when the 'Use projected cost?' box on the report start screen is checked. None of the above values are date sensitive, they are based on the most current information.
The unit price projection method defaults from the Job Cost Installation screen settings. It can be modified during Projected Cost Entry as well.
The column headings for this report are the same for projected and non-projected figures. Both reports print job-to-date and estimated figures; both reports calculate variance. The Projected cost report includes projected figures, whereas the non-projected report includes period-to-date figures.
The following tables describes how each column is calculated on this report.

## Field Descriptions

Field
Description

Qty
The period-to-date, job-to-date, and estimated quantities display from Job Phases. Variance is calculated as the difference between job-to-date and projected.

UM
The period-to-date, job-to-date, and estimated quantities display from Job Phases. Variance is calculated as the difference between job-to-date and estimated.

## Cost Type Columns

Field
Description

Hours
Actual labor and equipment hours display.

Hours Per Unit
For labor hours, the number of hours per unit is calculated by the system as the quotient of the "qty" and "labor hours" columns.

Unit Cost
All cost type Unit Cost columns display the estimated unit cost from Job Phases.

Total Cost
All cost type Total Cost columns calculate this figure as the product of Unit Cost and Quantity.

## Total

Unit Cost
The total Unit Cost is calculated as the sum of the unit costs for all cost types.

Total Cost
The total Total Cost is calculated as the sum of the total costs for all cost types.
Figures in the labor, materials, sub, and equipment columns are for the corresponding cost types for each phase (these cost types were specified on the start screen for the report). All other cost type figures are combined in the other column. The total columns provide the sums of figures in all the cost type columns.
In each column, period-to-date, job-to-date, and estimated figures display. Variance is calculated as the difference between the job-to-date and the estimated figures.
