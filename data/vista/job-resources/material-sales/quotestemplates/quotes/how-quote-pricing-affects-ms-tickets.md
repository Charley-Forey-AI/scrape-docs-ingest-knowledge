---
title: "How Quote Pricing Affects MS Tickets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/how-quote-pricing-affects-ms-tickets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/how-quote-pricing-affects-ms-tickets"
---

# How Quote Pricing Affects MS Tickets

Each time a ticket is entered in MS Ticket Entry, the system
 performs a hierarchical search of the various files in which material pricing can be
 defined. As described throughout the Material Sales help system, the standard search begins
 with the quote files. However, because quotes have their own hierarchical setup, the system
 must search the various levels within a quote to determine where the material’s unit price
 will come from.

 When you set up a quote, you have several
 options as to how to define a material’s unit price. For customer quotes, the first
 option is whether you will define pricing at the customer level (often called the Master
 quote), the customer job level, or the customer PO# level. When the system performs its
 search, it will first look to see if a quote exists at the customer PO# level, then the
 customer job level, then lastly, at the customer (or master quote) level.
 Once a quote is located, the system must
 then search the different levels of the quote for the material price. The first level
 searched is the quote detail. This level defines pricing at the location/material level,
 and if a job quote, will include an additional location/material/phase level. If pricing
 cannot be found for the material at these levels, the system then checks for price
 overrides. Within this level, pricing can be defined using the minimum set of
 information (i.e. Location Group/Category/UM) or the maximum set of information
 (Location Group/Location/Category/UM or, if a job quote, Location
 Group/Location/Category/UM/Phase). If no price overrides are found at either of these
 levels, the system then checks to see if the quote specifies an override price template.
 If an override price template exists, it will use that template to determine material
 pricing. If no override price template is specified, then the price template assigned to
 the purchaser (in AR Customers, JC Jobs, or IN Location Materials) is used.
