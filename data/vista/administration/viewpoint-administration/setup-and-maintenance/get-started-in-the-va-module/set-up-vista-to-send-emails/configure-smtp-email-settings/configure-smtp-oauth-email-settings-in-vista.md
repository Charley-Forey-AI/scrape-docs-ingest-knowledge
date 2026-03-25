---
title: "Configure SMTP OAuth Email Settings in Vista | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-oauth-email-settings-in-vista"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-oauth-email-settings-in-vista"
---

# Configure SMTP OAuth Email Settings in
 Vista

Configure Vista to send emails through an SMTP email relay. SMTP
 settings are located on the VA Site Settings form.
Before you configure SMTP
 settings, first [Set Up Your Email Service Provider](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/set-up-your-email-service-provider).
You do not need access to the Viewpoint Configuration Server to configure SMTP
 settings.

1. In Vista, go to Viewpoint
 Administration > Programs > VA Site
 Settings > Email Settings
 tab.

1. To enable SMTP, select the checkbox [Send email via
 SMTP](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000499e6--en).

1. Select your [Email
 Client](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-e8jfkjn9--en). It is recommended to choose an
 option that supports SMTP OAuth for increased security, so choose from
 one of the following OAuth options:

- Microsoft
 365

- Gmail
 (experimental) – *you may find that
 additional testing is needed*

1. Enter values in the Send Email
 fields:

- [Frequency (sec)](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-25kzja0p--en)

- [Retry Attempts](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-5nym9rjy--en)

1. In the SMTP Basic System Settings, enter
 the [Email
 Address](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-sffmocpy--en) associated with the main
 administrator account for your email provider. This address will show
 as the *From* address that your users will receive.The following fields automatically update to the
 correct values for the SMTP OAuth client you selected:
 Host, Port.
The following fields are not necessary for
 setting up SMTP OAuth: Domain,
 Username, Password.

1. Enter values in the SMTP OAuth fields.
 Retrieve this information from your email provider. These fields are
 editable as long as you selected either Microsoft 365 or
 Gmail
 for your email client above.

- [Client ID](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-hwcclrls--en)

- [Tenant ID](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-p9lom3ge--en) – *for Gmail only, leave
 this field blank, it is not required*

- [Client Secret](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-o9ivtxja--en)

1. Test your new configuration before committing your changes.

1. At the bottom of the form, select Send Test
 Email.The Send Test Email window opens,
 summarizing your current SMTP settings.

1. Enter the email address that you want to receive the test
 email, and select OK.You should see a messaging stating
 *Test email sent
 successfully to [youraddress@email.com]. Check
 your inbox or spam folder.*

1. Check your email to verify that the message sent. If you received the email, your
 email relay is set up properly.

1. Select OK to save your changes.

For all field descriptions listed in one place, see [Field Definitions: VA Site Settings
 Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000499e6--en).
