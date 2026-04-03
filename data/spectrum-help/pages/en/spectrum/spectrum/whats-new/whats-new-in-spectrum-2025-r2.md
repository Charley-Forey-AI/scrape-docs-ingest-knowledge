---
title: "What's New in Spectrum 2025 R2 | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/whats-new/whats-new-in-spectrum-2025-r2"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/whats-new/whats-new-in-spectrum-2025-r2"
---

# What's New in Spectrum 2025 R2

This release focuses on enhancing reporting flexibility, streamlining Accounts Payable processes, and providing key payroll/regulatory updates for year-end 2025.

## Reporting and Data Export Enhancements

We've added a new dedicated CSV format option to several reports, to improve data processing and analysis.

- G/L Detail Activity Report - Detail activity CSV

- G/L Transaction Journal - Transaction journal CSV

- Job Cost History Report - Detail history CSV

- Time Card History Report - Detail CSV

- Detail Billing History Report - Detail activity CSV

This new format includes report headers only once at the top of the file.

## Year-End and Regulatory Updates (2025)

Updates have been made to comply with the latest 2025 year-end requirements from the CRA and IRS.
Canadian T4 Export: The Export T4 functionality is aligned with the latest CRA guidance, which no longer writes blank spaces or 0.00 in optional fields in the XML file.
Tax Statement Instructions: The My Year End Tax Statement app has been updated with the latest instructions for Form W-2 and 1095-C.
Vendor Forms:

- The Golden parachute field and dollar amount has been added to the 1099-NEC form and removed from the 1099-MISC form.

- The Total Paid field on Form T5018 has been enhanced to accommodate a larger dollar amount (up to 9,999,999,999.99).

## Payroll & Tax Logic Enhancements

Permanent State Disability Insurance (SDI) State: A new override feature allows the Payroll Admin to designate a specific state for SDI tax calculations, which will be used even if the employee's resident and work states are different.Note: This new field has also been added to the Employee Payroll Tax Import process and Excel template via the SDX module.

T4 Slips

- CPP Limit Override: When building T4 Slips, the system now displays the current CPP earnings limits with the option to override them. This is useful when processing T4s for a prior year.

- Separate Totals: The T4 Listing now includes separate totals for CPP1 (First Additional Contribution) and CPP2 (Second Additional Contribution).

Tax Table Import: An 'Import Only' option has been added to allow users to skip the optional Listing (preview) step during the Tax Table Import process.
Audit Log: The Pay Cycle Settings table (PR_CYCLE_SETTINGS_MC) is now tracked in the Audit Log to help with reconciling tax calculation differences. For the current list of all tables tracked, see [Audit Log Tables](/en/spectrum/spectrum/system-administration/audit-log-tables).

## Accounts Payable (AP) Improvements

The Automatic Invoicing and ePayments processes have been updated to provide greater efficiency and visibility.

- ePayments Return File API: The system can now use an API to directly download all available ePayments return files from the AP Gateway. This eliminates the need to manually download and import the CSV files. See [Import ePayments Return File](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/import-epayments-return-file).

- Pending Automatic Invoices Management:

- New Report: The new [Pending Automatic Invoice Report](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/reports-overview/pending-automatic-invoice-report) provides counts and totals for invoice, sales tax, and total amount, which can be useful for month-end accruals.

- Enhanced Search: Purchase order number, operator code, operator name, and message text have been added to the Advanced Search options for pending automatic invoices.

- Purge Option: A Delete All button is now available in the Search Pending Automatic A/P Invoices window to quickly purge the list when needed.

## Other Module and System Updates

SDX (API): A new web service and corresponding Excel template are now available to update existing customer information. See [Update Customer](/en/spectrum/spectrum/api-web-services/list-of-web-services/accounts-receivable-services/update-customer).
Job Costing Phase Copy (JC): The Phase Copy function now defaults to copying only selected unions that have *active wage codes*.
Job Cost History Report (JC): The Job Cost History report can now be filtered by Equipment Code.
Credit Cards (CM): The employee code has been added to the Sub-account listbox to support the setup of the upcoming Traqspera Premium Expenses application.
Confidential Payroll Report Companies (CP): All companies listed on this page are now required to be consistent in their use of entities (that is, all set to "Yes" or all set to "No"). This restriction is enforced upon adding a new company or changing an existing company's entity setting. See [Confidential Payroll Report Companies](/en/spectrum/spectrum/accounting/confidential-payroll/confidential-payroll-screens/confidential-payroll-report-companies).
System Maintenance Removal: The following outdated maintenance features have been removed, as these functions are now managed using Trimble ID:

- Restriction Times Maintenance page

- Access Times Maintenance page

- The Disable Logon option found in System Admin > Upgrade

## Trimble Assistant for Spectrum - Beta Release

Spectrum now includes a beta version of the Trimble Assistant chat agent. Use this assistant to ask specific questions about the tasks you can perform in Spectrum.
For details, see [About Trimble Assistant - Beta](/en/spectrum/spectrum/whats-new/about-trimble-assistant---beta).

## Spectrum 2025 R2 Bug Fixes

This release includes fixes to customer-reported issues. To see the list:

1. Log in to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues?tabset-d4f10=2) of the Viewpoint Customer Portal.

1. Make your selections in the product and module filter options.

1. In the Fixed in Version field, enter 2025 R2.

1. Select Apply Filters
