---
title: "Material Pricing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/material-pricing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/material-pricing"
---

# Material Pricing

Material Sales uses a hierarchical method of locating the
 appropriate pricing for materials posted to tickets in MS Ticket Entry.

When a ticket is entered, the system performs a search in the following manner:

- Quote – The system first searches the quote files to see if an active quote exists for the specified customer/customer job/customer PO, JC job, or IN location. If an active quote exists, the system uses the quote to determine pricing. If no pricing exists on the quote for that material, it uses the quote’s price template.

- Pricing Templates – The system uses price templates
 when no pricing is specified for the material or material category on a quote.
 If an override price template is specified on the quote, it will use that price
 template first. If no price template is specified on the quote, then depending
 on the sale type (i.e. Customer, Job, or Inventory), it will use the price
 template assigned to the customer (in AR Customers), job (in JC Jobs), or
 location (in IN Locations), respectively.

- IN Location Materials (INMT) – If no pricing is
 found for the material or material category on a quote or price template, and
 the material is stocked, the system uses the cost/price defined in this program
 (based on the sale type’s Pricing Option as defined in IN Company Parameters),
 and applies any markup/discount rate defined for the sale type (in AR Customers,
 JC Jobs, or IN Location Materials).

- Headquarters Material file (HQMT) – If no pricing is found for the material or material category on a quote or price template, and the material is non-stocked (i.e. materials purchased from a material vendor), it will use the standard unit price defined in this program. For Inventory sales, the material must be stocked at the “To” location, even if it is not stocked at the sales location.

Note: When posting materials purchased from an outside vendor, the system treats them as non-stocked materials, regardless of whether the sales location normally stocks the specified material. Because it is recognized as a vendor-purchased material, inventory is not relieved during the update. However, the GL ‘sales’ accounts are updated accordingly.
The hierarchical method of defaulting a unit price for a material described above explains the different places that the system searches to find material prices. However, quotes and pricing templates have their own hierarchical setups, therefore, how the unit price for the material is actually determined is based on how the information is set up for the material on the quote or price template. For more detailed information, see Quote Pricing and Price Templates in Related Topics below.
