---
title: "SM Rate Override Base Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-base-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-base-form"
---

# SM Rate Override Base Form

Use the SM Rate Override Base form to override the equipment, labor, material, non-material purchases, and standard item rates defined for rate templates assigned to customers, service sites, and/or work order quotes.
 Access this form by clicking the Override Rates button in any of the following forms:

-  SM Customers

- SM Service Sites

- SM Work Order Quotes

## Equipment Rates

Use this section to override the standard equipment markup rate defined for rate templates associated with a customer, service site, and/or work order quote. You can also override rates for individual pieces of equipment by equipment/revenue code using the SM Rate Equipment Overrides form (accessed by clicking Advanced in this section). The system only uses the override rates defined in this form if overrides are not found for the equipment/revenue code. For more information about override rates by equipment/revenue, see [SM Rate Equipment Overrides Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-equipment-overrides-form).

## Labor Rates

Use this section to override the standard labor rates defined for the rate templates associated with a customer, service site, and/or work order quote. You can also override labor rates based on technician, craft/class, call type and/or pay type using SM Advanced Labor Overrides (accessed by clicking Advanced in this section). The system only uses the override rates defined in this form if overrides are not found for technician, craft/class, call type and/or pay type (depending on the data entered for the work completed labor line).

## Material Rates

Use this section to override the standard markup or discount rates defined for rate templates associated with a customer, service site, and/or work order quote. You can also define additional rate overrides

- by setting up rate break points based on material total cost or unit cost in SM Rate Override Material (accessed by clicking Advanced in this section);

- by category and/or material in SM Override Category Material (double-clicking in the Category & Material Overrides grid in SM Rate Override Material);

- by setting up rate break points for categories and materials in SM Override Category Material (on the Rate Break Points tab in SM Override Category Material).

The system only uses the rates defined in this form if none are found at the levels described above.

## Non-Material Rates

Use this section to override the standard markup rate
 for non-material purchases (that is, items other than materials, such as equipment
 rentals, subcontractors, etc.). You can also set up advanced non-material markup
 rates that apply based on rate break points and/or cost types. When you enter a
 non-material work completed purchase line (via SM Purchase Order Entry or PO
 Purchase Orders) or a work completed miscellaneous line (via SM Work Orders), the
 system applies a markup rate using the appropriate break point or cost type
 override. If no cost type or break point overrides exist, the standard markup rate
 is used.
 For more information about override markup rates for non-material purchases, see [SM Advanced Non-Material Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-advanced-non-material-form) or [SM Adv. Non-Material Overrides Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-adv.-non-material-overrides-form).

## Standard Item

The Standard Item Overrides button allows you to access the SM Standard Item Overrides form to defined override billable rates for standard items set up in SM Standard Items. You will only need to set up overrides in SM Standard Item Overrides if billable rates differ by customer, service site, or work order quote.

Note:For customer and service sites only: The equipment, labor, material, non-material, and standard item rates defined for a service site override those defined for a customer. If overrides are not defined at the service site or customer level, the system uses the rates defined for the rate template.

Click the following link for more information about using this form.
[Set Up Rate Overrides by Customer, Service Site, or Quote](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-rate-overrides-by-customer-service-site-or-quote)

Related concepts

- [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides/equipment-rate-hierarchy)

- [Labor Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy)

- [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy)
