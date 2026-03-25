---
title: "SM Rate Templates Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form"
---

# SM Rate Templates Form

Use the SM Rate Templates form to set up rate templates that define the equipment, labor, material, and non-material purchase rates used when entering work completed lines for work orders in SM Work Orders.
The system uses the rates defined for a template to derive the Billable Rate (charge to customer) for work completed lines. Once set up here, you assign rate templates to customers (in SM Customers), service sites (SM Service Sites), and work order scopes (SM Work Orders).
Note: Although you are not required to assign rate templates to customers or service sites, you must assign a rate template to work order scopes before you can enter any work completed lines.

## Equipment Rates

You will use this section to enter the standard markup rate, as well as any advanced
 markup rates that apply to individual pieces of equipment. When entering work
 completed equipment lines on a work order (in SM Work Orders), the system will use
 the advanced rate or the standard rate (if applicable) and apply it to the equipment
 usage rate defined for the revenue code (in EM Revenue Rates by Equipment or
 EM Revenue Rates by Category). For more information about override rates, see [SM Rate Equipment Overrides Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-equipment-overrides-form).

## Labor Rates

Use this section to define the labor rates (standard and advanced) used in
 calculating charges to the customer for labor performed on a work order. The
 Rate field is used to enter the standard labor rate
 charge to customers when entering work completed labor lines on a work order. If
 labor rates differ based on technician, craft/class, call type and/or pay type, you
 can set up rate a labor rate table using the SM Advanced Labor Overrides form
 (accessed by clicking the Advanced button). The system will use the rate table to
 determine which rate to use when entering work completed labor lines on a work
 order; however, if the rate table does not contain criteria matching the data
 entered on the labor line, the system will use the standard rate defined for the
 template.

## Material Rates

Use this section to define markup or discount rates for materials (stocked or
 purchased) used in service work. Although costs will be derived from purchase orders
 (for purchased materials) or from unit cost values for a location (for stocked
 materials), the actual charge to customers will be based on the cost of the part and
 the material rates defined here.
You will need to specify whether materials will be marked up or discounted, define
 the markup/discount basis (e.g. actual, standard, average, or last unit cost, or
 standard unit price), indicate the markup/discount percent, and specify whether to
 apply rate break points (entered in SM Rate Override Material) by total cost or unit
 cost.
For more information about material rate overrides, see [About Setting up Material Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides).

## Non-Material Purchases

Use this section to enter the standard markup rate for purchases that are for items
 other than materials (e.g. equipment rentals, subcontractors, etc.), as well as any
 advanced non-material markup rates that apply based on rate break points and/or cost
 types. When you enter a non-material work completed purchase line (via
 SM Purchase Order Entry or PO Purchase Orders) or a work completed
 miscellaneous line (via SM Work Orders), the system applies a markup rate using
 the appropriate break point or cost type override, or the standard rate if no
 overrides exist.
For more information, see [SM Advanced Non-Material Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-advanced-non-material-form). or [SM Adv. Non-Material Overrides Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-adv.-non-material-overrides-form).

## Standard Item Overrides

Standard Item OverridesThe Standard Item Overrides option allows you to override the
 billable rate defined for standard items in SM Standard Items. You will only need to
 set up overrides in SM Standard Item Overrides if billable rates differ for certain
 customers and/or service sites.

## Effective Dates

Use this tab to define material rate overrides by effective date. You must first add
 Effective Date templates using SM Add Effective Date (accessed by clicking the Add
 button below grid). You can then set up rate overrides for each effective date
 template as needed.
Note: Setting up effective date overrides is purely optional; you will typically
 only use this tab if rates change routinely and are applied based on a specific
 date.The system will only use the rates defined for an Effective Date
 template if no override rates are found at the service site or customer
 level.

For more information about effective date templates, see [Add a New Effective Date Template](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/add-a-new-effective-date-template) and [SM Rate Template Effect Dates Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-template-effect-dates-form).

Note: You can also override standard, advanced, and effective
 date rates for equipment, labor, materials, non-material purchases, and standard
 items at the customer and service site levels. The system uses a specific
 hierarchy to determine which rate to use.

The following are related tasks:
[Set up a Rate Template](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-a-rate-template)
[Set up Equipment Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides)
[Set up Labor Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides)
[About Setting up Material Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides)
[Set up Override Rates for Non-Material Purchases](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases)
[Set up Override Rates by Cost Type for Non-Material Purchases](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases/set-up-override-rates-by-cost-type-for-non-material-purchases)

Related concepts

- [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides/equipment-rate-hierarchy)

- [Labor Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy)

- [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy)

Related information

- [About the EM Revenue Codes Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-codes-form)

- [About the EM Revenue Rates by Category Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-category-form)

- [About the EM Revenue Rates by Equipment Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-equipment-form)

- [About the IN Location Materials Form](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form)

- [SM Customers Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form)

- [SM Service Sites Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [SM Rate Override Material Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-material-form)
