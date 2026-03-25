---
title: "Field Definitions: WF Notifier Job Manager Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager/field-definitions-wf-notifier-job-manager-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager/field-definitions-wf-notifier-job-manager-form"
---

# Field Definitions: WF Notifier Job Manager Form

The following is a list of field descriptions for the WF
 Notifier Job Manager form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Job Name

Enter a unique name to identify this Notifier job, up to 30 characters. Press F4 for a list of available jobs.
Note: Notifier jobs are not company-specific and are shared between all companies. Additionally, if you are copying the job from one database to another, the name must be modified so it is unique for each database.

## Description

 Enter a description of the job. The description can be up to 255 characters long.

## Query Type / Query

Select a value in the Query Type drop
 down and then use the Query field to select a specific
 query.
The selected query selects the records that create the notifications. You can select either a notifier query or an inquiry.

### WF Notifier Query

Press F4 to select a notifier query from a
 list. You can select a standard notification query included in the application or a
 notification query that you create yourself.
Notifier queries are created and maintained
 using the [WF
 Notifier Queries ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries) form. Press F5 to open this form. You can see the
 SQL SELECT statement and WHERE clause that will be used to select the records that will
 generate the notifications.
If you select a query that contains a local
 variable, make sure that you select a value for that variable using the Parameters tab
 on this form.

### VA Inquiry

Press F4 to select an inquiry from a list.
 This allows you to select a standard inquiry, or one that you created using the [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form) form. You can select a SQL or view query,
 but not a form query, which allow you to add a query to a tab on a form.

##  Enable Task

 Check this box to activate the job.
When this box is checked, the system automatically runs the job based on the frequency set up using the Info tab.
 Uncheck this box to deactivate the task.

## Occurs

Select the appropriate radio button to set the occurrence pattern:

- Daily – Select this option to have this job run on a daily basis.

- Weekly – Select this option to have this job run on a weekly basis.

- Monthly – Select this option to run on a monthly basis.

##  Day __ of

 This field is only available for the Monthly occurrence pattern.
 Specify the day of the month (1-31) this job runs. For example, if you select “15”, the job runs on the 15th of each specified month.

## Frequency

This field displays as Every _ Day/s
 when you select the ‘Daily’ occurrence pattern. Specify the interval of days (1-7) for
 running this job. For example, if you select “1”, the job runs every day. If you select
 “2”, the job runs every other day (e.g. Sun, Tues, Thurs, Sat), and so on.
This field displays as Every _ Week/s
 On when you select the ‘Weekly’ occurrence pattern. Specify the interval of
 weeks (1-4) for running this job. For example, if you select “1”, the job runs every week.
 If you select “2”, the job runs every other week, etc.
This field displays as Every _ Month/s
 when you select the ‘Monthly’ occurrence pattern. Specify the interval of months (1-12) for
 running this job. For example, if you select “1”, the job runs every month. If you select
 “6”, the job runs every 6 months, etc. Use this option in conjunction with the Day _ of field
 to determine when the job runs. For example, if you specified “1” here and “15” in the
 Day _
 of field, the job runs on the 15th of every month.

##  Weekly: Monday - Sunday

 These fields display for the Weekly occurrence pattern only.
 Check the box for each day of the week you want this Notifier job to run. Use this option in conjunction with the weekly interval to determine when the job runs. For example, if you checked Monday, Wednesday, and Friday, and entered “2” for the “Every __ Week/s” option, then the system runs the job Monday, Wednesday, and Friday every two weeks.

## Daily Frequency: Every __

These two options determine how often this job runs on the days specified by the occurrence pattern. The options available in the first drop-down box are determined by the option selected in the second drop-down box.
Box 1
Box 2
Description

1
Once
Select these options if you want the job to run once a day. The time the system runs the job is indicated in the Start/Stop Time fields below.

1-60
Minutes/s
Select these options to run the job in minute intervals. For example, if you select “Minute/s” and “30”, the job runs every half hour.

1-24
Hour/s
Select these options to run the job in hourly intervals. For example, if you select “Hours/s” and “4”, the job runs every 4 hours.

Note: The intervals specified here work in conjunction with the occurrence pattern and the daily frequency specified in previous fields.

## Daily Frequency: Start Time/Stop Time

Specify the start and stop times (24-hour format) for this job; this is the range within to run the job, based on the occurrence pattern and daily frequency.
If you elect to run at several intervals in a day, this is the hours between which the job is run (for example, once every hour between 8:00 and 17:00).

## Duration: Start Date/Stop Date

Specify the start and stop dates for this job. This is the range within to run the job, based on the occurrence pattern and the daily frequency. For example, you can specify to start running the job on 03/01/09 and end it on 12/31/09, or leave the ending date blank to indicate the job is ongoing.

## To/Cc/Bcc

