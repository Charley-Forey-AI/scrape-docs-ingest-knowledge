---
title: "Enter Flat Price Revenue | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service/enter-flat-price-revenue"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service/enter-flat-price-revenue"
---

# Enter Flat Price Revenue

If you create flat price scopes for customer work orders, work order quotes, or agreement services, you will need to break down the revenue (flat price amount) by cost type category.
You can set up as many entries as needed, but a minimum of one entry is required. All revenue sequences must be designated a cost type category. However, you can further break down revenue by assigning an SM cost type to each sequence. For example, you might set up two Equipment sequences, one using a cost type designated for rental equipment and one using a cost type designated for company equipment.
Work order scopes generated from approved work order quotes or agreement services will default the flat price revenue entries from the quote or agreement. You can edit the entries for scopes generated from a work order quote; however, you cannot edit entries for work orders generated from agreement services.
For Derived Flat Price quote scopes, the system automatically generates revenue entries based on entries added to the Materials, Labor, Misc, and Equipment tabs. If you need to change the revenue entries, you must do so by editing the applicable material, labor, miscellaneous, and/or equipment lines.

1. Open the SM Flat Price Revenue form using one of the following methods:

- From SM Work Scopes - Choose the appropriate work scope and select Revenue Split Setup.

- From SM Work Order Quotes - Select the work order quote and flat price quote scope, and then select Split.

- From SM Work Orders - Choose the work order and flat price scope, and then select Split.

- From SM Service - Choose the Flat Rate agreement service and select Split.

1. In the Seq field, enter N, New, or +.

1. From the Cost Type Category drop-down, select the cost type category which the specified revenue will be credited. Options are:

- Labor

- Equipment

- Material

- Other

- Subcontracts

1. If applicable, enter the cost type for this split revenue entry in the Cost Type field. The cost type's category (assigned in SM Cost Types) must match the cost type category specified for this sequence. If the line's cost type category is Other, any cost type may be entered.

1. In the Price Percent field, enter the percentage to apply to this sequence. If this is the only split revenue sequence you are entering, set this value to 100.00%.For work scopes, entry in this field is required. For agreement services, quotes, and work orders, you many leave this field blank if you prefer to enter a flat amount (in the Amount field).

1.  For agreement services, quotes, or work orders only, the Amount field defaults a value based on value entered in the Price Percent (or blank if no percent was entered). If you change the default amount, the system automatically recalculates the Price Percent.

1. If the specified Amount is taxable, select the Taxable checkbox. Otherwise, leave unselected.

1. Save the record.

1. Repeat the process to add additional split revenue sequences. Make sure the total of all sequences equals 100% of the Flat Price amount.

Related information

- [SM Flat Price Revenue Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-flat-price-revenue-form)

- [SM Service Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form)

- [SM Work Order Quotes Form](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [SM Work Scopes Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-work-scopes-form)
