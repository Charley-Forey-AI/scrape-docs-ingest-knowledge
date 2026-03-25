---
title: "Assign Deductions and Liabilities to a Craft | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-deductions-and-liabilities-to-a-craft"
---

# Assign Deductions and Liabilities to a Craft

You can assign deductions and liabilities to a craft using the
 Dedns/Liabs tab in PR Crafts.
This tab should only include deductions and
 liabilities required by the craft. Federal, state, city, insurance, and personal
 deductions and liabilities should not be set up here. Deductions and liabilities
 from PR Crafts are always applied, but rates can be overridden at the class, craft
 template, and/or craft class template levels.
The following instructions detail how to assign deductions and liabilities to a craft.
If you have [created a pre-tax deduction](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes) and want to assign it
 at the craft/class/template levels, you must first add the pre-tax deduction to the
 Dedns/Liabs tab in PR Crafts. Once you add the pre-tax deduction to PR Crafts, you
 can then specify overrides in PR Craft Templates, PR Craft Classes, or PR Craft
 Class Templates. If you attempt to add a pre-tax deduction to the Dedns/Liabs tab
 for one of the these forms without adding it to PR Crafts, the system will display a
 warning and prevents you from entering the deduction.

1. In PR Crafts, select the
 craft for which to set up deductions and liabilities.

1. Select the Dedns/Liabs tab.

1. In the DL
 Code field, enter the deduction/liability code that is required
 for this craft or press F4 to select from a list of
 valid codes.The system defaults values in
 the Description, Type, and Method fields.
Note: Liabilities that will be included in the
 capped basis for a craft must also be set up on the Dedns/Liabs tab in PR
 Crafts, PR Craft Classes, PR Craft Template, PR Craft Class Templates, or PR
 Employee Dedns/Liabs; otherwise, the system will not include them in basis
 calculations. For more information, see [Setting
 Capped Codes and Limits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-capped-codes-and-limits).

1. If the calculation
 method is V (variable), in the Factor field, enter the
 earnings factor that applies to this craft. For all other calculation methods,
 the factor is set to 0.000000 and cannot be changed. In the Old
 Rate field, enter the old rate for the deduction or liability
 code. The system will use this rate for timecards entered prior to the date
 specified in the Effective Date field (Info
 tab). You can override this rate at the craft template level. In the New Rate
 field, enter the new rate for the deduction or liability code. The system will
 use this rate for timecards entered on or after the date specified in the
 Effective Date field (Info tab). You can override this rate at
 the craft template level. In the Vendor field, enter the vendor to use for this deduction or
 liability or leave blank to use the vendor specified for the craft on the
 Info tab. You will typically do this if you need to print a separate check
 for each employee paid benefit within the union.
 If no vendor is specified on
 the Info tab, the system will use the vendor assigned to this
 deduction/liability in PR Deductions/Liabilities.

1. If you did not specify a vendor for this craft (on the Info tab), the system uses the vendor assigned to the deduction/liability in PR Deductions/Liabilities. Save the record.

Related information

- [About the PR Crafts Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-crafts-form)

- [Set Up Crafts](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-crafts)
