---
title: "SM Override Category Material Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-override-category-material-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-override-category-material-form"
---

# SM Override Category Material Form

Use the SM Override Category Material form to set up override markup/discount rates for materials used on work orders by category or material.
Access this form by double-clicking in the Category & Material Overrides grid in SM Rate Override Material.
For each override sequence you set up, you must specify whether the override is for a category or material; you cannot specify both on a sequence. However, you can set up one sequence for the material and one for the material category. The system always uses the material level override first, but if an override is not found for the material, it will then apply the override defined for the material category. This allows you to provide a discount/markup rate for all materials in a category, but to also define special markup/discounts rates for individual materials.
For each sequence, use the Override Rate section to specify the rate type (markup or discount), rate basis (actual, standard, average, or last cost, or standard price), break point basis (total cost or unit cost), and the standard percentage rate. When stocked or purchased materials are specified on a work completed line, the system will use this information to determine the billable rate (charge to the customer) for the parts used.Note: The system only uses the rate basis in determining the billable rate for work completed inventory lines. If the material is specified on a work completed purchase line (for a PO), the system will always apply the markup or discount rate to the material's actual unit cost, regardless of the basis specified here.

If you have different levels of discount or markup rates for the material or category, use the Rate Break Points tab to define the markup or discount levels. For more information, see [About Material Rate Break Points](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/about-material-rate-break-points).Note: Rate break points set up by material or category at the service site or customer levels, will override those set up at the rate template level.

Click the links below for more information about setting up material rate overrides.
[Set up Advanced Material Rate Overrides for Rate Templates](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-rate-templates)
[Set up Advanced Material Rate Overrides for Effective Date Templates](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-effective-date-templates)
[Set up Advanced Material Rate Overrides for Customers](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-customers)
[Set up Advanced Material Rate Overrides for Service Sites](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-service-sites)
[Set up Advanced Material Rate Overrides for Work Order Quotes](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-work-order-quotes)
[About Setting up Material Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides)
