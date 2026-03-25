---
title: "Upgrade Vista Logins to Trimble ID FAQ | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information/upgrade-vista-logins-to-trimble-id-faq"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information/upgrade-vista-logins-to-trimble-id-faq"
---

# Upgrade Vista Logins to Trimble ID FAQ

Answers to common questions about the Trimble ID upgrade, where Trimble Construction One cloud-hosted Vista customers will have Trimble ID logins
 enabled and classic logins (Windows or SQL credentials) disabled.

## What is this change?

In the first half of 2025, we are upgrading all Trimble Construction One cloud-hosted Vista customers to log in using Trimble ID. This upgrade will enable you to take advantage of the broader technology base throughout the Trimble ecosystem, which means a better software experience for you. We will be rolling out this change in two parts:
1: We will enable Trimble ID loginsWhat this means for you: Our migration team will enable Trimble ID in your Vista instance as a part of the upgrade process. After the upgrade, your users will be able to self-migrate to Trimble ID by selecting Sign in with Trimble ID from the Vista login screen. The system will walk them through the process.
As an admin, you may need to make sure user emails are set up correctly in VA User Profile. For more information, see [Set Up Trimble ID: Admin Information](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60002).
2: We will disable Vista classic loginsWhat this means for you: Starting in the *fall of 2025*, we will be turning off support for classic credentials used to log into the Vista application.
Integrations, service accounts, third-party applications, SQL logins, and database logins *will not be impacted*, as long as these accounts are set up with a [User Type](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:350001022) of User Application in VA User Profile. For more information, see [Create a Database Account for Non-Vista User](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60093).

For more information about how you can get ready for these upcoming changes, see [Prepare for the Upgrade to Trimble ID](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60066).

## Who is impacted?

All Trimble Construction One cloud-hosted Vista customers will be upgraded to Trimble ID logins.
If you are a legacy cloud or on-premises customer, contact your account representative to learn about how you can transition to the modern cloud and gain access to all the latest features.
Note:Trimble ID is currently not available for organizations in Australia.

## I'm already using Trimble ID, how does this impact me?

If you are already using Trimble ID, this upgrade should have very little impact on your organization. You can expect the following:

- Slight delay during first login: On the day after the upgrade, your users may experience a few extra seconds of delay during login as their credentials are reconfigured.

- Simplified future logins: Once the initial reconfiguration is complete, the login process itself consists of fewer screens. Users will be directed straight to the Trimble ID login page.

- Streamlined onboarding for new users: The process to onboard a new user will be simplified, no longer requiring separate user migrations to Trimble ID. As long as the user's email is set up correctly in VA User Profile, users will self migrate to Trimble ID the first time they log into Vista.

## What is the timeline for this?

We are planning a gradual migration to Trimble ID for our cloud customer base starting in early 2025, after the Vista 2024 R1 release.
Starting in the fall of 2025, we will gradually turn off classic logins for all Trimble Construction One cloud-hosted Vista customers.
As soon as your company has been upgraded to Trimble ID, you can opt in to disable Vista classic logins early, before the actual cutoff. It is a good idea to start transitioning your organization off classic logins in advance and understand the impact that the removal of classic logins might have. If you haven't already, review the article on how to [Prepare for the Upgrade to Trimble ID](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60066).

## What level of involvement will be expected from our company for a successful move to Trimble ID?

Before the migration, you should evaluate your organization's current Vista setup and take steps to [Prepare for the Upgrade to Trimble ID](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60066).
After Trimble ID is enabled for your company, every cloud user who doesn't currently log in using a Trimble ID will be required to do so. Users will be guided through the setup process on their own. To see what that process will be like, watch this video: [Upgrade Your Vista Login to Trimble ID](https://player.vimeo.com/video/1046540583?h=6919f3b932).

## Can I opt out?

We will contact all cloud-hosted organizations required to make the move to Trimble ID. This transition ultimately leads to a better software experience for you.

## How will we know when our organization is being migrated?

We will email you in advance with the transition plan. This email will include:

- A link to a video for your employees to watch

- A link to a recorded webinar for you to watch

- An email template that you can use to communicate with your users

