---
title: "About PM Module Email Integration | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/create-and-send/about-pm-module-email-integration"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/create-and-send/about-pm-module-email-integration"
---

# About PM Module Email Integration

With email integration, all emails generated from the PM
 module and the replies to those emails can be added to the associated records as
 attachments.
For example, if you use the Create and Send feature to generate an RFI document and then email that document to a contact on a project using the Create and Send feature, the original email and any replies to that email can be added to the RFI record as attachments.
The email integration feature has four basic steps.

1. Drag and drop sent emails onto a record - From the PM Work Center, highlight a project record
 (RFI, change order, subcontract, etc.) and then drop and drop an email
 associated with that record into the Related Items panel. The email will be
 associated with the record and added to the Emails folder in the Related Items
 panel. The email must have an .msg file extension.

1. Replies to the email are automatically indexed - All emails generated using the Create and Send
 feature include a token. When you receive an email that includes a token, for
 you example you receive a reply to an email, the Outlook Add-in will process the
 email and use the token to automatically attachment the email to the associated
 project record.

1. Optional: Replies to the email can also be manually indexed - You can also use the Outlook
 Add-in to manually attach an email to the project record.

1. View the emails - There are several ways to view the attached emails:

- PM Work Center > Related Items
 panel - Select a record in the PM Work Center and the Related
 Items panel will display all of the emails associated with that record
 in a folder titled Emails. For example
 if you want to view the emails associated with a project issue, open the
 project issue in the PM Work Center and all emails associated with that
 project issue will display in the Emails folder in the Related Items
 panel.

- PM Work Center >  Document Control >  PM Project
 Emails - The PM Project Emails query is a menu option on the
 standard PM Work Center that displays all of the emails associated with
 a selected project. For example, select a project in the Project drop down at the top of the PM Work Center,
 open the PM Project Emails menu option, and the grid will display all of
 the emails associated with the selected project.

- PM Document
 Tracking >  Project Emails
 tab - This tab displays the same information that displays on
 the in the PM Project Emails query on the PM Work Center.

- From the parent record -
 Open the parent record in a form and click the Attachments icon to view
 the emails. For example if you would like to view the emails associated
 with an RFI, open the RFI in PM Request for Information and click the
 Attachments icon. All attachments, including the emails will display in
 the form that opens.

- The Pre-Construction module also has an
 email integration feature. [More](/en/vista/vista/costs-and-contracts/pre-construction/pc-create-and-send/about-pc-module-email-integration)

Set up using MS Outlook
If you use MS Outlook and you want to use to the email integration feature, you need to install and use the [Outlook Add-In](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/email-integration-with-microsoft-outlook). The Outlook Add-In appends a token onto the subject line of emails sent using the PM Create and Send Document form - for example "Email Subject Line VP: SBZV5MBFUD". When you receive an email that contains a token, for example a reply email, the Outlook Add-In uses the token to attach the email to the correct parent record.
Set up using SMTP
If you are using SMTP, emails sent using SMTP include the token but the reply emails are not processed - only the Outlook Add-In can process the reply emails using the token and then associate them with the parent records.
Note: When using SMTP to send emails, you cannot have MS
 Outlook installed on your workstation.
There are two options for attaching the reply emails to parent records when using SMTP.

- Manually - Open the parent record in a
 form in the application and then drag and drop the email onto the form. This will add
 the email as an attachment to the parent record.

- Set up a single workstation to process all reply
 emails - Install MS Outlook and the Outlook Viewpoint Add-In on a single
 work station, create an MS Outlook box, and have that MS Outlook box process all of the
 reply emails. To ensure that all emails are sent to this box, you must set up your
 emails so that the processing email box is the reply address on all emails that are
 sent. For example, a single user can install MS Outlook and the MS Outlook Add-In and
 then all reply emails sent to their box will automatically be processed by the Outlook
 Add-in.

Note: Reply emails will only be processed by the Outlook
 Add-In when it is running, so the MS Outlook box where the reply emails are sent needs to
 be installed and running on a workstation with consistent and high usage.
