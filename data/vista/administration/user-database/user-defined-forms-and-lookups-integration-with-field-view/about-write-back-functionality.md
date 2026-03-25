---
title: "About Write-back Functionality | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/user-defined-forms-and-lookups-integration-with-field-view/about-write-back-functionality"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/user-defined-forms-and-lookups-integration-with-field-view/about-write-back-functionality"
---

# About Write-back Functionality

Note how UD forms that have been converted write back from Field View to Vista.
Valid FieldsThe following Field View form fields will write back to Vista. Fields other than the following will not.

- Text

- Dates

- Numeric

- Predefined Answers (Lookups and Combo Box fields)

- checkboxes

Note: For Combo Box fields in Vista, when the Input is Combo Box, the Input Type must be Text in order for write-back to be supported.
Company Based FormsFor Company Based forms, a "Vista Company" predefined answer field is added to the Field View form template.Field View Form reference numbersTo write back the Field View Form reference number to Vista, set up a field in the UD Form titled FieldViewFormReferenceNumber (must be exact) with a column control type of Textbox and input type of Text.Auto-incrementing Keys

- For a UD form with "Key" columns that are type "1-Auto value only" or "2-Auto value, but allow entry", if the form is converted to a Field View form template, the Key columns will be not be shown in Field View.

- When the form data is saved to Vista, the Key column will be auto-incremented.

Manually entered KeysManually entered Keys appear as required fields in Field View.Text Fields

- In Field View, the length of text fields is not constrained.

- After write-back to a UD form, if the text in a Field View form field exceeds the width of the corresponding UD form field in Vista, the text will be truncated.

Number FieldsDuring writeback, if the value returned to Vista is

- a decimal, it will be rounded to fit the Vista type.

- larger than the Vista field type allows, it will fail to save.

Date Fields

- Date and Month control type UD fields are both converted to date fields in Field View.

- When data from a Month field is saved to Vista, only the month part of the field is saved.

Field View Location

- When a UD form is converted to Field View, a Location field is added to the form.

- When form data is saved to Vista, the Location field is ignored.