All key contacts and any others who have opted in to receive release bulletins will receive this email. Key contacts are those designated in the [Viewpoint Customer Portal](https://support.viewpoint.com) as individuals in your company who will receive these types of communications.

## What can admins do to prepare for this?

There are a number of actions admins can take to make the transition smoother.

- Watch and share this video with your users: [Upgrade Your Vista Login to Trimble ID](https://player.vimeo.com/video/1046540583?h=6919f3b932).

- Communicate with users about the upcoming changes.

- Search through user records to identify and eliminate any duplicate email addresses.

- Since Trimble ID uses an email address for the user name, ensure each user has an email address to log in with, and enter the email address in the VA User Profile form.

- Consider if you want to require multifactor authentication (MFA) for all users in your organization. You can opt to turn it on in the VA Site Settings form.

For additional considerations, see [Prepare for the Upgrade to Trimble ID](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60066) and [Set Up Trimble ID: Admin Information](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60002).

## Will the user interface change?

No.

## Is there a cost associated with this migration?

No. This activity does not
 affect your current contract with Trimble Viewpoint.

## What if I use multiple logins?

As a best practice, it is not recommended that you use multiple logins. However, if you do, each will need to have its own email address. Duplicate emails are not allowed within your organization. Note that multiple usernames will consume additional licenses.

## Does this upgrade change how I add new Vista users?

Yes.
To directly set up the new user with a Trimble ID account, make sure to do the following on the VA User Profile form:

1. Enter the user's email address in the User Name field. This email should be the one that will be associated with the user's Trimble ID profile.

1. Select the Is SSO Account checkbox. This indicates to the system that the account uses Trimble ID credentials based on the user's email address, and to bypass the creation of a SQL login password.

For more information about adding Vista users, see [Create a Vista User SSO Account with Trimble ID](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60062).

## After the upgrade, can admins update the Trimble ID email address or password for users?

After the upgrade, all users will manage their own Trimble ID sign in credentials at [myprofile.trimble.com](https://myprofile.trimble.com/home).Note: Federated users must work with their IdP admin to change their email address.

## I don’t have access to my authentication app, so I cannot authenticate using MFA. What should I do?

Contact [Trimble Support](https://www.trimble.com/en/contact-support).

## Will this affect my federation with Microsoft Entra / Azure?

No.
If you’ve federated with Microsoft Entra ID (formerly Azure Active Directory, or AAD), you’re already using Trimble ID.
If you haven't already federated with Microsoft Entra, the upgrade to Trimble ID makes it possible. To get started with moving to federated logins, complete the [Trimble ID Federation form](https://docs.google.com/forms/d/13b6OmHB8vxe3aJEtHtviCAQWr7Zqta1PXQJsStui6j4/viewform).

## How do I know if I am already federated?

If you are already federated, when you go to [myprofile.trimble.com](https://myprofile.trimble.com/home) and enter your email, you will be redirected to Microsoft (or another federation provider, depending on your setup) to finish logging in.

## Can I use an existing Trimble ID to sign in?

Yes. One of the benefits of using a Trimble ID is that you can sign in to many Trimble products with this same set of credentials.Note: For security reasons, your administrator may require you to use a company email address. This may require you to edit your Trimble ID email address to match.

## How is this migration different from migrating users to Trimble Construction One?

The difference is that admins no longer need to migrate users. Each user will have the ability to self-migrate their existing Vista credentials to Trimble ID, by selecting Sign in with Trimble ID from the Vista login screen. The system will walk users through this process.

## How does using Trimble ID impact me if I access Vista through a remote desktop / AVD?

The implementation of Trimble ID will not impact logging in to your remote desktop / Azure Virtual Desktop. However, when users log into Vista through the remote desktop, they will need to update their Vista logins to Trimble ID.
If users have synced their remote desktop and Vista logins, this setup will break when classic logins are disabled in 2026. Users will need to have a login for accessing their remote desktop, and a Trimble ID login for accessing Vista.

## How will the Trimble ID migration impact Vista Web customers?

If you are a Vista Web cloud customer currently using Viewpoint ID, we anticipate minimal disruption to your users as you transition to SSO with Trimble ID. Requirements to use Trimble ID with Vista WebTo use Trimble ID, your organization must meet the following requirements:

- You are a Trimble Construction One cloud customer

- You are on Vista Web 25.2 or higher

- You are on Vista 2024 R1 or higher

- You have Trimble ID enabled in Vista. This requires flipping a switch on the Vista backend. Our migration team will complete this step.

Australian customers will continue to use Viewpoint ID at this time.
Changes to Vista WebYou will notice several changes in Vista Web once you transition from Viewpoint ID to Trimble ID:

- On the portal login page, the SSO option will update to Sign In with Trimble ID.

- Any reference of Viewpoint ID or VPID in the user interface will change to Trimble ID or TID.

- Once you have Trimble ID enabled, your users should log in with the existing email they used previously for Viewpoint ID. The first time they enter this email address to log in, their account will automatically upgrade to Trimble ID.

- Trimble ID is based on the user's email address in their Vista VA User Profile or PR Employee record. If a user does not have their email entered in either of these records, a system admin must add it so the user can log in and their account can automatically upgrade to Trimble ID.

- Similar to Vista, Vista Web will also be moving to Trimble ID-only logins. Once Trimble ID is enabled for your organization, you'll have a dedicated period of time to transition all user accounts to Trimble ID. We will begin enforcing Trimble ID logins starting in January 2026 in scheduled waves.

- Admins no longer manually link user portal profiles to Trimble ID accounts, as this is done automatically when the user logs in.

- Only Vista Web system admins or security admins will be able to unlink Trimble ID from a user's portal profile.

- You can now manage your organization's multifactor authentication (MFA) through settings in Vista.

For details, review the Vista Web Help: [Trimble ID Logins for Vista Web](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:HRV_000092:HRV:HRV).

## What if I have more questions?

Watch our recorded webinars on migrating from Vista classic credentials to Trimble ID:

- [Webinar 1](https://videos.trimble.com/construction/watch/uFKspkSJjANv3QaZEHPis4) (held on February 4, 2025)

- [Webinar 2](https://videos.trimble.com/construction/watch/J16DmhRcfcYuXHDzSDThLX) (held on February 6, 2025)

You can send additional questions to *vista-tid-questions-ug@trimble.com*.
