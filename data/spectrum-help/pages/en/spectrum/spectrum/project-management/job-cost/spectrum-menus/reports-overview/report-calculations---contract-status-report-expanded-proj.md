---
title: "Report Calculations - Contract Status Report (Expanded, Proj. Cost = Yes) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/report-calculations---contract-status-report-expanded-proj.-cost--yes"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/report-calculations---contract-status-report-expanded-proj.-cost--yes"
---

# Report Calculations - Contract Status Report (Expanded, Proj. Cost = Yes)

The following tables describe how each column is calculated on this report.
Field
Description

Contract Amount
The amount of the original contract plus the executed and approved change order amounts (through the specified period end date) displays.

Projected Cost
The amount of the original contract plus the executed and approved change order amounts (through the specified period end date) displays.

Gross Profit
The projected gross profit at completion is calculated as the difference between the contract amount and the projected cost.

GP%
The projected gross profit percentage at completion is calculated as the gross profit divided by the contract amount, divided by 100.

Percent Complete
The percent complete is calculated as the job-to-date actual cost divided by the projected cost, multiplied by 100 for jobs using the percent calculation method for earned revenue. When the percent complete exceeds 100%, it is automatically set to 100%.

If the job earned calculation is Billed or Cost, then the following codes display depending on the price type of the job:

- TM displays if the job price is Time + Material

- C displays if the job price is Cost Plus

- U displays if the job price is Unit Price

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
The job-to-date actual cost through the year and period displays.

Gross Profit
The job-to-date gross profit is calculated as the difference between the two preceding columns; that is, job-to-date earned revenue less job-to-date actual cost.

GP%
The job-to-date gross profit percentage is calculated as the job-to-date gross profit divided by job-to-date earned revenue, multiplied by 100.

Billed
The actual amount billed to date through the year and period displays.

Overbilling
When the amount billed exceeds earned revenue, over-billing has occurred. The over-billing figure is calculated as the difference between earned revenue and the billed amount.

Underbilling
When earned revenue exceeds the billed amount, under-billing has occurred. The under-billing figure is calculated as the difference between the billed amount and earned revenue.

## Thru Period

Revenue, cost, and profit figures display for two consecutive periods.
Field
Description

Earned Revenue
Earned revenue is calculated as the product of the contract amount and the percentage complete during the specified fiscal period.

Actual Cost
The period-to-date actual cost through the year and period displays.

Actual Cost
The period-to-date profit is calculated as the difference between the two preceding columns -- that is, earned revenue less actual cost.

GP%
The period-to-date gross profit percentage is calculated as the period-to-date gross profit divided by period-to-date earned revenue, multiplied by 100.
