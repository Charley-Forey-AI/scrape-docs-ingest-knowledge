---
title: "WF Notifier Job Manager | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager"
---

# WF Notifier Job Manager

Use the WF Notifier Job Manager form to create jobs that generate automatic email notifications.
Notifier jobs are user-defined tasks that the system performs when certain conditions exist. For example, you might need reviewers to review and approve AP unapproved invoices. In this instance, you could create a Notifier job that locates all unapproved invoices that are ready for review, and sends an email to assigned reviewers.
Notifier jobs utilize database queries to determine the type of information to include in notifications. You can use the standard queries included in the application, or you can create your own using the WF Notifier Queries form.
If you are using the Process Workflow feature for the review and approval of purchase orders and subcontracts, you can set up Notifier jobs to send notifications when POs or SLs have been submitted for review, as well as when documents are approved, rejected, or still waiting for review. Vista provides predefined queries for this purpose, which you can assign to the Notifier jobs you create. For more information about creating Notifier jobs, see [Set up a Notifier Job](/en/vista/vista/system-tools/work-flow/about-automated-notifications/set-up-a-notifier-job).
Note: In addition to the notifications sent via the Notifier jobs you create, reviewers and submitters will also receive the standard system notifications used with the Process Workflow feature. If you do not want to receive the standard system notifications, you can suppress them by selecting the Using Review Workflow Notifier Queries checkbox in PM Company parameters for each applicable company. This way, reviewers and submitters will receive only the Notifier job notifications. For more information, see [Using Review Workflow Notifier Queries](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#concept-3175--en).

## Test Email Button

The Test Email button on the Email tab allows you to send test emails to a selected email account. For example if you are creating a new job notification and would like to see how the emails will appear to the recipients, click the new Test Email button on the Email tab and then enter the email address where you want the test emails sent in the message box that appears. By default this message box will populate with the email address associated with your user account (VA User ProfileInfo tab Email Address field).
Use the Send Email button if you want to immediately run the notification job and send emails to the recipients set up using the To, Cc, and Bcc fields.
Important: The entire query will run when you click the Test Email button. This means that if your query returns 1,000 records and the job is not set up as a consolidated notification, you will create 1,000 test emails. Click [here](/en/vista/vista/system-tools/work-flow/about-automated-notifications/creating-consolidated-notifications) fore information about creating consolidated notifications.
Important: This also applies to the Send Email button.

## Send Email Button

The Send Email button on the Email tab allows you to immediately run the notification job and send emails to all of the recipients set up using the To, Cc, and Bcc fields.
Use the Test Email button if you want all of the generated emails to be sent to a single email account, for example your own email account.
Important: The entire query will run when you click the Send Email button. This means that if your query returns 1,000 records and the job is not set up as a consolidated notification, you will send 1,000 emails. Click [here](/en/vista/vista/system-tools/work-flow/about-automated-notifications/creating-consolidated-notifications) fore information about creating consolidated notifications.
Important: This also applies to the Test Email button.

## Consolidated Grouping Tab

The Consolidated Grouping tab only applies to Consolidated Notifications, and it determines how notifications will be grouped. This tab is only enabled when the Consolidated Notifications box on the Email tab is checked.
Click [here](/en/vista/vista/system-tools/work-flow/about-automated-notifications/creating-consolidated-notifications) for information on creating consolidated notifications.

## Parameters Tab

The Parameters tab displays all of the local variables set up on the SQL query selected in the Query field. Use the Input Value column on this tab to set the value of these local variables.

## Job History Tab

The Job History tab displays a history of the notification job. This is the same information that displays in the Log File Viewer in the SQL Server Agent in Microsoft SQL Server Management Studio.

Related information

- [About Automated Notifications](/en/vista/vista/system-tools/work-flow/about-automated-notifications)
