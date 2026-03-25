---
title: "Set up Existing Assets for Depreciation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/depreciation/set-up-existing-assets-for-depreciation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/depreciation/set-up-existing-assets-for-depreciation"
---

# Set up Existing Assets for Depreciation

Set up existing assets for depreciation and generate depreciation schedules to identify the depreciation amounts to take each month for the life of the asset.
The following details how to set up existing assets after you have already posted some depreciation (in other words, coming on-line with the software for the first time).

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

1. Select the Schedule tab.

1. In the Amount Taken field, enter the amount taken for each previous month or enter a lump sum amount taken (to include all previous years) in the last month of the year prior to going live.

1. Select Calculate to generate the depreciation schedule for the asset for the current year forward.If you are going live mid-year, you can use any of the following methods:

- Enter the Amount Taken for each month.

- Enter a lump sum Amount Taken (to include all previous years) in the last month of the year prior to going live.

- Calculate each month of the current year using EM Depreciation Processing and then manually adjust the monthly amounts where necessary.
