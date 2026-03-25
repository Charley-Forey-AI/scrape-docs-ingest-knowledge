---
title: "Set up SSRS reports after install | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/set-up-ssrs-reports-after-install"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/set-up-ssrs-reports-after-install"
---

# Set up SSRS reports after install

After you have run the SSRS Reports installer, you will need to give users access to the SSRS reports.
Follow the steps below once you have run the Viewpoint SSRS Reports installer.

1. To give system administrator access on the SSRS Report server, give the applicable user access to one or more of the following forms: VA Report Security, RP Report Titles, or RP Report Copy.In addition, this give the user access to the VCS folder on the SSRS Report Server. This means:

- The user will be able to change folder level security on any subfolder in the VCS folder.

- The user will be able to access any subfolder or report in the VCS folder that has not been set up with item level security. Item level security means that there is security set up on a specific folder or report, and that folder or report will no longer inherit security from the parent folder.

- If you have set up security on the SSRS reports using Vista, the user will only be able to access the reports in the VCS folder that they have been explicitly given access to. When you set up security on a report using Vista, the system sets item level security on the report. This means security set up at the folder level will no longer apply to the report and the user will only be able to access the reports that they have been given access to in Vista.

1. Give users access to SSRS reports using the VA Report Security form. If you have multiple SSRS Report Servers, security will apply to all of the servers that display in the RP RS Servers form.When you set security on a SSRS report using Vista, the system sets up security using item level security. This means that the SSRS report will no longer inherit security from the parent folder. If access only been granted to an SSRS report at the folder level, the user will no longer be able to access the report once Vista changes security on that report to the item level.

1. If you have users that only access SSRS reports using the SSRS Report Manager, verify that they can still log in and access the reports. If users cannot access the reports, use the SSRS Report Manager to grant those users item level security.

1. Verify that custom report locations are correct by opening the Grid tab in the RP Report Titles form, sorting the reports by application type, and verify that the Location and Path fields are correct on all custom SSRS reports. This step only applies to SSRS reports that are not part of the standard BI module library.

1. If the data sources on reports are set up to use the credentials that are supplied by the user running the report, you must set the reports up correctly to display in Vista. This applies to shared data sources that you have created yourself, and any custom reports with a custom data source. This does not apply to reports in the Standard folder or the standard Viewpoint shared data source; both of these are set up by the Viewpoint SSRS Reports installer

1. Set up any remaining custom reports. If there are reports on the SSRS Report Server that are not set up in the RP Report Titles form, you have to manually create those report titles to open them from Vista. This means that you have to manually create the report locations associated with those reports uring the RP Report Locations form. Note: If you are not using custom security and want the security you set up in Vista to sync with the SSRS Report Server, you must:

- Set up the account running the Viewpoint Remote Service as an administrative account on the SSRS Report Manager Site Settings and;

- This account must be assigned a Content Manager role for each individual report in the SSRS Report Manager.

- If the Viewpoint Remote Service is running as a "NT Authority\Network Service", and the SSRS Report Server does not reside on the same machine, the account name should be in this format: <Domain>\<MachineName>$

Related information

- [SSRS Overview and Security Considerations](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations)

- [Set Up Data Sources for SSRS Reports](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/set-up-ssrs-reports-after-install/set-up-data-sources-for-ssrs-reports)
