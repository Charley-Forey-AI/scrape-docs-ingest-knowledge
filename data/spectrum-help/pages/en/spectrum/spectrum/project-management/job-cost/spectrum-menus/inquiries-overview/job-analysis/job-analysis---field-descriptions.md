---
title: "Job Analysis - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-analysis/job-analysis---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-analysis/job-analysis---field-descriptions"
---

# Job Analysis - Field Descriptions

A reference for completing the fields on this screen.
FieldsDescriptions
Job codeThe selected job number and description. If the selected job is a Master job, the Job code field is labeled Master job and the grid includes amounts from sub-jobs for the master.
Job status (Current status)
Revised contractThe revised contract amount, calculated as the sum of the original contract dollar amount and the approved and executed change order dollar amounts. If the selected job is a Master job, sub-job values are included in this amount.
Gross profitThe revised contract amount, calculated as 'Revised contract' minus 'Projected cost' as of the period-end date associated with the current Job Cost processing date.
Gross profit %The gross profit %, calculated as 'Gross profit' divided by 'Revised contract'.
Committed costThe current open commitment total. If the selected job is a Master job, sub-job values are included in this amount.
Select the dropdown arrow to view the [Open Commitments window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-analysis/open-commitments-window). The open commitment calculation includes use tax recorded on purchase orders and job requisitions.

Earned revenueThe earned revenue amount on this job.
Select to view the [Job Contract Status](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-contract-status) screen (given that you have security authorization).
If the status is set to complete, this amount is set equal to the 'Total billed' amount (across all contracts for the job).
If the status is not set to complete, the earned revenue amount is based on the 'Earned calculation' method for this job:

- Percent or Master job calculation - *Percent complete x Revised contract*

- Cost - *Actual cost-to-date + cost markup %*

- Billed - *Billed-to-date + unbilled amount*

Over/under billedThe amount over-billed/under-billed on this job, if any. This value the difference between the amounts earned and billed-to-date. Positive values indicate the job is over-billed; negative values indicate the job is under-billed.
Cost to completeCalculated by subtracting the 'Job-to-date' cost from the 'Projected cost'. This amount is zero when either is true:

- The 'Job-to-date' cost is greater than the 'Projected cost'

- The job status is set to complete

% completeCalculated as the job-to-date actual cost divided by the projected cost.

- If the job status is set to complete, this value is automatically set to 100%.

- If the job is active or inactive AND the job's "price type" method is Time + Material (TM) or Cost Plus (CP), the corresponding code displays in this field.

- If the selected job is a Master job, the value is calculated using the master job total values (rather than those of the current job) when the price type is 'Fixed price' or 'Unit price'.

Cash flow
Cash inCalculated as the Job-to-date Total Billed amount minus the Job-specific Accounts Receivable Outstanding Balance amount. Refer to the [Calculating Cash In Total](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/calculating-cash-in-total) document for specific calculation details. If the selected job is a Master job, sub-job values are included in this amount.
Cash outCalculated by taking the cost-to-date amount from Job Cost History for all transactions on the job, and then subtracting the outstanding Accounts Payable balances (that is, open invoices and credit memos). If the selected job is a Master job, sub-job values are included in this amount. Note: The cash out calculation for open invoices with multiple jobs referenced in the distribution include the *entire open balance* within the total of the last referenced job. If this yields undesirable results, Accounts Payable invoices referencing multiple jobs should not be entered as a single invoice transaction.

Net cash flowCalculated as 'Cash in' minus 'Cash out'. If the selected job is a Master job, the value is calculated using the master job total values (rather than those of the current job).
Job info - select to view the [Job Cost Analysis Inquiry - Job Info window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-analysis/job-cost-analysis-inquiry---job-info-window).
Contract #The Contract # from the Jobs screen.
Job create dateThe Job create date from the Jobs screen.
Last cost dateThe Last cost date from the Jobs screen. If the selected job is a Master job, the latest date from both master and sub-jobs.
Cost and hours
CostCost totals for the job, including:

- JTD actual cost as of the period-end date associated with the current Job Cost processing date, plus other conditional amounts.

- [Projected Cost by Period window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-analysis/projected-cost-by-period-window) costs, regardless of the Job Cost processing date.

- The sum of current estimated costs of all phases.

- Cost variance (Projected cost - Estimate) as of the specified period-end date, when projected cost is shown.

- Variance % as of the specified period-end date.

 If the selected job is a Master job, sub-job values are included in the Job-to-date, Projected, and Estimate costs.
Labor hoursLabor hour totals for the job, including:

- Actual hours (all cost types) as of the period-end date associated with the current Job Cost processing date, plus other conditional amounts.

- Projected hours.

- The sum of current estimated hours of all phases.

- Hours variance (Projected hours - Estimate) as of the specified period-end date, when projected cost is shown.

- Variance % as of the specified period-end date.

 If the selected job is a Master job, sub-job hours are included in the Job-to-date, Projected, and Estimate hours.
Primary contract
CustomerThe customer code and description from the Jobs screen. Tip: If more than one contract exists for this job, a hyperlink indicates how many. Select the link to open the Contracts screen.

Original contractThe original contract amount from the Contracts screen.
Executed changesThe current total of executed changes for the designated contract (job + customer).
Select the dropdown to open the Change Orders window for the designated contract, showing executed change orders.

Approved changesThe current total of approved changes for the designated contract (job + customer).
Select the dropdown to open the Change Orders window for the designated contract, showing approved change orders.

Revised contractThe revised contract amount, calculated as the sum of the original contract dollar amount and the approved and executed change order dollar amounts.
Proposed changesThe current total of proposed changes for the designated contract (job + customer).
Select the dropdown to open the Change Requests window for the designated contract, showing proposed change requests only.

Price typeThe price type from the Job Cost Maintenance screen (Fixed, Unit Price, Time + Material or Cost Plus).
Note: If the *contract* is set to 'Use unit pricing' in the Contracts screen, the value shown is Unit price no matter the setting in the Job Cost Maintenance screen.

Contract dateThe Contract date from the Contracts screen.
Billed-to-dateThe billed-to-date total as of the period-end date associated with the current Job Processing date. Select the dropdown to view the [Job Billing History](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/job-billing-history) screen.
Sales taxCalculated by summing sales tax amounts on A/R invoices with G/L dates through the specified period-end date.
AppliedThe total amount applied to date (paid) by the customer on the contract.
Select the link to open the [Contract Payment History](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-financials/contract-payment-history) screen with the job and customer in context.

A/R balanceThe total A/R balance for the contract, calculated as the difference between the amounts billed and paid. Select the drill-down button to the right of this amount to open the Contract Detail Inquiry window.
Select the link to open the Contract Open Items screen with the job and customer in context.

Retention dueThe retention balance from the contract file.
Current dueThe current amount due, calculated as the difference between the total balance and retention amounts.
Last billed date Last paid dateThe last billed and paid dates from the Contracts screen.

Related information

- [Job Main Properties](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-main-properties)

- [Cost Activity](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/cost-activity)
