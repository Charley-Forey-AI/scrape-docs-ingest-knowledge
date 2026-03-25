---
title: "WF Notifier Queries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries"
---

# WF Notifier Queries

Use the WF Notifier Queries form to create and maintain queries for Notifier jobs you create in WF Notifier Job Manager.
The system uses queries to request information from the Vista SQL Server database. You must have a good understanding of how to create SQL queries in order to use this form. This help topic provides a basic overview of query construction, but does not go into detail. If you do not know how to create a database query, use one of the standard queries provided with the system. Standard queries are those queries with the Viewpoint Standard box checked.
Note: Notifier queries are run from an administrative account that has access to all Viewpoint data. This means that a query may return data that a given user has not been granted access to via the datatype security built into the Vista product. Users of Notifier must be cautious when choosing who receives notifications from Notifier. Make sure the users in the To, CC, and BCC sections of a Notifier Email have sufficient authority within your company to view the sent data.

Important: If you are using datatype security, you cannot use views in Notifier Queries; you can only use tables.

[Modify a Standard Notification Query](/en/vista/vista/system-tools/work-flow/about-automated-notifications/using-a-standard-notifier-query-and-job/modify-a-standard-notification-query)
[About Event-Driven Queries](/en/vista/vista/system-tools/work-flow/about-automated-notifications/about-event-driven-queries)
[Creating Notifier Queries](/en/vista/vista/system-tools/work-flow/about-automated-notifications/creating-notifier-queries)
[Restricting Notifier Queries](/en/vista/vista/system-tools/work-flow/about-automated-notifications/restricting-notifier-queries)
[Copying a Notifier Query](/en/vista/vista/system-tools/work-flow/about-automated-notifications/using-a-standard-notifier-query-and-job/copying-a-notifier-query)
[WF Notifier Job Manager](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager)

Related information

- [About Automated Notifications](/en/vista/vista/system-tools/work-flow/about-automated-notifications)
