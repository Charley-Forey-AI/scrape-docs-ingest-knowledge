---
title: "Field Definitions: SM Pay Type Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-pay-types-form/field-definitions-sm-pay-type-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-pay-types-form/field-definitions-sm-pay-type-form"
---

# Field Definitions: SM Pay Type Form

The following is a list of field descriptions for the SM Pay
 Type form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Pay Type

Enter a pay type code to represent the pay level you are setting up.
Some examples of pay types might be:

- REG (Regular time)

- OT (Overtime)

- DT (Double-time)

- HOL (Holiday pay)

- AH (After hours pay)

## Description

Enter a description of this pay type. Up to 60 characters allowed.

## Cost Method

Select the cost method for labor rate calculations when entering work completed labor lines referencing this pay type on a work order (in SM Work Orders, Work Completed tab).

- Multiplier - Select this method to calculate labor
 rates for work completed based on the pay rate defined for the technician who
 performed the work and a rate multiplier (specified in Factor
 field below). For example, if the technician's pay rate is $35.00 and the factor is
 1.50, the calculated Cost Rate for the work completed
 labor line will be $52.50 (35.00 x 1.5).

- Dollar Rate - Select this method to specify a flat
 pay rate (in the Rate/Amount field below) to use
 when calculating estimated labor costs on a work order. This rate overrides the pay
 rate defined for the technician (in SM Technicians), and will default as the
 Cost
 Rate when entering work completed labor lines on a work order.

## Factor or Rate/Amount

If you select 0-Multiplier from the Cost Method
 drop-down, this field's name displays as "Factor." In this case, use this field to enter
 the rate multiplier for this pay type. For example, enter 1.00 for regular time, 1.5 for
 time and one/half, 2.00 for double-time, etc.
Note: The system multiplies the technician's pay rate by
 this value to determine the Cost Rate for work completed labor
 entries (SM Work Orders).
If you select 1-Dollar Rate
 from the Cost
 Method drop-down, this field's name displays as "Rate/Amount." In this case,
 use this field to enter the override pay rate for this pay type.
Note: The amount entered in this field will be used instead of the technician's standard pay rate (defined in SM Technicians).

## Earnings Code

Enter earnings code to use as the default when entering timesheets or timecards (in PR My Timesheet or PR Timecard Entry, respectively) that reference this pay type.
Note: The earnings code entered here must be a valid
 timesheet earnings code (i.e. the Include in Remote Timesheet Entry box is
 checked for the earnings code in PR Earnings Codes). Press F4 for a list of valid timesheet
 earnings codes.

## Active

Check this box to activate this pay type. Once activated, you can assign this pay type to work completed labor entries on a work order (in SM Work Orders, Work Completed tab). In addition, this pay type will be included in pay type lookups.
Uncheck this box to deactivate this pay type. Pay type will not be available for assignment to work completed labor entries in SM Work Orders, nor will it be included in pay type lookups.
