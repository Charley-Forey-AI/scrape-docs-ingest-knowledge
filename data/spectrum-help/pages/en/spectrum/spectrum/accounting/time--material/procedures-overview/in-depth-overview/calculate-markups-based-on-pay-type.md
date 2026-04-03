---
title: "Calculate Markups Based on Pay Type | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/procedures-overview/in-depth-overview/calculate-markups-based-on-pay-type"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/procedures-overview/in-depth-overview/calculate-markups-based-on-pay-type"
---

# Calculate Markups Based on Pay Type

The Payroll update will apply all markups to billing transactions as they are updated to the Time + Material module, based on setup in T+M Job Billing Setup. When multiple markups are present for the same cost type, the software adds all markup calculations to the new billing record as follows:
Determine if the job/phase is applicable for update to Time + material module:

- Do not add if the transaction is associated with a 'fixed price' job if the phase is set to 'Job default', 'fixed price' or 'unit price'.

- Do not add if the transaction is associated with a 'unit price' job if the phase is set to 'Job default', 'fixed price' or 'unit price'.

- Do not add if the transaction is associated with a 'cost-plus' job if the phase is set to 'fixed price' or 'unit price'.

- Do not add if the transaction is associated with a 'time + material' job if the phase is set to 'fixed price' or 'unit price'.

If the job/phase is applicable for update to Time + Material module, determine whether to mark up the labor amount:

- Do not add markup if the phase/cost type is set for no markup.

- For 'cost-plus' jobs, determine whether the labor amount includes burden before computing markup.

After determining the payroll amount (with or without burden) and that the phase is applicable for markup, calculate each case as follows:

- To calculate markup amounts for All transactions, (Percentage and hourly Rate):

- Percentage: Multiply the specified percentage times the payroll amount divided by 100. Calculate this type of markup for every transaction (all pay types). Example: If the markup percentage is 25% and labor amount $200, the markup will be $50

- Hourly Rate: Multiply the specified hourly rate times the number of hours. Calculate this type of markup for every transaction (all pay types). Example: If the markup rate per hour is $2 and labor hours equals 40, the markup will be $80.

- To calculate markup amounts for Regular payroll, Percentage:

- Skip this markup if the transaction is assigned any pay type other than R (regular), SR (special regular) or ER (equipment regular).

- If the pay type is R, SR or ER, proceed as for Percentage type above.

- To calculate markup amounts for Regular payroll, Hourly Rate:

- Skip this markup if the transaction is assigned any pay type other than R (regular), SR (special regular) or ER (equipment regular).

- If the pay type is R, SR or ER, proceed as for Hourly Rate type above.

- To calculate markup amounts for Overtime payroll, Percentage:

- Skip this markup if the transaction is assigned any pay type other than O (overtime) or EO (equipment overtime).

- If the pay type is O or EO, proceed as for Percentage type above.

- To calculate markup amounts for Overtime payroll, Hourly Rate:

- Skip this markup if the transaction is assigned any pay type other than O (overtime) or EO (equipment overtime).

- If the pay type is O or EO, proceed as for Hourly Rate type above.

- To calculate markup amounts for Double time payroll, Percentage:

- Skip this markup if the transaction is assigned any pay type other than D (double time) or ED (equipment double time).

- If the pay type is D or ED, proceed as for Percentage type above.

- To calculate markup amounts for Double time payroll, Hourly Rate:

- Skip this markup if the transaction is assigned any pay type other than D (double time) or ED (equipment double time).

- If the pay type is D or ED, proceed as for Hourly Rate type above.

- To calculate markup amounts for Other payroll transactions, Percentage:

- Skip this markup if the pay type is R (regular), SR (special regular) ER (equipment regular), O (overtime) EO (equipment overtime), D (double time) or ED (equipment double time).

- If the transaction is assigned any other pay type, proceed as for Percentage type above.

- To calculate markup amounts for Other payroll transactions, Hourly Rate:

- Skip this markup if the pay type is R (regular), SR (special regular) ER (equipment regular), O (overtime) EO (equipment overtime), D (double time) or ED (equipment double time).

- If the transaction is assigned any other pay type, proceed as for Hourly Rate type above.
