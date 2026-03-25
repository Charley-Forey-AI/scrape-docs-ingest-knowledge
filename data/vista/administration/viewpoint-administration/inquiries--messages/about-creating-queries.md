---
title: "About Creating Queries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries"
---

# About Creating Queries

You can create and maintain queries, which you can add to a Dashboard, PM, or SM Work Center.
You can create and maintain queries that allow you to view specific information from Dashboard, Project Management, Service Management, and/or Accounting Work Centers.
Queries can also be linked together to create inquiries. Inquiries are two or more queries that are linked together so that users can drill-through from one query to another. See [Creating Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/creating-inquiries) for information on creating inquiries.
You can add queries and inquiries to Work Centers so that they display specific information. For example, you can write your own SQL SELECT statement and then add that query to a Work Center. For more information about adding queries to a Work Center, see [PM Work Center Overview](/en/vista/vista/system-tools/work-centers/about-the-project-management-work-center).

## Related Items and Attachments Functionality

Your custom SQL query must be configured in a specific way to work with the Related Items panel on the SM and PM Work Center. For example, if you add the inquiry to an SM Work Center, you can select an item in the inquiry, and the related items and attachments associated with that item will display in the Related Items panel in the work center.
To configure your SQL inquiry, you will need to add the following three columns to your inquiry:

- FormName

- KeyID

- UniqueAttchID.

 The FormName field is the name of the form associated with the record that the inquiry is displaying (for example PMDailyLog if you're displaying daily logs). These three columns do not have to be visible.

Click the links below for more information about creating queries.
[About Choosing the Type of Query to Create](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries/about-choosing-the-type-of-query-to-create#concept-3702--en__concept-3702)
[Create a View Query](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries/create-a-view-query#task-6069--en__task-6069)
[Create an SQL Query](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries/create-an-sql-query#task-2420--en__task-2420)
[Create a Dispatch Query](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries/create-a-dispatch-query#task-7359--en__task-7359)
[Adding a Query to a Tab](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/adding-a-query-to-a-tab)
