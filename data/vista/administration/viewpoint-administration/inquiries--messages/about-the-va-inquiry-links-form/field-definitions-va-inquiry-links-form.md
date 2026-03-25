---
title: "Field Definitions: VA Inquiry Links Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-links-form/field-definitions-va-inquiry-links-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-links-form/field-definitions-va-inquiry-links-form"
---

# Field Definitions: VA Inquiry Links Form

The following is a list of field descriptions for the VA
 Inquiry Links form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Default Drill-Through

Select this checkbox if double clicking on a record in the inquiry should drill through into this query - for example, if you have a query that displays purchase order information and you want to double click on a PO and view the PO items.
When a query is not the default drill-through, you must select a record in the grid, click the drop down arrow next to the Drill-Through () icon, and then select the query that you would like to drill-through into.

## Display Sequence

When using a query in a Work Center, related queries are opened using a drop down menu. Use this field to define the order that the queries will display in that drop down.
You can leave this field blank and click the
 Save
 icon, and the system will automatically assign the query the next available sequence
 number.

## Related Query

Use this field to select the query that you
 would like to relate. Press F4 to select the query from a list.

## Default Value

Use either this field or the Matching Column
 field to set up a parameter value on the linked query.
Check this box if you want the parameter value to come from the default value that was set up on the Parameters tab back on the [VA Inquiries ](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form) form.

## Matching Column

Use either this field or the Default
 Value field to set up a parameter value on the linked query.
Press F4 in this field to select the
 matching column in the linked query. Only the columns on the linked query will display
 in the list.
This is the column in the linked query that should
 match the parameter in the Parameter Name field. For example if
 you are linking a PO company parameter with a PO company field and @POCo is in the
 Parameter
 Name field, press F4 and select the POCo column from the
 list.
