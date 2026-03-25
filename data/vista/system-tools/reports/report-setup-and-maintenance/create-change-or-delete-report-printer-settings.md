---
title: "Create, Change, or Delete Report Printer Settings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/create-change-or-delete-report-printer-settings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/create-change-or-delete-report-printer-settings"
---

# Create, Change, or Delete Report Printer Settings

The system will only save changes to report printer settings made using
 the Properties button on the Print form if you select the Save Printer Settings With
 Each Report checkbox in User Options (Main
 Menu > Options > User
 Options) or VA User Profile.
These settings are saved (by user login) in the
 RPUP (RP Report Security) table; the system will continue to use the settings until they
 are changed again.Note: The system cannot save printer
 settings applied to sub-reports (the reports shown at each level of a drilldown
 report).
If you clear the
 Save
 Printer Settings With Each Report checkbox after the report settings have
 been saved, the system will retain the settings in the RPUP table but it use the
 standard settings for the report. To delete the settings in the RPUP table, follow
 the steps below.

1. Open the [RP Report Titles](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form) form.

1. In the Report
 ID field, select the desired report ID.

1. Open the Printer/Viewer
 Options tab.

1. Select your User ID in
 the grid.

1.  Click the Delete icon
 in toolbar to delete the user settings.

Note: When generating a report, the system saves the
 parameters in memory. If you refresh or change the parameters and then rerun the
 report, the original parameters are still in effect. To refresh the report
 completely, close the Launcher and reopen to run the report with new parameters.
