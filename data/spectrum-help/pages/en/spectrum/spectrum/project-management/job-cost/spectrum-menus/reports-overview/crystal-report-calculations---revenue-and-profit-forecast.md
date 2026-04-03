---
title: "Crystal Report Calculations - Revenue and Profit Forecast | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/crystal-report-calculations---revenue-and-profit-forecast"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/crystal-report-calculations---revenue-and-profit-forecast"
---

# Crystal Report Calculations - Revenue and Profit Forecast

This report takes the job's remaining revenue forecast and the estimated job completion date and uses the values to make a forecast for the next six months of the revenue for the job (assuming it will be earned equally each month).
Forecast Fiscal Months: This shows the next six accounting periods.
Forecast Revenue: If the job has an estimated completion date, then the forecast revenue for each month is the backlog revenue divided by the number of months until the estimated completion date for the job. Note that if there is not estimated completion date for the job, the entire revenue backlog is forecast into the first month.
Forecast Profit: The forecast profit for each month is the backlog profit divided by the number of months until the estimated completion date for the job. Again, if there is no estimated completion date for the job, the entire forecast profit goes into the first month.
The tables below describe how each column is calculated on this report.

## Projected at Completion

Field
Description

Revenue
The revised contract amount displays from Jobs.

Profit
The projected gross profit at completion is calculated as the difference between the revised contract amount and the total cost.

Months To Complete
The difference between the estimated completion date in the Jobs screen and the date for which the report is being run.

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

## Backlog

Field
Description

Revenue $
The backlog revenue is calculated as the difference between the revised contract amount and the earned revenue amount.
If this job is billed as T+M or cost plus and the revised contract amount is zero (0), then the Revenue amount is also zero (0). In all other cases, Spectrum computes the revenue amount.

Profit $
The backlog gross profit is calculated as the difference between projected gross profit and the job-to-date gross profit.
If this job is billed as T+M or cost plus and the revised contract amount is zero (0), then the Profit amount is also zero (0). In all other cases, Spectrum computes the profit amount.
