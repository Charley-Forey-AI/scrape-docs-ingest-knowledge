---
title: "Field Definitions: VA Report Security Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form/field-definitions-va-report-security-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form/field-definitions-va-report-security-form"
---

# Field Definitions: VA Report Security Form

The following is a list of field descriptions for the VA
 Report Security form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Companies

Select the company or companies to filter the
 grid for setting security. To set security for all companies, select the Global
 checkbox.
If you do not see the Global option or other company options in this list, you may not have been granted form security permissions to administer report security for those companies.
Note: The Global option sets the same security level across all companies. If you add any additional companies in the future, users who have access at the Global level will have access to those new companies as well.
Important: When setting up security on SSRS reports, you
 should always select the Global option. Any user with access to an
 SSRS report in one company can run it for all companies.

## Grouping

Select this checkbox to reorganize the grid display.
Once you check this box, you can group results in the grid by a column by dragging that column header to the grid header section.

## Groups/Users/Reports

Select the groups, users, or reports to filter the grid for setting security.
 The name of this field and the options displayed in it change depending on the option you selected in the [Select By](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form/field-definitions-va-report-security-form#ID-000494ff--en) field.
If you selected Report in the
 Select
 By field, this field's options also change depending on the options you
 selected in the Modules field.
Select the Group(s), User(s), or Form(s) in the selection box to filter the grid by

- To find options in the selection box, type in the
 Search field to filter options in the selection box. The Search field
 is case-sensitive.

-  To find options by first letter or number, type that character to automatically check the first option starting with that letter or number in the selection box. If you type the character again, the system will check the next option with the same first character.

- To filter by all, select the All check
 box. If you have first filtered the selection box by using the Search
 field, using All will select all of the filtered options, but will not select
 options not found by the search.

## Modules

Select the module or modules to filter the
 grid for setting security for reports. To filter by all modules, check the All
 checkbox.

## Select By

 Select the appropriate option to filter the gird for setting security. The option you select here determines what displays in the [Groups/Users/Reports](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form/field-definitions-va-report-security-form#ID-00049511--en) box.

- Group # — Select this option to filter by the security group number. The groups will display in numerical order.

- Group Name — Select this option to filter by the security group name. The groups will display box in alphabetical order.

- User — Select this option to filter by user name.

- Report — Select this option to filter by report. If you have selected one or more options in the [Modules](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form/field-definitions-va-form-security-form#ID-00048afe--en) field, the related reports will display in alphabetical order.
