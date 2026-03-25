---
title: "About Posted Detail: Flat Price Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/updates-to-gl/about-posted-detail-flat-price-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/updates-to-gl/about-posted-detail-flat-price-work-orders"
---

# About Posted Detail: Flat Price Work
 Orders

When you process invoices for flat price work order scopes, the system displays the
 related accounting entries on the Posted Detail tab in SM Work Orders.
Although similar to posted detail entries for
 work completed lines, the posted detail entries for flat price work orders are handled a
 little differently. Flat price work orders do not require entering work completed, since
 billings are generated from flat price work order scopes rather than work completed
 lines.
When you bill the work order scope, a minimum
 of one revenue entry will be added to the grid for the billed amount. The number of entries
 will depend on the split revenue entries you defined (in SM Flat Price Revenue) for the
 flat price scope. For example, say the flat price for a scope is $1,000.00. You set up
 split revenue entries as follows:
Labor: $500.00
Other: $200
Material: $300
If you then bill the full $1,000.00, the
 Posted Detail grid will show three revenue entries; one for $500, one for $200, and one for
 $300.
Note: If you bill a work order scope in increments (e.g.
 50% in one billing and 50% in a second billing), the system will generate revenue entries
 for each billing.
If you enter work completed lines for flat
 price scopes, a cost entry will be added to the Posted Detail grid for each posted work
 completed line for the cost amount. However, because no invoicing will occur for these
 lines, no revenue entries will be ever be generated for them.
The GL accounts shown in the Posted Detail
 grid for revenue entries are determined using a similar hierarchy as the one used for
 determining GL accounts for work completed lines. For more information, see [Updates to GL](/en/vista/vista/service-management/work-orders/updates-to-gl).
