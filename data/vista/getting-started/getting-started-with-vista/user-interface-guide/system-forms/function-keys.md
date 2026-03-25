---
title: "Function Keys | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/function-keys"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/function-keys"
---

# Function Keys

There are several function keys in the system that you can use as shortcuts to other forms or helpful tools.
Function KeyDescription
F1 - Field Help
Move the cursor into a field in a form and press F1. This will open the VistaHelp topic that applies to the selected field.
You can keep the Help window open as you use the application, pressing F1 while the cursor is in a field to open the related help topic in that window.

F3 - Field Properties
Pressing F3 in a field launches the [Field Properties](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-field-properties-form) form, which can be used to customize a field - for example customize the default values or validation.
For more information on the Field Properties form, see [About the Field Properties Form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-field-properties-form).

F4 - Lookup
This function key allows you to access the Lookup window from fields that require a valid value; that is, values that are set up and stored in a specific file. Examples are a job code, phase code, vendor number, contract number, or material code. You may also access a field's Lookup by selecting Tools > Field Lookup or by selecting the Field Lookup button () on the toolbar.
When you press F4, the lookup displays a list of valid values for the field which currently has the focus. If you have typed a value in the field, the lookup filters for that text when you press F4.
Note: Lookups are not available for all fields.
If there are more than a few records, you can use the grid filter to locate a specific record. For example, if you access the Job lookup and enter 11 in the Job column of the filter bar to begin displaying records starting with that value, the system will return values beginning with 11, such as "1100", "112", or "11-21".
You can refine filtering by entering values in more than one column. As you include more criteria, the filtering becomes more restrictive, and the system displays fewer records.
Note: If the Lookup window has been restricted to display a limited number of records either by design or by user option (the Lookups field in either the VA User Profile form or the User Options forms), and the records you are looking for are outside the displayed range, you can enter the specific value in a filter column and select Refresh to perform a new search.
You can also use comparison operators (for example, <, > , <>, =, >=, <=) or wildcards (% or *) to refine your search. For example, to see the next record set, you can enter the greater than operator and the value of the last record of the current record set (e.g., 540202). In this case,the system will display the next set of records beginning with the first record greater than the filter value (540202). If you use a wildcard before a value (e.g., %540), the system will return records containing the specified value (e.g., 15402, 33540, 54002, etc.).
In some cases, the Lookup window will contain multiple lookup options. Typically, this occurs when more than one lookup is available for a datatype and the current field allows values from any of the available lookups. In some cases, the options can be limited depending on other system factors. For example, if you are posting to a locked phases job, pressing F4 from a Phase field will display the Job Phases lookup option and will only allow a valid job phase. If the job is not locked, however, the Lookup window will display both a Job Phase and Phase Master option.
If data does not exist yet in the system for a field, or you need to modify existing data, you can do that through the Lookup window. To add or edit data, select Setup . The system will display the related setup form and leave the lookup window open. You can add/edit data and then close the setup form. Then from the lookup window, you can search for and select the record that you wish to use.

F5 - Setup
This function key allows you to access setup forms from fields (standard and custom) that require valid data; that is, data that is setup and stored in a specific file, such as phase codes, vendors, contract codes, material codes, and so forth. You can also access setup forms by selecting the Field Setup option from the Tools menu or by selecting the Setup button () on the toolbar.
When you press F5 in a field, you are taken directly to the related setup form (e.g. pressing F5 from a Vendor field will take you to the AP Vendors form). If you enter a value in the field, then press F5 , if the value exists, you will be taken to that record in the setup form.
You can add or change information as necessary, then exit out and be returned to the original form. The information that you just set up or changed will become immediately available for entry in the field.
Note: The form you see when pressing F5 from a field loads records based on a specified limit (designated in VA Site Settings or by override in VA User Profile or the VP Menu User Options). If a value exists in the field from which you pressed F5 , the form will load records from the specified value forward. For example, if the limit is 2500 and the value in the field is 62001, the form will load 2500 records beginning with 62001. If the field does not have a value, the form loads 2500 records beginning with the first record in the file. (Note: This situation only occurs with datasets.)Assigning Setup Forms to Custom Fields
If you use the custom fields feature (VA Custom Fields Wizard) or create your own forms in UD User Table and Form Setup, you can assign setup forms (custom or standard) to desired fields via the Field Properties form, System Overrides tab. You must be designated as a Form Administrator (VA User Profile) in order to use this feature.
Note: You also have the ability to assign F5 access to any standard field. However, we recommend that you do not use this functionality to override standard F5 assignments.

