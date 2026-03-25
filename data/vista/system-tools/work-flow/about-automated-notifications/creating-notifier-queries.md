---
title: "Creating Notifier Queries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/about-automated-notifications/creating-notifier-queries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/about-automated-notifications/creating-notifier-queries"
---

# Creating Notifier Queries

Follow the steps below to create a new notification query from scratch.
Instead of creating a new query, you can also:

- Use a standard Notifier Queries included in the application

- Copy a standard Notifier Query and [then modify the copy](/en/vista/vista/system-tools/work-flow/about-automated-notifications/using-a-standard-notifier-query-and-job/copying-a-notifier-query)

- Use a standard inquiry in VA Inquiries

- Copy a standard inquiry in [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

- Create a new inquiry from scratch using [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

Tip: When creating a query, you can select Options > Viewpoint Views to open the WF Notifier Viewpoint Tables form. This form lists all views associated with each module in the system. [More ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-viewpoint-tables)
To create a new Notifier query:

1. Open the [WF Notifier Queries ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries) form.

1. Enter a name for the query in the Query Name field.

1. Enter a title for the query in the Title field.

1. Check the Event Query box if this is an event-driven query.[ More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/about-event-driven-queries)

1. Enter a description of the query in the Description field.

1. Enter the SELECT clause in the Select Clause field. [More - Including an example](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries/field-definitions-wf-notifier-queries-form#ID-0004dd72--en)

1. Enter the FROM and WHERE clause in the From Where Clause field. [More - Including an example](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries/field-definitions-wf-notifier-queries-form#ID-0004dd83--en)

1. Click Test Query to have the system search the query for errors.

1. Add any local variables that you included in the SQL query to the Query Parameters tab. When the Notifier Query is associated with a Notifier Job, you will be able to define these local variables using the Parameters tab on the WF Notifier Job Manager form. [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/restricting-notifier-queries)

1. Save the query. The Email Fields tab displays all of the bracketed fields from the select clause. Note: The fields on this tab specify the data contained in email messages created by the Notifier job. These fields must be unique. If there are multiple occurrences of these fields, edit them in the Select Clause field to make each one unique. Make sure to edit only those fields in brackets. The system updates the Email Fields section once you save the record.

1. If you are creating an event-driven query, check the Is Key Field box on the Email Fields tab for each key field. For more information, see [Event-Driven Queries](/en/vista/vista/system-tools/work-flow/about-automated-notifications/about-event-driven-queries).

1. Once you create the query, use the [WF Notifier Job Manager](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager) form to associate it with a Notifier Job.

Related information

- [About Automated Notifications](/en/vista/vista/system-tools/work-flow/about-automated-notifications)
