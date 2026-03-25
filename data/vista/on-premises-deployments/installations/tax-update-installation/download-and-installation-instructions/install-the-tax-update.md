---
title: "Install the Tax Update | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/tax-update-installation/download-and-installation-instructions/install-the-tax-update"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/tax-update-installation/download-and-installation-instructions/install-the-tax-update"
---

# Install the Tax Update

Follow the installation wizard prompts to install the tax update on your computer.
Before you install the tax update, make sure you have the required version of Vista. To verify your Vista version, select Help > About Vista from the Vista main menu. The version displays at the top of this form. Tax updates are cumulative within the year. This means that any tax update for a given year includes all routines released in previous tax updates for that same year. Before you install a given tax update, make sure you first install the last tax update for each prior year, if you have not already done so.

Note: Users do not have to log off while you are loading the tax update.

1. Locate the VistaTaxUpdate_20YY.#.# file that you downloaded from the Viewpoint Customer Portal and double-click the icon to launch the installer.Depending on your system, you may receive a message asking if you want to allow the program to make changes to your computer. If this message displays, select Yes to launch the installer.
The Vista Tax Update screen loads. The tax update will install to the Program Files directory on your computer: C:\Program Files\Viewpoint Construction Software\TaxUpdate\
As you install subsequent tax updates, additional folders are added to this main folder for each new version.
Important: If you attempt to install the tax update to a location other than the Application Server, the system displays a warning and you will be unable to complete the installation.

1. On the Database Connection Information screen, enter your Vista database server and database name in the Server and Database fields.

1. Select the SQL Authentication radio button.The system defaults to the sa login.

1. In the Password field, enter the password for the sa login.Note: If you do not know the password for the sa login, enter an sa equivalent login and password. If your Windows login is the sa equivalent login, select the Integrated Security radio button.

1. As noted on the screen, a successful connection test is required in order to continue installation. Select Test Connection.The Install button remains grayed out and inactive until there is a successful connection test.

If you attempt to test the connection with invalid credentials, you will get a Login Failed error message.

1. After the test connection succeeds, select Install.The screen changes to show the installation progress.

Note: If you select Cancel before the install finishes, you must confirm that you do want to cancel. If you confirm the cancellation or something goes wrong during the installation, you will see a new screen reflecting the failure to install and directions for what to do next.

1. After a successful installation, select Finish to close the wizard.

The installation process generates an installation log for each individually scripted object. The following generic log returns the latest run for that tax update version:
C:\Program Files\Viewpoint Construction Software\TaxUpdate\YY.#.##\Vista_TaxUpdate_ScriptLog.log
Individual logs have the following naming convention with the version and a specific timestamp:
Vista_TaxUpdate_ScriptLog_YY.#.##_YYYYMMDDHHMMSS.log

Once you have completed installing the tax update, you must activate the new routines. For more information, see [Activate the New Routines](/en/vista/vista/on-premises-deployments/installations/tax-update-installation/download-and-installation-instructions/activate-the-new-routines).
