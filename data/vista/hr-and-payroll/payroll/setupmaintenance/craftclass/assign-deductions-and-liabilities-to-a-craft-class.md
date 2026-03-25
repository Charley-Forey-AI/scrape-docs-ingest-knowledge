---
title: "Assign Deductions and Liabilities to a Craft Class | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft-class"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft-class"
---

# Assign Deductions and Liabilities to a Craft Class

You can assign deductions and liabilities to a craft class
 using the Dedns/Liabs tab in PR Craft Classes.
Deductions and liabilities set up here override those set up at the craft level; therefore, you will only need to set up deduction and liability rates here if you are overriding the existing rate(s). If you want to exclude a specific rate from calculations, set it up here with a 0.00 amount.
Note: Overrides set up at the craft template or craft/class template level will override any rates set up here or at the craft level. Requiring only override rates to be defined here eliminates having to update multiple levels each time a rate change occurs.
You can assign a deduction (including pre-tax) or liability to multiple crafts/classes or craft/class templates; however, if the deduction or liability is using a Rate per Day calculation method and an employee works on more than one craft/class for the same day, the system will calculate the deduction or liability for each craft/class/template.
The following instructions detail how to assign deductions and liabilities to a craft class.
Note: If you have [created a pre-tax deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes) and want to assign it
 to a craft class here, you must first add the pre-tax deduction to the Dedns/Liabs
 tab in PR Crafts. The system will not allow you to add a pre-tax deduction here that
 does not exist in PR Crafts.

1. In PR Craft Classes,
 select the craft class for which to set up deductions and liabilities.

1. Select the Dedns/Liabs tab.

1. In the DL
 Code field, enter the deduction/liability code that is required
 for this class or press F4 to select from a list of
 valid codes. Note: Liabilities that will be included in the capped basis for a craft must
 also be set up on the Dedns/Liabs tab in PR Crafts, PR Craft Classes, PR
 Craft Template, PR Craft Class Templates, or PR Employee Dedns/Liabs;
 otherwise, the system will not include them in basis calculations. For more
 information, see [Setting Capped Codes and Limits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits).

1. If the calculation
 method is V (variable), in the Factor field, enter the earnings factor that
 applies to this class. For all other calculation methods, the factor is set to
 0.000000 and cannot be changed. In the Old Rate field, enter the old rate for
 the deduction or liability code. The system will use this rate for timecards
 entered prior to the Effective Date specified in PR Crafts or PR Craft Template.
 In the New Rate field, enter the new rate for the deduction or liability code.
 The system will use this rate for timecards entered on or after the Effective
 Date specified in PR Crafts or PR Craft Template. Save the record. [Crafts, Classes, and Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-crafts-classes-and-templates)

Related information

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)
