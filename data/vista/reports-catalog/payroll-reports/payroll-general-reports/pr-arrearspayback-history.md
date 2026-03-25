---
title: "PR Arrears/Payback History | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/payroll-reports/payroll-general-reports/pr-arrearspayback-history"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/payroll-reports/payroll-general-reports/pr-arrearspayback-history"
---

# PR Arrears/Payback History

You can use the PR Arrears/Payback History report to
 display life-to-date arrears, payback, and balance amounts for employees and deduction
 codes, as well as details of arrears and payback activity by selecting Payroll > Reports > PR Arrears/Payback History.
This report displays life-to-date arrears, payback, and balance amounts for employees and deduction codes, as well as details of arrears and payback activity.
Generally, an employee/deduction code combination is included in the report if it has a current life-to-date balance other than zero, or if it has any arrears or payback activity within the specified date range. All life-to-date amounts displayed in the report are current as of the date on which the report is run. For any employee/deduction code combination that is included in the report, all arrears and payback activity that occurred within the specified date range is displayed (or, more precisely, is available for display in the Detail format).
The report may be run for one PR Company. If a value is supplied for the optional PR Group input, then the results are restricted to employees that currently belong to the specified payroll group; if left blank, no such restriction applies. The results may be sorted by employee or by deduction code. The optional Beginning Employee and Ending Employee inputs restrict the results to employees within the specified range. Similarly, the optional Deduction Codes input restricts the results to specified deduction codes only. If you wish to specify several deduction codes, you must separate the values with commas (e.g.: 1, 3, 10). The optional Beginning Activity Date and Ending Activity Date inputs restrict the details of arrears and payback activity included in the report. An employee/deduction code combination that has a current life-to-date balance of zero will be included in the report only if it has activity within the specified date range, whereas an employee/deduction code combination with a balance other than zero will be included whether or not it has any activity within the specified date range.
The Summary format displays only life-to-date amounts for each employee/deduction code combination; the Detail format also displays details of any arrears or payback activity within the specified date range. The Threshold flag, when cleared, restricts the results to employee/deduction code combinations with current life-to-date balances that meet or exceed their respective reporting arrears thresholds; when this flag is set, no such restriction applies.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

PR Group
Select the Field Lookup button or press F4 to select the PR group, or leave blank for all.

Beginning Employee
Select the Field Lookup button or press F4 to select the beginning employee.

Ending Employee
Select the Field Lookup button or press F4 to select the ending employee.

Deduction Codes (eg: 1,3,10) (Blank for All)
Enter deduction codes separated by comma, e.g. 1,3,10, or leave blank for all.

Beginning Activity Date
Enter beginning activity date.

Ending Activity Date
Enter ending activity date.

(S)ummary or (D)etail Format
Enter S or D.

Include Employee/Dedn Codes Below Reporting Arrears Threshold
checkbox to include employees or deduction codes that are below the reporting arrears threshold amount.

Summary Option

Detail Option
