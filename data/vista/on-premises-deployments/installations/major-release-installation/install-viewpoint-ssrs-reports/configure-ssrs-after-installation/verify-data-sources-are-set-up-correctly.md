---
title: "Verify Data Sources are Set Up Correctly | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/verify-data-sources-are-set-up-correctly"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/verify-data-sources-are-set-up-correctly"
---

# Verify Data Sources are Set Up Correctly

If the data sources on reports are set up to use the credentials that are supplied by the user running the report, the reports have to be set up in a specific way to display in Vista.
 This applies to shared data sources that you have created yourself, as well as any custom reports with a custom data source. This does not apply to reports in the Standard folder or the standard Viewpoint shared data source; both of these are set up by the Viewpoint SSRS Reports installer.
To verify that the data sources are set up correctly:

1. Open the SSRS Report Manager (usually http://<server_name>/Reports).

1. Check the setup on each shared data source that you have created yourself. If you have not created your own shared data source, you can skip this step.Note: This step does not apply to the Viewpoint shared data source since it was configured during the installation.

1. Locate a data source that you have created yourself.

1. Move the cursor over the data source, click on the drop down that appears, and select Manage.

1. If the Credentials supplied by the user running the report checkbox is selected, make sure that the Use as Windows credentials when connecting to the data source checkbox is also selected.If the Credentials stored securely in the report server checkbox is selected and valid user and password is also entered, you do not have to change anything.

1. Click Apply.

1. Repeat the steps above on the remaining data sources that you have created yourself.

1. Check that each custom report that will be viewed in Vista has a data source that is set up correctly.

1. Locate a report in the Custom folder.

1. Move the cursor over the custom report, click the drop down that appears, and then select Manage.

1. Open the Data Sources tab.

1. If the A shared data source checkbox is selected, verify that the referenced data source has already been set up correctly. This applies only to data sources that are not the standard Viewpoint data source.

1. If the Credentials supplied by the user running the report checkbox is selected, make sure that the Use as Windows credentials when connecting to the data source checkbox is also selected.

1. Click Apply.
