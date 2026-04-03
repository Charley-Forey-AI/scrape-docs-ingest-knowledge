---
title: "Using a User-Defined Field in a Query | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/queries-and-user-defined-fields/using-a-user-defined-field-in-a-query"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/queries-and-user-defined-fields/using-a-user-defined-field-in-a-query"
---

# Using a User-Defined Field in a Query

Find examples of a user-defined field in a
 query.

1. In order to use a user-defined field in a query, first you have to determine the user-defined sequence of the desired field. To do this, you need to examine the PA.UDEFH file (Info-Link table PA_USER_FIELDS_SETUP_U). The screen below shows this file in Access. Look at the field in the employee file (Entry_Type = "EMP") and company code SEG. The field you are interested in is the CPR Class, which is a date. Note that the User_Def_Sequence is 000084; you will need this value to use this user-defined field.

1. Next, take a look at the table PR.UDEMP (long Info-Link name PR_EMP_USER_FIELDS_DET). Note that the rows with USER_DEF_SEQUENCE = 000084 contain the CPR_Class_Date for each employee. Because this is a date, the data is in the Date_Field (instead of the Alpha_Field, or Amount_Field).

1.  In the screen shot below, an Access query called CPR_Class_Date has been created. This query is reading all rows from the PR_EMP_USER_FIELDS_DET with User_Defined_Sequence = 000084. This query creates a simple way to access the CPR_Class_Date for each employee.

1. This screen shows this same query executed.
