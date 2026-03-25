---
title: "Field Definitions: Field Properties Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-field-properties-form/field-definitions-field-properties-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-field-properties-form/field-definitions-field-properties-form"
---

# Field Definitions: Field Properties Form

The following is a list of field descriptions for the Field Properties form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Field Seq#

Defaults the currently active input; however, you can use the drop-down menu to select any other input on the active form that you wish to work with.

## Form

Defaults the currently active form and cannot be changed.

## Lookup

Enabled only if assigned as a ‘Form Administrator’ in VA User Profile.
Specify the lookup to use for this field. This can be a standard lookup or a user lookup created via UD User Defined Lookups (must have the User Database module).
Note: If this is a standard field, the standard lookup assigned to the field (if applicable) will display as the first entry in the grid. You can change the Load Seq# for a standard lookup, but you cannot change the Active flag or delete the lookup.
To delete a non-standard lookup (i.e. standard and user-defined lookups that were added for the input by a user), select the lookup and press the Delete button. You can also use the Reset button (below the grid); however, this will clear all lookups that you have assigned to the input (except the for the input’s standard lookup).

## Lookups: Title

Display only, the title for this lookup.

## Lookups: Parameters

Enabled only if assigned as a ‘Form Administrator’ in VA User Profile.
Enter the lookup parameters for this input. This will be a list of one or more field sequence numbers from the active form (separated by commas) that are passed to the lookup to determine the selection of records that will display in the lookup form. For example, the lookup for the Phase field in JC Job Phases provides two lookup options: JCJP and JCPM.
The JCJP (Job Phases) lookup has parameters of ‘-1,4’. This tells the lookup to show only records for the current company (represented by ‘-1’) that match the job specified in the Job field (represented by ‘4’, the Job input’s Field Seq #).
The JCPM (Phase Master) has only a parameter of -1, which means the lookup will show all phases for the current company.
Note: To determine a field’s sequence number, press F3 from the field. The Field Seq # is shown above the tab pages in the Field Properties form.

## Lookups: Active

This option allows you to toggle a lookup option on or off.
Check this box to activate this lookup. When checked, this lookup will be activated each time F4 is pressed from the calling input. All lookups, when added to the grid, automatically default as ‘Active’. If multiple lookups are assigned to an input, those that are marked as ‘Active’ will appear as radio button options in the lookup window.
Leave this box unchecked to ‘deactivate’ this lookup (i.e. lookup will not be activated when F4 is pressed from the calling input). If multiple lookups are assigned, those that are marked as ‘inactive’ will not appear as radio button options in the lookup window.

## Lookups: Load Seq#

Enter the load sequence number for this input. The load sequence controls
 the display order of the lookup when multiple lookups are available for an input. For
 example, say you have a Material input with two lookups: HQ Materials and IN Location
 Materials. You want the IN Location Materials lookup to display first and the HQ Materials
 lookup to display second, so you would assign a load sequence of ‘1’ to the IN Location
 Materials lookup and a load sequence of ‘2’ to the Materials. Each option would show as a
 radio button in the lookup, with IN Location Materials listed (and defaulted) first and HQ
 Materials listed second.
 IN Locations    HQ Materials

## System Overrides: Type

The Type drop-down on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Using the drop-down menu, specify the type of default override or leave blank if no override.
Not all types are appropriate for an input. For example, you cannot use types 2 (fixed value) or 3 (variable date) on a radio button input.

- 0-Standard - Select this option to use the standard default for this field. Default will be either blank or a value as determined by coding for that specific field.

- 1-Previous Value - Select this option to default the previous value for this field. For example, if you selected this option for a date field, then each time a new record is added, the date field will default the date entered for the previous record.

- 2-Fixed Value - Select this option to define a specific default value for this field. When you select this option, the system enables the Value field. For example, setting a fixed value of Y for the Stocked in Inventory checkbox in HQ Materials will result in every new material record defaulting the box as checked. When you select this option, the system enables the Value field. 3-Variable Date - Select this option to set up date defaults by entering a specific formula in the Value field (which the system enables when you select this option). Click here for information on using the Value field to enter a formula for a variable date field.

## System Overrides: Value

The Value field on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

The system enables this field when you select 2-Fixed Value or 3-Variable Date from the Type field.
Fixed Value
If you select 2-Fixed Value from the Type field, enter the value to default in this field each time a new record is entered. For example, if a checkbox field, enter Y or N.
Note: Once you enter a value in this field, the system reformats this field to match the formatting for the field that you are modifying. This ensures that the value is entered in a valid format. If you later select a different option from the Type drop-down field, the system reverts this field back to its original formatting.Variable Date
If you select 3-Variable Date from the Type drop-down field, enter the formula to use for defaulting the date in this field each time a new record is added.
The table below lists some formula examples.
FormulaDefault Value
%Tcurrent date (i.e. today's date)
%Ffirst day of the current month
%Llast day of the current month
+5Current date plus 5 days
-5Current date minus 5 days
%F+4 fifth day of the month
%L-55 days prior to the last day of the month

## System Overrides: Skip Input

The Skip Input checkbox on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Initially defaults as null (box shaded green), indicating that no override has been set for the input and that it will use the standard default defined for the input.
Not available in key fields.
Select this checkbox to skip this field during the input process. For example, if you add a new contract and want all items to use the same department, you can check this option for the Department input (in JC Contract Items). Then when entering contract items, the Department input will be skipped, but will default the department from the contract header.
Leave this checkbox unselected if this input should not be skipped during data entry.
Note: You can still access a ‘skipped’ input by clicking on the field with the mouse.

## System Overrides: Show on Form

The Show on Form checkbox on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Initially defaults as null (box shaded green), indicating that no override has been set for the input and that it will use the standard default defined for the input.
Not available in key fields and fields linked to radio buttons.
Check this box to have this input display on the form.
Uncheck this box if you do not want this input to display on the form. This is useful for hiding inputs that you do not use. For example, if you never use the URL input in AR Customers, you can hide it by unchecking this box for that input.

## System Overrides: Include in Form Search

The Include in Form Search checkbox on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Include Form Search checkbox in the Field Properties form, System Overrides tab
Initially defaults as null (box shaded green), indicating that no override has been set for the input and that it will use the standard default defined for the input.
Not available in key fields.
Select this checkbox to include this input in the Search panel (accessed by clicking the icon in the toolbar or selecting Records à Form Search). Adding this input to the form filter (upper section of the Search panel) allows you to filter the records returned to the form based on this input’s values. For example, if you are filtering customer records (AR Customers), you might add the Temporary Customer input to the filter form, then filter records to show only customers with the Temporary Customer box unselected.
Clear this checkbox to remove this input from the Search panel (non-key fields only).
Note: If this input was already excluded from the Search panel by default and you want it to remain excluded, you can leave this checkbox as null (shaded); it is not necessary to clear the checkbox.

## System Overrides: Show in Grid

The Show in Grid checkbox on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Initially defaults as null (box shaded green), indicating that no override has been set for the input and that it will use the standard default defined for the input.
Not available in key fields.
Check this box to display this input on the Grid tab. For inputs having an associated description (e.g. phase, cost type, tax code, etc.), the Description in Grid input is enabled, allowing you to specify whether to show the description and where.
Uncheck this box if you do not want this input to display on the Grid tab. This is useful for hiding inputs that you do not use. For example, if you never use the URL input in AR Customers, you can hide it by unchecking this box for that input.

## System Overrides: Mask Text

The Mask Text checkbox on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Initially defaults to unchecked.
Available only for fields whose Control Type is 'TextBox'. (Click the Property Values tab to view the field's Control Type.) Not available in key fields. Does not mask text in Notes fields.
 Check this box to mask the text in this field by replacing it with asterisks (*). This prevents all users from reading the data in these text fields.
Note: Data will be masked on the Info tab only. Data in the same field on the Grid tab will not be masked. To hide the data in the Grid, [hide the grid column](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-grids). In this case, users can enter the data in the Info tab.
Uncheck this box if text should not be masked.

## System Overrides: Disable Input

The Disable Input checkbox on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Initially defaults to unchecked.
Available only for fields whose Control Type is 'TextBox'. (Click the Property Values tab to view the field's Control Type.) Not available in key fields or custom fields.
Check this box to prevent all users from editing the value in this field. This is useful in cases where, for example, the field has been customized to automatically calculate the value, and you don't want users to change the calculated value.
Uncheck this box to allow users to edit the value in this field. To uncheck the box after having previously checked it:

1.  Select another field on the form and press F3.

1.  In the Field Seq# drop-down, select the disabled field.

1.  On the Systems Override tab, uncheck the Disable Input checkbox and click OK.

## System Overrides: Display 4 digit year

The Display 4 digit year checkbox on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

This field is enabled for date fields using a bDate datatype and for Month fields using a bMonth datatype.
Select this checkbox to display dates or months in this field in a four-digit year format (YYYY). If you enter a date or month using a two-digit month number, the system automatically converts the year to four digits. For example, if you enter a date of 070123, the system converts it to 7/1/2023. If you enter a month of 0623, the system converts it to 06/2023.
Leave this checkbox unselected to display dates in this field in a two-digit format (YY). If you enter a date or month using a four-digit month number, the system automatically converts the year to two digits. For example, if you enter a date of 07012023, the system converts it to 7/1/23. If you enter a month of 062023, the system converts it to 06/23.
Note: If you select this checkbox, the system converts the field's datatype to bLongDate (date fields) or bLongMonth (month fields). The datatype will revert back to bDate or bMonth once you deselect this checkbox.

## System Overrides: Display as Timestamp Note

The Display as Timestamp Note checkbox on the Field Properties form, System Overrides tab.

Note: You must be designated as a Form Administrator in VA User Profile to set this option.

This field is enabled only for Notes fields using a bNotes datatype.
Select this checkbox to enable timestamped notes for this field. When selected, notes entered in this field are saved with a date/time stamp and the login name of the user who entered the note.
Note: Once you select this checkbox, notes entered in the field cannot be edited or deleted. However, if you later deselect this checkbox, you can edit or delete existing timestamped notes.

Leave this checkbox unselected if not using timestamped notes for this field. Notes entered in this field will not include a date/time stamp or the login name of the user who entered the note.
For information about time stamped notes, see [About Timestamping Notes](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/about-timestamping-notes).

## System Overrides: Description in Grid

The Description in Grid drop-down on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Check the Show on Grid box and then use this field to select where the description of the field will display. This field is enabled only if a field has an associated description (e.g. phase, cost type, tax code, etc.) and the Show in Grid box is checked.

- 0-Show in Grid Only – This will add a column to the grid that displays the description of the field.

- 1-Show Above Grid Only – This will add a description of the field above the grid.

- 2-Not Shown – Do not display this input’s description in the grid or above the grid.

Note: Setting this option will not affect the display of this input’s description on the form.
For custom fields, this field is only available if you have associated a custom validation with the field (using UD User Validation). Additionally, you can only select the 1-Show Above Grid Only option.

## System Overrides: Form Label

The Form Label field on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

The system disables this option for radio buttons.
Enter the override label to use for this field on the Info tab, up to 30 characters. You will typically use this field if you want to rename a field. To change the label of the field on the Grid tab, use the Col Heading field.
Note: You can always view the standard label for an input by checking the Standard Field Labels option in the View menu of the selected form, then toggle back to your custom label by unchecking the option.

## System Overrides: Col Heading

The Col Heading field on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

The system disables this option for radio buttons.
Enter the override label to use for this field on the Grid tab, up to 30 characters. You will typically use this you want to name the column differently than the standard name in the software. To change the label for this field on the Info tab, use the Form Label field.
Note: You can always view the standard label for an input by checking the Standard Field Labels option in the View menu of the selected form, then toggle back to your custom label by unchecking the option.

## System Overrides: Setup Form

The Setup Form field on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Specify the setup form to access when F5 is pressed at this input. Typically only used for fields that require valid inputs. For example, if you create a field called “Last Job” in the Vendor Master, and that field is linked to datatype bJob, then you would enter ‘JCCM’ (Job Master) here.
Note: You can also assign custom forms (created in the UD module), if applicable. Make sure you enter the full form name. For example: udFormName.
Note: Although you can assign F5 access to any standard Viewpoint field, the recommendation is that you do not use this functionality to override standard F5 assignments.

## System Overrides: Setup Parameters

The Setup Parameters field on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Enabled only for custom inputs (i.e. those created via VA Custom Fields Wizard or on a custom form created in User Database).
Enter the setup parameters for this input. The setup parameters tell the program how to select a set of records for the form to display. First, you will always need to include the company in the setup parameters. This is entered as -1 to indicate current company. Then, you will need to enter the sequence number of the field from which you will be calling the setup form. The sequence number is shown in the Field Seq# input above the tab pages in the Field Properties form.
For example, you add a custom ‘name’ field to a form and you want to point that field to the PR Employees setup form. Your custom field has a Field Seq# of ‘5000’. To assign the PR Employees form as the Setup form, you would enter the information as follows:
Form:    PREmpl
Parameters:  -1,5000
Now when F5 is pressed from your custom field, it will automatically open the PR Employees form. Upon exiting the PR Employees form, you will be returned to the calling form and field.
Note: If you associate a custom field with a setup form, you will typically want to also assign an F4 lookup that provides a list of valid records from the setup form.

## System Overrides: Assign to Tab

The Assign to Tab drop-down on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Enabled only for custom inputs (i.e. those created via VA Custom Fields Wizard or on a custom form created in User Database).
Using the drop-down menu, select the tab on which to display this input.

## System Overrides: Status Text

The Status Text field on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Enabled only for custom inputs (i.e. those created via VA Custom Fields Wizard or on a custom form created in User Database).
Enter a brief description of the information needed for the selected custom field, up to 60 characters. Entry here will display in the status bar (bottom of screen) whenever focus is in this field.

## System Overrides: Value is Required

The Value is Required checkbox on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Check this box if users should be required to enter a value in this field. When this box is checked, users will not be able to save new records unless there is a value in this field.
This field is disabled on radio buttons and standard fields that are already set up as required.
Initially defaults as null (box shaded green), indicating that no override has been set for the input and that it will use the standard default defined for the input.
Note: If you set this input as ‘required’ here, the Value is Required option on the User Overrides tab will be disabled.

## System Overrides: Level

The Level drop-down on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Select how the validation procedure set up using the Procedure, Parameter, Min Value, Max Value, Expression, and Error Message fields will be applied to the form:

- 0-No Warning, Allow Save — Select this option if you do not want a field validated, but want a description to be returned. You must specify a validation procedure and parameters, but no validation will actually occur. Instead, when an ‘invalid’ entry is made, the validation procedure returns the ‘error’ description and displays it to the right of the input field, and the cursor moves to the next field. No error message window is displayed.Example: Job #: 12345 “Not a valid Job!”
If the input field does not have a Description label (display only box next to field), then no description will be returned, regardless of the validation option.

- 1-Warning, Allow Save — Select this option to display a warning message but allow the entry to be saved.

- 2-Show Error, Disallow Save — Select this option to display a warning message and not allow the entry to be saved. Once the error message is displayed, the cursor moves to the next field. However, when you try to move to a new record or exit the form, the error message is redisplayed and you must enter a valid input or undo the entry.

- 3-Show Error, Stay on Input — Select this option to display a warning message and remain on the input until a valid entry is made.

Note: The selection in this field does not override the Value is required field. For example if you select the Value is required checkbox and you select No warning, allow save in the Level field, an entry in the field is still required, but the validation set up using the Procedure and Parameters fields will not keep the user from saving the record.

## System Overrides: Procedure

The Procedure field on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Enter a custom validation procedure created using the UD User Validation form, or press F4  to select one from a list. The lookup will not include standard validation procedures.
Tip: You cannot assign standard validation procedures (those created by Viewpoint Construction Software) to standard or custom fields. However, if you own the UD module, you can create a validation procedure using the UD User Validation form.
Once you have selected a validation procedure, click the Link button to map stored procedure parameters to the corresponding fields on the form.

### Why doesn't my validation procedure display in the lookup?

If you created a validation procedure using the UD User Validation form but it does not display in the lookup list, it's possible that you did not initialize and/or compile the procedure.

1. Open the UD User Validation form and open the SQL tab.

1. If SQL code does not display in the field, click the Initialize button. The SQL code will populate in the field.

1. Click the Compile button.

1. Click Save () to save your changes.

1. Return to the Field Properties form and press F4 in the Procedure  field. The validation procedure should now display in the lookup.

Related concepts

- [About the UD User Validation Form](/en/vista/vista/administration/user-database/custom-validation-procedures/about-the-ud-user-validation-form)

- [About the Field Properties Form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-field-properties-form)

## System Overrides: Parameters

The Parameters field on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Specify the input parameters for the validation procedure. This will typically include the sequence number of the field being validated, as well as the sequence numbers of any fields the validation routine needs to accomplish the validation.
Note: If you mapped stored procedure parameters to corresponding fields on the form using the Validation Field Linking form (accessed by clicking the Link button above), this field defaults the defined parameters.
When manually entering parameters, make sure you enter the sequence numbers in the order that the validation routine is expecting them. For example, in HR Resources, the validation procedure for SSN (Social Security Number) uses the following parameters:
-1,5,2,80
In this example, ‘-1’ represents the currently active company, ‘5’ is the sequence number for the PR Co # field, ‘2’ is the sequence number of the Resource # field, and ‘80’ is the sequence number of the SSN# field. The validation procedure will use the values in the specified fields to ensure the SSN is valid for the current HR company, the specified PR Co, and Resource (i.e. the SSN is not assigned to another resource).
Note: If you are passing static (constant) values to the validation procedure, they must be in single quotes (e.g. ‘N’).

## System Overrides: Min Value

The Min Value checkbox on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Optional. Used for numeric fields only.
Enter the minimum value allowed for this input or leave blank if no minimum value is required. For example, if the input requires a value between 1 and 255, the minimum value would be ‘1’.
Note: Validation will check the minimum/maximum values before implementing the validation procedure. If the entry is outside the specified minimum/maximum range, an error is returned and the validation procedure is not executed.

## System Overrides: Max Value

The Max Value field on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Optional. Used for numeric fields only.
Enter the maximum value allowed for this input or leave blank if no maximum value. For example, if the input requires a value between 1 and 255, the maximum value would be ‘255’.
Note: Validation will check the minimum/maximum values before implementing the validation procedure. If the entry is outside the specified minimum/maximum range, an error is returned and the validation procedure is not executed.

## System Overrides: Expression

The Expression field on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Use this field to use a regular expression to validate the field - for example you can use the following regular expression to validate an email address field:
\w[-._\w]*\w@\w[-._\w]*\w\.\w{2,3}
Click on a link below for more information about writing regular expressions.
[http://regexlib.com/DisplayPatterns.aspx](http://regexlib.com/DisplayPatterns.aspx)
[http://etext.virginia.edu/services/helpsheets/unix/regex.html](http://etext.virginia.edu/services/helpsheets/unix/regex.html)
[http://www.codeproject.com/KB/dotnet/regextutorial.aspx](http://www.codeproject.com/KB/dotnet/regextutorial.aspx)

## System Overrides: Error Message

The Error Message text box on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Enter the error message to return if the validation fails, up to 255 characters.

## System Overrides: Input Seq #

The Input Seq # field on the Field Properties form, System Overrides tab.
Note: You must be designated as a Form Administrator in VA User Profile to set this option.

Enabled only for custom inputs (i.e. those created via VA Custom Fields Wizard or on a custom form created in User Database).
Specify the input sequence for this input. The input sequence determines the order in which the cursor moves to an input (e.g. a sequence of 5 means the input will be the 5th input accessed when tabbing or entering through the inputs). You may want to consider initially assigning a number that will set the input as last in the input order (e.g. 999). You can then use the Set Order option that is available on the form (Tools à Input Order à Set Order) to reset the input order. The Set Order option shows the sequence number of all inputs on the form, and allows you to manually set the order for each input, including custom inputs. You will need to first select the desired tab before accessing the Set Order function.
Note: Make sure you do not assign a sequence to more than one input. If you decide to assign a sequence that is already assigned to another input, make sure you reassign the sequence for that input.

## User Overrides: Type

Using the drop-down menu, specify the type of default override or leave blank if no override.
Note: Not all types are appropriate for an input. For example, you cannot use types 2 (fixed value) or 3 (variable date) on a radio button input.

- 0-Standard - Select this option to use the standard default for this field. Default will be either blank or a value as determined by coding for that specific field.

- 1-Previous Value - Select this option to default the previous value for this field. For example, if you selected this option for a date field, then each time a new record is added, the date field will default the date entered for the previous record.

- 2-Fixed Value - Select this option to define a specific default value for this field. When you select this option, the system enables the Value field. For example, setting a fixed value of Y for the Stocked in Inventory checkbox in HQ Materials will result in every new material record defaulting the box as checked. When you select this option, the system enables the Value field. 3-Variable Date - Select this option to set up date defaults by entering a specific formula in the Value field (which the system enables when you select this option). Click here for information on using the Value field to enter a formula for a variable date field.

## User Overrides: Value

The system enables this field when you select 2-Fixed Value or 3-Variable Date from the Type field.
Fixed Value
If you select 2-Fixed Value from the Type field, enter the value to default in this field each time a new record is entered. For example, if a checkbox field, enter Y or N.
Note: Once you enter a value in this field, the system reformats this field to match the formatting for the field that you are modifying. This ensures that the value is entered in a valid format. If you later select a different option from the Type drop-down field, the system reverts this field back to its original formatting.Variable Date
If you select 3-Variable Date from the Type drop-down field, enter the formula to use for defaulting the date in this field each time a new record is added.
The table below lists some formula examples.
FormulaDefault Value
%Tcurrent date (i.e. today's date)
%Ffirst day of the current month
%Llast day of the current month
+5Current date plus 5 days
-5Current date minus 5 days
%F+4 fifth day of the month
%L-55 days prior to the last day of the month

## User Overrides: Skip Input

Initially defaults as null (box shaded green), indicating that no override has been set for the input and that it will use the standard default defined for the input.
Check this box to skip this field during the input process. For example, if you add a new contract and want all items to use the same department, you can check this option for the Department input (in JC Contract Items). Then when entering contract items, the Department input will be skipped, but will default the department from the contract header.
Uncheck this box if this input should not be skipped during data entry.
Note: You can still access a ‘skipped’ input by clicking on the field with the mouse.

## User Overrides: Show on Form

Initially defaults as null (box shaded green), indicating that no override has been set for the input and that it will use the standard default defined for the input. (Note: This option is disabled for key fields and fields linked to radio buttons.)
Check this box to have this input display on the form.
Uncheck this box if you do not want this input to
 display on the form. Useful for hiding inputs that you do not use. For example, if you
 never use the URL input in AR Customers, you can hide it by unchecking this box for that
 input.
IMPORTANT: This option is not intended to be used as a security feature. Users can reset hidden fields to show even if they have been hidden by the system administrator.

## User Overrides: Show in Grid

Initially defaults as null (box shaded green), indicating that no override has been set for the input and that it will use the standard default defined for the input.
Check this box to display this input on the Grid tab. For inputs having an associated description (e.g. phase, cost type, tax code, etc.), the Description in Grid input is enabled, allowing you to specify whether to show the description and where.
Uncheck this box if you do not want this input to
 display on the Grid tab.Useful for hiding inputs that you do not use. For example, if
 you never use the URL input in AR Customers, you can hide it by unchecking this box for
 that input.

## User Overrides: Description in Grid

Initially defaults as null (box shaded green), indicating that no override has been set for the field and that it will use the standard default defined for the input.
Enabled only for inputs having an associated description (e.g. phase, cost type, tax code, etc.) where the Show in Grid option is checked.
Using the drop-down menu, specify where to display the description for this field or leave blank if no override.

- 0-Show in Grid Only – Display this input’s description in the grid only. Description will display to the right of the input.

- 1-Show Above Grid Only – Display this input’s description above the grid only. Description will display above grid where space allows.

- 2-Not Shown – Do not display this input’s description in the grid or above the grid.

Note: Setting this option will not affect the display of this input’s description on the form.
For custom fields, this field is only available if you have associated a custom validation with the field (using UD User Validation). Additionally, you can only select the 1-Show Above Grid Only option.

## User Overrides: Value is Required

Disabled for fields that are designated as ‘required’ by Viewpoint or on the System Overrides tab. Also disabled for radio buttons.
Initially defaults as null (box shaded green), indicating that no override has been set for the input and that it will use the standard default defined for the input.
Check this box if entry in this input is required. If user tries to move off the input without entering a value, they will get a message indicating an entry is required in that field. Once the user clicks OK to the message, the cursor will move off the input; however, the record will not be saved unless the required value is entered.
Do not check this box if entry in this input is not required.
