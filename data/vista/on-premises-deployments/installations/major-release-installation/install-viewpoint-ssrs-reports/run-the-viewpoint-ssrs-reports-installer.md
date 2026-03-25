---
title: "Run the Viewpoint SSRS Reports Installer | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/run-the-viewpoint-ssrs-reports-installer"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/run-the-viewpoint-ssrs-reports-installer"
---

# Run the Viewpoint SSRS Reports Installer

If you use SSRS Reports, you can run the SSRS Reports installer to load the library of standard Vista SSRS reports onto your SSRS Report Server.
Before you proceed with the instructions below, you should first:

- Upgrade your Vista server to the selected release.

- Verify that you do not have any custom reports in the "VCS\Standards" folder on the SSRS Reports Server. During the installation, all of the reports in this folder will be deleted before the new reports are installed.

Important: You are not required to run the SSRS installer, but doing so will do no harm. If and when an SSRS reinstall is required, the installation guide will include that information as applicable.
Follow these steps to run the Viewpoint SSRS Reports installer on your SSRS Report Server.

1. Verify that the SSRS Report Server is installed, configured, and running. A quick test is to open the SSRS Report Manager (usually located at http://<server name>/Reports).

1. Locate the VistaSSRSReports.42.0.0.exe file. This file is where you saved it to when you downloaded it from Viewpoint Customer Portal.

1. Run the VistaSSRSReports.42.0.0.exe file file on your Vista SSRS Report Server.Note: If you are installing Vista SSRS Reports to a server other than your Vista database server, you must update the SSRS Host name in the Server Config form after installation.

1. In the Viewpoint SSRS Reports InstallShield Wizard, click Next.The Destination Folder screen displays.

1. Verify that the displayed directory is the correct location to temporarily store the SSRS files as they are being installed. Click Next to accept the location.Note: Changing the default location is not typical. However, if you need to change the location where the upgrade is installed, click Change. In the Change Current Destination Folder screen, browse to and select a different location.

1. In the Custom Setup screen, click Next.The Database Server screen displays.

1. In the Database server that you are installing to field, enter the name of the server where the Viewpoint database is located or click Browse to locate the server.

1. The Connect using section defaults with the Server authentication using... option selected and a Login ID of sa. Accept the defaults.

1. In the Password field, enter the password for the sa login.

1. The Name of the database catalog field should default to Viewpoint. Accept the default or you can click Browse to search for the database name, if necessary.

1.  Click Next.The SSRS Setup Information screen displays.

1. Accept the default values for all fields or change the values as needed.Note: The SSRS Instance Name field is used to select the instance of the SSRS Report Server where the Viewpoint SSRS Reports installer should be run. If you are running the Viewpoint SSRS Reports installer on multiple SSRS Report Servers, use this field to select the correct instance. Each SSRS Report Server instance needs a unique description.

1. Click Next.The next SSRS Setup Information verification screen displays.

1. Verify that the paths to the SSRS Report Manager and Report Server are correct and then click Next. These paths are based on the SSRS instance selected in the prior step.

1. In the Ready to Install the Program screen, click Install.The system begins the installation and displays the Installing Viewpoint SSRS Reports screen. The installation process may take several minutes to finish.

1. In the InstallShield Wizard Completed screen, click Finish.

This completes the SSRS Reports installation.
Once you've run the Viewpoint SSRS Reports installer, you should configure SSRS. For more information, see [Configure SSRS After Installation](/en/vista/vista/on-premises-deployments/installations/major-release-installation/install-viewpoint-ssrs-reports/configure-ssrs-after-installation).
