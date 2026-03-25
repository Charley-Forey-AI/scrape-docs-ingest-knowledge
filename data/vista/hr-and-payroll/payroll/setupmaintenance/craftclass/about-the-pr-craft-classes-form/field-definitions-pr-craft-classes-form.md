---
title: "Field Definitions: PR Craft Classes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form/field-definitions-pr-craft-classes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form/field-definitions-pr-craft-classes-form"
---

# Field Definitions: PR Craft Classes Form

The following is a list of field descriptions for the PR Craft Classes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Craft

Craft field on the PR Craft Classes form.
 Enter a valid craft code (set up in PR
 Crafts) or press F4 to select from a list of valid craft codes.

Related information

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

## Class

Class field on the PR Craft Classes form.
 Enter a class code that will be used to identify the type of work within the craft, up to 10 characters.
 You must set up a separate class for each pay rate. For unions, this would typically be the code for Journeyman, Foreman, Apprentice, etc.

Related information

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Description

 Description field on the PR Craft Classes form, Info tab.
Enter a description for this class, up to 30 characters.

Related information

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Use Weighted Average Overtime Rates

The Use Weighted Average Overtime Rates checkbox
 on the PR Craft Classes form, Info tab.
 Select this checkbox to use weighted-average
 overtime rates when applying auto overtime to timecards posted to this craft/class. Because
 this option is used in conjunction with the Use Weighted Average Overtime Rates option in JC Jobs, you must also check
 this option for each job to which this craft/class applies.
Once you select this checkbox, the Average By field is
 enabled, and you must select the weighted-average overtime calculation
 method (Week or Day). When the system applies auto overtime to timecards
 posted to jobs, crafts, and classes for which both Use Weighted Average Overtime
 Rates options are selected, the system uses a
 weighted-average overtime rate adjustment based on the Average By
 calculation method you selected. If both options are not selected, regular
 overtime rates are used.
 Do not select this checkbox if you are using regular overtime rates.
For more information about weighted-average overtime rates, see [Weighted Average Overtime Rates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime/weighted-average-overtime-rates).

Related information

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Average By

The Average By field on the PR Craft Classes form, Info
 tab.
This field is only enabled when you select the Use weighted average overtime rates checkbox.
Select the option to use for calculating weighted average auto overtime:

- Week (Default) - Calculate weighted average overtime based on the employee's weighted-average regular rate for the weekly or bi-weekly pay period.

- Day - Calculate weighted average overtime based on the employee's weighted-average regular rate for the day.

Note: It is suggested that the option you select here be assigned to each
 applicable job (in JC Jobs) associated with this craft/class to ensure the correct
 weighted average overtime rate is used. If you set one option to Weekly and one to
 Day, the systems uses the daily weighted-average rate.

## EEO Class

 EEO Class field on the PR Craft Classes form, Info tab.
Enter an EEO class to be on the PR Monthly Employment Utilization Report or PR Certified Export - eMars (ReportID 1315, U.S. only).
The three standard classes are J (Journeyman), A (Apprentice), and T (Trainee). You may enter other values; however, in order for the reports to count the number of employees per type, you must specify one of the three standard classes.
Entering A or T enables the Wage Pct and Apprentice
 Level fields.

Related information

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Wage Pct

Wage Pct field on the PR Craft Classes form.
This field applies to users of the PR Certified - eMars report (U.S. only).

 Enter the percentage of the full wage the employee is being paid. The field is enabled when
 EEO Class is set to A-Apprentice or T-Trainee.
You are not required to enter this field's value before processing payroll because the value entered is not used in payroll calculations. It is only passed to the eMars version of the certified report.
Important: Enter as a whole number, not as a decimal. For example, if the apprentice employee is being paid 80% of a regular employee wage, enter 80.

## Apprentice Level

Apprentice Level field on the PR Craft Classes form.
Enter the apprentice level, 1 through 9.
Only required for certified reporting to the State of California for DBRA-governed projects where an approved apprenticeship program is in place and a participating employee (apprentice) is represented in the payroll being reported. No other circumstances are known to require specification of apprentice level.
This field:

