---
title: "Report Calculations - Job Overview Report, Non-Projected Cost | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/report-calculations---job-overview-report-non-projected-cost"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/report-calculations---job-overview-report-non-projected-cost"
---

# Report Calculations - Job Overview Report, Non-Projected Cost

The following table describes how each column is calculated on this report.

## Header Information

Field
Description

Original Contract
The amount of the original contract plus the executed and approved change order amounts (through the specified period end date) displays.

Executed Changes
The dollar amount for all executed change orders displays from Job.

Approved Changes
The dollar amount for all approved change orders displays from Job.

Revised Contract
The revised contract amount is calculated as the sum of the original contract amount plus the Change order amount.

Proposed Change Orders
The dollar amount for all Proposed change orders displays from Accounts Receivable Change Request Log/Entry.

% Complete
For active and inactive jobs with earned calculation of Fixed price, the percent complete is calculated as actual divided by Estimate, multiplied by 100. When the percent complete calculation exceeds 100%, it is automatically set to 100%. For completed jobs, the percent complete is always automatically set to 100%.
If the job earned calculation is Billed or Cost, then the following codes display depending on the price type of the job:

- TM displays if the job price is Time + Material.

- C displays if the job price is Cost Plus.

- U displays if the job price is Unit Price.

Billed To Date
The actual amount billed to date among all contracts for the job through the year and period displays.

Earned To Date
The job-to-date earned amount among all contracts for the job is calculated as the product of the revised contract amount multiplied by the percent complete.
This is the standard percent calculation. The calculation in this field is
 computed differently if a Method of Calculation is entered the Job > File > Maintenance > Price window for the master job:
If (P)ercent is entered in Job, then the Job-to-Date Earned amount will be calculated as follows:
 Actual cost-to-date
 Estimate
 X Contract Amount
If (C)ost is entered in Job, then the Job-to-Date Earned amount will be calculated as follows:
 Actual Cost-to-date + cost markup %
If (B)illed is entered in Job, then the Job-to-Date Earned amount will be calculated as follows:
 Actual Billed-to-date + Unbilled amount.

Over/Under
Over/under-billing is calculated as the difference between the billed amount and the amount earned. When earned revenue exceeds the billed amount, under-billing has occurred; when the billed amount exceeds earned revenue, over-billing has occurred.

Paid
The total amount paid by the customer among all contracts for the job displays from the Accounts Receivable Contracts.

Balance
The balance due is calculated as the difference between the amount billed and the amount paid.

Retention Balance
The retention balance displays from the Accounts Receivable ContractFile Maintenance.

Current Due
The current amount due is calculated as the difference between the balance less the retention balance.

## Hours

Field
Description

Period
Actual hours display for the month specified.

Job To Date
Actual job-to-date hours through the year and period display.

Estimate
Estimated hours for the job display from Job Phases.

% Complete
The percent complete is calculated as actual hours divided by estimated hours, multiplied by 100.

## Costs To Date

Field
Description

Period
Costs to date for the specified period display.

Job To Date
Actual job-to-date costs through the year and period display.

Estimate
The total estimated costs for the job display from Job Phases.

Variance
Variance is calculated as the difference between the actual cost-to-date less the job's estimated cost.

% Complete
Percent complete is calculated as the actual cost divided by the estimated cost, multiplied by 100.

Open Commitments
Open commitments display from open purchase orders in the Purchase Order module.

Gross Profit
Gross profit displays for actual and estimated job costs, and for variance. These figures are calculated as follows:
- Job-to-date gross profit equals earned-to-date less actual job-to-date.
- Estimated gross profit equals the revised contract amount less the estimated amount.
- Variance gross profit equals the difference between job-to-date and estimated gross profits.

GP%
The gross profit percent displays for actual and estimated job costs, and is calculated as follows:
- Job-to-date gross profit percent equals job-to-date gross profit divided by earned to date, multiplied by 100.
- Estimated gross profit percent equals the estimated gross profit divided by the revised contract amount, multiplied by 100.
