---
title: "Modify a Standard Notification Query | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/about-automated-notifications/using-a-standard-notifier-query-and-job/modify-a-standard-notification-query"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/about-automated-notifications/using-a-standard-notifier-query-and-job/modify-a-standard-notification-query"
---

# Modify a Standard Notification Query

The
 steps below are an example of how you can modify a standard Notification Query. In this
 example, you will copy a standard HR module Notifier Query and then add a condition to the
 WHERE clause so that only active employees are included in the query.

1. Open the [WF Notifier Queries](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries) form.

1. Open the
 HRRSExpireDate
 query in the form. This query displays a list of skills that are near or past their expiration date. The expiration of a skill is set using the
 Expire Date
 field on the [HR Resource Skills](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/talent-and-performance/about-the-hr-resource-skills-form) form. Only skills that have an expiration date will be included in this query.

1. Use the File > Copy
 Query option in the menu at the top of the form to copy the query. [More](/en/vista/vista/system-tools/work-flow/about-automated-notifications/using-a-standard-notifier-query-and-job/copying-a-notifier-query)

1. Open the copied query in the
 WF Notifier Queries form.

1. Make the following addition to the text in the
 FROM WHERE Clause
 field (the addition is in bold): FROM bHRRM d (Nolock)
JOIN bHRRS m (Nolock) on d.HRCo =m.HRCo and d.HRRef = m.HRRef
JOIN bHRCM c (Nolock) on m.HRCo = c.HRCo and m.Code = c.Code and c.Type='S'
WHERE m.ExpireDate < (getdate() + @days)
 and d.ActiveYN='Y'
ActiveYN
The ActiveYN column in the bHRRM table
 contains the value from the Active PR Employee field on the Payroll
 Info tab of the [HR Resources ](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form) form. Generally, this is a good field to
 use to filter the records by active employees.
The text that you included in the WHERE clause used the alias for the bHRRM which was assigned during the FROM clause ("FROM bHRRM d"), that is why you added the text "and d.ActiveYN='Y'" instead of "and bHRRM.ActiveYN='Y'".
Note: Because the bHRRM table is already included in the FROM
 clause, you did not have to add a JOIN to use the ActiveYN column. If the bHRRM
 table wasn't include in the FROM statement, you would have had to add a JOIN to
 the FROM clause before being able to use the ActiveYN column. @days
@days is a local variable that is defined using the Parameters tab on the [WF Notifier Job Manager](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager) form when the query is associated with a Notifier Job. This will be covered in a later step.

1. Save the query.

1. Open the Query Parameters tab. The @days local variable on the SQL query will display as an item on this tab. When you associate the query with a Notification Job, you will be able to define this parameter using the Parameter tab on the WF Notifier Job Manager form.

1. Click the
 Test Query
 button to test the query. A success message will display if the SQL statement is written correctly.

1. Add the new query to an existing Notifier Job, or create a new Notifier Job using the [WF Notifier Job Manager](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager) form. A Notifier Query is associated with a
 Notifier Job using the Query field on the Info tab of WF
 Notifier Job Manager. You can either change the query selected in this field on an
 existing Notifier Job, or you can create a new Notifier Job.Click [here](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager/field-definitions-wf-notifier-job-manager-form#ID-0004de06--en) for more information about the Query
 field.

1. Use the Info tab on the WF
 Notifier Job Manager form to set up how often the notifications will be sent. For
 example, if these notifications should only be sent out once a week, you can use the
 Info tab to set up the job to run on the weekend after business hours.

1. Use the Email tab on the WF
 Notifier Job Manager form to define who should receive the notifications and what the
 notifications should look like.

1. Use the Parameters tab on
 the WF Notifier Job Manager form to define the local variables on the SQL query. In
 this example there is only the @days local variable. Enter a '7'
 in the Input
 Value column if skills within 7 days of expiring, or past the
 expiration date should be included in the query.

1. Open the Info tab on the WF
 Notifier Job Manager form and then click the Execute Job button. This will
 execute the new job on the SQL server.

1. Check the Enable
 Task box on the Info tab of the WF Notifier Job Manager form to
 activate the job.

1. The standard Notifier Query has now been modified and associated with a Notifier Job.

Related information

- [About Automated Notifications](/en/vista/vista/system-tools/work-flow/about-automated-notifications)
