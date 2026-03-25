---
title: "Set Up Report Security in Vista | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/set-up-report-security-in-vista"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation/set-up-report-security-in-vista"
---

# Set Up Report Security in Vista

Security settings in the Vista application are automatically pushed to the SSRS Report Server.
For example, if you give a user access to an SSRS report using the VA Report Security form, the system automatically applies that security on the SSRS Report Server. This means you should use Vista to manage SSRS report security.
If you have multiple SSRS Report Servers, security is pushed to all of the SSRS Report Servers that display in the RP RS Servers form in Vista. All of the servers that display in that form must point to the same Vista database.

## Why do I have to set up security again?

Vista will break folder level security on a report on the SSRS Report Server when it pushes security to that report.
When you set security on a SSRS report using Vista, the system sets up security using item level security. This means that the SSRS report will no longer inherit security from the parent folder. If a user has been granted access to an SSRS report at the folder level only, that user will no longer be able to access the report once Vista changes security on that report to item level.
If you used SSRS reports before upgrading, you should set up security on the SSRS reports using Vista.
Folder level security will work immediately after you run the Viewpoint SSRS Reports installer because the installer does not apply any security, but folder level security will break on a report once Vista applies any security to that report.
