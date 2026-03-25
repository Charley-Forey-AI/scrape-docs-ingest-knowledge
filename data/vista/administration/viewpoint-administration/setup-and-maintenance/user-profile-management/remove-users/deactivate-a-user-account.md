---
title: "Deactivate a User Account | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/remove-users/deactivate-a-user-account"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/remove-users/deactivate-a-user-account"
---

# Deactivate a User Account

You can deactivate a user account so that the user no longer has access to Vista.
Deactivating a user account prevents the user from logging into Vista, but it does not remove the user from the system. The system preserves the deactivated user's

- account settings in the VA User Profile form

- activity history throughout the system

- deactivation dateNote: Deactivation dates are reported in the VA Systems User report, using the Detail option.

Users who happen to be logged in at the time their account is deactivated are not automatically logged out. However, once they've logged out, they are prevented from logging back in with the same account.
Note:Deactivation is a two-part process:

1. Deny user access to the MS SQL Server database. The software you use to manage your SQL server may require you to deviate from the instructions in this part.

1. Deactivate the user record in Vista.

Re-activating the user account requires the reversal - clearing the Deactivated checkbox and saving the user record, then restoring access to the MS SQL Server database.

1. Using an administrator login, open a connection to your Microsoft SQL Server.

1. Locate your server and select the appropriate Database directory.

1. In the database from which you are removing the user's access, expand the Logins folder.

1. In the Logins folder, locate and right-click the user account you want to deactivate.

1. In the context menu, select Properties.The Login Properties dialog box opens.

1. In the Login Properties dialog box, select the General tab.

1. In the Password and Confirm Password fields, change the password.

1. In the Login Properties dialog box, select the Status tab.

1. In the Permissions field, select Deny.

1. In the Login field, select Disabled.This completes the first part - denying user access to the database.

1. In Vista, open the VA User Profile form.

1. In the Info tab, select the user record and select the Deactivated checkbox.

1. Select Save.

The user is prevented from logging into Vista.Note: The user history is still present.

If the deactivated user accessed Vista in the cloud, you must also delete the user record in the cloud portal to avoid potential unnecessary license costs. See [Delete Users from the Cascade Portal](/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/cascade-cloud-administrator-portal-help/cascade-cloud-administrator-portal---vista/user-management/add-and-delete-users/delete-users-from-the-cascade-portal).

Related information

- [About the VA User Delete Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/about-the-va-user-delete-form)
