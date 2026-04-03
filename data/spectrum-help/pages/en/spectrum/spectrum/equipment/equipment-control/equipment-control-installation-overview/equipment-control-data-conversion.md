---
title: "Equipment Control Data Conversion | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/equipment-control-installation-overview/equipment-control-data-conversion"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/equipment-control-installation-overview/equipment-control-data-conversion"
---

# Equipment Control Data Conversion

Below is a summary of the steps needed to complete
 installation.
It is important that these steps be performed in the order listed.

1. Complete the Equipment Control Installation screen.

1. Complete the Equipment Control portion of
 the Processing Date Change screen.

1. Set the processing dates for the new period using Processing
 Date Change.

1. Enter the equipment types using Equipment Type File
 Maintenance. Print the Equipment Type File Listing and check for accuracy.


1. Enter the cost category codes using Cost Category File
 Maintenance. Print the Cost Category File Listing and check for accuracy.


1. Enter the fuel and oil codes using Fuel / Oil File
 Maintenance. Print the Fuel/Oil File Listing and check for accuracy.

1. Enter the equipment status codes using Equipment Status File
 Maintenance. Print the Equipment Status File Listing and check for accuracy.


1. Enter Equipment Area codes using Equipment Area File
 Maintenance. Print the Equipment Area File Listing and review for accuracy.


1. Enter yard codes using Yard File Maintenance. Print the
 Yard File Listing and review for accuracy.

1. Enter equipment file information using Equipment. Print
 the Equipment File Listing and review for accuracy.

1. Enter quick equipment setup information, if desired, using
 Quick Equipment Setup Maintenance.

1. Enter the special job rates for equipment usage, if applicable,
 using Job-Specific Equipment Charge Rates. Print the Job/Equipment Rate File
 Listing and check for accuracy.

1. Confirm that there are no equipment transaction entries in
 progress, using Transaction Report and G/L Detail Report.

1. In General Ledger
 Installation, confirm that the Post to G/L checkbox is not
 selected for Equipment
 Control .

1. Enter the equipment cost and usage to-date as of the conversion
 date using Transaction Entry.

1. Print and update the Transaction Report (retain the
 printout), then post to G/L using G/L Detail Report.

If the Fixed Assets module is present on the system and should be converted in conjunction with Equipment Control depreciation conversion, please refer to the Fixed Assets Conversion Worksheet contained in the User's Guide.

1. Calculate depreciation, licensing, and insurance as of the
 conversion date using Build Ownership Cost Transactions.

1. Enter the actual life-to-date cost for the equipment depreciation,
 license, and insurance using DLI Entry. Print the Depreciation, License and
 Insurance Edit List and check for accuracy using DLI Edit List.

1. Update the depreciation, license, and insurance to Equipment
 Control records using Update DLI Cost.

1. Update the depreciation, license, and insurance to General Ledger
 records using DLI G/L Detail Report and Update.

1. Select the Equipment Control transactions checkbox on the
 General Ledger Installation screen's Properties tab, if the General Ledger
 module is present.

1. If converting at fiscal year-end, set the new year's balances
 using Open Forward Balance Update.

Note: To create the Equipment Revenue History
 file without falsifying the job, create a temporary conversion job with one phase with
 an Equipment cost type. For example, "E". Use this job in the Equipment Transaction Entry screen,
 by Job. After updating the Equipment
 Transaction Report screen, change the temporary conversion job status to
 Complete, and add an actual
 complete date in Job File
 Maintenance. Run the Deleted Completed Job update in the Period End Processing menu of
 Job Cost.
