---
title: "Field Definitions: MS Quotes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quotes-form/field-definitions-ms-quotes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quotes-form/field-definitions-ms-quotes-form"
---

# Field Definitions: MS Quotes Form

The following is a list of field descriptions for the MS
 Quotes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Quote

If you are adding a new quote and have enabled
 the 'auto-generate quote numbers' feature (option in MS Company Parameters), enter
 N,
 New,
 or +. The system will
 automatically assign the next available quote number based on the Last Used Quote
 # specified in MS Company Parameters.
Note: The system automatically updates the generated number
 to the Last Used
 Quote # field.
If you are not using the 'auto-generate quote numbers' feature, enter a number to identify this quote. Up to 10 characters allowed.
Tip: Press F4 to display a list of quote numbers based on sale type (i.e. customer, job, or inventory).

## Type

Select the type of quote that you are creating. The selection in this field determines which fields will display on this tab.

- C-Customer – Select this option if the quote will be used when selling materials to a customer.

- J-Job – Select this option if the quote will be used when selling materials to a job.

- I-Inventory – Select this option if the quote will be used when selling materials to another Inventory location.

##  Customer

 Enter the customer number or press F4 to select a
 customer from a list. Customers are created and maintained using the [
 AR Customers ](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form) form. You can open this form by pressing F5 in this
 field.
Note: The Active box is only enabled when a
 customer is selected in this field.

##  Cust Job

 Optional field for Customer quotes only. This field is accessible only after you enter a customer in the Customer field.
 If applicable, specify the customer job for this template, up to 20 characters.

##  Cust PO#

 Optional field for Customer quotes only. This field is accessible only after you enter a customer in the Customer field.
 Enter the customer’s purchase order number, up to 20 characters.

##  JC CO#

 For Job quotes only.
 Enter the Job Cost company (from HQ Company Setup) for this quote.

## Job

For
 Job quotes only.
Specify the job (from JC Jobs) for this quote.
Note: If you enter a soft- or hard-closed job, the status displays in red above the tab page. Entry is allowed, regardless of whether you have specified to allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).

##  IN CO#

 For Inventory quotes only.
 Enter the Inventory company (from HQ Company Setup) for this quote.

##  To Location

 For Inventory quotes only.
 Specify the location (from IN Locations) for
 this quote.

## Description

Enter a description of the quote. The description can be up to 30 characters long.
Depending on the type of quote, this field defaults with the customer name, job description, or location description.

## Contact

Informational only.
Enter the person to contact regarding this quote, up to 30 characters. This field initially defaults as follows:

- Customer Quote - Defaults the contact specified for the customer in AR Customers or null if no contact specified for the customer.

- Job Quote - Defaults the project manager specified
 for the job in JC Jobs or null if no project manager specified.

-  Inventory Quote - Defaults as blank.

## Phone

Informational only.
Enter the telephone number of the specified contact. Initially defaults the phone number as follows:

- Customer Quote - Defaults the phone number specified for the customer in AR Customers or null if no phone number specified for the customer.

- Job Quote - Defaults the phone number specified for
 the job in JC Jobs or null if no phone number specified for the job.

- Inventory Quote - Defaults as null.

## Price Template

Enter the price template (from MS Price Templates) to use for material price defaults. Initially defaults as follows:

- Customer Quote - Defaults the price template specified for the customer in AR Customers or null if no price template specified for the customer.

- Job Quote - Defaults the price template specified
 for the job in JC Jobs or null if no price template specified for the job.

-  Inventory Quote - Defaults the price template
 specified for the inventory location in IN Locations or null if no price template
 specified for the inventory location.

Note: The system will only use this template if no material-specific pricing or pricing overrides exist for the quote.

## Discount Template

For Customer quotes only.
Enter the discount template (from MS Payment Discount Templates) to use for calculating material-based payment discounts. Initially defaults the discount template specified for the customer in AR Customers; defaults as null if no discount template is specified for the customer.
Note: The system uses this template only if you flagged the customer’s payment terms for material-based discounts (Discount Based on Material checkbox selected in HQ Payment Terms) and discount overrides do not exist for the quote.

## Tax Code

Enter the tax code for calculating taxes on materials and haul charges when
 sales are made to the purchaser on this quote.
Note: This tax code is only used if the Tax Option in
 MS Company Parameters is set to 2-Sale Type / Purchaser or 3-Sale Type / Purchaser / Sales
 Location, and overrides the tax code specified for the purchaser in AR Customers, JC Jobs,
 or IN Locations. For example, if the Sale Type is Customer for the ticket (in
 MS Ticket Entry), the tax code specified here will override the tax code specified for the
 customer in AR Customers.

