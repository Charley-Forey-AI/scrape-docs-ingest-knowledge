---
title: "Upgrade the Database Server | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-database-server"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-database-server"
---

#  Upgrade the Database Server

This section will guide you through the database server upgrade process.

- Upgrading the database server takes approximately one (1) hour to complete. Make sure that all users are logged out prior to upgrading.

- To prevent logins during the install process, select the Do not allow logins checkbox in the Configure Viewpoint Remote Service application prior to starting the install.

- To complete the upgrade, you must know the sa password or be using a login with Windows authentication.

1. Locate and run this version's executable file on your Vista database server. This file is located where you saved it to when you downloaded it from Viewpoint Customer Portal. It may take a few minutes for the system to prepare for installation.

1. When the Vista Database Server InstallShield Wizard appears, click Next.The License Agreement screen displays.

1. Read the End User License Agreement and select the I accept... radio button.

1. Click Next.The Destination Folder screen displays.

1. Verify that the default repository location is correct and click Next to accept the location.The Database Server screen displays.

1. In the Database server... field, enter the name of your Vista database server or click Browse to locate the server.

1. In the Connect using section, select the appropriate option:

- If you know the sa password, select Server authentication using... and enter the sa password.

- If you do not know the sa password, select Windows authentication....

1. The Name of the database catalog field defaults to Viewpoint. Accept the default or click Browse to search for the database name.

1. Click Next.The Ready to Install the Program screen displays.

1. Click Install.The system begins the installation and displays the Installing Vista by Viewpoint Server Upgrade screen. The installation process may take several minutes to finish.

1. In the VCS DBUpgrader window, the Server field defaults the name of the server that you are using to run the installation wizard. Confirm that this is the correct default.Note: In some cases, you may need to enter a different server name (for example, when specifying a database server/instance name).

1.  Click Connect. The wizard verifies the connection to your SQL Server.

1. In the Upgrade Type field, select Viewpoint. This is the type of database that is being upgraded.

1. Do not change the setting in the Source Database field.

1. In the Destination Database field, select the database to update.

1. We recommend that you leave the Yes, I would like to help Viewpoint... checkbox selected. Once installation is complete, Vista sends information electronically to Viewpoint. This information is used to help Viewpoint focus on the functionality that is most important to you.Note: No sensitive data is sent to Viewpoint. The collected information includes:

- current Vista version

- current SQL version

- the number of times each form and report were accessed within the last 3 months

- the record size (number of rows) for all tables in the Vista database

You can opt out of sending information by clearing the Yes, I would like to help Viewpoint... checkbox.

1. Click Update to start running the database scripts. The Progress field displays information while the update is running. The update process takes approximately one (1) hour.

1. If you have a separate attachments database on the database server, you must run the DBUpgrader again. Repeat these steps starting with the [Upgrade Type](#d0e11--en__Update_Type) field; select Attachments and enter the attachments database in the Destination Database field.

1. Once the update process is finished, a confirmation message displays. Close the message and then close the VCS DBUpgrader window by selecting the X in the right hand corner.

1. In the InstallShield Wizard Completed screen, click Finish.Note: In some cases, the wizard may have installed required applications. If this has occurred, the system may prompt you to reboot the server before continuing.

1. If you have an attachments database on another server, you must rerun this installer on that database to upgrade it to the selected release.

1. Install the Application Server upgrade on your application server. For more information, see [Upgrade the Application Server](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/upgrade-the-application-server).
