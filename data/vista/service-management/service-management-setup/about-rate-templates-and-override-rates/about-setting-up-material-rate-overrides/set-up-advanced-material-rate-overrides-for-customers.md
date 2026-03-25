---
title: "Set up Advanced Material Rate Overrides for Customers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-customers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-customers"
---

# Set up Advanced Material Rate Overrides for Customers

You can set up base rate overrides for materials at the customer level using the SM Rate Override Base form (accessed via SM Customers). You can also set up advanced overrides for materials by rate break point or category/material using the SM Rate Override Material (accessed via SM Rate Override Base).
You will only need to set up material rate overrides by customer if they differ from the base and override rates defined for the rate template associated with the customer.The following instructions guide you through setting up overrides to the base rate, as well as overrides by break point and category or material.

1. Open the SM Customers form.

1. In the Customer field, enter the customer for which to set up override material rates.

1. Select the Override Rates button (below Rate Template field).The SM Rate Override Base form displays.

1. In the Material Rates section, use the Type drop-down to select M-Markup or D-Discount as the material rate type.Select the N-No Overrides option if you do not want to override the base rate defined for the customer's rate template. This will disable the remaining fields in the Material Rates section; however, you can still set up advanced material rate overrides.

1. If you selected M-Markup or D-Discount as the rate type, use the Basis drop-down to select whether to use the A-Actual Cost, S-Standard Cost, V-Average Cost, L-Last Cost, or P-Standard Price to derive the Bill Rate for materials on a work order.

1. If you selected M-Markup or D-Discount as the rate type, use the Break Points By drop-down to select Total Cost or Unit Cost . The option selected here determines whether rate break points will be based on the material's total cost or unit cost.

1. If you selected M-Markup or D-Discount as the rate type, use the Percent field to enter the override markup or discount rate.

1. Save the record.

1. Set up overrides by rate break point:

1. Select the Rate Break Points tab.

1. In the Break Point Value field, enter the value at which to begin discounting or marking up materials. Depending on the Break Points By option you selected for the customer (in SM Rate Override Base), this amount will represent either Total Cost or Unit Cost. For example, if you selected the Total Cost option and you provide a larger discount when a material's total cost exceeds $500, you would enter 500.00 in this field.Note: If you selected the N-No Overrides rate type option, the system uses the Break Point By value selected for the customer's rate template to determine whether this amount represents Total Cost or Unit Cost.

1. In the Percent field, enter the rate that will be applied when the material's total or unit cost equals or exceeds the specified break point value. The rate type specified in SM Rate Override Base determines whether this rate is a Markup or Discount rate. However, if you selected the N-No Overrides rate type, the system will use the rate type selected for the customer's rate template to determine whether the rate is a markup or discount rate.

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

1. Save the record.

1. If you want to set up break point overrides for the category or material, double-click the Category & Material Overrides grid to open SM Override Category Material.

1. Select the Rate Break Points tab.

1. In the Break Point Value field, enter the value at which to begin discounting or marking up the category or material (e.g. 500.00). Depending on the Break Points By option you selected for the category or material, this amount will represent either Total Cost or Unit Cost.

1. In the Percent field, enter the rate that will be applied when the material's total or unit cost equals or exceeds the specified break point value.

1. Save the record.

1. Add additional break point levels as needed.

Related concepts

- [About Setting up Material Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides)

Related tasks

- [Set up Advanced Material Rate Overrides for Rate Templates](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-rate-templates)

- [Set up Advanced Material Rate Overrides for Effective Date Templates](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-effective-date-templates)

- [Set up Advanced Material Rate Overrides for Service Sites](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-service-sites)

- [Set up Advanced Material Rate Overrides for Work Order Quotes](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/set-up-advanced-material-rate-overrides-for-work-order-quotes)

Related information

- [SM Rate Override Base Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-base-form)

- [SM Rate Override Material Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-material-form)

- [SM Rate Templates Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form)