- applies to the PR Certified Export - eMars (ReportID 1315, U.S. only)

- is enabled only when EEO Class is set to A-Apprentice or T-Trainee

- accepts all 1- and 2-character entries

## Calculation Method

Calculation Method drop-down on the PR Craft
 Classes form, Info tab.
 This field is enabled only if you have set up
 capped codes for the craft in PR Crafts.
From the drop-down list, select the calculation method for this craft/class.
Note: If the craft for this class has one or more liability
 capped codes set up in PR Crafts, the system will only allow a calculation method of
 Standard.

- Standard - Traditional overtime
 (OT) calculation where Prevailing Hourly Rate is factored up and combined with
 standard un-factored Prevailing Fringe Benefit Rate as a basis for determining the
 hourly amount of Cash Fringe to be provided above the employees normal overtime
 earnings and bona fide fringes.

- Cash Fringe Factored - A
 calculation method where all cash paid, including hourly cash fringe amounts, will
 be factored equally to determine hourly overtime cash fringe amounts to be paid
 necessary to match a prevailing wage total hourly rate.

- Generous Fringe Benefit Pkg #1 -
 A method of calculation typically used when the employee bona fide benefit package
 exceeds the minimal prevailing wage fringe benefit rate. With this method,
 overtime calculations will continue to utilize the full fringe benefit hourly
 rate, including any cash fringe hourly rates determined to be paid, throughout
 prevailing wage calculations involving overtime hours.

- Generous Fringe Benefit Pkg #2 -
 A method of calculation typically used when the employee bona fide benefit package
 exceeds the minimal prevailing wage fringe benefit rate. With this method,
 overtime calculations will continue to utilize the bona fide fringe benefit hourly
 rate, excluding any cash fringe rates, throughout prevailing wage calculations
 involving overtime hours.

- Constant Fringe Benefit Rate -
 Straight time cash fringe benefit hourly rate will remain constant and the same
 constant rate will be included in an employee’s hourly rate regardless of the
 earnings factor for overtime. This calculation method has been associated with
 earnings packages where employees actual earnings were typically stronger than the
 prevailing wage hourly rate but often without associated bona fide fringe
 benefits.

Related information

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

- [Prevailing Wage Calculations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/prevailing-wage-calculations)

## Old Basic Hourly Rate

Old Basic Hourly Rate field on the PR Craft
 Classes form, Info tab.
 This field is enabled only if you set up
 capped codes for the craft in PR Crafts AND you selected a calculation method other than
 Cash Fringe Factored for the craft/class.
Prevailing wage rates, including the Basic Hourly Rate, the Fringe Benefit Rate, and when combined, the Total Prevailing Wage Rate, are determined by various labor organizations and published in documents establishing Prevailing Wage regulations. If appropriate, enter a Basic Hourly Rate retrieved from such a document. See the [Prevailing Wage Calculations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/prevailing-wage-calculations) chart to see how the value is used once entered in this field.

Related information

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## New Basic Hourly Rate

 New Basic Hourly Rate field on the PR Craft
 Classes form, Info tab.
 This field is enabled only if you set up
 capped codes for the craft in PR Crafts AND you selected a calculation method other than
 Cash Fringe Factored for the craft/class.
Prevailing wage rates, including the Basic Hourly Rate, the Fringe Benefit Rate, and when combined, the Total Prevailing Wage Rate, are determined by various labor organizations and published in documents establishing Prevailing Wage regulations. If appropriate, enter a Basic Hourly Rate retrieved from such a document. See the [Prevailing Wage Calculations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/prevailing-wage-calculations) chart to see how the value is used once entered in this field.

Related information

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Old Fringe Benefit Rate

Old Fringe Benefit Rate field on the PR Craft
 Classes form, Info tab.
 This field is enabled only if you set up
 capped codes for the craft in PR Crafts AND you selected a calculation method other than
 Cash Fringe Factored for the craft/class.
