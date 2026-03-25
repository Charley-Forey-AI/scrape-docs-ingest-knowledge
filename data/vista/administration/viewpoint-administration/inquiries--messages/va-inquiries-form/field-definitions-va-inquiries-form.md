---
title: "Field Definitions: VA Inquiries Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form/field-definitions-va-inquiries-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form/field-definitions-va-inquiries-form"
---

# Field Definitions: VA Inquiries Form

The following is a list of field descriptions for the VA
 Inquiries form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Active

 Check this box if users should be able to add the inquiry to the selected Work Center.
 Click [here](/en/vista/vista/system-tools/work-centers/about-work-center-setup) for information about setting up Work Centers.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

- [About Work Center Setup](/en/vista/vista/system-tools/work-centers/about-work-center-setup)

## Template Name

Press F4 to select the Work Center template
 that should be associated with the inquiry. For example if users should be able to add the
 inquiry to the PM Work Center, select PM in the menu that displays.
Click [here](/en/vista/vista/system-tools/work-centers/about-work-center-setup) for information about setting up Work Centers.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

- [About Work Center Setup](/en/vista/vista/system-tools/work-centers/about-work-center-setup)

## Column Name

 This field defaults the column names
 specified in the Query Text field on the Info tab.
 If you enter a new column name here, you must also reference it in the query text.

## Datatype

Datatype field on the VA Inquiries form, Columns tab
Use this field to set the data type of the
 information in the column. Press F4 to select a data type from a list.
For example, select bDollar if you would like the value in the column to display as a dollar value.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Default Order

Default Order field on the VA Inquiries form, Columns tab
Use this field to set the default order of the column in the Work Center.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

- [About Work Center Setup](/en/vista/vista/system-tools/work-centers/about-work-center-setup)

## Exclude from Query

 Select this checkbox to prevent the column
 displaying in the Work Center.

When the Exclude from Query checkbox is selected, the column does not display in the Work Center and users do not have the option to add it. You map opt to check this box for columns containing confidential information.
This is different than if the Visible On Grid checkbox is not
 selected. In this case, the column will not display in the Work Center by default but
 individual users can choose to make it visible.

## Visible On Grid

Visible On Grid checkbox on the VA Inquiries form, Columns tab
Select this checkbox if the column should show up on the Work Center.

When the Visible On Grid checkbox is not selected, the column will not display in the Work Center by default but individual users can choose to make it visible.
When the Exclude from Query checkbox is selected, the column does not display in the Work Center and users do not have the option to add it. You map opt to check this box for columns containing confidential information.

## API: Published

Select this checkbox to make this inquiry available to the Inquiry API. When the checkbox is selected, the system will display the last date this inquiry was executed via the API, as well as how many times it has been executed.
Clear the checkbox to make this inquiry unavailable to the Inquiry API.
Note: Be very careful about editing any inquiries that have this checkbox selected. They have already been made available to the API, and any changes could break existing API integrations.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Assignable in Work Center

Assignable in Work Center checkbox on the VA Inquiries form
This checkbox is available only if the
 Type
 field is set to SQL or View.
This checkbox defaults to unselected for all drill-through queries. Generally, drill-through queries expect specific parameter values to exist. Therefore, most drill-through queries make sense only if they are being drilled through from a base query and are not themselves the base query.
Select this checkbox to make this query
 available to be assigned to a Work Center from the Base Inquiry field of the Inquiry
 Settings form.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

- [About Work Center Setup](/en/vista/vista/system-tools/work-centers/about-work-center-setup)

## Description

Description field on the VA Inquiries form
Enter the description of this query, up to 255 characters. Typically, the description should describe what function the query performs.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Query Name

Query Name field on the VA Inquiries form
Enter the query name or press F4 to select
 from a list of all available queries.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Query Text

Query Text field on the VA Inquiries form
The function of this field varies depending on if you are creating a View or SQL query.
If you are creating a View query, enter the name of a view or table and then click the Update Columns button. This will populate the Columns tab with the columns in the selected table or view.
If you are creating a SQL query, enter the text of the query, making sure to include the Select and From Where clauses. Enter the query text manually or copy and paste it from an existing query. Space is virtually unlimited, with a maximum allowance of 8k.
Note: The Select clause identifies the information returned by the query. The From Where clause identifies the table where information is being pulled from, the joins for associating multiple tables (if applicable), and how the information is filtered.

## Title

Title field on the VA Inquiries form
Enter the title of the inquiry. The title can be up to 255 characters long.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Type

Type field on the VA Inquiries form
 Select the type of inquiry that you are creating:

- View - Select this type and then
 enter either a table or view name in the Query Text field.

- SQL - Select this type and then
 enter a full SQL statement in the Query Text field.

- Form - These are system queries
 that allow you to add a query to a custom tab on a form. You cannot create new form
 queries. Click [here](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/adding-a-query-to-a-tab) for information on adding a query to a tab on a form.

- Dispatch - This type of query (standard or custom) is used with the Service Management Dispatch Board to filter work orders based on specific criteria. For example, the "SMDispatchWorkOrdersOverdue" query displays work orders having one or more scopes where the Due Date has passed and no trips have been created.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Viewpoint Standard

