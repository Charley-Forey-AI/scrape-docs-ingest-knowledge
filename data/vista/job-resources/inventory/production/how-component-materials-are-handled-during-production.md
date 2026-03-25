---
title: "How Component Materials are Handled During Production | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/production/how-component-materials-are-handled-during-production"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/production/how-component-materials-are-handled-during-production"
---

# How Component Materials are Handled During Production

When you produce a finished good, the system uses a Bill of
 Materials to determine the components needed for the finished good, as well as the locations
 affected. In addition, the bill of materials determines how the components are
 handled.
During production entry, the system will first look to see if there is an override Bill of Materials for the specified production location. If there is, the system uses that Bill of Materials to product the finished good and relieve inventory. If an override Bill of Materials does not exist, it will use the standard Bill of Materials for the location group.
If the standard Bill of Materials is used, the system pulls all components from the production location specified in IN Production Entry (manual production) or in MS Ticket Entry (auto production). If entering production manually, the system will also store the finished good at the same location.
If an override Bill of Materials is used, the system pulls each component from the location specified for that component in IN Bill of Materials Override. The finished good is stored at the location specified in the override bill of materials header. When a finished good is produced in this manner, the [ Usage Option ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form#ID-0001380a--en) (IN Company Parameters) determines how the component materials are handled. There are two usage options available:

- Sale - If this usage option is selected, the materials are “sold” to the production location and priced using the MS pricing hierarchy (i.e., quote, price template, or Pricing Option in IN Company Parameters).

- Quote – If an active quote exists for the production location that includes component materials from another location, the system uses the quote to determine pricing. If no pricing exists on the quote for the material, the system uses the quote’s price template.

- Pricing Templates – If an override price template is
 specified on the quote, the system uses the override template. If a price
 template is not specified on the quote, the system uses the MS Price
 Template specified for the production location in IN Locations.

- Pricing Option – If pricing is not found on a quote or price template, the system uses the cost or price defined for the production location (depending on the Pricing Option selected for inventory sales in IN Company Parameters) and applies any markup or discount rate defined for the materials in IN Location Materials).

Note:For more information about the MS pricing hierarchy, refer to Material Pricing in Related Topics below.

- Transfer - If this usage option is selected, the
 component materials are “transferred” to the production location. Value is
 determined by the Cost Method specified for the location (IN Locations) or
 material category (IN Location Category Override).
