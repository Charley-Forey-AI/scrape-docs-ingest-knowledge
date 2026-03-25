---
title: "Set Up Equipment Depreciation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/depreciation/set-up-equipment-depreciation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/depreciation/set-up-equipment-depreciation"
---

# Set Up Equipment Depreciation

You can set up equipment asset records so that the system will create and post depreciation entries to GL when you run the EM Depreciation Processing program
The following outlines the basic steps to setting up your equipment for depreciation processing.

1. HQ Company Setup – Confirm that the company is set up in the correct Default Country. Depreciation calculations are handled differently in the US, Canada, and Australia.

1. EM Cost Types/EM Cost Codes – Set up the cost type and cost code for posting depreciation costs. Typically, this will be a separate Ownership Costs or Depreciation cost type and a Depreciation cost code for effective presentation on reports.

1. EM Departments – Make sure the depreciation cost type (on the Cost Types tab) has an assigned GL account for debiting depreciation entries, and that you enter the offsetting account in the Accumulated Depreciation GL Account field (Info tab).

1. EM Company Parameters – Specify your designated cost code and cost type in the Depreciation Cost Code and Depreciation Cost Type fields (Info tab). Decide whether you want the system to ensure you complete all depreciation posting before allowing you to close in GL by setting the Calculations Required option to Monthly, Annual, or None.

1. EM Asset Setup – Set up equipment assets and calculate their depreciation schedules either using a straight line or declining balance method. Note that you can have multiple assets under one equipment number. This allows you, for example, to set up all your office furniture as individual assets, but lump them under one equipment code.

1. EM Depreciation Processing – Generate monthly, quarterly, or yearly depreciation cost adjusting entries for all assets at once, or selectively one at a time.

1. EM Batch Process – Post and purge the batch. Note: As depreciation entries are created, they are added to the Cost Detail table (EMCD), along with other cost adjustments created in EM Cost Adjustments. Although there is normally no reason to do so, you can view and edit depreciation entries in EM Cost Adjustments until you post the batch.

Related information

- [About Declining Balance / Diminishing Value Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-declining-balance--diminishing-value-depreciation)

- [About Posting Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-posting-depreciation)

- [Equipment Depreciation Using Third-Party Software](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/equipment-depreciation-using-third-party-software)
