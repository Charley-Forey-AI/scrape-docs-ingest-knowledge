---
title: "Crystal Report Calculations - JTD Contract Status with MTD - Active | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/crystal-report-calculations---jtd-contract-status-with-mtd---active"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/crystal-report-calculations---jtd-contract-status-with-mtd---active"
---

# Crystal Report Calculations - JTD Contract Status with MTD - Active

The following tables describe how each column is calculated on this report.

## Projected at Completion

Field
Definition

Contract Amount
The amount of the original contract plus the executed and approved change order amounts (through the specified period end date) displays.

Projected Cost
The total projected cost at completion displays from Jobs. The projected formats of the Contract Status Report provide date-sensitive financial information for both projected costs and change order amounts.

Gross Profit
The projected gross profit at completion is calculated as the difference between the contract amount and the projected cost.

Gross Profit %
The projected gross profit percentage at completion is calculated as the gross profit divided by the contract amount, multiplied by 100.

Percent Complete
The percent complete is calculated as the job-to-date actual cost divided by the projected cost, multiplied by 100 for jobs using the percent calculation method for earned revenue. When the percent complete exceeds 100%, it is automatically set to 100%.
If the job earned calculation is Billed or Cost, then the following codes display depending on the price type of the job:

- TM displays if the job price is Time + Material

- C displays if the job price is Cost Plus

- U displays if the job price is Unit Price

Revenue
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
If the Jobs Earned Calculation window is set to MasterJob Calc, then the Job-to-Date Earned amount will be calculated as follows:
Sum earned of all jobs included in the master job
Profit $ The job-to-date gross profit is calculated as the difference between job-to-date earned revenue and job-to-date actual cost.

## Job-To-Date

Field
Definition

Earned Revenue
Percent: The percent method is usually selected for fixed price and unit price jobs. This method is used in the contract status report and over report and inquiries for the calculation of the earned amount.
Earned Revenue = % Complete * Revised Contract
% Complete =(JTD Actual / Projected Cost) * 100
Percent Complete = Actual JTD Cost / Projected Cost
Billed: The Billed method is normally used when calculating earned revenue for a T+M job This method prompts the user to enter an unbilled amount, if desired.
Earned Revenue = Billed Amount + Unbilled Amount.
The system will enter TM under the percent complete field on the Contract Status report - MTD and YTD formats.
Cost: The Cost method is used when it is a cost-plus job. The cost method also prompts you to enter in a cost percent, if desired.
Earned Revenue = (Actual Cost x Cost Markup %)
The system will then enter CP under the percent complete field on the Contract Status report – MTD and YTD formats.
Master job method: Select this option when the sub jobs should use the master job's earned revenue calculation.
Sub job method: Select this option when each sub job should use their own earned revenue calculated method and then summarized up into the master job.

Actual Cost
The job-to-date actual cost amount through the year and period displays.

Gross Profit
The job-to-date gross profit is calculated as the difference between the job-to-date earned revenue and the job-to-date actual cost.

Gross Profit %
The job-to-date gross profit percentage is calculated as the gross profit divided by the earned revenue amount, multiplied by 100.

Billed
The actual amount billed to date through the year and period displays.

## Balance Sheet

Field
Description

Under-billing
When earned revenue exceeds the billed amount, under-billing has occurred. The under-billing figure is calculated as the difference between the billed amount and earned revenue.

Over-billing
When the amount billed exceeds earned revenue, over-billing has occurred. The over-billing figure is calculated as the difference between earned revenue and the billed amount.

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
The current period gross profit percentage is calculated as the current period gross profit divided by the current earned revenue, multiplied by 100.

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
