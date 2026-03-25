---
title: "Set Up Your Email Service Provider | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/set-up-your-email-service-provider"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/set-up-your-email-service-provider"
---

# Set Up Your Email Service Provider

Choose an email service provider for your relay and set up the company
 email account.
Adapt these steps to apply them
 to any email service provider that supports OAuth or authenticated basic SMTP. Important:Attention all customers using Microsoft 365 as
 your email provider:If your current email client is
 Microsoft 365, you *must set up SMTP OAuth before March 2026*. At this time, the
 current Basic Auth configuration will be retired, and your emails will no longer
 work.
We've enhanced our email settings and provided
 options for setting up [SMTP OAuth](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-oauth-email-settings-in-vista) in order to assist you with this transition. We encourage
 you to reconfigure your email relays as soon as possible before the deadline.
 Look for additional communications as this date approaches.

Note: This task is intended for
 technical audiences, such as your local IT consultant, and is a
 prerequisite for configuring Vista to send emails.For additional technical details and methods for setting up an
 email service, log into the Viewpoint Customer Portal and reference the following
 Knowledge Base article: [Changing From
 TurboSMTP to an Email Service of Your
 Choice](https://support.viewpoint.com/s/knowledgedetail?c__urlname=Changing-from-Turbo-SMTP-to-email-service-of-your-choice).

1. Choose an email service.Common recommended services you could choose for
 your relay include Microsoft Office 365 and Google Gmail. For
 more information about using either of these services, see the
 following articles:

- [Microsoft
 Office 365](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365)

- [Google
 Gmail](https://support.google.com/a/answer/2956491) – *currently experimental. You may
 find that additional testing is needed.*

1. Set up the email account. Make sure this is the main administrator account, which should have
 send
 as or allowed
 sender permissions to allow other accounts to
 send emails on behalf of this account.
Tip: Search your email service's help documentation for
 specific steps and details.

After you set up the email
 service and confirm that the account is able to send emails through SMTP, you must
 configure SMTP email settings in Vista. The configuration is different depending on if you use SMTP OAuth or Basic
 Auth:

- [Configure SMTP OAuth Email Settings in
 Vista](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-oauth-email-settings-in-vista)

- [Configure SMTP Basic Auth Email
 Settings](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-basic-auth-email-settings)