F6 - Calculator
This opens a calculator. You can use either your mouse or the numeric pad on your keyboard to enter your calculations. There are some general rules when using the keyboard to enter calculations:

- Use ENTER to total the calculations.

- A subtotal is generated after each operator is entered. For example, if you enter 100, press the + key, enter 50, and press the + key again, the Total display will show 150; however, the calculations may be continued as long as you do not press the Enter key until you are finished.

- Always enter 0 + Enter to begin a new calculation. If you have not totaled your calculation, you can 0 + Enter twice to clear the total.

- To use the % feature, you must use your mouse.

When you are finished with your calculations, you can return the value to the currently active field by selecting the Return Value to Field button. If using the keyboard, you will have to tab to the Return Value to Field button on the calculator, then press Enter.
To close the calculator using the keyboard, press Alt + F4.
You can also access the calculator by selecting the calculator icon () from the toolbar or by selecting the Calculator option from the Tools menu or shortcut menu (right mouse click).

F7-Calendar
The Calendar function is activated by selecting the Calendar button () to the right of any date field on a form. When the calendar displays, it automatically defaults to the current month and shows the current date in a red box. The input date, which may or may not be the current date, is highlighted in gray. Additionally, the calendar can be accessed by pressing the F7 key when in a date field.
You can select a different month by either using the arrow keys at the top of the calendar or by left-clicking the mouse on the month or year. If you left-click on the month, a drop-down menu displays a list of all months, allowing you to select the month you want to see. If you left-click on the year, a calendar box appears and you must click the up or down arrows to scroll to the desired year.
To change the existing input date, go to the desired month (if not the current month), then select the desired date. The calendar will close and the input is updated with the selected month, date, and year.
Note: The Calendar function does not work on grid fields. Additionally, it is not available for month/year inputs. Month/year inputs use a combo box for month/year selection.

F8- Hot Key
This function key is called the Hot Key. It allows you to access a designated form from within any other form throughout the software without going through the main menu. There are two methods by which you can designate the form to launch when F8 is pressed: 1) via the User Options form, which is accessed by selecting User Options in the Options menu of the main menu or, 2) by selecting the form in the main menu and then selecting the Select as F8 Jump-to Form option from the Items menu or the shortcut menu (right mouse click).
To activate the hot key form, just press the F8 key from anywhere on a form (cannot be activated from the main menu). Once pressed, the designated hot key form is opened, allowing you to use the form as needed, such as view, add, or modify information as necessary. Once you exit the hot key form, you are returned to your original form.

Related information

- [System Forms](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms)

- [Form Menu Options](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-menu-options)

- [Keyboard Shortcuts for Moving Through Form Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/keyboard-shortcuts-for-moving-through-form-fields)

- [Shortcut Keys](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/shortcut-keys)

- [Date Field Shortcuts](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/date-field-shortcuts)

- [Toolbar Options](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/toolbar-options)

- [Status Bar](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/status-bar)

- [Record Deletion](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/record-deletion)

- [Batch Processing](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/batch-processing)

- [Email a Deep Link to a Record](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/email-a-deep-link-to-a-record)

- [About the Form Properties form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-form-properties-form)

- [Associate a Report with a Form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/associate-a-report-with-a-form)

- [About the Field Properties Form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-field-properties-form)

- [Field Validation](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/field-validation)

- [Schedule Data Changes for Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/schedule-data-changes-for-fields)

- [Search Form Records](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/search-form-records)

- [Group Custom Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/group-custom-fields)

- [Add a Standard Note to a Field](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/add-a-standard-note-to-a-field)

- [Form Grids](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-grids)
