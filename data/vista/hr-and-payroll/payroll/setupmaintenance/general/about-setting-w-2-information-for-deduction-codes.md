---
title: "About Setting W-2 Information for Deduction Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-w-2-information-for-deduction-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-w-2-information-for-deduction-codes"
---

# About Setting W-2 Information for Deduction Codes

This topic applies to United States users only. For each deduction code that will be used for W-2 reporting, you must set up the appropriate W-2 information in PR Deductions/Liabilities.
When creating deduction codes, use the W-2 section (Addl Info tab) to indicate that this is an employee-based deduction that you must report on W-2s. The system enables this section when you are creating a deduction with the Calculation Category field set to E-Employee or A-Any.
Note: Use PR Federal Info, PR State Information, or PR Local Codes to set up any addition, non-employee-based deductions that require reporting on W-2s.
To set up employee-based deductions for W-2 reporting, first select the Include on W-2s as a Local Tax checkbox. Then specify the reporting state and the local code in the Reporting State and Local fields, respectively. Finally, select an option in the Tax Type drop-down to identify the type of local tax for the deduction. For more information, refer to the F1 help for these fields.
Note: If you set up employee-based local tax deductions (for example, school districts) along with city taxes, and they both need to be reported on W-2s as local taxes, assign the city tax deduction to a Local code in PR Local Codes, and set the Reporting State and Local fields on this form for the employee-based tax. Make sure you enter an unused local code that you will not confuse with the Local codes in PR Local Codes.Additionally, if you file your W-2s via Aatrix, you must assign the deduction/liability code an Aatrix Tax Type. For more information, see [ Aatrix Tax Type](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036b63--en).

Related information

- [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes)
