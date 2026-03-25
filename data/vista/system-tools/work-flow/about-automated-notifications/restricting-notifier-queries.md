---
title: "Restricting Notifier Queries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/about-automated-notifications/restricting-notifier-queries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/about-automated-notifications/restricting-notifier-queries"
---

# Restricting Notifier Queries

Use the Query Parameters tab in [WF Notifier Queries ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries) to define parameters for restricting records that queries return. Enter parameters on this tab when multiple jobs use the same query, but the restrictions change. Parameters act like placeholders. When creating a Notifier Job in WF Notifier Job Manager, you can assign specific parameter values for the query to return.
For example, if you want to pull a company’s name and address from the HQ Company Parameters (HQCO) table, you might create the following query:
Select Clause: Select Name as [Name], Address as [Address], City as [City], Zip as [Zip]
Where Clause: From HQCO Where HQCO =@company
In the example, the WHERE contains the @company parameter. When using this query, the system replaces the parameter with the input value on the Parameters tab in WF Notifier Job Manager. Even though the @company parameter is specified in the query, you must enter it on the Query Parameters tab. This enables the system to recognize the parameter when you set up a Notifier job in WF Notifier Job Manager.
To enter a parameter on the Query Parameters tab,
 enter the query in the Param field and enter an optional
 description for the query in the Description field. Save the record as
 normal. The parameter now displays on the Parameters tab for any Notifier Job
 referencing this query.
For more information, see [WF Notifier Queries](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries) or [WF Notifier Job Manager](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager).

Related information

- [Creating Notifier Queries](/en/vista/vista/system-tools/work-flow/about-automated-notifications/creating-notifier-queries)

- [Copying a Notifier Query](/en/vista/vista/system-tools/work-flow/about-automated-notifications/using-a-standard-notifier-query-and-job/copying-a-notifier-query)
