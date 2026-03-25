---
title: "Delete Users from SQL Server | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/remove-users/delete-users-from-sql-server"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/remove-users/delete-users-from-sql-server"
---

# Delete Users from SQL Server

Delete users from the SQL server.
After you have deleted a user account from Vista™ using [VA User Delete](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/about-the-va-user-delete-form) or [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/remove-users/delete-a-user-account-with-va-user-profile), you may also want to delete the user from SQL Server. Deleting a user from Vista using either of these forms does not automatically delete the user from SQL Server.
To delete a user from SQL Server:

1. In Microsoft SQL Management Studio, locate your server and select the Database directory.

1. Select the database from which you are deleting the user, and select Security > Users.

1. Right-click the user to delete and select Delete.