## Active

Check this box to activate this quote. Pricing, haul rates, and other defaults and overrides set up on this quote will be used during ticket entry and hauler time sheet entry. If reactivating an inactive quote, you must manually reset the status to “Ordered” for any quote detail.
Note: When creating a Customer quote, this field is only
 enabled when a customer is selected in the Customer field.
Uncheck this box if this quote is inactive. Defaults and overrides defined for this quote will not be used. If changing an active quote to this status, you must set the status for all quote detail entries to “Complete”, and relieve any remaining Inventory allocations.

## Use Metric UM

Check this box to use the Metric UM (defined in metric unit of measure when selling materials set up on this quote. When you specify any material set up on this quote on a ticket (MS Ticket Entry), the material's metric unit of measure defaults as the sales unit of measure (i.e. the unit of measure in which the material is being sold). Define a metric unit of measure for the material in IN Location Materials (Add'l U/M tab). If you do not define a metric unit of measure for the material, the system uses the sales unit of measure.

- Checking this box does not affect the unit of measure default for materials added to the quote. The default will always be the sales unit of measure for the material (which you can override, if necessary).

- If you are using any of the MS Ticket Batch imports
 (e.g. Alkon, AMI, Libra, Seltec, etc.), and you checked the Use Viewpoint Default
 Value box for UMs in your template, checking this option for a quote
 will cause the imported UM, unit price, and units values to be converted to metric.
 If you do not want this conversion to occur, uncheck this option for the quote or
 uncheck the Use Viewpoint Default Value box in the import template (IM Template
 Detail).

Uncheck this box to use the Sales UM when selling materials set up on this quote.

## Haul Tax Option

Indicate whether haul charges on this quote are taxable. The option
 specified here overrides the option specified for the “purchaser” in AR Customers, JC Jobs,
 PM Projects, or IN Locations (depending on sale type).

- 0-Not Taxable – Haul charges are not taxable.

- 1-Taxable Using Haul Vendor – Haul charges are only taxable when using an outside vendor to haul materials.

- 2-Always Taxable – Haul charges are always taxable, regardless of whether using company vehicle or outside haul vendor.

##  Quoted By

 Informational only.
 Enter the name of the person who prepared this quote, 30 characters.

##  Quote Date

 Informational only.
 Enter the date for this quote. Automatically defaults to the current date.

##  Expiration Date

 Informational only.
 Enter the date through which the pricing, overrides, and defaults on this quote are valid.

## Apply Price Escalators

This field is enabled for Job and Customer quotes only, and is only applicable if you are using the oil price escalation/de-escalation feature (i.e. have set up price indexes in HQ Escalation Index).
Check this box to apply price escalators (defined in HQ Escalation Index) to this job or customer/customer job quote. When checked, the MS Oil Price Escalation report tracks sales of applicable materials (e.g. asphalt mixes) to this job or customer/customer job in MS Ticket Entry, and determines increases/decreases in pricing based on the bid index date specified below and the price index (monthly escalation/de-escalation). Use the MS Oil Price Escalation report to review the resulting pricing adjustments.
Uncheck this box if you are not using the oil price escalation/de-escalation feature or if not applying price escalators to this job or customer/customer job quote.
[Click here for more information about the price escalation feature](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-escalation-index-form).

## Bid Index Date

This field is enabled for Customer and Job quotes only, when the Apply Price Escalators checkbox is
 selected. You will only use this field if you are using the oil price
 escalation/de-escalation feature (i.e. have set up price indexes in HQ Escalation Index).
Enter the bid index date for this job or customer/customer job quote. This is generally the first day of the job’s start month and will become the starting date for price escalation. The system will use this date in conjunction with the price index (defined in HQ Escalation Index) to determine price escalation adjustments.
Note: For job quotes, if the Apply Price Escalators checkbox is
 selected for the job (in JC Jobs), the system uses the Contract Start Month for the
 job's contract (in JC Contracts) rather than the bid index date specified on the
 quote.

## Factor

This field is enabled only when the Apply Price
 Escalators box is checked.
Enter the escalation factor (e.g. 5% as .05) for this quote. This is the amount by which pricing must increase/decrease before an adjustment will be applied. Assigning the factor at the quote level will allow designating different factors for jobs based on whether the job is a single-year or multi-year job.
Note: If set to .000000, system will use the factor specified in HQ Escalation Index (either defined by month on Monthly Index tab or the standard factor defined on the Info tab).

