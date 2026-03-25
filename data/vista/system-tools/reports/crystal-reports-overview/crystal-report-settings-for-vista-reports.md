---
title: "Crystal Report Settings for Vista\u2122 Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/crystal-reports-overview/crystal-report-settings-for-vista-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/crystal-reports-overview/crystal-report-settings-for-vista-reports"
---

# Crystal Report Settings for Vista™ Reports

In order to successfully create or modify Crystal reports in the Vista™ software environment, some of the Crystal Report Options require specific settings to work optimally with Vista software.
Review the following options indicated below in the Crystal Report Designer. Access to these options can be found in the File/Options menu.
The following examples are from the Crystal XI Designer:
Database Tab

- Views and Stored Procedures – Because only the database owner has permissions to see the base tables, the Views and Stored Procedures boxes should be the only settings checked.

- Use Indexes or Server for Speed – This setting enables the server to perform most of the processing rather than Crystal.

- Database Server is Case-Insensitive – Because much of the data in Vista software tables is case sensitive, this option should be unchecked.

- Automatic Smart Linking – DO NOT check this option. Otherwise, Crystal will automatically create unnecessary linking of fields having the exact same name in two or more tables. (Note: This option is not available in Crystal 9.)

Formula Editor Tab

- Default Formula Language – It is recommended that this option be set to Crystal Syntax. As a standard practice, Vista™ creates formulas in Crystal Syntax. Selecting the other choice of Basic Syntax will cause errors when running your reports in Vista. (Note: In Crystal 9, the Formula Language option is under the Reporting Tab.)

Reporting Tab

- Convert Database NULL Values to Default – Crystal uses this default when you create formulas. If the result of a formula is a null value, then this feature will default numeric nulls = 0 and string nulls = “”.

Related information

- [Crystal Report Troubleshooting Tips](/en/vista/vista/system-tools/reports/crystal-reports-overview/crystal-report-troubleshooting-tips)
