---
title: "About PC Module Email Integration | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-pc-module-email-integration"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-pc-module-email-integration"
---

# About PC Module Email Integration

With email integration in the PC module, you can associate email threads with potential projects so that from within the application, you can view all correspondence related to a potential project.
Note: If you have MS Outlook installed, you need to install the [MS Outlook add-in](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/email-integration-with-microsoft-outlook) and have MS Outlook open while you are using the application to take advantage of the email integration feature.

## Sending Emails

If you use the [PC Create and Send](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-the-pc-create-and-send-form) form to send emails, Vista attaches them (and any responses) to the potential project or bid package record. A record of the email is also added to the Correspondence tab of the [PC Potential Projects](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-potential-projects-form) form, which stores a log of all sent emails that are associated with a selected project.Note: This applies whether you're set up to use the MS Outlook Client or SMTP to send emails.

Whichever Vista form you use to send the email dictates where it gets attached and where you may view it later:

- PC Potential Project > Info tabCreate and Send - a copy of the email is attached to the potential project record. Click the Attachments icon at the top of the [PC Potential Projects](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-potential-projects-form) form.

- PC Potential Project > Bid Package tabCreate and Send - a copy of the email is attached to the bid package record. Click the Attachments icon at the top of the [PC Bid Package](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/bids/about-the-pc-bid-package-form) form.

## Receiving Emails

Received emails are attached to potential project records in several ways.

- Automatically, with the Add-in - If you're [set up to use the MS Outlook Add-In](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/email-integration-with-microsoft-outlook), Vista applies a token in the subject field of all emails you send using the PC Create and Send form (for example, VP: SBZV5MBFUD). Using the token, Vista adds the response emails as attachments to the associated record, that is, either the bid package or the potential project.

- Manually, with the Add-in - Even if a received email does not contain a token, you can achieve the same outcome:

1. use the Outlook Add-In Index form to index the email by adding the bid package number to it

1. attach the email to an existing record

1. open the bid package in the PC Bid Package form

1. locate the email using the DM Attachment Index Search form

1. associate the email with the bid package record

- Manually, without the Add-in - If you do not have the Outlook Add-In installed, you can drag and drop sent and received emails directly to an open record in PC module forms. This adds the email as an attachment to the record.

## Automated Response Forms

The Outlook Add-In includes an automated response processing feature.

1. You: email a PDF form to a vendor or contact on a potential project.

1. Your contact: returns the completed form via reply email.

1. Vista: extracts the information from the completed form and applies it to the record

For more information, see [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms).

## SMTP and Email Integration

If you do not have MS Outlook installed, the following applies:

- Sending Emails - Vista saves sent emails as attachments on the associated parent record.

- Receiving Emails - Even though SMTP cannot automatically process received emails and attach them to the associated parent record, these options accomplish the same thing:


- Set up a single workstation to process all reply emails:Note: The Outlook Add-In must be actively running in order to process reply emails, so choose a workstation with consistent and high usage. It need not be a dedicated workstation.

1. Install MS Outlook and the Vista Add-in on the work station.

1. Use the Reply To Email field on the Messages tab of the PC Create and Send form.All reply emails will be routed to this workstation, processed by the Outlook Add-in, and attach them to the associated parent record.Note: This is feasible since Vista applies a token to all outbound emails, even if you don't have the MS Outlook Add-in installed on the senders' workstations.

- Manually attach emails

1. Save the email as a file in a local or network folder location.

1. Open the pertinent record in Vista.

1. Drag and drop the file onto the record.

Related concepts

- [About Automated Response Forms](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-automated-response-forms)

- [Email Integration with Microsoft Outlook](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/email-integration-with-microsoft-outlook)
