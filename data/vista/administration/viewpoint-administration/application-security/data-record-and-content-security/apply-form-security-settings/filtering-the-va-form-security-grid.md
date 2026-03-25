---
title: "Filtering the VA Form Security Grid | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-form-security-settings/filtering-the-va-form-security-grid"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-form-security-settings/filtering-the-va-form-security-grid"
---

# Filtering the VA Form Security Grid

When assigning form security in VA Form Security, you first filter for specific groups/users or forms, and then set access levels and well as record-level and attachment permissions.
You can change the grid display by selecting the Grouping checkbox. This allows for filtering by specific values in each column. You can regroup the grid into a custom hierarchy by dragging column headers to the gray area along the top of the grid. Additionally, you can use a wildcard (*, %) to filter information in the grid. For example, if you want to filter for all AP forms, enter *AP in the filter bar under the Mod column.
The following instructions detail how to filter the form security grid in VA Form Security. For more information , see the F1 Help in each field.

1. Select the company (or companies) to filter by from the Companies list. To set security for all companies, select Global.

-  If you do not see a company in this list, you have not been granted form security permissions to administer form security for that company.

- If the Global option is not available, then you have not been granted form security permissions to administer form security for all companies.

1. Select the module (or modules) to filter by from the Modules list. To filter by all modules, select All.

1. In the Select By field, select whether the form filters by Group #, Group Name, User, or Form. The selection box to the right displays all available groups, users, or forms (depending on the filter selection).

1. Select the Group(s), User(s), or Form(s) to filter by in the selection box.

- To find options in the selection box, type in the Search field to filter options in the selection box.

-  To find options by first letter or number, type that character to automatically check the first option starting with that letter or number in the selection box. If you type the character again, the system will check the next option with the same first character.

- To filter by all, select the All checkbox. If you have first filtered the selection box by using the Search field, using All will select all of the filtered options, but will not select options not found by the search.

1. Click the Refresh Grid button to display the results in the grid. The system groups the filter results in the grid differently depending on the filter selection in the Select By field.

- If you filter by Form, the system groups the results hierarchically by Company, Module, Form, and Groups/Users.

- If you filter by Group # or Group Name, the system groups the results by Company Module, Group, and Form.

-  If you filter by User, the system groups the results by Company, Module, User, and Form.

- If [VA Security Administration](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-administration-form) is turned on, you may see only some company/module combinations in the grid, regardless of the modules selected in Step 2.

1. If desired, check the Grouping checkbox to enable you to manipulate the grid display.

1. If desired, click the Refresh Grid button again to clear the grid.

Now you can apply form security for the records in the grid. For more information, see [Applying Form Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-form-security-settings).

Related information

- [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

- [Apply Form Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-form-security-settings)

- [Apply Tab Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-tab-security-settings)

- [Logged On Users uses Form Security](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-0004990e--en)

- [User Permission Levels](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/user-permission-levels)

- [Interaction Between Group and User Level Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings)
