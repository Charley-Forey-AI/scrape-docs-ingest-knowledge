---
title: "Configure Automated Document Upload for Imports - VRL Cloud | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/configure-automated-document-upload-for-imports---vrl-cloud"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/configure-automated-document-upload-for-imports---vrl-cloud"
---

# Configure Automated Document Upload for
 Imports - VRL Cloud

In order for your Vista
 application to automatically import data files into the Vista database in the cloud, there
 are configuration steps that you must complete on your local LAN-connected server. This
 includes assigning the username and password the system should use during the import
 process, as well as specifying how often the application should check for new data files to
 import.
Note: Your company's Vista deployment method affects which actions you should take on this page. Your deployment method is shown at the bottom of the Main Menu in the status bar.
If your deployment/connection method is:

- VRL Cloud - and if you want fully-automated imports - you
 must take the configuration steps described in this topic. If you manually place
 files into the Pickup folder, you do not need to take these steps.

- LAN, VFC, or VRL on-premises - do not take the steps on this
 page. Instead, see [Server Setup for Automatic Imports: On-premises](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/server-setup-for-automatic-imports-on-premises).

In order for your application to automatically import data files into the database,
 there are configuration steps that you must complete on the server. This includes
 assigning the username and password the system should use during the import process, as
 well as specifying how often the application should check for new data files to import.
 Prerequisites to completing this task include:

- [Set up the Auto Import Profile](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/create-an-auto-import-profile---vrl-cloud#ID-00011e90--en__ID-00011e90).

- Ensure that your LAN-connected server has a [VPN connection](/en/vista/vista/cloud-deployment/about-vrl-cloud/about-vpn-use-for-vrl-cloud-users#concept_iyl_srk_snb--en__concept_iyl_srk_snb) to the cloud server.

- Ensure that a Windows file share is located on the Vista
 server in the cloud directed to the folder named in the
 Pickup field of the IM Auto Import Profile form. If
 you do not have this already, submit a Cloud Support Ticket to request it.

- If needed, submit a support ticket to request an Import username and password
 that enables Vista to process files that are automatically placed in the
 designated file location. If you have a 3rd-party application already placing
 files in the designated location and your automated imports are already working,
 this pre-requisite is already met.

To enable automatic imports
 into the Vista database in the cloud:

1. On a system that has VPN access (that is, the "source" system from where you
 intend to automatically upload files), create a mapped drive letter pointing to
 the Windows file share on the cloud Vista server; this is the file share
 described in the prerequisites above.You must use an account with the ability to connect to that file share.
 Viewpoint will have created that account for you and assigned it to the file
 share. Use this account to mount the file share on your “source” system.

1. Create a Powershell or DOS Batch file that can copy files from the output
 directory of your automated system to the mapped drive letter from step 1.

1. Using a fully privileged account (administrator), create a Scheduled Task that
 will run the script / batch file on a regular basis:

1. Using Windows 10 or Windows Server 2016, launch Task Scheduler.

1. Click Create Task.The Create Task window appears.

1. Give the Scheduled Task a name and description.

1. Change the User to the new service account you set up in step 2
 above.

1. Select the Run whether user is logged on or not option.

1. Select the Run with highest privileges checkbox.

1. In the Trigger tab, click New.The New Trigger window appears.

1. In the Begin the task field, select On a schedule.

1. Under the Settings section, select an option of Daily, Weekly, or
 Monthly and set the recurrence.

1. Under the Advanced Settings section, set the repetition, and expiration
 (if needed).

1. Select the Enabled checkbox and click OK to close the New Trigger
 window.

1. In the Actions tab, click New.The New Action window appears.

1. In the Program/script field, enter the name and location of the script
 (from step 2 above) which can copy the files from your drop directory of
 your automated system to the mapped drive. Click OK to close the New
 Action window.

1. (Optional) In the Conditions and Settings tabs, make selections as
 desired.

1. Click OK to save your changes and close the Create Task window.

Your Scheduled Task is now
 ready to test and use.

Related tasks

- [About Importing Files Automatically](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically)
