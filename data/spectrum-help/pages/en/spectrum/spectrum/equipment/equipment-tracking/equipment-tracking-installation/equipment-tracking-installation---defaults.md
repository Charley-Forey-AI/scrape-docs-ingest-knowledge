---
title: "Equipment Tracking Installation - Defaults | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-tracking/equipment-tracking-installation/equipment-tracking-installation---defaults"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-tracking/equipment-tracking-installation/equipment-tracking-installation---defaults"
---

# Equipment Tracking Installation - Defaults

Use this tab to define Equipment Tracking defaults. These settings can be changed as needed at any time.
Fields
Descriptions

Equipment phase, cost type
Enter the default phase to display during equipment tracking processing for the equipment class. Only alpha characters and numeric values are allowed, and up to 20 characters are allowed.
The phase will be operational only during direct cost requisitions. This phase is used as the default in the Equipment Tracking Requisition screen.

Inventory phase, cost type
Enter the default phase to display during equipment tracking processing for the inventory class. Only alpha characters and numeric values are allowed, and up to 20 characters are allowed.
The phase will be operational only during direct cost requisitions. This phase number is used as the default in the Equipment Tracking Requisition screen.

Small tools phase, cost type
Enter the default phase to display during equipment tracking processing for the small tools class. Only alpha characters and numeric values are allowed, and up to 20 characters are allowed.
The phase will be operational only during direct cost requisitions. This phase number is used as the default in the Equipment Tracking Requisition screen.

Default transaction code
Enter the default transaction code, or click the drop-down arrow to select from a list of transaction codes.
During Equipment Tracking Requisition, the transaction code will default. If a default transaction code is not entered in this screen, then no transaction code will default and you must enter a code for each requisition.

Next requisition number
Enter the next equipment tracking requisition sequence number the system should assign during Equipment Tracking Requisition. Spectrum features auto-count equipment tracking requisition numbers for ease of entry. This feature can be overwritten by specifying a desired sequence number when adding equipment tracking requisitions.
If you are already using the Equipment Tracking module, the most recently used requisition sequence number is displayed, and can be changed if desired. The number is updated automatically during equipment tracking requisition processing, and will then be used to offer the next higher number as a default when you enter requisitions.
In order for the system to sort these requisitions properly and in sequential order, it is important to set up an appropriate numbering system. Unless leading zeroes are used, the system will sort as "1", "10," "100," then "2," "20," and "200," and so forth. If leading zeroes are used, the requisitions will sort as 001, 002, 003 ... 099, and so forth. All codes will then be three digits long and, as long as you don't go to 1000, the requisitions will sort properly.

Default billing period
Select the default billing period option corresponding to the expected issues billing period you want to display in the Equipment Tracking Requisition screen.
If you select None, the system will not prompt for an expected billing period.
If this option is set to Daily, Weekly, or Monthly, the system starts billing requisitions at the level in the Rates brackets (Daily, Weekly, or Monthly) and skips any levels above it in the Rate brackets setup. For example, if the Default billing period is set to W for weekly and a requisition is entered, no matter how little time elapses between issue and billing, the Weekly rates will be used first, then Monthly next, if appropriate. The Hourly and Daily rates would not be used at all.
