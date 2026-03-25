---
title: "About the JC Override Projections Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-override-projections-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-override-projections-form"
---

# About the JC Override Projections Form

Use the JC Override Projections form to override
 projected costs by job and month, and set up projected revenue by contract and month.

It is similar to the JC Cost Projections form, except that it tracks projection information at a higher level. Projection values are tracked by month, and are a representation of all information through and including the specified month. Overrides entered in this form do not affect any of the projected amounts in JC Cost Projections.

- Copy Overrides - The Copy Cost Overrides and Copy Revenue Overrides options
 (File Menu) allow you to transfer projected data from the previous month to the
 current month. You will typically only use these options if override projection
 amounts do not change from one month to the next. Click [here](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-overrides-copy-cost-revenue-form) for more information.

- Show Soft Close - Once you have entered the 'through month',
 the Cost and Revenue grids are automatically populated with jobs/contracts
 (respectively) having an 'open' status. However, you have the option to include
 jobs/contracts with a 'soft close' status by selecting the Show Soft Close
 option from the Options menu. When checked, cost/revenue grids will refresh to
 include all jobs/contracts with a status of 2 (Soft Close) that have detail
 existing in JCCD (JC Cost Detail). Note: This
 option is not dependent on the Allow Posting to Soft Closed
 Jobs option in JC Company Parameters, so will not affect
 entering override cost and revenue projections for 'soft closed' jobs. Also,
 once the option is set, it will remain at that setting until
 changed.

- Cost - This tab is used to override costs at the job level. Fore more
 information, see [About Overriding Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-overriding-cost-projections#concept-610--en__concept-610).

- Revenue - This tab is used to override revenue at the contract level. Fore more
 information, see [About Overriding Revenue Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-overriding-revenue-projections#concept-3397--en__concept-3397).

- Future CO and Included CO Amounts - Values displayed in the
 Future CO Amt and Included CO Amt columns on
 both the Cost and Revenue tabs will depend on the how you have set the
 Include in Projections checkbox for the PCO’s document type (in
 PM Document Types) and the Projections Option for the PCO’s status code (in PM
 Status IDs). For more information, see [Future CO / Included CO Amounts for Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/future-co--included-co-amounts-for-projections#concept-9870--en__concept-9870).

- Adjustment Column - This column on each grid will default an amount based on the
 difference between the ‘new override’ amount and the Current Detail Projection
 (Cost) or Current Contract Amount (Revenue) amounts. Any manually entered
 adjustment amount will automatically adjust the new override amount.

- Other Amount Column - This column on each grid is used to track any other value
 (i.e. dollars, hours, etc.) that may be significant to the specified job or
 contract. This is not a required field and does not affect the values in any of
 the other columns. Additionally, this amount is not carried over from month to
 month. This allows separate tracking of additional amounts that are applicable
 to each month only.

- Work in Progress Overrides Report - You can include override information with
 your “work in progress” reporting using the “JC Work in Progress with Overrides”
 report. This report uses the projected override amounts entered here to derive
 the percent complete and the earned revenue. If no override amounts exist for
 the contract amount, the report then uses the current contract through the
 ending month. If no override amounts exist for the estimated cost at completion,
 the report will use projected cost if it exists, otherwise, it will use the
 current estimate.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-overrides-copy-cost-revenue-form)JC Overrides Copy Cost Revenue
