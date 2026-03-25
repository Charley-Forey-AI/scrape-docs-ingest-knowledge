---
title: "Create a Custom Lookup | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/lookups/create-a-custom-lookup"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/lookups/create-a-custom-lookup"
---

# Create a Custom Lookup

Use the UD User Defined Lookups form to create custom lookups.
Lookups are windows that display when you press F4 from a field, showing valid data related to that field.
Lookups are created using “clauses” that act as data filters. Before creating a lookup, you must first determine the “from” database table (where the required data is located), as well as the specific database fields/columns to filter information by. Use the following instructions to create a custom lookup.
Custom lookups can also be created by copying a standard lookup and modifying it. For more information, see [Copying a Lookup](/en/vista/vista/administration/user-database/lookups/copying-a-lookup).
Note: This topic provides basic information on creating clauses; however, clauses can be quite complex. For additional help and information, speak to your system administrator.

1. Identify the table that the lookup will pull data from. To do this, press F3 in any field on the form. Note the name displayed in the View field. This the table that needs to be specified when creating the "from clause".

1. Determine which fields in the form will display in the lookup. These fields define the lookup columns. You will define these fields in a later step.

1. Repeat step 1 to identify the calling table (the table/form using the lookup).

1. Determine which columns on the calling table will be used in the Where Clause to filter data. Press F3 (Form Properties) for each field on the calling form and note the number displayed in the Field Seq # drop-down. These numbers will used when assigning the lookup to the calling field.

1. In the UD User Defined
 Lookups form, enter the name of your new lookup in the Lookup field. The name must begin with the letters ud.

1. In the Title field, enter the title for your lookup. This is the
 description/title that displays when accessing this lookup.

1.  Create clauses in the From Clause, Where Clause, Join Clause, and GroupBy Clause fields. For more information on creating clauses, see [From Clause](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-0004752f--en), [Where Clause](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-0004753a--en), [Join Clause](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-00047544--en), and [GroupBy Clause](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-0004754c--en). Note: These topics provides basic information on creating clauses. For additional help and information, speak to your system administrator.

1. Select the [Sort Descending](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-0004757a--en) checkbox if necessary to adjust the order in which the columns will display in the lookup.

1. Use the [Order by Column](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form/field-definitions-ud-user-defined-lookups-form#ID-00047552--en) field if necessary to adjust the sort order of the columns.

1. On the Details tab, define the lookup columns on the Details tab. For more information, [Defining Lookup Columns](/en/vista/vista/administration/user-database/lookups/define-lookup-columns).

1. Assign the lookup to the field. For more information, see [Assigning a Lookup to a Field](/en/vista/vista/administration/user-database/lookups/assign-a-lookup-to-a-field). The lookup is now created.

Related information

- [Copying a Lookup](/en/vista/vista/administration/user-database/lookups/copying-a-lookup)

- [About the UD User Defined Lookups Form](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-defined-lookups-form)

- [About the UD User Lookups Copy Form](/en/vista/vista/administration/user-database/lookups/about-the-ud-user-lookups-copy-form)

- [Set the Maximum Number of Records for Lookups](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-the-maximum-number-of-records-for-lookups)
