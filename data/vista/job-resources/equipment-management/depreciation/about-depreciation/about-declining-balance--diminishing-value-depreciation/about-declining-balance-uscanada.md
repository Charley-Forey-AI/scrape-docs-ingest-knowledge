---
title: "About Declining Balance (US/Canada) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-declining-balance--diminishing-value-depreciation/about-declining-balance-uscanada"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-declining-balance--diminishing-value-depreciation/about-declining-balance-uscanada"
---

# About Declining Balance (US/Canada)

The Declining Balance (US & Canada) method of depreciation allows you to depreciate larger amounts in the first year of an asset's life, and then gradually decrease depreciation amounts in subsequent years until the total amount to depreciate has been reached.
When using this method, the system begins with the Purchase Price of the asset and ends depreciation at the Residual Value (the expected value of the asset when fully depreciated). The acceleration factor specified for the asset (the Factor field in EM Asset Setup) determines the amounts that will be taken during the depreciation process. The system will take larger amounts during the first year, then gradually decrease the amounts until the full depreciation amount is realized.
In some cases, the amount taken in the last month may differ slightly--generally due to the amount left over and/or rounding. Additionally, if the Total Amount to Depreciate is realized before the end of the depreciation schedule is reached, the remaining months will be set to 0.00.
Example of the Declining Balance Depreciation Schedule
Fiscal Year-End: 12/15
Purchase Price: 50,000
Residual Value: 10,000
Total Amt to Depreciate: 40,000
First Month to Depreciate: 4/15
# of Months to Depreciate: 36
Depreciation Factor: 1.5
Note: For United States companies only: The system will automatically switch to the straight-line method when the depreciation amount calculated by the straight line method is greater than the amount calculated by the declining balance method.

You can see the depreciation schedule for a particular asset in the Schedule tab of EM Asset Setup. The form header displays the total depreciation amount taken and the remaining amount to take.
