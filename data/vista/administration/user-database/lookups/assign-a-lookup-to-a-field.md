---
title: "Assign a Lookup to a Field | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/lookups/assign-a-lookup-to-a-field"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/lookups/assign-a-lookup-to-a-field"
---

# Assign a Lookup to a Field

You can assign lookups to fields.
Lookups are windows that display when F4 is pressed in a field, showing valid data related to that field. Typically, lookups are assigned only to fields that require valid input from a specific table, such as Vendor (APVM), Job (JCJM), Phase (JCPM), and so forth. See [F4 - Lookup](/en/vista/vista/system-tools/user-interface-guide/system-forms) for general information on lookups.
By default, many standard fields have one or more standard lookups assigned. If multiple lookups are assigned to a field, they are shown as options in the lookup window. For example, when F4 is pressed for the Phase field in JC Cost Adjustments, two lookup options will display: Job Phases and Phase Master. The selected lookup determines what phases display.
You can override the standard lookup with a different standard lookup. If you have created a custom lookup, you can assign it to a specific field in a form (the calling form). If a custom field is associated with a standard datatype (e.g. bJob, bPhase, bVendorSortName, etc.), the datatype's lookup will be used by default. You must be designated as a Form Administrator (in VA User Profile) in order to edit lookup information.

1. Press F3 in the field that the lookup was created for. This opens the Field Properties form.

1. Open the Lookups tab.

1. Enter the name of the lookup in the Lookup field or press F4 to see a list of valid lookups.

1. If the Parameters field is enabled, enter lookup parameters in that field. See the F1 Help for more information.

1. Select the Active checkbox to enable the lookup.

1. Use the Load Seq field to determine which lookup(s) will display when F4 is pressed from a field, and in what order.

- To assign a custom lookup to a field, set the Load Seq field with the number(s) collected in step 4 of [Creating a Custom Lookup](/en/vista/vista/administration/user-database/lookups/create-a-custom-lookup). Enter the numbers in the order specified by the Where Clause in that step.

- To override a standard lookup with a different lookup, set the Load Seq field to 1 for the new lookup, and then clear the Active checkbox for the overridden standard lookup.

1. To add another lookup to a field, repeat steps 3-6 in additional rows in the Lookups grid for that field.

1. Click OK. The lookup is now assigned and is ready for use.
