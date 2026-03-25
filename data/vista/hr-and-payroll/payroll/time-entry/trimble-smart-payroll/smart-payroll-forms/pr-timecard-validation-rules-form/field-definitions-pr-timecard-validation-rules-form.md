---
title: "Field Definitions: PR Timecard Validation Rules Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-validation-rules-form/field-definitions-pr-timecard-validation-rules-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-validation-rules-form/field-definitions-pr-timecard-validation-rules-form"
---

# Field Definitions: PR Timecard Validation Rules Form

The following is a list of field descriptions for the PR Timecard Validation Rules form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Rule

The Rule field on the PR Timecard Validation Rules form.
This field is display only, and shows the name of the validation rule. Rules are as follows:

- Daily hours variance rule - Checks if work hours in a day exceed a specified threshold for variance.

- Minimum wage compliance rule - Checks that an employee's pay rate is not below the state-mandated minimum wage.

- Multiple site detection rule - Checks time in/out for an employee working multiple sites to ensure no overlapping times.

- New state or local code rule - Detect new state and local codes in employee timecard record.

- Pay period hours variance rule - Checks if work hours in a pay period exceed a specified threshold for variance.

- Pay rate validation rule - Cross-references each employee's timecard with their employment record to ensure the pay rate aligns with their designated position and contract agreement.

 Validation rules are predefined; you cannot add, edit, or delete them. You can, however, use the Enabled checkbox to activate the rule so it will be included when checking timecards for discrepancies before they are posted.
Note: Each rule's parameters (Parameters tab) are used in determining whether discrepancies exist in the timecard batch. The value you specify for each parameter determines how the system uses historical data when performing timecard validations. For more, see the [Value](/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-validation-rules-form/field-definitions-pr-timecard-validation-rules-form#concept-b61bdc6f-aa97-4ba3-94c5-64e776dd2a0e--en) F1 Help.

## Description

The Description field on the PR Timecard Validation Rules form, Info tab.
This field is display only and shows a detailed description of the selected rule, describing what the rule does when implemented.

## Enabled

The Enabled checkbox on the PR Timecard Validation Rules form, Info tab.
Select this checkbox to enable the specified rule. Once enabled, the system includes the rule when checking timecards for discrepancies (in PR Timecard Entry). If a discrepancy is found, the severity level for the rule determines the action to take.
Leave this checkbox unselected to exclude this rule from timecard validation/compliance checks.

## Severity

The Severity dropdown on the PR Timecard Validation Rules form, Info tab.
Choose the severity level for the selected rule. The severity level selected here determines how timecard discrepancies are handled when they are encountered in a timecard batch.

- Allowed No Warning - If this option is selected, the system does not warn you when discrepancies are found in the timecard batch, and allows you to post the batch.

- Allowed With Warning - If this option is selected, the system warns you when discrepancies are found in the timecard batch, and allows you to either accept the discrepancies or correct them, before you post the batch.

- Not Allowed - If this option is selected, the system warns you when discrepancies are found in the timecard batch, but will only allow you to post the batch once you have corrected the errors.

## Name

The Name field on the PR Timecard Validation Rules form, Parameters tab.
This field is display only and shows the name of the parameter.
Parameters are predefined; you cannot add, edit, or delete them. You can, however, use the Value field to set the parameter value.

## Description

The Description field on the PR Timecard Validation Rules form, Parameters tab.
This field is display only and shows a detailed description of the parameter.

## DataType

The DataType field on the PR Timecard Validation Rules form, Parameters tab.
This field is display only and shows the datatype (for example, Integer).

## Value

The Value field on the PR Timecard Validation Rules form, Parameters tab.
Enter the value for the selected parameter.
Look back monthsEnter the number of months of historical data to use when performing timecard validations. For example, if you want the system to use 12 months of historical data, enter 12 as the value.Tolerance FactorIndicate how much a validated record can vary from its usual historical average before it is flagged for review.

- 1 = Low - Slightly Off (minimal deviation). This allows for the typical, everyday ups and downs. Most normal timecards fall within this range. If a timecard falls outside this range, it is unusual, but not alarmingly off.

- 2 = Medium - Noticeable Off (moderate deviation). This allows for almost all of the usual variations in hours (about 95% of normal timecards). Timecards that fall outside this range are rate and will require a closer look, since it is likely not a normal variation.

- 3 = High (recommended) - Significantly Off (major deviation). This covers almost all conceivable normal variations (about 99.7% of timecards). Timecards that go beyond this are extremely uncommon and are very likely a mistake, an outlier, or something that requires attention.
