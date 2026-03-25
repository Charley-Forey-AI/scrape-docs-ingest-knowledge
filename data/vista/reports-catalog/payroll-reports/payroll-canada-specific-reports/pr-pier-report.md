---
title: "PR PIER Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/payroll-reports/payroll-canada-specific-reports/pr-pier-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/payroll-reports/payroll-canada-specific-reports/pr-pier-report"
---

# PR PIER Report

You can use the PR PIER Report report to show discrepancies between actual, accumulated CPP and EI deduction amounts in the employee's payroll for the tax year.

This report shows discrepancies between actual, accumulated CPP, CPP2, and EI deduction amounts in the employee's payroll for the tax year, and required amounts per the CRA calculation formula for multiple pay periods or year-end verification.
Payroll amounts are aggregated for the tax year from employee accumulations (PREA), supplemented by amounts that exist only in employee pay sequence totals (PRDT). Thus, amounts are included from all processed payrolls (before or after payment, before or after update to accumulations). The report may be run for a given tax year any time after processing of the first payroll whose end date falls within the year. Results reflect year-to-date values as of the end date of the latest payroll processed in the year.
Minor discrepancy amounts (up to $1.00) should be expected as a result of rounding of deduction amounts in payroll processing. To exclude employees with minor discrepancy amounts, specify a threshold dollar value for the relevant parameter.
This report requires that Box 14 be configured for the tax year on the T4 Box Items tab of the PR Canada T4 form. Further, the report may be run only for a year that appears in the F4 lookup for the Tax Year parameter on the report launcher. If the desired year does not appear in the lookup, apply the Vista tax update for the year. Finally, for accurate results whenever the report is run, the value specified for Pay Periods Per Year in the PR Groups form -- for each payroll group associated with an employee included in the results -- must be appropriate for the tax year specified for the report.
In the event that an employee has a "balance forward" in employee accumulations (PREA) during the tax year without supporting detail in employee pay sequence totals (PRDT), the report may calculate inaccurate values for the employee's count of pay periods with pensionable earnings, required CPP contributions, and CPP discrepancy. This is due to the lack of payroll detail required for the calculations. For such an employee, you should calculate those values manually. Other report values for the employee are not affected by the "balance forward" condition.
Note: This report is not intended for evaluating amounts for any employee that has worked in Quebec at any time during the tax year. This report uses the calculation formula specified by the CRA in Appendix 3 of Publication T4001 (Employers Guide - Payroll Deductions and Remittances). That formula is the only one authorized by the CRA for verification of employee contribution amounts. The formula does not take employment within Quebec into consideration (e.g., it disregards the effects of QPP on payroll calculations for CPP). Consequently, this report may yield inaccurate results for any such employee.

Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Tax Year
Select the Field Lookup button or press F4 to select the tax year.

PR Group (Blank for All)
Select the Field Lookup button or press F4 to select the PR group, or leave blank for all.

Beginning Employee
Select the Field Lookup button or press F4 to select the beginning employee.

Ending Employee
Select the Field Lookup button or press F4 to select the ending employee.

Exclude employees with discrepancy amounts less than
Enter maximum amount of discrepancy to which employees will be excluded from the report.

Sort by Employee (S)ort Name or (N)umber
Enter S or N.
