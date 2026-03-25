---
title: "About Diminishing Value (Australia) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-declining-balance--diminishing-value-depreciation/about-diminishing-value-australia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-declining-balance--diminishing-value-depreciation/about-diminishing-value-australia"
---

# About Diminishing Value (Australia)

The Diminishing Value method of depreciation allows you to depreciate larger amounts in the first year of an asset's life, and then gradually decrease depreciation amounts in subsequent years until the total amount to depreciate has been reached.
With this method, it is assumed that the value of a depreciating asset decreases more in the early years of its effective life. The value of the equipment is depreciated by a defined percentage of the base value on a monthly basis.

## Calculations for Diminishing Value Depreciation

The formula for calculating diminishing value:
base value × (days
 held ÷ 365) × (200% ÷ asset's
 effective life)

- The base value represents the
 Purchase Price of the
 asset.

- The days
 held represent the Depreciation
 Start Date until the end of the fiscal
 year (July for AU). This value is recalculated for
 every fiscal year being scheduled. For all months in
 a fiscal year, the Amount to
 Take is approximately equal.

- The asset's
 effective life represents the asset's
 life in years (in the formula, this number comes
 from #
 of Months Held ÷ 12).

- The 200% is the Diminishing
 Value Factor (factor of 2.0), which is
 used for assets from May 2006 and forward.

The base value reduces each year by the decline in the
 value of the asset. So if the purchase price is $50,000, the days
 held is 365, and the effective life is 5 years, the base value for
 the first year is $50,000. Based on the formula above, the total
 amount to take for the first year is $20,000:
50,000 × (365 ÷ 365) × (200% ÷ 5) = 20,000
The system then subtracts the $20,000 from the $50,000
 to get the base value for the next year ($50,000 – $20,000 =
 $30,000). This process continues until the value reaches zero.
However, when no residual value is assigned and the
 monthly depreciation falls below $1.00 per month, the system stops
 calculating depreciation. This limits the total number of months
 calculated.
Important: If the number of years
 to depreciate is less than two (24 months held or
 fewer), this formula for diminishing value will not produce
 an accurate schedule. This is because when the number of
 years is less than the diminishing value factor (2.0), the
 result of 200% ÷ asset's effective
 life is greater than one, producing a
 value that is greater than the starting base value.
 However, this is an unlikely scenario considering
 most assets have an effective life of more than two
 years.

## Example of the Diminishing Value Depreciation Schedule

Fiscal Year-End: 06/15
Purchase Price: 50,000
Residual Value: 0.00
Total Amt to Depreciate: 50,000
First Month to Depreciate: 7/14
# of Months to Depreciate: 60
Depreciation Factor: 2.0
You can see the depreciation schedule for a particular
 asset in the Schedule tab of EM Asset Setup. The form header
 displays the total depreciation amount taken and the remaining
 amount to take.
For more information about what to enter in this form, see [Field Definitions: EM Asset Setup Form](/en/vista/vista/job-resources/equipment-management/depreciation/em-asset-setup-form/field-definitions-em-asset-setup-form).

Related information

- [About Posting Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-posting-depreciation)

- [About Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation)
