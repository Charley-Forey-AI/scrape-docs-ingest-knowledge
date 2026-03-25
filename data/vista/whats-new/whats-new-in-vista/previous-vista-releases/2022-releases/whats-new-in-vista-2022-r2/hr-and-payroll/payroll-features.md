---
title: "Payroll Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r2/hr-and-payroll/payroll-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r2/hr-and-payroll/payroll-features"
---

# Payroll Features

Vista 2022 R2 delivers on user-requested Payroll enhancements, fixes, and other improvements.

## Improved Direct Deposit Processing

Vista can now process direct deposit for more than one employee at a time. If you use this option, the overall time required by Vista to process all employees paid via direct deposit may be reduced.
Vista's default behavior remains the same: process direct deposit records one at a time, completing all processing tasks for the current employee record before beginning processing on any other employee record.
If you select the new Parallel Direct Deposit checkbox in the PR Company Parameters form, Vista doesn't necessarily wait until it's done processing an employee direct deposit record before starting on any remaining employee direct deposit records.
Note: Using this option will not have the same effect on all organizations. Any cumulative impact is dependent on several factors, which means you may not notice a difference if your current processing is not impacted by the underlying changes.

## New Federal Tax Exempt Flag for U.S.

You can now flag an employee as exempt from Federal tax withholding, eliminating the need to set up an calculation override for Federal Withholding deduction codes.
A Federal Tax Exempt checkbox was added to the PR Employees form, Add'l Info tab. When selected for an employee, the system calculates a zero amount for Federal withholding during payroll processing, overriding any calculation overrides you may have set up for the employee/deduction code in the PR Employee Dedns/Liabs form.
Also added a Federal Tax Exempt checkbox to the HR Resources form. For information, see [Human Resources Features](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r2/hr-and-payroll/human-resources-features).
Note: If the W4 Info checkbox in the HR Company Parameters form is selected, your changes to the Federal Tax Exempt checkbox in either the HR Resources or the PR Employees form automatically updates the corresponding checkbox in the other form. If the W4 Info checkbox is not selected, a change in either form must be applied manually in the other.

## Generate Electronic Files for Federal W-2s in Vista

With this release, you can now use Vista to generate files for electronic submission of Federal W-2s. This functionality was added back to Vista to accommodate companies that don't have Aatrix available in their jurisdiction.
Changes made to accommodate this functionality include:

- Restored the PR W-2 Electronic Filing form and renamed it "PR Generate W-2 e-File". You can use this form to export your Federal W-2 data (only) to an electronic file for submission to the Social Security Administration (SSA). Filtering options allow you to filter employees included in the e-file by state and local code. See also [ PR Generate W-2 e-File Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/pr-generate-w-2-e-file-form).

- Added a Generate W-2 e-File link back to the Tasks and File menus in the PR W-2 Processing form. Clicking this link opens the PR Generate W-2 e-File form.

For more information about generating an electronic file for federal W-2s, see [Create a Federal W-2 Electronic File](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/create-a-federal-w-2-electronic-file).

## Electronic Delivery Consent for W-2s and 1095s (US only)

In support of the IRS allowed consent for electronic delivery of year-end filing information, you can designate whether an employee has consented to receive W-2s and 1095s via email. Aatrix supports both direct mail and email of W-2s and 1095s, allowing you to save on mailing costs by having W-2s and 1095s sent via email to those who have consented.
We made changes in these forms:
PR Employees:Added new W-2 Email Consent and 1095 Email Consent checkboxes to the Add'l Info tab, above the Pay Info section.Selecting these checkboxes indicates the employee has consented to receive W-2s and/or 1095s via email, and requires that an email address be specified for the employee. If the employee wishes to receive paper copies of W-2s and/or 1095s via direct mail, leave the applicable checkbox(es) unselected.
During processing of either W-2s or 1095s, the setting in this form is applied by default, but you may override either or both at that time.
For more information, see [Set an Employee to Receive W-2s and 1095s via Email](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-an-employee-to-receive-w-2s-and-1095s-via-email).
PR W-2 Employee Edit form:Added a new W-2 Email Consent checkbox to the Info tab. The default setting for this checkbox matches whatever is set on the corresponding checkbox in the PR Employees form. You may override the setting for the employee and reporting year; however, if you change the checkbox to selected for a reporting year/employee, the employee must have an email address specified in PR Employees.When you launch the Aatrix via the PR W-2 Process form (Tasks > Launch Aatrix Print and eFile), the setting defined here is sent to Aatrix and determines how Aatrix will handle delivery of W-2s for the employee.
PR ACA 1095-C Employee:Added a new 1095 Email Consent checkbox to the Info tab (Part 1 - Employee section). The default value of this checkbox matches whatever is set on the corresponding checkbox in the PR Employees form. You may override the setting for the employee and reporting year; however, if you change the checkbox to selected for a reporting year/employee, the employee must have an email address specified in PR Employees.When you launch Aatrix via the PR ACA Process form (Tasks > Launch Aatrix Print and eFile), the setting defined here is sent to Aatrix and determines how Aatrix will handle delivery of 1095s for the employee.

