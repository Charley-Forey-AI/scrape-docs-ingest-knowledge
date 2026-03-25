---
title: "About the MS Quotes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quotes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quotes-form"
---

# About the MS Quotes Form

Use this form to set up quotes for selling materials to customers, jobs, and/or other inventory locations.
Quotes allow you to assign materials, quantities, and prices for specific customer jobs, your own jobs, or purchasing inventory locations. You can also establish defaults and overrides for material pricing, payment discounts, haul codes, haul zones, pay codes, phases and cost types for job sales, and invoice controls for customer sales. The system treats accepted quotes like sales orders indicating the materials, prices, and quantities for shipping or hauling.
Note: The system automatically updates allocations of stocked materials to Inventory when quoted materials become 'ordered' and relieved when tickets are posted or the quote is closed. General Information

## How a Quote is Used

The system uses quotes to provide
 certain information—specifically, material prices and/or haul rates—when entering
 tickets in [MS Ticket Entry](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form). When you upload a ticket or enter
 it manually, the system searches for active quote information based on the sale type
 and purchaser. When you make a customer sale, the system searches for the customer’s
 entry based on Customer #, Customer Job, and PO#. If the sale is to a job or other
 inventory location, the system searches for an active quote entry for that specific
 job or location. If the system finds an entry, it uses the information on that quote
 to provide default values.
The types of quotes used in this form
 are:

- Customer — Customer quotes can
 be set up at the customer, customer job, or customer PO level.  Customer
 level quotes enable you to define one master quote for several jobs. Use
 master quotes when quote information does not change on a per job basis. For
 example, if you have a customer that typically receives a certain discount
 on selected materials, set up the master quote to include the discount.
Customer Job level quotes are used when certain jobs require special pricing
 or discounts. By setting up customer job quotes, you can override certain
 material pricing, discounts, and haul information without affecting any
 quotes set up at the customer level.
Customer PO level quotes enable
 you to define specific pricing and/or discounts for use with a specific
 purchase order.
Note: When you enter customer-related tickets in [MS Ticket Entry](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form), the systems makes a
 hierarchical search for a customer quote. The system will first search for
 an active quote matching the customer, customer job, and customer PO#. If a
 quote is not found at that level, the system searches for an active quote
 matching the customer and customer job. If a quote is not found at that
 level, the system then searches for an active quote for the customer.


- Job — Job quotes are set up on a
 per job basis, allowing you to define material pricing information and haul
 rates for each job to which you sell materials. You also have the option to
 establish phase and cost type information that the system uses as defaults
 when entering or editing tickets and hauler time sheets.

- Inventory— Inventory quotes are set up on a company/location basis; pricing
 information is specific to each location within a company to which you sell
 materials. Remember, selling materials to another inventory location is not the
 same as a material transfer; do not use quotes unless you are actually selling
 the materials. If you are selling materials to other inventory locations, you
 may also need to set up the intercompany invoicing option (in MS Company
 Parameters) so that sales can be invoiced and paid in the same manner as a
 customer sale.

## Info and Invoices Tab

Use the Info tab to set up general
 information about the quote: quote type (Customer, Job, Inventory), quote contact,
 expiration date, and the price and discount templates that the system uses for
 material pricing and payment discounts, respectively.
For job and customer quotes, if you are
 using the oil price escalation/de-escalation feature (i.e. have set up price indexes
 in HQ Escalation Index), you can apply price escalators to the job or
 customer/customer job by checking the Apply Price Escalators box (Info
 tab) and setting a Bid Index Date. Based on the sales of applicable materials (e.g.
 asphalt mixes, etc.) to the job or customer/customer job in MS Ticket Entry, the MS
 Oil Price Escalation report will determine increases/decreases in pricing using the
 bid index date specified for the quote and the pricing index (monthly
 escalation/de-escalation). You can then use the MS Oil Price Escalation report to
 review the resulting pricing adjustments.Note: If you check
 the Apply Price Escalators box for a job quote, and have also
 checked the Apply Price Escalators box
 for the job/project in JC Jobs/PM Projects, the bid index date specified on the
 quote will take precedence over the contract start date. The contract start date
 will only be used if no quote exists for the job.
Note: You can use the MS Oil Price Setup report to easily review
 quotes, by state, that are using this feature.

 See [HQ Escalation Index ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-escalation-index-form) for information about the
 pricing escalation feature.
