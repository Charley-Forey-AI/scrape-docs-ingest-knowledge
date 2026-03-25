---
title: "Associating a Report with a Module | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/associating-a-report-with-a-module"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/associating-a-report-with-a-module"
---

# Associating a Report with a Module

Use the RP Reports by Module form to associate a report with a
 module.
Once you associate a report with a module, you can open the Report from the Reports sub-folder under a module in the Main Menu.
This applies only to reports with an application type of Crystal or SQL Reporting Services (SSRS).
To associate a report with a module:

1. Open the RP Reports by Module form.

1. In the Module field, enter the module that you want to be associated
 with the report. Typically, you will assign reports to associated modules. For
 example, you would assign an AP Vendor report to the AP Reports menu, but not to
 the GL Reports menu.

1. In the Report
 ID field, press F4 to select from a list of
 reports. Standard SSRS reports are available only if the Business Intelligence
 module is turned on.

1. In the Menu Sequence field, enter the sequence number for the report. This field controls the order in which reports display in the specified module’s Reports sub-folder..

1. To make the report
 visible in the Reports sub-menu, select the Active checkbox.

1. Close the RP Reports by Module form. If the report does not display in the Reports sub-menu of the module, you may not have been assigned security permissions for this report in VA Report Security. See VA Report Security for more information.

Related information

- [About the RP Reports by Module Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-module-form)

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)
