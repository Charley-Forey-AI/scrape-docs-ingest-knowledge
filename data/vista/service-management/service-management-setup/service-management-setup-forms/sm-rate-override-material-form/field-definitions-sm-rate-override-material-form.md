---
title: "Field Definitions: SM Rate Override Material Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-material-form/field-definitions-sm-rate-override-material-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-material-form/field-definitions-sm-rate-override-material-form"
---

# Field Definitions: SM Rate Override Material Form

The following is a list of field descriptions for the SM Rate
 Override Material form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Break Point Value

Enter the amount to use as a break point when applying discounts or markups to stocked or purchased materials specified on a work completed line (in SM Work Orders). The system will apply a markup or discount rate (depending on the rate type selected for the rate template) using the percentage specified to the right.
 The option you selected in the Break Point By
 field for the category or material determines what the break point value represents. If you
 selected Total Cost, the system will apply the specified percentage when the total cost of
 the material reaches this amount. If you selected Unit Cost, the system will apply the
 specified percentage when the unit cost of the material reaches this amount. For more
 information about rate break points, see [Rate Break
 Points](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/about-material-rate-break-points).

## Percent

Enter the percent to use for applying discounts or markups (depending on material rate type) to stocked or purchased materials on a work order (e.g. enter 5% as 5.00000).
The system will apply this percentage when the total cost or unit cost of the material
 (depending on the Break Points By option selected for the rate
 template) reaches the amount specified in the Break Point Value
 field for this entry. (This percent will also apply to miscellaneous work completed lines
 that specify a material cost type.)
For information about how the system uses rate break points when calculating the discount or markup rate for materials on a work completed line, see [Rate Break Points](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/about-material-rate-break-points).

- You can override the rates defined here by category or material in [SM Override Category Material](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-material-form) (accessed by double-clicking in the Category & Material Overrides). The system will only use the rate break points defined here if no advanced rates are found for the material/category.

- Because material rates/overrides can be defined at the rate template, effective date, customer, service site, and work order quote levels, the system will use a specific hierarchy to determine which material rates to use. For more information, see [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy).