For customer quotes only, use the
 Invoice tab to set up additional information related to invoices. This includes the
 Create a
 Separate Invoice checkbox, which in conjunction with the Invoice
 Level in AR Customers, determines how the system groups tickets and hauler time
 sheets together for invoicing. You can also set the billing frequency to have the
 system bill qualifying and hauler time sheet detail at specific times.

## Quote Detail Tab

Use this tab to quote specific
 materials, prices, and quantities. Material pricing is defined by location and
 material, but may also be defined by material vendor.
For each location/material, indicate the
 quoted units, unit price, required date for the material, quote status, and the
 number of units ordered. The system automatically updates the number of units
 sold-to-date each time you post a ticket that includes the specified material.
If you are setting up a job quote, you
 can also override the pricing by phase. Pricing defined on this tab overrides all
 other pricing defined for the location or material category. The system always
 checks here first for pricing information when posting tickets that include
 materials specified on this quote.
The pricing hierarchy for quote detail
 depends on whether the quote is a non-job (customer or inventory) or job quote.
Customer and Inventory Quotes:

- Location/Material/UM

- Location/Material Vendor/Material/UM

Job Quotes:

- Location/Material/UM/Phase - blank

- Location/Material/UM/Phase (valid part)

- Location/Material/UM/Phase

Regardless of quote type, the first
 level represents the minimum information set, while the last level represents the
 maximum set of information available
Note: If the quote is for a locked job, you should
 only define pricing overrides for phases set up for the job in JC Job Phases. MS
 Ticket Entry does not allow entering non-job phases for locked jobs; therefore,
 material pricing defined for a phase that is not set up for a locked job (in JC Job
 Phases) would never be used.
If you interfaced material quotes from
 PM (PM Material Detail), the records will be set up on this tab. The interface (from
 PM) checks all material quote records by location, material, UM, and phase. If
 multiple phase records exist for the same location/material/UM and the unit price is
 the same, the system adds a single record to this grid and the phase is left blank.
 If the unit price differs for any phase matching the location/material/UM, the
 system adds a separate record to this grid for each phase occurrence.

## Price Overrides Tab

Use this tab to override the quote’s
 price template at the material category level. Overrides allow you to establish
 special pricing for a quote without having to create a new price template. Unless
 you override pricing for a material on the Quote Detail tab, the system uses these
 overrides for a unit price default.
The pricing hierarchy for material
 category overrides depends on whether the quote is a non-job (customer or inventory)
 or job quote. For customer and inventory quotes (non-job), there are only two
 material category pricing levels. The first level represents the minimum set of
 information required and applies to all materials within a category for all
 locations within a group. The second level also applies to all materials within a
 category, but only within a specific location. The levels display below; an x
 indicates a value supplied by the user.
Loc Group
Location
Category
UM

x

x
x

x
x
x
x

For job quotes, there are six material
 category pricing levels. The first level represents the minimum set of information
 required, while the last level represents the maximum set of information available.
 The levels display below; an x indicates a value supplied by the user.
Loc Group
Location
Category
UM
Phase

x

x
x

x
x
x
x

x

x
x
x (valid part)

x

x
x
x

x
x
x
x
x (valid part)

x
x
x
x
x

Note: If the quote is for a locked job, you should
 only define pricing overrides for phases set up for the job in JC Job Phases. MS
 Ticket Entry does not allow entering non-job phases for locked jobs; override
 pricing defined for a phase that is not set up for a locked job (in JC Job Phases)
 would never be used.

## Discount Overrides Tab

Use the Discount Overrides tab to set up
 overrides to the quote’s discount template. Discount overrides apply to customer
 quotes only, and allow you to establish special payment discounts without having to
 set up a new discount template. For the system to use these discount overrides,
 payment terms must be set up for the customer in AR Customers, and the payment terms
 must be material based (i.e. “Discount Based on Material” checkbox is selected).
When you enter tickets, the system
 searches for an active quote with payment discount overrides set up on this tab.
 While searching, the system uses the same hierarchy outlined for standard payment
 discounts.
The first level of the hierarchy
 represents the minimum set of information required. Each successive level provides
 additional information and overrides all preceding levels. For example, discounts
 established for a specific location override those set up for the location group.
 The levels display below; an x indicates a value supplied by the user.
