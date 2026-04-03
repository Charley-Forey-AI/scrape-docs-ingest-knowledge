---
title: "Calculate Markup Based on Pay Type | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/in-depth-overview/calculate-markup-based-on-pay-type"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/in-depth-overview/calculate-markup-based-on-pay-type"
---

# Calculate Markup Based on Pay Type

The Payroll update will apply all markups to billing transactions as they are updated to the Time + Material module, based on setup in Job Billing Maintenance. When multiple markups are present for the same cost type, the software adds all markup calculations to the new billing record as follows:
Determine if the job/phase is applicable for update to Time + Material module:

- Do not add if the transaction is associated with a 'fixed price' job if the phase is set to 'Job default', 'fixed price' or 'unit price'.

- Do not add if the transaction is associated with a 'unit price' job if the phase is set to 'Job default', 'fixed price' or 'unit price'.

- Do not add if the transaction is associated with a 'cost-plus' job if the phase is set to 'fixed price' or 'unit price'.

- Do not add if the transaction is associated with a 'time + material' job if the phase is set to 'fixed price' or 'unit price'.

If the job/phase is applicable for update to Time + Material module, determine whether to mark up the labor amount:

- Do not add markup if the phase/cost type is set for no markup.

- For 'cost-plus' jobs, determine whether the labor amount includes burden before computing markup.

After determining the payroll amount (with or without burden) and that the phase is applicable for markup, calculate each case as follows:

- To calculate markup amounts for Code P:

- Multiply the specified percentage times the payroll amount divided by 100.

- Calculate this type of markup for every transaction (all pay types). Example: If the markup percentage is 25% and labor amount $200, the markup will be $50.

- To calculate markup amounts for Code R:

- Multiply the specified hourly rate times the number of hours.

- Calculate this type of markup for every transaction (all pay types). Example: If the markup rate per hour is $2 and labor hours equals 40, the markup will be $80.
