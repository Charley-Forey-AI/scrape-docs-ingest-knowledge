---
title: "About Event-Driven Queries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/about-automated-notifications/about-event-driven-queries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/about-automated-notifications/about-event-driven-queries"
---

# About Event-Driven Queries

 Event-driven queries allow you to reduce the number of notifications that are sent
 when a specific event occurs.
When creating queries, you can control when notifications are
 sent using event-driven queries. For example, if you create a query to alert you when a job
 is over budget, you want to receive notification only when a job is over budget, not each
 time the associated notification job is run. By setting up an event-driven query, you can
 specify that notification be sent only when the specific event occurs.
When initially running an event-driven query, the system notes
 all records that meet the notification criteria (for example, a job is over budget) and
 keeps track of them. The next time the query runs, the system compares the results against
 previous notifications and only sends a notification for a new event.
In order to prevent the system from continually sending a
 notification, you need to identify key fields for your query using the Email Fields
 tab.

- Notifier Query - If you are using a notification query to select the records, select
 the Event Query checkbox on the
 Info tab of the WF Notifier Queries form, and then use the Email Fields tab to select
 the key fields.

- Inquiry - If using a VA module inquiry to select the records, use the Notifier Email
 Fields tab on the VA Inquiries form.Note: There is no Event Query checkbox on the VA Inquiries
 form. If there are key fields selected on the Notifier Email Fields tab, the
 system assumes that the query is event driven

Note: If you want to create an event-driven query from a standard query, make a
 copy of the query (VA Inquiries > File > Copy Query), associate the copy with the notification job (Query field, WF Notifier Job Manager form) and
 then make changes to the copy.
As long as a key field remains a constant value and the
 notification criteria is still met, the system will not send an additional notification.
 However, if the key fields change and the notification criteria is met, the system will
 send a notification.
Using the prior example, you could create an event-driven query
 to alert you when a job’s actual costs have exceeded the estimated costs. For this query,
 you might pull information from the JCCo,
 Job, ActualUnits, and ActualCost fields in the JC Cost Projections table
 (JCCostProjection). The system would send a notification when the amount in the Actual Cost column exceeded the Estimated Cost column. In this example, you would
 identify JCCo and Job as the key fields. The following table shows
 when the system would send a notification for this query.
JCCoJobEst CostActual CostSend Notification?
1150,00048,000N
1150,00051,000Y
1150,00052,000N
2150,00050,500Y

In the table above, the key fields (JCCo and Job) remain constant for the first three items. Because the first three
 items represent a single job for a specific company, a notification is only sent once. If
 the actual cost for that company/job combination dipped below the estimated cost and the
 next time the actual cost went above the estimated cost, the system would send another
 notification. The fourth line represents a new company/job combination, so the system sends
 a notification.
When preparing a Notifier job that uses an event-driven query,
 you should perform a test run first in order to record notification settings. When
 performing the test run, it is recommended that you send notification emails to a single
 account, as a consolidated notification, to prevent the system from generating numerous
 emails. In other words, as the system tries to compare data, it will discover multiple
 discrepancies (no previous notifications were run) and send multiple emails.

Related information

- [WF Notifier Queries](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries)

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

- [About Automated Notifications](/en/vista/vista/system-tools/work-flow/about-automated-notifications)
