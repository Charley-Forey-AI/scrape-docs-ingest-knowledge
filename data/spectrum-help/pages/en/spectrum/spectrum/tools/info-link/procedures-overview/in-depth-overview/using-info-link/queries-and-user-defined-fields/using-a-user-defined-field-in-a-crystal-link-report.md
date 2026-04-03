---
title: "Using a User-Defined Field in a Crystal-Link Report | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/queries-and-user-defined-fields/using-a-user-defined-field-in-a-crystal-link-report"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/queries-and-user-defined-fields/using-a-user-defined-field-in-a-crystal-link-report"
---

# Using a User-Defined Field in a Crystal-Link Report

Find examples of a user-defined fields in a crystal-link
 report.

1. This example shows a Crystal-Link report using the employee code and employee name from the employee master table and the CPR_Class_Date from the PR_EMP_USER_FIELDS_DET table. Here is what the Crystal Visual Linking Expert looks like.

1. Here is the Report Record selection formula, selecting only fields where the USER_DEFINED_SEQUENCE is 000084.

1. Here is the screen shot of the report. Combining Multiple User-Defined Fields on One Query
Combining multiple user-defined fields on one query is fairly easy in Access, but not in Crystal-Link. To do this in Crystal-Link, it is simpler to create tables from the Access queries and then do the Crystal reports on these Access tables.
