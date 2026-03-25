---
title: "Field Definitions: UD User Validation Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/custom-validation-procedures/about-the-ud-user-validation-form/field-definitions-ud-user-validation-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/custom-validation-procedures/about-the-ud-user-validation-form/field-definitions-ud-user-validation-form"
---

# Field Definitions: UD User Validation Form

The following is a list of field descriptions for the UD User
 Validation form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Validation Procedure

 Enter a name for your validation procedure, up to 27 characters. The name must be entered without any spaces. After tabbing off this field, the system automatically assigns a prefix to the lookup name (“usp”), identifying it as a user-created validation procedure (for example, uspCompanyVehicles).

##  Description

 Enter a description of your validation procedure, up to 30 characters.

## Table Name

Enter the table/view that applies to the
 procedure or press F4 to select one from a list.
You can add more tables/views to the validation by adding more records to the Tables tab.

##  Error Message

 Enter the message that displays when an invalid entry is made. Up to 255 characters are allowed.
 For example, “Invalid XXX,” where XXX represents the input that is being validated.

##  Description Column

 Specify which column from the specified table contains the description of the validated value. Press F4 for a list of column names for the table.
 For example, if the validated input is “Employee”, and “SortName” is specified as the description column, the employee’s name is pulled from the “SortName” column and displayed to the right of the employee number.

##  And/Or

Note: Use these operators only if multiple conditions exist in the validation procedure.
 Specify the logical operator that determines the set of conditions to be validated.You will typically not assign an operator to the first sequence of the validation procedure. Options are as follows:

 (
 And
 Or
 Not

 )
 And(
 Or(
 Not(

 )And
 )Or
 )Not

Note: The “Not” operators, though listed, are not currently available for use; they will be available for use in a future enhancement.
 Use the parentheses to group conditions together. Use “And” operators when more than one condition must be true, and “Or” operators when either condition can be true.
 For example, using A, B, and C to represent conditions:
Scenario 1 – If A and B and C must be true:
Seq
And/Or
Param/Col

 1

 A

 2
 And
 B

 3
 And
 C

Scenario 2 – If A or B or C must be true:
Seq
And/Or
Param/Col

 1

 A

 2
 Or
 B

 3
 Or
 C

Scenario 3 – If (A and B) or C must be true:
Seq
And/Or
Param/Col

 1
 (
 A

 2
 And
 B

 3
 )Or
 C

Scenario 4 – If A and (B or C) must be true:
Seq
And/Or
Param/Col

 1

 A

 2
 And(
 B

 3
 Or
 C

Note: In scenario 4, the closing parenthesis will be added automatically during compilation.

##  Type (Left side)

 Specify whether the first part of the validation comparison is a parameter or column.

- Parameter - Use this type when the procedure must compare a form field to a specific column or value. If you select this option, enter a value in the Parameter/Column Name field. Enter any value, as it is simply acting as a place holder for the parameter. When you assign this parameter to a field, the system replaces the place holder with the comparison value. When you select this option, you should select Column from the Type (Right side) field. For example, if you want to validate a Job code, select Parameter for this field, Column for the Type (Right side) field, and enter "Job" in the Column Name field.

- Colum - This this type when the procedure must look for a specific value. If you select this option, enter the column name in the Parameter/Column Name field. You will use this situation where a Y/N, On/Off, or other type of flag condition must be met. When you select this option, you should select Value for the Type (Right side) field. For example, if the Job validation includes a condition that only allows open jobs, select the Column option, enter the column name in the Parameter/Column Name field, select Value in the Type (Right side) field, and enter 1 in the Value field.

##  Parameter/Column Name

 When “Parameter” has been specified in the Type (Left side) field, enter a value for the parameter. Any value is acceptable, as it is simply acting as a place holder for the parameter (which will be later substituted for a form input sequence.
 When “Column” has been specified in the Type (Left side) field, enter the column name that the input is validated against.

##  Operator

 Specify the operator that will be used to compare the second part of the comparison with the first part.
= Equal to
< Less than
> Greater than
<= Less than or equal to
>= Greater than or equal to
<> Not equal to

##  Type (Right side)

 Specify whether the second part of the validation comparison is a column or value.

- Column - Use this type when the stored procedure must locate a specific column in the table and validate input against existing records. If this option is selected, enter the column name in the ColumnName field. Typically, when this option is selected, “Parameter” should be selected for the Type (Left side) field. For example, if you want to validate a Job code, select “Parameter” for the Type (Left side) field, “Column” for this field, and enter “Job” in the Column Name field.

- Value - Use this type when the procedure must validate a specific value in a column or parameter. This option is most often used for “Y/N”, “On/Off”, or other types of “flag” conditions. Enter the specific value in the Value field. For example, if the Job validation includes a condition that only open jobs are valid for input, select “Column” in the Type (Left side) field, enter the column name in the Parameter/Column Name field, select “Value” in this field, and enter “1” in the Value field.

##  ColumnName

 This field is only available when “Column” has been selected in the Type (Right side) field.
 Indicate which column the validation
 procedure uses when validating an entry based on this sequence’s validation comparison.
 Press F4
 for a list of valid columns for the specified table.

##  Value

 This field is only available when “Value” has been selected in the Type (Right side) field.
 Indicate the value for this validation sequence. The input must match this value in the specified table in order for the entry to be allowed. For example, if validating the job status where only open jobs are valid, enter “1” as the value. When the job code is validated, the procedure looks to see if the job is flagged as “1” (Open). All other entries cause an error to display.
