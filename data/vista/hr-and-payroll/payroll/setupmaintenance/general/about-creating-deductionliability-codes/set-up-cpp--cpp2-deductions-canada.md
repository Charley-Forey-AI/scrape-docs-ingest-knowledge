---
title: "Set up CPP / CPP2 Deductions: Canada | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-cpp--cpp2-deductions-canada"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-cpp--cpp2-deductions-canada"
---

# Set up CPP / CPP2 Deductions: Canada

Create a deduction code when setting up Canadian Pension Plan (CPP and CPP2) withholding.
Use the following steps to set up a CPP deduction code.
Note: Beginning in 2024, if an employee's annual income exceeds the maximum CPP limit, the employee must contribute an additional portion of their earnings to the CPP. For [qualifying companies](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/vista-2023-r2-service-packs/vista-2023-r2.01#concept-98fefa07-8aee-472a-aa85-5c2aa07bc044--en__CPP_QualifyingCOs), when you install the 2023 year-end service pack, a new CPP2 deduction code is automatically set up for you. You can set up a different deduction code for CPP2 contributions if desired; however, you will need to designate the new code in the CPP2 Deduction field in PR Federal Info.

If you need a more general description of creating deduction and liability
 codes, see [Creating Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes).

1. Open the PR Deductions and Liabilities form (Payroll > Programs > PR Deductions and Liabilities)

1. In the Dedn / Liab Code field, enter a number to uniquely identify the code.

1. In the Description field, enter a description for the code.

1. In the Type section of the form, select the Deduction radio button.

1. Set the Calculation Category drop-down to F-Federal.

1. In the Federal
 Type drop-down, select one of the following:

- 2-CPP (combined base CPP contribution and first additional CPP contribution)

- 6-CPP2 (second additional CPP contribution)

1. In the GL Account field, enter the GL account to credit for this deduction code.

1. In the Method drop-down, select R-Routine.

1. In the Routine field, enter a value as follows:

- If you selected 2-CPP in the Federal Type field, enter CPP or press F4 to locate and select the routine.

- If you selected 6-CPP2 in the Federal Type field, enter CPP2 or press F4 to locate and select the routine.

1. In the Rate / Amount #1 field, enter the current rate.

1. In the Amount field (Limit section), select the Subject Amount option and enter the annual contribution amount.

1. Set up automatic AP updates for the code, making sure to select the Separate AP Transaction per Employee checkbox. For more information, see [Setting Automatic Accounts Payable Updates for D/L Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-automatic-accounts-payable-updates-for-dl-codes#ID-00032440--en__ID-00032440).

For the CPP routine only (does not apply to the CPP2 routine): In [PR Routines](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-routines-form), enter the annual basic exemption amount in the Misc Amt #1 field. For more information, see [Deduction and Liability Based Routines: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-canada).Note: You must add this CPP deduction code to the PR Federal Info form prior to processing payroll.

Related information

- [PR Pre-Tax Deduction Groups Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-pre-tax-deduction-groups-form)

- [PR Routines Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-routines-form)
