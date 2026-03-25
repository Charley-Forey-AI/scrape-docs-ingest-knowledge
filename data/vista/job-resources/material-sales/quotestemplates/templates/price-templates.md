---
title: "Price Templates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/templates/price-templates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/templates/price-templates"
---

# Price Templates

Material pricing is based on several factors (such as special
 pricing for customers who repeatedly buy large quantities of
 specific materials), the Material Sales module provides you with the
 ability to set up price templates (in MS Price Templates) which
 allow you to define specific pricing for a material or category of
 materials. Material prices are defined in HQ Materials and, if the
 material is stocked, in IN Location Materials.
Once you create a templaye, you can then assign it
 to customers (in AR Customers), jobs (in JC Jobs),
 or locations (in IN Location Materials), and when
 tickets are entered that specify the material or
 its category, the system will default the
 material’s unit priced based on the information on
 the template.
Price templates can be set up at different levels,
 allowing you to price materials based on a minimum set of information, or to price
 them more specifically with a maximum set of information. For example, you may have
 a material that comes in several finishes and/or sizes (such as concrete blocks),
 and certain customers routinely buy large quantities of those materials. You can set
 up each material separately on the template and specify a unit price or discount
 rate for each, or you can set them up by category, and have the unit price or
 discount rate apply to all materials within that category.
Pricing can also be set up at the location level, so if all the locations within a location group will sell the same product at the same standard price, then you need only set up pricing at the location group and material level. If a location will sell all materials within a category discounted from their standard unit price by the same percent, then set up the markup/discount percent at the location and category level.
There are four levels at which pricing can be defined (MS Price Templates, Rates tab). The first level represents the minimum set of information required. Each successive level provides more specific information, and overrides all preceding levels. For example, unit prices established for a specific location override those set up for the location group. Prices referencing a specific material override those at the category level, and so forth.

1. Location Group/Location (blank)/Category/Material (blank)/UM: Pricing is set up by location
 group and category.

1. Location Group/Location (blank)/Category/Material/UM: Pricing is set up by location group,
 category, and material.

1. Location Group/Location/Category/Material (blank)/UM: Pricing is set up by location group,
 location, and category.

1. Location Group/Location/Category/Material/UM: Pricing is set up by location group, location,
 category, and material

When a price template is searched for material pricing, the system must check the various levels at which pricing can be set up on the template. The first level searched will always be the level with the maximum amount of information provided (Level 4 in illustration above). If the material is not found at that level, it then checks the next highest level and so on, until it reaches the level with the minimum amount of information (Level 1 in illustration above). If no pricing is found at any level, the system will use the Pricing Option defined in IN Company Parameters for the purchaser to determine the material’s unit price.
Because of the various places in which pricing for materials can be defined, you should be aware that price templates assigned to customers, jobs, and locations may not always be used to determine a material’s unit price. If a quote exists for a customer, job, or location, the system will always use the pricing on the quote first, thereby overriding any pricing on a price template. If no pricing is found for the material on the quote, but the quote specifies an override price template, the system will use the quote’s price template rather than the standard price template assigned to the purchaser. The purchaser’s assigned price template is only used when there is no quote existing for the purchaser, or if there is a quote, when no pricing exists for the material/category, and no override price template is specified.
