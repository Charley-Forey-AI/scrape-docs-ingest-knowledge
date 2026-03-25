---
title: "Set up a Rate Template | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-a-rate-template"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-a-rate-template"
---

# Set up a Rate Template

Rate templates are used to define the equipment, labor, material, and non-material purchase rates used in billable rate calculations (charge to customer) for work completed on a work order.
The following instructions will guide you through the process of setting up a rate template.

1. From the Vista main menu, select Service Management > Programs.

1. Double-click the SM Rate Templates icon to open the SM Rate Templates form.

1. In the Template field, enter a code to identify this rate template.

1. In the Description field, enter a description of the rate template.

1.  In the Markup Percent field, enter the markup rate for equipment usage.

1. In the Rate field, enter the default rate for labor.

1. From the Type drop-down, select Markup or Discount to identify what the material rate represents.

1. From the Basis drop-down, select whether to use the A-Actual Cost, S-Standard Cost, V-Average Cost, L-Last Cost, or P-Standard Price to derive the Billable Rate for materials on a work order.

1. From the Break Points By drop-down, select Total Cost or Unit Cost. The option selected here determines whether rate break points will be based on the material's total cost or unit cost.

1. In the Percent field, enter the percentage to use when calculating the markup or discount for materials on a work order.

1. In the Markup
 Percent field (Non-Material Purchases), enter the markup percent
 for work completed purchase lines referencing non-material purchase order items.
 Enter 0.00 if no markup will be applied to non-material purchases.Note: Use the SM Adv. Non-Material Overrides form to enter cost types for
 non-material purchases based on cost type instead of rate template.

1. Select the Active checkbox to activate the rate template.Note: Inactive rate templates will not display in F4 lookups, nor can they be assigned to customers, service sites, or work orders.

 Once you have set up a rate template, use the Advanced
 buttons to optionally set up override rates for equipment, labor, materials, and
 standard items. You can also set up effective date templates that allow you to define
 equipment, labor, material, and standard items rates in advance that will take effect by
 a specific date.Click the following links for more information.
[Set up Equipment Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides)
[Set up Labor Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides)
[About Setting up Material Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides)
[Set up Override Rates for Non-Material Purchases](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases)
[About Setting up Standard Item Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-standard-item-overrides)
[SM Add Effective Date Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-add-effective-date-form)

Related information

- [SM Rate Templates Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form)

- [About the EM Revenue Rates by Category Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-category-form)

- [About the EM Revenue Rates by Equipment Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-equipment-form)
