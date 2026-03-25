---
title: "About the MS Payment Discount Templates Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/templates/about-the-ms-payment-discount-templates-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/templates/about-the-ms-payment-discount-templates-form"
---

# About the MS Payment Discount Templates Form

Use this form to set up discount templates for material-based discounts.
Assign templates to customers in AR Customers; the system only uses the templates for “Customer” sales. Templates assigned to quotes (in MS Quotes) override those assigned in AR Customers.
When you enter a ticket or hauler time sheet, the system calculates the payment discount based on the payment terms assigned to the Customer. If the payment terms are “rate based” (Discount Based on Material checkbox in HQ Payment Terms is not selected), discounts are calculated using the rate specified in HQ Payment Terms. If a customer’s payment terms are “material based” (Discount Based on Material checkbox is selected in HQ Payment Terms), then the system determines the discount as follows:
The system applies the rate found based on the material’s Payment Discount type (defined in HQ Materials). If rate based, the calculation is the rate multiplied by the material total. If unit based, the calculation is the rate multiplied by the number of units sold.

## Setting Up Payment Discounts

To reduce the amount of setup required,
 the system allows payment discounts at several different levels. For example, if all
 the locations within a location group discount the same product at the same standard
 rate or amount, set up discounts at the location group and material level. If a
 location sells all materials for a category by the same rate or amount, setup the
 New Rate at the location and category level.
Since discounts may be set up at several
 levels, the system uses a hierarchy to find default unit prices. The following table
 displays the hierarchy. Each column in the table represents a column on the Rates
 tab. The first row represents the minimum set of information required. The system
 sets up discounts by the columns containing a supplied value. An X denotes a
 supplied value. In the table, the first row indicates that the system sets up
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