Prevailing wage rates, including the Basic Hourly Rate, the Fringe Benefit Rate, and when combined, the Total Prevailing Wage Rate, are determined by various labor organizations and published in documents establishing Prevailing Wage regulations. If appropriate, enter a Fringe Benefit Rate retrieved from such a document. See the [Prevailing Wage Calculations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/prevailing-wage-calculations) chart to see how the value is used once entered in this field.

Related information

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## New Fringe Benefit Rate

New Fringe Benefit Rate field on the PR Craft
 Classes form, Info tab.
 This field is enabled only if you set up
 capped codes for the craft in PR Crafts AND you selected a calculation method other than
 Cash Fringe Factored for the craft/class.
Prevailing wage rates, including the Basic Hourly Rate, the Fringe Benefit Rate, and when combined, the Total Prevailing Wage Rate, are determined by various labor organizations and published in documents establishing Prevailing Wage regulations. If appropriate, enter a Fringe Benefit Rate retrieved from such a document. See the [Prevailing Wage Calculations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/prevailing-wage-calculations) chart to see how the value is used once entered in this field.

Related information

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

##  Old Total Wage Rate

Old Total Wage Rate field on the PR Craft
 Classes form, Info tab.
 This field is enabled only if you have set up
 capped codes for the craft in PR Crafts AND you selected Cash Fringe Factored as the
 calculation method for the craft/class.
Prevailing wage rates, including the Basic Hourly Rate, the Fringe Benefit Rate, and when combined, the Total Prevailing Wage Rate, are determined by various labor organizations and published in documents establishing Prevailing Wage regulations. If appropriate, enter a Total Wage Rate retrieved from such a document. See the [Prevailing Wage Calculations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/prevailing-wage-calculations) chart to see how the value is used once entered in this field.
For craft classes with a calculation method
 other than Cash Fringe Factored, this field is disabled and displays the total of the
 Old Basic Hourly
 Rate and Old Fringe Benefit Rate fields.

Related information

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## New Total Wage Rate

New Total Wage Rate field on the PR Craft
 Classes form, Info tab.
 This field is enabled only if you have set up
 capped codes for the craft in PR Crafts AND you selected Cash Fringe Factored as the
 calculation method for the craft/class.
Prevailing wage rates, including the Basic Hourly Rate, the Fringe Benefit Rate, and when combined, the Total Prevailing Wage Rate, are determined by various labor organizations and published in documents establishing Prevailing Wage regulations. If appropriate, enter a Total Wage Rate retrieved from such a document. See the [Prevailing Wage Calculations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/prevailing-wage-calculations) chart to see how the value is used once entered in this field.
For craft classes with a calculation method
 other than Cash Fringe Factored, this field is disabled and displays the total of the
 New Basic Hourly
 Rate and New Fringe Benefit Rate fields.

Related information

- [Set Up Craft Class Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-class-templates)

- [About the PR Craft Class Templates Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-class-templates-form)

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

## Shift

Shift field on the PR Craft Classes form, Pay Rates tab.
Enter the shift number for this pay rate entry.

Related information

- [Set Up Pay Rates for Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-pay-rates-for-craft-classes)

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Old Rate

Old Rate field on the PR Craft Classes form,
 Pay Rates tab.
Enter the old rate for this shift. The system
 will only use this rate for timecards entered prior to the Effective Date specified in PR
 Crafts or PR Craft Template.

Related information

- [Set Up Pay Rates for Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-pay-rates-for-craft-classes)

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

- [About the PR Craft Templates Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-templates-form)

## New Rate

New Rate field on the PR Craft Classes form,
 Pay Rates tab.
Enter the new rate for this shift. The system
 will only use this rate for timecards entered on or after the Effective Date specified in
 PR Crafts or PR Craft Template.

Related information

- [Set Up Pay Rates for Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-pay-rates-for-craft-classes)

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

- [About the PR Craft Templates Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-templates-form)

## Shift

Shift field on the PR Craft Classes form, Variable Earnings tab.
Enter the variable earnings shift number.

Related information

- [Set Up Variable Earnings for Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-variable-earnings-for-craft-classes)

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Earn Code

