---
title: "SM Rate Equipment Overrides Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-equipment-overrides-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-equipment-overrides-form"
---

# SM Rate Equipment Overrides Form

Use the SM Rate Equipment Overrides form to set up override rates for equipment used on Service Management work orders.
Access this form by
 clicking Advanced in the Equipment Rates
 section of SM Rate Templates. You can also access this form via the SM Rate Template
 Effect Dates form (accessed by double-clicking in the
 Effective Date grid in SM Rate Templates), and the SM
 Rate Override Base form (accessed by clicking Override
 Rates in the SM Customers or SM Service
 Sites forms).
You can set up override rates for equipment at the rate template, customer, and/or service site levels based on equipment and revenue code.
Note: You will only need to use
 this form if the equipment markup rate differs by
 equipment and revenue code. If you will be using the
 same markup rate for all work orders referencing
 this template, use the Markup field in SM Rate Templates
 (Equipment Rates section) to specify that
 rate.
For each override
 rate you set up, you must specify the EM Co,
 equipment, and revenue code to which the rate applies, as well as the rate type (Markup or Flat
 Rate) and the markup amount/flat rate amount. When
 capturing work completed (in SM Work Orders), the
 system compares the equipment and revenue code
 on the work completed line to the overrides
 defined here to determine which equipment rate to
 use. If a match is found, the system uses the
 override rate to determine the line's Billable Rate.
 If no match is found, the system uses the equipment
 markup rate defined in SM Rate Override Base (for
 service sites or customers) or in SM Rate Templates
 (at rate template level) to determine the Billable
 Rate.
For information
 about the hierarchy used to determine which
 equipment rate to use, see [Equipment Rate
 Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides/equipment-rate-hierarchy).

## Markup Rate vs. Flat Rate

If
 the override is defined as a markup rate, the
 billable rate for the work completed line will be
 a calculation of the Cost Rate + (Cost Rate x
 Markup Rate). For example, if the Cost Rate is
 250.00 and the Markup rate is 5.00%, the resulting
 Billable Rate will be 262.50.
250.00 + (250.00 x .05 =12.50) = 262.50
If
 the override is defined as a Flat Rate, the
 billable rate will be a calculation of the Flat
 Rate x Time Units. For example, if the work
 completed line's Time Units = 8.00 and the Flat
 Rate amount = 150.00000, the resulting Billable
 Rate will be 1200.00.
8.00
 x 150.00000 = 1200.00

Related information

- [Set up Equipment Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides)

- [SM Rate Templates Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form)

- [SM Rate Override Base Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-base-form)

- [SM Customers Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form)

- [SM Service Sites Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form)