## Apply Surcharges

This field is enabled only for Customer and Job quotes.
Check this box to allow assessing surcharges for MS tickets referencing the purchaser associated with this quote. During ticket entry (in MS Ticket Entry), the system will automatically assess surcharges based on the surcharge group assigned to this quote. If no surcharge group is assigned to this quote, surcharges will be assessed using the default surcharge group specified in MS Company Parameters.
Note: You must check this box to assess surcharges for tickets posted to this quote's purchaser. Even if you have designated a default surcharge group in MS Company Parameters to ensure surcharges are assessed on all tickets, if a quote exists for a purchaser and this box is not checked, no surcharges will be assessed.
Additionally, if you check this box, you must ensure you have a surcharge group designated on the quote or in MS Company Parameters. If the system does not locate a surcharge group at the quote or company level, no surcharges will be assessed.
Uncheck this box if you do not want surcharges assessed when entering MS tickets for the purchaser designated on this quote.

## Surcharge Group

This field is enabled only when the Apply
 Surcharges box (above) is checked.
Enter the surcharge group to use for assessing
 surcharges when entering tickets for this quote's purchaser (in MS Ticket Entry). The
 system will assess surcharges based on the surcharge codes assigned to this surcharge
 group, the data entered for the ticket, and the override surcharge rates defined for this
 quote (Surcharge Override tab). If override criteria is not met or no override rates are
 defined for this quote, the system will use the surcharge rates defined in MS Surcharge
 Codes.
Note: If no surcharge group is specified here and no default
 group is specified in MS Company Parameters, no surcharges will be assessed, regardless of
 whether the Apply
 Surcharges box is checked.

##  Pay Terms Override

 For Customer Quotes only.
 Enter the override pay terms to use for this quote/customer, if applicable, or leave blank to use the customer's standard pay terms as defined in AR Customers. This field initially defaults blank.

## Create a Separate Invoice

For Customer quotes only.
Check this box to have separate invoices generated from tickets and hauler time sheets posted to this quote, based on the Invoice Level assigned in AR Customers. For example, if a Customer’s Invoice Level is set to summarize sales onto a single invoice, but a quote for one of that Customer’s jobs is flagged to create a separate invoice, sales to that Customer Job will be put on one invoice, and other sales to that Customer will be put on another.
Uncheck this box if you do not want separate invoices generated from tickets and hauler time sheets posted to this quote.

##  Separate Haul Info on Invoice

 For Customer quotes only.
 Only applicable if the ‘Create a Separate Invoice’ option is checked. If unchecked, the system follows the ‘Separate Haul Info on Invoice’ option in AR Customers.
 Check this box to print material amounts and haul charges (Haul Rate and Haul Amount) in separate columns on the invoice.
 Leave this box unchecked to combine haul information with material information when printing invoices for this customer. Haul charges will be included with material amounts rather than printing in separate columns on the invoice. The system calculates the unit price as Total divided by Material Units.

##  Billing Frequency

 Optional field for Customer quotes only.
 Enter the frequency code (from HQ Frequency Codes) for restricting the generation of invoices from tickets and hauler time sheets posted to this quote. When initializing invoices based on frequency code, only ticket and hauler time sheet detail that is ready for billing, and posted to a quote with the same billing frequency as the one you specified during initialization will be included on an invoice. Leave blank if ticket and hauler time sheet detail posted to this quote will always be included when invoices are initialized.

##  Misc Distribution Code

 Optional field for Customer quotes only. Use this field only when you select the “Create Miscellaneous Distributions on Invoice” checkbox in AR Customers.
 Indicate the distribution code (from AR Misc Distribution Codes) to use for distributing amounts invoiced from ticket and hauler time sheet detail posted to this quote.

## Print Level

For Customer quotes only.
Select the lowest level of detail to print on
 all MS invoices for this customer. This option is accessible only if you check the
 Create a
 Separate Invoice box. If you do not select that option, the system uses the
 print level selected in the AR Customers form. This may be overridden by invoice (MS
 Invoice Edit).

- 1-Unit Price – Summarizes and prints detail at the material, unit of measure, and unit price level as one line on the invoice.

- 2-Trans# – Prints one line on the invoice for each transaction. If you select this option, the ticket number for each transaction prints on the invoice.

## Subtotal Level

