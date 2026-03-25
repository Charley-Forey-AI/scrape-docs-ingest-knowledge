---
title: "Configure Multifactor Authentication and Additional Login Settings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/configure-multifactor-authentication-and-additional-login-settings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/configure-multifactor-authentication-and-additional-login-settings"
---

# Configure Multifactor Authentication and Additional Login Settings

Set up multifactor authentication (MFA) for your organization and place additional restrictions on logins for your Vista users.
MFA and login settings are enforced at the company level, meaning that the settings you select apply to all user profiles in that Vista company.
You must be a system administrator to make changes to the VA Site Settings form. MFA fields only apply to organizations with Trimble ID implemented.

1. From the main Vista menu, go to Viewpoint Administration > Programs > VA Site Settings.

1. Select the Add'l Settings tab.

1. In the Single-Sign On section, select an option from the MFA Required dropdown field:

- None: Select this option if you do not want to require any sort of multifactor authentication at log in. Users can still choose to enable MFA on an individual basis while setting up their Trimble ID profile.

- MFA: Select this option to require multifactor authentication through Trimble ID. Other MFA methods are not permitted with this option.

- Federated: Select this option to require multifactor authentication, either through external providers (such as Microsoft, Okta) *or* through Trimble ID. Federated authentication is based on a user's email domain.

For more details about this field, see [MFA Required](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-drt37bpl--en).

1. If you want to require users to log into Vista using the email address specified in VA User Profile, select the User Email Enforcement checkbox. Tip: This is recommended in order to simplify the process of upgrading to SSO with Trimble ID, as it forces matching emails between the Vista user profile and Trimble ID profile.

For details, see [User Email Enforcement](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-j3xpblzb--en).

1. Select Save.
