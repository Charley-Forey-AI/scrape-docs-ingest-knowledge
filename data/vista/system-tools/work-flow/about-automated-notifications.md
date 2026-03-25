---
title: "About Automated Notifications | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/about-automated-notifications"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/about-automated-notifications"
---

#  About Automated Notifications

When creating workflow checklists, you can have the system send automated notifications to users.
Notifier sends emails or Vista messages to users, and it has several uses:

- Process Workflow - If you are using the [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) feature, the system automatically sends email notifications or system messages when documents (POs and Subcontracts) are ready for review and when they are approved or rejected. However, if you prefer to schedule notifications, you can use predefined queries assigned to Notifier jobs to control when notifications are sent and how often. For more information, see [Use Notifier Queries for Workflow Notifications](/en/vista/vista/project-management/setupmaintenance/use-notifier-queries-for-workflow-notifications).

- Checklists - The Checklists feature uses it to notify users that there is work ready for them. For more information, see [Checklists](/en/vista/vista/system-tools/work-flow/checklists).

- Custom- You can also create your own notifications to alert users when certain conditions are met. For example, you can alert reviewers when an unapproved invoice in AP requires attention.

Click on a link below for more information on a topic.

## Basic Overview

Notifier is broken down into two pieces, which both have to be set up before notifications are sent:

- Queries - Queries are used to select the records that create the notifications. You can use notification queries that are created and maintained using the WF Notifier Queries form, or inquiries that are created and maintained using the VA Inquiries form.

- Use a standard notifier query or inquiry - The application includes many standard notifier queries and inquiries. You can use these standard queries and inquiries to create notifications.

- Copy a standard notifier query or inquiry and then modify the copy - You cannot change a standard notifier query or inquiry, but you can copy the standard and then modify the copy. You can do this using either WF Notifier Queries or VA Inquiries .

- Create a notifier query or inquiry from scratch - You can also use WF Notifier Queries or VA Inquiries to create a query or inquiry from scratch.

- Notifier Job - Once a query has been created, they are associated with notifier jobs. The notifier job determines how often the users should receive notifications, who should receive the messages, and what information should be included. Just like with notifier queries, you can either use the standard notifier jobs included in the application, or you can create your own. Notifier jobs are created and maintained using the WF Notifier Job Manager form.

## Security Consideration

Notifier queries are run from an administrative account that has access to all Viewpoint data. This means that a query could return data that a user should not be able to access. When using Notifier, make sure that the users receiving notifications should be allowed to view the data that is being sent.

## Notification Method

Notifications can be sent in one of two ways:

- Email - These are emails sent to the email address associated with user accounts using the Email Address field on the Info tab of the VA User Profile form.

- VP Message - These are messages sent in the application and are viewed using the VA Messages form.

You can set up how users will receive messages in three places in the application:

- In VA User Profile, define the notification method as follows:

- Notify By field (Info tab) - Use this field to specify the default behavior (that is, whether the user will receive notifications via email or VP message).

- Notification Preferences tab - Use this tab to override the default setting in the Notify By field. For example if a user should receive emails when they have documents to review that are part of the Process Workflow feature, but should receive VP Messages when they have work to complete that is part of the Checklists feature, you can set that up using the Notification Preferences tab. For more information, see [Set User Notification Preferences](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/set-user-notification-preferences).

- In User Options (accessed via the main menu by selecting Options > User Options), use the Notify By field in the Default Notification Method section to change the default behavior on a user account. This will update the selection in the Notify By field on the VA User Profile form.

Before using Notifier, you need to set up an SMTP server using the ServerConfig_Host.exe file, which is located on the Vista server in the Viewpoint Remote Service folder.
The SMTP server is used to send the emails generated by Notifier.
Use the [WF Notifier Options ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-options) form to define the From address on the notifications.
