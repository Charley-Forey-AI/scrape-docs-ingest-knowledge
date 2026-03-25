---
title: "Set Data Level Security when Creating a New Custom Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms/set-data-level-security-when-creating-a-new-custom-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms/set-data-level-security-when-creating-a-new-custom-form"
---

# Set Data Level Security when Creating a New Custom Form

 You can set data level security for custom tables/forms.
Data level security requires that there is a company association for the user-defined field you are securing. Use this procedure if the table has not yet been finished and you have not clicked Update Table in the UD User Table and Form Setup form.

1. In the UD User Table and Form Setup form, for the form you are currently creating, select the Company Based checkbox in for the related custom form. When the table is created, the system automatically generates an invisible Company column (“Co”) that populates with the active company when the form is accessed. In addition, this makes the table available for selection in VA Data Security Setup.

1. Configure the table and columns as needed. For more information see [UD User Table and Form Setup](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form).

1. Click Update Table to save the table.

1. Access VA Data Security Setup and locate the custom table.

1. Select the In Use checkbox.

1. Click Regenerate Views to access the VA View Generator form.

1. Follow the instructions for adding tables. For more information, refer to [VA View Generator ](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-va-view-generator-form) . Data level security is now set for the custom table.

Related concepts

- [Data Level Security for Custom Tables and Forms](/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms)

Related tasks

- [Set Data Level Security for Existing Tables and Forms](/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms/set-data-level-security-for-existing-tables-and-forms)

Related information

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)

- [About the UD User Table and Form Setup Form](/en/vista/vista/administration/user-database/custom-tables-and-forms/about-the-ud-user-table-and-form-setup-form)

- [About the VA View Generator Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-va-view-generator-form)
