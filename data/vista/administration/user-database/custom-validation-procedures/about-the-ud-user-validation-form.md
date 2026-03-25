---
title: "About the UD User Validation Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/custom-validation-procedures/about-the-ud-user-validation-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/custom-validation-procedures/about-the-ud-user-validation-form"
---

# About the UD User Validation Form

Use this form to create validation procedures that can be
 attached to any non-validated field, standard or custom (user-defined).
Once created, validation procedures are assigned to the
 appropriate fields using the [Field
 Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form) form (System Overrides tab, Validation section).

## Configuring Validation Parameters

Creating validation parameters enables the
 system to compare data entered into a field against existing data in a table or
 another field. Validation parameters are configured using the grid on the
 Parameters tab. Each line on the grid is used for a single parameter and must be
 tied to the validating table. Only tables, and their columns, specified on the
 Tables tab can be entered on the Parameters tab.
Additionally, a validation
 comparison must be established. Generally, there are three comparisons that are
 used: parameter to column, column to value, and parameter to value. When setting
 a comparison by column, the stored procedure looks for a specific column and
 validates the input against existing records. When setting a comparison by
 value, the stored procedure looks for a specific value in the input field. Click
 the links below for additional information on both validation comparisons.
The following provides additional information:

- Parameter to Column - Generally, when setting this comparison, the Type (Left
 side) field is set to Parameter. Since the parameter acts as a place holder, any
 value can be entered into the Parameter/Column Name field; when assigned to a
 field, the place holder is replaced with the comparison value. Typically, when
 the Type (Left side) field is set to Parameter, the Type (Right side) field is
 set to Column and the column name is specified in the Column Name field. Speak
 to your system administrator for any other configurations.

- Column to Value - Generally, when setting a comparison by value, the Type (Left
 side) field is set to Column. Enter the column name into the Column Name field.
 Typically, when the Type (Left side) field is set to Column, the Type (Right
 side) field is set to Value and the value is specified in the Value field.

## Comparing Parameters to Values

In rare cases, a parameter can be compared to a value.
Generally, when setting this comparison, the
 Type (Left side) field is set to Parameter. Since the parameter acts as a place holder,
 any value can be entered into the Parameter/Column Name field; when assigned to a field,
 the place holder is replaced with the comparison value.
When creating a validation comparison, the
 Operator field is used to determine how the system compares the left and the right
 sides. For more information, refer to the [F1 help](/en/vista/vista/administration/user-database/custom-validation-procedures/about-the-ud-user-validation-form/field-definitions-ud-user-validation-form#ID-000478df--en) for
 the Operator field.
The following example displays how a parameter might
 be set up. In this example, the stored procedure will compare the input against the
 Job column in the JCJM (JC Jobs) table.
Table Name
Seq
And/Or
Type (Left side)
Parameter/Column
 Name
Operator
Type (Right side)
ColumnName
Value

JCCM
1

Parameter
Job
=
Column
Job

When specifying more than one parameter, use
 the And/Or field to specify the logical operators that determine the set of conditions
 for validation. Expanding on the previous example, the job validation procedure might
 require that the job entered in the input field must be a valid, active job. In this
 instance, another parameter would be added with an "and" operator, specifying that the
 Active field/column in JCCM has been set to Yes.
Table Name
Seq
And/Or
Type (Left side)
Parameter/Column
 Name
Operator
Type (Right side)
ColumnName
Value

JCCM
1

Parameter
Job
=
Column
Job

JCCM
2
And
Column
Active
=
Value

Y

Note: Typically, an And/Or operator is not assigned to the
 first sequence.
Click [here](/en/vista/vista/administration/user-database/custom-validation-procedures/about-the-ud-user-validation-form/field-definitions-ud-user-validation-form#ID-000477be--en) for more
 information and a complete list of operators.

Related information

- [About the Field Properties Form](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form)

- [System Overrides: Procedure](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form/field-definitions-field-properties-form#ID-0004cb41--en)

- [Create a Validation Procedure](/en/vista/vista/administration/user-database/custom-validation-procedures/create-a-validation-procedure)

- [Assign a Validation Procedure](/en/vista/vista/administration/user-database/custom-validation-procedures/assign-a-validation-procedure)
