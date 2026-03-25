---
title: "Field Definitions: MS Ticket Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form/field-definitions-ms-ticket-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form/field-definitions-ms-ticket-entry-form"
---

# Field Definitions: MS Ticket Entry Form

The following is a list of field descriptions for the MS
 Ticket Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq #

Enter NEW to create a new entry, or enter the
 batch sequence number of an existing entry you wish to edit or delete.

## Action

When adding new entries, this field defaults to A-Add and is not accessible. If this is an existing transaction, specify the action for this entry.

- Change – Use this action to make changes to previously processed transactions.

- Delete – Use this action to delete the transaction from all files in Material Sales. (The delete functions in the toolbar and Records menu only delete the entry from the batch.)

Note: If the ticket has already been invoiced (indicated by a message in red showing the AR and/or AP invoice/reference number), you cannot select the Delete option.

##  Sale Date

 Enter the sales date for this ticket. This field initially defaults the current date, but the system allows overrides. The system records this date as the ‘actual’ date in the ticket detail table (MSTD) and related subledgers when the batch posts.

##  From Loc

 Specify the location (IN Locations) that will receive credit for this
 sale. If a material vendor supplied the material, the system credits this location’s sales
 accounts, but does not credit Inventory.

## Ticket #

Optional field.
Enter the ticket number for this transaction, up to 10 characters. This may be the shipping number provided at the scale house, or any other internal transaction number to identify this entry.
Tip: Consider using only numeric characters for the Ticket # field. The field will accept alphanumeric characters, however ticket numbers that include alphabetical characters, punctuation, or special characters will not be evaluated in the MS Missing Ticket report.
If you enter a value, and you opted to have the system check for duplicate numbers (Ticket Warning field in MS Company Parameters), the system displays a warning if it determines that this value already exists for the MS company or MS company/location.

## Void

Check this box to set the status of this ticket to ‘voided’. This entry will not update Inventory or any other subledger, nor can you invoice it.
Uncheck this box to allow invoicing this ticket, and to update the appropriate Inventory and sub ledger accounts.

##  Matl Vendor

 If an outside vendor provided the material, enter the vendor number (from AP Vendors).
 Otherwise, leave this field blank.
 When you enter a vendor number, updates to the ‘sales’ accounts for this location will occur as normal, but no updates to Inventory occur. Additionally, the system does not record material cost. The cost of materials sold on this transaction will be recorded only when the vendor invoice is posted in AP.

## Sale Type

Select the type of purchaser for this transaction. The selection determines which fields display on the form.

- C- Customer

- J-Job

- I-Inventory

## Customer

Enter the customer that bought the material or
 press F4 to select one from a list.
Note: If the Status field on the Additional
 Information tab on the [
 AR Customers ](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form) form is set to On Hold or Inactive, a warning displays next to the
 customer number. If the customer is on hold, the batch can be posted. If customer is
 inactive, you cannot post the batch until you change the status of the customer or remove
 the ticket from the batch.

##  Cust Job

 For Customer sales only.
 If applicable, enter the customer’s job number, up to 20 characters.

##  Cust PO

 For Customer sales only.
 If applicable, enter the customer’s purchase order number, up to 20 characters.

## Paymt Type

For Customer sales only.
Specify the payment type for this transaction.

- A-On Account.

- C-Cash (the Check # field is enabled for optional entry.)

- X-Credit Card

Note: The system initializes invoices based on the invoice level specified for the customer in AR Customers. However, if multiple payment type transactions have been posted to a customer, separate invoices generate for each payment type, based on the Invoice Level option.
For example, if the Invoice Level
 is set to 1-One Invoice Per Customer and Joband you post only cash transactions, the system
 will print one invoice for each customer/customer job combination. However, if you post
 both cash and credit card transactions, the system will print one invoice for the cash
 transactions and one invoice for the credit card transactions for each customer/customer
 job combination.

## Check # / Cheque #

United States: Check # field on the MS Ticket
 Entry form.
Australia and Canada: Cheque # on the MS
 Ticket Entry form.
This field is only available when the
 Sale
 Type is Customer and the  Paymt Type is C-Cash.
United States: Check #
Enter the check number, up to 10 characters.Check # / Cheque #
Entry of a check number is not required. However, if one is entered, the system uses it when initializing invoices to group tickets together. The initialization process generates a separate invoice for each unique check number, and the system groups all tickets with the same check number together on the same invoice.
Note: The check number entered here is informational only; actual payment processing must be performed separately in Accounts Receivable.
Australia: Cheque #
Enter the cheque number, up to 10 characters.
Entry of a cheque number is not required. However, if one is entered, the system uses it when initializing invoices to group tickets together. The initialization process generates a separate invoice for each unique cheque number, and the system groups all tickets with the same cheque number together on the same invoice.
Note: The cheque number entered here is informational only; actual payment processing must be performed separately in Accounts Receivable.
Canada: Cheque #
nter the cheque number, up to 10 characters.
Entry of a cheque number is not required. However, if one is entered, the system uses it when initializing invoices to group tickets together. The initialization process generates a separate invoice for each unique cheque number, and the system groups all tickets with the same cheque number together on the same invoice.
Note: The cheque number entered here is informational only; actual payment processing must be performed separately in Accounts Receivable.

## Hold

For Customer sales only.
Select this checkbox to place the transaction on hold and have it withheld from invoicing.
Uncheck this box to include this ticket during invoicing.

##  JCCo

 For Job sales only.
 Specify the Job Cost company to which this material was sold. Must be a valid Job Cost company.

## Job

For
 Job sales only.
Specify the job (from JC Jobs) to be expensed
 with the materials, haul, and tax posted on this ticket.
Note: If you enter a soft- or hard-closed job, the status displays in red above the tab page. Entry will only be saved if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).

