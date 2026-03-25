---
title: "Single Sign-On with Trimble ID: Admin Information | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information"
---

# Single Sign-On with Trimble ID: Admin Information

Trimble ID allows your users to use the same login credentials for Vista as for other Trimble-licensed products.
Note: Once implemented in early 2025, Trimble ID will be available to Trimble Construction One cloud-hosted Vista customers only.If you are a legacy cloud or on-premises customer, contact your account representative to learn about how you can transition to the modern cloud and gain access to all the latest features.

The following information is for Vista administrators. If you are not an admin, see the following article for information about upgrading your login to Trimble ID: [Single Sign-On with Trimble ID](/en/vista/vista/system-tools/user-interface-guide/log-in-to-vista/single-sign-on-with-trimble-id).

## Prepare for the Upgrade to Trimble ID

Review the following articles so you know what to expect and how to prepare for the migration to Trimble ID:

- [Prepare for the Upgrade to Trimble ID](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information/prepare-for-the-upgrade-to-trimble-id)

- [Upgrade Vista Logins to Trimble ID FAQ](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60053)

## Configure Your Vista Setup and User Records for Trimble ID

Once Trimble ID is enabled for your company, as an administrator, you must complete the following in order for your users to log in with Trimble ID:Make Sure User Records are UniqueEnsure each VA User Profile record is unique for each active Vista user: [VA User Profile Form](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:1d61e29d8f2a42b183c5bf5571aa619e).

- Search through user records to identify and eliminate any duplicate email addresses.

- In each user's VA User Profile, enter the email address that is or will be affiliated with that user's Trimble ID profile.

- When setting up new Vista users in VA User Profile, select the Is SSO Account checkbox and enter the user's email address directly in the User Name field.

Configure MFAConfigure MFA and other login settings for your company: [Configure Multifactor Authentication and Additional Login Settings](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information/configure-multifactor-authentication-and-additional-login-settings).
Set Up Identity Federation (Optional)If you want your organization to have federated logins, you can set up federation through Trimble ID: [Set Up Identity Federation Through Trimble ID](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information/set-up-identity-federation-through-trimble-id).

## Help Your Users Set up Their Own Trimble ID Profiles

Instruct each user to set up their own Trimble ID profile: [Upgrade Your Vista Login to Trimble ID](/en/vista/vista/system-tools/user-interface-guide/log-in-to-vista/single-sign-on-with-trimble-id/upgrade-your-vista-login-to-trimble-id).

- Each user should be able to complete this login upgrade process on their own.

- Share this video with users to provide additional guidance: [Upgrade Your Vista Login to Trimble ID - Video](/en/vista/vista/videos/administration/upgrade-your-vista-login-to-trimble-id---video).

- After a user upgrades their login, going forward they will be required to [log in using Trimble ID](/en/vista/vista/system-tools/user-interface-guide/log-in-to-vista/single-sign-on-with-trimble-id/log-in-to-vista-using-trimble-id).

- After moving to Trimble ID,
 non-federated users will manage their own login credentials at [myprofile.trimble.com](https://myprofile.trimble.com/home).
 For more information, see [Manage My
 Trimble ID Profile](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:accountservices_003:accountservices:accountservices).

Important:Information about classic SQL and Windows domain logins:In the fall of 2025, classic logins (SQL or Windows domain logins) will gradually be removed for Trimble Construction One cloud-hosted Vista customers. Legacy cloud and on-premises customers will continue to use classic logins.
It is a good idea to start fully transitioning your organization to Trimble ID in advance and understand the impact that the removal of classic logins might have. If you haven't already, review the article on how to [Prepare for the Upgrade to Trimble ID](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information/prepare-for-the-upgrade-to-trimble-id).
