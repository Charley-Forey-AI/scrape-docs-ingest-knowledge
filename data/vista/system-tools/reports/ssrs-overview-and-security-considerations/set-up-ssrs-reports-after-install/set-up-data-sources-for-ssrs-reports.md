---
title: "Set Up Data Sources for SSRS Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/set-up-ssrs-reports-after-install/set-up-data-sources-for-ssrs-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/set-up-ssrs-reports-after-install/set-up-data-sources-for-ssrs-reports"
---

# Set Up Data Sources for SSRS Reports

If the data sources on SSRS reports are set up to use the credentials that are supplied by the user running the report, you must set the reports up correctly to display in Vista. This applies to shared data sources that you have created yourself, and any custom reports with a custom data source. This does not apply to reports in the Standard folder or the standard shared data source; both of these are set up by the SSRS Reports installer

1. Open the SSRS Report Manager (generally http://<server name>/Reports).

1. Check the setup on each shared data source that you have created. If you have not created your own data source, you can skip this step. You do not need to do this for the Viewpoint shared data source since it was configured during installation.

1. Locate the data source.

1. Move the cursor over the data source, click on the drop-down that appears, and select Manage.

1. If the Credentials supplied by the user running the report check box is selected, select the Use as Windows credentials when connecting to the data source checkbox.Note: If the Credentials stored securely in the report server box is checked, and valid user and password exists, you do not have to change anything.

1. Click Apply.

1. Repeat the steps above for each remaining data source.

1. Check that each custom report in Vista has a valid data source.

1. Move the cursor over a custom report. For example, use a report in the Custom folder.

1. Click the drop-down that appears and select Manage.

1. Open the Data Sources tab.

1. If the A shared data source box is checked, verify that the referenced data source has already been set up correctly.

1. If the Credentials supplied by the user running the report check box is selected, select the Use as Windows credentials when connecting to the data source checkbox.

1. Click Apply.

Related information

- [Set up SSRS reports after install](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/set-up-ssrs-reports-after-install)
