---
title: "The Update Pay Cycle tracks differences between actual and standard | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/standard-costing-in-payroll/the-update-pay-cycle-tracks-differences-between-actual-and-standard"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/standard-costing-in-payroll/the-update-pay-cycle-tracks-differences-between-actual-and-standard"
---

# The Update Pay Cycle tracks differences between actual and
 standard

The journal entry based on actual costs will be generated
 and posted to the G/L first.
Then any adjustments for standard cost will be calculated
 and added to the transaction. The net value will post the General Ledger using standard
 costs.
To determine any adjustments, the system performs the following:

1. By Payroll Department, identify all with 'Post with standard rates' as selected.

1. Calculate the following to create adjustment journal entries.

- Actual Labor Cost: The actual direct labor cost is stored.

- Standard Labor Cost: Recalculate the labor time card line to post to Job Cost History as the hours multiplied by the standard labor rate found on the wage code.

- Suppress Burden: Suppress posting actual burden to the job.

1. Calculate the difference between actual cost and standard cost by time card line

1. Difference = Standard Labor Cost – Actual Labor Cost

1. The Difference is used to create the following journal entry:

1. Book the Difference to the 'Standard cost variance' G/L code as:

- When the Difference is positive = credit entry

- When the Difference is negative = debit entry

1. Book the offset to this entry using the 'Direct cost adjustment' G/L code.

- When the Difference is positive = debit entry

1. When the Difference is negative = credit entry
Example
Company ABC uses standard labor rates for Job Cost. The employee works 40 hours on job 300 using wage code FM + union code 150FMX. The setup is as follows:
Wage Code FM + Union Code 150FMX

- Employee's pay rate is $35.00/hour.

- The standard job labor rate is $85.00/hour.

Job 300

- Actual Payroll Burden selected.

- No job overhead is defined.

Actual Direct Labor = 40.0 X $35.00 = $1,400.00
Total Standard Labor = 40.0 X $85.00 = $3,400.00
The journal entry will debit the direct labor G/L code for $1,400.00. The Total standard cost labor will then be calculated to "true up" the first entry. Here, a $2.000.00 entry will be added.
The following lines will be added to the existing journal entry:
DR Direct Cost Adjustment 2,000
CR Standard Cost Variance 2,000
Where 3,400 – 1,400 = 2,000.
