---
title: "Calculation Formula and Example | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/calculation-formula-and-example"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/calculation-formula-and-example"
---

# Calculation Formula and Example

When the system performs a cost projection calculation, it
 uses a standard formula.

-  Percent Complete = (Actual Units ÷
 Estimated Units) x 100

- Projected Final = (Actual ÷ Percent
 Complete) x 100

Note: If you specified to include pending change order
 amounts in projection calculations (Projections Option for the PCO’s status code is
 ‘Display & Calculate in Projections), the calculation will include all pending
 changing order item amounts meeting the criteria.
Example
In the JC Original Estimates form, you set
 up an estimate for a Concrete Form Work phase for your Labor cost type as 5,000 CY
 (cubic yards) with a cost of $8,000. You then post work progress in JC Progress Entry
 totaling 2,500 CYs, and have posted actual costs to date of $6,000.
Next, you initialize projections for the
 job. You find that the system has calculated the phase/cost type's Projected Final cost
 to be $12,000 ($4,000 over the original estimate) by assuming that if $6,000 is spent
 and the phase is 50% done, then it will take $12,000 to complete the job.

1.  (2500 ÷ 5000) x 100 = 50 (% complete)

1. (6,000 ÷ 50) x 100 = 12,000 (projected final cost)

You can now evaluate the projection and if
 needed, revise (plug) the projected Final for units, hours, cost, and unit cost, as well
 as units/hour, hours/unit, man days, or cost/hour (depending on the option selected in
 the last line of the JC Cost Projections entry grid). You can also adjust the projected
 Final amount by changing the % Complete, Over/Under, or Remaining values for any of the
 projection lines.
Using projection calculations above, you
 decide that since you have developed ways to compensate for early high costs, you want
 to project that the labor on this phase will only overrun the estimate by $2,000 (rather
 than $4,000). To do this, you will override (plug) the projected cost figure to show
 $10,000 on the Cost Projections screen. This would recalculate to show the Projected
 Final as $10,000, the Remaining as 4,000, and the % Complete on cost as 60%.
Note: If the percent complete for a phase/cost type is less than
 the minimum projection percent specified for the job (in JC Jobs) or the company (in JC
 Company Parameters), projected values will be calculated at the higher of estimated or
 actual costs. If you are using linked cost types, they will follow the primary cost
 type. For example, if you use estimated values for primary cost types, estimated values
 will also be used for the linked cost types. However, if a primary cost type has no
 estimated values or actual costs, the linked cost types will be treated as individual
 cost types.
