---
title: "Create a Custom Table/Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/custom-tables-and-forms/create-a-custom-tableform"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/custom-tables-and-forms/create-a-custom-tableform"
---

# Create a Custom Table/Form

You can create custom tables and forms.
You will define the table name, as well as the columns within the table. Once you save the table and columns, the new form appears in the UD Programs folder. You can then move the form to any module folder(s) as appropriate.
Note: When setting up custom UD tables and forms, do not use special characters in column or table names.The underscore ( _ ) is the only special character allowed. Use of any other special character will result in a processing failure for any dependencies.

To create a custom table/form:

1. Prior to creating a table, establish the form's design. Carefully consider how its associated form will be used. A form should be used for a specific purpose and not as a location for collecting multiple pieces of unrelated information, as this could potentially confuse other users.

1. Use the header section of this form to enter details such as the table name, description (form name), and whether you will use the form in the current company only. Additionally, you can choose whether you want to audit the form/table (monitoring additions, modifications or deletions), as well as decide what kind of Notes you want to include.

1. Use the detail section of the form to add columns to the table. When creating columns, keep in mind that at least one field must be a key field (specified by the Key Seq field). The system uses key fields to uniquely identify data records. For more information, refer to [Key Seq](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form/field-definitions-ud-user-table-form-setup-form#ID-000471f9--en).

1. Click the Update
 Table button. The system saves the table.

1. Set form security for the table so that the form will display in the UD Programs folder. For more information on setting form security, refer to [VA Form Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form).

1. If desired, set data level security for the table/form. For instructions on how to set data level security, see [Setting Data Level Security in User Tables and Forms](/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms/set-data-level-security-when-creating-a-new-custom-form).

Related information

- [About the UD User Table and Form Setup Form](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form)

- [Delete a Custom Table/Form or Column](/en/vista/vista/administration/user-database/custom-tables-and-forms/delete-a-custom-tableform-or-column)

- [Move a Custom Form](/en/vista/vista/administration/user-database/custom-tables-and-forms/move-a-custom-form)

- [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

- [Set Data Level Security when Creating a New Custom Form](/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms/set-data-level-security-when-creating-a-new-custom-form)
