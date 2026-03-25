---
title: "Configure SMTP Basic Auth Email Settings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-basic-auth-email-settings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-basic-auth-email-settings"
---

# Configure SMTP Basic Auth Email
 Settings

Configure Vista
 to send emails through an SMTP email relay. SMTP settings are located on the VA Site
 Settings form.
Before you configure SMTP
 settings, first [Set Up Your Email Service Provider](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/set-up-your-email-service-provider).
You no longer need access to the Viewpoint Configuration Server to configure SMTP
 settings.

1. In Vista, go to Viewpoint
 Administration > Programs > VA Site
 Settings > Email Settings
 tab.

1. To enable SMTP, select the checkbox [Send email via
 SMTP](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000499e6--en).

1. In the [Email Client](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-e8jfkjn9--en) field, select
 Basic SMTP.

1. Enter values in the Send Email
 fields:

- [Frequency (sec)](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-25kzja0p--en)

- [Retry Attempts](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-5nym9rjy--en)

1. Enter values in the SMTP Basic System
 Settings.

- [Host](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-76v1pwu6--en)

- [Port](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-pu8c0vib--en)

- [Email Address](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-sffmocpy--en)

- [Domain](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-3iwn9e7q--en) – *Only needed if your SMTP service requires authentication
 and the service is within an NT domain*

- [Username](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-cahjn5v9--en)

- [Password](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-j17enu9g--en)

1. Test your new configuration before
 committing your changes.

1. At the bottom of the form,
 select Send
 Test Email.The Send Test Email window opens,
 summarizing your current SMTP settings.

1. Enter the email address that
 you want to receive the test email, and select OK.You should see a messaging stating
 *Test email sent
 successfully to [youraddress@email.com]. Check
 your inbox or spam folder.*

1. Check your email to verify
 that the message sent. If the message sent, your email
 relay is set up properly.

1. Select OK to save your
 changes.

For all field descriptions listed in one place, see [Field Definitions: VA Site Settings
 Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-76v1pwu6--en).
