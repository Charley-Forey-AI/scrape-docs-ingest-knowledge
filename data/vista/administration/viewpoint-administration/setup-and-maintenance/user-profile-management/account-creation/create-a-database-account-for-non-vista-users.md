---
title: "Create a Database Account for Non-Vista Users | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-database-account-for-non-vista-users"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-database-account-for-non-vista-users"
---

# Create a Database Account for Non-Vista Users

Integrations, service accounts, third-party applications,
 SQL logins, and database logins that do not require logging in to the Vista application must
 be set up with a User Type of User
 Application.
Database accounts with a User Type of
 User Application may
 continue to use SQL login credentials even when classic logins are disabled for
 cloud-hosted Vista users in fall of 2025. Note: For cloud-hosted
 customers, if your organization has consultants that require access to both the
 Vista application and the Vista database, they will need to have two separate
 accounts:

- To log in to the Vista application, consultants must have a Vista user SSO
 account and use Trimble ID credentials.

- To log in to the Vista database, consultants must have a Vista database
 account, which requires a classic SQL login.

For products such as Trimble Construction One
 Analytics, or for specific Vista Web workflows, linking Vista security to a Trimble
 ID user is necessary. In these situations, you should [Create a Trimble Construction One Analytics Account for Non-Vista Users](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-trimble-construction-one-analytics-account-for-non-vista-users).
To set up a database account
 for a non-Vista user, complete the following:

1. From the Vista main menu, go to Viewpoint
 Administration > Programs > VA User Profile.

1. At the top of the form,
 select the New Record
 icon () in the toolbar.Alternatively, locate an existing account and open the record.

1. In the [User Type](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-0004bd04--en)
 dropdown, select User Application.

1. Enter any other necessary information and save the
 record. If this account has not been set up in
 Microsoft SQL Server, a message displays that the system will attempt to create
 a SQL Server login.

1. Select Close.The VA Password form opens.

1. Enter and confirm the password in the appropriate
 fields and select OK.The system creates the required SQL
 server login (if the user does not already have one), so that the user can
 access information from the Vista
 database.

1. Save the record.

1. Share the SQL login credentials with the user.

Note: Any user profile records
 with a User Type of User
 Application will not be included in your organization's migration to
 Trimble ID and will not be impacted when classic logins are disabled.
For more information, watch this video about creating Vista accounts: [Trimble ID Account Creation for Vista - Video](/en/vista/vista/videos/administration/trimble-id-account-creation-for-vista---video).
