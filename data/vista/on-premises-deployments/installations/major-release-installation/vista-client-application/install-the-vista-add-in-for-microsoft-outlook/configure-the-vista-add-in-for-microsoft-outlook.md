---
title: "Configure the Vista Add-In for Microsoft Outlook | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-client-application/install-the-vista-add-in-for-microsoft-outlook/configure-the-vista-add-in-for-microsoft-outlook"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-client-application/install-the-vista-add-in-for-microsoft-outlook/configure-the-vista-add-in-for-microsoft-outlook"
---

# Configure the Vista Add-In for Microsoft
 Outlook

Set up the Vista
 Add-in for Outlook. The add-in enables you to use Outlook to index emails to Vista records.

- The Vista Add-in for Outlook
 must already be installed on your workstation. It can be installed only during
 the installation of the Vista client.

- If you opted out of installing the add-in when you first installed Vista on your workstation, uninstall and reinstall Vista, this time including the add-in. For instructions, see
 [Install the Vista Add-in for Microsoft Outlook](/en/vista/vista/on-premises-deployments/installations/major-release-installation/vista-client-application/install-the-vista-add-in-for-microsoft-outlook). If you need assistance reinstalling the Vista client, contact your system
 administrator.

- If at any point the system prompts it, restart your computer. This may require repeating certain steps.

After installing the
 Vista add-in, you must configure
 Outlook to integrate with Vista.Through this
 integration, Vista does the following:

- Creates and applies indexes to emails and attachments
 received in Outlook

- Adds indexed items to data records

- Uses your search terms to scan the text contained in
 these items

Note: The Viewpoint menu does
 not display on new emails that you create in Outlook. This functionality is
 available only from email messages that you receive in your Inbox.
To
 configure email integration:

1. Log on to the workstation with the credentials of
 the user of the Vista Add-in.

1. Log in to Vista.

1. Close Outlook if it is open, and then restart
 it.

1. Open the Outlook Options window by going to
 File > Options > Add-Ins and selecting Add-In Options.The Add-in Options window
 displays.

1. Select the Vista Login Information tab and enter your Vista user credentials:

- If you select Use Windows Login, your
 username appears in the User
 Name field. Enter your Windows password.

- If you select Use Trimble ID, the Trimble login page opens.
 Enter your Trimble ID
 credentials and wait for the page to close. You do not need to enter
 anything in the User Name or Password fields on the Add-in Options form.

- If you select neither option above,
 enter your system (SQL) credentials in the User Name and Password
 fields.

1. In the Server Information section, select the Internet Connection checkbox and enter your server information.If needed, contact your system administrator for the correct entries for the Application Server and Access Server URL fields.

1. Select Apply and OK.The Add-in Options window closes.

Vista will now create indexes on emails and attachments, and
 add these items to the pertinent Vista
 records. For more information, see [Email Integration with Microsoft Outlook](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/email-integration-with-microsoft-outlook).
To take advantage of
 any new functionality, you must restart each workstation using the Vista Add-in after each new version of Vista is installed on the server.

Related information

- [About the Vista Add-in for Microsoft Outlook](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/email-integration-with-microsoft-outlook/about-the-vista-add-in-for-microsoft-outlook)

- [Index and Send Emails from Outlook to Vista](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/email-integration-with-microsoft-outlook/index-and-send-emails-from-outlook-to-vista)

- [Email Integration with Microsoft Outlook](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/email-integration-with-microsoft-outlook)
