---
title: "Field Definitions: IN Location Materials Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form/field-definitions-in-location-materials-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form/field-definitions-in-location-materials-form"
---

# Field Definitions: IN Location Materials Form

The following is a list of field descriptions for the IN
 Location Materials form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Location

 Enter the location (from IN Locations) to which this material is to be
 assigned.

##  Material

 Enter a valid HQ material. The “Stocked in Inventory” checkbox in HQ Materials must be selected for the material. The material’s description, assigned unit of measure, and material category will display to the right of this field.

##  Last Vendor

 Enter the last vendor from which this material was purchased for this location. This field is automatically updated by the system each time this material is purchased for this location through PO Receipts or AP invoices.

## Last Unit Cost

 Enter the last unit cost per standard unit of measure for this material.
 After the initial setup, the system will update this field each time the following
 occurs:

- The material is received for this location in PO Receipts using original unit cost

- The material is purchased for this location in AP invoices using actual unit cost plus miscellaneous amount and tax if burdened.

- If you purchase this material in a unit of measure other than the standard unit of measure, the Last Unit Cost is updated for both the purchase UM (on Addl UMs tab) and the standard UM (here).

- If using the 'Last Cost plus Markup' pricing option (IN Company Parameters), this is the unit cost used to calculate the unit price.

- If using the 'Last Cost' cost method (IN Location
 Category Override, IN Locations, or IN Company Parameters, respectively), this is the
 unit cost used to value inventory for GL updates.

##  ECM

 Select the quantity this unit cost or unit price represents.

- E – Per Each

- C – Per Hundred

- M – Per Thousand

##  Last Cost Update

 Enter the last date this material was purchased for this location. After the initial setup, this field will be updated automatically by the system each time this material is purchased for this location through PO Receipts or AP invoices. However, the update will only occur if the purchase date is equal to or greater than this field’s current date.

##  Low Stock

 Enter the low stock quantity for this material. This is the quantity at which additional stock should be reordered.
 Low stock quantities are only used for reporting purposes; purchase orders will not be generated automatically when a material reaches (or falls below) this level.

##  Reorder Qty

 Indicate what quantity of this material should be reordered whenever the material’s “Low Stock” level is reached. Quantities must be reordered manually, as a purchase order will not be generated automatically when a material falls below its low stock level.

##  Weight Conversion

 Enter the number of pounds it takes to equal one unit of this material’s unit of measure. This value will be the conversion factor used when setting up Bills of Materials by weight percentages. For example, if the material’s standard unit of measure is TON, this value should be 2000.
 This conversion factor overrides the standard weight conversion specified for this material in HQ Materials.

##  Physical Location

 Enter the actual location, such as the bin number, shelf, or aisle, of this material.This location is used for sorting and/or posting physical counts in IN Physical Count Worksheet.

##  Last Count Date

 Enter the date this material was last counted.Once set up, the system automatically updates this field with the Count Date specified when running IN Physical Count Worksheet.

## JC Costing Phase

If using the Plant Costing Links feature (IN Locations), specify the JC
 phase for this material/location that will be used to track operational costs for a plant.
 Must be a valid phase for the JC Co/Job specified for this location in IN Locations. For
 more information about the Plant Costing Links feature, see Related Topics below.

Related information

- [Plant Costing Links](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/plant-costing-links)

- [About the IN Location Materials Form](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form)

##  Active

 Check this box if this material is currently active at this location. If checked, this material can be purchased, transferred, used, produced, or sold from this location.
 Do not check this box if this material is not currently active at this location.

##  Auto Production

 Used by Material Sales only.
 Check this box if this material is produced as it is sold. Only applicable to materials set up with a Bill of Materials. If checked, the Bill of Materials is used to produce enough of this material to match the quantity sold, and the appropriate quantities of the raw materials needed to produce the material will be relieved from on-hand inventory.
 Do not check this box if this material is sold as a finished good. If this material is produced from a Bill of Materials, that production step must be made independently of the sale (using IN Production Posting).

##  Update Units Produced to GL

 Check this box if units of this material that are produced at this location will be updated to GL. When a batch is posted, units are updated to the corresponding GL accounts as defined in the Location Master. If override GL accounts exists (by Company and/or Category), they are updated instead.
Note: Since units updated to GL will always be made in the material’s standard unit of measure, make sure only matching units of measure are accumulated within a single GL Account.
 If unchecked, units of this material that are produced at this location will not be updated to GL.

##  Update Units Sold to GL

 Check this box if units of this material that are sold from this location will be updated to GL. When a batch is posted, units are updated to the corresponding GL accounts as defined in the Location Master. If override GL accounts exists (by Company and/or Category), they are updated instead.
Note: Since units updated to GL will always be made in the material’s standard unit of measure, make sure only matching units of measure are accumulated within a single GL Account.
 If unchecked, units of this material that are sold from this location will not be updated to GL.

## Display warning if Qty On Hand is negative in MS Ticket Entry

Check this box to display a warning when
 specifying this material on an ticket (in MS Ticket Entry) and posting the transaction will
 result in a negative 'on hand' quantity for this inventory location. Entry will still be
 allowed.