##  INCo

 For Inventory sales only.
 Specify the Inventory company to which this material was sold (must be a valid IN company).

##  To Loc

 Specify the location (from IN Locations) to which this material was sold.

## Material

Enter a material for the ticket or press
 F4
 to select a material from a list.
 If supplied by a vendor, this material must
 be a valid material from HQ Materials. If sold from stock, material must be set up for the
 selling location. If selling to another Inventory location, material must also be set up
 for the receiving (to) location.

##  UM

 This field defaults to the sales unit of measure for the material. You can override this field, but it must be either the material’s standard unit of measure (defined in HQ Materials) or a valid unit of measure that has been defined for the material.
If no unit of measure has been defined for the material:

- If a vendor has been defined in the Matl
 Vendor field, you can define the unit of measure in HQ Materials.

- If this is a stocked material and no vendor has been
 defined in the Matl Vendor field, you can define
 the unit of measure in IN Location Materials.

 If material is sold from stock, unit of measure must be valid for the ‘Sell From’ location, and if sold to another Inventory location (Inventory sales), must also be a valid UM for the ‘Sell To’ location.

## Matl Phase

For Job sales only.
Specify which phase of the specified job will be expensed with the material units and costs.
Defaults:

- If a quote exists, this field defaults the material phase specified on the quote (MS Quotes > Job Phases tab).

- If no quote exists, the field defaults the material phase from HQ Materials, which you can override as necessary.

##  Matl CT

 For Job sales only.
 Specify which cost type will be expensed with the material units and costs on this ticket.
Defaults:

- If a quote exists, this field defaults the cost type specified for the material phase on the quote (MS Quotes > Job Phases tab).

- If no quote exists, this field defaults the material cost type from HQ Materials, which you can override as necessary.

## EMCo

Use this field only when Hauler Type is
 set to Equipment.
Specify the EM company owning the equipment used for hauling this material.

## Equipment

Use this field only when Hauler Type is
 set to Equipment.
Specify the piece of equipment (from EM Equipment) used to haul the material on this ticket. If the specified piece of equipment has an attachment, and that attachment is flagged for revenue posting (in EM Equipment), a separate sequence will be created for the attachment (with just the revenue amounts) once the ticket is validated. Sequence will be displayed once the form is exited and re-entered.

## PRCo

Use this field only when Hauler Type is
 set to Equipment.
Specify the PR company employing the equipment operator.

## Employee

Use this field only when Hauler Type is
 set to Equipment.
Specify the employee (from PR Employees) who operated the equipment. This field initially defaults the employee assigned to the equipment in EM Equipment.

## Hauler Type

Specify the haul type for this ticket.

- Equipment – Material was hauled using your own equipment.

- Haul Vendor – Material was hauled using an outside haul vendor.

- None – No hauling involved.

## Haul Vendor

Use this field to select the vendor that
 hauled the material on the ticket. Enter an AP vendor number or press
 F4 to select one
 from a list.
This field is only enabled when Haul Vendor is
 selected in the Hauler Type field.
AP vendors are created and maintained using the
 [AP Vendors ](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form) form.
Note: Although you are required to enter a haul vendor
 before saving the ticket, you can skip this field and enter a truck below. The system will
 automatically default the haul vendor assigned to the truck in [ MS Vendor Trucks ](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-vendor-trucks-form). If the truck exists for multiple
 vendors, it will default the first vendor with the specified truck.

## Truck

Used only when the Hauler Type is
 set to Haul Vendor.
Specify the truck (from MS Vendor Trucks) used to haul the material on this ticket. If you specify a truck that has not been set up for the specified haul vendor, a warning displays, but entry is allowed. The truck will not be updated for the vendor in MS Vendor Trucks.
Note: If you did not enter a haul vendor above, but you
 enter a truck that exists in MS Vendor Trucks, the system will default the haul vendor for
 you. If the truck exists for multiple vendors, the system will default the first haul
 vendor assigned the specified truck.
