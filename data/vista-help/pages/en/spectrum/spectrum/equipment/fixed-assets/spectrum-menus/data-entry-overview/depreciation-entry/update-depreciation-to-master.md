---
title: "Update Depreciation to Master | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry/update-depreciation-to-master"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry/update-depreciation-to-master"
---

# Update Depreciation to Master

This function updates the computed depreciation to the Fixed Assets File Maintenance and associated Fixed Assets history files. It prints a report of entries to be updated to the General Ledger for all assets not tied to Equipment Control. If an equipment code was recorded in Fixed Assets File Maintenance, then this update will also print a report of all entries posted to the Equipment Control depreciation transaction file (DLI Entry). Equipment Control entries update to Equipment Control, not the General Ledger, for depreciation.
When creating journal entries for Equipment Control transactions, the following hierarchy occurs:

1. First, if the fixed asset has an Equipment Control equipment code
 assigned in the Fixed Assets File Maintenance screen, Spectrum will look to the fixed
 asset's G/L Control Code.

1. Spectrum will next look to the G/L Control Code Maintenance screen
 to see if an equipment code is assigned in the Equipment expense account code field;
 if one is assigned, Spectrum will debit this account when creating the transactions
 for Equipment Control. If the Equipment expense account code field is blank, Spectrum
 will look to the equipment code's equipment type and use its debit depreciation
 code.

1. If the equipment control depreciation code is left blank in this
 screen, then Spectrum will used the Fixed Assets G/L control code expense when
 updating to Equipment Control.

1. If you attempt to enter this screen before running the
 Build Depreciation Transactions,an error message will
 display.
Important: The depreciation
 calculation must be run before selecting this option. Additionally, this report
 should be retained as a permanent record of the company.

Related information

- [Update Depreciation to Master Files - Sample Report](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry/update-depreciation-to-master/update-depreciation-to-master-files---sample-report)

- [Fixed Assets G/L Summary Report - Sample Report](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry/update-depreciation-to-master/fixed-assets-gl-summary-report---sample-report)
