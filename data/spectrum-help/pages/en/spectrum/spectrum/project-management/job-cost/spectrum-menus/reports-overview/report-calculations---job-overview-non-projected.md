---
title: "Report Calculations - Job Overview, Non-Projected | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/report-calculations---job-overview-non-projected"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/reports-overview/report-calculations---job-overview-non-projected"
---

# Report Calculations - Job Overview, Non-Projected

The following table describes how each column is calculated on this report.

## Heading Information

Field
Description

Original Contract
The amount of the original contract plus the executed and approved change order amounts (through the specified period end date) displays.

Change Orders
The executed change orders amount displays from Jobs.

Revised Contract
The revised contract amount is calculated as the sum of the original contract amount plus the change order amount.

Proposed COs
The dollar amount for all Proposed change orders displays from Accounts Receivable Change Request Log/Entry.

% Complete
If the job earned calculation type is Billed or Cost, then the following codes display depending on the price type of the job:

- TM displays if the job price is Time + Material.

- C displays if the job price is Cost Plus.

- U displays if the job price is Unit Price.

For active and inactive jobs with earned calculation of Fixed Price, the percent complete is calculated as actual divided by estimate, then multiplied by 100. When the percent complete exceeds 100%, it is automatically set to 100%.
If the job earned calculation type is not billed or cost and the job is complete then 100 displays.

% Billed
Percent billed is the billing to date amount divided by the revised contract amount multiplied by 100.

Billed To Date
The billed to date amount displays from Jobs.

Earned To Date
If the job status code equals active or inactive and the job earned calculation equals billed then the earned to date amount is the billed to date amount plus the under billed amount.
If the job status code equals active or inactive and the job earned calculation equals cost then the earned to date amount is the total cost to date plus the markup.
If the job status code equals active or inactive and the job earned calculation does not equals cost or billed then the earned to date amount is the cost to date divided by the projected cost divided by 100 then multiplied by the revised contract amount.
If the job status is complete, then the earned to date amount is the billing to date amount.

Over / Under
The over / under amount is difference between the billing to date amount and the earned to date amount. When earned revenue exceeds the billed amount, under-billing has occurred; when the billed amount exceeds earned revenue, over-billing has occurred.

Billed (With Tax)
The billed with tax amount is the job-to-date billed amount plus the job-to-date tax amount.

Applied
The amount applied by the customer displays among all contracts for the job from Accounts Receivable Contracts.

Balance
The balance is calculated as the difference between the billed with tax amount and the applied amount.

Retention Balance
The retention balance displays from Accounts Receivable Contracts.

Current Due
The current amount due is calculated as the difference between the balance amount and the retention balance amount.

## Report Column Descriptions

Field
Description

Hours
Current Month The actual hours for the current month display for the cost type.
Job to Date The actual job-to-date hours through the year and period display for the cost type.
Estimate Estimated hours for the cost type display from Job Phases.
% Complete The percent complete for the cost type is calculated as the job-to-date hours divided by the estimated hours, multiplied by 100.

Costs to Date
Current Month The costs for the current month display for the cost type.
JTD + Open The actual job-to-date costs through the year and period display for the cost type.
Estimate The estimated costs for the cost type display from Job Phases.
Variance Variance is calculated as the difference between the JTD + Open cost and the estimated cost.
% Complete Percent complete for the cost type is calculated as the JTD + Open cost divided by the estimated cost, multiplied by 100.
Open Commitments Open commitments display from open purchase orders in the Purchase Order module.
