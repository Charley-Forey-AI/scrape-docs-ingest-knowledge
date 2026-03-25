---
title: "Field Validation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/field-validation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/field-validation"
---

# Field Validation

Most forms throughout the software have some type of validation applied to one or more
 fields on the form. Depending on the field, validation may require an entry and/or that the
 entry meets specific requirements.
For example, validation for a Job field on
 one form may require that an entry is made, that the job is valid (i.e., exists in JC
 Jobs), and that the job status is ‘Open’. On another form, validation may not require
 entry of a job, but if an entry is made, that the job is valid. In some cases,
 validation may be controlled by a flag setting in a company file. For example, if the
 Validate Material flag is unchecked in JC Company Parameters, validation will allow
 entering non-HQ materials in JC Material Use, but only for ‘MI-Miscellaneous’ type
 transactions. If the flag is checked, all materials entered in JC Material Use must be
 valid.
Note: Although most required fields will require a valid
 entry, there are specific situations where validation will allow a non-valid entry in a
 required field. In the company setup forms, it is quite common for information to be
 required that has not yet been set up in related forms. For example, you may be required
 to enter a GL company, but have not yet set up all the GL companies you will use.
 Validation will allow you to save the record with the non-valid entry, but you must make
 sure that you set up the referenced GL company in GL Company Setup, especially when you
 are also assigning default GL accounts.
For non-validated fields, you have the
 option to apply validation via the Field Properties (F3) form. If applying user-specific
 validation (the User Overrides tab), you can only define whether a value is required on
 a non-validated field. However, if you are applying validation at the system level (the
 System Overrides tab), you have the option to assign a custom validation procedure and
 define how it operates.
Note: You cannot apply standard Viewpoint validation
 procedures to custom or non-validated fields; however, from within SQL Server, you can
 copy a standard validation procedure, rename it, modify it as necessary, and then assign
 it as secondary validation to the desired field. See your database administrator for
 assistance in copying validation procedures.
Note: In order to apply custom validation to a field, you
 must have created a custom validation procedure (using UD User Validation).

## Secondary Validation

You cannot remove or override the standard
 validation defined for a field; however, you can apply a secondary validation procedure
 to supplement existing validation. Secondary validations allow you to implement a more
 restrictive validation process than what is standardly applied.
For example:

- Your company requires that haul
 charge and haul vendor payment amounts be equal when entering tickets (in MS
 Ticket Entry). You could apply a secondary validation to the Haul Charge and/or
 pay Total fields to warn when this condition is not met.

- Your company requires that purchase
 orders be posted to a specific cost type (e.g. cost type ‘2’). You could apply a
 secondary validation to the Cost Type field (in PO Purchase Order Entry) that
 restricts entry to only that cost type.

The system initiates standard validation
 first; secondary validation occurs only if the required standard validation conditions
 are met. If the validation level (specified in the Level field) differs between the
 standard and secondary validation procedures, the system uses the more restrictive
 level. For example, if the validation level for one procedure is set to ‘1-Warning,
 allow save’ and the other is set to ‘3-Show error, stay on input’, both procedures will
 use ‘3-Show error, stay on input’.
Once validation is complete, the standard
 and secondary validation messages display in a single window, with the standard
 validation messages appearing first.
Note: The system automatically applies secondary
 validation once you assign it to a field and save the record. If you wish to disable
 secondary validation during data entry, deselect the Secondary Validation option in the
 Options menu. You can reselect the option to reactivate secondary validation once you
 complete posting.

Related information

- [System Forms](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms)

- [Form Menu Options](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-menu-options)

- [Keyboard Shortcuts for Moving Through Form Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/keyboard-shortcuts-for-moving-through-form-fields)

- [Shortcut Keys](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/shortcut-keys)

- [Date Field Shortcuts](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/date-field-shortcuts)

- [Toolbar Options](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/toolbar-options)

- [Function Keys](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/function-keys)

- [Status Bar](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/status-bar)

- [Record Deletion](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/record-deletion)

- [Batch Processing](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/batch-processing)

- [Email a Deep Link to a Record](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/email-a-deep-link-to-a-record)

- [About the Form Properties form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-form-properties-form)

- [Associate a Report with a Form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/associate-a-report-with-a-form)

- [About the Field Properties Form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-field-properties-form)

- [Schedule Data Changes for Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/schedule-data-changes-for-fields)

- [Search Form Records](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/search-form-records)

- [Group Custom Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/group-custom-fields)

- [Add a Standard Note to a Field](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/add-a-standard-note-to-a-field)

- [Form Grids](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-grids)
