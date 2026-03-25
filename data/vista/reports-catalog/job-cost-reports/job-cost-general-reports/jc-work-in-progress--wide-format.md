---
title: "JC Work in Progress \u2013 Wide Format | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/job-cost-reports/job-cost-general-reports/jc-work-in-progress--wide-format"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/job-cost-reports/job-cost-general-reports/jc-work-in-progress--wide-format"
---

# JC Work in Progress – Wide Format

You can use the JC Work in Progress – Wide Format report
 by selecting Job Cost > Reports > JC Work in Progress – Wide
 Format.
The report groups by Department or Project Manager (based on the "Sort by
 (D)epartment, (P)roject Manager, (C)ontract" parameter) and Open/Closed Status.
 Below these group headers, the report will print one line per contract with the
 option of sorting four different ways. Contract Number (ascending), Start Month
 (ascending), Contract Amount (descending), or Estimated Gross Profit (descending).
 If "C" is selected for the "Sort by (D)epartment, (P)roject Manager, (C)ontract"
 parameter, the report will summarize by contract only with same option for sorting
 by Start Month, Amount, or Estimated GP.
In addition to the normal criteria filtered by the report parameters, the report will only include open contracts as well as contracts closed in the prior or current fiscal year (based on the closed month in the JC Contract Master). Pending and Potential projects will print after grand totals if included.
If the number of columns specified by the user spans the width of a page, the same contracts will repeat on subsequent pages beginning with the next column after the last one on the previous page. Optionally, users can also change the paper size, such as legal or 11 X 17 in the print dialog in order to fit more columns on a single sheet of paper. If all possible columns are chosen, the amount of information will exceed 17 inch paper width.
****************************
Calculated Column Definitions:
Gross Profit columns. (Earned Revenue) - (Actual Cost) (displayed as a percentage).
Adjustments. (Estimated Revenue at Completion) - (Current Contract).
Estimated Revenue at Completion. Revenue Override if entered in JC Override Projections in the same month as the Through Month parameter, and parameter "Include Overrides in Estimated Revenue at Completion?" = Y. Otherwise, the field accumulates projected revenue or current contract amount by contract item (uses projected revenue first if exists, else uses current contract).
Estimated Cost at Completion. Cost Override if entered in JC Override Projections in the same month as the Through Month parameter, and parameter "Include Overrides in Estimated Cost at Completion?" = Y. Otherwise, the field accumulates projected cost or current estimated cost by job/phase/cost type (uses projected cost first if exists, else uses current estimated cost).
Earned Revenue. % Complete (Actual Cost/ Estimated Cost at Completion)*Estimated Revenue at Completion, unless Estimated Cost at Completion exceeds Estimated Revenue at Completion
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Beginning Contract
Select the Field Lookup button or press F4 to select the beginning contract.

Ending Contract
Select the Field Lookup button or press F4 to select the ending contract.

Department (Blank for All)
Click the Field Lookup button or press
 F4 to select the department or leave
 blank for all.

Project Manager (Blank for All)
Click the Field Lookup button or press
 F4 to select the project manager or
 leave blank for all.

Sort by (D)epartment, (P)roject Manager, (C)ontract
Enter D, P, or C.

Through Month
Enter through month (MM/YY).

Prior Fiscal Year End Month
Enter prior fiscal year end month (MM/YY).

One Line Summary for Closed Contracts?
checkbox to have a one line summary for closed contracts.

One Line Summary for Small Contracts?
checkbox to have a one line summary for small contracts.

Small Contract Threshold
Enter threshold amount for small contracts if summarizing.

Include Overrides in Estimated Revenue at Completion?
checkbox to include overrides in estimated revenue at completion amount.

Include Overrides in Estimated Cost at Completion?
checkbox to include overrides in estimated cost at completion amount.

Include Contract Original + Change Order Columns?
checkbox to include both original contract and change order columns.

Prior Year Section Order (1 – 4, 0 = Omit)
Enter 0 - 4

Current Year Section Order (1 – 4, 0 = Omit)
Enter 0 - 4

Current Month Section Order (1 – 4, 0 = Omit)
Enter 0 - 4

Backlog Section Order (1 – 4, 0 = Omit)
Enter 0 - 4

Sort Contracts by (C)ontract Number, Contract (A)mount, Estimated (G)ross Profit, Start (M)onth
Enter C, A, G, or M

Include Pending and Potential Projects?
checkbox to include pending and potential projects.
