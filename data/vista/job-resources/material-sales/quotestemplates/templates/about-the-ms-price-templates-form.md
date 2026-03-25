---
title: "About the MS Price Templates Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/templates/about-the-ms-price-templates-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/templates/about-the-ms-price-templates-form"
---

# About the MS Price Templates Form

Use this form to create and maintain price templates that
 define material pricing levels and minimum charges that can be shared by Customers, Jobs,
 and Inventory Locations.
Price templates can be assigned in AR
 Customers, JC Jobs, and IN Locations, with overrides available per individual
 customer quotes (MS Quotes).

## Default Unit Price

When entering tickets in MS Ticket Entry, the system determines the default unit
 price based on the following hierarchy:

1. Material detail set up on an active quote - If an active
 quote exists for the purchaser, the system searches the Quote Detail tab for
 an entry matching the sales location and material. If the system finds an
 entry, it uses the unit price on that entry, regardless of status.

1. Pricing overrides set up on an active quote - If the
 system does not find pricing in the quote detail, it searches the Price
 Overrides tab on the quote based on sales location and material category. If
 the system finds an entry, it uses the unit price for the location and
 material category.

1.  Price template assigned to an active quote - If a price
 override does not exist, the system searches the price template assigned to
 the quote. Pricing hierarchy will determine which unit price to use.

1. Price template assigned in the AR Customers, JC Jobs, or
 IN Locations (depending on sale type) - If you did not assign a price
 template to the quote, or no active quote exists, the system searches the
 price template assigned to the purchaser in AR Customer, JC Job, or IN
 Location. Pricing hierarchy will determine which unit price to use.

1. If you did not assign a price template, or no entry
 within the price template exists for the material, the system applies the
 Pricing Option selected in IN Company and the markup/discount rates assigned
 in AR Customers and JC Jobs to standard prices in IN Location Materials
 (stocked) or HQ Materials (non-stocked).

## Moving New Pricing to Old

Once the effective date has passed, the ‘new’ prices are in effect and the 'old'
 prices are no longer valid. If you no longer need the 'old' values for ticket
 corrections, you can replace the 'old' values with the 'new' values. Select File > Move New Pricing to Old and the system updates all of the old values with the new values.
 Using this feature allows you to reset the Effective Date
 field and enter new pricing for the next scheduled update.

## Material Pricing

To reduce the amount of setup required, the system allows material pricing at several
 different levels. For example, if all the locations within a location group sell the
 same product at the same standard price, set up pricing at the location group and
 material level. If a location sells all materials for a category with the same
 discount, then setup the New Rate at the location and category level.
Since material pricing may be set up at
 several levels, the system uses a pricing hierarchy to find default unit prices. The
 following table displays the hierarchy. Each column in the table represents a column
 on the Rates tab. The first row represents the minimum set of information required.
 The system sets up pricing by the columns containing a supplied value. An X denotes
 a supplied value. In the table, the first row indicates that the system sets up
 pricing by location group, category, and unit of measure.
Each successive level provides
 additional information and overrides all preceding levels. For example, unit prices
 established for a specific location overrides those set up for the location group.
Loc Group
Location
Category
Material
UM

X

X

X

X

X
X
X

X
X
X

X

X
X
X
X
X
