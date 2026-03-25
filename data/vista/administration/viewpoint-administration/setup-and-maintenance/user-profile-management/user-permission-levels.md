---
title: "User Permission Levels | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/user-permission-levels"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/user-permission-levels"
---

# User Permission Levels

Users within the Vista™ application can be granted various levels of access to the application.
Level
Created by
Permissions
For more information

Database Owner
 Clicking the Grant DBO button for that user in VA User Profile.
 Only users with elevated SQL permissions can grant database owner permissions.
 Total access to the Viewpoint database. Grants the selected user SQL database owner (DBO) privileges, including:

- granting and revoking access

- creating tables

- creating stored procedures and views

- running backups

- scheduling jobs

- dropping the database

See [Granting DBO Privileges](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/grant-full-application-access-and-dbo-security-permissions)

Full Access User
Clicking the Grant Full Access button for that user in VA User Profile.
 Has permissions for full access in all companies:

- form security for all forms; add, update, and delete permissions; and full attachment security levels

- report security for all reports

- attachment type security for all attachment types

- work center security for all work center templates

- inquiry security for all queries.

- payroll group security for all companies and all payroll groups

- default datatype security groups for secured datatypes

See [Granting Full Access to the Application](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/grant-full-application-access-and-dbo-security-permissions)

Master Security Administrator
Selecting the Enable Security Administration checkbox in VA Site Settings to turn Security Administration on. The first user to select the checkbox becomes the first Master Security Administrator. Subsequent Master Security Administrators are created in VA Security Administration. Users should be given access to VA Form Security before being created as a Master Security Administrators.
If Security Administration is turned on, then a Master Security Administrator can use the VA Security Administration form.
A Master Security Administrator can restrict a user with security form access to granting security permissions in only specific company/module combination in VA Form Security and VA Report Security.
[Creating a Master Security Administrator](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/create-a-master-security-administrator)

Users with security form access
Granting to that user access to administer security in VA Form Security, VA Report Security, VA Attachment Type Security, VA Inquiry Security, and/or VA Work Center Security.
Can assign to users form security. Can use own form security to gain access to report, attachment type, inquiry, and work center template security forms, and thereby grant those permissions.
[Setting Form Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

If Security Administration is turned on, a Master Security Administrator can restrict a user with security form access to granting security permissions for only specific company/module combinations in VA Form Security and VA Report Security.
If Security Administration is turned on and a Master Security Administrator has restricted the user's security form access, the user may be able to grant security permissions in only specific company/module combination in VA Form Security and VA Report Security.
[Restricting Security Form Access to Specific Company/Module Combinations](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/restrict-security-form-access-to-specific-company--module-combinations)

Menu Administrator
Selecting the Menu Administrator checkbox in VA User Profile for that user.
The user can add, edit, or delete Main Menu subfolders.
[Setting Up Users](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-vista-sql-user-in-va-user-profile)

Form Administrator
Selecting the Form Administrator checkbox in VA User Profile for that user.
The user can use the System Overrides tabs on the Form Properties form and Field Properties form to change the settings on a form.
[Setting Up Users](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-vista-sql-user-in-va-user-profile)

Vista User
Creating the user in VA User Profile, and then granting security permissions to the user, or to groups to which the user belongs, in VA Form Security, VA Report Security, VA Attachment Type Security, VA Inquiry Security, and VA Work Center Security.
Has whatever form, report, attachment type, inquiry, and work center template security permissions that has been granted to the user. Can be granted security permissions as part of a user group or individually.
[Setting Up Users](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-vista-sql-user-in-va-user-profile)

Related information

- [Assign User Security](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/assign-user-security)

- [Datatype Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security)

- [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)

- [VA Attachment Type Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form)

- [About the VA Inquiry Security Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form)

- [About the VA Work Center Security Form](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-security-form)

- [VA Security Groups Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form)

- [VA Security Administration Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-administration-form)
