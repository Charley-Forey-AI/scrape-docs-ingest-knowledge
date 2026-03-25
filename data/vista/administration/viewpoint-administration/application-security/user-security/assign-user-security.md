---
title: "Assign User Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/user-security/assign-user-security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/user-security/assign-user-security"
---

# Assign User Security

The VA module allows administrators to set up different types
 of security for areas including data, forms, reports, attachment types, inquiries, and work
 centers.
 You must assign security permissions for all users
 before giving them access to the system. It is recommended that you assign security to
 groups of users, then customize security settings for individual users if their group
 settings are too restrictive.Important: Consider which
 individuals have access to the security forms. If you restrict access to specific
 forms, but do not also restrict access to the security forms, then any user can
 change the security setup for themselves.
Set up users with different types of security depending on their
 role and access needs:

- Data: Use this
 security to prevent unauthorized users from viewing or posting
 information to system fields, or from accessing sensitive information
 through other sources.

- Form: Use this
 security to prevent users from accessing forms or specific form
 tabs.

- Report: Use this
 security to define which reports are available to users.

- Attachment Type: Use
 this security to define what types of attachments users can access.

- Inquiry: Use this
 security to define what queries users can access on the dashboard Work
 Center on the main menu.

- Work Center: Use this
 security to define the Work Center templates that users can access.

- Security
 Administration: Use this security to restrict users who
 have security form access to administering only some company / module
 combinations in VA Form Security and VA Report Security. This feature is
 optional and should be used *only* if
 you want some users to administer security for selected company / module
 combinations.

Create
 Security GroupsSecurity
 groups provide a way of administering permissions over a group of users rather
 than by individual user. When creating security groups, you assign a specific
 group type. Group types include the following:

- 0 - Data

- 1 - Program

- 2 - Reports

- 3 - Attachment Types

Because security groups are associated with a single group / security type,
 most users will belong to at least four security groups (one for each group
 type). For larger and more complex operations, users may belong to more
 groups.

1. [Create Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/create-security-groups)
 on the VA Security Groups form.

1. Add users to the security group using either the
 VA Security Groups or VA User Profile form.

- [Add Users to Security Groups with VA
 Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/add-users-to-security-groups/add-users-to-security-groups-with-va-security-groups)

- [Add Users to Security Groups with VA User
 Profile](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/add-users-to-security-groups/add-users-to-security-groups-with-va-user-profile)

Define Group PermissionsOnce you create a group, you can
 set specific permissions for that group's ability to access the application or
 administer security. All users added to the group will have the same security
 settings. Set these group permissions using the security form that corresponds
 to the assigned group or security type.Note: Before setting data security permissions in VA Data
 Security Access, use VA Data Security Setup to secure specific datatypes and
 tables.

1. Use the appropriate security form to assign
 specific types of security permissions to different groups.Security forms include: [VA Data Security Setup](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form), [VA Form Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form), [VA Report Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form), [VA Attachment Type Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form), [VA Inquiry Security](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form), [VA Work Center Security](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-security-form)
For more details about specific permissions and access provided by each security form, see the descriptions in the article [Initialize Security Access Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/initialize-security-access-form).

Define User-Specific PermissionsWhile security groups specify
 generalized security permissions, some user accounts require specific permission
 settings that no one group provides. See [User Permission Levels](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/user-permission-levels) for more
 information.Note: You can assign data-level security only to groups and not to individual
 users.

1. Use VA Form Security to grant individual users
 access to security forms so they can administer security for other users.

1. Use security forms to grant
 individual users permissions to access various areas of the application.Security forms include: [VA Form Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form), [VA Report Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form), [VA Attachment Type Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form), [VA Inquiry Security](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form), [VA Work Center Security](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-security-form), [VA Data Security Setup](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)
The user-level security settings in these forms interact with group-level
 security settings. For more information, see [Interaction Between Group and User Level Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings).

1. To restrict a specific user's ability to grant
 security permissions to only certain company / module combinations, Master
 Security Administrators can hide the unwanted modules from those users in VA
 Form Security.

- [Create a Master Security Administrator](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/create-a-master-security-administrator)

- [Restrict Security Form Access to Specific
 Company / Module Combinations](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/restrict-security-form-access-to-specific-company--module-combinations)

1. Grant a user full form, report, attachment type,
 inquiry, and work center security, as well as membership in payroll and datatype
 security groups, for all companies.

1. In VA User Profile, select the user.

1. On the Grant tab, select Grant Full Access.


For more detailed information, see [Grant Full Application Access and DBO Security Permissions](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/grant-full-application-access-and-dbo-security-permissions). 

1. Grant full database ownership to a user.

1. In VA User Profile, select the user.

1. On the Grant tab, select Grant DBO. Note: This button is available only if you
 have elevated SQL permissions to grant database ownership (DBO)
 privileges.

For more detailed information, see [Grant Full Application Access and DBO Security Permissions](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/grant-full-application-access-and-dbo-security-permissions).

Related information

- [User Permission Levels](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/user-permission-levels)

- [Interaction Between Group and User Level Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [VA Security Groups Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form)

- [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)

- [VA Attachment Type Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form)

- [About the VA Inquiry Security Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form)

- [About the VA Work Center Security Form](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-security-form)

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)

- [VA Data Security Access Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-data-security-access-form)
