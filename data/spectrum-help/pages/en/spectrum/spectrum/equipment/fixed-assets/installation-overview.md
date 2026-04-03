---
title: "Installation Overview | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/fixed-assets/installation-overview"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/fixed-assets/installation-overview"
---

# Installation Overview

On the Site Map, select System Administration and then select Installation. From the Installation list, select Company. Note that the System Administrator should have previously completed this screen.
Ensure that the checkbox for this specific module has been selected.
Fixed Assets Data Conversion
Below is a summary of the steps needed to complete installation. It is important that these steps be performed in the order listed.

## Fixed Assets Data Conversion: Part I - Setup

1. Enter Fixed Asset department codes using [Department Code File Maintenance](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/maintenance-overview/department-code-file-maintenance).

1. Print the [Department Code File Listing](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/maintenance-overview/department-code-file-maintenance/department-code-file-listing) and check for accuracy.

1. Enter General Ledger control codes using [G/L Control Code Maintenance](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/maintenance-overview/gl-control-code-maintenance).

1. Print the [G/L Control Code File Listing](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/maintenance-overview/gl-control-code-maintenance/gl-control-code-file-listing) and check for accuracy.

1. Enter MACRS tables, if necessary, using [MACRS Table Maintenance](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/maintenance-overview/macrs-table-maintenance).

1. Print the Accelerated Cost Recovery System (MACRS) Tables.

1. Enter fixed assets file information using [Fixed Assets File Maintenance](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/maintenance-overview/fixed-assets-file-maintenance). Enter assets acquired through prior fiscal period before doing Part II below. Enter assets acquired during the current fiscal year after step 10 and before step 12 in Part II below. Assets that link to equipment need to have the equipment code entered on the asset. Do NOT enter life-to-date depreciation on this screen.

1. Print the [Fixed Assets File Listing](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/maintenance-overview/fixed-assets-file-maintenance/fixed-assets-file-listing) and check it for accuracy.

1. Set the processing date to the conversion date (prior year-end date) using the [F/A Processing Date Change](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/fa-processing-date-change) screen.

## Fixed Assets Data Conversion: Part II - Conversion

1. On the [General Ledger Installation - Properties](/en/spectrum/spectrum/accounting/general-ledger/general-ledger-installation-overview/general-ledger-installation---properties) screen, in the 'Post to G/L' section, make sure the Fixed Assets checkbox IS selected.

1. On the[General Ledger Installation - Properties](/en/spectrum/spectrum/accounting/general-ledger/general-ledger-installation-overview/general-ledger-installation---properties) screen, in the 'Post to G/L' section, make sure the Equipment Control checkbox is NOT selected.

1. In Equipment Control, Calculate depreciation as of the prior year-end. Nothing will show up in the build list.

1. In Fixed Assets, to begin entering the life-to-date figures on your assets, calculate depreciation as of last year's fiscal end date using Build Depreciation Transactions.

1. Print the [Depreciation Edit Listing](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry/depreciation-edit-listing)

1. In Fixed Assets, Depreciation Entry/Edit, make changes as necessary to "curr depr" for Book, Tax and Other, so that the current depreciation equals life-to-date depreciation as of prior year-end.

1. Reprint the associated edit listing as necessary. Retain the printout.

1. Update Fixed Asset depreciation using the Depreciation Entry - [Build Depreciation Transactions](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry/build-depreciation-transactions) button and then the [Update Depreciation to Master](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry/update-depreciation-to-master) button. You will receive a GL Transaction Report for non-equipment assets. You will need to create a journal entry to reverse these transactions. You will also receive and Equipment Transfer Report.

1. Print the [Fixed Assets Additions Register](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/reports-overview/fixed-assets-additions-register) and Purge the Fixed Assets Additions Register.

1. In Equipment Control > Data Entry > Ownership Costs, update the depreciation and select the Update G/L button.

1. Enter assets acquired in current fiscal year. Do you need to update current year depreciation to the General Ledger? Or do you need to just update the assets themselves? The instructions below are for updating just the assets and not the General Ledger. If you need to update both the General Ledger and the assets, please refer to the instructions at the end of this document.

1. In Equipment Control, calculate depreciation as of the conversion date.

1. In Fixed Assets > [Depreciation Entry](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry), calculate current year depreciation as of the conversion date for Book, Tax and Other.

1. Print the Fixed Assets > [Depreciation Edit Listing](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry/depreciation-edit-listing).

1. In Fixed Assets, Depreciation Entry make changes as necessary to current depreciation for Book, Tax and Other, so that the current depreciation equals the current year-to-date depreciation.

1. Reprint the associated edit listing as necessary. Retain the printout.

1. Update depreciation using [Update Depreciation to Master](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry/update-depreciation-to-master) in [Depreciation Entry](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry).

1. In Equipment Control, update the depreciation and run the G/L update.

1. On the[General Ledger Installation - Properties](/en/spectrum/spectrum/accounting/general-ledger/general-ledger-installation-overview/general-ledger-installation---properties) screen, in the 'Post to G/L' section, make sure the Equipment Control checkbox IS selected.

1. On the [General Ledger Installation - Properties](/en/spectrum/spectrum/accounting/general-ledger/general-ledger-installation-overview/general-ledger-installation---properties) screen, in the 'Post to G/L' section, make sure the Fixed Assets checkbox IS selected and designate the General Ledger update method for Fixed Assets (Book or Tax). Usually you will want to use Book.

1. Set the processing dates to the new period for Fixed Assets using Processing Date Change.

## Fixed Assets Data Conversion: Part III - Ongoing Processing

1. On the[General Ledger Installation - Properties](/en/spectrum/spectrum/accounting/general-ledger/general-ledger-installation-overview/general-ledger-installation---properties) screen, in the 'Post to G/L' section, make sure the Equipment Control checkbox IS selected.

1. On the [General Ledger Installation - Properties](/en/spectrum/spectrum/accounting/general-ledger/general-ledger-installation-overview/general-ledger-installation---properties) screen, in the 'Post to G/L' section, make sure the Fixed Assets checkbox IS selected and designate the General Ledger update method for Fixed Assets (Book or Tax). Usually you will want to use Book.

1. Set the processing dates to the new period for Fixed Assets using Processing Date Change.

1. In Equipment Control, calculate depreciation as of the period end date.

1. In Fixed Assets > [Depreciation Entry](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry), calculate current period depreciation as of the period end date for Book, Tax and Other.

1. Print the Fixed Assets > [Depreciation Edit Listing](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry/depreciation-edit-listing).

1. In Fixed Assets > [Depreciation Entry](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry), make changes as necessary to current depreciation for Book, Tax and Other, so that the current depreciation equals the current period depreciation.

1. Reprint the associated edit listing as necessary. Retain the printout.

1. Update depreciation using the [Update Depreciation to Master](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry/update-depreciation-to-master) button in [Depreciation Entry](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/data-entry-overview/depreciation-entry).

1. In Equipment Control, update the depreciation and run the GL update.

Related information

- [Installation Overview](/en/spectrum/spectrum/equipment/fixed-assets/installation-overview)
