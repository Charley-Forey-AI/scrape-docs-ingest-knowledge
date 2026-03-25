---
title: "About the Depreciation Schedule | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-the-depreciation-schedule"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-the-depreciation-schedule"
---

# About the Depreciation Schedule

The depreciation schedule for an asset is displayed on the Schedule tab of the EM Asset Setup form.
It is generally used after the schedule has been calculated to override calculated amounts or when first coming on-line with existing assets where you need to enter to-date depreciation amounts. Any amount you enter in this form’s Amount Taken will NOT be posted to GL. If you need prior depreciation amounts posted to GL, you must maintain the change here and post an adjusting entry in EM Cost Adjustments.

## Calculate the Depreciation Schedule

The EM Asset Setup form automatically calculates a depreciation schedule for an asset after you have set up
 the asset's parameters (Info tab) and
 selected the Calculate button. This calculation determines the amount to take on
 a month-by-month basis for the asset.
You must calculate a schedule before you
 can use the EM Depreciation Processing form to post depreciation costs to GL. When
 processing depreciation, the Amount Taken column is updated
 for the specified month(s), along with the total amount taken-to-date and the
 remaining amount to take (shown in the Taken and Balance
 fields above the grid).

## Recalculating the Schedule

If you make changes to an asset that causes the existing calculated schedule to be outdated (such as changing the depreciation method or disposing of the asset), you must recalculate the schedule.
 To recalculate, make the necessary changes on the Info tab of EM Asset Setup and
 select Calculate. If you are using the Straight Line method or the
 Diminishing Value method (Australia only), the schedule is recalculated based on the
 new information. If you are using the Declining Balance method (US & Canada
 only), the screen displays the following message:
Once you select OK, the
 Recalculation for Year Ending field appears in the upper section of
 form (below the Asset number). Specify the year-end month of the fiscal year with
 which to begin recalculation, and select Calculate again. The schedule
 will be recalculated beginning with the first month of the fiscal year you
 specified, replacing all existing Amount to Take values with recalculated ones.
When you recalculate a schedule,
 recalculate only the remaining months of the asset; do not recalculate any of the
 prior months that have already been fully depreciated. Recalculating prior months
 will cause the Amount to Take values to be recalculated, which may result in changes
 to the original values. Although this will not affect any costs already posted to
 GL, it would mean the Amount to Take and the Amount Taken values displayed for those
 prior months will no longer balance with each other. If this happens, you will need
 to correct the Amount Taken values manually to bring them back into balance.
Note: Recalculating a schedule after disposing of an
 asset does not recalculate the Amount to Take values. The system will only truncate
 the schedule, removing all months remaining after the specified disposal
 month.

Related information

- [About Posting Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-posting-depreciation)

- [EM Asset Setup Form](/en/vista/vista/job-resources/equipment-management/depreciation/em-asset-setup-form)
