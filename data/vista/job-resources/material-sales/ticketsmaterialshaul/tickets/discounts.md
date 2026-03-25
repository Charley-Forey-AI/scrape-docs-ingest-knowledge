---
title: "Discounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/discounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/discounts"
---

# Discounts

Discounts are used only when entering tickets for customer sales. How payment discounts are calculated for a customer depends on the customer’s assigned payment terms.

## Rate-Based Payment Terms

If a customer’s payment terms are rate-based (the Discounts Based on
 Material option in HQ Payment Terms is not checked), the discount
 offered is calculated using the discount percent specified for the payment terms.
 Rate-based discounts are always calculated on the sale total.

## Material-Based Payment Terms

If the payment terms are material-based (the Discounts Based on Material
 option in HQ Payment Terms is checked), the system will perform a hierarchical
 search to determine what discount rate/amount to use:

1. The system checks for a quote, and if one exists, looks to see if a discount
 override exists for the material or material category. If one exists, that
 rate or amount (depending on the Payment Discount type specified for the
 material in HQ Materials) will be used.

1. If a quote with a discount override does not exist, the system then uses the
 discount template specified on the quote.

1. If a discount template is not specified on the quote, the discount template
 specified for the customer in AR Customers is used.

1. If no discount template is specified for the customer, the discount
 specified for the material in HQ Materials is used. If unit-based, the
 discount offered is calculated on units sold. If rate-based, it is
 calculated on the material total.

## Discount Templates

Discount templates are used for defining discount rates for material-based discounts.
 They are not required, but they do allow you to tailor payment discounts for
 specific materials or material categories. Also, by assigning the templates to
 customers (in AR Customers), you can control the discounts offered by customer. For
 example, you may have customers that frequently buy large quantities of a specific
 material. By setting up the material on a discount template, you can assign an
 appropriate discount to that material, then restrict to which customers you assign
 the template. However, customers will receive the discount for that material only if
 the customer’s payment terms are material-based. Discount templates are set up in
 [MS Payment Discount Templates](/en/vista/vista/job-resources/material-sales/quotestemplates/templates/about-the-ms-payment-discount-templates-form).
