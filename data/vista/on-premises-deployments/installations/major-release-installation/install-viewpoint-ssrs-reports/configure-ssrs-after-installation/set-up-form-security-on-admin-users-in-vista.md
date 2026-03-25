---
title: "Set up Form Security on Admin Users in Vista | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/set-up-form-security-on-admin-users-in-vista"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/set-up-form-security-on-admin-users-in-vista"
---

# Set up Form Security on Admin Users in Vista

You can set up one or more selected Vista users as system administrators on the SSRS Report Server.
The system automatically sets up a Vista user as a system administrator on the SSRS Report Server when you give them access to any of the following forms:

- VA Report Security

- RP Report Titles

- RP Report Copy

The user needs access to only one of these forms to be a system administrator on the SSRS Report Server. For example, if they are denied access to VA Report Security but can access the RP Report Titles or RP Report Copy form, they will still be set up as a system administrator on the SSRS Report Server.
The system will also give the user access to the VCS folder on the SSRS Report Server. This means the following:

- The user will be able to change folder level security on any subfolder in the VCS folder.

- The user will be able to access any subfolder or report in the VCS folder that has not been set up with item level security. Item level security means that there is security set up on a specific folder or report, and that folder or report will no longer inherit security from the parent folder.

- If you have set up security on the SSRS reports using
 Vista, the user will only
 be able to access the reports in the VCS folder that they have been
 explicitly given access to. When you set up security on a report using
 Vista, the system sets item
 level security on the report. This means security set up at the folder level
 will no longer apply to the report and the user will only be able to access
 the reports that they have been given access to in Vista.
