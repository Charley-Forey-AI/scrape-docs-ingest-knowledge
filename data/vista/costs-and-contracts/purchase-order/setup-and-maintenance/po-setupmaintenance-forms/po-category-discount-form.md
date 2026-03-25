---
title: "PO Category Discount Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-category-discount-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-category-discount-form"
---

# PO Category Discount Form

Use this form to set up discounts offered by a vendor based on a category of materials.
It will provide unit cost defaults when entering purchase order items (PO Purchase Order Entry).
When setting up category discounts, the discount percent assigned to each material group/category becomes the standard discount offered by the vendor whenever materials in the category are purchased.
Entries made in this form calculate costs in either of the following ways:

- As a discount percent off the Vendor's Book Price (if set up in PO Vendor Materials)

- As a discount percent off the Price of the material in HQ Materials

Note that in both of these cases, it is calculated as a discount-off price and not cost.
Use the grid on the Job Discounts tab to set up override discount rates for specific jobs. The discount specified for each job is used to override the standard rate whenever buying materials for that job. The material's unit cost is calculated based on the standard price in HQ and the discount specified here.
Note: Material groups are assigned in HQ Company Setup and are specific to the assigned company (or companies). If you have multiple companies that purchase materials from the same vendor, and each company uses a different material group, make sure to set up category discounts for the vendor for each material group.
