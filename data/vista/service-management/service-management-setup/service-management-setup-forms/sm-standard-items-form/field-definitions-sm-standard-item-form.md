---
title: "Field Definitions: SM Standard Item Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-standard-items-form/field-definitions-sm-standard-item-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-standard-items-form/field-definitions-sm-standard-item-form"
---

# Field Definitions: SM Standard Item Form

The following is a list of field descriptions for the SM
 Standard Item form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Standard Item

The Standard Item field on the SM Standard Items form.
Enter a name or code to represent this standard item (for example, Trip Chg, Surcharge, etc.). Up to 20 characters allowed.

## Description

The Description field on the SM Standard Items form.
Enter a description of this standard item. Up to 60 characters allowed.

## Cost Rate

The Cost Rate field on the SM Standard Items form.
Enter the default cost rate for this serviceable item. The rate specified here defaults as the Cost Rate when entering miscellaneous work completed items for a work order (in SM Work Orders). May be overridden.

## Billable Rate

The Billable Rate field on the SM Standard Items form.
Enter the default billable rate for this standard. The rate specified here defaults as the Billable Rate when entering miscellaneous work completed items for a work order (in SM Work Orders), and is also the rate that defaults when creating an invoice for the work completed item. May be overridden on the work order and/or invoice.

- When referencing this standard item on a work completed line (in SM Work Orders), if the work order scope specified for the line has a Price Method of Non-Billable or Flat Rate, the line's Billable Rate is set to blank (and cannot be changed), regardless of the billable rate specified here.

- You can override the billable rate for a standard item at the rate template, effective date template, customer, service site, and work order quote level. For more information, see [Setting up Standard Item Overrides.](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-standard-item-overrides)

## Billable Markup Percent

The Billable Markup Percent field on the SM Standard Items form.
Optional.
Enter the markup percent (enter 5% as 5.00000) to define a markup instead of a flat price for a standard item.
Note: An entry in the Billable Markup Percent field replaces the Billable Rate.

## Cost Type

The Cost Type field on the SM Standard Items form.
Enter the cost type (from SM Cost Types) related to this standard item, if applicable. The cost type specified here defaults as the cost type for miscellaneous work completed lines (entered in SM Work Orders) referencing this standard item.
