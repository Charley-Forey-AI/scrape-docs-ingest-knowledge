---
title: "About the Form Properties form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-form-properties-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-form-properties-form"
---

# About the Form Properties form

You can use the Form Properties form to customize the look of the application,
 associate reports with forms, and reset form and field overrides (i.e. F3 settings) at the
 user and/or system-wide level.
You can access this form using one of the following methods:

- Select the form in the Items pane (Main Menu), and then select the Form Properties option from the Items menu or the shortcut menu (accessed by right-clicking the mouse).

- Open the form, and then select the Form Properties option from the Tools menu or the context menu (accessed by right-clicking the mouse in any gray area of the form).

Note: If you are not designated as a Form Administrator (in VA User Profile), you will be limited to changing the settings defined on the User tab.

## User Tab

This tab is used to reset specific user
 overrides for a form (i.e. overrides defined on the User Overrides tab of the Field
 Properties (F3) form). You can select one or more overrides to reset or reset all
 form and field overrides. You can also use this tab to set or reset the User’s
 Default tab, which is the tab that will display when a form opens.
For information on a specific reset
 option, move the cursor to the box and press F1. This will open the help that
 relates to that field.
Note: Resetting overrides on this tab will affect
 only the user overrides for the current user. All other user override settings are
 left intact.

## System Wide Tab

This tab is used to reset system wide
 form and field overrides. Resets initiated on this tab will affect only the
 overrides defined on the System Overrides tab of the Field Properties (F3) form. You
 can select one or more overrides to reset or indicate to reset all form and field
 overrides.
For information on a specific reset
 option, move the cursor to the box and press F1. This will open the help that
 relates to that field.
Note: Resetting overrides on this tab will affect
 system wide overrides for all users and all occurrences of the selected form.
 Overrides defined by user on the User tab will be left intact.

## Images Tab

This option allows you to change or
 reset the form and progress indicator images for the selected form. Changes made
 here affect this form for all users.

- Menu Icon – This option allows
 you to change the Icon for the selected form. Click the Display Icons button
 to display the Icon Viewer window. Select the desired icon from the list of
 available icons and click OK. The new icon image appears in the box to the
 left and the icon name in the Menu Icon input.

- Progress Clip – This option
 allows you to change the progress indicator for some posting and processing
 forms (disabled for Setup forms). Click the Display Clips button to display
 the Icon Viewer window. Select the desired clip from the list of available
 clips and click OK. The new progress clip appears in the box to the left and
 the clip name in the Progress Clip input.

To reset the images, just click the
 Reset button. A message displays indicating that you are about to reset the form
 images and warning you that the form will be reloaded and any pending record changes
 lost. Click Yes to reset the form and progress indicator to their default images, No
 to cancel the reset and leave the image assignments intact. (Note: This reset
 affects all users.)

## Tab Pages Tab

This tab is used to customize the tabs
 for the current form. You can change the order in which the tabs on the form are
 displayed, add new tabs, or change/delete existing tabs.

- Change Tab Position – Highlight
 the desired tab name in the selection box. Then using the up and down arrows
 (to the right), move the tab to the desired position.

- Add – Click this button to add a
 new tab. An Add Tab form displays, allowing you to enter the Tab Title. Once
 you click OK, the new tab is added as the last tab in the form. You can then
 use the up/down arrows to reposition the tab as desired.

- Edit– Use this button to change
 the name of a customized tab, or set up a customized tab to display a query
 or UD table. [More](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-tabs-form)

- Delete– Click this option to
 delete a user-defined tab. (Note: You cannot delete standard form tabs.)


- Reset– Click this button to
 reset the tab pages for the form. A message displays indicating you are
 about to reset the tab pages for the form and asking if you want to
 continue. Click Yes to continue, No to cancel the reset and leave the image
 assignments intact. (Note: Resetting tab pages will delete all user-defined
 tabs for the form.)

To reset the tab pages, just click the
 Reset button. A message displays indicating that you are about to reset the tab
 pages and warning you that the form will be reloaded and any pending record changes
 lost. Click Yes to reset the tab pages to their standard settings, No to cancel the
 reset.
Once the reset is finished, the Form
 Properties form is closed and you are returned to the main menu or selected form,
 depending on how you accessed Form Properties. Reset is effective immediately; you
 will not be required to close and reopen the form for the changes to take effect.


## Fields Tab

This display-only tab lists all of the
 fields for the selected form in grid format. For each field listed, you can view
 specific information about the field including the sequence number, description,
 associated view (if applicable), column name, and field value, as well as the input
 type, field type, datatype, input mask, length, and precision. Other information
 shown includes the default settings for each field, such as the skip input,
 required, show on grid, validation, and status text.
Because the grid is display only, you
 are restricted from adding, changing, or deleting a form's fields; however, you can
 access the properties for any field by double-clicking the row of the desired field.
 Overrides to the field's properties will be updated to the grid once you exit the
 Field Properties window and close the form.
You can change the sort order of the
 grid records by clicking on the heading of any column in the grid.

## Security Tab

This tab shows the user’s
 ‘add/update/delete’ permissions for the selected form. The Permissions options
 indicate whether the user has the ability to add new records, update existing
 records, and/or delete existing records. If a permission option is unchecked, the
 user will not have the ability to perform the indicated function. (Note: Record
 permissions are defined in VA Form Security).
The Security Link section is intended
 for use with header/detail forms, and shows the ‘header form’ to which the detail
 form is linked. The security defined for a detail form (e.g. AP Transaction Entry
 Detail) is automatically determined by the security defined for its associated
 header form (e.g. AP Transaction Entry). If you want to maintain detail form
 security separately, select the “Allow security for this form…” checkbox. This
 removes the link between the header and detail form, allowing you to maintain
 security for each form separately (in VA Form Security).
Once you change the security link, an
 audit record is created indicating the change. You can view the audit record in the
 Viewpoint Log Viewer (Help  > System > View
 Logs). For example, if you check this option for AP
 Transaction Entry Detail, the description provided in the log viewer would be:
“Security Link for APEntryDetail has
 been changed. No longer linked to APEntry – access must be maintained separately.”
[Click here for information about setting up Form Security.
 ](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

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

- [Associate a Report with a Form](/en/vista/vista/system-tools/user-interface-guide/system-forms/associate-a-report-with-a-form)

- [About the Field Properties Form](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form)

- [Field Validation](/en/vista/vista/system-tools/user-interface-guide/system-forms/field-validation)

- [Schedule Data Changes for Fields](/en/vista/vista/system-tools/user-interface-guide/system-forms/schedule-data-changes-for-fields)

- [Search Form Records](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records)

- [Group Custom Fields](/en/vista/vista/system-tools/user-interface-guide/system-forms/group-custom-fields)

- [Add a Standard Note to a Field](/en/vista/vista/system-tools/user-interface-guide/system-forms/add-a-standard-note-to-a-field)

- [Form Grids](/en/vista/vista/system-tools/user-interface-guide/system-forms/form-grids)
