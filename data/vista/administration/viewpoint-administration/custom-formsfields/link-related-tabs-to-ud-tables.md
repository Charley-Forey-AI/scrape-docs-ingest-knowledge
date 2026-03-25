---
title: "Link Related Tabs to UD Tables | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/link-related-tabs-to-ud-tables"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/link-related-tabs-to-ud-tables"
---

# Link Related Tabs to UD Tables

When creating user-defined (custom) forms/tables, you may want
 to associate them with another form (the “parent” form). For example, you might create a
 “vehicles” form and want to associate it with the EM Equipment parent form.
You can do this using a custom related grid tab. Related grid tabs allow you to provide information that is associated with the record in the current form, but does not directly affect the record. The grid on the custom related grid tab is tied to your user defined form (which can be accessed by double-clicking on a record in the grid or by highlighting the record and selecting Records > Open Related Record in Form).
When linking a user-defined table to a related grid, you should be aware of the following:

- You can only link user-defined tables to custom related tabs that do not already have custom fields. In other words, you can only link user-defined tables to blank tabs.

- You cannot add or move any custom fields onto a custom tab that has a linked user-defined table.

Follow the steps below to link a user-defined table to a related grid tab.

1. Create the user-defined table. For more information, see [About the UD User Table and Form Setup Form](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form)Note: When creating the user-defined table, make sure to create at least one key field (using the Key Seq field) that matches a field on the form where you will create the related tab. Key fields uniquely identify data records. Having both the user-defined table and the parent form share a key field enables data linking.

1. Open the form that you want to add the tab to.

1. Select Tools > Field Properties from the menu at the top of the form to launch the Form Properties form.

1. Click the Add
 button on the Tab Pages tab and then enter the name of the tab that you want to
 create. This will add the new tab to the form.

1. Use the Tab Pages tab on the Form Properties form again, highlight the new tab and click the Edit button. This will launch the VA Custom Form Tabs form.

1. Select 0-Default in the Control Type drop down.


1. Press F4
 in the Grid Form field to select the user-defined table that you
 created.

1. Open the Grid Links tab.

1. Press F4
 in the GridKeySeq field and select the key field sequence number from
 the user-defined table.

1. Press F4
 in the ParentFieldSeq field and select the field sequence number from
 the parent form.

1. Repeat steps 9 and 10 for more user-defined table key fields if necessary.

1. Save your changes and return to the form you just added the tab to.

1. A grid displaying the information from the user-defined table/form displays on the parent form’s custom related grid tab.

Note: Deleting a tab: Before deleting a related tab associated with a UD table, you must remove the link between the tab and the table. To do this, access the VA Custom Form Tabs form and look up the parent form. Search for the correct tab using the Tab# field. Clear the Grid Form field and save the record. Then, delete the tab using Form Properties.

Related information

- [About the UD User Table and Form Setup Form](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form)

- [VA Custom Form Tabs Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-tabs-form)

- [About the Form Properties form](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-form-properties-form)
