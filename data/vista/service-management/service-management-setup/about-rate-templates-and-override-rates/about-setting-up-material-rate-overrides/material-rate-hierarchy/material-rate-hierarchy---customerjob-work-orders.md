---
title: "Material Rate Hierarchy - Customer/Job Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy/material-rate-hierarchy---customerjob-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy/material-rate-hierarchy---customerjob-work-orders"
---

# Material Rate Hierarchy - Customer/Job Work Orders

When capturing materials on customer and job work orders, the
 system uses a specific hierarchy to determine the markup and discount rates to use for
 calculating billable rates.
The following explains how the system derives billable rates for work
 completed inventory and work completed purchase lines on customer work orders based on
 your material rates setup.

1. Service Site Overrides - The system first checks for a
 material override in SM Override Category Material for the service site
 specified on the work order. If a record is found for the specified material,
 the system uses the material's rate Basis and Break Points
 By option to determine the cost used in billable rate
 calculations.

- Actual Cost - For Inventory lines, this will be
 the Actual Cost from the work completed line (if Break Points By is
 Total Cost) or the Cost Rate (if Break Points By is Unit Cost). For
 Purchase lines, this will be the Proj Cost from the work completed line
 (if Break Points By is Total Cost) or the Cost Rate (if Break Points By
 is Unit Cost).

- Standard Cost - For Inventory and Purchase
 lines where Break Points By is Total Cost, this will be the Std Unit
 Cost from IN Location Materials (Inventory lines) or HQ Materials
 (Purchase lines) times the material quantity. If the line's UM does not
 match the material's standard UM, the system will use the unit cost
 defined for the UM in the related Additional Units of Measure table. For
 Inventory and Purchase lines where Break Points By is Unit Cost, this
 will be the Std Unit Cost from IN Location Materials or HQ Materials,
 respectively.

- Average Cost - For Inventory and Purchase lines
 where Break Points By is Total Cost, this will be the Avg Unit Cost from
 IN Location Materials (Inventory lines) or HQ Materials (Purchase lines)
 times the material quantity. If the line's UM does not match the
 material's standard UM, the system will use the unit cost defined for
 the UM in the related Additional Units of Measure table. For Inventory
 and Purchase lines where Break Points By is Unit Cost, this will be the
 Avg Unit Cost IN Location Materials or HQ Materials, respectively.

- Last Cost - For Inventory and Purchase lines
 where Break Points By is Total Cost, this will be the Last Unit Cost
 from IN Location Materials (Inventory lines) or HQ Materials (Purchase
 lines) times the material quantity. If the line's UM does not match the
 material's standard UM, the system will use the unit cost defined for
 the UM in the related Additional Units of Measure table. For Inventory
 and Purchase lines where Break Points By is Unit Cost, this will be the
 Last Unit Cost from IN Location Materials or HQ Materials,
 respectively.

- Standard Price - For Inventory and Purchase
 lines where Break Points By is Total Cost, this will be the Std Unit
 Price from IN Location Materials (Inventory lines) or HQ Materials
 (Purchase lines) times the material quantity. If the line's UM does not
 match the material's standard UM, the system will use the unit cost
 defined for the UM in the related Additional Units of Measure table. For
 Inventory and Purchase lines where Break Points By is Unit Cost, this
 will be the Std Unit Price from IN Location Materials or HQ Materials,
 respectively.

The system then compares the calculated total cost (if using Total Cost
 Break Point By option)
 or the specified unit cost/unit price (if using Unit Cost Break Point By option) to the rate
 break points defined for the material (in SM Override Category Material). If
 the total cost or unit cost/unit price falls within any of the rate break
 point ranges, the system applies the specified markup or discount rate to
 determine the Bill Subtotal. It will then divide the Bill Subtotal by the
 line's quantity to determine the Bill Rate.

1. If the total cost or unit cost/unit price does not fall within any of the rate
 break point ranges or no rate break points have been defined for the material,
 the system will then apply the override rate specified for the material in SM
 Override Category Material ( Percent field).

1. If an override record is not found for the material, the system will then look
 for an override for the material's category. If a category override record
 exists, the system follows the same process indicated above to determine the
 Bill Subtotal and Bill Rate.

1. If no category override record is found, the system will then use the rate Basis
 defined in SM Rate Override Base (and displayed above the Rate Break Points grid
 in SM Rate Override Material) to determine which cost to use in determining the
 Bill Rate (as described in Step 1 above).The system then compares the
 calculated total cost or unit cost/unit price to the rate break points
 defined in SM Rate Override Material. If the total cost or unit cost/unit
 price falls within any of the rate break point ranges, the system applies
 the specified markup or discount rate to determine the Total Billable. It
 will then divide the Total Billable by the line's quantity to determine the
 Bill Rate.

1. If the total cost does not fall within any of the rate break point ranges or no
 rate break points have been defined, the system will then apply the override
 rate specified in SM Override Base ( Percent field).

1. If no rate is defined in SM Rate Override Base (i.e. the rate type is N-No
 Override) and this is a customer work order, the system will then look for
 overrides at the Customer level (see Step 7). If this is a Job work order, the
 system will then look for overrides at the scope rate template level (see Step
 8).

1. Customer Overrides (Customer WOs only) - The system looks
 for override rates using the same hierarchy defined above (Steps 1-5)

1. Effective Date Overrides - If override rates are not
 found at the Service Site level or Customer level (customer
 work orders only), the system will then look for Effective Date overrides using the
 rate template specified for the work order scope. If Effective Date overrides
 exist, the system will compare the Date specified on the work completed line to
 the Effective Dates specified for the rate template. If the work completed date
 falls within any of the effective date ranges, the system will then use the
 appropriate effective date template to determine material rates, using the same
 hierarchy indicated in Steps 1-5 above. No further rate search is
 performed.

1. Rate Template - If the work completed date does not fall
 within any of the effective date ranges or no effective dates are defined, the
 system will then use the rate template to determine the material rate (using the
 same process indicated above).Note: If at any level, the markup or
 discount rate is set to 0.00, the system assumes you do not want to
 discount/markup the material; therefore, no discount or markup rate will be
 applied and no further rate search will occur.If you
 define rate break points at the service site or customer level (in SM
 Rate Override Base), it is recommended that you do not set the override
 type to N-No Override. The system will ignore rate break points when
 this condition occurs and will go to the next level to locate a
 discount/markup rate.

Related concepts

- [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy)

- [About Setting up Material Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides)
