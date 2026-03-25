---
title: "Set up Advanced Material Rate Overrides for Effective Date Templates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-effective-date-templates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-effective-date-templates"
---

# Set up Advanced Material Rate Overrides for Effective Date Templates

You can set up advanced overrides to the standard markup/discount rates defined for materials on an Effect Date template. You will only need to set up overrides here if you have different discount/markup rates based on the total cost or unit cost of a material or if rates differ based on the material category or material.
 You must have already set up Effect Date templates. If you have not, you must [set them up](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/add-a-new-effective-date-template/update-rates-for-effective-date-templates) before proceeding here.
The following details setting up material rate overrides for an Effect Date template by rate break point and by category/material.

1. Open the SM Rate Templates form.

1. In the Template field, enter the rate template for which to update effective date templates.

1. Select the Effective Dates tab.

1. In the grid, double-click on the desired Effective Date. The SM Rate Template Effect Dates form displays.

1. Select the Advanced button in the Material Rates section. The SM Rate Override Material form displays.

1. To set up up overrides by break point:

1. Select the Rate Break Points tab.

1. In the Break Point Value field, enter the value at which to begin discounting or marking up materials. Depending on the Break Points By option you selected for the Effective Date template, this amount will represent either Total Cost or Unit Cost. For example, if you selected the Total Cost option and you provide a larger discount when a material's total cost exceeds $500, you would enter 500.00 in this field.

1.  In the Percent field, enter the rate that will be applied when the material's total or unit cost equals or exceeds the specified break point value. The rate type specified for the template determines whether this rate is a Markup or Discount rate.

1. Save the record.

1. Add additional break point levels as needed.

1. To set up overrides by Category or Material:

1. Select the Category & Material Overrides tab.

1. In the Seq field, enter N, New, or +. The system will automatically assign the next available sequence number.

1. If the rate override applies to a material category, use the Category field to enter the category to which the rate applies and leave the Material field blank.If the rate override applies to a specific material, use the Material field to enter the material to which the rate applies and leave the Category field blank.

1. From the Type drop-down, select M-Markup or D-Discount to identify the type of rate override for this sequence.

1.  From the Basis drop-down, select whether to use the A-Actual Cost, S-Standard Cost, V-Average Cost, L-Last Cost, or P-Standard Price to derive the Bill Rate for materials on a work order.

1. From the Break Points By drop-down, select Total Cost or Unit Cost. The option selected here determines whether rate break points will be based on the material's total cost or unit cost.

1. In the Percent field, enter the override markup or discount rate

1. If you want to set up break point overrides for the category or material, double-Select the Category & Material Overrides grid to open SM Override Category Material.

1. Select the Rate Break Points tab.

1. In the Break Point Value field, enter the value at which to begin discounting or marking up the category or material (e.g. 500.00). Depending on the Break Points By option you selected for the category or material, this amount will represent either Total Cost or Unit Cost.

1. In the Percent field, enter the rate that will be applied when the material's total or unit cost equals or exceeds the specified break point value.

1. Save the record.

1. Add additional break point levels as needed.

Related concepts

- [About Setting up Material Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides)

Related tasks

- [Set up Advanced Material Rate Overrides for Rate Templates](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-rate-templates)

- [Set up Advanced Material Rate Overrides for Customers](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-customers)

- [Set up Advanced Material Rate Overrides for Service Sites](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-service-sites)

- [Set up Advanced Material Rate Overrides for Work Order Quotes](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-work-order-quotes)

Related information

- [SM Add Effective Date Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-add-effective-date-form)

- [SM Rate Template Effect Dates Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-template-effect-dates-form)

- [SM Rate Templates Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form)
