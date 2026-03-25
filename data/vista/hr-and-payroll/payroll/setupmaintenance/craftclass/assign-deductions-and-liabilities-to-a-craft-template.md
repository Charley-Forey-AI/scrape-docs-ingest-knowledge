---
title: "Assign Deductions and Liabilities to a Craft Template | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft-template"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft-template"
---

# Assign Deductions and Liabilities to a Craft Template

You can assign deductions and liabilities to a craft template
 using the Dedns/Liabs tab in PR Craft Template.
You can override deductions/liabilities specified in
 PR Crafts or PR Craft Classes by entering them here and adjusting information as
 necessary. You can also specify additional deductions/liabilities as required by
 this template. The system will use the rates on this tab unless overridden at the
 craft class template level (PR Craft Class Templates).
Important: Deduction and liability rates defined at the craft/class or craft levels do not need to be set up here unless you are overriding the existing rate(s). If you do not override an existing rate here, the rate defined at the craft/class or craft level will be used (respectively). If you want a specific rate excluded from calculations, set it up here with a 0.00 amount. Note that overrides set up in PR Craft Class Templates will override any rates set up here or at the craft/class and craft levels.
The following instructions detail how to assign deductions and liabilities to a craft template.
If you have [created a pre-tax deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes) and want to assign it
 at the craft/class/template levels, you must first add the pre-tax deduction to the
 Dedns/Liabs tab in PR Crafts. Once you add the pre-tax deduction to PR Crafts, you
 can then specify overrides in PR Craft Templates, PR Craft Classes, or PR Craft
 Class Templates. If you attempt to add a pre-tax deduction to the Dedns/Liabs tab
 for one of the these forms without adding it to PR Crafts, the system will display a
 warning and prevents you from entering the deduction.

1. In PR Craft Templates, select the Dedns/Liabs tab.

1. Enter the
 deduction/liability code that is required for this craft template in the
 DL
 Code field. Press F4 for a list of codes.The system defaults values in the Description, Type, and Method fields.Note: Liabilities that
 will be included in the capped basis for a craft must also be set up on the
 Dedns/Liabs tab in PR Crafts, PR Craft Classes, PR Craft Template, PR Craft
 Class Templates, or PR Employee Dedns/Liabs; otherwise, the system will not
 include them in basis calculations. For more information, see [Setting Capped Codes and
 Limits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits).

1. If the calculation
 method (Method field) is variable (V), enter the earnings factor that
 applies to this craft template in the Factor field. For all other
 calculation methods, the factor is set to 0.000000 and cannot be changed.

1. Enter the old rate for
 this deduction/liability code in the Old Rate field. The system
 uses this rate for timecards entered prior to the effective date specified in PR
 Crafts or PR Craft Templates. You can override this rate at the craft class
 template level.

1. Enter the new rate for
 this earnings code in the New Rate field. The system
 uses this rate for timecards entered prior to the effective date specified in PR
 Crafts or PR Craft Templates. You can override this rate at the craft class
 template level.

1. Save the record as normal. [Crafts, Classes, and Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-crafts-classes-and-templates)

Related information

- [About the PR Craft Templates Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-templates-form)
