---
title: "Set up Standard Items | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-standard-items"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-standard-items"
---

# Set up Standard Items

You can set up standard items to identify common work order charges that are not specific to work completed labor, equipment, or parts.
You can set up standard items to identify common work order charges that are not specific to work completed labor, equipment, or parts. Some examples are fuel surcharges, trip charges, and waste disposal.
 You can also use standard items for services that you perform but do not charge for based on special conditions. For example, if you have customers that you do not charge for certain materials, you can set those materials up as standard items, and set the cost and billable rates to 0.00. If you prefer to track the costs and charges for a standard item, you can enter cost and billable rate values here, and then select the No Charge checkbox for each applicable work completed miscellaneous line on the work order before you create the invoice.
To set up standard items in SM Standard Items:

1. Open the SM Standard Items form.

1. In the Standard Item field, enter the standard item code/name (e.g. TrpChg, Surchg, etc.).

1. In the Description field, enter a description of the standard item.

1. In the Cost Rate field, enter the default cost rate for the standard item. This amount will default as the Cost Rate when entering work completed miscellaneous lines that reference this standard item in SM Work Orders (work completed tab).

1. In the Billable Rate field, enter the default billable rate for the standard item. This amount will default as the Billable Rate when entering work completed miscellaneous lines that reference this standard item in SM Work Orders (work completed tab).

1. (Optional) In the Billable Markup Percent field, enter the markup percent (e.g. enter 5% as 5.00000) to define a markup instead of a flat price for a standard item.Note: An entry in the Billable Markup Percent field replaces the Billable Rate.

1. In the Cost Type field, enter the cost type (from SM Cost Types) related to this standard item, if applicable. The cost type specified here will default as the cost type for miscellaneous work completed lines (entered in SM Work Orders) referencing this standard item. Note: You can override the billable rate for standard items at the rate template, effective date template, customer, service site, and/or work order quote level. For more information, see [Setting up Standard Item Overrides.](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-standard-item-overrides)
