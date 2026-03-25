---
title: "Verify Upgrade Success | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/service-pack-installation/verify-upgrade-success"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/service-pack-installation/verify-upgrade-success"
---

# Verify Upgrade Success

Once you have installed the server upgrades, there are a number of items that you should check to ensure that Vista is functioning correctly.

1. Review the update logs and report any errors to Viewpoint Support. The installer creates two logs - one log for the application server and another log for the database server.

1. To review the log for application changes, go to the Viewpoint Repository\Updates folder. The log name is formatted like this:Vista_ServicePack_ScriptLog_20.##_yyyymmddhhmmss.log

1. To review the log for database changes, go to the Viewpoint Repository folder. The log name is formatted like this:Vista by ViewpointService Pack.MSILog.yyyymmddhhmmss.log

1. Verify that you can log into the Vista application. For instructions connecting the local client to your server, see [Access Vista - VRL On-Premises](/en/vista/vista/on-premises-deployments/access-vista---vrl-on-premises) or [Access Vista - Local Area Network
 (LAN)](/en/vista/vista/on-premises-deployments/access-vista---local-area-network-lan).

1. From the Main Menu, select Help > About Vista and verify that the version number is accurate

1. Run a few standard reports.

1. Open a few standard forms.

1. Review the release notes and grant/modify security to any new/modified forms and reports in Vista.To review release notes:

1. From the left side menu, select What's New.

1. At the bottom of the What's New menu section, select Vista Service Packs.Note: The title of the Vista Service Packs section differs for each release. For example, for the 2023 R1 release, the title will show as Vista 2023 R1 Service Packs.

The Vista Service Packs section expands and displays all available service packs for the specified release.

1. Select the applicable service pack.The release notes for the selected service pack display to the right.

1. [Regenerate all database views](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/regenerating-views).

1. If problems occur, [submit a Vista support case](https://support.viewpoint.com/s/submit-a-case).
