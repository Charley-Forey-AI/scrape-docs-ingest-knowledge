---
title: "Payroll Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/hr-and-payroll/payroll-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/hr-and-payroll/payroll-features"
---

# Payroll Features

Vista 2023 R1 delivers on user-requested Payroll enhancements, fixes, and other improvements.

## Improved Pay Period Close Process

When you close a pay period in PR Pay Period Control, you are now presented with the option to run Leave Entry for accrual/usage updates. This new prompt appears after you are given the option to run the ledger update and the ledger update has been completed. If you select Yes (recommended), the system presents you with the batch selection form so that you can open a PR Leave Entry batch and process leave.
 If you select No, the pay period's final leave update will be considered completed. However, this is not recommended, especially if you processed timecards that affect leave (that is, the timecards are associated with a leave entry earn code), since it can cause errors later due to unbalanced or negative leave.
For information about closing a pay period, see [Close a Pay Period](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-closingopening-pay-periods/close-a-pay-period).

## Added Support for Aatrix FFD/EFF Functionality

You now have the ability to use the FFD/EFF functionality offered by Aatrix to handle employee data requirements for state reporting.

A new "Aatrix ID Values" tab was added to the PR Employees form to enable setting up Aatrix IDs that identify additional employee data unique to various state regulatory reports (for example, the 7-digit NAICS, Corporate Officer identification, and Coverage Types needed for Wyoming unemployment reporting). This new tab includes the following fields:

- [Aatrix ID](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#concept-8993--en)

- [Value](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#concept-2688--en)

- [Memo](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#concept-4448--en)

You can set up multiple Aatrix IDs for each employee as needed based on your company's reporting needs. When you initiate regulatory reporting via the PR Aatrix Report Selection form, the system passes the applicable Aatrix IDs and their corresponding values (based on the state and report selected) to Aatrix.
For more information, see [Set up Aatrix IDs for State Regulatory Reporting](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-aatrix-ids-for-state-regulatory-reporting).

## More efficient use of the Vista application

Processes which occupy the Vista client for extended periods - such as printing a long list of Payroll Checks or Direct Deposit Stubs - can now run in the background and allow you to proceed to other tasks.
Until Vista completes processing of any given task, the task appears in the Background Jobs form. If at any time you want to check the progress of a background task, you can open the Background Jobs form and view any remaining jobs in the queue, and without affecting processing in any way.
To open the form, go to the Main Menu > View > Display Job Queue. Once Vista completes a given task, the Background Jobs form removes the task from the list.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
