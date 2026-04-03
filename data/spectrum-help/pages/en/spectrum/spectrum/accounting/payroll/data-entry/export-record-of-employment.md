---
title: "Export Record of Employment | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/export-record-of-employment"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/export-record-of-employment"
---

# Export Record of Employment

This screen allows users to generate a Record of Employment
 (ROE) report.
Use this screen to
 select which employees to include in the export file and specify certain parameters for the
 export file. After making selections in the Build Employee List for
 Export window, and prompting for certain file settings, the software
 displays a list of (potential) employees to include in the export. You can then remove any
 employees that should not be included on the report and click
 Continue to initiate the export update.Note: This screen is only available if you have set the Payroll Installation > Payroll reporting option to 'Canada'.
About the ROE
 generated from this screen:

- The Record of
 Employment (ROE) is the form that Canadian employers must complete
 for employees receiving insurable earnings who stop working and experience an
 interruption of earnings. Insurable earnings include most of the different types
 of compensation provided to employees in which employment insurance (EI) premiums
 are paid. While the Canada Revenue Agency (CRA) determines what types of earnings
 and hours are insurable, it is Service Canada who manages the EI benefits.

- Spectrum supports the electronic ROE format only.

- In the event that a revised ROE is required, you should submit
 these changes directly to Service Canada's website.

- Spectrum does not support the 'weekly average formula'
 calculations for commission-only employees.

- The ROE compilation might include an employee that is exempt
 from ROE reporting. In this cases, the Payroll Administrator would manually remove
 them from the exports start screen. Alternatively, a specific employee status
 could be created to represent these types of employees. This status would then be
 excluded when running the compilation.

- The CRA Payroll Account Number is set to the first 15
 characters of the Spectrum federal tax code's tax ID number.

- The export file is in XML format, following ROE WEB Version
 2.0.

- Employment dates in Spectrum are calculated as follows:

- First Day
 Worked (B10 in the file): Spectrum will use the Rehire date,
 or if that doesn't exist, the Hire date. If both fields are blank, Spectrum
 will use the first time card date after the last ROE submission for this
 employee. If there is no ROE history for the selected employee, the system
 will use the first time card date worked in Spectrum.

- Last Day
 for Which Paid (B11 in the file): Spectrum will use the last
 day for which the employee had hours in Time Card History to determine the
 last day for which paid.

- Final Pay
 Period Ending Date (B12 in the file): Spectrum will use the
 most recent pay period ending date, up to the Earnings Calculations Submit
 through date.

1. Select Insurable Earnings and Build the file.

1. Set up [Insurable Earnings Maintenance](/en/spectrum/spectrum/accounting/payroll/data-entry/export-record-of-employment/insurable-earnings-maintenance) via the
 available button, and then return to this Export screen to enter selections for
 employees to include and then click Build. A list of qualifying
 employees will display for review. Remove any employees that should not be
 submitted before creating the export file.

- In addition to the field selections found below, an employee
 must also have reportable earnings in Payroll Cheque History based on the
 'Submit through' date. The system looks for reportable earnings from
 approximately one year ago (based on employee's pay frequency) unless a ROE has
 been submitted for the employee since then.

- Only regular and manual checks are reviewed to determine if
 reportable earnings exist. Void check amounts will be used later when compiling
 the export file.

1. Complete submission details, finalize employee list, click Export.

1. Complete the Submission details and Company
 contact information. The Comment field should only be
 used to submit information regarding specific cases as defined in the Service
 Canada documentation.

1. Review the employees on the screen. As needed,
 highlight and click Remove to not include the employee in the export. The ability
 to multi-select records is provided. Click the Export option on the Command
 Bar.

1. Reset ROE records to Unsubmitted and Generate a New
 Export File.

1. To view the ROE history for an employee, click
 the History button.
 This will be useful for HR Managers who want to review previous ROE's
 submitted.

1. Click the Reset to Unsubmitted button
 to reset the ROE records back to 'Unsubmitted' and then generate a new export
 file, as if for the first time. This is useful if you were to export the ROE
 file with pop-up blockers on and need to re-submit the file. This will not
 submit a corrected ROE record.
