---
title: "Creating Inquiries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/inquiries--messages/creating-inquiries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/inquiries--messages/creating-inquiries"
---

# Creating Inquiries

An inquiry is two or more queries that are linked together. Inquiries allow you to drill-through one query to another query on a Work Center.
For example, if you have a query that displays a list of purchase orders and a query that displays detailed information about PO items, you can link these two queries together so that from a Work Center you can double click on a PO and see detailed information about the PO items.
Follow the steps below to create two basic queries, link them together to create an inquiry, and then add the inquiry to a Work Center.
The following steps use the example of creating two
 PO queries, linking them together to create an inquiry, and adding them to the PM
 Work Center.
Step 1: Create a query that displays PO item information.
In this step you will create a query that displays PO item information and includes two parameters. Later you will use these parameters to link the PO and PO item queries together.

1. Open the [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form) form.

1. Open the Info tab and click the New Record icon to create a new query.

1. Enter a name for the new query in the Query Name field - for example, InquiryTest_Detail.

1. Select View in the Type drop down. This field
 allows you to create queries based on tables or views.

1. Select the Assignable in Work Center checkbox.

1. Enter POIT in the Query Text field. This is the table that includes the PO general information.

1. Click the Update Columns button. The columns in the POIT table will populate on the Columns tab.

1. Optional: Use the Columns tab to select which columns will display in the Work Center when the query is launched.

1. Open the Parameters tab
 and create the following two records. These are the two parameters that you are
 going to link to the query that displays the PO information. This will define
 the relationship between the two queries. Once you select a Column
 Name, the system will populate most of the remaining rows as you
 TAB through the fields. Column Name
Parameter
 Name
Comparison
Default Type
Value
Operator

POCo
@POCo
=
5-Active Company
%C
AND

PO
@PO
=
0-Fixed Value

AND

1. Save the query.

Step 2: Create a query that displays PO information.
In this step you will create a query that displays PO information, and then you will link it to the PO item query that you just created using the parameters on that query.

1. Open the VA Inquiries form again.

1. Open the Info tab and click the New Record icon to create another query.

1. Enter a name for the new query in the Query Name field - for example "InquiryTest".

1. Select View in the Type drop down. This field
 allows you to create queries based on tables or views.

1. Select the Assignable in Work Center checkbox.

1. Enter POHD in the Query Text field. This is the table that includes the PO general information.

1. Click the Update Columns button. The columns in the POHD table will populate on the Columns tab.

1. Optional: Use the Columns tab to select which columns will
 display in the Work Center when the query is launched.

1. Open the Parameters tab
 and create the following record. Once you select a Column
 Name, the system will populate most of the remaining rows as you
 TAB through the fields.Column Name
Parameter
 Name
Comparison
Default Type
Value
Operator

POCo
@POCo
=
5-Active Company
%C
AND

1. Open the Links tab. This is where you link the queries together.

1. Press F4
 in the Related Query field and select the query you made in Step 1 -
 for example "InquiryTest_Detail".

1. Check the Default
 Drill-Through box. This means that when you double click on a
 PO, you will automatically launch the query that displays the PO items.

1. Double click in the Display Sequence field. This will launch the [VA Inquiry Links](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-links-form) form.

1. Open the Parameters tab on the VA Inquiry Links form. There should already be two records in this grid. These are the two parameters that you set up on the "InquiryTest_Detail" query.

1. Link the parameters in the "InquiryTest_Detail" query to the matching rows in the "InquiryTest" query. This defines how the two queries relate.

- Press F4 in the Matching Column field next to the @POCo record and select POCo from the list that appears.

- Press F4 in the Matching Column field next to the @PO record and select PO from the list that appears.

1. Save the query.

Step 3: Give yourself access to both of the queries.
Once you have created the queries, you have to give yourself access to them before you can add them to a Work Center.

1. Open the [VA Inquiry Security](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form) form.

1. Press F4
 in the User field and select yourself from the list of users that
 displays.

1. Click the Refresh button and a list of queries populates in the form.

1. Locate the two queries
 that you just created and select 0-Allowed in the Access field.

1. Click the Apply button when complete and then close the form.

Step 4: Add the queries to a Work Center
You can add an inquiry to any kind of Work Center: Dashboard, PM, or SM Work Centers. In this example, you will add the inquiry to a PM Work Center.

1. Open a PM Work Center. If you do not have a PM Work Center, you can add one to your application window using the [Work Centers](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-work-centers-form) form.

1. Add the query to the menu. Right-click in the menu where you want to add the inquiry and select Add Inquiry from the menu that appears. This will open the Inquiry Settings form.

1. Select the "InquiryTest" query in the Base Inquiry field.

1. Enter the name that you
 want to display in the PM Work Center menu in the Name field.

1. Click the OK
 button. This will add the inquiry to the PM Work Center menu.

1. In the PM Work Center,
 click on the inquiry that you just added. All POs in the current company will
 display in the grid.Note: If the inquiry doesn't display any
 information, you may have to close and then reopen the PM Work
 Center.

1. Double-click on a PO in the list to launch the link query, which will display the items on the selected PO. You are able to do this because you set up "InquiryTest_Detail" as the default drill-through of "InquiryTest".

1. You can navigate through the related queries using the two icons above the grid. These icons appear only when the query in the grid is related to other queries. - Select a record and click this icon to drill down into the related query.
 - Click this button to move back to the related query - for example move from the PO items query back to the query that displays a list of all purchase orders.
You can also click the drop down arrow next to these icons and select the query that you would like to navigate to - for example if you have multiple queries related to a single query.

For more information, see [About Relationships Between Queries in Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-relationships-between-queries-in-inquiries).
