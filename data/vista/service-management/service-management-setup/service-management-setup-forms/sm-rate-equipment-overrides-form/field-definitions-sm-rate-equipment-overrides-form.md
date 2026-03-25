---
title: "Field Definitions: SM Rate Equipment Overrides Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-equipment-overrides-form/field-definitions-sm-rate-equipment-overrides-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-equipment-overrides-form/field-definitions-sm-rate-equipment-overrides-form"
---

# Field Definitions: SM Rate Equipment Overrides Form

The following is a list of field descriptions for the SM Rate
 Equipment Overrides form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## EM Co

Required.
Enter the EM company to which this equipment
 rate override applies. This is the company in which the specified equipment resides. Press
 F4
 for a list of valid EM companies.

## Category

Category field on the SM Rate Equipment Overrides form.
Enter a
 category for your equipment. Press F4 for the Category Lookup list from
 which to select a category for your override equipment rate. Press F5 to connect
 to the [EM Categories](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-categories-form) form.

## Equipment

Required.
Enter the equipment to which this override
 rate applies. Press F4 for a list of valid equipment for the specified EM company.
When capturing equipment on a work order (in SM Work Orders), the system will apply the markup or flat rate (specified to the right) to any work completed equipment line matching the equipment and revenue code specified here.
Note: Equipment rates can be defined at the rate template, effective date, customer, and service site levels; therefore, the system will use a specific hierarchy to determine which equipment rates to use. For more information, see [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-equipment-overrides-form).

## Rev Code

Required.
Enter the revenue code to which this override
 rate applies. Press F4 for a list of valid revenue codes for the specified equipment or
 equipment category.
When capturing equipment on a work order (in SM Work Orders), the system will apply the markup or flat rate (specified to the right) to any work completed equipment line matching the equipment and revenue code specified here.
Note: Equipment rates can be defined at the rate template, effective date, customer, and service site levels; therefore, the system will use a specific hierarchy to determine which equipment rates to use. For more information, see [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-equipment-overrides-form).

## Rate Type

Select the rate type for this override rate entry.

- M - Markup — Select this option if using a markup rate to derive billable rates for work completed lines referencing the equipment/revenue code specified for this entry.

- F - Flat Rate — Select this option if using a flat rate to derive billable rates for work completed lines referencing the equipment/revenue code specified for this entry.

## Markup Percent

This field is enabled when the Rate Type is
 set to M-Markup
Enter the markup rate to use for calculating billable rates on equipment work completed lines (entered in SM Work Orders). For example, enter 5% as 5.00000.
 The system will calculate the billable rate for work completed lines as Cost Rate + (Cost Rate x Markup Rate).

- The system will only use this markup rate for work completed equipment lines specifying an equipment and revenue code matching the equipment and revenue code specified here.

- Equipment rates can be defined at the rate template, effective date, customer, and service site levels; therefore, the system will use a specific hierarchy to determine which equipment rates to use. For more information, see [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-equipment-overrides-form).

## Flat Rate

This field is enabled when the Rate Type is
 set to F-Flat
 Rate.
Enter the flat rate to use for calculating billable rates on equipment work completed lines (entered in SM Work Orders). The system will multiply this rate by the time units specified on the work completed line to derive the billable rate.

- The system will only use this flat rate for work completed equipment lines specifying an equipment and revenue code matching the equipment and revenue code specified here.

- Equipment rates can be defined at the rate template, effective date, customer, and service site levels; therefore, the system will use a specific hierarchy to determine which equipment rates to use. For more information, see [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-equipment-overrides-form).
