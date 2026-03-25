---
title: "Install the Upgrade | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/service-pack-installation/vista-servers/install-the-upgrade"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/service-pack-installation/vista-servers/install-the-upgrade"
---

# Install the Upgrade

This section describes the service pack installation process.

1. From the Viewpoint Application server, browse to the location of the Vista_ServicePack_##.#.#.###.exe file and double-click the icon to run the upgrade. The InstallShield Wizard launches and displays the Welcome screen.

1. Select Next.The Destination Folder screen displays.

1. The system automatically defaults to your Viewpoint Repository and Viewpoint Remote Service directories. If either path is incorrect or you want to install to different folders, do the following:

1. Select Change (for either option).

1. Locate the correct directory and select OK.

1. Select Next to accept both locations.

Note: If you attempt to install to a location that does not have a valid Viewpoint Repository or Viewpoint Remote Service directory, an "Invalid Location" warning displays. Select Back to change the destination location (strongly recommended) or Ignore to continue with the installation (not recommended).

The Database Server Login screen displays.

1. In the Database server... field, enter the name of your database server or select Browse to locate the server.

1. Select the Server authentication... radio button. The system defaults to the sa login.

1. Enter the password for the sa login. Note: If you do not know the password for the sa login, enter an sa-equivalent login and password. If your windows login is the sa-equivalent login, please select the Windows authentication... radio button.

1. The Name of the database catalog field defaults to Viewpoint. Accept the default or select Browse to search for the database name.

1. Select Next.The Ready to Install the Program screen displays.

1. Select Install. It may take a few minutes for the system to install the update.
Once the update is installed, the InstallShield Wizard Completed screen displays.

1. Select Finish to close the wizard.

1. If applicable, restart Citrix/Terminal Services before allowing users to log on.
