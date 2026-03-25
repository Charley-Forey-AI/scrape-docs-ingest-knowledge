---
title: "Install the Vista Application on a Test Server | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/install-the-vista-application-on-a-test-server"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/install-the-vista-application-on-a-test-server"
---

# Install the Vista Application on a Test Server

You may choose to install Vista on a test server prior to installing on your production server to try out new enhancements or test any custom work (reports, triggers, procedures) against the new release. The following explains how to install Vista on a test server.
If this section doesn't apply to you, skip to [Modify Service Accounts](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/modify-service-accounts#_Ref-1814873501--en___Ref-1814873501).Note: Viewpoint does not support multiple Vista databases in a single SQL instance. Do not install a test database to your production instance—it will cause your production instance to fail.

1. Locate and run the VistaApplicationServer.YY.v.#.##.Rel.exe file on your Vista test server. For guidance, see [Upgrade the Application Server](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-application-server).

1. When you get to the step that displays the Production or Test Install screen, complete the following:

1. Select Next on the installation wizard.The Production Environment warning displays.

1. Review the warning and select Continue.The Ready to Install screen displays.

1. Select Install.

At this point, the system begins the installation and displays the Installing Vista Server Upgrade screen. The installation process may take several minutes to finish.

1. On the InstallShield Wizard Completed screen, click Finish.Note: In some cases, the wizard may install required applications. If this occurs, you should follow any prompts to reboot the server before continuing.

1. Verify that Vista is running correctly. For more information, see [Verify Upgrade Success](/en/vista/vista/on-premises-deployments/installations/major-release-installation/verify-upgrade-success).
