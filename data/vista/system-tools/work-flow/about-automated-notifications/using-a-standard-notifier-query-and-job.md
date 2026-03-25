---
title: "Using a standard Notifier Query and Job | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/about-automated-notifications/using-a-standard-notifier-query-and-job"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/about-automated-notifications/using-a-standard-notifier-query-and-job"
---

# Using a standard Notifier Query and Job

There are several standard Notification Queries and Jobs included in the application. Follow the steps below to set up and activate a standard Notification Job that uses a standard Notifier Query.

1. Open the [WF Notifier Job Manager](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager) form.

1. Select a standard Notifier job.

1. Select
 0-WF Notifier Query
 in the
 Query Type
 field. Note: You can also select
 1-VA Inquiry
 if you want to use a query created using the [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form) form. [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager/field-definitions-wf-notifier-job-manager-form#ID-0004de06--en)

1. The query selected in the
 Query field is the query that will be used to create the
 notifications. [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager/field-definitions-wf-notifier-job-manager-form#ID-0004de06--en)

1. Check the
 Enable Task
 box. This activates the Notifier Job. [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager/field-definitions-wf-notifier-job-manager-form#ID-0004de1a--en)

1. Open the Info tab and use
 the Frequency section to select how often the notifications will be sent - for
 example if notifications should be sent every day, check the Daily box
 and select 1 in the Every: Day/s field.

1. Use the Daily Frequency section to set up how often on the selected days the notifications will be sent.

Example: Once a day, at night
If notifications should be sent at night after
 business hours, select 1 and Once in
 the Every
  fields and then enter a time in the Start Time field.
Example: Multiple times during business hours
If notifications should be sent out multiple times
 during the day during business hours, select 1 and Hour/s in
 the Every fields, and then enter your business hours in the Start
 Time and Stop Time fields. This means
 notifications will be sent once an hour during business hours.

1. Use the Email tab to create
 a rich text or plain text email. For a rich text email, see the
 following.
All standard notification jobs create
 a plain text email. If you want a standard notification job to create a formatted
 email, use the Email tab on the WF Notification Job Manager form to recreate the
 plain text email in rich text.

1. Select Rich
 Text in the Format field.

1. Use the To, CC, and BCC fields to select who should receive the notifications.
 [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager/field-definitions-wf-notifier-job-manager-form#ID-0004de88--en)

1. Complete the Subject field.

1. In the Body section, place the
 cursor where the table should be added.

1. Click the Table button. This will open the [WF Notifier Table Layout ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-table-layout) form.

1. Use the WF Notifier Table
 Layout form to add and format the table that will appear in the email. [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-table-layout)

1. Optional: To add email fields
 to the email, click the  Email Fields button and
 use the form that displays to add parameters to the email. [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-email-parameters)

1. Complete the Body section of
 the email. To add blank lines between paragraphs, press Shift+Enter.

For a plain text email, see the following.

1. Use the Format field to select the type of email that you would like
 to send. [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager/field-definitions-wf-notifier-job-manager-form#ID-0005e14c--en)

1. Click the  Email
 Fields button. This will open the [WF Notifier Email Parameters ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-email-parameters) form, which
 displays a list of parameters from the query. You will use this form to add
 parameters to the fields on the Email tab.

1. Use the To, CC, and BCC fields to select who should receive the notifications.
 [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager/field-definitions-wf-notifier-job-manager-form#ID-0004de88--en)

1. Use the Subject and Header fields to set up
 the subject and body of the notification. Press F1
  in either of these fields for more detailed information.

1. Close the WF Notifier Email
 Parameters form.

1. Check the Consolidated
 Notifications box if you want to create a consolidated
 notification. [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/creating-consolidated-notifications)

1. Open the Parameters tab. If there are local variables on the Notification Query selected in the
 Query
 field on the Info tab, they will display as items on this tab. Set the local variables to define which records will be selected. [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager)

1. Save the Notifier Job.

1. If you want to test the notification, open the Info tab and click the
 Execute Job
 button. This will execute the notification.

1. Notifications will be sent based on the selected Notifier Query and the schedule set up using the Info tab.

Related information

- [About Automated Notifications](/en/vista/vista/system-tools/work-flow/about-automated-notifications)
