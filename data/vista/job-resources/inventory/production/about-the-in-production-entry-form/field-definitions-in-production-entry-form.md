---
title: "Field Definitions: IN Production Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/production/about-the-in-production-entry-form/field-definitions-in-production-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/production/about-the-in-production-entry-form/field-definitions-in-production-entry-form"
---

# Field Definitions: IN Production Entry Form

The following is a list of field descriptions for the IN
 Production Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq#

 Enter NEW to create a new entry or enter the batch sequence number of an existing entry you wish to display.

##  Date

 Enter the production date for the finished good. Initially defaults to the current date.

##  Location

 Enter the finished good’s production location (from IN Locations).

##  Material

 Enter the material (finished good) being produced. This must be an active material stocked at the production location (IN Location Materials) and must be a finished good set up with a Bill of Materials.

##  Amounts: Units

 Enter the number of units produced (expressed in the finished good’s unit of measure). This may be a positive or negative amount, but cannot be 0.00.
Note: Negative amounts will typically be used when making adjusting entries (e.g. backing out a production entry made in error).

##  Amounts: Unit Cost

 Defaults a unit cost based on the Cost Method for the location (IN
 Locations) or category (IN Location Category Override).
 The Unit Cost may be overridden only if the
 Allow Unit Cost
 Overrides checkbox is selected in IN Company Parameters. Override values
 must be equal to or greater than 0.00. The amount entered here will be used to update the
 Inventory value of the finished good.
Note: If Cost Method is Std Unit Cost, and the amount
 entered here is not equal to the Std Unit Cost, the difference will be posted to the
 appropriate Cost Variance account (defined in IN Locations or IN Location Category
 Override).

##  ECM

 Indicates what quantity the unit cost represents. This can only be overridden if the Allow Unit Cost Overrides option is checked (IN Company Parameters).

- E – Per Each

- C – Per Hundred

- M – Per Thousand

##  Memo

 Use this field to enter a description of the production transaction, up to 30 characters.

##  Comp Location

 This is the Location from which the component material is pulled. For
 initialized components, default will be either the production location (if using a standard
 Bill of Materials) or the location specified for the component material if an override Bill
 of Materials is used. This value cannot be overridden.
 If adding a new component, enter the
 component’s source location. This must be an active location (IN Locations), but does not
 need to be the same as the production location, nor does it need to be within the same
 location group as the production location.

##  Material

 Component material required for the production of the finished good. For initialized components, defaults from the Bill of Materials.
 If adding a new component, enter a valid material stocked at the source location specified in previous field. Cannot be the same as the finished good, and must be unique within this batch entry.
 Material’s description and standard unit of measure are displayed to the right of this field.

##  UM

 This field displays the unit of measure for the component material (set in [HQ Materials](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form)). This value cannot be overridden.

##  Units

 The number of units of this component material needed to produce the specified quantity of the finished good.
 For initialized components, defaults an amount based on the units specified in the Bill of Materials times the quantity being produced. If add a new component, the quantity entered must be greater than 0.00.
Note: If the quantity entered here causes the component’s on-hand quantity to fall below zero, and the 'Display Warning if Qty On Hand is Negative' option is checked (IN Company Parameters), a warning message will be displayed indicating that the transaction will result in a negative “on hand” quantity. Posting will still be allowed.

##  Unit Cost

 Defaults a unit cost based on the Cost Method for the location (IN
 Locations) or category (IN Location Category Override).
 The Unit Cost may only be overridden if the Allow Unit Cost Overrides option is checked (IN Company Parameters). Override value must be equal to or greater than 0.00.

##  ECM

 Indicates what quantity the unit cost represents. This can only be overridden if the Allow Unit Cost Overrides option is checked (IN Company Parameters).

- E – Per Each

- C – Per Hundred

- M – Per Thousand

##  Unit Price

 Used only when the component’s source location differs from the production
 location and the Usage Option (IN Company Parameters) is ‘Sale’.
 Enter the unit price for this component material. Must be equal to or greater than 0.00. Initially defaults a unit price based on the MS pricing hierarchy as follows:

- Quote – If an active quote exists for the production IN location that includes component materials from another location, the system uses the quote to determine pricing. If no pricing exists on the quote for the materials, it will use the quote's price template.

- Pricing Templates – If an override price template is
 specified on the quote, it will use that price template first. If no price template
 is specified on the quote, the price template assigned to the production location (in
 IN Locations), will be used.

- IN Location Materials (INMT) – If no pricing is found on a quote or price template, the system uses the cost/price defined for the production location (based on the Pricing Option for inventory sales defined in IN Company Parameters), and applies any markup or discount rate defined for the materials in IN Location Materials).

 This amount will be used to calculate the revenue generated from the ‘sale’ of this component to the production location. Defaults based on the Pricing Option for Inventory Sales (IN Company Parameters) and the markup/discount rate specified for the location in IN Location Materials.

##  Price ECM

 Indicates what quantity the unit price represents.

- E – Per Each

- C – Per Hundred

- M – Per Thousand
