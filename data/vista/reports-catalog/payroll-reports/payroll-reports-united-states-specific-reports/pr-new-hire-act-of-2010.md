---
title: "PR New Hire Act of 2010 | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/payroll-reports/payroll-reports-united-states-specific-reports/pr-new-hire-act-of-2010"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/payroll-reports/payroll-reports-united-states-specific-reports/pr-new-hire-act-of-2010"
---

# PR New Hire Act of 2010

You can use the PR New Hire Act of 2010 report by
 selecting Payroll > Reports > PR Certified Export Template -
 eMars.
This report selects qualified employees under the HIRE Act of 2010. In order for a qualified employee to be reported, the employees start date must be entered in the New Hire Act Employee Eligibility Date Start field.
This report needs to be run prior to the PR 941 Federal Form report. It will generate a summary box referencing parameter fields on the PR 941 Federal Form. Use these values as input parameters when running the quarterly PR 941 Federal Form report.
Since the first quarter was finishing at the same time the HIRE Act of 2010 became law, the first quarter credits pay periods including March 19th - March 31st and will be reported in the second quarter (fields 12c and 12d) on the PR 941 Federal Form. Running the report with a quarter end date of 6/30/2010 will calculate fields 12c and 12d for the first quarter (March 19th - March 31st) and fields 6a, 6b, and 6c for the second quarter.
For the third and fourth quarters this report will calculate the following fields for PR 941 Federal Form: 6a Number qualified employees’ first paid exempt wages/tips this quarter, 6b Number of qualified employees paid exempt wages/tips this quarter and 6c Exempt wages/tips paid to qualified employees this quarter. Fields 12c and 12d will always be zero for the third and fourth quarters.
When the detail option of the report is selected (Recommended), it lists the eligible wages for each pay period in the quarter. Qualified employees with their FICA liability code not set up properly prior to running a pay period will have their data displayed on the report after they have been appropriately set up. However, liability amounts would have been paid and will be displayed in the amount column.
All calculations are based on date the payment was recorded (PRSQ.PaidDate). The paid date is the date used to determine employee's monthly accumulation.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Date The Quarter Ended
Enter quarter end date.

FICA Social Security Liability Code
Click the Field Lookup
 button or press F4 to select the FICA social security liability
 code.

(D)etail or (S)ummary
Enter D or S.

Sort by Employee (S)ort Name or (N)umber
Enter S or N.
