---
title: "JC Backlog Forecast Drilldown \u2013 Rolling 12 | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/job-cost-reports/job-cost-general-reports/jc-backlog-forecast-drilldown--rolling-12"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/job-cost-reports/job-cost-general-reports/jc-backlog-forecast-drilldown--rolling-12"
---

# JC Backlog Forecast Drilldown – Rolling 12

You can use the JC Backlog Forecast Drilldown – Rolling 12
 report to help analyze backlog by showing forecasted revenue, cost or profit for up to 12
 future months by selecting Job Cost > Reports > JC Backlog Forecast Drilldown – Rolling
 12.
This report will help analyze backlog by showing forecasted revenue, cost or profit for up to 12 future months. Based on a parameter, users will have the option of viewing/printing either revenue, cost, or profit forecast amounts from the JC forecast table that are initialized from the JC Contract Master.
The Earned column (see formula below) will show earned revenue or profit (actual costs if run for the cost option) through the month prior to the "Beginning Month" parameter. If the Earned amount is less than the original forecast amount through the prior month, the difference (Forecast - Earned) will show in the "Remaining" column (after the last period column). Conversely, when earned is greater than forecast (in the prior month), the forecasted amounts will only show up to the period where the total to date equals the current contract, cost, or profit (see sample test case illustrating this scenario)
Also, the report will show a summary, along with the ability of drilling down, of potential projects (from the PC module) grouped by 3 ranges of Award Probability. 0 - 50%, 50-75%, 75 - 100%. Finally, contracts without forecast amounts will show the total earned revenue and the backlog remaining in the last column. Drilling down on the "contracts without forecasts" is also possible.
Earned Revenue = earned revenue calculated using the same method as the standard JC Work in Progress reports.
Cost = Actual Cost
Earned Profit = Earned Revenue - Actual Cost.
Access this report by clicking Job Cost > Reports > JC Backlog Forecast Drilldown – Rolling 12.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Beginning Contract
Select the Field Lookup button or press F4 to select the beginning contract.

Ending Contract
Select the Field Lookup button or press F4 to select the ending contract.

Beginning Month
Enter beginning month (MM/YY) for transactions to be included or leave blank for all.

Show Backlog (R)evenue, (C)ost, or (P)rofit
Enter R, C, or P

Sort by Project Manager?
checkbox to sort by project manager.

Include Pending in Monthly Column?
