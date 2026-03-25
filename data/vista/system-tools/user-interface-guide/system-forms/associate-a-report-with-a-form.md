---
title: "Associate a Report with a Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/user-interface-guide/system-forms/associate-a-report-with-a-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/user-interface-guide/system-forms/associate-a-report-with-a-form"
---

# Associate a Report with a Form

You can associate a report with a form that allows you to run
 the report directly from the form.
To associate a report with a form, you must be set up as a form administrator (VA User Profile > Info tab > Form Administrator field). The report will be associated with this form for all user accounts.

This functionality is important in the PM module Create and Send feature. Reports that are associated with a form can be generated and sent to project contacts using Create and Send. See [Create and Send - Overview](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for more information.

1. From the form that you want to associate with the report, select Tools > Form Properties.

1. Open the Reports tab on the Form Properties form. The reports that are already associated with the form display.

1. Click the Assign button. (If this button is not enabled, you are not set up as a form administrator.)  The RP Reports by Form form displays.

1. Click the New Record () icon to add a new record to the form.

1. Press F4n in the Form Name field and select the form that you want to associate with the report.

1. Press F4 in the Report ID field and select the report from the list that displays. Standard SSRS reports are available only if the Business Intelligence module is turned on.

1. Make sure that the Active box on the Info tab is checked.

1. (Optional) Use the Parameter Defaults tab to set report parameter defaults for a specific form. For example the JC Detail report has both a
 ?Company and ?BegJob parameter. When assigning the
 report to JC Jobs, you can set the Override
 Default Type field to 4-Form Input
 Value and the Override
 Default Value to %FI0 (0 is the
 sequence number for the Job field) to have the
 report parameters default the Company and Job
 currently selected on the form. This default can
 still be overridden and is not a permanent
 setting.
The Reset button is available when standard parameters have been overridden. Click this button to reset the parameters to the original defaults.

1. Close RP Reports by Form. The report now displays on the Reports tab of the Form Properties form.

1. Close the Form Properties form.

1. If the report does not display in the the Options > Report menu, close and reopen the associated form again.

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

- [About the Field Properties Form](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form)

- [Field Validation](/en/vista/vista/system-tools/user-interface-guide/system-forms/field-validation)

- [Schedule Data Changes for Fields](/en/vista/vista/system-tools/user-interface-guide/system-forms/schedule-data-changes-for-fields)

- [Search Form Records](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records)

- [Group Custom Fields](/en/vista/vista/system-tools/user-interface-guide/system-forms/group-custom-fields)

- [Add a Standard Note to a Field](/en/vista/vista/system-tools/user-interface-guide/system-forms/add-a-standard-note-to-a-field)

- [Form Grids](/en/vista/vista/system-tools/user-interface-guide/system-forms/form-grids)

- [About the RP Reports by Form Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form)

- [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)
