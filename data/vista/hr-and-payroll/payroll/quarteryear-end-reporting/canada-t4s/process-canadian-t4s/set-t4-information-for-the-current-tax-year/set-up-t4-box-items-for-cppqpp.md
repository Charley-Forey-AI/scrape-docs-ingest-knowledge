---
title: "Set up T4 Box Items for CPP/QPP | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/canada-t4s/process-canadian-t4s/set-t4-information-for-the-current-tax-year/set-up-t4-box-items-for-cppqpp"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/canada-t4s/process-canadian-t4s/set-t4-information-for-the-current-tax-year/set-up-t4-box-items-for-cppqpp"
---

# Set up T4 Box Items for CPP/QPP

(Canada only) To ensure you accurately capture CPP, CPP2, QPP, and QPP2 amounts for T4 reporting, you must map the applicable T4 Box Items to the appropriate EDL Codes in the PR Canada T4 form, T4 Box Items tab.

All deduction/liability codes assigned to T4 Box Items related to CPP, CPP2, QPP, and QPP2 must be defined for the company in PR Federal Info (Info tab). You can only use these deductions and liabilities when mapping T4 Box Items for CPP, CPP2, QPP, and QPP2.

1. Open the PR Canada T4 form (Main Menu > Payroll > Programs > PR Canada T4)).

1. In the Tax Year field, enter the applicable tax year.Note: If you entered a new tax year, the Info tab auto-defaults the appropriate company info. You may edit as needed.

1. If you entered a new tax year, select Initialize Employer T4 Items/Codes.For existing tax years, you only need to select this option if you have not yet initialized item codes or if you need to reinitialize them.
The initialization process automatically populates the T4 Box Items and T4 Other Codes grids with the applicable codes, including only those that are valid for the specified tax year.

1. Select the T4 Box Items tab.

1. Set up the CPP/QPP box items as follows:Note: The system will warn you if you enter an EDL code that does not match what you have defined in PR Federal Info or if you enter the wrong EDL or Amount types.

T4 Box NumberEDL TypeEDL CodeAmount Type
16 (Employee's CPP contributions)D-DeductionCPP DeductionA-Amount
161 (Employee's second CPP) (Box 16A) *D-DeductionCPP2 DeductionA-Amount
17 (Employee's QPP contributions)D-DeductionQPP DeductionA-Amount
171 (Employee's second QPP) (Box 17A) *D-DeductionQPP2 DeductionA-Amount
26 (CPP/QPP pensionable earnings)D-DeductionCPP Deductionblank
26 (CPP/QPP pensionable earnings)D-DeductionCPP2 Deductionblank
26 (CPP/QPP pensionable earnings)D-DeductionQPP Deductionblank
26 (CPP/QPP pensionable earnings)D-DeductionQPP2 Deductionblank
27 (Employer's CPP contributions)L-LiabilityCPP LiabilityA-Amount
271 (Employer's second CPP) (Box 27A) *L-LiabilityCPP2 LiabilityA-Amount

* Due to legacy technical limitations, T4 Boxes 16A, 17A, and 27A are represented within Vista by T4 Box Numbers 161, 171, and 271, respectively. Additionally, T4 Box Numbers 17 and 171 (17A) are optional and need to be configured only if you have employees working in Quebec. Likewise, for T4 Box Number 26, the mappings for the QPP Deduction and QPP2 Deduction are optional and need to be configured only if you have employees working in Quebec.
