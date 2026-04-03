---
title: "Time Card History Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/payroll-reports/time-card-history-report/time-card-history-report---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/payroll-reports/time-card-history-report/time-card-history-report---field-descriptions"
---

# Time Card History Report - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/ButtonsDescriptions
EmployeeEnter the code of the employee to be included on the report, or press Enter to include ALL the employees.
DepartmentEnter the code of the department to be included on the report, or press Enter to include ALL departments.
JobEnter the number of the job to be included on the report, or press Enter to include ALL jobs.
Pay typesEnter the pay type to include on this report, or press Enter to include ALL pay types. You can also enter an add-on or deduction code for entries recorded in the time card file.
For example, you can use the SuperSelect options to display only vacation time on the report. In this case, the Detail format would provide one line on the report for each time card line of vacation; the Summary format would show one line of vacation per employee within the date range specified.

Check dateEnter the first and last check dates to include on this report, or press Enter to begin with the first check date and end with the current Payroll processing date.
Sort bySelect a sort format for the report.
Report formatNote: Available only if the Sort by field is set to Employee or Employee alpha reference.

- Summary - prints one line per pay type per employee.

- Detail  - prints each time card line separately.

- Retro pay - the time card lines serve as the source for the retro pay calculation. This format shows the starting screen selections for check date, employee, department, job, and pay types refer to the retro paycheck (allocated to the penny), not the original source details.

- Detail CSV - export as a CSV file for deeper analysis. Report headers appear only once, at the top of the CSV file.

Job burden optionsIf the Job with burdens sort option was selected above, select whether to Include pre-time cards. If selected, specify the work date through which to report pre-time cards.
Check cost center
Cost groupNote: Displays only if cost centers are enabled in the current company. If you have a user-defined cost group label specified in Enterprise Installation, the field name may differ.
This field works as a filter that allows you to include only a portion of the records you have security for, thereby allowing reports to be produced for a segment of employees.
The application does NOT check for authorization of individual cost centers contained within the specified cost group to determine permission for the check cost center.
