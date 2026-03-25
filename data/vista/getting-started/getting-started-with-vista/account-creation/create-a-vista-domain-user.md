---
title: "Create a Vista Domain User | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-vista-domain-user"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-vista-domain-user"
---

# Create a Vista Domain User

Legacy cloud or on-premises customers can set up Vista users
 as domain users, requiring Windows login credentials to access the Vista application.
To create domain users, each user must have access to
 the Vista database at the SQL level. Administrators can provide this access in two ways:


- Set users up individually in SQL Server with a domain user
 (DOMAINNAME\Windows Account).

- Set users up in a Windows Domain Group and then set up the
 Domain Group in SQL Server.

Important: If you are a
 Trimble Construction One cloud-hosted Vista customer, this option to create new
 users with classic credentials (SQL or Windows logins) will no longer be
 supported in the fall of 2025. At that point, you should [Create a Vista User SSO Account with Trimble ID](/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-vista-user-sso-account-with-trimble-id) when setting up new Vista users. Legacy cloud and
 on-premises customers will still be able to set up new users with classic
 credentials.

The following steps create a domain
 login name for the user using the VA User Profile form. If you are setting up access
 for the user on the database at the SQL level individually, you can do that either
 before or after performing these steps.
To set up a domain user in the VA User Profile form:

1. From the Vista main menu, go to Viewpoint Administration > Programs > VA User Profile.For more information about this form, see [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form).

1. At the top of the form,
 select the New Record
 icon () in the toolbar.

1. On the Info tab, in the
 User
 Name field, enter the user name for the domain user (e.g.
 DOMAINNAME\username). You can also press F4, select the System
 Users option, and select the user from the list.For more information, see [User Name](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049ae1--en).

1. In the User Type dropdown, select
 Vista. This ensures the user can log in to the Vista
 application.

1. Enter any additional
 information for the user, making sure to customize the security setup as
 applicable. See [Create a Vista SQL User
 in VA User Profile](/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-vista-sql-user-in-va-user-profile) for more
 information.

1. Save the user account.When the user logs in using the domain user option, the system uses their Windows password.

Related information

- [User Name](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049ae1--en)

- [User Type](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-0004bd04--en)

- [Create a Vista SQL User in VA User Profile](/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-vista-sql-user-in-va-user-profile)

- [Log in to Vista Using Classic Credentials](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/log-in-to-vista/log-in-to-vista-using-classic-credentials)
