---
title: "JC Contract Profit with Change Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/job-cost-reports/job-cost-general-reports/jc-contract-profit-with-change-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/job-cost-reports/job-cost-general-reports/jc-contract-profit-with-change-orders"
---

# JC Contract Profit with Change Orders

You can use the JC Contract Profit with Change Orders
 report for a summary of revenue, costs and profit by selecting Job Cost > Reports > JC Contract Profit with Change
 Orders.
Like the Contract Profit report, this report summarizes the revenue, costs and profit at the top of the report. Cost information is stored in JCCP (Job Cost by Period) table while the contract and billed amounts are pulled from JCCM (Contract Master) table. Below the profit section, the report has two sections for change orders - approved and pending. So that the figures are consistent with other job cost reports, the report only prints approved change orders that exist in Job Cost. Therefore, pending change orders approved in PM but not yet interfaced are listed in the Pending Change Order section. An asterisk indicates these types of change orders. In order to exclude pending change orders considered rejected, cancelled, etc., from printing on the report, assign the change order a status code where the "Include In Projections" box is unchecked for the status code- See PM Status Codes program.
The next page summarizes the costs for each contract item, phase, and cost type between the beginning and ending months specified by the user. The report pulls the amounts for each of these fields, with the exception of PCO Estimated Cost, from the JCCP table. The source for PCO Estimated Costs is change order cost detail from PM Change Order Lines (PMOL), including non-interfaced approved change orders, and change order add-on amounts from PMOA where the add-on is assigned to a phase/cost type in PM Project Add-ons.
Finally, the Projected Variance column is the difference between Current Estimated and Projected Costs, provided that a projection is posted from JC Cost Projections. If projected costs are 0 and have not been overridden (plugged), the variance will be 0.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Beginning Contract
Select the Field Lookup button or press F4 to select the beginning contract.

Ending Contract
Select the Field Lookup button or press F4 to select the ending contract.

Ending Month
Enter ending month (MM/YY).

Exclude Internal Change Orders
checkbox to exclude internal change orders.
