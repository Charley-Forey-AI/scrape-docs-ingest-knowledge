---
title: "Adding a Query to a Tab | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/inquiries--messages/adding-a-query-to-a-tab"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/inquiries--messages/adding-a-query-to-a-tab"
---

# Adding a Query to a Tab

You can add a tab to a form and then add a query to that tab.
Things to know before you start

- The form must have a corresponding form query. Form queries allow you to link a tab to a query, and currently every form in the application does not have a corresponding form query. To see a list of available form queries, open the Grid tab on the [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form) form and sort the queries using the Query Type column.

- You cannot drill-through a query that has been added
 to a tab. The Links tab on the VA Inquiries form allows you to relate
 queries so that you can drill-through from one query to another. This
 functionality has not been implemented on queries that are on forms. See
 [Creating Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/creating-inquiries) for more information on
 relating queries in inquiries.

- You can also add a custom table to a tab on a form. [More](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/link-related-tabs-to-ud-tables)

Click on a step below for more information. These steps outline an example of adding of adding a query to a tab: creating a query that displays a list of RFIs. This query is then added to the PM Projects form so that the query only displays the RFIs associated with the project selected in the form.
Step 1: Create a query
Use the [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form) form to create the View or SQL type query that you want to display on the new tab. You can skip this step if the query already exists. This example uses a View type query.
Click [here](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries) for information on creating queries.

1. Open VA Inquiries.

1. Create a new query and name it using the Query Name field.

1. Select View in the Type drop down.

1. Enter PMRI in the Query Text field and then
 click the Update Columns button. PMRI
 contains general information about RFI.

1. Open the Parameters tab and create the following item: Column Name
Parameter Name
Comparison
Default Type

Project
@Project
=
4-Form Input Value

The 4-Form Input Value option means that the query will be filtered by the project that displays in the form.

1. Do not use the Links tab. This tab is used to link queries so that you can drill-through from one query to another within an inquiry. Click [here](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries) for more information about creating inquiries.

1. Save your changes.

Step 2: Link the query to the standard form query
In this step you link the query that you just created to the form query that represents the form. This allows you to add the query to the form later in this process.

1. Open the VA Inquiries form.

1. Locate the form query that represents the form - for example select PMProjects if you want to add a query to a tab on the PM Projects form. Form queries are standard queries that allow you to add a query to a tab on a form. You can only add a query to a form if it has a corresponding form query.
To see a list of form queries, open the Gird tab on the VA Inquiries form, click the Query Type column heading to sort the queries in the grid, and then scan the list of form queries.

1. Open the Links tab.

1. Select the query that you just created in the Related Query field. This is the query that will display on a tab in the form.

1. Double click on the
 Related Query field to open the [VA Inquiry Links](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-links-form) form.

1. Open the Parameters tab. This tab displays all of the parameters associated with the query.

1. Use the Matching
 Column field to match the parameter to a field in the form. For
 example press F4 in the Matching
 Column field and select Project from the list.

1. Save your changes.

Step 3: Add a tab to the form
You can add a tab to a form only if you are set up as a form administrator. This is set up using the Form Administrator box on the Info tab of the [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form) form.

1. Open the form that you are going to add the tab to. For example, open the PM Projects form.

1. Make sure that you are on the Grid or Info tab of the form.

1. Select Tools > Form
 Properties from the toolbar at the top of the form. This will open the [Form Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-form-properties-form) form.

1. Open the Tab Pages tab.

1. Click the Add
 button.

1. Enter the name of the new tab in the Tab Title field on the form that displays and then click OK.

Step 4: Add the linked query to the tab

1. On the Tab Pages tab of the Form Properties form, select the tab that you just created and then click the Edit button. This will open the [VA Custom Form Tabs ](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-tabs-form) form.

1. Select 3-Query in the Control Type drop down on the Info tab.

1. Press F4
 in the Query Name field and select the query that you would like to
 add to the tab. If the query does not display, it is not related to the form
 query that corresponds to the form. Return to Step 2: Link the query to the
 standard form query.

1. Save your changes.

1. Open the new tab on the
 form and verify that the query is displaying correctly.