## Updated Oregon Multnomah County / Portland Metro Routines (U.S. only)

New stored procedures were added to the Multnomah County and Portland Metro tax routines (bspPRMultnomahORC22.sql and bspPRPDXMetroORC22.sql, respectively) for computing tax when subject earnings amounts exceed the specified thresholds.
These new stored procedures require some additional setup to enable accurate tax computations as follows:
Multnomah County Income Tax

- In the PR Deductions/Liabilities form, use the Rate/Amount #1 and Rate/Amount #2 fields to enter the tax rates.

- In the PR Routines form, use the Misc Amt #1 - Misc Amt #4 fields to set up the threshold amounts.

For more specific instructions, see [OR Multno](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states/north-carolina-philadelphia#ID-000332be--en__OR_Multno) in the tax routine tables.
Portland OR Metro Income Tax

- In the PR Deductions/Liabilities form, use the Rate/Amount #1 fields to enter the tax rate.

- In the PR Routines form, use the Misc Amt #1 and Misc Amt #2 fields to set up the threshold amounts.

For more specific instructions, see [OR PDX Met](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states/north-carolina-philadelphia#ID-000332be--en__OR_Metro) in the tax routine tables.

## Support State Tax Withholding from Resident and Work State

If your state requires withholding for all residents, even if they are working in another state, you now have the ability to have tax deducted for both the resident and posted (work) state when no reciprocal agreement exists between the states.
To enable this functionality, the Post Difference to Resident State checkbox in the PR State Information form was replaced by a new Calculate Tax Option section where you can define the behavior using these radio buttons:

- Posted Only - The system calculates tax for the posted state only, regardless of the employee's resident state.

- Full Tax for Both Posted and Resident when No Reciprocity

- If no reciprocal agreement exists between the posted and resident state: the system calculates and deducts tax for both states.

- If a reciprocal agreement exists: the system calculates and deducts only the resident state tax.

- Both with Difference to Resident - The system calculates tax for both the posted state and resident state, if the posted and resident states are different.

- If the resident state tax is higher than the posted state tax: the system deducts the full amount of the posted tax, but only the difference is deducted for the resident state.

- If the posted state tax is higher than the resident state tax: the system deducts the full amount of the posted tax, and does not deduct any resident state tax.

## Unemployment Reporting Includes SOC codes for AK and WA (U.S. only)

The states of Alaska and Washington recently started requiring employers to include Standard Occupational Classification (SOC) codes in their quarterly unemployment reporting.
To meet this requirement, Vista's PR Unemployment reporting process now adds SOC codes when generating unemployment data, and passes these codes to Aatrix.
If you haven't already, and to ensure proper reporting, you must:

- define SOC codes in the PR Occupational Categories form

- assign the SOC codes to employees as needed in the PR Employees formNote: For the state of Alaska, you must also assign geographic codes to employees in the PR Employees form. Vista passes both to Aatrix.

Aatrix unemployment files impacted:

- Alaska - AK TQ01C Efile Report

- Washington - WA 5208 A eFile Report

## Deleted Timecards Can Be Recovered

Retaining 'deleted' timecards makes it possible to assess timecards that may have been deleted in error, and restore them if needed. To make this possible, when you delete a timecard in any of the PR Timecard Entry, HR Management, or Field Management forms, Vista now creates an associated record for that timecard and adds it to the new vPRTimeCardSafetyNet database table.
Timecards can be recovered only only via the HR Management or Field Management web applications and only by Timecard or System Admins in those applications. See [Timecard Safety Net User Guide](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:HRV_000031:HRV:HRV).

## Recoverable Timecard Records can be Purged

When purging pay periods in the PR Purge form, the system now also purges records in the vPRTimecardSafetyNet table, if they meet the purge criteria.
Once you specify the payroll group(s) and through date, the purge process deletes all applicable records from the vPRTimecardSafetyNet table matching the PR company, PR Group, and PR Ending Date.
For more information about purging pay periods, see [Purge Pay Periods](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/purge-pay-periods).

## Removed Restart Employee Amounts Initialization (CAN only)

Removed the Restart Employee Amounts Initialization button from the PR Company Parameters form (for companies with Canada payrolls only), as it is no longer being used.

## Update for Aatrix CA Pay Data Report

For companies with California employees only.
Updated the procedure that passes payroll data to Aatrix for the CA Pay Data Report to include hours and the correct Race/Ethnicity/Sex codes as required by California state law.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
