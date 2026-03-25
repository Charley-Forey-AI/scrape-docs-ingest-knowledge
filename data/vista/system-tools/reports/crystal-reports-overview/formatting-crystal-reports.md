---
title: "Formatting Crystal Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/crystal-reports-overview/formatting-crystal-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/crystal-reports-overview/formatting-crystal-reports"
---

# Formatting Crystal Reports

The information explained in this topic assumes that Crystal Report users have received intermediate level training from Business Objects and/or previous experience in developing Crystal reports.

1. Determine the data items, views, record restrictions, grouping/sorting, and layout needed to create your report. Refer to the “Viewpoint View Columns” and “Views and Reports by View Type DrillDown” reports.

1. Determine the lay out of the report – headings, columns, margins, fonts, etc.

1. Determine if copying and modifying an existing report will accomplish your reporting need. Look for reports that use the same views, or at least contain views that will link efficiently to any new views needed for your report.

1. Review the predefined templates located in the Templates subfolder of your Viewpoint\Reports folder. They use special report views (beginning with "brv") that can be of help when encountering the following situations:

- Your report requires two detail views

- Table linking results in “many-to-many” relationships.

1. Add and link necessary views to the report by using the ODBC connection in the Crystal Database Expert.

1. Add parameter fields. If not using a predefined template, add defaults for each parameter. Following are some standard guidelines:

- Numeric Beginning Parameters – 0

- Numeric Ending Parameters – 99999… (number of 9’s should equal the length of the database field to be selected in step 7)

- String Beginning Parameters – “ “ (space)

- String Ending Parameters – zzzzzz… (number of “z” characters should equal the length of the database field to be selected in step 7)

- Note: Crystal reports display dates based on the Report Date Format in HQ Company Setup, but do not accept any date parameters other than the United States format. When creating custom, or modifying, reports for companies outside the US, you must ensure that the "ReportDateFormat" parameter is set to convert the date format to US for the report to recognize the date and then convert it.

1. Use the parameters in the Select Expert to filter data for your report. In other words, select database fields to restrict records based on the input parameters entered at the time the report is run.

1. Add sort/group fields to detail section. This makes it easy to find the fields for adding your group levels in step 10.

1. Add amount fields to detail section.

1. Insert Group levels to summarize the data from the main or detail table used in the report. Because detail views seldom are summarized at the level needed for the report, you will almost always need to insert at least a couple of groups.

1. Insert summaries/subtotals in your group levels.

1. Add report to appropriate Report menu. See [Adding Reports to Module Menus](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/adding-reports-to-module-menus).

Related information

- [Crystal Report Troubleshooting Tips](/en/vista/vista/system-tools/reports/crystal-reports-overview/crystal-report-troubleshooting-tips)

- [Adding Reports to Module Menus](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/adding-reports-to-module-menus)
