---
title: "Prepare for the Upgrade to Trimble ID | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information/prepare-for-the-upgrade-to-trimble-id"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information/prepare-for-the-upgrade-to-trimble-id"
---

# Prepare for the Upgrade to Trimble ID

Before classic logins are disabled for Trimble Construction One cloud-hosted customers in 2026, you should review
 your organization's current Vista setup
 and customizations to make sure that disabling classic logins will not cause
 problems for your operations.
The following applies to administrators of Trimble Construction One cloud-hosted Vista customers only. *These changes do not impact legacy
 cloud or on-premises customers.*
Note: This is not a comprehensive list of scenarios or areas impacted by the changes surrounding the removal of classic logins. As an administrator, you will need to consider additional ways that your operations may be impacted.

Consider the following situations, and take action as necessary for your organization.User ProfilesYou may need to address the following scenarios relating to user profiles:
Duplicate User Email Addresses: Having multiple user profiles with the same email address *will* cause issues when users create their Trimble ID and Vista attempts to link the accounts. Remove any duplicate email addresses before your users start creating their Trimble ID accounts.
Users Without Email Addresses: Since Trimble ID uses an email address for the user name, ensure each user has an email address to log in with, and enter the email address in the VA User Profile form.
Wrong User Type for Database
 Logins: All integrations, service
 accounts, third-party applications, SQL logins,
 and database logins *must* be set up with a [User
 Type](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:350001022) of User
 Application in VA User Profile. As
 long as these accounts are set as User
 Application, they will not be impacted
 when Vista classic logins are
 disabled. For more information, see [Create a Database Account for Non-Vista Users](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-database-account-for-non-vista-users).

SecurityHaving individuals with multiple Vista VA User Profiles or logins to bridge complex security scenarios may cause issues when switching from classic logins to Trimble ID. Trimble Viewpoint typically does not support these setups.
AutomationIf your organization has automation running against usernames that migrate to Trimble ID, the automation will break. This could affect user-defined forms and fields, in addition to other areas, but the full impact is unknown and difficult to predict. You may want to reconfigure your automation before your users move to Trimble ID and off Vista classic logins.
Custom Reports If your organization has custom reports designed with hardcoded filters or logic that looks at particular users, moving to Trimble ID logins may affect your custom reports. Similar to automation, these impacts are difficult to predict.
Datatype OverridesVPUserName Length: If the input length for the VPUserName field has been shortened, this may cause issues when the username must be an email address for Trimble ID. The VPUserName field allows up to 128 characters, which should be sufficient for most email addresses.

ConsultantsIf consultants for your organization currently use a single login for both the Vista application and the Vista database, they will need to have two separate accounts. Once Vista classic logins are disabled for your company, consultants will not be able to access the Vista application with that login.
