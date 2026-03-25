---
title: "About Posting Depreciation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-posting-depreciation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-posting-depreciation"
---

# About Posting Depreciation

Once you have defined an asset's depreciation parameters and calculated a schedule (in EM Asset Setup), you can then use the EM Depreciation Processing form to calculate the actual depreciation amounts.
The system uses depreciation scheduling information set up in EM Asset Setup to determine how much depreciation to post. Calculations are based on the scheduled Amount to Take for that year through the current month and the Amount Taken to-date for that year through the current month.
The amount taken-to-date is subtracted from the scheduled Amount to Take, and the result is entered in the Amount Taken for the current month.
 For example, assume you are posting depreciation on a monthly basis:
EM Asset Setup: Total Amt to Depreciate: $1200.00
EM Depreciation Processing: Posting Date: 03/23
Month
Amount to Take
Amount Taken
Balance

01/23
100.00
100.00
0.00

02/23
100.00
100.00
0.00

03/23
100.00
0.00
100.00

The total Amount to Take through the current month (03/23) is $300.00. The total Amount Taken for the year through 03/23 is $200.00. The remaining balance of $100.00 is posted to 03/23 in the Amount Taken column.
The system stores depreciation entries created in EM Depreciation Processing in the Cost Detail file (EMCD). Until you post the batch in EM Batch Process, you can edit or delete the entries in EM Cost Adjustments. However, nothing you do in EM Cost Adjustments affects the asset's Amount Taken value.
If you elected to update GL when posting depreciation (the Summary or Detail option selected on the Adjustments tab in EM Company Parameters), calculated depreciation updates an accumulated depreciation account and a depreciation expense account. Normally, both of these accounts come from the EM Department file. In the case of expense, it uses the account assigned to the cost code/cost type for depreciation specified in EM Company Parameters. However, you may override these accounts for each asset in EM Asset Setup.
For additional information about declining balance/diminishing value depreciation calculations, see [About Declining Balance / Diminishing Value
 Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-declining-balance--diminishing-value-depreciation).

## Recalculating a Month

Rerunning the depreciation process for the same month does not double up depreciation, but it will correct for any schedule changes made since the first run.
 For example, say that after posting depreciation for month 06/23, you find you must change the asset's life (# of month's to depreciate). This causes the asset's Amount to Take value to change when you recalculate its schedule.
In EM Asset Setup:

Before
After Recalc

To Take
$1,200.00
$2,000.00

Taken To Date
600.00
600.00

Example:
If month 06/23 = 6/12 (six twelfths) of year, the system calculates what 6/12 of the annual total 'to take' amount (2,000) should be, which in this case, is $1000. It then looks at how much of that has already been taken to-date ($600) and creates another entry to post the difference ($400) to bring the Amount Taken to-date to $1000.
As you can see from the above example, if you rerun a month in EM Depreciation Processing and the asset's scheduled amount has increased, then EM Depreciation Processing will post the amount needed to catch up. If instead, the asset's scheduled amount has decreased, it will post a negative amount to catch up. If the asset's scheduled amount has not changed, then rerunning EM Depreciation Processing for the same month will result in no additional depreciation posting.

Related information

- [EM Depreciation Processing Form](/en/vista/vista/job-resources/equipment-management/depreciation/em-depreciation-processing-form)
