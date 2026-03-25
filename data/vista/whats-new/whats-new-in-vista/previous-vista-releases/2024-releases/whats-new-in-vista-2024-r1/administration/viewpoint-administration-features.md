---
title: "Viewpoint Administration Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/administration/viewpoint-administration-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/administration/viewpoint-administration-features"
---

# Viewpoint Administration Features

The Vista 2024 R1
 release delivers on user-requested Viewpoint Administration
 enhancements, fixes, and other improvements.

## Coming Soon in 2025! Upgrade Your Vista Login to Trimble ID

Note: Once implemented in early 2025, Trimble ID will be available to Trimble Construction One cloud-hosted Vista customers only.If you are a legacy cloud or on-premises customer, contact your account representative to learn about how you can transition to the modern cloud and gain access to all the latest features.

After the Vista 2024
 R1 release, in early 2025 Trimble ID
 will be enabled for all Trimble Construction One
 cloud-hosted Vista customers over a
 gradual rollout period. Once Trimble ID
 has been enabled for your company, your users will be able to upgrade their logins
 from classic credentials (SQL or Windows domain logins) to Trimble ID.
Trimble ID requires
 that the Vista VA User Profile username
 is an email address, among other requirements. As an admin, you need to review your
 current Vista setup and customizations
 to make sure that switching to Trimble ID logins will not cause problems for your operations.
For more information, see the following resources:

- For information about what to expect, see [Upgrade Vista Logins to Trimble ID FAQ](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information/upgrade-vista-logins-to-trimble-id-faq).

- For guidance about actions admins need to take, see
 [Single Sign-On with Trimble ID: Admin Information](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information).

- For an overview video about the process of creating a
 new Trimble ID and using it to
 log in to Vista, see [Upgrade Your Vista Login to Trimble ID - Video](/en/vista/vista/videos/administration/upgrade-your-vista-login-to-trimble-id---video).

Important:Admins: Prepare for the Upgrade to Trimble IDAfter your company is upgraded to Trimble ID following the 2024 R1 release, you can opt in
 to disable classic logins (SQL and Windows domain logins). Classic logins
 will be disabled for all Trimble Construction One
 cloud-hosted Vista customers in
 the fall of 2025.
It is a good idea to opt in as
 early as possible to understand the impact that the removal of classic
 logins may have on your organization. If you haven't already, review the
 article on how to [Prepare for the Upgrade to Trimble ID](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information/prepare-for-the-upgrade-to-trimble-id).

## Set MFA Requirements for Your Company from the VA Site Settings Form

Note: This information applies to Trimble Construction One cloud-hosted Vista customers using Trimble ID.

Vista administrators
 can now configure multi-factor authentication (MFA) requirements from the VA Site
 Settings form. To access these settings, go to Viewpoint Administration > Programs > VA Site Settings > Add’l Info tab.
Choose how to enforce MFA for your company (options include no
 MFA, MFA through Trimble ID, or MFA
 through other federation methods), whether to allow social logins, or whether to
 require company email addresses in logins.
For details about each option, see [Field Definitions: VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-drt37bpl--en).

## Configure SMTP Settings from the VA Site Settings
 Form

Vista
 administrators can now configure SMTP email settings from the VA Site Settings Form.
 To access SMTP settings, go to Viewpoint Administration > Programs > VA Site Settings > Add’l Info tab. These settings were previously located on the Viewpoint Configuration Server.
For more information about this setup, see [Set Up Vista to Send Emails](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails).
For details about each field, see [Field Definitions: VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-76v1pwu6--en).

## Review Named User License Counts

If you use on-demand licensing to have access to named Vista
 licenses when you need them, you should periodically review your named user count to
 make sure your company does not exceed the number of named user licenses purchased
 in your contract. Your company will be charged for any additional named user
 licenses.
You can review your license counts using the VA User License Allocation
 Report. For more information about reviewing and updating user
 licenses, see [Audit and Update Licenses in Vista](/en/vista/vista/getting-started/getting-started-with-vista/vista-licensing/audit-and-update-licenses-in-vista).

## Improved Auditing to Track System-Wide Changes to F3 Field
 Property Overrides

System administrators can now track system-wide changes to field
 property (F3) overrides and the users who made these changes. Admins can use this
 data to help determine why form or field behaviors changed. F3 changes are audited
 and recorded in the HQ Master Audit (HQMA) table and can be viewed through the HQ
 Audit Detail report or using SQL Server Management Studio.
For more information about viewing these changes, see [View Changes to F3 Field Property System Overrides](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log/view-changes-to-f3-field-property-system-overrides).
Note: User-level field overrides are not audited at this
 time.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
