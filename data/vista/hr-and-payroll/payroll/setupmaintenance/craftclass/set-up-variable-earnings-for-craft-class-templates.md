---
title: "Set Up Variable Earnings for Craft Class Templates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-variable-earnings-for-craft-class-templates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-variable-earnings-for-craft-class-templates"
---

# Set Up Variable Earnings for Craft Class Templates

You can use the Variable Earnings tab in PR Craft Class
 Templates to override variable earnings set up in PR Craft Classes.
Variable earnings override the pay rate calculations and are used when the pay rate times the earnings factor will not produce a desired rate.
For example: Shift 1 pays $10/hour for straight time and $15/hr for time and a half, whereas Shift 2 pays $12/hr for straight time and $15/hr for time and a half. Shift 1 can use the pay rate and factor to calculate the proper rate, and no variable earnings are needed. However, Shift 2 overtime is not 1.5 times its straight time pay rate, so variable earnings must be set up to override the standard calculation.
When you enter timecards, the system will compare the variable overtime rates set up on this the Variable Earnings tab to the employee's rate. The system will only use the variable overtime rate if it is the higher of the two rates. If you are using variable rates and auto-overtime, the system calculates the overtime rate using what is set up at the craft/class level.
Important: Variable earnings defined at the craft template, craft/class, or craft levels (as applicable) do not need to be set up in PR Craft Class Templates unless you are overriding the existing rate(s). If you do not override an existing rate here, the rate defined at the next hierarchical level will be used (i.e. craft template rates override craft class rates). If you want a specific rate excluded from calculations, set it up here with a 0.00 amount. (Note: Requiring only override rates to be defined here eliminates having to update multiple levels each time a rate change occurs.)
The following instructions detail how to set up variable earnings for craft class templates.

1. Enter a shift number in
 the Shift field.

1. Enter a valid earnings
 code in the Earn Code field. Press
 F4 to select from a list of earnings codes. The system defaults
 information in the Description and Method fields.Note: Do not specify an add-on earnings on
 this tab.

1. Enter rates in the
 Old
 Rate and New Rate fields. The system
 uses the effective date specified in PR Crafts or PR Craft Templates to
 determine which rate is used. The old rate is used for timecards entered prior
 to the effective date and the new rate for timecards entered on or after the
 effective date.

1. Save the record as normal.

Related information

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [About the PR Craft Templates Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-templates-form)

- [About the PR Craft Class Templates Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-class-templates-form)
