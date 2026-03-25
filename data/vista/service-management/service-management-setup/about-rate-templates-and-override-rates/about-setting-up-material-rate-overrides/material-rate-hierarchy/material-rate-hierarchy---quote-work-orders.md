---
title: "Material Rate Hierarchy - Quote Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy/material-rate-hierarchy---quote-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy/material-rate-hierarchy---quote-work-orders"
---

# Material Rate Hierarchy - Quote Work Orders

When capturing materials on quote-related work orders, the
 system uses a specific hierarchy to determine the markup and discount rates to use for
 calculating billable rates.
For work orders generated from a work order quote, the system uses a similar
 hierarchy to determine material rates. However, for these work orders, the system will
 use only the rate overrides/rate template defined for the quote sequence. Overrides
 defined at the customer or service site level are not used.
Note: The hierarchy described below is used only when the work order scope referenced
 on the work completed equipment line has a Price Method of Time and Material. Billable rates are not
 calculated for work completed lines associated with Flat Price or Non-Billable work
 order scopes.

1. Quote Override
 Rates - The system first checks for a material override in SM
 Override Category Material at the quote sequence Override Rates level. If a
 record is found for the specified material, the system uses the material's rate
 Basis and Break Points By option to determine
 the cost used in billable rate calculations.

- Actual Cost - For Inventory
 lines, this will be the Actual Cost from the work completed line (if
 Break Points By is Total Cost) or the Cost Rate (if Break Points By is
 Unit Cost). For Purchase lines, this will be the Proj Cost from the work
 completed line (if Break Points By is Total Cost) or the Cost Rate (if
 Break Points By is Unit Cost).

- Standard Cost - For Inventory
 and Purchase lines where Break Points By is Total Cost, this will be the
 Std Unit Cost from IN Location Materials (Inventory lines) or HQ
 Materials (Purchase lines) times the material quantity. If the line's UM
 does not match the material's standard UM, the system will use the unit
 cost defined for the UM in the related Additional Units of Measure
 table. For Inventory and Purchase lines where Break Points By is Unit
 Cost, this will be the Std Unit Cost from IN Location Materials or HQ
 Materials, respectively..

- Average Cost - For Inventory
 and Purchase lines where Break Points By is Total Cost, this will be the
 Avg Unit Cost from IN Location Materials (Inventory lines) or HQ
 Materials (Purchase lines) times the material quantity. If the line's UM
 does not match the material's standard UM, the system will use the unit
 cost defined for the UM in the related Additional Units of Measure
 table. For Inventory and Purchase lines where Break Points By is Unit
 Cost, this will be the Avg Unit Cost from IN Location Materials or HQ
 Materials, respectively.

- Last Cost - For Inventory and
 Purchase lines where Break Points By is Total Cost, this will be the
 Last Unit Cost from IN Location Materials (Inventory lines) or HQ
 Materials (Purchase lines) times the material quantity. If the line's UM
 does not match the material's standard UM, the system will use the unit
 cost defined for the UM in the related Additional Units of Measure
 table. For Inventory and Purchase lines where Break Points By is Unit
 Cost, this will be the Last Unit Cost from IN Location Materials or HQ
 Materials, respectively.

- Standard Price - For
 Inventory and Purchase lines where Break Points By is Total Cost, this
 will be the Std Unit Price from IN Location Materials (Inventory lines)
 or HQ Materials (Purchase lines) times the material quantity. If the
 line's UM does not match the material's standard UM, the system will use
 the unit cost defined for the UM in the related Additional Units of
 Measure table. For Inventory and Purchase lines where Break Points By is
 Unit Cost, this will be the Std Unit Price from IN Location Materials or
 HQ Materials, respectively.

The system then compares the calculated total cost
 (if using Total Cost Break Point
 By option) or the specified unit cost/unit price (if using
 Unit Cost Break Point By
 option) to the rate break points defined for the material (in SM Override
 Category Material). If the total cost or unit cost/unit price falls within
 any of the rate break point ranges, the system applies the specified markup
 or discount rate to determine the Total Billable. It will then divide the
 Total Billable by the line's quantity to determine the Billable
 Rate.

1. If the total cost does not fall within any of the rate break
 point ranges or no rate break points have been defined for the material, the
 system will then apply the override rate specified for the material in SM
 Override Category Material ( Percent field).

1. If an override record is not found for the material, the
 system will then look for an override for the material's category. If a category
 override record exists, the system follows the same process indicated above to
 determine the total billable and billable rate.

1. If no category override record is found, the system will then use the rate Basis
 defined in SM Rate Override Base (and displayed above the Rate Break Points grid
 in SM Rate Override Material) to determine which cost to use in determining the
 billable rate (as described in Step 1 above).The system then compares the
 calculated total cost or unit cost/unit price to the rate break points
 defined in SM Rate Override Material. If the total cost or unit cost/unit
 price falls within any of the rate break point ranges, the system applies
 the specified markup or discount rate to determine the Total Billable. It
 will then divide the Total Billable by the line's quantity to determine the
 Billable Rate.

1. If the total cost does not fall within any of the rate break
 point ranges or no rate break points have been defined, the system will then
 apply the override rate specified in SM Override Base (Percent field).

1. Effective Date Overrides -  If
 no rate is defined in SM Rate Override Base (i.e. the rate type is
 N-No Override) at the quote sequence Override Rates
 level, the system will then look for Effective Date overrides using the rate
 template specified for the quote sequence. If Effective Date overrides exist,
 the system will compare the Date specified on the work completed line to the
 Effective Dates specified for the rate template. If the work completed date
 falls within any of the effective date ranges, the system will then use the
 appropriate effective date template to determine material rates, using the same
 hierarchy indicated in Steps 1-5 above. No further rate search is performed.

1. Rate
 Template - If the work completed date does not fall within any
 of the effective date ranges or no effective dates are defined, the system will
 then use the quote's rate template to determine the material rate (using the
 same process indicated above).Important: If you enter a 0.00 value
 in the markup or discount rate field, the system assumes you do not want to
 discount/markup the material; therefore, no discount or markup rate will be
 applied and no further rate search will occur.

Related concepts

- [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy)

- [About Setting up Material Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides)
