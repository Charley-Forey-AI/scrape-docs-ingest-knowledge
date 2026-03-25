---
title: "Set up a Notifier Job | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/about-automated-notifications/set-up-a-notifier-job"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/about-automated-notifications/set-up-a-notifier-job"
---

# Set up a Notifier Job

You can set up Notifier jobs that generate automatic email notifications.

Notifier jobs are user-defined tasks that the system performs when certain conditions exist. For example, if you are using the review/approval workflow process for purchase orders and subcontracts, you might need to send a notification to approvers once a purchase order or subcontract is submitted for approval. In this instance, you would create a Notifier job sends an email to assigned reviewers/approvers that lists all purchase orders and subcontracts that are ready for review.You should have a good understanding of how to create Notifier jobs in order to use this form. This help topic provides a basic overview of job construction, but does not go into detail.
Use the F1 help for fields on this form to get additional information.

1. Open the WF Notifier Job Manager.

1. In the Job Name field, enter a unique name for the job that identifies the purpose of the job.Note: Notifier jobs are not company-specific and are shared between all companies.

1. In the Description field, enter a description for the job.

1. From the Query Type drop-down, select the type of query for this job.

- 0-WF Notifier Query

- 1-VA-Inquiry

1. In the Query field, enter the query/inquiry to use for this job or press F4 to select from a list of valid queries/inquiries.

1. Define the job's schedule using the Occurs, Daily Frequency, and Duration parameters. This determines when the job will run and how often.

1. Configure the 'from' address for notifications by selecting Options > Notifier Options. For more information, see [WF Notifier Options](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-options).

1. Use the Email tab to define the email parameters; that is, the email format, recipients, subject line, and what information to include in the email body.Note: You can use the Email Fields or Table buttons to control what information to include in the email body and how it is presented. The fields available are based on the query/inquiry you selected for your job. For more information about email parameters, see [WF Notifier Email Parameters](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-email-parameters) and [WF Notifier Table Layout](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-table-layout).

1. If using consolidated notifications (that is, the Consolidated Notifications checkbox is selected), use the Consolidation Groups tab to define how the notifications will be consolidated. For more information, see [ Consolidated Notifications](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager/field-definitions-wf-notifier-job-manager-form#ID-0004deeb--en).

1. The Parameters tab automatically defaults the parameters applicable to the query/inquiry. For each parameter, use the Input field to specify the applicable value. For example, if the parameter is @Co, enter the applicable company number.

1. Once you complete setting up the job, click Start Job to activate the job.

The system will begin running the job based on the start date and the schedule criteria.
