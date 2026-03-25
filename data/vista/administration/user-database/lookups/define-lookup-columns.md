---
title: "Define Lookup Columns | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/lookups/define-lookup-columns"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/lookups/define-lookup-columns"
---

# Define Lookup Columns

When you create custom lookups, you must define the columns (fields) that display in the custom lookup.
 You can use only columns that exist in the table(s) referenced in the From Clause field in UD User Defined Lookups form. (These columns were identified in step 2 of [Creating a Custom Lookup](/en/vista/vista/administration/user-database/lookups/create-a-custom-lookup).)

1. Determine which columns (fields) in the form will display in the lookup. These fields define the lookup columns. (These fields were also identified in step 2 of [Creating a Custom Lookup](/en/vista/vista/administration/user-database/lookups/create-a-custom-lookup).)

1. In the Details tab of the UD User Defined Lookups form, assign each column a sequence number in the Seq# field. By default, this determines the order in which columns display in the lookup. When using a lookup for field input, data returns to the form from the column with the lowest sequence number.

1. Enter the column name in
 the ColumnName field and a description in the ColumnHeading field (which the system uses to display in the
 lookup). Associated datatypes display in the Datatype field, which you can change if necessary. All other
 fields are display only and default based on the datatype.

Related information

- [Create a Custom Lookup](/en/vista/vista/administration/user-database/lookups/create-a-custom-lookup)

- [About the UD User Defined Lookups Form](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form)

- [About the UD User Lookups Copy Form](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-lookups-copy-form)