Loc Group
Location
Category
Material
UM

x

x

x

x

x
x
x

x
x
x

x

x
x
x
x
x

## Haul Code Defaults Tab

Use the Haul Code Defaults tab to set up
 haul code defaults that the system uses when entering tickets (that include
 equipment or a haul vendor) and hauler timesheets. The location group, location,
 category, material, truck type, and unit of measure columns are similar to the
 standard haul code setup, except here they provide a haul code default and are not
 dependent on a Haul Code basis.
When you enter a ticket or hauler time
 sheet with a haul vendor or equipment code, the system searches for an active quote
 with haul code default information using the hierarchy from the following table. An
 x denotes a value supplied by the user. In the table, the first row indicates that
 the system sets up pricing by location group and unit of measure. Each successive
 level provides additional information and overrides all preceding levels. For
 example, a haul code default for a specific location overrides those set up for the
 location group.
Loc Group
Location
Category
Material
Truck Type
UM

x

x

x

x
x

x

x

x

x

x

x
x

x

x
x

x

x

x
x
x
x

x
x

x

x
x

x
x

x
x
x

x

x
x
x

x
x

x
x
x
x

x

x
x
x
x
x
x

If the system finds an entry, it uses
 that haul code as the default. If a default haul code is not found here, the
 standard haul code assigned to the material in HQ Materials will be used, and the
 standard haul rates assigned in MS Haul Codes determine its rate.

## Haul Overrides Tab

Use the Haul Overrides tab to set up
 haul rate override information that defaults when entering tickets and hauler time
 sheets. The location group, location, category, material, truck type, and unit of
 measure columns provide override haul rates.
When you enter a ticket or hauler time
 sheet with a haul vendor or equipment code, the system searches for an active quote
 with haul rate and minimum amount overrides using the following hierarchy.
The following table identifies the
 levels and search order the system uses to find an override haul rate and minimum
 amount. An x denotes a value supplied by the user. In the table, the first row
 indicates that the system sets up pricing by location group and unit of measure.
 Each successive level provides additional information and overrides all preceding
 levels.
Loc Group
Location
Category
Material
Truck Type
UM
Haul Code

x

x
x

x

x
x
x

x

x

x
x

x

x

x
x
x

x

x
x

x
x

x

x
x
x
x
x

x
x

x
x

x
x

x
x
x

x
x
x

x
x

x
x
x

x
x
x

x
x
x
x

x
x

x
x
x
x
x
x
x

The following table identifies the
 levels and search order the system uses to find an override haul rate and minimum
 amount for job quotes. An x denotes a value supplied by the user. In the table, the
 first row indicates that the system sets up pricing by location group and unit of
 measure. Each successive level provides additional information and overrides all
 preceding levels.
Loc Group
Location
Category
Material
Truck Type
UM
Haul Code
Phase
Valid Part

x

x
x

x

x

x
x
x

x

x
x
x

x

x

x
x
x
x

x

x

x
x

x

x

x

x
x
x

x

x

x
x
x

x

x

x

x
x
x
x

x

x
x

x
x

x

x

x
x

x
x
x

x

x
x
x
x
x

x

x

x
x
x
x
x
x

x
x

x
x
x

x

x
x

x
x
x
x

x
x
x

x
x

x

x
x
x

x
x
x

x
x
x

x
x
x

x

x
x
x

x
x
x
x

x
x
x
x

x
x

x

x
x
x
x

x
x
x

x
x
x
x
x
x
x

x

x
x
x
x
x
x
x
x

## Haul Zones Tab

Use this tab to set up haul zone
 defaults that the system uses when entering or editing tickets or hauler time
 sheets. Use haul zones to determine unit or load-based vendor haul and pay rates.


## Pay Codes Tab

Use this tab to provide haul vendor pay
 code defaults and pay rate override information when entering or editing tickets and
 time sheets.
When you enter a ticket or hauler time
 sheet with a haul vendor, the system searches for an active quote with pay code
 information using the hierarchy from the following table. An x denotes a value
 supplied by the user. In the table, the first row indicates that the system sets up
 pricing by location group and unit of measure. Each successive level provides
 additional information and overrides all preceding levels. For example, a pay code
 default for a specific location overrides those set up for the location group.
