---
title: "Set up Override Rates for Non-Material Purchases | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases"
---

# Set up Override Rates for Non-Material Purchases

You can override the standard markup rate for non-material
 purchases defined on a rate template by rate break point and/or by cost type.
When you capture non-material purchases on work
 completed purchase lines (in SM Purchase Order Entry or PO Purchase Order) or
 work completed miscellaneous lines (in SM Work Orders or AP Transaction
 Entry), the system determines the markup rates to use based on the overrides defined for
 non-material purchases on the work order scope's assigned rate template.You can set up override markup rates for non-material purchases
 at the rate template, effective date, customer, and service site levels, as well as
 at the work order quote scope level. The system uses a specific hierarchy to
 determine the rate to use. For more information, see [Non-Material Purchases Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases/non-material-purchases-rate-hierarchy).

1. Depending on the level at which you want to set up
 markup rate overrides, do one of the following:

- Rate Template - Open SM Rate Templates and select
 the rate template to work with.

- Effective Date - Open SM Rate Template, select
 the rate template, and then on the Effective Dates tab, double-click in the
 grid to open the SM Rate Template Effect Dates form.

- Customer - Open SM Customers, select the
 customer, and click the Override Rates button to open the SM Rate Override
 Base form.

- Service Site - Open SM Service Sites, select the
 service site, and click the Override Rates button to open the SM Rate
 Override Base form.

1. In the Non-Material Purchases section of the selected form, click the Advanced
 button.The SM Advanced Non-Material form displays.

1. On the Rate Break Points tab, in the Break Point field,
 enter the total dollar amount to use as the first break point when calculating
 markups for non-material purchases.

1. In the Percent field, enter the percent to use when
 calculating markups for non-material purchases on an SM work order.

1. Save the record.

1. Add additional break points as needed.

1. If you want to set up override markup rates by cost type, select the Cost Type
 Overrides tab and do the following:

1. In the Seq field, enter N
 or + to add a new line.

1. In the Cost Type field, enter a cost type for
 non-material purchases or press F4 to select from
 a list of valid SM Cost Types.

1. In the Markup Percent field, enter the override
 markup percent (e.g. enter 5% as 5.00000) for the specified cost type.


1. Save the record.

1. Add additional cost types as needed.

1. If you want to set up cost type override rates by break point:

1. Select the Cost Types tab and double-click in the grid.The SM Adv. Non-Material Overrides form displays.

1. Click on the Rate Break Points tab.

1. Use the Break Point and
 Percent fields to enter override break point
 markup rates (as described in Steps 3-5).
