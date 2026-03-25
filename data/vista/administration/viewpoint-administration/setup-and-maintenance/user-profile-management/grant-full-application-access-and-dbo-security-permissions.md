---
title: "Grant Full Application Access and DBO Security Permissions | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/grant-full-application-access-and-dbo-security-permissions"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/grant-full-application-access-and-dbo-security-permissions"
---

# Grant Full Application Access and DBO Security Permissions

​Vista enables certain users to have full access to the Vista application and/or
 database. These users are security administrators.
There are several levels of security
 administrator permissions. For more details on specific permissions, see [User Permission Levels](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/user-permission-levels).
Grant Full
 Access to the Application
Granting full access is typically done
 only when you want to give total access to your system to a particular user, such as
 the vcssupport account or system administrators. If the user has already had
 specific security settings set up, then granting full access will add security only
 for items not previously set up.
Important: Report security will
 be applied for SSRS reports only if the Sync Security checkbox is
 selected in the [RP RS Server Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/rp-rs-server-form).
For a description of the permissions granted to a Full Access
 user, see [User Permission Levels](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/user-permission-levels).

Set up a Full Access User

1. Set up the user as a
 Vista
 user. See [Create a Vista SQL User
 in VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-vista-sql-user-in-va-user-profile).

1. On the Grant tab of
 [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form), select Grant Full
 Access.

1. Make any additional needed changes in the form, and save the form.

Grant DBO Privileges
Granting database ownership privileges is typically done only when you want to provide total access to your Viewpoint database to particular users, such as the vcssupport account or system administrators.
You can grant these privileges using VA User Profile only if you have SQL permissions to grant database owner privileges.
Following the steps below grants the selected user SQL database owner (DBO) privileges. Some of these privileges include:

- granting and revoking access

- creating tables

- creating stored procedures and views

- running backups

- scheduling jobs

- dropping the database

To grant DBO privileges:

1. Set up the user as a Vista user. See [Setting Up Users.](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-vista-sql-user-in-va-user-profile)

1. On the Grant tab of [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form), click the Grant DBO button.

1. Make any additional needed changes in the form, and save the form.

To remove DBO privileges, you must use
 Microsoft SQL Management Studio (or some other third-party management tool).

Related information

- [VA Security Groups Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)

- [VA Attachment Type Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form)

- [About the VA Inquiry Security Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form)

- [About the VA Work Center Security Form](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-security-form)

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)

- [VA Data Security Access Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-data-security-access-form)
