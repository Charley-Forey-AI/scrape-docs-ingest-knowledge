---
title: "Vista Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/system-tools/vista-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/system-tools/vista-reports"
---

# Vista Reports

The following discusses new reports, as well as updates made to existing standard reports for the 2021 R2 release.

## A note about security

 When new reports are added, their default security level is set to None, even for users who have Full Access to Vista. When reviewing new reports for this release, determine who should have access to which reports. Add or change security as needed in VA Report Security. Make sure to include any Audit and Distribution reports as permission to access the related batch forms does not automatically give permission to access the audit/distribution reports. You can locate audit/distribution reports in VA Report Security using the Filter bar. Enter Audit in the Type column, and the grid will restrict the list of reports to only audit and distribution reports.
For a list of report defects fixed in this release, click [here](https://support.viewpoint.com/s/browse-cases-and-issues?tabset-d4f10=2) to go to the Track Cases/Issues page of the Viewpoint Customer Portal. Use the filter options to select your product and module. Then in the Fixed In Version field, select this version.

## Accounting

The Vista 2021 R2 release affects reports in the Accounts Payable module. There are no new or changed reports for the Accounts Receivable, Cash Management, or General Ledger modules.
Table 1. New ReportsReportReport IDDescription
AP GL Reconciliation1335This new report is a tool that helps reconcile the differences between payables accounts in the GL and the AP module for a given company and month.
The report displays activity for the given month in these categories:

- AP Line/Detail Inconsistency - This section appears on the report only if there are one or more AP Lines with detail amounts not matching the line amount.

- Direct GL Entries - This section appears on the report only if there are transactions to a payable account from a non-AP module.

- AP Clear - This section appears on the report only if cleared invoices for a month do not net to zero for a particular payable account, and shows the invoices that were included in the AP Clear batches.

- Account Activity - This section always shows on the report, and includes all GL accounts listed in AP Pay Types that had activity in the specified month in AP, GL, or both.

You can drill down to additional levels in any of the above sections for more information. For example, you can drill down in each of the following fields, if displayed, for additional information:

- BatchID - Drilldown displays batch info and attachments

- GL Amount - Drilldown shows the detail from the GL Batch

- AP Amount - Drilldown shows the current AP data for that batch, with an additional drilldown for lines that provides more information about the transaction.

Table 2. Changed ReportsReportReport IDDescription
AP Entry Audit List28This audit report now includes a Ticket field for job-related invoice lines associated with a Field Ticket.
AP Vendor Master List71This report is now titled "AP Vendors - Detail".
AP Vendor Master - Summary70This report is now titled "AP Vendors - Summary".

## Costs and Contracts

The Vista 2021 R2 release affects reports in the Job Billing, Job Cost, and Purchase Order modules. There are no new or changed reports for the PreConstruction or Subcontract Ledger modules.
Table 3. New ReportsReportReport IDDescription
JC Field Ticket Status1336This new report shows the status of Field Tickets, sorted by contract. Tickets are displayed in numerical order, and show the date created, customer PO (if applicable), billing and ticket approved by person, and Period and LTD costs. You can drill down on the Period Cost and LTD Cost fields to see cost detail for the Actual Cost Date range and for the life of the field ticket, respectively. If attachments exists, you can view them using the "Attch" link.

Table 4. Changed ReportsReportReport IDDescription
JB T&M Invoice By Date458These reports now include a Field Ticket line for invoice detail lines associated with a JC field ticket.

JB T&M Invoice By Sequence461
JB T&M Invoice By Sequence with Dates462
JB T&M Invoice Detail 463
JB T&M Invoice FreeForm464
JC Committed Cost Drilldown473This report now includes parameter selections in the header when not printing the cover page.For the Jobs parameter, if you enter a single job, that value displays in the report header. If you enter multiple values (separated by commas), the report header displays as *multiple*. If the parameter is left blank, the header displays "All" for that parameter.

JC Contract Item Master - CO Detail478This report is now titled "JC Contract Items with CO Detail".
JC Contract Item Master - Detail479This report is now titled "JC Contract Items - Detail".
JC Contract Items Master - Summary480This report is now titled "JC Contract Items - Summary".
JC Contract Master - Detail481This report is now titled "JC Contracts - Detail".
JC Contract Master - Summary482This report is now titled "JC Contracts - Summary".
JC Contract Master Start Month Exception1059This report is now titled "JC Contract Start Month Exceptions".
JC Cost Adj Audit List489This audit report now includes a Ticket field for cost adjustment entries associated with a JC field ticket.
JC Cost Totals Drilldown494These reports now include parameter selections in the header when not printing the cover page.For multiple-value selection parameters, if you enter a single value (such as a single job), that value displays in the report header. If you enter multiple values (separated by commas), the report header displays as *multiple*. If the parameter is left blank, the header displays "All" for that parameter.

JC Detail506
JC Job Master518This report is now titled "JC Jobs".
JC Material Audit List525This audit report now includes a Ticket field for material usage entries associated with a JC field ticket.
JC Unit Cost Drilldown554This report now includes parameter selections in the header when not printing the cover page.For multiple-value selection parameters, if you enter a single value (such as a single job), that value displays in the report header. If you enter multiple values (separated by commas), the report header displays as *multiple*. If the parameter is left blank, the header displays "All" for that parameter.

PO Entry Audit List727This audit report now includes a Ticket field for job-related lines associated with a JC field ticket.

## HR and Payroll

The Vista 2021 R2 release affects reports in the Human Resources and Payroll modules.
Table 5. Changed ReportsReportReport IDDescription
HR Codes Master328 This report is now titled "HR Codes".
HR Resource Master362This report is now titled "HR Resources".
HR Resource Master Drilldown363This report is now titled "HR Resource Drilldown".
PR 940 Schedule A976 This report was removed from the Reports menu, as it is no longer being used.
PR 941 Federal Form (prior years)The following PR 941 Federal Form reports were removed from the reports menu, as they are no longer being used.

- PR 941 Federal Form (2012/2013)
 Report ID 765

- PR 941 Federal Form (2014)
Report ID 1243

- PR 941 Federal Form (2015)
Report ID 1266

- PR 941 Federal Form (2016)
Report ID 1296

- PR 941 Federal Form (2017)
Report ID 1309

- PR 941 Federal Form (2018)
Report ID 1317

PR 941 Schedule B766 These reports were removed from the Reports menu, as they are no longer being used.
PR Certified Export Template - eMars (Pre-6.16 version)1298
PR Certified Export Template - LCPtracker (Pre-6.19 version)1300
PR Department Costs (Pre 6.11 version)1294
PR Department Costs by Expense Month (Pre 6.11 version)1295
PR Craft Template Master785This report is now titled "PR Craft Templates".
PR Timecard Entry Audit List857This audit report now includes a Ticket field for job timecard lines associated with a JC field ticket.

## Project Management

The Vista 2021 R2 release affects reports in the Project Management module.
Table 6. Changed ReportsReportReport IDDescription
PM Contract Analysis Drilldown1120These reports now include parameter selections in the header when not printing the cover page.For multiple-value selection parameters, if you enter a single value (such as a single contract), that value displays in the report header. If you enter multiple values (separated by commas), the report header displays as *multiple*. If the parameter is left blank, the header displays "All" for that parameter.

PM Contract Analysis Drilldown - A/NZ1134
PM Contract Status Drilldown984
PM Firm Master643This report is now titled "PM Firms".
PM Project Drilldown686This report now includes parameter selections in the header when not printing the cover page.For multiple-value selection parameters, if you enter a single value (such as a single project), that value displays in the report header. If you enter multiple values (separated by commas), the report header displays as *multiple*. If the parameter is left blank, the header displays "All" for that parameter.

PM Project Master691This report is now titled "PM Projects".

## Job Resources

The Vista 2021 R2 release affects reports in the Equipment Management and Inventory modules. There are no new or changed reports for the Material Sales module.
Table 7. Changed ReportsReportReport IDDescription
EM Department Master165This report is now titled "EM Departments".
EM Equipment Master180This report is now titled "EM Equipment".
EM Usage Audit List232This audit report now includes a Ticket field for job-related equipment usage lines associated with a JC field ticket.
IN Location Master402This report is now titled "IN Locations".

## Service Management

The Vista 2021 R2 release affects reports in the Service Management module.
Table 8. Changed ReportsReportReport IDDescription
SM Labor Allocation Commitment Drill Down1325These reports now include parameter selections in the header when not printing the cover page.For multiple-value selection parameters, if you enter a single value (such as a single job), that value displays in the report header. If you enter multiple values (separated by commas), the report header displays as *multiple*. If the parameter is left blank, the header displays "All" for that parameter.

SM WIP Report1323
SM Monthly Profitability Report1312Added a Work Order Status parameter to report. This new parameter is a multi-value selection parameter, allowing you to enter multiple values separated by commas (New,Complete, etc.)Also added Company totals for WO To-Date Cost, WO To-Date Rev, To-Date Margin, and TD Margin % columns.

## Administration

The Vista 2021 R2 release affects reports in the Viewpoint Administration module. There are no new or changed reports for the Headquarters, Imports, or User Database modules.
Table 9. New ReportsReportReport IDDescription
VA License Usage by Day1333This new drilldown report shows you the number of Vista licenses in use concurrently during the day compared with the current number of licenses purchased by your company.
Once you enter the beginning and ending dates (required), the report displays for each day in the specified range, the maximum concurrent license usage and the utilization rate for each license type (Office and Project Manager). The utilization rate is the ratio of concurrent usage to the number of purchased licenses. If the utilization rate exceeds 100%, it displays in red.
A Login Details button displays for each day where there was license usage for one or both license types. When you click the button, the report drills down into additional information for that day, including time of login, user name, workstation, usage and utilization rate.
Note: This report replaces the VA Logged on Users and VA Maximum License Usage reports.

Table 10. Changed ReportsReportReport IDDescription
VA Logged On Users974These reports were removed from the Reports menu, as they are no longer being used.Both reports were replaced by the new VA License Usage by Day report.

VA Maximum License Usage973
VA Datatype Security by Group/User Report916To improve performance, the following changes were made to the parameters for this report:

- Group Type: (S)ecurity, (P)ayroll, (A)ll - This new parameter is used to specify whether to run the report for a specific security group (defined in VA Security Groups), a specific payroll group (defined in PR Group Master) or all groups (security and payroll).

- Beginning Security Group / Ending Security Group - These parameters were relabeled to Beginning Group and Ending Group to better represent all group types.

- Security (G)roup or (U)ser Detail - This parameter was relabeled to Sort by (G)roup or (U)ser Detail to better reflect its functionality.

VA Form Security924The following changes were made to improve the usability of this report:

- Relabeled the username parameter to User Name.

- Moved the User Name parameter to the top of the list of parameters and made it a required field.

Also added the VA Form Security report to the Options > Reports menu of the VA Form Security and VA Security Groups forms
