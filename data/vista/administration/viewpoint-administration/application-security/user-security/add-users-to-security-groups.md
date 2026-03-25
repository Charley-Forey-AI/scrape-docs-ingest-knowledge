---
title: "Add Users to Security Groups | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/user-security/add-users-to-security-groups"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/user-security/add-users-to-security-groups"
---

# Add Users to Security Groups

Once you have created security groups, you can add users to security groups from two locations in the software.
When you first implement group security, you will typically add users in [VA Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form). If you add users to the system after group security has been implemented, it is easier to add users to the group after you create their login in [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form). Changes made on one form automatically update the other. You can also add multiple users to a security group at once with [VA Add Users to Group](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-add-users-to-group-form).
 If a user belongs to more than one group, the group
 with the least restrictive setting takes precedence over the other group's settings. If
 a user belongs to a security group and also has user-level security settings, those
 settings interact. To learn more, see [Interaction Between Group and User Level Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings).
Important: In order to add or delete users from security groups, you must have permissions for all relevant areas relating to security, including:

- Form security access to VA Security Groups form

- Form security access to *all* of the companies where that security group is used

- Access to all other types of security where that security group is used (such as Forms, Reports, Inquiries, Work Center, or Attachment Types).

It is recommended that the system administrator create a
 security group named *Standard Viewpoint Forms* that has access to [VP Forms](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/vp-module-forms). Forms not assigned to a specific form or
 module (for example: Batch Selection, Field Properties, etc.) are VP forms. You should
 associate all users with this group in all companies. For details about creating
 security groups, see [Create Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/create-security-groups).
Here are the various ways you can add users to security groups:

- [Add Users to Security Groups with VA
 Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/add-users-to-security-groups/add-users-to-security-groups-with-va-security-groups)

- [Add Users to Security Groups with VA User
 Profile](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/add-users-to-security-groups/add-users-to-security-groups-with-va-user-profile)

- [Add Multiple Users to a Security
 Group](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/add-multiple-users-to-a-security-group)

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [VA Security Groups Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form)

- [VA Add Users to Group Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-add-users-to-group-form)

- [Create Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/create-security-groups)
