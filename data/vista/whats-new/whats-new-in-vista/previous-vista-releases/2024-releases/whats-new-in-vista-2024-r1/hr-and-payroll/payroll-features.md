---
title: "Payroll Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/hr-and-payroll/payroll-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/hr-and-payroll/payroll-features"
---

# Payroll Features

Vista 2024 R1 delivers on user-requested Payroll enhancements, fixes, and other improvements.

## Added Report Type Filtering for Aatrix ACA History

When you launch the Aatrix History feature from the PR Aatrix - ACA Print & eFile form (by selecting the History button), the report history grid now shows only ACA history. In addition, the All Available Form Types filter no longer includes non-ACA report types; only the ACA report type option is available. Previously, the ACA report history grid and the All Available Form Types filter included all report types (for example, 1099s, W2s, ACAs, etc.).
Another change includes the removal of ACA report history from all other other history screens (W-2s, 1099s, and other general payroll history lists).

## Improved Check Print Success Message

When you print checks via PR Check Print and have a successful print run, the success message now includes the check range. Message will appear as shown in the following example:

## Unemployment Reporting Includes SOC codes for SC (U.S. Only)

The state of South Carolina now requires employers to include
 Standard Occupational Classification (SOC) codes in their unemployment
 reporting.
To meet this requirement, Vista's PR
 Unemployment reporting process now adds SOC codes when generating unemployment data,
 and passes these codes to Aatrix.
To ensure proper reporting, if you haven't
 already, you must:

- Define SOC codes in the [PR Occupational Categories Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-occupational-categories-form)

- Assign the SOC codes to employees as needed in the PR
 Employees form [Occupational Category](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-00038176--en) field

Aatrix unemployment report impacted:

- SC UCE-120 Report

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
