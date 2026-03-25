---
title: "User Roles and Data Access | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/automatic-invoicing-for-trimble-construction-one-users/give-a-user-access-to-automatic-invoicing/user-roles-and-data-access"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/automatic-invoicing-for-trimble-construction-one-users/give-a-user-access-to-automatic-invoicing/user-roles-and-data-access"
---

# User Roles and Data Access

The Trimble Construction One user role
 controls what the user can see and do in Viewpoint Team™, Trimble Analytics™, or
 Automatic Invoicing, and whether or not a
 user can access the Admin Center.
See the following sections for details on each user setting:
[Enterprise Roles](#reference-913--en__tc1_enterprise_roles)
[Project Communication Roles](#reference-913--en__tc1_project_comm)
[Analytics Roles](#reference-913--en__tc1_analytics_roles)
[Analytics Features](#reference-913--en__tc1_analytics_features)
[HR Forms Roles ](#reference-913--en__tc1_HR_mgmt_roles)
[Accounts Payable Roles](#reference-913--en__tc1_ap_roles)
Note: HR user roles are managed in HR Management.

## Enterprise Roles

The Enterprise Role determines who has the Enterprise Admin level of access.
RoleDescription
UserMost users have this access level. Contacts who are invited to create a login are given this access level. These users cannot access the Admin Center.Note: This setting alone does not provide access to Team. To work in Team, users must also have a Project Comm. role of User, Reviewer, or Admin.

Enterprise AdminThese users can access the Admin Center and modify other users and system settings.
This access should be limited to trusted individuals within your own organization.
For Team, these users can assign a Project Manager to a project.
For the Employee Self-Service module of HR Management, these users can perform the same administrative tasks as HR admins.

## Project Communication Roles

The Project Communication (Project Comm.) role determines what a user can see and do in Team.
Note: To work in Team, a user must have a Project Communication role of User, Reviewer, or Admin. A user set to None will not be able to access to Team.

RoleDescription
UserMost users have this access level. This allows them to work in Team. Contacts who are invited to create a login are given this access level.
ReviewerReviewers can be invited to Team projects for review-only purposes. They can view all work items, and comment on those work items, but cannot edit anything.
AdminIn addition to working in Team, these users can add, manage, and delete projects. They can also assign a Project Manager to a project.
Note: This setting does not provide access to the Admin Center. To access the Admin Center Team, a user must have an Enterprise Role of Enterprise Admin.

## Analytics Roles

The Analytics role determines what a user can see or do in Trimble Analytics.
RoleDescription
UserMost users have this access level.User permissions are defined by the Permissions Group to which a user is assigned. For more details, see [Access Levels for Permission Groups](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:Analytics_000008:Analytics:Analytics).
ReviewerPermissions are defined by the Permissions Group to which a user is assigned. For more details, see [Access Levels for Permission Groups](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:Analytics_000008:Analytics:Analytics).

AdminAdmins have full permissions to view, create, edit, and delete reports, tags, and permission groups.

## Analytics Features

The Analytics Features setting determines what features the user can access in Trimble Analytics. For details about the different features see [About Trimble Construction One Analytics](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:Analytics_000001:Analytics:Analytics).
FeatureDescription
DashboardsThe Dashboards feature in Trimble Analytics provides detailed visualizations of your ERP data (Vista and Spectrum). It includes:

- Access to Standard Power BI Reports.

- Power BI Report creation.

The Dashboards feature requires an Analytics license.
Paginated ReportsPaginated Reports in Trimble Analytics enable you to view and share reports for data in Vista and Vista Web without accessing those applications directly. Paginated Reports requires an Analytics license.
Vista ReportsVista Reports provide access to your Vista Crystal Reports on the web from Trimble Analytics without opening Vista. The Vista Reports feature requires an Analytics license.

## HR Forms Roles

The HR Forms Role determines whether a user can configure your hiring process
 builder, manage custom tasks, or manage lookups for HR Management.
RoleDescription
AdminThese users can configure your hiring process builder, manage custom
 tasks, and manage lookups for forms in Onboarding.Note: This setting is
 specific to forms and does not provide access to admin
 settings in HR Management. See [Manage HR User Roles](https://help.trimble.com/en/viewpoint-hr-management-for-spectrum/hr-management-for-spectrum/hr-administration/hr-administration/hr-role-management/manage-hr-user-roles) for details.
Note: This setting does not provide access
 to the Admin Center. To access the Admin Center, a user must
 have an Enterprise Role of Enterprise Admin.

SpecialistThese users can configure your hiring process builder, manage custom
 tasks, and manage lookups for forms in Onboarding.Note: This setting is
 specific to forms and does not provide specialist-level
 access to Onboarding or Employee Self-Service. See [Manage HR User Roles](https://help.trimble.com/en/viewpoint-hr-management-for-spectrum/hr-management-for-spectrum/hr-administration/hr-administration/hr-role-management/manage-hr-user-roles) for details.
Important: HR Specialists must be assigned to a profile group in
 Onboarding or a permission group in
 Employee Self-Service in order to see any
 information after logging in.

## Accounts Payable Roles

The Accounts Payable role determines whether or not a user can access Automatic Invoicing, and other permissions regarding batches.
RoleDescription
UserThe User can access Automatic Invoicing.
NoneNo access to Automatic Invoicing.
AdminThe Admin can access Automatic Invoicing and delete batches created by any user in the Enterprise. Whereas, Users can only delete the batches they created. The Admin can also add an account to the Inbox.
