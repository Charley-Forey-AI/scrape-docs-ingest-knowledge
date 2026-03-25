---
title: "About Calculating Material Costs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/about-calculating-material-costs"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/about-calculating-material-costs"
---

# About Calculating Material Costs

 For PO items referencing material codes set up in HQ Materials, the system automatically defaults the unit cost of each item on the purchase order.
 The ECM field defaults from the Materials file in HQ Materials. Units are defined as being purchased per each, per hundred, or per thousand. This method is illustrated in the following example:
Units Ordered
Unit Cost
ECM
Total Cost

100
$200
E (1)
$20,000

100
$200
C (100)
$ 200

100
$200
M (1000)
$ 20

## Material Cost Overrides

If you are using the Category Discount and/or Vendor Materials features, you can set up overrides to material costs by vendor/category or by vendor. How costs for materials are calculated depends on how overrides are defined in these two forms.
When setting up category discounts, you assign a specific discount percent to each material group/category. The default material cost will then be calculated at the standard unit price in HQMT less the discount.
When setting up material cost overrides by vendor, you select one of four cost options that will be used to calculate the override cost for materials in the selected category. With either of these override methods, you can also set up overrides that apply to specific jobs, but do not affect purchases for other jobs.
For more information about category discounts, see [PO Category Discount Form](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-category-discount-form).
For more information about vendor materials, see [PO Vendor Materials Form](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-vendor-materials-form).