Use these fields to set up who will receive the notifications. You can either select an email address or use a parameter from the query.

### Select a Contact

To select a contact, click on the
 To, Cc, or Bcc buttons
 on the Email tab. This will open a form that allows you to select a contact from a
 list.

### Parameters

To use a parameter, click in the To,
 Cc, or Bcc fields, click the Email Fields
 button to display a list of available parameters, and then double click on an email
 parameter.
For example, if you are setting up an email
 notification job for unapproved invoices, select the [Reviewer
 Email] parameter. The job will send a notification to each reviewer
 assigned to the unapproved invoice using the email address assigned to each reviewer in
 HQ Reviewers.

##  Subject

Use this field to enter the subject of the notification. The text in this field can be up to 100 characters long.
You can manually enter text into this field, and you can also use the [WF Notifier Email Parameters ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-email-parameters) form to add parameters to the field.

##  Body

Use this field to enter the body of the email.
This field displays only when Rich Text is
 selected in the Format field.
Adding a formatted table
Click the Table button to add a formatted table to
 the body of the email. This will add the query results to the email in a formatted
 query.
For more information, see [WF Notifier Table Layout ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-table-layout).
Adding email fields
Click the Email Fields button to add email fields
 to the body of the email.
Adding blank lines in the body of the email
Press Shift+Enter to add a blank line within
 the body of the email.

##  Header

### Standard Notifications

 Use this field to enter the body of the
 email.
In addition to manually entering text, you
 can also use the query’s available parameters to include specific information. For
 example, if the email notification is set up for unapproved invoices, you can use
 parameters to pull in the invoice number, date, invoice total, vendor, etc. A separate
 email notification is sent for each record returned by the query.

### Consolidated Notifications

The text in this field will display once at
 the top of each email and can be up to 1,000 characters long.
The diagram below outlines the basic
 structure of a consolidated notification. The Headerand Footer each
 display once, and the Line field displays for each record
 returned by the Notifier Query.
For more information, see [Creating Consolidated Notifications](/en/vista/vista/system-tools/work-flow/about-automated-notifications/creating-consolidated-notifications#ID-0004d77c--en__ID-0004d77c).

## Line

This field is only enabled when the Consolidated
 Notifications box is checked.
The information in this field displays for each record returned by the Notifier Query. Use the [WF Notifier Email Parameters ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-email-parameters) form to add parameters to this field.
Refer to the standard AP Unapproved
 Detail Notifier Job for an example on using this field.
Diagram of consolidated notifications
The diagram below outlines the basic structure
 of a consolidated notification. The Header and Footer each
 display once, and the Line field displays for each record
 returned by the Notifier Query.

##  Footer

 This field is only enabled when the
 Consolidated
 Notifications box is checked.
The text in this field will display once at the bottom of each email and can be up to 8,000 characters long.
 Click [here](/en/vista/vista/system-tools/work-flow/about-automated-notifications/creating-consolidated-notifications) for information on creating consolidated notifications.
Diagram of consolidated notifications
The diagram below outlines the basic structure
 of a consolidated notification. The Header and Footer each
 display once, and the Line field displays for each record
 returned by the Notifier Query.

##  Consolidated Notifications

There are two kinds of notifications:

- Standard - When you create a
 standard Notifier job, the system sends an email for every record returned by the
 query.

- Consolidated - When you consolidate
 notifications, the system sends a single notification with multiple data records.
 This can reduce the emails generated by the system. The records are consolidated
 using the groupings set up using the Consolidation Groups tab on the WF Notifier Job
 Manager form.

When the Consolidated Notifications box is
 checked, you are creating a consolidated email. The function of this box changes depending
 on the option selected in the Format field.
 See [Creating Consolidated Notifications](/en/vista/vista/system-tools/work-flow/about-automated-notifications/creating-consolidated-notifications) for more
 information.

### Rich Text

When sending a rich text email notification
 (Rich
 Text is selected in the Format field), this box is always
 disabled and is set using the Pivot Table box on the WF Notification
 Table Layout form.
To change the selection in this field,
 click on the Table button to open the [WF Notifier Table
 Layout](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-table-layout).

### Plain Text

This box is enabled when Plain is
 selected in the Format box.
Check this checkbox to send consolidated
 notifications. This will enable the Line and Footer
 fields on the Email tab.
If you do not check this box, the system
 sends a notification for each record returned by the associated query.

## Input Value

Enter a specific value for the specified parameter.
For example if the SQL query selected in the
 Query field on the Info tab of this form has a local variable named @days
 in the SQL query, enter the number of days in this field to set the local variable in that
 SQL query. All records that meet the criteria based on this value will be selected.

## Email Format

 Use this field to create plain or rich text emails.
A text formatting toolbar will display about
 the Body section of the email if you select Rich Text, which allows you to format the
 text of the email.
