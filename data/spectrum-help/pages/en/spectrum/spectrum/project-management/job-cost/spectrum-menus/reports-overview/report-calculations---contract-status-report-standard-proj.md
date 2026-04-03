---
title: "Report Calculations - Contract Status Report (Standard, Proj. Cost = Yes) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/report-calculations---contract-status-report-standard-proj.-cost--yes"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/report-calculations---contract-status-report-standard-proj.-cost--yes"
---

# Report Calculations - Contract Status Report (Standard, Proj. Cost = Yes)

The following tables describe how each column is calculated on this report.
Field
Description

Contract Amount
The amount of the original contract plus the executed and approved change order amounts (through the specified period end date) displays.

% Complete
Percent complete is calculated as the job-to-date actual cost divided by the Projected cost, multiplied by 100 for jobs using the percent calculation method for earned revenue. When the percent complete exceeds 100%, it is automatically set to 100%.

If the job earned calculation is Billed or Cost, then the following codes display depending on the price type of the job:

- TM displays if the job price is Time + Material

- C displays if the job price is Cost Plus

- U displays if the job price is Unit Price

Job-To-Date Earned
The job-to-date earned amount is calculated as the product of the two preceding columns; that is, the revised contract amount multiplied by the percent complete.
This is the standard percent calculation. The calculation in this field is computed differently if this is a master job and a Method of Calculation is entered JobsEarned Calculation window for the master job:
If Percent is entered in Jobs, then the Job-to-Date Earned amount will be calculated as follows:
Actual cost-to-date
Estimate (=Y) or Proj Cost (=N)
X Contract Amount
If Cost is entered in Jobs, then the Job-to-Date Earned amount will be calculated as follows:
Actual Cost-to-date + cost markup %
If Billed is entered in Jobs, then the Job-to-Date Earned amount will be calculated as follows:
Actual Billed-to-date + Unbilled amount
If the Jobs Earned Calculation window is set to 'Master Job Calc', then the Job-to-Date Earned amount will be calculated as follows:
Sum earned of all jobs included in the master job

Billed To Date
The total job-to-date amount billed through the year and period displays.

Over/Under Billed
The amount overbilled or under-billed is calculated as the difference of the two preceding columns; that is, the billed-to-date amount less the job-to-date earned amount.

Actual Cost To Date
The total job-to-date cost through the year and period displays.

Projected Cost
The total projected cost at completion displays from the job file (Jobs or "entered" projected cost; if "entered" is zero, then the projected cost equals the sum of all phases).

Projected Profit
The projected profit is calculated as the difference between the contract amount and the projected cost.

Profit To Date
The profit to date is calculated as the difference between the earned-to-date amount and the actual costs to date.

Cost To Complete
The "cost to complete" column is set to projected cost - actual cost for projected reports. If the projected cost amount is zero, then a negative number will print in the cost to complete column. The cost to complete is set to zero if the projected cost is zero. If the job is complete, the "cost to complete" is set to zero.

Prior Year Earned
The prior year earned revenue recorded in Prior Period Earned Revenue Entry displays.
