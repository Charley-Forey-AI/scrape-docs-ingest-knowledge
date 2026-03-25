---
title: "JC Labor Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/job-cost-reports/job-cost-general-reports/jc-labor-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/job-cost-reports/job-cost-general-reports/jc-labor-report"
---

# JC Labor Report

You can use the JC Labor Report report to compare
 estimated and job to date hours and cost by phase for the labor cost type specified in the
 input parameter by selecting Job Cost > Reports > JC Labor Report.
This report primarily allows you to compare estimated and job to date hours and cost by phase for the labor cost type specified in the input parameter. Users are required to input the labor cost type, but may also include more estimated and actual dollars by entering additional cost types (input parameter). The report also prints Units and UC (unit cost) columns in order to calculate a variance between projected and estimated costs. The variance column subtracts the estimated cost (labor and additional cost types) from a unit based projected calculation, which uses the same logic as the other Viewpoint standard JC Unit Cost reports. See a more a specific explanation of the projected cost calculation below:
Projected Cost calculation. Computes by phase and cost type in the following logical order.
If projection records exist. Projected Cost for labor and addl. cost types.
If actual units exist. (Estimated Units*Est UC) - Estimated Cost.
The Estimated Units and Estimated UC only include units posted to the labor cost type whereas the Estimated Cost will include costs for any of the additional cost types entered.
If actual units = 0. Estimated Cost if not equal to 0, otherwise use Actual Cost. Estimated and Actual Costs include additional cost types entered.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Labor Cost Type
Select the Field Lookup button or press F4 to select the labor cost type.

Add’l Cost Types. 2,3,5,7
Click the Field Lookup
 button or press F4 to select additional cost types – separated
 by a comma. E.g. 2,3,5,7.

Beginning Job
Select the Field Lookup button or press F4 to select the beginning job.

Ending Job
Select the Field Lookup button or press F4 to select the ending job.

Through Date
Enter through date (MM/YY).
