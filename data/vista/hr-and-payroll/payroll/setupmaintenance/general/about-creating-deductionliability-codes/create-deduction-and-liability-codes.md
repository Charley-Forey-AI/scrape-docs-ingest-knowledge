---
title: "Create Deduction and Liability Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes"
---

# Create Deduction and Liability Codes

Use the PR Deductions/Liabilities form to create deduction codes (standard and pre-tax) and liability codes.
The system uses a specific hierarchy for processing and displaying codes, so it is recommended that you develop a numbering scheme or code sequence to enable easier maintenance. For additional information, see [About Creating Deduction/Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes).

The following instructions detail how to create deduction and liability codes.Note: For standard (not pre-tax) deduction and liabilities with a calculation category of Craft, it is not necessary to create multiple codes. For example, if you have three crafts that have a vacation deduction calculated at an hourly rate, use the same deduction code for all three. However, if the method of calculation is different, or a different GL credit account is required, different codes are necessary. For more information on calculation categories, see [Setting the Calculation Category](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-setting-the-calculation-category-for-dl-codes).

1. Enter a code number in the Dedn/Liab Code field and enter a description of the code in the Description field.

1. Set the code type in the Type section of the form by selecting the appropriate radio button: Deduction or Liability. Note: When creating a liability code, you must also assign a liability type in the Liability Type field. The liability type determines which GL account the system debits when expensing this liability to either a PR or JC department (in the PR Departments and JC Departments forms, respectively). You may want to group similar liabilities together using the same type (e.g., taxes, insurance, union benefits, etc.). You can use the [HQ Liability Types ](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-liability-types-form) form to set up liability types.
Note: You can also designate taxable liability codes in the basis code list of deduction codes. See the field information for [Basis code on other dedn/liab codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-0005bf11--en) for more information.

1. [Set the calculation category](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-setting-the-calculation-category-for-dl-codes) for the code using the Calculation Category and Federal Type fields.

1. [Set the method of calculation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-methods-of-calculation/about-determining-the-method-of-calculation-for-dl-codes) for the code.

1. Assign rates/amounts for the code in the Rate/Amount #1 and Rate/Amount #2 fields.

1. [Set any applicable limits for the code](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-setting-limits-for-deductionsliabilities) by using the fields in the Limit section of the form.

1. There are a number of additional checkboxes on this form to establish settings for this code. Select them as appropriate; for more information, refer to the F1 help for each box.

1. If this is a pre-tax deduction, select the Pre-Tax Deduction box. Note: When you select the Pre-Tax Deduction checkbox, and you have set the Calculation Category drop-down to E-Employee, the system enables the Pre-Tax Group field. Enter a group in this field if you have multiple pre-tax deductions that require a combined limit. See [Setting Up Pre-Tax Deduction Groups](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-a-pre-tax-deduction-group) for more information.
Note: Once you select the Pre-Tax Deduction checkbox, the system enables the Catch up Deduction box. Select this checkbox if the deduction code will be used as a catch up code. United States users might use this for employees who are 50 and older who want to make catch-up contributions to a 401(k) or Roth plan. For more information, see [Setting Up Pre-Tax Deductions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions).

1. For Craft and Employee liability codes only: If this liability code can be included in the basis code list of specific deduction or liability codes, select the Basis code on other dedn/liab codes checkbox.For more information about this checkbox, see the [F1 Help](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-0005bf11--en).

1. Set codes to [automatically process AP transactions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-automatic-accounts-payable-updates-for-dl-codes) for the deduction/liability amount, as necessary.

1. For U.S. users, if this deduction/liability code is subject to state and local tax or unemployment reporting and you file those reports via Aatrix, use the Aatrix Tax Type field to assign the appropriate tax type. Press F4 for a list of valid tax types.Note: If you have locals that are included in W-2 reporting and those locals do not have a specific Aatrix Tax Type, use tax type 2000. The AUF files generated for Aatrix W-2 reporting will include records using tax type 2000.

1. For U.S. users, [set W-2 information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-w-2-information-for-deduction-codes) for specific deduction codes.

1. For Australian users, select the Australian Taxation Office category for this deduction/liability code from the ATO Category drop-down (Addl Info tab), if necessary. For more information on the options available from this drop-down, see [ATO Category](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036b98--en). Note: If you select either Superannuation or Superannuation-Extra, the system enables the Fund field. For more information on Superannuation, see [Setting Up Liability Codes for Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/setting-up-liability-codes-for-superannuation).

1. If you are creating a deduction code, you can set it as subject to arrears. For more information, see [Setting Deductions as Subject to Arrears](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-deductions-as-subject-to-arrears).

1. [Determine the calculation basis](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/about-determining-the-calculation-basis-for-deduction-and-liability-codes) for the deduction/liability code, as necessary.

1. Save the code as normal. You can now [assign the deduction and liability codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/assigning-deductions-and-liabilities) to the appropriate level tax, craft/class or employee level.

Related information

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [PR Employee Dedns/Liabs Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form)

- [Set up superannuation fund clearing houses](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation/set-up-superannuation-fund-clearing-houses)

- [About the HQ Super Funds Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/about-the-hq-super-funds-form)
