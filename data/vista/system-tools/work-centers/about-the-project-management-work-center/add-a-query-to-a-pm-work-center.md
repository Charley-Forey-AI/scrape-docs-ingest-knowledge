---
title: "Add a Query to a PM Work Center | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-centers/about-the-project-management-work-center/add-a-query-to-a-pm-work-center"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-centers/about-the-project-management-work-center/add-a-query-to-a-pm-work-center"
---

# Add a Query to a PM Work Center

You can add any query to a PM module Work Center, but only some queries support all of the PM module Work Center functionality.
Follow the steps below to add a query to the PM Work Center and then customize it.

1. Open a PM Work Center.

1. Right click on the folder in the menu tree where the query should be saved and
 select Add Inquiry.The Inquiry Settings form displays.

1. Select the query that you would like to add to the PM Work Center in the
 Base
 Inquiry drop down.Note: A query will only display in this drop-down menu if
 the Assignable in Work Center checkbox is selected in VA
 Inquiries, it is associated with the PM Work Center template on the
 Associations tab in VA Inquiries, and you have security set to access it in
 VA Inquiry Security.

1. In the Name field, enter a name for the query. Entering a unique name in this field allows you to have multiple instances of
 the same query on a single PM Work Center.

1. Using the Parameters tab, customize which items will display in the list.A description of each parameter displays in the Description column, including the expected format of the
 parameter value. For example, if the Hot List should only include PCOs with a
 create date within the last two days, enter %D-2 in the @PCOCreationDateFilter field. Note: When entering parameter values,
 make sure that you do not include the spaces, apostrophes, or <>'s
 that display in the format description. For more information, see [About Parameter Values](/en/vista/vista/system-tools/work-centers/about-the-dashboard-work-center/about-parameter-values).

1. Click OK to save the changes.

The form closes and you are returned to the PM Work
 Center, which is updated with the changes.
