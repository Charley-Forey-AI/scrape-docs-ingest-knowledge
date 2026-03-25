---
title: "Server Setup for Automatic Imports: On-premises | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/server-setup-for-automatic-imports-on-premises"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/server-setup-for-automatic-imports-on-premises"
---

# Server Setup for Automatic Imports: On-premises

To automatically import third-party files into Vista, you must first configure automatic imports on the Vista server. Configuring the server includes specifying how often imports occur, as well as the username and password the system should use during the import process.

Note: Your company's Vista deployment method affects which actions you should take on this page. Your deployment method is shown at the bottom of the Main Menu in the status bar.
If your deployment method is:

- LAN, VFC, or VRL on-premises, you must take the configuration steps described in this topic.

- VRL Cloud, do not take the steps on this page. Instead, see [Configure Automated Document Upload for
 Imports - VRL Cloud](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/configure-automated-document-upload-for-imports---vrl-cloud).

In order for your application to automatically import data files into the database, there are configuration steps that you must complete on the server. This includes assigning the username and password the system should use during the import process, as well as specifying how often the application should check for new data files to import. Prerequisites to completing this task include:

- You must have login access to the Vista server.

- You must have the username and password for a user profile whose User Type is User Application. This type of user account does not belong to an actual user but is an account created specifically for automated processes like imports. If you have database security turned on, this user account must belong to a [security group](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form) that has [database security assigned](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-data-security-access-form) to it. See [User Type](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-0004bd04--en) for more information.

To enable automatic imports at the server level:

1. On the Vista server, select Start > Programs > Viewpoint Construction Software > Configure Viewpoint Remote Service.The Viewpoint Server Configuration form displays.

1. In the Imports section's Frequency field, enter the number of minutes between each time the system should check for new data files.

1. In the Import Username and Import Password fields, enter the login name and password for a valid Vista user account that has a user type of User Application.

Your server is now enabled to process imports automatically.
For Vista to perform the automatic import, you must create an import profile there. See [Create an Auto Import Profile - on-premises](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/create-an-auto-import-profile---on-premises).

Related information

- [Add Users to Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/add-users-to-security-groups)

- [Datatype Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security)

- [Create an Auto Import Profile - on-premises](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/create-an-auto-import-profile---on-premises)

- [About Importing Files Automatically](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically)

- [Securing Datatypes](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes)

- [Set Import Notifications](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/set-import-notifications)
