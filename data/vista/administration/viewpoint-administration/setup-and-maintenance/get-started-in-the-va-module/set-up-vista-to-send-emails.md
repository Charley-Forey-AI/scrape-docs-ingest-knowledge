---
title: "Set Up Vista to Send Emails | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails"
---

# Set Up Vista to Send Emails

Configure Vista
 to send emails through an SMTP email relay managed by your company.
Using an email account managed by your company has several advantages:

- Reduces the potential for emails sent through the relay to be detected
 as spam.

- Provides direct control over logs to track emails that have been
 sent.

To get started, you first need to choose an email service. Common
 services you could choose include Microsoft Office 365 or Google Gmail. If you
 have a cloud-hosted deployment of Vista, your organization may already have access to Office 365 as a part of your
 subscription, which you could use for your email relay service at minimal extra
 cost.
Important:Attention all customers using Microsoft 365 as
 your email provider:If your current email client is
 Microsoft 365, you *must set up SMTP OAuth before March 2026*. At this time, the
 current Basic Auth configuration will be retired, and your emails will no longer
 work.
We've enhanced our email settings and provided
 options for setting up [SMTP OAuth](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-oauth-email-settings-in-vista) in order to assist you with this transition. We encourage
 you to reconfigure your email relays as soon as possible before the deadline.
 Look for additional communications as this date approaches.

Configure SMTP settings in Vista on the VA Site Settings form and test your email
 account setup *before* committing the changes.
You no longer need access to the Viewpoint Configuration Server to configure SMTP settings.
 Additionally, changing SMTP settings does not require a restart to your
 services.

## What to Do

Complete the following tasks in order. In general, only administrators or your
 company's IT consultants should be the ones configuring the email service
 and SMTP settings.

1. [Set up your email service
 provider](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/set-up-your-email-service-provider).

1. Configure your SMTP email settings in
 Vista:

- [Configure SMTP
 OAuth](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-oauth-email-settings-in-vista)

- [Configure SMTP Basic
 Auth](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-basic-auth-email-settings)

1. [Test
 your SMTP email configuration](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/test-your-vista-smtp-email-configuration).