Entry of a haul vendor is required when the
 Hauler
 Type is Haul Vendor. If you did not specify a haul vendor above and then
 entered a truck that does not exist in MS Vendor Trucks, you will need to assign a haul
 vendor before saving the record.

## Driver

Used only when Hauler Type is
 set to Haul Vendor.
Enter the name of the driver who operated the
 vendor truck, up to 30 characters.

##  Truck Type

 Specify the type of truck used to haul material. Defaults the truck type specified for the equipment in EM Equipment (if own equipment) or MS Vendor Trucks (if haul vendor).
 The truck type is one of the factors used to determine haul and pay rates.

##  Start Time

 Optional field.
 Enter the start time for this haul, in 24-hour format (e.g. '08:00' for 8:00 a.m.). Use '00:00' for 12 midnight.
Note: If both start time and stop time are '00:00', the stop time is assumed to be midnight of the following day, and the total hours will be 24.00.

## Stop Time

Optional field.
Enter the stop time for this haul, in 24-hour format. Use '00:00' for 12 midnight.
Note: If stop time is less than the start time, stop time is assumed to be on the following day. For example, if start time is '17:00' (5:00 p.m.), and the stop time is '02:00' (2:00 a.m.), the total hours will be 9.00.If both start time and stop time are '00:00', the stop time is assumed to be midnight of the following day, and the total hours will be 24.00.

## Loads

Optional field.
Enter the total number of loads it took to complete this haul, up to 4 digits. If not using vehicle weights to calculate units sold, then the number of loads specified here will be used in conjunction with the delivery vehicle’s capacity to determine units sold.  See Material Units below for more information.

## Miles

This field displays as Kms for
 Australia and Canada (i.e. the Default Country in HQ Company Setup is AU
 or CA).
Optional field.
Enter the total number of miles/kilometres traveled to complete this haul, up to 3 digits and 3 decimals.

##  Hours

 Optional field.
 This field defaults the total number of hours it took to complete this haul, based on the start and stop times for this haul. You can override this field, but start/stop times do not automatically recalculate.

##  Zone

 Enter the haul zone for this haul, up to 10 characters. May be used to determine haul and pay rates.
 If a quote exists for the purchaser, and a haul zone is defined on the quote for the sales location, that haul zone will default here.

## Gross

Specify the weight of this vehicle when it is fully loaded. This will be
 the tare weight of the vehicle plus the weight of the material. The system uses the gross
 and tare weights to determine the net weight, which it uses to calculate material units
 (i.e. Units Sold).
The gross weight may be set to 0.00, which may be typical if you do not yet know the vehicle's gross weight. A warning displays stating that gross weight must be equal to or greater than tare weight, but entry is allowed. If set to 0.00 and a tare weight is entered, the system cannot calculate the material units. You will need to enter them manually. If you later enter a gross weight, existing material units will be overridden with the system's calculation (gross weight less tare weight).

- Weight will be converted to the sales location’s
 weight unit of measure (tons, pounds, or kilograms) as specified in IN Locations.

- If this is an imported ticket, and the weight UM
 (shown to the right of the Net Weight field) is not a valid HQ
 unit of measure, you will need to delete the ticket batch, fix your import template
 or text file, and then re-import the data.

## Tare

Enter the tare weight of this vehicle (i.e. the weight of the vehicle when
 empty). Initially defaults the tare weight (in add mode only) specified in EM Equipment (if
 own equipment) or MS Vendor Trucks (if a haul vendor). The system converts the weight to
 the sales location’s weight unit of measure (tons, pounds, or kilograms) as specified in IN
 Locations. If the vehicle’s weight unit of measure is other than TONS, LBS, or kg, no
 conversion will occur, and default tare weight will be 0.00.
