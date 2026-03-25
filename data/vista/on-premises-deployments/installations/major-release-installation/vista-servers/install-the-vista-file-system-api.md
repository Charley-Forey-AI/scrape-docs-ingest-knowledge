---
title: "Install the Vista File System API | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/install-the-vista-file-system-api"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/install-the-vista-file-system-api"
---

# Install the Vista File System API

When new versions of the File System API application are released, you must download and install the API on either your application server or a server that the application server can access.
Important: This section applies to you only if you are using VRL on-premises. Skip this section if it do not apply to you.

The following steps guide you through the Vista File System API install process as a part of the required steps to provide remote Vista access to your users.
You must install this executable with each major release.
Important: The network service account needs to have full read/write permissions for the folders.

To install the Vista File System API:

1. Locate and run the Vista.FileSystemApi.#.#.#.###.exe file on your Vista application server. This file is located in the directory it was saved to when it was downloaded from the Viewpoint Customer Portal. It may take a few minutes for the system to prepare the InstallShield Wizard.

1. When the File System API InstallShield Wizard appears, click Next.The License Agreement screen displays.

1. Read the End User License Agreement and select the I accept... radio button.

1. Click Next.The Destination Folder screen displays.

1. Verify that the default location is correct and click Next.Note: Changing the default location is not typical. However, if you need to change the location where the API is installed, click Change. The system displays the Change Current Destination Folder screen, where you can browse to and select a different location. If you change the location, you must ensure the Internet Information Service (IIS) has access permissions to the new location.

1. When the Database Server screen appears, do the following:

1.  In the Database server that you are installing to field, enter the machine name of your Vista database server or click Browse to locate the server. Make sure this is the machine name and not the Fully Qualified Domain Name.

1. In the Connect using section, select the appropriate option:

-  If you do not know the password for the sa login ID, and if your Windows login has sufficient permission, select the Windows authentication... radio button.

- If you select the Server authentication... radio button, the system defaults to the sa login ID. Enter the password for the sa login.

1. The Name of the database catalog field defaults to Viewpoint. Accept the default database or click Browse to search for the database name.

1. Click Next.

1. If you opted to change service accounts, an informational screen appears. Click Next.

1. In the Ready to Install the Program screen, click Install. The system begins the installation. The process may take several minutes to finish.

1. In the InstallShield Wizard Completed screen, click Finish.Note: In some cases, the wizard installs required applications. If this has occurred, you may receive and should follow any prompts to reboot the server before continuing.

We recommend you review and/or take notes of the default settings in the Viewpoint Remote Services Configuration form, especially if this is the first time you are installing the File System API on this server. For more information, see [Review the Vista File System API Configuration](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-servers/review-the-vista-file-system-api-configuration).
