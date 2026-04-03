---
title: "Calculating Cash In Total | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/calculating-cash-in-total"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/calculating-cash-in-total"
---

# Calculating Cash In Total

The Cash in total for Job Analysis Inquiry will be calculated using the following formula:

## Job-to-date Total Billed

The software will read the Job Cost Billing History Table (JC_ALT_BILLING_MC) to determine the total billed to-date for the job. This will calculate by summing records for the particular job.

## Job-specific Accounts Receivable Outstanding Balance

The software will read the Accounts Receivable Open Items Table (CR_OPEN_ITEM_MC) to determine the balance due for transactions referencing the particular job:

- Find transactions referencing the Job (Job_Number) with non-zero outstanding balance (Invoice_Balance): Transaction types include Invoice, Credit Memo, Payment and Adjustment

- Adjust the outstanding balance by any sales tax included on the Invoice or Credit memo total:

- If the entire balance of the item is outstanding (that is, no partial payment), the adjusted outstanding balance will equal "Total due minus Sales tax"

- If a partial payment has been applied to the item, the adjusted outstanding balance will equal ("Total due minus Sales tax") times ("Total due minus Applied amount" divided by "Total due")

The Cash in total will be calculated as the Job-to-date Total Billed amount minus the Job-specific Accounts Receivable Outstanding Balance amount.
