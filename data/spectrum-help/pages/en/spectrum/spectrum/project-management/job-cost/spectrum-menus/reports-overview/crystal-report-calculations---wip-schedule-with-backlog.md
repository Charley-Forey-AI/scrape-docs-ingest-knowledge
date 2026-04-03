---
title: "Crystal Report Calculations - WIP Schedule with Backlog | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/crystal-report-calculations---wip-schedule-with-backlog"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/crystal-report-calculations---wip-schedule-with-backlog"
---

# Crystal Report Calculations - WIP Schedule with Backlog

The tables below describe how each column is calculated on this report.

## Original Contract

Field
Description

Contract Amount
The amount of the original contract.

Estimated Cost
The original estimated cost displays from Jobs.

Estimated Profit
The estimated profit is calculated as the difference between the original contract amount and the original estimated cost.

Estimated Gross Profit %
The estimated gross profit percentage is calculated as the estimated profit divided by the original contract amount, multiplied by 100.

## Projected at Completion

Field
Description

Change Orders
The change order amount displays from the Jobs.

Revised Contract
The amount of the original contract plus the executed and approved change order amounts (through the specified period end date) displays.

Total Cost
The total projected cost at completion displays from Jobs.

Gross Profit
The projected gross profit at completion is calculated as the difference between the revised contract amount and the total cost.

Gross Profit %
The projected gross profit percentage at completion is calculated as the gross profit divided by the total cost, multiplied by 100.

## Job-To-Date

Field
Description

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
The job-to-date actual cost amount through the year and period displays.

Gross Profit %
The job-to-date gross profit percentage is calculated as the job-to-date gross profit divided by the job-to-date earned revenue, multiplied by 100.

Billed
The actual amount billed to date through the year and period displays.

## Balance Sheet

Field
Description

Under-billing-
When earned revenue exceeds the billed amount, under-billing has occurred. The under-billing figure is calculated as the difference between the billed amount and earned revenue.

Over-billing
When the amount billed exceeds earned revenue, over-billing has occurred. The over-billing figure is calculated as the difference between earned revenue and the billed amount.

## Backlog

Field
Description

Revenue
The backlog revenue is calculated as the difference between the revised contract amount and the earned revenue amount.
If this job is billed as T+M or cost plus and the revised contract amount is zero (0), then the Revenue amount is also zero (0). In all other cases, Spectrum computes the revenue amount.

Gross Profit
The gross profit is the projected gross profit less the job-to-date gross profit.
If this job is billed as T+M or cost plus and the revised contract amount is zero (0), then the Profit amount is also zero (0). In all other cases, Spectrum computes the profit amount.

Gross Profit %
The backlog gross profit percentage is calculated as the backlog gross profit divided by backlog revenue, multiplied by 100.
