---
title: "SM Rate Template Effect Dates Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-template-effect-dates-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-template-effect-dates-form"
---

# SM Rate Template Effect Dates Form

Use the SM Rate Template Effect Dates form to define equipment, labor, material, non-material purchase, and standard item override rates for effective date templates.
Access this form by double-clicking on
 an Effective Date in the Effective Date grid in SM Rate Templates.
Effective Date templates are created by
 copying the basic rate template or an existing effective date template (using
 SM Add Effective Date). The system copies the override and advanced override
 rates defined for the source template to the new effective date template. You can
 then use this form to modify the existing rates as applicable or enter new ones.
Note: You cannot create new Effective Date templates
 using this form; you must use [SM Add Effective Date](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-add-effective-date-form).
The following describes the different
 rates you can set up for an effective date template.

- Equipment - Use this section to enter the standard markup rate for the
 effective date rate template, as well as any advanced markup rates that apply to
 individual pieces of equipment. The system uses these rates when none are found
 at the customer or service site level.For information
 about how the system determines which rates to use, see [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides/equipment-rate-hierarchy).

- Labor - Use this section to define the standard labor rate for the effective
 date rate template, as well as any advanced labor rates that apply based on
 technician, craft/class, call type and/or pay type. The system uses these rates
 when none are found at the customer or service site level.For information about how the system determines which rates to use, see
 [Labor Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy).

- Material - Use this section to define the standard material markup/discount rate
 for the effective date rate template, as well as any advanced material rates
 that apply based on rate break points, category, or material. The system uses
 these rates when none are found at the customer or service site level.For information about how the system determines which
 rates to use, see [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy).

- Non-Material Purchases - Use this section to enter the markup rate for purchases that are for items other than materials (e.g. equipment rentals, subcontractors, etc.), as well as any advanced non-material markup rates that apply based on rate break points and/or cost types. When you enter a non-material work completed purchase line (via SM Purchase Order Entry or PO Purchase Orders) or a work completed miscellaneous line (via SM Work Orders), the system applies a markup rate using the appropriate break point or cost type override, or the standard rate if no overrides exist. For more information, see [SM Advanced Non-Material Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-advanced-non-material-form) and [SM Adv. Non-Material Overrides Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-adv.-non-material-overrides-form).Note: The system only uses the rates defined here when no override rates are found at the customer or service site levels.

- Standard Item Overrides - The Standard Item Overrides option allows you to
 override the billable rate defined for standard items in SM Standard Items. You
 will only need to set up overrides in SM Standard Item Overrides if billable
 rates differ for certain customers and/or service sites. The system uses these
 rates if none are found at the service site, customer, or effect date levels
 (respectively).

## How the System Uses Effective Date Rates

When you enter a work completed line for a work order, the system will first look for
 overrides at the service site and/or customer level.
If no overrides are found, the system
 will then look to see if Effective Date overrides exist for the rate template
 specified on the work order scope. If one or more effective dates exist, the system
 will then compare the date specified for the work completed line with the effective
 dates on the rate template. If a match is found, the rates defined for that template
 will be used.
For example:
Rate Template: Standard
Effective Date: 10/01/18
Effective Date: 06/01/19
Effective Date: 01/01/20
If the work completed line date is
 05/15/19, the system will use the Effective Date 10/01/18 template, since the entry
 date falls after 10/01/19, but prior to 06/01/19. However, if the work completed
 line date is 09/30/18, the system will use the Standard rate template, since the
 entry date falls prior to the first effective date template (10/01/18).

Related concepts

- [SM Rate Equipment Overrides Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-equipment-overrides-form)

- [SM Advanced Labor Overrides Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-advanced-labor-overrides-form)

- [SM Rate Override Material Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-material-form)

- [About Material Rate Break Points](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/about-material-rate-break-points)

Related tasks

- [Update Rates for Effective Date Templates](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/add-a-new-effective-date-template/update-rates-for-effective-date-templates)

Related information

- [SM Rate Templates Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form)
