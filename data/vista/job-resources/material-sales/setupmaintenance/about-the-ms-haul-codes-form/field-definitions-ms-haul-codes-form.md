---
title: "Field Definitions: MS Haul Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-haul-codes-form/field-definitions-ms-haul-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-haul-codes-form/field-definitions-ms-haul-codes-form"
---

# Field Definitions: MS Haul Codes Form

The following is a list of field descriptions for the MS Haul
 Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Haul Code

 Enter a haul code, up to 10 characters.

##  Description

 Enter a description of this haul code, up to 30 characters.

## Haul Rate is Based On

Indicate how haul charges will be calculated for this pay code.

- 1-Per Unit

- 2-Per Hour

- 3-Per Load

- 4-Units Per Mile

- 5-Units Per Hour

## UM

Indicate the unit of measure (from HQ Units of Measure) that the system uses when updating haul units to JC.
If pay basis = 1 (per unit), this field is disabled, and the unit of measure specified for the material when ticket is entered will be used.
If pay basis = 2 (per hour), this field is disabled, and haul units will be updated to Job Cost as hours (if the posted cost type tracks hours).
If pay basis = 3 (per load), 4 (units per mile), or 5 (units per hour), enter a valid unit of measure.  Haul units will be posted to Job Cost using this UM.

## Subject to Sales Tax

Check this box if haul charges posted using
 this haul code are subject to sales tax. When entering haul charges on a ticket (in MS
 Ticket Entry) or hauler timesheet (in MS Hauler Time Sheet Entry), the system will
 calculate haul charges based on the Tax Option, Sale Type, Haul Tax Option, and Hauler Type
 settings. Leave this box unchecked if haul charges posted to this haul code are never
 subject to sales tax.
 If you never tax haul charges, make sure to
 leave this box unchecked for every haul code you set up. However, if some or all haul
 charges are subject to taxes, check this box for each applicable haul code. When checked,
 the system calculates haul charge taxes based on the following:

- Tax Option — This option is located in
 MS Company Parameters and identifies where the tax code defaults from (e.g., sales
 location, sale type/purchaser, or delivery).

- Sale Type — The sale type is assigned in
 MS Ticket Entry or MS Hauler Time Sheets and identifies the purchaser (e.g. customer,
 job, or inventory). If the Tax Option is set to Sales Type/Purchaser, the sale type
 also determines which haul tax option to use (e.g., if a Customer sale, the system
 will use the haul tax option selected in AR Customers).

Note: If a quote exists for the purchaser, the haul tax
 option selected on the quote overrides the haul tax option specified for the purchaser.

- Haul Tax Option — This option is
 located in AR Customers, JC Jobs/PM Projects, IN Locations, and MS Quotes. It is
 used to identify whether haul charges are taxable, and if so, whether they are
 always taxable or only taxable if using a haul vendor.

- Hauler Type — The hauler type
 (Equipment or Haul Vendor) is specified on the ticket or hauler time sheet and is
 used in conjunction with the haul tax option to determine whether to apply taxes
 to haul charges. If the hauler type is Equipment, taxes will only be applied to
 haul charges if the haul tax option is 2-Always Taxable. If the hauler type is
 Haul Vendor, taxes will be applied to haul charges when the haul tax option is
 1-Taxable using Haul Vendor or 2-Always Taxable.

Note: If you are entering haul charges during ticket entry
 and the material specified on the ticket is taxable, the tax basis will be the sum of the
 material total and the haul charge total; the system does not break these amounts out. If
 the material is not taxable, the tax basis will be the haul charge total.
