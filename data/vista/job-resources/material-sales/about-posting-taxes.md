---
title: "About Posting Taxes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/about-posting-taxes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/about-posting-taxes"
---

# About Posting Taxes

When posting tickets, haul ticket add-ons, hauler time sheets,
 or material payments, the calculation of taxes is determined by whether the material and/or
 haul charges are flagged as taxable.

- Materials – The ‘Taxable’ option in
 HQ Materials determines whether a material is taxable. If checked, taxes will be
 calculated on the material based on the tax code specified on the ticket or
 material payment transaction. If unchecked, no taxes will be calculated on the
 material.

- Haul Charges – The ‘Subject to Sales
 Tax’ option defined for a haul code (in MS Haul Codes) determines whether haul
 charges posted to that haul code are taxable. If unchecked, haul charges are not
 taxable and will not be included in the tax basis on ticket, haul ticket add-on,
 or hauler time sheet transactions. If checked, haul charges are taxable based on
 the sale type (i.e. customer, job, or inventory), the Haul Tax Option assigned
 to the purchaser (in AR Customers, JC Jobs, IN Locations, or MS Quotes), and the
 hauler type (equipment or haul vendor). The Haul Tax Option determines whether
 haul charges are taxable and if so, whether they are taxable only when a haul
 vendor is used or are always taxable.

Another option to consider is the Tax Option
 in MS Company Parameters. This option allows you to specify where to default the tax
 code from when entering tickets, haul ticket add-ons, and hauler time sheets:

- 0 = No sales tax. Tax code will default as null. Typically, you would use this
 option if you are not calculating taxes for materials or haul charges. However,
 if taxes are to be calculated for a specific material and/or haul charge, you
 can enter the tax code manually.

- 1 = Sales Location. Defaults the tax code assigned to the
 sales location (IN Locations).

- 2 = Sale Type/Purchaser. Defaults tax code assigned to the “purchaser” based on
 the sale type. For example, if the sale type is 'Customer', tax code will
 default from AR Customers.

- 3 = Sale Type/Purchaser or Sales Location. Defaults tax code assigned to the
 “purchaser” based on the sale type. However, if no tax code assigned, use the
 tax code assigned to the sales location.

- 4 = Delivery. If materials are delivered, the tax code will default based on the
 sales type and purchaser. If materials are not delivered, the tax code defaults
 from the sales location.

Note: The existence of a tax code does not mean taxes will
 be calculated on the ticket. Taxes will only be calculated if the material and/or haul
 charges are flagged as taxable. If both the material and haul charges are taxable, the
 system adds the material total and the haul total together and calculates tax using the
 rate defined for the specified tax code. If only the material or haul charges are
 taxable, the tax basis will only include the taxable amount.

## Value Added Tax

The tax type selected when entering
 transactions (tickets, haul ticket add-ons, and/or hauler time sheets) indicates
 whether whether you are posting Sales tax, Use tax, or Value Added Tax (VAT). If you
 are tracking Provincial Sales Tax (PST) and/or Goods and Services Tax (GST), you
 will need to select the the 3-VAT tax type.
Note: If the Default Country for the active company is
 not ‘US’ (e.g. AU, CA, etc.), the tax type automatically defaults as ‘VAT’.
When processing VAT-related
 transactions, the update credits the appropriate GST and/or PST tax payable accounts
 (i.e, the Credit GL Account defined in HQ Tax Codes). For GST, if you are tracking
 Income Tax Credits (ITC), the update debits the GST amount to the tax payable
 expense account (Debit GL Account, HQ Tax Codes).
These updates will only occur for
 tickets, haul ticket add-ons, and hauler time sheets where the Sales Type is ‘Job’
 or ‘Inventory’. If the Sales Type is ‘Customer’, the GST/PST updates occur when
 posting the related invoice (in MS Invoice Edit). As with job and inventory
 transactions, the update credits the GST/PST tax payable accounts; however, no
 update occurs to the contra account (i.e. the Debit GL Account specified in HQ Tax
 Codes for tracking income tax credits).

Related information

- [About the MS Haul Ticket Add-Ons Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-ticket-add-ons-form)