Loc Group
Location
Category
Material
Truck Type
UM

x

x

x

x
x

x

x

x

x

x

x
x

x

x
x

x

x

x
x
x
x

x
x

x

x
x

x
x

x
x
x

x

x
x
x

x
x

x
x
x
x

x

x
x
x
x
x
x

If the system finds an entry, it uses
 that pay code as the default. If the pay code has an override rate, the pay rate
 also defaults. If you did not assign an override rate, the system determines the
 default using the standard pay rates assigned in MS Pay Codes.
Note: If a default haul code is not found here, the
 system uses the standard pay code assigned to the material in HQ Materials and the
 standard haul rates assigned in MS Haul Codes determine its rate.

## Job Phases Tab

For Job quotes only, use this tab to set
 up phase and cost type information that defaults when you enter or edit tickets and
 hauler time sheets. This information is searched to determine which phase and cost
 type should apply to the material and haul charges of a job sale. If values are not
 found here, the standard phase and cost type defaults in HQ Materials will be used.
The system uses the hierarchy in the
 following table to determine phase and cost type defaults. An x denotes a value
 supplied by the user. The first level represents the minimum set of information
 required. Each successive level provides additional information and overrides all
 preceding levels. For example, defaults established for a specific Location override
 those setup for the Location Group.
Loc Group
Location
Category
Material

x

x

x

x
x

x
x
x

x
x
x
x

If the system does not find any values,
 it uses the standard phase and cost type defaults in HQ Materials.

## Surcharge Overrides Tab

Use the Surcharge Overrides tab to
 override the standard surcharge rates for a quote. Overrides set up on this tab will
 be applied to the surcharge codes within the quote's designated surcharge group, and
 allow you to establish special rates for a quote without affecting the standard
 rates for a surcharge group.
Overrides set up on this tab will be
 applied to the surcharge codes within the quote's designated surcharge group, and
 allow you to establish special rates for a quote without affecting the standard
 rates for a surcharge group.
When a ticket is entered using [MS Ticket Entry ](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form), the system will first check for a
 quote and if one exists, verify that the Apply Surcharges box is checked.
 (If the box is not checked, no surcharges will be assessed, regardless of whether
 surcharge overrides exist on this tab or a surcharge group is assigned in MS Company
 Parameters.) If the Apply Surcharges box is checked,
 the system will then assess surcharges for the ticket based on the surcharge codes
 within the surcharge group. If the values entered on the ticket meet the criteria
 defined on this tab, surcharges will be assessed using the override rates. If the
 override criteria is not met, surcharges will be assessed based on the standard
 rates defined in MS Surcharge Codes.
Note: The surcharge rates defined on this tab are not
 affected by the Effective Date designated for the surcharge rates in MS Surcharge
 Codes. The Effective Date will only apply if override criteria is not met and
 standard rates are used.
Surcharges are assessed for each
 surcharge code within a surcharge group. If surcharge overrides exist and the
 Apply
 Surcharges box is checked (on the quote), the system will compare
 the values entered on the ticket with the override values. If a match is found, a
 surcharge will be assessed using the specified override rate. The system will repeat
 this process for each surcharge code in the group. If no match is found for a
 surcharge code, the system will use the standard rate defined for that code in MS
 Surcharge Codes.
The following table shows the hierarchy
 used when determining the override rate to use. An x denotes a supplied value. The
 first row in the table identifies the minimum set of information required for a
 surcharge code. Each successive row provides more specific information, and
 overrides all preceding levels. For example, rates defined by location will override
 rates defined for the location group; rates defined by material will override rates
 defined for the category, and so forth.
Surcharge Code
Loc Grp
Location
Category
Material
Truck Type
UM

x
x

x
x

x

x
x

x

x
x

x
x

x
x

x

x
x

x

x

x
x

x

x

x
x

x

x
x

x
x

x

x
x

x

x

x
x

x

x

x
x

x

x
x

x
x
x

x
x
x

x

x
x
x

x

x
x
x

x
x

x
x
x
x

x
x
x
x

x

x
x
x
x

x

x
x
x
x

x
x

x
x
x
x
x

x
x
x
x
x

x

x
x
x
x
x
x

x
x
x
x
x
x
x

Related information

- [About the MS Surcharge Groups Form](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-groups-form)