Viewpoint Standard checkbox on the VA Inquiries form
This checkbox is selected automatically if the inquiry is a standard viewpoint inquiry.
This field is always disabled.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Default Drill-Through

Select this checkbox if double clicking on a record in the inquiry should drill through into this query - for example, if you have a query that displays purchase order information and you want to double click on a PO and view the PO items.
When a query is not the default drill-through, you must select a record in the grid, click the drop down arrow next to the Drill-Through () icon, and then select the query that you would like to drill-through into.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Display Seq

Display Sequence field on the VA Inquiries form, Links tab
When using a query in a Work Center, related queries are opened using a drop down menu. Use this field to define the order that the queries will display in that drop down.
You can leave this field blank and click the
 Save
 icon, and the system will automatically assign the query the next available sequence
 number.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Related Query

Related Query field on the VA Inquiries form, Links tab
Use this field to select the query that you
 would like to relate. Press F4 to select the query from a list.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Notes

Use this field to enter notes about the inquiry.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

## Comparison

The Comparison and Operator fields
 are used to define the relationship between the parameter and the value.

The Comparison field has the following
 options:
SymbolDescription
=Equal
<>Does not
 equal
>Greater
 than
>=Greater then
 or equal to
<Less
 than
<=Less than or
 equal to

Note: The Comparison and Operator fields
 do not support parenthetical grouping and advanced filtering. If you need to create this
 relationship, you should create a SQL query. For more information on types of queries, see [Type](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form/field-definitions-va-inquiries-form#ID-00048e93--en).

## Datatype

Datatype field on the VA Inquiries form, Parameters tab
Enter the parameter’s datatype (data format).

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Default Order

Use this field to define the default order of the parameters. By default this field will populate with the next available number when you create a new parameter.

## Default Type

Default Type field on the VA Inquiries form, Parameters tab
Select a default type if you want to restrict the parameter to a current system setting or a fixed value.
If you are creating a query that you are going
 to put on a tab on a form, select the 4-Form Input Value option to pass a
 parameter from a form to the query. For example, if you want to add a query that displays a
 list of change orders to the PM Projects form, select the 4-Form Input
 Value option to pass the current project to the query as a parameter.
For more information about adding a query to a tab on a form, see [Adding a Query to a Tab](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/adding-a-query-to-a-tab).

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Description

Description field on the VA Inquiries form, Parameters tab
 Enter a description of the parameter, up to 255 characters.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Input Length

Input Length field on the VA Inquiries form, Parameters tab
Enter the maximum number of characters allowed for entry. For example, if the field should allow up to 30 characters, enter 30 as the input length.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Input Type

Input Type field on the VA Inquiries form, Parameters tab
Enter the field type of this parameter. There are six input types that can be used:

- 0 - String

- 1 - Numeric

- 2- Date (mm/dd/yy)

- 3 - Month (mm/yy)

- 4 - Time (hh:mm)

- 5 - Multi-part

- 6 - String to Numeric

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Lookup

Enter the lookup you want assigned to the
 parameter. Press F4 for a list of valid lookups (standard and custom).

## Operator

The Comparison and Operator fields
 are used to define the relationship between the parameter and the value.
This field appears only
 when you are creating/modifying a View query. For more information on types of queries, see [Type](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form/field-definitions-va-inquiries-form#ID-00048e93--en).

The Operator field has the following
 options:

- AND

- OR

The value in this field is ignored if this is the last record in the Parameters grid.
Note: The Comparison and Operator
 fields do not support parenthetical grouping and advanced filtering. If you need to create
 this relationship, you should create a SQL query. For more information on types of queries, see [Type](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form/field-definitions-va-inquiries-form#ID-00048e93--en).

## Parameter Name

Parameter Name field on the VA Inquiries form, Parameters tab
Enter a parameter for this query, up to 50 characters.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Precision

Precision field on the VA Inquiries form, Parameters tab
 The field is enabled when a Datatype is not
 specified for the parameter and when you select 1 - Numeric from the Input Type
 field.
Specify the total number of significant digits that can be stored in this input. The available options are:

- 0-TinyInt - Input must be between 0 and 255.

- 1-SmallInt - Input must be between -32,768 and 32,767.

- 2-Int - Input must be between -2,147,483,648 and 2,147,483,647.

- 3-Numeric - Use for decimals. Allows up to 38 digits.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Value

Value field on the VA Inquiries form, Parameters tab
Enter a value for restricting the parameter.

- If you selected an option other than Fixed
 Value in the Default Type field, the Value
 field automatically defaults the correct value.

- If you selected the Fixed
 Value option in the Default Type field, enter a value
 in the Value field.

If you selected the Fixed Value option in the
 Default Type field, but do not enter a value in the Value field . . .

- and the underlying datatype that the parameter will
 be applied to is an integer, the system will default Value to
 zero (0).

- and the underlying datatype that the parameter will
 be applied to is a date, the system will default Value to the current date.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

## Visible

Visible checkbox on the VA Inquiries form, Parameters tab
Select this checkbox if the parameter should display in the Inquiries Settings window on the Dashboard Work Center.

Related information

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)
