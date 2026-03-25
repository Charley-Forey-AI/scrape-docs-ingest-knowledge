---
title: "About Relationships Between Queries in Inquiries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-relationships-between-queries-in-inquiries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-relationships-between-queries-in-inquiries"
---

# About Relationships Between Queries in Inquiries

An inquiry is two or more queries that are linked together. Inquiries allow you to drill-through one query to another query on a Work Center.
For example if you have a query that displays a list of purchase orders and a query that displays detailed information about PO items, you can link these two queries together so that from a Work Center you can double click on a PO and see detailed information about the PO items.
Inquiries allow you to create levels of relationships between the queries. Below are some examples of the relationships that you can create.

- Parent  > Children - A single parent query can be related to several child queries. For
 example a query that displays a list of projects can be linked to several different
 queries that display POs, change orders, and subcontracts. This would allow you to
 bring up a list of projects in a Work Center and then drill-through into a project
 to see the POs, change orders, and subcontracts on that project. In this example the
 parent query is the query that displays the project information, and the child
 queries are the queries that display the POs, change orders, and subcontracts.

- Parent  > Children > Grandchildren - You can link child queries to more queries so that there are two
 levels of drill-through relationships. In the example above, you could link the
 child queries that display the POs, change orders, and subcontracts to grandchildren
 queries that displays PO items, change order items, and subcontract items. This
 would allow you to bring up a list of projects in a Work Center, drill-through into
 a project to see the POs, change orders, and subcontracts on that project, and then
 drill through a PO, change order, or subcontract to see the items.

There is no limit on the number of relationship levels that you can create, so you can even create Parent> Children> Grandchildren> Great Grandchildren inquiries if necessary.
 See [Creating Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/creating-inquiries) for information on how to create an inquiry.
