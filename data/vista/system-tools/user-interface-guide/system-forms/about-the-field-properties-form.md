---
title: "About the Field Properties Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form"
---

# About the Field Properties Form

You can use the Field Properties form to customize fields. For example, you can customize the default value or validation on a field.
You can open this form by moving the cursor into a field and then doing one of the following:

- Press F3 while in the field

- Select Tools  Field Properties

- Right-click and select Field Properties from the menu that appears

 If you access this form from a key field, you are limited in the changes that you can make. The system uses key fields to identify a unique record, and are generally located on a form above the tabs.

## User Overrides Tab

This tab is used to set user overrides to default, display, and validation settings that are specific to your login. This includes:

- how a field defaults values; that is, standard default, previous value, fixed value, or variable date.

- whether to skip the field during input

- whether to display the field on the form and/or grid

- whether to display the field’s description (if applicable) in the grid only, above the grid only, or not at all

- whether a value is required in the field

Settings at this level override the system and standard settings, with the exception of settings for key fields and for fields that are hard-coded as ‘Required’ or are designated as ‘Required’ at the System level.
Note: If you elect to ‘hide’ a required field (i.e. uncheck the Show on Form option) , it is imperative that you set a default value for the field to ensure it is correctly populated even though the field is hidden.

## System Overrides Tab

This tab is used to set up override default, display, setup, custom field, and validation settings that affect all users. To set overrides on the System Overrides tab, you must be designated as a Form Administrator in VA User Profile.Important: Although you can assign F5 access to any standard Viewpoint field, we recommend that you do not use this functionality to override standard F5 assignments.

Custom ValidationWhen creating custom validation using the Validation section on the System Overrides tab, be aware of the following:

- The custom validation does not override or replace the system validation - Both the custom and system validation will be applied. When you create custom validation you are adding additional validation. You are not overriding the existing system validation.

- Since both the system and custom validations are applied, they both must be met. For example, this means that you cannot override the system validation with a less restrictive custom validation. The system and the custom validation will both be applied.

For information about setting up validation for custom fields, see [UD User Validation](/en/vista/vista/administration/user-database/custom-validation-procedures/about-the-ud-user-validation-form).

Timestamp Notes
You can set up timestamping on Notes fields so that entries in the field are recorded with the time and date, as well as the user who entered the data. Timestamping is set up by selecting the Display as Timestamp Note checkbox on the System Overrides tab for the selected field. However, this option is only enabled for Notes fields using a bNotes datatype (which you can check using the Property Values tab).
 If you select the Display as Timestamp Note checkbox for a Notes field, each time a note is entered, it is timestamped with the date, time, and user's login name. You cannot change or delete the notes, as long as the timestamp function is in effect. Once you deselect the Display as Timestamp Note checkbox, you can change or delete any previously entered notes.

## Property Values Tab

This tab is display only and allows you to see the all of the properties for the selected input, such as column name, control type (e.g. text box, checkbox, etc.), the datatype (if applicable), default value, grid column sequence, input length and mask, related view, and so forth.

## Lookups

This tab allows you to edit lookup information. This includes assigning lookups to a custom or standard field, as well as changing the parameters, load sequence, and ‘active’ status for existing lookups. For more information, see [Assigning a Lookup to a Field](/en/vista/vista/administration/user-database/lookups/assign-a-lookup-to-a-field).
To edit lookup information, you must be assigned as Form Administrator in [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form).
You can limit the number of records displayed in a lookup. See [Setting the Maximum Number of Records for Lookups](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-the-maximum-number-of-records-for-lookups).

Related information

- [System Forms](/en/vista/vista/system-tools/user-interface-guide/system-forms)

- [Form Menu Options](/en/vista/vista/system-tools/user-interface-guide/system-forms/form-menu-options)

- [Keyboard Shortcuts for Moving Through Form Fields](/en/vista/vista/system-tools/user-interface-guide/system-forms/keyboard-shortcuts-for-moving-through-form-fields)

- [Shortcut Keys](/en/vista/vista/system-tools/user-interface-guide/system-forms/shortcut-keys)

- [Date Field Shortcuts](/en/vista/vista/system-tools/user-interface-guide/system-forms/date-field-shortcuts)

- [Toolbar Options](/en/vista/vista/system-tools/user-interface-guide/system-forms/toolbar-options)

- [Function Keys](/en/vista/vista/system-tools/user-interface-guide/system-forms/function-keys)

- [Status Bar](/en/vista/vista/system-tools/user-interface-guide/system-forms/status-bar)

- [Record Deletion](/en/vista/vista/system-tools/user-interface-guide/system-forms/record-deletion)

- [Batch Processing](/en/vista/vista/system-tools/user-interface-guide/system-forms/batch-processing)

- [Email a Deep Link to a Record](/en/vista/vista/system-tools/user-interface-guide/system-forms/email-a-deep-link-to-a-record)

- [About the Form Properties form](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-form-properties-form)

- [Associate a Report with a Form](/en/vista/vista/system-tools/user-interface-guide/system-forms/associate-a-report-with-a-form)

- [Field Validation](/en/vista/vista/system-tools/user-interface-guide/system-forms/field-validation)

- [Schedule Data Changes for Fields](/en/vista/vista/system-tools/user-interface-guide/system-forms/schedule-data-changes-for-fields)

- [Search Form Records](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records)

- [Group Custom Fields](/en/vista/vista/system-tools/user-interface-guide/system-forms/group-custom-fields)

- [Add a Standard Note to a Field](/en/vista/vista/system-tools/user-interface-guide/system-forms/add-a-standard-note-to-a-field)

- [Form Grids](/en/vista/vista/system-tools/user-interface-guide/system-forms/form-grids)
