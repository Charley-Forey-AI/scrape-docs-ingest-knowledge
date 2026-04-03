---
title: "Contract Status Calculations | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-contract-status/contract-status-calculations"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-contract-status/contract-status-calculations"
---

# Contract Status Calculations

The following table provides calculation details for each column on the [Job Contract Status](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-contract-status) tab.
Field
Description

Date
The fiscal period-end date displays in this column.

Rev. contract
This column displays the original contract amount of the job plus approved and executed changes at period-end date.

Projected cost
The total projected cost at the period-end date displays in this column.

Gross profit
This column displays the gross profit at contract completion (rev. contract -projected cost).

GP%
The column displays the gross profit percent (rev. contract - projected cost / rev. contract x 100).

Earned revenue
The job-to-date earned revenue is calculated based on the 'earned calculation' type in Jobs:

- Percent: Rev. contract x % complete

- Billed: Bill-to-date + unbilled amount

- Cost: Cost-to-date + cost markup %

- Master job calc: Calculate as for percent

If the job status is set to 'complete', the earned revenue amount for the most recent period (row 1) will be set equal to the 'total billed' amount.

Under billed
If the 'earned revenue' is greater than 'billed-to-date', the difference is calculated in this column. If not, this column will remain blank.

Over billed
If the 'billed-to-date' is greater than 'earned revenue', the difference is calculated in this column. If not, this column will remain blank.

% comp
This column is calculated as 'job-to-date cost' divided by 'projected cost' as of the period-end date multiplied by 100. When the total exceeds 100%, this column will automatically be set to 100%. When the total is less than 0, this column will automatically be set to 0%.
Note: This calculation is different than the one on the Financials tab, and will always be calculated separately, even if the 'Percent complete' method is not applicable for the job as a whole due to the 'earned calculation' method.

Cost history
This column is calculated as actual cost-to-date through the period-end date.

Cost to complete
This column is calculated as 'projected cost' minus 'cost history'. When the 'job-to-date cost' is greater than the 'projected cost' this amount is automatically set to 0. When the job status is 'complete' this amount is automatically set to 0.

Net cost
The actual cost history during the selected period will display in this column.

Appr chgs
This column is calculated as total approved change requests + change orders at period-end date.

Net appr
This column displays the net change in approved change requests and change orders during the selected period. This value represents the total approved changes at period end minus the total in the previous period.

Exec chgs
This column is calculated as the total executed change requests + change orders at period-end date.

Net exec
This column is calculated as the net change in executed change requests and change orders during this period. This value represents the total executed changes at period end minus the total in the previous period.

Total chgs
This column is calculated as the sum of total approved changes + total executed at period-end date.

Net chgs
This column is calculated as total changes at current period-end minus total changes at previous period-end.

Bill history
This column displays the actual billed-to-date through the period-end.

% billed
This column is calculated as 'billed-to-date' / 'revised contract' x 100.

Net billed
This column displays the actual billing history during the period.

Net earned
This column is calculated as earned at current period-end minus earned at previous period-end.

Fiscal yr/per
The column displays the fiscal year and fiscal period (YYYY-MM).
