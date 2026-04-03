---
title: "Crystal Report Calculations - JTD Contract Status with MTD - All | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/crystal-report-calculations---jtd-contract-status-with-mtd---all"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/crystal-report-calculations---jtd-contract-status-with-mtd---all"
---

# Crystal Report Calculations - JTD Contract Status with MTD - All

The tables below describe how each column is calculated on this report.

## Projected at Completion

Field
Description

Contract Amount
The amount of the original contract plus the executed and approved change order amounts (through the specified period end date) displays.

Projected Cost
The total projected cost at completion displays from Jobs. The projected formats of the Contract Status Report provide date-sensitive financial information for both projected costs and change order amounts.

Gross Profit
The projected gross profit at completion is calculated as the difference between the contract amount and the projected cost.

Gross Profit %
The projected gross profit percentage at completion is calculated as the gross profit divided by the projected cost, multiplied by 100.

Percent Complete
The percent complete is calculated as the job-to-date actual cost divided by the projected cost, multiplied by 100 for jobs using the percent calculation method for earned revenue. When the percent complete exceeds 100%, it is automatically set to 100%.

If the job earned calculation is Billed or Cost, then the following codes display depending on the price type of the job:

- TM displays if the job price is Time + Material

- C displays if the job price is Cost Plus

- U displays if the job price is Unit Price

## Job-To-Date

Field
Description

Revenue $
Job-to-date earned revenue is calculated as the product of the percent complete and the revised contract amount.
This is the standard percent calculation. The calculation in this field is computed differently if this is a master job and a Method of Calculation is entered in the Jobs Earned Calculation window for the master job:
If Percent is entered in Jobs, then the Job-to-Date Earned amount will be calculated as follows:
Actual cost-to-date
Estimate (=Yes) or Projected Cost (=No)
X Contract Amount
If Cost is entered in Jobs, then the Job-to-Date Earned amount will be calculated as follows:
Actual Cost-to-date + cost markup %
If Billed is entered in Jobs, then the Job-to-Date Earned amount will be calculated as follows:
Actual Billed-to-date + Unbilled amount
If the Jobs Earned Calculation window is set to Master Job Calc, then the Job-to-Date Earned amount will be calculated as follows:
Sum earned of all jobs included in the master job

Profit $
The job-to-date gross profit is calculated as the difference between job-to-date earned revenue and job-to-date actual cost.

## Balance Sheet

Field
Description

Under-billing
When earned revenue exceeds the billed amount, under-billing has occurred. The under-billing figure is calculated as the difference between the billed amount and earned revenue.

Over-billing
When earned revenue exceeds the billed amount, over-billing has occurred. The over-billing figure is calculated as the difference between the billed amount and earned revenue.

## Through Prior Period End

Revenue, cost, and profit figures display for the prior period end.
Field
Description

Earned Revenue
Earned revenue is calculated as the product of the contract amount and the percentage complete during the specified fiscal period.

Actual Cost
The period-to-date actual cost through the prior period end displays.

Gross Profit
The prior period end profit is calculated as the difference between earned revenue and actual cost.

## This Period

Revenue, cost, and profit figures display for the current period.
Field
Description

Earned Revenue
Earned revenue is calculated as the product of the contract amount and the percentage complete during the specified fiscal period.

Actual Cost
The period-to-date actual cost through this period displays.

Gross Profit
The period-to-date profit is calculated as the difference between earned revenue and actual cost.

Gross Profit %
The current period gross profit percentage is calculated as the current period gross profit divided by the current earned revenue, multiplied by 100

## Provision for Loss

Provision should be made for the entire loss on a contract in the period when current estimates of total contract costs indicate a loss. This applies to both the percentage-of-completion method and the completed-contract method.
The following reporting requirements related to the contractor's financial statements should be disclosed:

- The provision for loss should be accounted for in the income statement as an additional contract cost rather than as a reduction of contract revenues.

- Separate disclosure in the balance sheet and income statement is normally required if the loss is material.

- If the loss is not material, the accrual for loss may be included in under or overbillings, and it should be disclosed parenthetically in the notes to the financial statements.

A Provision for Loss amount is typically entered as a reversing journal entry, with the full job to date amount booked each period the adjustment is made.
Field
Description

Summary of Jobs with Provision for Loss
Gross Profit (Projected at Completion) less Gross Profit (Job to Date)
