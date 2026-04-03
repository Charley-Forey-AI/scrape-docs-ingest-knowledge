---
title: "The Update Pay Cycle will post to Job Cost using Standard Labor Rates. | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/standard-costing-in-payroll/the-update-pay-cycle-will-post-to-job-cost-using-standard-labor-rates."
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/standard-costing-in-payroll/the-update-pay-cycle-will-post-to-job-cost-using-standard-labor-rates."
---

# The Update Pay Cycle will post to Job Cost using Standard Labor Rates.

When standard labor costs are used, the update will
 suppress posting burden to jobs. By time card, the system identifies all wage codes with 'Post
 with standard rates' option selected.
The following explains how labor is posted to Job Cost:

- Employee: Unless the employee is marked as a confidential employee, it will continue to write the employee code and name to Job Cost as in past versions.

- Actual Hours: Unless the employee is marked to suppress hours, it will continue to write hours to Job Cost as in past versions.

- Hourly Rate: Continue to post the hourly rate, but use the standard labor rate found on the wage code.

- Standard Labor Cost: Recalculate the labor time card line to post to Job Cost History as the hours multiplied by the standard labor rate found on the wage code. In the event that the standard labor rate is zero or <BLANK>, the standard labor cost will be zero.

- No Burden: When using standard labor rates, no actual or percentage burdens will be charged to the job.

- Overhead: If defined on the job, overhead will continue to charged to the job as in past versions. The percentage method is based on the actual labor cost and burdens.
