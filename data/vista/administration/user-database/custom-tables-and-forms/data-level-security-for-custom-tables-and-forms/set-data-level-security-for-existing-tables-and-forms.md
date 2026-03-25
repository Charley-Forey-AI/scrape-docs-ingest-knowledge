---
title: "Set Data Level Security for Existing Tables and Forms | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms/set-data-level-security-for-existing-tables-and-forms"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms/set-data-level-security-for-existing-tables-and-forms"
---

# Set Data Level Security for Existing Tables and Forms

You can add data level security to existing database tables or forms.
In order to add data level security to an existing table or form, you must associate it with a company.

1. In the UD User Table and Form Setup form, in the



 Table Name field, select the custom table/form to which you want to add security.

1. Create a new "company" column for the table.Note: The new “company” column cannot be named “Co” as that name is reserved for the Company column generated when the Company Based checkbox has been selected. Other variations on “company” are allowed (e.g., Company, company, comp, etc.).

1. Assign the column the company datatype associated with the datatype that requires security. Typically, this is the same datatype as the majority of the securable datatypes reference companies. For example, if a column was added with the APCo (AP Company) datatype referenced, the company datatype would be APCo. The company datatype is not always apparent for every datatype. The following table displays the associated company datatypes with these other securable datatypes. If the datatype that requires securing is:Then the company datatype should be:
bCMAcct
bCMCo

bContract
bJCCo

bEmployee
bPRCo

bHRRef
bHRCo

bJob
bJCCo

bLoc
bINCo

1. Click



 Update Table to save the table.

1. Access VA Data Security Setup and lookup the Datatype that requires security.

1. Verify that the UD table name appears on the Secure Tables tab.

1. Enter the UD table name in the



 Table Name column.

1. Enter the name of the field that requires security in the



 Instance Column.

1. Enter the name of the company datatype in the



 Qualifier Column.

1. Select the



 In Use checkbox for the field.

1. Click



 Regenerate Views to access the VA View Generator.

1. Follow the instructions for adding tables in the VA View Generator help. For more information, refer to [VA View Generator](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-va-view-generator-form). Data level security is now set for the custom table.

Related concepts

- [Data Level Security for Custom Tables and Forms](/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms)

Related tasks

- [Set Data Level Security when Creating a New Custom Form](/en/vista/vista/administration/user-database/custom-tables-and-forms/data-level-security-for-custom-tables-and-forms/set-data-level-security-when-creating-a-new-custom-form)