For Customer quotes only.
Enabled only when the Create a Separate
 Invoice box (above) is checked for the quote.
Note: If you did not check the Create a Separate
 Invoice box, the system uses the selected subtotal level in AR Customers.
 This may be overridden by invoice (MS Invoice Edit).
Indicate the lowest level of subtotals to print on all MS invoices for this customer.

- 1-Customer Job

- 2-Customer PO#

- 3-Sales Date

- 4-Location

- 5-Material

- 6-UM - Quantity subtotals are only available at this level.

Other setup options in AR and MS may affect the Subtotal Level. Review the following setup options before selecting an option in this field.

- MS Company Parameters (Invoices tab) — The
 Sort by
 Sales Date and Sort by Location checkboxes affect
 the availability of each subtotal level. If you check both boxes, all subtotal levels
 are available. If you do not check the Sort by Sales Date box, the date
 will not print on invoices and you cannot use the 3-Sales Date option above. If you
 do not check the Sort by Location box, the location
 will not print on invoices and you cannot use the 4-Location option above.

- AR Customers (Material Sales tab) — The Invoice
 Level drop-down field determines how sales will be grouped and printed
 on invoices for the customer. If you selected to print one invoice per customer, all
 subtotal levels are available. If you selected to print one invoice per customer/job,
 you cannot use the 1-Customer Job option above. If you selected to print one invoice
 per customer/job/PO, you cannot use the 1-Customer Job or 2-Customer PO# options
 above.

Note: In addition to printing subtotals at the selected level, the system prints subtotals for each level above the selected level. If you do not select the Create a Separate Invoice checkbox, this field is inaccessible and the system uses the subtotal level selected in AR Customers.

## Ship To: Address

For Customer quotes only.
Enter the delivery address for the materials
 on this quote, up to two lines, 60 characters each. This address prints on the invoice if
 the Invoice
 Level is set to 1-One invoice per Customer Job for the customer in AR
 Customers . Otherwise, it is informational only.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Ship To: City

For Customer quotes only.
Enter the delivery city, up to 30 characters.
 This city prints on the invoice if the Invoice Level is set to 1-One invoice per
 Customer Job for the customer in AR Customers . Otherwise, it is informational only.
If you have Internet access, you can click the
 Map button () to view the
 address using your default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Ship To: State

For Customer quotes only.
Specify the delivery state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
This state prints on the invoice if the
 Invoice
 Level is set to 1-One invoice per Customer Job for the customer in AR
 Customers . Otherwise, it is informational only.
If you have Internet access, you can click the
 Map button () to view the
 address using your default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Ship To: Zip Code

For Customer quotes only.
Specify the zip code for the delivery address.
 This zip code prints on the invoice if the Invoice Level is set to 1-One invoice per
 Customer Job for the customer in AR Customers . Otherwise, it is informational only.
If you have Internet access, you can click the
 Map button () to view the
 address using your default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Ship To: Country

Enter the 2-character delivery country. Entry in this field is required when the delivery address exists outside the Default Country specified in HQ Company Setup for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.
If you have Internet access, you can click the
 Map button () to view the
 address using your default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

##  Quote Detail: Location

 Required.
 Enter the selling location for the quoted
 material. This must be a valid location set up in IN Locations.

##  Quote Detail: Material Vendor

 Enter the vendor (AP Vendors) from which you are purchasing the material.

##  Quote Detail: Material

 Required.
 Enter the material you are quoting. Material must be set up in HQ Materials, but is not required to be active or stocked at the specified IN location.
Materials not flagged as active will not display when using the F4 lookup.

## Quote Detail: UM

Initially defaults to the sales unit of measure for the specified material.
You can override this field, but the override must be either:

-  the material’s [standard unit of measure](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form/field-definitions-hq-materials-form#ID-0000f0b8--en) (defined in HQ Materials > Info tab) or

- a valid [unit of measure that has been defined](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) for the material (in HQ Materials > Additional Units of Measure tab).

## Quote Detail: Phase

Available for Job quotes only.
Enter the phase for this material pricing. This must be a valid phase or valid part of phase (as defined in JC Company Parameters). If this is a locked job, the value must be a valid job phase (from JC Job Phases). If this field is blank, material pricing applies to all phases.
If you interfaced this material from PM (material quote), the phase defaults as follows:

- If you interfaced a single quote record for this material/location/UM, the phase defaults as blank.

- If you interfaced multiple quote records for this material, and the unit price was the same for all phases matching this location/material/UM, the system generates a single record for the material and the phase defaults as blank.

- If you interface multiple quote records for this material, and the unit price differed for any phase matching this location/material/UM, the system creates separate records for each phase occurrence, and the phase defaults from PM Material Detail.

##  Quote Detail: Quote Units

 Enter the total quantity needed of this material, or enter a maximum amount.

## Quote Detail: Unit Price

Enter the unit price for this material.
This field populates with a default value based on the following:

- If a price template is specified for the quote and the material's category, location, and UM matches the location, category, and UM specified on the price template, defaults the unit price from the price template.

- If no match is found on the price template or no price template is specified on the quote, defaults the unit price from the location/material setup in IN Location Materials.

- If the location/material is not set up in IN Location Materials, defaults the unit price from HQ Materials.

## Quote Detail: ECM

Indicate what quantity the unit price represents.

- E-Each

- C-Per Hundred

- M-Per Thousand

##  Quote Detail: Date Req'd

 Enter the required date for the quoted material. This field is informational only.

## Quote Detail: Status

Select the status of this quoted material.

- 0-Bid – The system does not allocate inventory and you cannot edit ‘ordered’ units.

- 1-Ordered – The system is using the quote for
 current sales and allocating inventory. Changes to ‘ordered’ and ‘sold’ units will
 update the Allocated Units in IN Location Materials. This status is only valid
 for active quotes.

- 2-Completed – All sales are complete and the system has relieved remaining Inventory allocations. You can no longer edit ‘ordered’ units.

Note: The system updates the Sold Units regardless of the material's quoted status.

## Quote Detail: Ordered Units

This field displays the current number of units ordered on this quote.
If the quoted material’s status is 0-Bid, this field is set to 0.00 and cannot be edited.
If the quoted material’s status is 1-Ordered, this field defaults the quoted units. You can edit this amount to be more or less than the quoted units.

##  Quote Detail: Sold Units

 Indicates the current number of units sold to date. This field updates automatically each time you enter a ticket (MS Ticket Entry) for the quoted material, regardless of the material’s quoted status (i.e. bid, ordered, or completed); however, the system only updates inventory allocations if the status is 'Ordered'.

##  Quote Detail: Unit Cost

 The field is enabled when a material vendor is specified for the quote detail line.
 Enter the vendor’s unit cost for the material.

## Quote Detail: Notes

Use this tab to enter any miscellaneous notes about this item. The space allowance is virtually unlimited.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

##  Price Overrides: Location

 Optional field.
 Specify the location for this pricing. This
 must be a valid location (from IN Locations) for the specified location group. If this
 field is blank, pricing applies to all locations within the specified location group.

##  Price Overrides: Location Group

 Required field.
 Specify the location group (from IN Location Groups) for this pricing.

##  Price Overrides: Category

 Required field.
 Specify the category (from HQ Material Categories) for this pricing.

##  Price Overrides: UM

 Required field.
 Specify the sales unit of measure for this material or category of materials. This must be a valid unit of measure set up in HQ Units of Measure.

## Price Overrides: Phase

 Available for Job quotes only.
 Specify the phase for this pricing override. This must be a valid phase or valid part of phase (as defined in JC Company Parameters).

- If this is a locked job, the job phase must be valid
 (from JC Job Phases). Press F4 to select from a list of valid
 job phases.

- If this field is blank, override haul rate apply to all phases.

##  Price Overrides: Markup/Disc Rate

 Use this field when the Unit Price field is 0.00.
 Enter the rate to calculate a default unit price. The system applies this rate to the standard cost or price found in IN Location Materials (stocked materials) or HQ Materials (non-stocked materials) based on the selected pricing option in IN Company Parameters.

##  Price Overrides: Unit Price

 Enter the unit price to use as a default for this material or category of materials when entering tickets. This may be a positive or negative value.
 If this field is set to 0.00, the system uses the value in the Markup/Disc Rate field.

## Price Overrides: ECM

Specify what quantity the unit price (previous field) represents.

- E-Each

- C-Per Hundred

- M-Per Thousand

##  Price Overrides: Minimum Amt

 Specify the minimum amount to charge per ticket for this material or category of materials. The system uses this amount if the calculated total for the material is less than this amount and the material units are greater than 0.00.

##  Discount Overrides: Loc Grp

 Required field.
 For Customer quotes only, where you flagged the customer’s payment terms for material-based discounts (Discount Based on Material checkbox in HQ Payment Terms).
 Specify the location group (from IN Location Groups) for this discount.

##  Discount Overrides: Location

 Optional field.
 For Customer quotes only, where you flagged the customer’s payment terms for material-based discounts (Discount Based on Material checkbox in HQ Payment Terms).
 Specify the location for this discount. It
 must be a valid location (from IN Locations) for the specified location group. If this
 field is blank, the discount applies to all locations within the specified location group.

##  Discount Overrides: Category

 Required field.
 For Customer quotes only, where you flagged the customer’s payment terms for material-based discounts (Discount Based on Material checkbox in HQ Payment Terms).
 Specify the category (from HQ Material Categories) for this discount.

## Discount Overrides: Material

Optional field.
For Customer quotes only, where you flagged the customer’s payment terms for material-based discounts (Discount Based on Material checkbox in HQ Payment Terms).
Enter the material for this discount. This must be a valid material (from HQ Materials) assigned to the specified category. If this field is blank, the discount applies to all materials in the specified category.
Note: Entry here overrides discounts entered at the category level.

##  Discount Overrides: UM

 Required field.
 For Customer quotes only, where you flagged the customer’s payment terms for material-based discounts (Discount Based on Material checkbox in HQ Payment Terms).
 Specify the sales unit of measure for this material or category of materials. This must be a valid unit of measure set up in HQ Units of Measure.
 If you entered a material for this line, this field defaults the sales unit of measure for the material (from HQ Materials). You may override this field, but it must be either the standard unit of measure for the material or a unit of measure specified for the material in HQ Materials.

## Discount Overrides: Pay Disc Rate

For Customer quotes only, where you flagged
 the customer’s payment terms for material-based discounts (Discount Based on
 Material checkbox in HQ Payment Terms).
Enter the number to be used to calculate the discount for this material or material category:

- This number will be the discount rate if the posted
 material’s Payment Discount Type field (in HQ
 Materials) is set to R-Discount Rate per dollar.

- This number will be the amount per unit used to
 calculate the discount amount if the posted material’s Payment Discount
 Type field (in HQ Materials) is set to U-Discount Amt per
 unit.

Note: Enter all amounts as decimals (for example, ".10"). If a discount rate, the system interprets this value as 10%. If a discount rate per unit, the system interprets this value as $.10 per unit.

##  Haul Code Defaults: Location Group

 Required field.
 Enter the location group for this haul code default. Tickets and hauler timesheets referencing this location group, and all other criteria defined for this information set, default the haul code specified in the Haul Code field.

##  Haul Code Defaults: Location

 Specify the location (from IN Locations) for this haul code default. This
 must be a valid location (from IN Locations) for the specified location group. Tickets
 and/or hauler timesheets referencing this location, and all other criteria defined for this
 information set, will default the haul code specified in the Haul Code field.

##  Haul Code Defaults: Category

 Specify the category (from HQ Material Categories) for this haul code default. Tickets and hauler timesheets referencing this category, and all other criteria defined for this information set, will default the haul code specified in the Haul Code field. Entry in this field is required if you are entering a material.

##  Haul Code Defaults: Material

 Specify the material for this haul code default. Tickets and hauler timesheets referencing this material, and all other criteria defined for this information set, will default the haul code specified in the Haul Code field.

##  Haul Code Defaults: Truck Type

 Required field.
 Specify the truck type (from MS Truck Types) for this haul code default. Tickets and hauler timesheets referencing this truck type, and all other criteria defined for this information set, will default the haul code specified in the Haul Code field.

##  Haul Code Defaults: UM

 Required field.
 Specify the sales unit of measure for this haul code default. This must be a valid unit of measure set up in HQ Units of Measure. Tickets and hauler timesheets referencing this UM, and all other criteria defined for this information set, will default the haul code specified in the Haul Code field.

##  Haul Code Defaults: Haul Code

 Required field.
 Specify the default haul code (from MS Haul Codes) for entering tickets and hauler timesheets posted with equipment or a haul vendor that meets all criteria defined for this information set.

##  Haul Zones: Location

 Specify the location (from IN Locations) for this haul zone. This should be
 the selling location for the materials on this quote.

##  Haul Zones: Haul Zone

 Specify the default haul zone for delivering materials from the specified location to the “purchaser” indicated on this quote.

##  Pay Codes: Location Group

 Required field.
 Specify the location group (from IN Location Groups) for this pay rate.

##  Pay Codes: Location

 Optional field.
 Specify the location for this pay rate. This
 must be a valid location (from IN Locations) for the specified location group. If this
 field is blank, pay rate applies to all locations within the specified location group.

##  Pay Codes: Category

 Specify the category (from HQ Material Categories) for this pay rate. Entry is required if you are entering a material. If this field is blank, pay rate applies to all categories and materials.

##  Pay Codes: Truck Type

 Optional field.
 Specify the truck type (from MS Truck Types) for this pay rate. If this field is blank, the pay rate applies to all truck types.

##  Pay Codes: Vendor

 Optional field.
 Specify the vendor (from AP Vendors) for this
 pay rate. If this field is blank, the pay rate applies to all vendors.

##  Pay Codes: Truck

 Optional field. This field is only available when you enter a vendor in the Vendor field.
 Enter the truck (MS Vendor Trucks) for this pay rate. If this field is blank, and you do not specify a vendor, the pay rate applies to all trucks. If this field is blank, and you specify a vendor, the rate applies to all trucks for the vendor.

##  Pay Codes: UM

 Required field.
 Specify the sales unit of measure for this pay rate. This must be a valid unit of measure set up in HQ Units of Measure.
 If you enter a material for this line, this field defaults the sales unit of measure for the material (from HQ Materials). You can override this field, but it must be either the standard unit of measure for the material or a unit of measure specified for the material in HQ Materials.

##  Pay Codes: Pay Code

 Required field.
 Specify the pay code (from MS Pay Codes) to use as a default when entering tickets and hauler time sheets, and to which the override pay rate applies.

## Pay Codes: Override

Check this box to override the standard pay rate for this haul code. The system uses override rate entered in the Pay Rate field to calculate payments for the specified haul vendor when entering tickets and hauler time sheets.
Uncheck this box to use the standard pay rate specified for this pay code (MS Pay Codes) to calculate payments for the haul vendor when entering tickets and hauler time sheets.

##  Pay Codes: Pay Rate

 This field is accessible when you select the Override checkbox.
 Specify the override rate for this pay code. The system uses this rate to calculate payments to the specified haul vendor when entering tickets and hauler time sheets.

##  Pay Codes: Pay Min Amt

 Required field.
 Specify the minimum payment amount for tickets, hauler time sheets, haul ticket add-ons, and haul payment worksheets posted to this pay code, or enter 0.00 if no minimum payment applies. The system defaults this amount when the pay basis is greater than 0.00 and the calculated payment amount is less than the amount specified here.

##  Job Phases: Location Group

 Required field.
 Specify the location (from IN Locations) for
 the phase and cost type defaults.

## Job Phases: Location

Optional field.
Specify the location for the phase and cost
 type defaults.  This must be a valid location (from IN Locations) for the specified
 location group.  If this field is blank, phase and cost type defaults apply to all
 locations within the specified location group.

##  Job Phases: Category

 Required field.
 Specify the category (from HQ Material Categories) for the phase and cost type defaults.

##  Job Phases: Material

 Optional field.
 Specify the material (from HQ Materials) for the phase and cost type. If this field is blank, the phase and cost type are applicable to all materials within the specified category.

##  Job Phases: Matl Phase

 Required field.
 Specify the phase (from JC Phases or JC Job
 Phases) for the material expenses associated with sales to the job on this quote.

##  Job Phases: Material CT

 Specify the cost type (JC Cost Types) to use for the material expenses associated with sales to the job on this quote.

##  Job Phases: Haul Phase

 Required field.
 Specify the phase (from JC Phases or JC Job
 Phases) to use for haul charges associated with sales to the job on this quote.

##  Job Phases: Haul CT

 Specify the cost type (from JC Cost Types) to use for haul charges associated with sales to the job on this quote.

##  Haul Code Overrides: Location Group

 Required field.
 Specify the location group (from IN Location Groups) for this override haul rate.

##  Haul Code Overrides: Location

 Optional field.
 Specify the location for this haul rate. This
 must be a valid location (from IN Locations) for the specified location group.If this field
 is blank, the override haul rate applies to all locations within the specified location
 group.

##  Haul Code Overrides: Category

 Specify the category (from HQ Material Categories) for this haul rate. Entry in this field is required if you are entering a material in the Material field. If this field is blank, override haul rate applies to all material categories.

## Haul Code Overrides: Material

Optional field.
Enter the material for this haul rate. This must be a valid material (from HQ Materials) assigned to the specified category. If this field is blank, the override haul rate applies to all materials in the specified category.
Note: Entry here overrides haul rates entered at the category level.

##  Haul Code Overrides: Truck Type

 Specify the truck type (from MS Truck Types) for this override haul rate. If left blank, the haul rate applies to all truck types.

##  Haul Code Overrides: UM

 Required field.
 Specify the sales unit of measure (from HQ Units of Measure) for this haul rate. If you enter a material for this line, this field defaults the sales unit of measure for the material (from HQ Materials). You can override this field, but it must be either the standard unit of measure for the material or a unit of measure specified for the material in HQ Materials.

##  Haul Code Overrides: Haul Code

 Required field.
 Specify the haul code (from MS Haul Codes) for this override haul rate. Tickets and hauler timesheets referencing this haul code, and other criteria defined for this information set, will use the override haul rate specified in the Haul Rate field.

## Haul Code Overrides: Phase

Available for Job quotes only.
Specify the phase for this override haul rate. This must be a valid phase or valid part of phase (as defined in JC Company Parameters). If this is a locked job, use a valid job phase (from JC Job Phases). If this field is blank, override haul rate apply to all phases.

##  Haul Code Overrides: Haul Rate

 Required field.
 Enter the override haul rate for the specified haul code. The rate must be equal to or greater than 0.00. Ticket and hauler timesheets referencing the haul code and other criteria defined for this information set will use this haul rate.

##  Haul Code Overrides: Min Amt

 Required field.
 Specify the minimum haul charge for tickets and hauler time sheets posted to this haul code or enter 0.00 if no minimum haul charge. The system uses this amount as a default if the haul units are greater than 0.00 and the calculated haul charge is less than the amount specified here.

## Surcharge Overrides: Sequence

Enter a sequence number for this rate override
 or enter N, New, or + to have
 the system automatically assign the next sequential number.

## Surcharge Overrides: Loc Grp

Enter the location group (from IN Location Groups) for this override surcharge rate.
The rate specified for this override sequence will apply to only those tickets referencing locations within this location group and meeting all other override criteria.

## Surcharge Overrides: Location

Enter the location (from IN Locations) for
 this override surcharge rate.
The rate specified for this override sequence will apply to only those tickets referencing this location and meeting all other override criteria.

## Surcharge Overrides: Category

Enter the category (from HQ Material Categories) for this override surcharge rate.
The rate specified for this override sequence will apply to only those tickets referencing materials within this category and meeting all other override criteria.

## Surcharge Overrides: Material

Enter the material (from HQ Materials) for this override surcharge rate.
The rate specified for this override sequence will apply to only those tickets referencing this material and meeting all other override criteria.

## Surcharge Overrides: Truck Type

Enter the truck type (from MS Truck Types) for this override surcharge rate.
The rate specified for this override sequence will apply to only those tickets referencing this truck type and meeting all other override criteria.

## Surcharge Overrides: UM

Enter the unit of measure (from HQ Units of Measure) for this override surcharge rate.
The rate specified for this override sequence will apply to only those tickets referencing this unit of measure and meeting all other override criteria.

## Surcharge Overrides: Pay Code

Enter the pay code (from MS Pay Codes) for this override surcharge rate.
The rate specified for this override sequence will apply to only those tickets referencing this pay code and meeting all other override criteria.

## Surcharge Overrides: Surcharge Code

Enter the surcharge code (from MS Surcharge Codes) for this override surcharge rate.
The rate specified for this override sequence will apply to only those tickets referencing this surcharge code and meeting all other override criteria.

## Surcharge Overrides: Surcharge Rate

Enter the override rate for the specified surcharge code. The system will use this rate to assess surcharges for tickets meeting all criteria for this override rate sequence.
Note: If you enter a negative rate in this field, you must
 set the Surcharge
 MinAmt to 0.00.

## Surcharge Overrides: Surcharge Min Amt

Enter the minimum surcharge to assess for tickets referencing this surcharge code and meeting all criteria specified for this override sequence, or enter 0.00 if no minimum surcharge amount applies. The system will apply this amount if the calculated surcharge amount is less than the amount specified here.
Note: If you entered a negative Surcharge Rate
 for this sequence, you must set this amount to 0.00.

## Pay Codes: Material

Optional field. This field is only available when you enter a category in the Category field.
Enter the material for this pay rate. This must be a valid material (from HQ Materials) assigned to the specified category. If this field is blank, the pay rate applies to all materials in the specified category.
Note: Entry here overrides pay rates entered at the category level.
