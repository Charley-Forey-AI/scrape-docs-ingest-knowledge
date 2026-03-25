---
title: "PO Vendor Materials Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-vendor-materials-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-vendor-materials-form"
---

# PO Vendor Materials Form

Use this form to enter overrides to material costs by vendor.
You can also use this form to set up overrides to material costs by job, vendor cross-references to HQ materials, and material substitutions.
When setting up material cost overrides, select one of four cost options to use for calculating the override cost for materials in the selected category:

- Standard Unit Cost – Uses the unit cost defined in HQ Materials for each material to calculate material costs. Used to define substitutes or vendor material numbers rather than override the standard cost.

- Vendors Unit Cost – Uses the unit cost specified for the vendor in this form to calculate material cost.

- Standard Book Price Less Discount – Uses the book price specified in HQ Materials for each material, plus the discount specified in this form to calculate material costs.

- Vendor Book Price Less Discount – Uses the book price and the discount specified in this form to calculate material costs.

## Material Cost Overrides by Job

Use the grid on the Overrides by Jobs tab to set up material cost overrides for specific jobs. For each job, specify one of two cost options:

- Unit Cost - the unit cost that will be used to calculate the material cost when buying for this job.

- Discount - the discount rate to be used in conjunction with the vendor's book price (if one exists) or the HQ book price to calculate material costs for the selected job.

## Cross-Referencing Vendor Materials to HQ Materials

The Vendor Material ID is generally the primary number used by the vendor to identify each of the materials they supply.
These numbers may be accepted and used by most vendors, such as Trade Service product ID's for electrical materials and equipment manufacturer's part numbers, or they may be unique to each vendor.
To cross-reference these vendor identification numbers with their HQ Material counterparts, use the Vendor's Matl ID field to enter the vendor's material ID number. The system cross-references this number with the HQ material each time the material is specified on a purchase order.

## Substitute Materials

Vendors often carry several products (each with its own identification number) that can be used as substitutes when a specific material is not available (for example, interchangeable filters from several different manufacturers). You can set up these substitute materials using the Substitute Materials tab.
For each substitute material, specify its material identification number and a description of the material. When entering a purchase order item (PO Purchase Order Entry), if a HQ Material has not been entered, but a Vendor Material ID has, the first occurrence of that number as a primary Vendor Material or Substitute will provide the HQ material number.
For example, you purchase a case of filters from a specific manufacturer, and the vendor sends a case of substituted filters. If you do not know the HQ Material number, enter the Vendor Material # when setting up the purchase order item. The system searches for the first occurrence of the Material ID number, whether it is set up as a cross-reference or substitute, and will provide the corresponding HQ material number in the Material field.
Note: Substitute materials are not validated, nor are they checked for uniqueness across materials.
