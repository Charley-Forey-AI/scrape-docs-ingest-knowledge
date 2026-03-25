---
title: "Install the Vista Client on a Workstation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-client-application/install-the-vista-client-on-a-workstation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-client-application/install-the-vista-client-on-a-workstation"
---

# Install the Vista Client on a Workstation

Viewpoint provides an .msi file for installing the Vista client on each workstation.
 You may use this file to push the client upgrade via group policy or via other third-party
 applications.
Important:Client prerequisites:

- Your account must have local admin rights to use the client installer
 .msi. Limited user accounts do not work.

- You must have already installed all required components for the
 installation to complete correctly and for Vista to operate properly.
 (The installation file contains only the Vista client software.) For
 more information, see [Components Required by the Vista Client Application](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-client-application/components-required-by-the-vista-client-application).

The Vista client installer detects missing required components. An example prompt is shown
 here:
If you receive such a prompt to
 install an application or missing component, do the following before installing the
 Vista client:

1. Download and install the application or component.

1. Reboot the workstation.

1. Run the client installer again, from the beginning.

To install the Vista client on a workstation:

1. Locate the VistaClient.YY.V.#.###.Rel.msi file. This
 file is located in the folder where you saved it when you downloaded it from the
 Viewpoint Customer Portal.

1. Right-click the .msi file and select Run As
 Administrator.It may take a few minutes for the system to prepare the InstallShield
 Wizard.

1. In the Viewpoint Client InstallShield Wizard, select
 Next.The next several screens collect your preferences for use during the
 installation.

1. Change the default version setting from 32-bit to 64-bit, and select
 Next.Note: Install the 32-bit version only if you need to maintain compatibility
 with a 32-bit version of Office.

1. Read and accept the end user license agreement and select
 Next.

1. In the Custom Setup screen, the default setting pertains to the bit version you selected in step 4. Accept the default setting and select
 Next.

1. In the Destination Folder screen, select Next to accept
 the default location.Note: If you are re-installing the client, you typically do not want to change the
 destination folder from the default location. However, you may opt to do so
 by selecting Change and choosing a different
 location.

1. In the Vista Add-In Install Mode screen, choose how broadly the MS Outlook
 add-in should be installed and select Next.

1. On the Ready to Install the Program screen, select
 Install to begin installation using your
 selections.It may take a few minutes for the system to complete the installation. During
 this time, the Installing Viewpoint Client screen displays.

1. When installation is complete, the InstallShield Wizard Completed screen
 displays. If you want to review the install log, select the Show the
 Windows Installer Log checkbox.

1. Select Finish to close the wizard.