Earn Code field on the PR Craft Classes form,
 Variable Earnings tab.
Enter a valid earnings code (cannot be an add-on earnings) or press F4 to select from a list of valid earnings codes.

Related information

- [Set Up Variable Earnings for Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-variable-earnings-for-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Method

Method field on the PR Craft Classes form,
 Variable Earnings tab.
Display only, the calculation method assigned
 to the specified earnings code in PR Earnings Codes.

Related information

- [Set Up Variable Earnings for Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-variable-earnings-for-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

## Old Rate

Old Rate field on the PR Craft Classes form,
 Variable Earnings tab.
Enter the old rate for the specified variable
 earnings shift. The system will only use this rate for timecards entered prior to the
 Effective Date specified in PR Crafts or PR Craft Template.

Related information

- [Set Up Variable Earnings for Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-variable-earnings-for-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

- [About the PR Craft Templates Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-templates-form)

## New Rate

New Rate field on the PR Craft Classes form,
 Variable Earnings tab.
Enter the new rate for the specified variable
 earnings shift. The system will only use this rate for timecards entered on or after the
 Effective Date specified in PR Crafts or PR Craft Template.

Related information

- [Set Up Variable Earnings for Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-variable-earnings-for-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

- [About the PR Craft Templates Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-templates-form)

## Earn Code

Earn Code field on the PR Craft Classes form,
 Add-on Earnings tab.
Enter a valid earnings code for this add-on earnings or press F4 to select from a list of valid earnings codes.

Related information

- [Assign Add-on Earnings to a Craft Class](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-add-on-earnings-to-a-craft-class)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Method

Method field on the PR Craft Classes form,
 Variable Earnings tab.
Display only, the calculation method assigned
 to the specified earnings code in PR Earnings Codes.

## Old Rate

Old Rate field on the PR Craft Classes form,
 Variable Earnings tab.
Enter the old rate for the specified variable
 earnings shift. The system will only use this rate for timecards entered prior to the
 Effective Date specified in PR Crafts or PR Craft Template.

## New Rate

New Rate field on the PR Craft Classes form,
 Variable Earnings tab.
Enter the new rate for the specified variable
 earnings shift. The system will only use this rate for timecards entered on or after the
 Effective Date specified in PR Crafts or PR Craft Template.

## Earn Code

Earn Code field on the PR Craft Classes form,
 Add-on Earnings tab.
Enter a valid earnings code for this add-on earnings or press F4 to select from a list of valid earnings codes.

## Method

Method field on the PR Craft Classes form, Add-on Earnings tab.
Display only, the calculation method assigned to the specified earnings code in PR Earnings Codes.

Related information

- [Assign Add-on Earnings to a Craft Class](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-add-on-earnings-to-a-craft-class)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

## Factor

Factor field on the PR Craft Classes form, Add-on Earnings tab.
This field is enabled only when earnings code calculation method is V (Variable Factored Rate). For all other calculation methods, the factor is set to 0.000000 and cannot be changed.
Enter the factor (number) by which to multiply the rate for this add-on earnings (e.g. 0.5 for half time, 1.0 for regular time, 1.5 for time and a half, and 2.0 for double time).

Related information

- [Assign Add-on Earnings to a Craft Class](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-add-on-earnings-to-a-craft-class)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Old Rate

Old Rate field on the PR Craft Classes form,
 Add-on Earnings tab.
Enter the old rate for this add-on earnings.
 The system will only use this rate for timecards entered prior to the Effective Date
 specified in PR Crafts or PR Craft Template.

Related information

- [Assign Add-on Earnings to a Craft Class](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-add-on-earnings-to-a-craft-class)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

- [About the PR Craft Templates Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-templates-form)

## New Rate

New Rate field on the PR Craft Classes form,
 Add-on Earnings tab.
Enter the new rate for this add-on earnings.
 The system will only use this rate for timecards entered on or after the Effective Date
 specified in PR Crafts or PR Craft Template.

Related information

- [Assign Add-on Earnings to a Craft Class](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-add-on-earnings-to-a-craft-class)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

- [About the PR Craft Templates Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-templates-form)

## DL Code

DL Code field on the PR Craft Classes form,
 Dedns / Liabs tab.
Enter the deduction or liability code that is
 required for this class or press F4 to select from a list of valid
 deduction and liability codes.

Related information

- [Assign Deductions and Liabilities to a Craft Class](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft-class)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Type

Type field on the PR Craft Classes form, Dedns
 / Liabs tab.
Display only, the DL code type indicating
 whether it the selected code is a deduction (D) or liability (L).

Related information

- [Assign Deductions and Liabilities to a Craft Class](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft-class)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Method

Method field on the PR Craft Classes form,
 Dedns / Liabs tab.
Display only, the calculation method assigned
 to the specified deduction or liability code in PR Deductions/Liabilities.
Note: If a deduction (including pre-tax) or liability using a method of Rate per Day is assigned to multiple crafts/classes or craft/class templates and an employee works on more than one craft/class for the same day, the deduction/liability will be calculated for each craft/class/template.

Related information

- [Assign Deductions and Liabilities to a Craft Class](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft-class)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

## Factor

Factor field on the PR Craft Classes form,
 Dedns / Liabs tab.
This field is enabled only when the deduction or liability calculation method is V (Variable Factored Rate). For all other calculation methods, the factor is set to 0.000000 and cannot be changed.
Enter the factor (number) by which to multiply the rate for this deduction or liability (e.g. 0.5 for half time, 1.0 for regular time, 1.5 for time and a half, and 2.0 for double time).

Related information

- [Assign Deductions and Liabilities to a Craft Class](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft-class)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Old Rate

Old Rate field on the PR Craft Classes form,
 Dedns / Liabs tab.
Enter the old rate for this deduction or
 liability. The system will only use this rate for timecards entered prior to the Effective
 Date specified in PR Crafts or PR Craft Template.

Related information

- [Assign Deductions and Liabilities to a Craft Class](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft-class)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## New Rate

New Rate field on the PR Craft Classes form,
 Dedns / Liabs tab.
Enter the new rate for this deduction or
 liability. The system will only use this rate for timecards entered on or after the
 Effective Date specified in PR Crafts or PR Craft Template.

Related information

- [Assign Deductions and Liabilities to a Craft Class](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft-class)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Allowance

Allowance field on the PR Craft Classes form,
 Allowance Earnings tab.
Enter the allowance name or press F4 to select
 from a list of valid allowances. Allowance must be assigned a Rule Set Location of Craft
 Class in PR Allowances.

Related information

- [Assign Allowances to Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-allowances-to-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [PR Allowances Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-allowances-form)

## Earn Code

Earn Code field on the PR Craft Classes form,
 Allowance Earnings tab.
Enter the earnings code for this allowance or
 press F4 to select from a list of valid earnings codes.
Tip: You should specify an earnings code that is specific to the allowance you enter. The system does not report based on allowances, but on earnings. Therefore, if you use a generic earnings code for each allowance, the system will only display a lump sum amount for earnings and you will be unable to tell which allowances contributed to the amount (PR Employee Pay Seq Control, Earnings Code tab, for example).

Related information

- [Assign Allowances to Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-allowances-to-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Rule Set

Rule Set field on the PR Craft Classes form,
 Allowance Earnings tab.
Enter the rule set to use for determining how
 this allowance will be calculated. Press F4 for a list of valid rule sets.

Related information

- [Assign Allowances to Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-allowances-to-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

## Shift Rate Override

Shift Rate Override field on the PR Craft
 Classes form, Allowance Earnings tab.
Enter the shift rate to use for this allowance. The system will use this rate regardless of the shift worked for the employee.
Note: If an employee works under multiple classes, shifts, and/or templates, the system will use the highest straight time rate for the shift. However, a higher rate specified for the employee in PR Employees (Hourly Rate field) will override any/all shift rates.
 Leave this field blank to use the straight time rate for the shift worked by the employee.

Related information

- [Assign Allowances to Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-allowances-to-craft-classes)

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)
