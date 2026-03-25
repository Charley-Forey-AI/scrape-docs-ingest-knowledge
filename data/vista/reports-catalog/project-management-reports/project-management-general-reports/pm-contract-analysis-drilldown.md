---
title: "PM Contract Analysis Drilldown | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/project-management-reports/project-management-general-reports/pm-contract-analysis-drilldown"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/project-management-reports/project-management-general-reports/pm-contract-analysis-drilldown"
---

# PM Contract Analysis Drilldown

You can use the PM Contract Analysis Drilldown report by
 selecting Project Management > Reports > PM Contract Analysis Drilldown.
The first level of the drilldown lists the contracts with estimates, committed, and actual costs.
On the second level of the drilldown, significant calculations printed on the report include Gross Profit, Earned Revenue, Over/Under Billings, Paid to Date, and Open Payables. Paid to Date is calculated as the Total Actual Costs minus Open Payables. The ProjectedOrEstimated formula, used as the basis for % Complete, will total the projected cost for all phases/cost types assigned to a contract item if at least one phase assigned to that item has a projected amount. Otherwise, the formula will total the current estimated cost for an item when none of the assigned phases have projected costs. Therefore, the final result of the ProjectedOrEstimated formula may include total projected costs for some items and current estimated costs for other items.
The Pending Change Order total represents all change orders entered in PM that do not have an ACO assigned. All SL's and PO's must be interfaced from PM to appear in the committed cost column.
A Cost Type summary for each contract prints estimated, actual, and projected costs. From the second level of the drilldown, each cost type can be selected to see the phase balances which can further be drilled upon to see the transactions that total the actual costs. Also on the phase drilldown level, the committed costs can be selected to see the detail. Attachments included at this level come from AP invoice header, AP invoice line level, JC Adjustments, IN Material Orders, and PR Timecards.
Amounts indicated in blue font can be selected to see detail backup.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Beginning Project
Select the Field Lookup button or press F4 to select the beginning project.

Ending Project
Select the Field Lookup button or press F4 to select the ending project.

Project Manager
Select the Field Lookup button or press F4 to select the project manager or leave blank for all.

Beginning Month
Enter beginning month.

Ending Month
Enter ending month.

Include Cost Types (ie: 2,3)
Enter cost types to include, separated by commas, i.e. 2,3,30 or leave blank for all.