The tare weight must be equal to or less than the gross (fully loaded) weight of the vehicle. The system subtracts the tare weight from the gross weight to determine the net weight, which is then used to calculate material units (i.e. Units Sold).  See Material Units below for more information.
If the gross weight is 0.00 (which may be typical if you do not yet know the vehicle's gross weight), entry of a tare weight greater than the gross weight is allowed; however, the system cannot calculate the material units and you will need to enter them manually.
Note: If this is an imported ticket and the weight UM (shown to the right of the Net Weight) is not a valid HQ unit of measure, you will need to delete the ticket batch, fix your import template or text file, and then re-import the data.

## Haul Code

Enter the haul code (from MS Haul Codes) for this transaction. The system uses the haul code to determine haul rate. If a haul code is not entered, the system disables the remaining haul-related fields.
This field defaults as follows:

- If an active quote exists, the field defaults from the haul code information set up on the quote.

- If an active quote does not exist or haul code information is not set up on the quote, the field defaults the haul code defined for the material in HQ Materials.

- If an active quote does not exist and no haul code is defined in HQ Materials, the field defaults blank.

## Haul Phase

For Job sales only.
Enter the phase to which haul charges will be expensed.
Defaults:

- If an active quote exists and you entered a valid
 code in Truck
 Type field, this field defaults the haul phase defined on the quote
 (MS Quotes > Job Phase tab).

- If no haul phase is defined on the quote, this field defaults to the haul phase defined for the material in HQ Materials.

- If no haul cost type is defined for the material in
 HQ Materials, and a valid code has been entered in the Haul Code
 field, this field defaults to the material cost type specified in the Matl
 Phase field.

Note: If an attachment exists for the specified equipment, and you have elected to post revenue to the attachment (EM Equipment), the attachment sequence (created when ticket is validated/saved) will default the haul phase and haul cost type specified for the equipment.

## Haul CT

For Job sales only.
Enter the cost type to which haul charges will be expensed.
Defaults:

-  If an active quote exists and you entered a valid
 code in Truck
 Type field, this field defaults the haul cost type defined on the
 quote (MS Quotes form, Job Phase tab). If no haul cost type is defined on the quote,
 this field defaults to the haul cost type defined for the material in HQ Materials.
 If no haul cost type is defined for the material in HQ Materials, and a valid code
 has been entered in the Haul Code field, this field
 defaults to the material cost type specified in the Matl Phase field.

Note: If an attachment exists for the specified equipment, and you have elected to post revenue to the attachment (EM Equipment), the attachment sequence (created when ticket is validated/saved) will default the haul phase and haul cost type specified for the equipment.

## Units Sold

Specify the number of units sold of this material. This field
 initially defaults a value based on the net weight of vehicle (gross weight minus tare
 weight), material weight conversion factor (specified in IN Location Materials), and sales
 unit of measure.
For example, if the net weight is 5,500 lbs, the sales unit of measure is TON, and the material’s weight conversion factor is 2,000 (lbs per TON), the units sold default would be 2.75.
If the gross weight is 0.00 (which may be
 typical if you do not know the vehicle's gross weight) and the tare weight is greater than
 0.00, the system cannot calculate the material units. You will need to enter them
 manually.
If not using vehicle weights to calculate
 units sold, then the system uses the number of loads in conjunction with the delivery
 vehicle’s capacity to determine units sold. For more information, see Material Units in
 Related Topics below.
Note: Changing units sold on an existing ticket will cause
 the system to recalculate the material total. If a customer sale, the system only
 recalculates the material total if the  Paymt Type is A-On Account. If the
  Paymt
 Type is C-Cash or X-Credit Card, the tax basis will not be recalculated,
 which may cause the material total to be equal to the units x unit price.
The units posted to a job ticket will only be
 updated to JCCD (Cost Detail) if you have checked the Update Actual Units From MS option
 for the specified job in JC Jobs. If option is unchecked, units will be set to 0.00 in
 JCCD. For more information, refer to Transaction Detail in Related Topics below.

## Unit Price

Enter the unit price of the material. This field defaults based on the
 pricing hierarchy.
Note: Changing the unit price on an existing ticket will
 cause the material total to recalculate. If a customer sale, the material total only
 recalculates if the Paymt Type is A-On Account. If the Paymt Type is C-Cash or X-Credit Card,
 the material total will not be recalculated, which may cause the material total to not be
 equal to the units x unit price.
The unit cost posted for a job ticket will
 only be updated to JCCD (Cost Detail) if you have checked the Update Actual Units From MS
 option for the specified job in JC Jobs. If option is unchecked, units will be set to 0.00
 in JCCD.
Pricing Hierarchy

1. Material detail set up on an active quote - If an active quote exists for the purchaser, the system searches the Quote Detail tab for an entry matching the sales location and material. If the system finds an entry, it uses the unit price on that entry, regardless of status.

1. Pricing overrides set up on an active quote - If the system does not find pricing in the quote detail, it searches the Price Overrides tab on the quote based on sales location and material category. If the system finds an entry, it uses the unit price for the location and material category.

1.  Price template assigned to an active quote - If a price override does not exist, the system searches the price template assigned to the quote. Pricing hierarchy will determine which unit price to use.

1. Price template assigned in the AR Customers, JC
 Jobs, or IN Locations (depending on sale type) - If you did not assign a price
 template to the quote, or no active quote exists, the system searches the price
 template assigned to the purchaser in AR Customer, JC Job, or IN Location. Pricing
 hierarchy will determine which unit price to use.

1. If you did not assign a price template, or no entry
 within the price template exists for the material, the system applies the Pricing
 Option selected in IN Company and the markup/discount rates assigned in AR Customers
 and JC Jobs to standard prices in IN Location Materials (stocked) or HQ Materials
 (non-stocked).

## ECM

Indicate what quantity the unit price represents.

- E-Per Each

- C-Per Hundred

- M-Per Thousand

## Material Total

This field displays the total price of the material sold on this ticket. Defaults a value based on the number of units x unit price (adjusted by ECM). If changed, unit price recalculates. Units remain the same.
Note: Changing the material total on an existing ticket will
 cause the unit price to recalculate. If this is a customer sale, the unit price only
 recalculates if the Paymt Type is A-On Account. If the Paymt Type is C-Cash or X-Credit Card,
 the unit price will not be recalculated, which may cause the material total to not be equal
 to the units x unit price.

## Haul Basis

Enter the quantity on which to calculate the haul charges. Initially defaults a value based on the haul code’s basis (i.e. per unit, per hour, per load, units/mile, or units/hour). If based on units, units/mile, or units/hour, the default will be the posted material units. If hourly based, default will be the posted hours.
Note: If haul charges are based on values entered with the
 revenue or pay code (i.e., the Use EM Revenue/Hauler Pay Amounts box is
 checked in MS Haul Codes), this field will automatically default the revenue or pay basis
 and will be disabled.

## Haul Rate

Enter the rate at which to calculate haul charges.
If an active quote exists for the purchaser, haul rate will default from quote based on information on ticket. If no override rate is found, or no quote exists, will default the haul rate defined for the haul code in MS Haul Codes.
Note: If haul charges are based on values entered with the
 revenue or pay code (i.e., the Use EM Revenue/Hauler Pay Amounts box is
 checked in MS Haul Codes), this field will automatically default the revenue or pay rate
 and will be disabled.

## Haul Charge

Enter the total charge for hauling this material. Initially defaults an amount based on the haul basis x haul rate or, the minimum amount specified for the haul code (in MS Quotes or MS Haul Codes) if the haul basis is greater than 0.00 and the calculated haul charge is less than the minimum amount. Overriding the default will cause the system to recalculate the haul rate.
Note: If haul charges are based on values entered with the
 revenue or pay code (i.e., the Use EM Revenue/Hauler Pay Amounts box is
 checked in MS Haul Codes), this field will automatically default the revenue or pay total
 and will be disabled.

## Rev Code

Used only when Hauler Type is
 set to Equipment.
Specify the revenue code (from EM Revenue
 Codes) to which equipment usage will be posted, and by which equipment revenue will be
 calculated. Defaults the revenue code assigned to the equipment in EM Equipment.
Note: If revenue code is unit-based, and hours were posted to this ticket, both work and time units will be updated to the EM Revenue Detail table (EMRD). In addition, the posted hours will be updated to the equipment's hour meter. If the revenue code is hourly based, only time units will be updated to EMRD.

## Revenue Basis

Used only when Hauler Type is
 set to Equipment.
Enter the basis on which to calculate equipment revenue. Defaults a value based on the revenue basis defined for the revenue code in EM Revenue Codes.

- If the revenue basis is ‘Hour’, defaults a value based on the posted hours divided by the revenue code’s hours/time unit. For example, if the Hours/Time Unit is 8.00 and 12 hours were posted, the revenue basis would be 1.5.

- If the revenue basis is ‘Unit’, defaults the posted material units.

- If revenue charges are based on values entered with the haul code (i.e. ‘Based on MS Haul Charge” option is checked in EM Revenue Codes), this field automatically defaults the haul basis and is disabled.

- If haul charges are revenue based, the haul basis will default from this value. In addition, if the equipment has attachments, and the attachment is flagged to receive revenue (in EM Equipment, Comp/Attach tab), the system will automatically calculate revenue and haul charges for the attachment as well.

## Revenue Rate

Used only when Hauler Type is
 set to Equipment.
Enter the revenue rate to use for calculating
 usage for the specified equipment. Defaults the rate specified for the revenue code in EM
 Revenue Rates by Category or EM Revenue Rates by Equipment. You may override this amount if
 you have checked the Allow Rate Change box in EM Company
 Parameters (Usage tab) and the Allow Posting Override box in EM Revenue
 Rates by Category or EM Revenue Rates by Equipment.

- If revenue charges are based on values entered with
 the haul code (i.e., you have checked the Based on MS Haul Charge box in EM
 Revenue Codes), this field automatically defaults the haul rate and is disabled,
 regardless of whether you specified to allow rate changes and posting overrides.

- If haul charges are revenue based, the haul rate will default from this value. In addition, if the equipment has attachments, and the attachment is flagged to receive revenue (in EM Equipment, Comp/Attach tab), the system will automatically calculate revenue and haul charges for the attachment as well.

## Revenue Total

Used only when Hauler Type is
 set to Equipment.
This field defaults the total revenue for this
 piece of equipment (revenue basis x revenue rate). You may override this amount if you have
 checked the Allow
 Rate Change box in EM Company Parameters (Usage tab) and the Allow Posting
 Override box in EM Revenue Rates by Category or EM Revenue Rates by
 Equipment. Overriding this amount will cause the system to recalculate the revenue
 rate.

- If revenue charges are based on values entered with the haul code (i.e., you have checked the ‘Based on MS Haul Charge’ option in EM Revenue Codes), this field automatically defaults the haul total and is disabled, regardless of whether you specified to allow rate changes and posting overrides.

- If haul charges are revenue based, the haul total will default from this value. In addition, if the equipment has attachments, and the attachment is flagged to receive revenue (in EM Equipment, Comp/Attach tab), the system will automatically calculate revenue and haul charges for the attachment as well.

## Pay Code

Optional. Used only when Hauler Type is
 set to Haul Vendor.
Specify the pay code (from MS Pay Codes) that will be used to determine the haul vendor’s payment. Defaults the pay code assigned to the vendor/truck in MS Vendor Trucks.

## Pay Basis

Used only when Hauler Type is
 set to Haul Vendor.
Enter the basis on which to calculate the haul vendor’s payment. Defaults a value based on the pay rate basis defined for the pay code (in MS Pay Codes). If pay rate basis is:

- Per Unit, Units/Mile, or Units/Hour – Defaults the posted material units.

- Hourly – Defaults the posted hours.

- Per Load – Defaults the posted loads.

- Percent of Haul Charge – Defaults the posted haul charge.

## Pay Rate

Used only when Hauler Type is
 set to Haul Vendor.
Specify the rate per haul unit that will be paid to the haul vendor for these haul charges. Defaults the pay rate as follows:

- If a quote exists, uses the pay rate defined on the quote.

- If no override pay rate defined or no quote exists, uses the standard pay rate defined in MS Pay Codes.

Note: If you change the pay code or pay total for this entry, this rate will be recalculated.

## Pay Total

Used only when Hauler Type is
 set to Haul Vendor.
Enter the total amount to pay the haul vendor for hauling the material on this ticket. Initially defaults an amount based on the pay basis x pay rate or the minimum payment amount specified for the pay code (in MS Quotes or MS Pay Codes) if the pay basis is greater than 0.00 and the calculated payment amount is less than the minimum payment amount. Overriding the default will cause the system to recalculate the pay rate.

## Tax Type

Select the tax type of this transaction.
This field defaults as 2-Use when Job or
 Inventory is selected in the Sale Type field.
For Customer sales, this field defaults based on the Default Country associated with the active company in the [HQ Company Setup](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form) form.

- If the default country is US, defaults to 1-Sales.

- If the default country is not US(e.g. AU, CA, etc.), defaults to 3-VAT.

## Tax Code

Enter the tax code for calculating taxes on material and/or haul charges on
 the ticket, or press F4 to select a tax code from a list.
Note: Taxes can only be calculated for materials and/or haul charges that are flagged as taxable. If the material and haul charges are not taxable, a warning displays and entry is not allowed.
Tax code will default from AR Customers, JC
 Jobs, or IN Locations, depending on the selection in the Tax Option
 field on the Info tab of [MS Company Parameters ](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-company-parameters-form).

- If tax code default is based on sale type and purchaser, and a quote exists for the purchaser (Customer, Job, or Location), the tax code will default from the quote.

- If no tax code is specified on the quote, or no
 quote exists, the tax code will default from AR Customers, JC Jobs, or IN Locations,
 depending on the purchaser.

Note: If you have defined a tax code default using the F3 Properties window, it will override the standard routine used to find the correct tax code. This is NOT recommended.

## Tax Basis

This field is disabled when the Tax Type is
 null and the Tax
 Code is blank.
Enter the amount on which taxes will be
 calculated for this ticket. Default will be based on whether the material and/or haul
 charges are taxable. If neither is taxable, default will be 0.00. If both are taxable,
 default will be the material total plus the haul charge. If material is taxable, but not
 the haul charge, default will be the material total. If material is not taxable, but the
 haul charge is, then default will be the haul charge.
Default may be overridden. If overridden, tax amount will be recalculated.
Note: Changes to the material total on an existing ticket
 will update the tax basis. If a customer sale, tax basis will only be updated if the
 Paymt
 Type is A-On Account. If the Paymt Type is C-Cash or X-Credit Card,
 the tax basis will not be updated, which may cause the tax basis to not be equal to the
 material total.

## Tax Total

This field is disabled when the Tax Type is
 null and the Tax
 Code is blank.
Enter the total amount of tax for this ticket.
 Initially defaults a calculation of the tax basis times the tax rate. You should not need
 to change this amount; however, if you do change the default amount, the tax basis will not
 be recalculated. If the Tax Type is Sales or VAT, this amount
 will print on the invoice. If the Tax Type is Use, this amount will be
 accrued and paid later to the appropriate taxing authority.
Note: Changes to the tax code, material total, or tax basis
 on an existing ticket will cause the tax amount to be recalculated. If a customer sale, the
 tax amount will only be recalculated if the Paymt Type is A-On Account. If the
 Paymt
 Type is C-Cash or X-Credit Card, the tax amount will not be
 recalculated.

## Tax Total

Enter the tax amount for this surcharge. Initially defaults an amount based on the tax rate for the tax code specified on the parent ticket and the surcharge total. If no taxes were calculated on the parent ticket, this field defaults as 0.00.
Note: Surcharge code must be flagged to allow taxes (i.e.
 the Subject to
 Sales Tax When Material is Taxable box is checked in MS Surcharge Codes). If
 the surcharge code does not allow taxes, this field will be disabled and the tax amount
 will default as 0.00, regardless of whether taxes were calculated on the parent
 ticket.

## Disc Type

For Customer sales only.
Display only, the discount type for this customer, based on the payment terms, payment terms type, and the material’s payment discount type.

- If payment terms are rate-based (i.e. Discount Based on
 Material box is unchecked in HQ Payment Terms), default will be
 'Rate'.

- If payment terms are material-based (i.e.,
 Discount
 Based on Materialbox is checked in HQ Payment Terms), default will be
 'R-Discount Rate per dollar', ' U-Discount per Unit', or 'N-No Discount', depending
 on the material’s payment discount type (in HQ Materials).

## Discount Basis

For Customer sales only.
Enter the basis amount to use when calculating the discount amount for this ticket.

- If using rate-based discounts (i.e.,  Discount Based on
 Material box is unchecked in HQ Payment Terms), the basis defaults the
 material total plus any haul charges.

-  If using material-based discounts (i.e., Discount Based on
 Material box is checked in HQ Payment Terms) and the material’s
 payment discount type is Rate, the basis defaults the material total. If the
 material’s payment discount type is Unit, this field defaults the material units
 sold. Haul charges are not included in material-based discounts.

Note: If the Payment Terms selected in AR Customers have no
 Discount Date (i.e., None is selected for Discount Date
 in HQ Payment Terms), then this Discount Basis field is unavailable for editing.

## Discount Rate

For Customer sales only.
Enter the rate or amount per unit to be used in the calculation of the discount offered on this ticket (based on the Payment Terms assigned to the customer in AR Customers).
Note: If the Payment Terms selected in AR Customers has no
 Discount Date (i.e., None is selected for Discount Date
 in HQ Payment Terms), then this Discount Rate field is unavailable for editing.

- If using rate-based discounts (i.e.,
 Discount Based on Material box is unchecked in HQ Payment Terms),
 this field defaults the rate specified in HQ Payment Terms.

- If using material-based discounts
 (i.e., Discount Based on Material box is checked in HQ Payment Terms),
 rate or amount will default as follows:

- uses the discount overrides set
 up on an active Quote

- uses the Discount Template
 assigned to an active Quote

- uses the Discount Template
 assigned to the specified customer in AR Customers

- uses the standard discount set
 up for the material in HQ Materials

Once the system determines the rate, it
 applies the rate based on the material’s Payment Discount type (defined in HQ Materials).
 For rate-based discounts, calculation is the rate times the material total. For unit-based
 discounts, calculation is the rate times the number of units sold.

## Disc Offered

Enter the discount offered for this surcharge sequence. Initially defaults an amount based on the customer's discount rate and the surcharge total. If no discount was offered on the parent ticket, this amount defaults as 0.00.
Note: This surcharge code must be flagged to allow discounts
 (i.e. the Allow
 Discounts with Material Discounts box is checked in MS Surcharge Codes). If
 this surcharge code does not allow discounts, this field will be disabled and the discount
 amount will default as 0.00, regardless of whether a discount was offered on the parent
 ticket.

## Tax Discount

Enter the tax discount amount for this surcharge sequence. Initially defaults an amount based on the tax rate for the tax code specified on the parent ticket and the surcharge's discount offered amount. If no surcharge discount is offered, this field defaults as 0.00.
Note: This surcharge code must be flagged to allow discounts
 (i.e. the Allow
 Discounts with Material Discounts box is checked in MS Surcharge Codes). If
 the surcharge code does not allow discounts, this field will be disabled and the tax
 discount amount will default as 0.00.

## Haul Pay Tax Type

Enabled for Australia and Canada only (i.e.
 the Default
 Country in HQ Company Setup is AU or CA); used only when Hauler Type is
 set to Haul Vendor.
Specify the haul payment tax type. Initially defaults as 3-VAT, but may be overridden.

- 1-Sales

- 2-Use

- 3-VAT (Value Added Tax)

## Haul Pay Tax Code

Enabled for Australia and Canada only (i.e.
 the Default
 Country in HQ Company Setup is AU or CA); used only when Hauler Type is
 set to Haul Vendor.
Specify the tax code to use for calculating taxes on payments to the haul vendor. Initially defaults the tax code specified for material and/or haul charges (in the Tax Code field above). May be overridden.

## Haul Pay Tax Amt

Enabled for Australia and Canada only (i.e.
 the Default
 Country in HQ Company Setup is AU or CA); used only when Hauler Type is
 set to Haul Vendor.
Specify the total amount of tax to apply to the haul vendor payment or accept the default calculation (pay total x tax rate).
Note: The default calculation may be overridden; it will not affect the vendor payment amount.

## Ship To: State

Enter the delivery state (as defined in HQ States) for the materials on this ticket. The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
This state will print on the invoice if the customer’s Invoice Level (AR Customers) is set to print a separate invoice per customer job. Otherwise, it is informational only
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Ship To: Street

Enter the street address to which the material specified on this ticket will be delivered,. Up to 60 characters allowed. The street address specified here overrides the address specified at the quote level, and will print on the invoice. A separate invoice is created for each ticket with a different 'ship to' address, regardless of invoice level settings in AR Customers.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Ship To: City

Enter the delivery city, up to 30 characters.
 This city will print on the invoice if the customer’s Invoice Level (AR Customers) is set
 to print a separate invoice per customer job. Otherwise, this is informational only.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Ship To: Zip

Specify the zip code for the delivery address.  This zip code will print on the invoice if the customer’s Invoice Level (AR Customers) is set to print a separate invoice per customer job. Otherwise, it is informational only.
If you have Internet access, you can click the
 Map button () to view the
 address using your default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Ship To: Country

Enter the 2-character country code for the delivery address. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Setup for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

##  Reason Code

 Optional field.
 Enter the reason code (from HQ Reason Codes) that identifies why this tickets is being entered, changed, or deleted. For example, a reason code might be entered to provide an explanation for a credit being issued or a correction being made.

## Sur Seq

This field displays the sequence number
 assigned to each auto-generated surcharge. If you are manually adding surcharges, enter
 N,
 New,
 or +. The system will
 automatically assign the next available sequence number.

## Action

This field is automatically defaults to A-Add for auto-generated and manually entered surcharges, and cannot be changed.
 If this is an existing surcharge (i.e., you pulled the parent ticket back into a batch), this field will default as C-Change. If you are not changing the parent ticket, but need to make a change to the surcharge, leave this field as defaulted. If you are not changing the parent ticket, but want to delete the surcharge, set this field to D-Delete.
If you make any changes to the parent ticket, this field will automatically default as D-Delete for all existing surcharges (manual and auto-generated) and cannot be changed. In addition, the entire line will be highlighted in red. The system reassess the surcharges and adds them below the original surcharges. Surcharges that were previously added manually will need to be re-entered. Once you post the batch, the system deletes the surcharges marked as D-Delete. This allows for the surcharges to be backed out of GL and then re-added with the new values.

## Surcharge Code

If surcharges were auto-assessed (i.e. a surcharge group is assigned to the related quote or in MS Company Parameters), this field initially defaults the surcharge code for each assessed surcharge.
Enter the surcharge code (from MS Surcharge Codes) for this sequence.

## Surcharge Basis

If surcharges were auto-assessed (i.e. a surcharge group is assigned to the related quote or in MS Company Parameters), this field defaults the amount on which the surcharge was originally assessed.
Enter the basis for this surcharge sequence. This amount will be multiplied by the surcharge rate to determine the surcharge amount.

## Surcharge Rate

If surcharges were auto-assessed (i.e. a surcharge group is assigned to the related quote or in MS Company Parameters), this field defaults the surcharge rate defined for this surcharge code in MS Quotes (Surcharge Overrides tab) or MS Surcharge Codes (Rates tab).
Enter the rate for this surcharge sequence. This amount will be multiplied by the surcharge basis to determine the surcharge amount.

## Surcharge Total

If surcharges were auto-assessed (i.e. a surcharge group is assigned to the related quote or in MS Company Parameters), this field defaults the original surcharge amount.
This amount is a calculation of Surcharge Basis x Surcharge Rate.
Important: If you change the default amount, the surcharge basis and surcharge rate values will not be updated.

## Discount Offered

For Customer sales only.
Enter the total discount amount offered for early payment on this ticket. Default is the [discount basis](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form/field-definitions-ms-ticket-entry-form#ID-0001e7a6--en) x [discount rate](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form/field-definitions-ms-ticket-entry-form#ID-0001e7b7--en).
Note: If the Payment Terms selected in AR Customers has no
 Discount Date (i.e., None is selected for Discount Date
 in HQ Payment Terms), then this Discount Offered field is unavailable for editing.
The default may be overridden. In this case, the [tax discount](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form/field-definitions-ms-ticket-entry-form#ID-0001e7dc--en) will be recalculated, but discount basis and discount rate will not be recalculated.

## Tax Discount

For Customer sales only. Used only when the
 Allow TaxDisc on
 Invoices & Receipts box is checked in AR Company Parameters.
The total amount of sales tax to credit off the customer’s payment if the discount offered is taken. Default is the tax rate x discount offered.
Note: If the Payment Terms selected in AR Customers has no
 Discount Date (i.e., None is selected for Discount Date
 in HQ Payment Terms), then this Tax Discount field is unavailable for editing.
