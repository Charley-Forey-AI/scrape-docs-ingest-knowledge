---
title: "Job Billing/Cost Analysis Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/spectrum-menus/sample-reports-overview/job-billingcost-analysis-report/job-billingcost-analysis-report---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/spectrum-menus/sample-reports-overview/job-billingcost-analysis-report/job-billingcost-analysis-report---field-descriptions"
---

# Job Billing/Cost Analysis Report - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Selections

Job Phase
Enter or search for the job phase you want to view.

Cost type
Enter a Cost type.

From date To date
Enter the first date and last dates to be included.

Only include T+M and cost-plus phases?
Leave this checkbox selected to include only Time + Material and cost plus phases on the report. Likewise, if the phase is set to use the job default, only Time + Material and cost plus job phases are included. This excludes fixed price and unit price phases.

Include phases with no activity?
Select this checkbox to include phases/cost types with pre-billing, billing in progress, billing history, and cost history at 0.00.

Price types

Include fixed price jobs?
Leave this checkbox selected to include jobs with a fixed price type on the report. To set up a T+M phase for a fixed price job, see [Set Up a T+M Phase for a Fixed or Unit Price Job](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/job-overview/tm-job-billing-setup/set-up-a-tm-phase-for-a-fixed-or-unit-price-job).

Include T+M jobs?
Leave this checkbox selected to include jobs that are billed as Time +
 Materials on the report. To set up a T + M job, see [Set Up a T+M Job](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/job-overview/tm-job-billing-setup/set-up-a-tm-job).

Include Cost plus jobs?
Leave this checkbox selected to include jobs that are contracted to be billed as Cost plus on the report. To set up a cost-plus job, see [Set Up a Cost Plus Job](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/job-overview/tm-job-billing-setup/set-up-a-cost-plus-job).

Include unit price jobs?
Leave this checkbox selected to include Unit Price Jobs on the report. To set up a T+M phase for a unit price job, see [Set Up a T+M Phase for a Fixed or Unit Price Job](/en/spectrum/spectrum/accounting/time--material/spectrum-menus/job-overview/tm-job-billing-setup/set-up-a-tm-phase-for-a-fixed-or-unit-price-job).

Job status

- Active

- Inactive?

- Complete?

Select the Job status. The Active checkbox defaults to selected.

Variance filter

- All phases

- Under variance

- Over variance

- Variance %

- Variance amount

If the default of All phases is selected, then all phases of the selected jobs will display on the report. If either Under variance or Over variance is selected, then the Variance % and Variance amount boxes become active. Both negative and positive numbers are allowed in these fields.
Under variance
If this option is selected, and a Variance % is specified, the variance of the phase is calculated according to the following formula:
Variance Percent = (Billing Total – Total Cost) / Billing Total x 100 for selected date range
 If a Variance amount is specified, the variance of each phase is calculated according to the following formula:
Variance Amount = Billing Total – Total Cost for selected date range
 Each cost type of each phase is evaluated separately, whether or not it is at variance. If the variance percent and amount calculations are greater than or equal to the amount entered on the start screen, then the phase will not display on the report. If the calculations are less than the start screen amount, then the phase will display.
Example

- Entering a variance of -10.00% returns all variances of -10.00% and below. No positive variances would display on the report.

- Entering a variance of 10.00% returns all variances of 10.00% and below. All positive variances of 1 through 10% plus all negative variances would display.

Over variance
If this option is selected and a Variance % is specified, the variance of the phase is calculated according to the following formula:
Variance Percent = (Billing Total – Total Cost) / Billing Total x 100 for selected date range
If a Variance amount is specified, the variance of the phase is calculated according to the following formula:
Variance Amount = Billing Total – Total Cost for selected date range
Each cost type of each phase is evaluated separately, whether or not it is at variance. If the variance percent and amount calculations are equal to or less than the amount on the start screen, the phase will not display on the report. If the variance calculations are greater than the amount on the start screen, then the phase will display.
Example

- Entering a variance of -10.00% returns all variances of -10.00% and above. Negative variances of -1 through -10% plus all positive variances would display.

- Entering a variance of 10.00% returns all variances of 10.00% and above. Only positive variances of 10% and above would display.
