---
title: "Set up New Assets for Depreciation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/depreciation/set-up-new-assets-for-depreciation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/depreciation/set-up-new-assets-for-depreciation"
---

# Set up New Assets for Depreciation

Set up assets for depreciation and generate depreciation schedules to identify the depreciation amounts to take each month for the life of the asset.
The following details how to set up new assets when you acquire them.

1. Open the EM Asset Setup form (Equipment Management > Programs > EM Asset Setup

1. In the Equipment field, enter the equipment for which to set up an asset or press F4 to select from a list of valid equipment.

1. In the Asset field, enter a code (alpha or numeric) to represent the asset.

1. In the Description field, enter a description of the asset.

1. In the Purchase Price field, enter the purchase price of the asset.

1. In the Residual Value field, enter the expected value of the asset after it has been fully depreciated.Note: The system calculates the Total Amount to Depreciate based on the purchase price less the residual value.

1. For U.S. and Canadian companies:

1. In the First Month to Depreciate field, enter or select the first date for which to calculate depreciation for the asset.

1. In the # of Months to Depreciate field, enter the total number of months for which to calculate depreciation for the asset.The system uses this value in conjunction with the First Month to Depreciate to generate the depreciation schedule.

1. For Australian companies:

1. In the Depreciation Start Date field, enter or select the first date for which to calculate depreciation for the asset.

1. In the # of Months Held field, enter the total number of months from the Depreciation Start Date that this asset will be held. The system uses this value in conjunction with the Depreciation Start Date to generate the depreciation schedule.

1. In the Method field, select the method of depreciation to use for the asset:

- Straight Line - Depreciate the same amount each month.

- Declining Balance (US/CAN) / Diminishing Value (AUS) - Base the monthly depreciation amount for this asset on an acceleration factor (specified in the Factor field).

1.  If you selected the Declining Balance (US/CAN) or Diminishing Value (AUS) depreciation method, use the Factor field to enter the acceleration factor for calculating depreciation (e.g. 1.00, 1.50, 2.00).

1. If overriding the depreciation accounts for this asset, use the GL Accounts section to indicate the override accumulated depreciation, depreciation expense, and asset GL accounts.

1. Select Calculate to generate the depreciation schedule for the asset.

If you set up an asset months after you acquire it, the next time you process depreciation, the program will bring it up to date. For example, if you set up an asset in June that you acquired in April, and then run EM Depreciation Processing, the system will post 3 months of depreciation to June.If you want the depreciated amounts to go to the correct months and those months are still open, process depreciation for each month. If the acquisition dates back to the prior fiscal year, process depreciation for the last month of that year; the depreciation process only looks at one year at a time.
