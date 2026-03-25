---
title: "About Overriding Cost Projections | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/about-overriding-cost-projections"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/about-overriding-cost-projections"
---

# About Overriding Cost Projections

You can override cost projections for a job using the Cost tab in JC Override Projections.
The Previous Override Projection column
 tracks the override projection amount entered in the previous month. This is the amount
 that is copied when using the File > Copy Cost
 Overrides option (see below). The Current Detail Forecast and
 Current
 Detail Projection columns are the sum of the ForecastCost and ProjCost columns (for all phases/cost
 types) in the Costs by Period table (JCCP). The Original Est Cost and Current Est
 Cost columns are the sums of the OrigEstCost and CurrentEstCost columns in the Costs by Period table (JCCP),
 respectively, by JC company, job, and month.
Values displayed in the
 Future CO
 Amt
 and
 Included CO
 Amt
 columns depend on the how you have set the
 Include in
 Projections
 checkbox for the PCO’s document type (in PM Document Types) and the
 Projections Option for the PCO’s status code (in PM Status IDs).

- If the Include in Projections option is
 unchecked for the PCO’s document type, change order amounts will not be included in
 either the Future CO Amt or Included CO Amt columns,
 regardless of the Projections Optiondefined for the PCO’s status code.

- If the Include in Projections option is
 checked and the status code’s Projections Option is:

- None, change order amounts will be excluded from the Future CO
 Amt and Included CO Amt columns.

- Display in Projections, change order amounts will be included in the
 Future
 CO Amt column, but excluded from the Included CO
 Amt column.

- Display & Calculate in Projections, change order amounts will be
 included in the Future CO Amt and Included CO
 Amt columns.

If you typically review jobs by project
 manager, clicking on the
 Project
 Manager
 column will allow you sort cost records by project manager for faster
 entry.