Note: This checkbox initially defaults the setting defined
 for the Display
 warning if Qty On Hand is negative checkbox in IN Company Parameters.
 Changing the default here will affect only this material for this location.
Uncheck this box if you do not want the
 “negative quantity” warning message displayed when specifying this material on a ticket in
 MS Ticket Entry.

## Update Average Cost of Material with Sum of Component Costs

Intended for use with finished materials only.
Select this checkbox to update this
 material's average unit cost with the sum of the component costs when entering production
 activity for this material in IN Production Entry or when auto-producing the material in MS
 Ticket Entry (i.e. Auto Production checkbox is selected in IN Location Materials).
The system will only update the average unit
 cost if the location for this material has a Cost Method of 1-Average Cost.
Do not select this checkbox if you do not want the system to update the average unit cost with component costs when producing this material.

## Average Unit Cost

 Enter the average unit cost for this material. If the [ Burdened Unit Cost - Include AP Misc Amt and Tax ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form#ID-00013743--en) box on
 the Info tab of the IN Company Parameters form is checked , this unit cost will include tax
 and freight posted in AP Transaction Entry.
 If using the ‘Average Cost’ cost method (IN
 Location Category Override, IN Locations, or IN Company Parameters, respectively), this is
 the cost used to value inventory for GL updates.
Note: This field is automatically updated each time new materials are added to inventory using the following formula:
 ((Old qty x avg unit cost) + (new qty x unit cost)) ¸ (old qty + new qty)
For example if a material has a total quantity on hand of 100 and an average unit cost of $35.00 each, and you purchase 200 units at $37.00 each, the new unit cost is calculated in the following way:
(100 x $35.00) + (200 x $37.00) = 10,9000
10,900 (100 + 200) = $36.33
New average unit cost = $36.33
 If the old quantity in stock is zero or negative, the average unit cost is set equal to the unit cost of the purchase.

##  Std Unit Cost

 Enter the current standard unit cost for this material/location.
 If using the ‘Standard Cost Plus Markup’ pricing option (IN Company Parameters), this is the unit cost used to calculate the unit price.
 If using the ‘Standard Cost’ cost method (IN
 Location Category Override, IN Locations, or IN Company Parameters, respectively), this is
 the unit cost used to value inventory for GL updates.
Note: If you manually change this value for a material and additional units of measure exist, upon saving or moving off the record, you will receive a message indicating the change and asking if you want to update the unit cost for the additional units of measure. Select Yes to update the changes, No to save the record without updating the additional units of measure.

##  Std Unit Price

 Enter the current standard unit price for this material/location. The price may be a positive or negative amount. If using the ‘Standard Price Less Discount’ pricing option (IN Company Parameters), this unit price (less the specified discount) will be used as the default whenever this material is sold.
Note: If you manually change this value for a material and additional units of measure exist, upon saving or moving off the record, you will receive a message indicating the change and asking if you want to update the unit price for the additional units of measure. Select Yes to update the changes, No to save the record without updating the additional units of measure.

##  Markup/Discount Rates: Customer

Enter the markup/discount rate to be used when selling this material to customers from this location. For example: for 6%, enter ".06".
 This rate is multiplied by the unit cost or price, as specified in the [pricing option](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form#ID-000137ba--en) selected for customer sales in the [IN Company Parameters](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) form. However, this rate is used only if no [markup/discount rate](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form/field-definitions-ar-customers-form#ID-0000833b--en) is set up for the customer in the [ AR Customers](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form) form.

##  Markup/Discount Rates: Job

Enter
 the markup/discount rate to be used when selling this material to jobs from this location.
 For example: for 6%, enter ".06".
 This rate is multiplied by the unit cost or
 price, as specified in the [pricing option](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form#ID-000137cb--en) selected for job sales in the [IN Company Parameters](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) form. However, this rate is used only
 if no [markup/discount rate](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form/field-definitions-jc-jobs-form#ID-00018cb3--en) is set up for the job in the [JC Jobs](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) form.

##  Markup/Discount Rates: Inventory

Enter the markup/discount rate to be used when selling this material to other inventory locations from this location. For example: for 6%, enter ".06".
 This rate is multiplied by the unit cost or price, as specified in the [pricing option](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form#ID-000137dc--en) selected for inventory sales in the [IN Company Parameters](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) form.

##  Markup/Discount Rates: Equipment

Enter the markup/discount rate to be used when selling this material to equipment from this location. For example: for 6%, enter ".06".
 This rate is multiplied by the unit cost or price, as specified in the [pricing option](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form#ID-000137ec--en) selected for equipment sales in the [IN Company Parameters](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) form.

## Markup/Discount Rates: Service

Enter the markup/discount rate to be used when selling this material to service work orders from this location. For example: for 6%, enter ".06".
 This rate is multiplied by the unit cost or price, as specified in the [pricing option](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form#ID-000137fc--en) selected for service sales in the [IN Company Parameters](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) form. This calculation determines the Cost Rate when this material is specified on a work completed Inventory line in SM Work Orders (Work completed tab).

##  On Hand

 Display only, the total quantity of stock (Invoiced and Received/Not Invoiced) on hand for this location.
 This field is automatically updated when posting transactions in AP, IN (material orders, adjustments, transfers, production), JC (Material Use), MS Ticket Entry, and PO Receipts. If you need to make quantity adjustments or corrections, you should do so using IN Adjustments.

##  Allocated

 Displays the total quantity of this material currently allocated to jobs on quotes or material orders.
 During initial setup, this field should be left blank. Once set up, this field is automatically updated each time this material is allocated to jobs on active MS Quotes and/or IN Material Orders.

##  Available

 Display only, the total quantity of stock available for this location. This value is based on the On Hand quantity less the Allocated quantity, and is updated automatically when posting transactions in AP, IN (material orders, adjustments, transfers, production), MS Ticket Entry, PM Materials (once interfaced), and PO Receipts.

##  On Order

 This field displays the quantity of this material that is currently on order, but has not yet been received or invoiced on purchase orders.
 During initial setup, this field should be left blank. Once set up, this field is automatically updated when this material is set up on a purchase order (PO), and relieved as purchase orders are received or invoiced in AP.

##  Received not/Invoiced

 Displays the current quantity of stock received in PO, but not yet invoiced in AP.
 During initial setup, this field should be left blank. Once set up, this field is automatically updated when items on a purchase order are received (must have been flagged for receiving in PO Purchase Order Entry), and relieved from AP when the invoice batch is posted.
 Received units will also be included in the On Hand quantity.

##  Booked

 Display only, the total units of this material recorded in Inventory and General Ledger.This quantity equals the On Hand quantity and is automatically updated when posting transactions in AP, IN (material orders, adjustments, transfers, production), JC (Material Use), and MS Ticket Entry.
If the "Update GL/Sub Ledgers on Receipt" option is checked in PO Company, this quantity will be also be updated when receiving units in PO Receipts Entry. If the "Update GL/Sub Ledgers on Receipt" option is not checked, this quantity will only be updated once 'received' units are invoiced in AP.

## UM

The UM field on the IN Location Materials form, Addl UMs tab.
If you initialized this material to this location (IN Material Initialize), any additional units of measure set up for this material in HQ Material Units of Measure will automatically default here.
Enter the unit of measure in which this material may be bought or sold for this location. Must be valid unit of measure defined for this material in HQ Materials.

##  Conversion

 Defaults the conversion factor (used to convert this unit of measure to the standard unit of measure) defined for this unit of measure in HQ Material Units of Measure. This will be the number of units of the standard unit of measure that makes up one unit of this unit of measure. For example, if this material is normally dealt with in square feet, but is sometimes bought or sold in 4’ x 8’ sheets, the conversion factor will be 32.
Note: The 'bUnits' datatype has a decimal precision of three (i.e. .000); therefore, it is important that you understand the effects that the conversion factor specified here may have when updating IN/GL with posted units. If the conversion factor has a non-zero value in the 4th (.0245) or 5th position (.00245), rounding may occur.
 For example:
                 Posted Units:         10.00
                       Unit Cost:       128.25000
          Conversion Factor:            .00245
 Conversion to Std Units:            .025      (10.00 x .00245 = 0.0245, rounded to .025)
                     Total Cost:          3.21        (.025 x 128.25 = 3.20625, rounded to 3.21)

 Calculation with decimal precision of 5 (.00000)
                 Posted Units:         10.00
                       Unit Cost:       128.25
          Conversion Factor:            .00245
             Converted Units:            .0245    (10.00 x .00245 = 0.0245)
                     Total Cost:          3.14 (.0245 x 128.25 = 3.14212, rounded to 3.14)

                       Variance:            .07 (3.21 – 3.14 = .07)

## Std Unit Cost

Defaults the unit cost for this unit of measure as defined in HQ Materials. This is the unit cost that will default whenever this material is bought in this unit of measure.

##  ECM

 Defaults from HQ Material Units of Measure, and indicates which quantity the unit cost represents.

- E – Per each

- C – Per Hundred

- M – Per Thousand

## Std Unit Price

Defaults the unit price for this unit of measure as defined in HQ Materials. This is the unit price that will default whenever this material is sold in this unit of measure. The price may be a positive or negative amount.

##  ECM

 Defaults from HQ Material Units of Measure, and indicates which quantity the unit price represents.

- E – Per each

- C – Per Hundred

- M – Per Thousand

##  Last Cost

 Enter the last unit cost for this material in this unit of measure. This field will be updated automatically by the system each time this material is purchased for this location in this unit of measure through PO Receipts or AP invoices.

##  ECM

 Defaults from HQ Material Units of Measure, and indicates which quantity the Last Cost represents.

- E – Per each

- C – Per Hundred

- M – Per Thousand

##  Last Cost Update

 Enter the last date this material was purchased for this location in this unit of measure. After the initial entry, this field will be updated automatically by the system each time this material is purchased for this location in this unit of measure through PO Receipts or AP invoices. Update will only occur if the purchase date is equal to or greater than this field’s current date.
