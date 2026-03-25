---
title: "Set up QPP / QPP2 Deductions: Canada | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-qpp--qpp2-deductions-canada"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-qpp--qpp2-deductions-canada"
---

# Set up QPP / QPP2 Deductions: Canada

Applies only to Canada users who have one or more employees subject to Quebec's deduction and liability amounts.
Note: Beginning in 2024, if an employee's annual income exceeds the maximum QPP limit, employees can contribute an additional portion of their earnings to the QPP. For [qualifying companies](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/vista-2023-r2-service-packs/vista-2023-r2.01#concept-98fefa07-8aee-472a-aa85-5c2aa07bc044--en__CPP_QualifyingCOs), when you install the 2023 year-end service pack, a new QPP2 deduction code is automatically set up for you. You can set up a different deduction code for QPP2 contributions if desired; however, you will need to designate the new code in the QPP2 Deduction field in PR Federal Info.

1. Open the PR Deductions and Liabilities form (Payroll > Programs > PR Deductions and Liabilities)

1. In the Dedn / Liab Code field, enter a number to uniquely identify the code.

1. In the Description field, enter a description for the code.

1. In the Type section of the form, select the Deduction radio button.

1. Set the Calculation Category drop-down to F-Federal.

1. In the Federal Type drop-down, select one of the following:

- 3-QPP (combined base QPP contribution and first additional QPP contribution)

- 7-QPP2 (second additional QPP contribution)

1. In the GL Account field, enter the GL account to credit for this deduction code.

1. In the Method drop-down, select R-Routine.

1. In the Routine field, enter a value as follows:

- If you selected 3-QPP in the Federal Type field, enter CPP or press F4 to locate and select the routine.

- If you selected 7-QPP2 in the Federal Type field, enter CPP2 or press F4 to locate and select the routine.

1. In the Rate / Amount #1 field, enter the current rate.

1. In the Amount field (Limit section), select the Subject Amount option and enter the annual contribution amount.

Note: You must add this QPP deduction code to the PR Federal Info form prior to processing payroll.

Related information

- [PR Routines Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-routines-form)
