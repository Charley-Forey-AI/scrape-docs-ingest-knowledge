---
title: "PR and AP Superannuation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/payroll-reports/payroll-australia-specific-reports/pr-and-ap-superannuation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/payroll-reports/payroll-australia-specific-reports/pr-and-ap-superannuation"
---

# PR and AP Superannuation

You can use the PR and AP Superannuation report to display
 superannuation contributions for each employee and On-Cost vendor along with their
 associated membership number(s) by selecting Payroll > Reports > PR and AP Superannuation.
This report will display superannuation contributions for each employee and On-Cost vendor along with their associated membership number(s). The reporting period parameters determine the data reported based on the employee or vendor's paid date. Year to date (YTD) totals are calculated and based on the federal fiscal tax year for the reporting period. Only employees or vendors that have been paid within the date range will show along with their current and YTD values. If an employee or vendor has been paid between the start of the tax year but before the beginning date range then the report will not show all their related records. If the user would like to see those employees or vendors then the date range values will need to be expanded, typically to the start and end dates of the tax year.
Display\Parameter Restrictions. Because this report shows both PR and AP data the parameters are a mix of both modules. The PR and AP Company parameter values default the current company. Paid Date is common between both PR and AP result sets as are the sorting and show detail flags. Finally the user can choose whether or not to show AP and/or PR results via their related 'show results' flag.
Data Sources:

- HQCO - main report

- vrptPRSuperannuation - PR sub-report

- vrptAPSuperannuation - AP sub-report

Sub Reports:

- PRSuperannuation

- APSuperannuation

Related Reports. No reports directly related, but there are multiple PR and AP reports that can be run to help validate the data in this report including PR Payroll Register, PR Timecard Entry, AP Invoice, and AP Vendor Payment History Drilldown.
Development Notes. Because the code to get the PR data is a bit more complex than the code to get the AP data this report was designed to keep both aspects separate. That is why this report has a main 'shell' aspect to it that just pulls in parameters and then passes those parameters to a PR sub-report (the original PR Superannuation report modified to work within the shell) and an AP sub-report. Because the AP sub-report returns far less columns when compared to the PR sub-report the AP sub-report is designed to render as Portrait while the PR report renders landscape. This functionality is supported by Crystal Reports 2008 and newer.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

PR Group (Blank for All)
Select the Field Lookup button or press F4 to select the PR group, or leave blank for all.

PR Employee Number (Blank for All)
Click the Field Lookup
 button or press F4 to select the employee number or leave blank for
 all.

AP Company
Click the Field Lookup
 button or press F4 to select the accounts payable company.

AP Vendor Number (Blank for All)
Click the Field Lookup
 button or press F4 to select the vendor number or leave blank for
 all.

Beginning Reporting Period
Enter beginning reporting period (MM/DD/YY).

Ending Reporting Period
Enter ending reporting period (MM/DD/YY).

Show PR Results
checkbox to show payroll results.

Group by (E)mployee or (S)upper Fund
Enter E or S.

Sort by (E)mployee Name or (N)umber
Enter E or N.

Show AP Results
checkbox to show accounts payable results.

Group by (V)endor or (S)upper Fund
Enter V or S.

Sort by (V)endor Name or (N)umber
Enter V or N.

Show Details (applied to both AP and PR)
checkbox to show details.
