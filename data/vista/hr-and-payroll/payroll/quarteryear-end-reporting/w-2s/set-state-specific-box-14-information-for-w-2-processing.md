---
title: "Set State-Specific Box 14 Information for W-2 Processing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/set-state-specific-box-14-information-for-w-2-processing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/set-state-specific-box-14-information-for-w-2-processing"
---

# Set State-Specific Box 14 Information for W-2 Processing

You can set state-specific deductions to the Box 14 tab in PR W-2 Process so that they will print in Box 14 of the W-2.

Use the Box 14 Information tab in PR W-2 Process to enter descriptions for Box 14 of state/local W-2s when you want to report state-specific earnings, deduction, or liability information (e.g., CA SDI or AK ESC). The system uses the earnings/deduction/liability (EDL) codes and types to determine where to get the amounts for each item that you enter on this tab.Using this tab, you can enter as many records as you want, but the system will print only the first eight (8) records with amounts greater than zero on W-2s. Additionally, the system only allows you to add up to twelve (12) lines per state on this form.
To set state-specific deductions for processing W-2s:

1. In the State field, enter the state or press F4 to select from a list of states.

1.  In the Line field, enter a line number to add a state-specific record. Note: The system processes lines in numerical order (from smallest to greatest, regardless of the actual numbers that you use). To assist you in keeping track of the number of records per state, you should enter 1 for the first record that you create for an individual state and continue on in sequential order. If you do not enter 1, the system will display a warning, but will allow you to save the record.

1. From the EDL Type drop-down, select the type of code you are adding: Earnings, Deduction, or Liability.

1.  In the Code field, enter the EDL code or press F4 to select from a list of codes.

1. In the Description field, enter a description for the code or accept the default.

1. Save the record.

1. For New Jersey users only:Enter the code you have defined for the following state-specific information as needed (make sure you have set these codes up with the appropriate Aatrix tax type).
ItemAatrix Tax Type
NJ State Unemployment - Employee (UI)1094
NJ Workforce (WF/SWF)2020
NJ Health Care Subsidy2018
NJ State Disability Ins - Employee (SDI)5402

Note: If you have Private Family Leave Insurance and/or Private Disability Insurance plans, you can set those up here only for the purpose of printing the Vista PR W2 Preview Report and PR W2 Employee Copies reports. This information is not passed to Aatrix; you must set these items up manually in the Aatrix wizard when filing W-2s. For more information, see [File W-2s Using Aatrix](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/file-w-2s-using-aatrix).

1. For New York users only:You may want to configure NY State W-2s to display the NY State earned wages on a line in Box 14. Follow the steps below to make the line display the Subject Amount from PR Employee Accumulations.Note: Using the New York state withholding deduction/liability code is the only case in which the Subject Amount from PR Employee Accumulations will display in Box 14. Using any other deduction/liability code will display the Amount from PR Employee Accumulations instead. For this functionality to work for the state of New York, a state W-2 must be printed for New York.

1. In PR State Information form, in the State field, enter NY or press F4 to select NY from a list.

1. In the Tax Dedn field, take note of the deduction code being used for New York State withholding tax.

1. In PR W-2 Process, open the State Box 14 Information tab.

1. In the State field, enter NY.

1. In the Line field, enter a line number.

1. In the EDL Type field, enter D-Deduction.

1. In the Code field, press F4 to select the deduction code for the New York state withholding tax (that you took note of in Step 2).

1. In the Description field, enter NY State Wages (or something similar).

1. Select Initialize State Box 14.

1. For Oregon users only:To report Oregon Transit Tax withheld for employees residing or working in Oregon, you must add the Oregon Transit Tax deduction to the Box 14 list in PR W-2 Process. However, when you generate the W-2s (via Aatrix), the Oregon Transit Tax prints in the Local section in Boxes 18, 19, and 20; it does not print in Box 14.

 You can now continue with W-2 processing.

Related information

- [PR W-2 Process Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/pr-w-2-process-form)

- [Process W-2s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/process-w-2s)
