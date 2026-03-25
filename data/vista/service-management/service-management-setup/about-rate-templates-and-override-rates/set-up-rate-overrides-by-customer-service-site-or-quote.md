---
title: "Set Up Rate Overrides by Customer, Service Site, or Quote | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-rate-overrides-by-customer-service-site-or-quote"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-rate-overrides-by-customer-service-site-or-quote"
---

# Set Up Rate Overrides by Customer, Service Site, or Quote

You can set up overrides to equipment, labor, material, and
 standard item rates defined on a rate template by customer, service site, or work order
 quote.
Rate overrides at the customer, service site, and
 work order quote level are handled in SM Rate Override Base. However, access to this
 form depends on whether you are setting up overrides at the customer, service site, or
 quote level.Note: If you set up overrides at multiple levels, the system uses a specific
 hierarchy to determine the correct rates to use. For more information, see [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides/equipment-rate-hierarchy), [Labor Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy), or [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy).

1. Open SM Customers, SM Service Sites, or SM Work Order Quotes, depending on where you want to set up rate overrides.

1. In the form you opened, select the record for which to set up rate overrides.

1. Click the Override Rates button (below the Rate Template field).The SM Rate Override Base form displays.

1. In the Markup field of the Equipment Rates section, enter the override
 markup rate for equipment used on a work order.Leave blank if no override
 markup applies.

1. In the Rate field of the Labor Rates section, enter the override labor
 rate to use when capturing labor on a work order. Leave blank if no override
 markup applies.

1. From the Type drop-down in the Material Rates section, select Markup or Discount to identify what the
 material rate represents. Select N-No
 Override if you are not overriding the standard material
 rate. Then skip to Step 11.

1. For Markup or Discount
 rate types only, use the Basis drop-down to select the
 rate type for deriving the Billable Rate for materials
 on a work order:

- A-Actual Cost

- S-Standard Cost

- V-Average Cost

- L-Last Cost

- P-Standard Price

1. If you selected the
 M-Markup or D-Discount rate
 type in Step 5, use the Percent field to enter the
 override markup or discount rate.

1. If you selected the
 M-Markup or D-Discount rate
 type in Step 5, use the Break Points By drop-down to
 select how to apply rate break points:

- T-Total Cost

- U-Unit Cost

1. In the Markup
 Percent field of the Non-Material Purchases section, enter the
 markup percent to use for non-material work completed purchase lines on a work
 order.

1. Save the record.

1. Optionally, [set up equipment rate overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides#ID-0003f6ff--en__ID-0003f6ff).

1. Optionally, [set up labor rate overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides#ID-0003f7a6--en__ID-0003f7a6).

1. Optionally, [set up material rate overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides#ID-0003f98c--en__ID-0003f98c).

1. Optionally, [set up standard item overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-standard-item-overrides#ID-0005d4fb--en__ID-0005d4fb).

1. Optionally, [set up non-material purchase overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases).

Related concepts

- [SM Rate Override Base Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-override-base-form)