Click [here](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-haul-codes-form/field-definitions-ms-haul-codes-form#ID-0005abde--en) to see the field definition for Australian and Canadian users.

## Subject to VAT

Check this box if haul charges posted using this haul code are subject to
 Value Added Tax (VAT). When entering haul charges on a ticket (in MS Ticket Entry) or
 hauler timesheet (in MS Hauler Time Sheet Entry), the system will calculate haul charges
 based on the Tax Option, Sale Type, Haul Tax Option, and Hauler Type settings. Leave this
 box unchecked if haul charges posted to this haul code are never subject to VAT.
If you never tax haul charges, you can leave
 this box unchecked for each haul code you set up. However, if some or all haul charges are
 subject to taxes, you can check this box for each applicable haul code. When entering haul
 charges on tickets or hauler time sheets, if you specify a taxable haul code, the system
 will calculate haul charge taxes based on how you have set the following options.

- Tax Option — This option is located in MS Company Parameters and
 determines from where the system will default tax codes when entering haul charges. For
 example, if the Tax Option is Sales Location, the system will default the tax code
 assigned to the sales location (From Loc) specified in MS Ticket Entry or MS Hauler Time
 Sheet Entry.

- Sale Type — The sale type is assigned in MS Ticket Entry or MS
 Hauler Time Sheets and identifies the purchaser (e.g. customer, job, or inventory). If
 the Tax Option is set to Sales Type/Purchaser, the sale type also determines which haul
 tax option to use (e.g., if a Customer sale, the system will use the haul tax option
 selected in AR Customers).

Note: If a quote exists for the purchaser, the haul tax
 option selected on the quote overrides the haul tax option specified for the purchaser.

- Haul Tax Option — This option is located in AR Customers, JC
 Jobs, IN Locations, and MS Quotes. It is used to identify whether haul charges are
 taxable, and if so, whether they are always taxable or only taxable if using a haul
 vendor.

- Hauler Type — The hauler type (Equipment or Haul Vendor) is
 specified on the ticket or hauler time sheet and is used in conjunction with the haul
 tax option to determine whether to apply taxes to haul charges. If the hauler type is
 Equipment, taxes will only be applied to haul charges if the haul tax option is
 2-Always Taxable. If the hauler type is Haul Vendor, taxes will be applied to haul
 charges when the haul tax option is 1-Taxable using Haul Vendor or 2-Always
 Taxable.

Note: If you are entering haul charges during ticket entry
 and the material specified on the ticket is taxable, the tax basis will be the sum of the
 material total and the haul charge total; the system does not break these amounts out. If
 the material is not taxable, the tax basis will be the haul charge total.

## Use EM Revenue/Hauler Pay Amounts

Check this box if this haul code’s basis, rate, and total on a ticket or hauler time sheet will default from the values entered with either the EM revenue code (Equipment haul type) or the vendor’s pay code (Haul Vendor haul type).  If checked, no haul rates will be set up here, nor can override rates be entered in MS Quotes.
Uncheck this box if this haul code’s basis, rate, and total on a ticket or hauler time sheet will default from values set up here or on a quote.
In order for this feature to work, set the
 haul code basis to be equal to the revenue or pay code basis. If the haul code is unit
 based, the revenue code (or pay code) must also be unit based, and its unit of measure must
 match the material unit of measure entered for the ticket. Likewise, if the haul code is
 hourly based, the revenue code (or pay code) must also be hourly based.
When you enter tickets and hauler time sheets,
 the form verifies that the basis of the haul code is consistent with the posted revenue
 code or pay code. If the Hauler Type is “Equipment”, haul information will be based on
 values for the revenue code. If the Hauler Type is “Haul Vendor”, then the system bases
 haul information on values entered for the pay code. If the validation is successful, the
 values entered for the revenue code or pay code will default into the related haul charge
 fields.

##  Location Group

 Required.
 Specify the location group (from IN Location Groups) to which this haul rate applies.

## Location

Optional.
Specify the location to which this haul rate
 applies. Must be a valid location (from IN Locations) for the specified location
 group.  If left blank, haul rate applies to all locations within the specified
 location group.

##  Category

 Optional.
 Specify the category (from HQ Material Categories) to which this haul rate applies. If left blank, haul rate applies to all categories and materials, and no material can be entered in the next field.

## Material

Optional, but can only be entered if a category is specified in previous field.
Enter the material to which this haul rate applies. Must be a valid material (from HQ Materials) assigned to the specified category. If left blank, haul rate applies to all materials in the specified category.
Note: Entry here overrides haul rates entered at the category level.

##  Truck Type

 Optional.
 Specify the truck type (from MS Truck Types) to which this haul rate applies. If left blank, haul rate applies to all truck types.

##  UM

 Required for haul codes with basis of “Unit”, “Units per Mile”, and “Units per Hour”.
 Specify the sales unit of measure to which this haul rate applies. Must be a valid unit of measure set up in HQ Units of Measure (HQUM).
 If a material was entered for this line, this field defaults the sales unit of measure for the material (from HQ Materials). May be overridden, but must be either the standard unit of measure for the material or a unit of measure specified for the material in HQMU (HQ Material Units of Measure).

##  Zone

 Optional.
 Specify the delivery zone to which this haul rate applies, up to 10 characters. (Not validated.) If left blank, haul rate applies to all haul zones.

##  Haul Rate

 Specify the rate that will be used as the default when calculating haul charges posted to this haul code.

##  Min Amt

 Specify the minimum haul charge. This amount will be used as a default if the haul units are greater than 0.00 and the calculated haul charge is less than the amount specified here.
