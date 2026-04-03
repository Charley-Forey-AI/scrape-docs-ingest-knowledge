---
title: "Depreciation Calculation Method | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/reports-overview/depreciation-method-evaluation-report/depreciation-calculation-method"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/reports-overview/depreciation-method-evaluation-report/depreciation-calculation-method"
---

# Depreciation Calculation Method

Learn about the different methods to calculate fixed assets
 depreciation in Spectrum.
These depreciation methods are used on the [Depreciation Method Evaluation Report](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/reports-overview/depreciation-method-evaluation-report).

## Straight Line

The straight line calculation method has the asset's value depreciate evenly over the course of its lifespan, regardless of when the asset is placed in service. The depreciation value will be calculated using the following formula:
Asset value - Salvage value / Life in Months = Depreciation value
Example:
20,000 (Asset value) - 1,000 (Salvage value) = 19,000
19,000 / 60 (Life in Months) = 316.67 (Depreciation value)

## Declining Balance

The declining balance calculation method utilizes a depreciation method that is a multiple of the straight line method. The depreciation value will decrease in subsequent months as the remaining value of the asset decreases. Therefore, if an asset is given a five-year lifespan the depreciation formula is as follows:
Asset value / Life in months x 2 = Depreciation value
Note: The declining balance does not use Salvage value to
 calculate depreciation total. However, the asset will stop depreciating once the Salvage
 value has been reached.
Example:
1st Month: 20,000 (Asset value) / 60 (Life in months) x 2 = 666.66 (Depreciation value)
2nd Month: 19,333,34 (Asset value - 1st month's depreciation value) / 60 (Life in months) x 2 = 644.44 (Depreciation value)

## Sum of the Years Digits

The sum of the years digits calculation method results in a decreasing depreciation charge based on a decreasing fraction of depreciable cost (original cost less salvage value). The depreciation value will be calculated using the following formula:
1st year: Asset value - Salvage value x 5 / 15 / 12 months = Depreciation value
2nd year: Asset value - Salvage value x 4 / 15 / 12 months = Depreciation value
If the asset is placed into service mid-year, the monthly depreciation amount for the first period will be 200% of the Straight line depreciation calculation. This amount will be deducted from the end of the asset's lifespan.
Example:
An asset is put into service 7/1/07, therefore the depreciation value for the first six months is 633.33 (Straight line depreciation value = 316.67 x 2)
1st full-year: 20,000 - 1,000 x 5 / 15 = 6333.33 6333.33 / 12 = 527.78 (Depreciation value)
2nd year: 20,000 - 1,000 x 4 / 15 = 5066.66 5066.66 / 12 = 422.22 (Depreciation value)

## MACRS

The MACRS ( Accelerated Cost Recovery System) calculation method will have the asset depreciate based on the yearly percentages defined in the [MACRS Table Maintenance](/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/maintenance-overview/macrs-table-maintenance) screen.
If the asset is placed into service mid-year, the monthly depreciation amount for the first period will still add up to the amount defined in the MACRS Table Maintenance screen.
Note: MACRS does not use a Salvage value to calculate depreciation
 total.
