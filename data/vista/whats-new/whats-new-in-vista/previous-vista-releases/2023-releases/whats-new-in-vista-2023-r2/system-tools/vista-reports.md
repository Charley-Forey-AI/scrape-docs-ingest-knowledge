---
title: "Vista Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/system-tools/vista-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/system-tools/vista-reports"
---

# Vista Reports

The following discusses new reports, as well as updates made to existing standard reports for the 2023 R2 release.

## A note about report security

Each new report's default security level is set to None for all users.
When reviewing new reports included with any release:

- determine which users should have access to which reports

- in the VA Report Security form, add or change access as needed

- if you happen to be granting access to batch form reports, consider also any needed access to Audit and Distribution reports, since permission to access a given batch form report does not automatically allow access to other reports.Tip: Use the Filter bar in the VA Report Security form to easily locate audit/distribution reports. In the Type column, enter Audit so the grid displays only audit and distribution reports.

## Accounting

Table 1. Changed ReportsReportReport IDDescription
AP Vendor Payment History72Modified reports to include the option of displaying Viewpoint ePayments details. Select the new Show Viewpoint ePayments Fulfillment Info checkbox to display the following values on the report:

- Paid Date

- Pay Method

- Pay Reference

AP Vendor Payment History Drilldown73
PR Check Print772 Modified reports to display filing status values from the 2020 version of IRS Form W-4 for any employee that has completed that version.Values that are now included on these reports are:

- Filing Status

- Multiple Jobs

- Dependent Amount

- Other Income

- Other Deductions

 These values will display (as defined for the employee) in the upper right corner of report, below the Social Security Number. If the values in any of these fields is null, they will show on the report as follows:

- Filing Status = S

- Multiple Jobs = N

- Dependent Amount = 0.00

- Other Income = 0.00

- Other Deductions = 0.00

For employees that have not submitted the 2020 Form W-4, report will continue to display the Filing Status and Regular Exemptions values.
Note: If you have custom check/eft pay stub reports and wish to include the new W-4 info, it is recommended that instead of trying to modify your custom reports to include the changes made in this release, you create new reports by copying one of the updated reports and then modifying the new copy as needed.
If you do not have the ability to modify your pay stub reports, you may need help from Technical Support or a Development Partner to make the desired changes.

PR Check Print Stub773
PR Check Print Stub by Employee1035
PR Check Print-2-Mail Format1160
PR EFT Remittance800
PR EFT Remittance by Employee1036
