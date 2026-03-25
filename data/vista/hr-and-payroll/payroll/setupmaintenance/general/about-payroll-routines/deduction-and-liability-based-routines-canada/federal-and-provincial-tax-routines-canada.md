---
title: "Federal and Provincial Tax Routines: Canada | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-canada/federal-and-provincial-tax-routines-canada"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-canada/federal-and-provincial-tax-routines-canada"
---

# Federal and Provincial Tax Routines: Canada

The system accommodates specific Canada deductions through the use of a routine.
Province
Routine
Procedure Name
Form Used
Description

Additional Information for Setup

Canada Pension Plan
CPP / QPP
bspPRCPP
PR Deductions/Liabilities
Set up deductions for CPP and QPP using this routine.
Calculation Category = Federal.
For CPP: Federal Type = 2-CPP
For QPP: Federal Type = 3-QPP
Method = R-Routine
Routine = CPP
For more information, see [Setting Up a CPP Deduction Code](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-cpp--cpp2-deductions-canada).

PR Routines
Enter the annual basic exemption amount in the Misc Amt #1 field.

CPP2 / QPP2bspPRCPP2PR Deductions/LiabilitiesSet up deductions for CPP2 and QPP2 using this routine.
Calculation Category = Federal
For CPP2: Federal Type = 6-CPP2
For QPP2: Federal Type = 7-QPP2
Method = R-Routine
Routine = CPP2
Note: For [qualifying companies](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/vista-2023-r2-service-packs/vista-2023-r2.01#concept-98fefa07-8aee-472a-aa85-5c2aa07bc044--en__CPP_QualifyingCOs), the CPP2 and QPP2 deduction codes are set up for you automatically upon installation of the 2023 year-end service pack. It is recommended that you review these codes for accuracy before you process your first 2024 payroll. If you choose to do so, you can set up different deduction codes for CPP2 and QPP2 using these settings.

Federal Tax
FED Tax
bspPR_CA_FWTXX
PR Deductions/Liabilities
Set up a deduction code using this routine.
Use Calculation Category of Federal.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

Alberta
AB Tax
bspPR_CA_ABTXX
PR Deductions/Liabilities
Select S-State from the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

British Columbia

BC Tax
bspPR_CA_BCTXX
PR Deductions/ Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

Daily Ben
Daily Ben
bspPRDailyBen
PR Routines
Set up daily rates in the Misc Amt fields as follows:
Misc Amt #1 – Weekdays Misc Amt #2 – Saturday Misc Amt #3 – Sunday
You should only use this routine if you have varying hourly benefits depending on the day of the week (i.e. separate rates for Mon-Fri, Sat, and Sun/Holidays). It assumes there are no regular time hours on Saturday, Sunday, or holidays.

Exempt Rate of Gross

ExemptROG

bspPRExemptRateOfGross

PR Routines
Set up a separate routine for each applicable local, and assign 'bspPRExemptRateOfGross' as the procedure.
Enter the exemption amount in Misc Amt #1.

PR Deductions/ Liabilities
Assign routine to appropriate deductions.
Set up tax rates where applicable (i.e. Federal, State, Local, Craft, Employee), and make sure to update taxes when needed.

Manitoba

MB Tax

bspPR_CA_MBTXX

PR Deductions/ Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

New Brunswick

NB Tax

bspPR_CA_NBTXX

PR Deductions/ Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

Newfoundland / Labrador

NL Tax

bspPR_CA_NTXX

PR Deductions/ Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

Nova Scotia

NS Tax

bspPR_CA_NSTXX

PR Deductions/ Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use the Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Note: If the employee did not file a TD1, do not create the employee deduction record. The system will determine taxes based on the BPA (basic personal amount) calculation.
Note: If the employee did not file a TD1, but does have Authorized Tax Credits (see below), you must enter an amount in the Total Claim Amount field, even if it is an estimated amount. Setting the Total Claim Amount to 0 (zero), will cause the employee to be taxed at a higher rate.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

Northwest Territories
NT Tax
bspPR_CA_NTTXX
PR Deductions/ Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

Nunavut
NU Tax
bspPR_CA_NUTXX
PR Deductions/ Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

Ontario
ON Tax
bspPR_CA_ONTXX
PR Deductions/ Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the K3/K3P field to enter K3P amount.
Use the Additional Exemptions field to enter the number of dependents under age 18, plus disabled dependents over age 18.

Prince Edward Island
PE Tax
bspPR_CA_PETXX
PR Deductions/ Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

Quebec
QC Tax
bspPR_CA_QCT15
PR Deductions/ Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

Saskatchewan
SK Tax
bspPR_CA_SKTXX
PR Deductions/ Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.

Yukon
YT Tax
bspPR_CA_YTTXX
PR Deductions/Liabilities
Select ‘S-State’ in the Calculation Category field.

PR Employee Dedns/Liabs
Use Total Claim Amount field to enter the Total Claim Amount from the TD1 form.
Use the Authorized Tax Credits field to enter the Annual Amount from line 15 of the employee's TP-1016-V form. See [Authorized Tax Credits](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form/field-definitions-pr-employee-dednsliabs-form#ID-000377eb--en) for more information.
