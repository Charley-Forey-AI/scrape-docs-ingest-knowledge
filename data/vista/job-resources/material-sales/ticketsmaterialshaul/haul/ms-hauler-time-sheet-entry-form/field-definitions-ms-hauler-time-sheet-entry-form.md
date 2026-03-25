---
title: "Field Definitions: MS Hauler Time Sheet Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/ms-hauler-time-sheet-entry-form/field-definitions-ms-hauler-time-sheet-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/ms-hauler-time-sheet-entry-form/field-definitions-ms-hauler-time-sheet-entry-form"
---

# Field Definitions: MS Hauler Time Sheet Entry Form

The following is a list of field descriptions for the MS
 Hauler Time Sheet Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq#

 Enter NEW to create a new entry or enter the batch sequence number of an existing entry you wish to display.

## Action

When entering new records, this field defaults to A (Add) and cannot be accessed.
If this is an existing record, specify the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all MS files. (The delete functions in the toolbar and Records menu only deletes the entry from the batch.)

##  Freight Bill

 Enter the freight bill number. This number identifies the hauler’s time sheet, and is typically a pre-assigned number printed on the time sheet document.
The freight bill number can be up to 10 characters long.

## Sale Date

Enter the sales date for this transaction. Initially defaults to the current date. This date is the sales date for this transaction. The system records this date in MS Haul Header (MSHH) and Ticket Detail (MSTD) tables, and updated to related sub-ledgers when the batch posts. This field defaults to the previous value; if blank, it defaults to system date.
Note: Once you enter line detail, this field is disabled.  If you need to change the sales date, you must first delete all line detail.

## Employee

Used only when Hauler Type is
 E-Equipment.
Specify the employee (from PR Employees) who operated the equipment. Initially defaults the employee assigned to the equipment in EM Equipment (if one assigned).
Note: Once you enter line detail, this field is disabled. If
 you need to change the employee, you must first delete all line detail.

## Hauler Type

Specify the haul type for this hauler time sheet.

- E-Equipment – Material was hauled using your own equipment.

- H-Haul Vendor – Material was hauled using an outside haul vendor.

Note: Once you enter line detail, this field is disabled.  If you need to change the hauler type, you must first delete all line detail.

## EMCo

Used only when Hauler Type is
 E-Equipment.
Specify the EM company owning the equipment used for hauling the material on this time sheet.
Note: Once you enter line detail, this field is disabled.
 If you need to change the EM company, you must first delete all line detail.

## Equipment

Used only when Hauler Type is
 E-Equipment.
Specify the piece of equipment used to haul the material on this time sheet. Must be an active piece of equipment set up in EM Equipment.
Note: Once you enter line detail, this field is disabled. If
 you need to change the equipment, you must first delete all line detail.

##  PRCo#

 Used only when Hauler Type is ‘Equipment’.
 Specify the PR company employing the person who operated the equipment. Initially defaults the PR company assigned to the equipment in EM Equipment (if one assigned).
Note: Once you enter line detail, this field disables. If you need to edit this field, delete line detail first.

##  Haul Vendor

 Used only when Hauler Type is ‘Haul Vendor’.
 Specify the haul vendor (from AP Vendors)
 whose truck was used to haul the material on this time sheet.
Note: Once you enter line detail, this field disables. If you need to edit this field, delete line detail first.

##  Truck#

 Used only when Hauler Type is ‘Haul Vendor’.
 Specify the truck (from MS Vendor Trucks) used to haul the material on this time sheet. If you specify a truck that has not been set up for the vendor, a warning displays; however, entry is allowed.
Note: Once you enter line detail, this field disables. If you need to edit this field, delete line detail first.

## Driver

Used only when Hauler Type is
 H-Haul Vendor.
Enter the name of the driver who operated the
 vendor truck, up to 30 characters.

##  Line #

 Enter the line number, up to 4 digits, or enter ‘N’ or ‘New’ for the next sequential line number.
 Line numbers are used within the haul batch only; that is, once posted, their value is not saved.If an existing transaction is pulled into the batch, the system will assign a sequential line number to it as it is added to the batch.

## Action

When entering new records, this field defaults to A (Add) and cannot be accessed.
If this is an existing record, specify the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all MS files. (The delete functions in the toolbar and Records menu only deletes the entry from the batch.)

Note: If a line has already been invoiced (indicated by a message in red next to the line number showing the AR and/or AP invoice/reference number), it cannot be flagged for delete, nor may any field related to purchaser, material, haul, tax, or discount be changed.

##  From Location

 Specify the IN Location (from IN Locations) that will receive credit for
 the hauling revenue posted with this line.

##  Material Vendor

 If an outside vendor supplied the material, specify the vendor number (from AP Vendors).
 Otherwise, leave this field blank.

##  Material

 Specify the material (from HQ Materials) being delivered.
 If this is an Inventory sale, material must be stocked at the ‘to’ location.

##  UM

 Initially defaults the sales unit of measure for the specified material. You can override this field, but it must be either the material’s standard unit of measure (defined in HQ Materials) or a valid unit of measure that has been defined for the material.
If no unit of measure has been defined for the material:

- If a vendor has been defined in the Matl
 Vendor field, you can define the unit of measure in HQ Materials.

- If this is a stocked material and no vendor has been
 defined in the Matl Vendor field, you can define
 the unit of measure in IN Location Materials.

 If this is a stocked material, this value
 must also be a valid unit of measure for the ‘from location’. If this is an Inventory sale,
 the unit of measure must be valid for the ‘to location’. You can set these up in IN
 Location Materials.

## Sale Type

Specify the sale type (purchaser) for this hauler time sheet.
Corresponding fields for entering purchaser information will display once the sale type is indicated.

##  Customer

 For Customer sales only.
 Specify the customer (from AR Customers) to which these haul charges apply.

##  Customer Job

 For Customer sales only.
 If applicable, specify the customer’s job number, up to 20 characters.

## Customer PO#

For Customer sales only.
If applicable, enter the customer’s purchase order number, up to 20 characters.

##  Payment Type

 For Customer sales only.
 Specify the payment type for this hauler time sheet.

- A-On Account

- C-Cash (Check # input is enabled for optional entry)

- X-Credit Card

## Check#

For Customer sales only, where Payment Type is
 C-Cash.
Enter the check number, up to 10 characters. This field is informational only.

##  Hold

 For Customer sales only.
 Indicate whether this transaction should be included in the invoicing process.
 When you select this checkbox, the transaction is on hold and the system withholds it from the invoicing process. When initializing invoices (MS Invoice Initialize), the system skips this ticket..

##  JCCo#

 For Job sales only.
 Specify the JC company to be charged for these haul charges.

##  Job

 For
 Job sales only.
 Specify the job (from JC Jobs) to be expensed
 with the haul and tax posted for this haul line.

##  Phase

 For Job sales only.
 Specify the phase to be expensed with this line’s haul units and costs.
 If an active quote exists, will default the haul phase defined on quote (Job Phase tab). If no override haul phase is defined, will default the haul phase defined for the material in HQ Materials.

##  CT

 For Job sales only.
 Specify the cost type to be expensed with this line’s haul units and costs.
 If an active quote exists, will default the haul cost type defined on quote (Job Phase tab). If no override cost type is defined, will default the haul cost type defined for the material in HQ Materials.

##  INCo#

 For Inventory sales only.
 Specify the Inventory company to be expensed for this line’s haul charges.

##  To Location

 For Inventory sales only.
 Specify the location (from IN Locations) to
 be expensed for this line’s haul charges. This will be the Inventory location to which the
 materials were delivered.

##  Truck Type

 Specify the type of truck (from MS Truck Types) used to deliver the material on this transaction. Defaults the truck type specified for the equipment in EM Equipment (if own equipment) or MS Vendor Trucks (if haul vendor).
 The truck type is one of the factors used to determine haul and pay rates.

##  Start

 Optional.
 Enter the start time for this haul line, in 24-hour format.

##  Stop

 Optional.
 Enter the stop time for this haul, in 24-hour format.
Note: If the stop time is less than the start time, a warning is displayed. If you accept your entry, the stop time is assumed to be on the following day. So, if start time is 17:00 (5:00 p.m.), and the stop time is 02:00 (2:00 a.m.), the total hours will be 9.

##  Loads

 Optional.
 Enter the total number of loads it took to complete this haul, up to 4 digits. May be used to determine haul charges.

##  Miles

 Optional.
 Enter the total number of miles travelled to complete this haul, up to 3 digits and 3 decimals. May be used to determine haul charges.

## Hours

Optional.
The total number of hours it took to complete this haul, based on the start and stop times for this haul. May be overridden, but start/stop times will not be recalculated. May be used to determine haul charges.

##  Zone

 Enter the haul zone for this haul, up to 10 characters. May be used to determine haul and pay rates.
 If a quote exists for the purchaser, and a haul zone is defined on the quote for the sales location, that haul zone will default here.

##  Haul Code

 Optional.
 Enter the haul code (from MS Haul Codes) for this transaction. Haul code will be used to determine haul rate.If no haul code is entered, remaining haul-related inputs will be disabled.
 If an active quote exists, this field defaults from the haul code information set up on the quote. If this is not an active quote, or no haul code information is set up, then this field defaults the haul code defined for material in HQ Materials. Otherwise, this field defaults blank.

## Haul Basis

Enter
 the basis on which to calculate haul charges. Defaults a value based on the haul rate
 specified for the haul code (in MS Haul Codes). If haul rate basis is: If pay rate basis
 is:

- Per Unit, Units/Mile, or Units/Hour – Defaults as 0.00 (no material units on which to base calculation).

- Hourly – Defaults the posted hours.

- Per Load – Defaults the posted loads.

- If haul charges are based on values entered with the
 revenue or pay code (i.e., the Use EM Revenue/Hauler Pay Amounts
 box is checked in MS Haul Codes), this field will automatically default the revenue
 or pay basis and will be disabled.

- If you checked the Update Actual Units
 From MS box for the specified job in JC Jobs, units (haul basis)
 posted to a job-related timesheet will only be updated to JCCD (Cost Detail). If
 option is unchecked, units will be set to 0.00 in JCCD.

##  Haul Rate

 Enter
 the rate (per unit) at which to calculate haul charges.
 If an active quote exists for the purchaser, haul rate will default from quote based on information for this haul line. If no override rate is found, or no quote exists, will default the haul rate defined for the haul code in MS Haul Codes.
Note: If haul charges are based on values entered with the revenue or pay code (“Use EM Revenue/Hauler Pay Amounts” option in MS Haul Codes), this field will automatically default the revenue or pay rate and will be disabled.
 The unit cost (haul rate) posted to a
 job-related timesheet will only be updated to JCCD (Cost Detail) if you have checked the
 Update Actual Units From MS option for the specified job in JC Jobs. If option is
 unchecked, unit cost will be set to 0.00 in JCCD.

##  Haul Charge

 Enter the total charge for hauling this material. Initially defaults an amount based on the haul basis x haul rate or the minimum amount specified for the haul code (in MS Quotes or MS Haul Codes) if the haul basis is greater than 0.00 and the calculated haul charge is less than the minimum amount. Overriding the default will cause the system to recalculate the haul rate.
Note: If haul charges are based on values entered with the revenue or pay code (“Use EM Revenue/Hauler Pay Amounts” option in MS Haul Codes), this field will automatically default the revenue or pay total and will be disabled.

##  Revenue Code

 Used only when Hauler Type is ‘Equipment’.Optional
 Specify the revenue code (from EM Revenue Codes) to which equipment usage will be posted, and by which equipment revenue will be calculated.Defaults the revenue code assigned to the equipment in EM Equipment.
Note: If revenue code is unit-based, and hours were posted to this time sheet, both work and time units will be updated to the EM Revenue Detail table (EMRD). In addition, the posted hours will be updated to the equipment's hour meter. If the revenue code is hourly based, only time units will be updated to EMRD.

##  Revenue Basis

 Used only when Hauler Type is ‘Equipment’.
 Enter the basis on which to calculate equipment revenue. Defaults a value based on the revenue basis defined for the revenue code in EM Revenue Codes.

- If the revenue basis is ‘Hour’, defaults a value based on the posted hours divided by the revenue code’s hours/time unit. For example, if the Hours/Time Unit is 8.00 and 12 hours were posted, the revenue basis would be 1.5.

- If the revenue basis is ‘Unit’, defaults the posted material units.

Note: If revenue charges are based on values entered with the haul code (i.e. ‘Based on MS Haul Charge” option is checked in EM Revenue Codes), this field automatically defaults the haul basis and is disabled.
 If haul charges are revenue based, the haul basis will default from this value. In addition, if the equipment has attachments, and the attachment is flagged to receive revenue (in EM Equipment, Comp/Attach tab), the system will automatically calculate revenue and haul charges for the attachment as well.

##  Revenue Rate

 Used only when Hauler Type is ‘Equipment’.
 Enter the basis on which to calculate equipment revenue. Defaults a value based on the revenue basis defined for the revenue code in EM Revenue Codes.

- If the revenue basis is ‘Hour’, defaults a value based on the posted hours divided by the revenue code’s hours/time unit. For example, if the Hours/Time Unit is 8.00 and 12 hours were posted, the revenue basis would be 1.5.

- If the revenue basis is ‘Unit’, defaults the posted material units.

Note: If revenue charges are based on values entered with the haul code (i.e. ‘Based on MS Haul Charge” option is checked in EM Revenue Codes), this field automatically defaults the haul basis and is disabled.
 If haul charges are revenue based, the haul basis will default from this value. In addition, if the equipment has attachments, and the attachment is flagged to receive revenue (in EM Equipment, Comp/Attach tab), the system will automatically calculate revenue and haul charges for the attachment as well.

##  Revenue Total

 Used only when Hauler Type is ‘Equipment’.
 This field defaults the total revenue for this piece of equipment (revenue basis x revenue rate). You may override this amount if you have checked the ‘Allow Rate Change’ option in EM Company Parameters (Usage tab) and you have specified to ‘Allow Posting Override’ in EM Revenue Rates by Category or EM Revenue Rates by Equipment. Overriding this amount will cause the system to recalculate the revenue rate.
Note: If revenue charges are based on values entered with the haul code (i.e., you have checked the ‘Based on MS Haul Charge’ option in EM Revenue Codes), this field automatically defaults the haul total and is disabled, regardless of whether you specified to allow rate changes and posting overrides.
 If haul charges are revenue based, the haul total will default from this value. In addition, if the equipment has attachments, and the attachment is flagged to receive revenue (in EM Equipment, Comp/Attach tab), the system will automatically calculate revenue and haul charges for the attachment as well.

##  Pay Code

 Used only when Hauler Type is ‘Haul Vendor’.Optional
 Specify the pay code (from MS Pay Codes) that will be used to determine the haul vendor’s payment. Defaults the pay code assigned to the vendor/truck in MS Vendor Trucks.

##  Pay Basis

 Used only when Hauler Type is ‘Haul Vendor’.
 Enter the basis on which to calculate the haul vendor’s payment. Defaults a value based on the pay rate basis defined for the pay code (in MS Pay Codes). If pay rate basis is:

- Per Unit, Units/Mile, or Units/Hour – Defaults to 0.00 (as there are no material units on which to based the calculation).

- Hourly – Defaults the posted hours.

- Per Load – Defaults the posted loads.

- Percent of Haul Charge – Defaults the posted haul charge.

##  Pay Rate

 Used only when Hauler Type is ‘Haul Vendor’.
 Specify the rate per haul unit that will be paid to the haul vendor for these haul charges. Defaults the pay rate as follows:

- If a quote exists, uses the pay rate defined on the quote

- If no override pay rate defined or no quote exists, uses the standard pay rate defined in MS Pay Codes.

Note: If you change the pay code or pay total for this entry, this rate will be recalculated.

##  Pay Total

 Used only when Hauler Type is ‘Haul Vendor’.
Enter the total amount to pay the haul vendor. Initially defaults an amount based on the pay basis x pay rate or the minimum payment amount specified for the pay code (in MS Quotes or MS Pay Codes) if the pay basis is greater than 0.00 and the calculated payment amount is less than the minimum payment amount. Overriding the default will cause the system to recalculate the pay rate.

## Tax Type

Specify the tax type for this hauler time sheet.

- 1-Sales

- 2-Use

- 3-VAT (Value Added Tax)

For Job and Inventory sales, this field defaults as 2-Use. For Customer sales, this field defaults based on the Default Country specified for the active company in HQ Company Setup:

- If Default Country is US, defaults as 1-Sales.

- If Default Country is not US(e.g. AU, CA, etc.), defaults as 3-VAT.

You may override the default as necessary.

## Tax Code

Specify the tax code (from HQ Tax Codes) to use for calculating taxes on
 this line’s haul charges.
Initially defaults from AR Customers, JC Jobs,
 or IN Locations, depending on the Tax Option selected in MS Company Parameters. If the tax
 code default is based on sale type and purchaser and a quote exists for the purchaser
 (Customer, Job, or Location), the tax code will default from the quote. If no tax code is
 specified on the quote or no quote exists, tax code will default from AR Customers, JC
 Jobs, or IN Locations, depending on the purchaser.
Note: Entering a value here does not guarantee automatic calculation of taxes. Taxes will only be calculated for haul charges if both of the following conditions are met:

- The haul code is flagged as taxable in MS Haul Codes.

- The Haul Tax Option for the sale
 location or purchaser (depending on Tax Option in MS Company Parameters) is set to
 1-Taxable using Haul Vendor or 2-Always Taxable (if using a haul vendor) or
 2-Always Taxable (if using own equipment).

## Tax Basis

Enter the amount on which to calculate taxes for this haul line. Initially defaults the haul charge value. May be overridden.
Note: If haul charges are not taxable, this field defaults to 0.00 and is disabled.

## Tax Amount

This is the total amount of tax calculated for
 this haul line (tax basis x tax rate). If the Tax Type is 1-Sales or 3-VAT, this is the
 amount that will print on the invoice. If the Tax Type is 2-Use, this is the amount
 that will be accrued and paid later to the appropriate taxing authority.

##  Discount Type

 For Customer sales only.
 Display only, the discount type for this customer, based on the assigned payment terms, payment terms type, and material payment discount type.

- If payment terms are material based (i.e.,
 Discount
 Based on Material box is checked in HQ Payment Terms), default will be
 'Rate', ' Unit', or 'None', depending on the material’s payment discount type (in HQ
 Materials).

- If payment terms are rate based (i.e.,  Discount Based on
 Material box is unchecked in HQ Payment Terms), default will be
 'Rate'.

## Discount Basis

For Customer sales only.
This is the amount on which the payment discount offered will be calculated for this haul line.

- If the payment terms are rate-based, default will be
 the haul charges.

- If payment terms are material-based, default will be zero.

Note: If the Payment Terms selected in AR Customers have no
 Discount Date (i.e., None is selected for Discount Date
 in HQ Payment Terms), then this Discount Basis field is unavailable for editing.

## Discount Rate

For Customer sales only.
This number is the rate or amount per unit used to calculate the discount offered for this haul line. The number will default based on the Payment Terms assigned to the customer in AR Customers.

- If the Payment Terms are rate-based (i.e., the
 Discount
 based on Material checkbox is unchecked in HQ Payment Terms), the
 default will be the rate specified in HQ Payment Terms. 

- If the Payment Terms are material-based (i.e., the
 Discount
 based on Material checkbox is checked in HQ Payment Terms), rate will
 default to zero.

Note: If the Payment Terms selected in AR Customers have no
 Discount Date (i.e., None is selected for Discount Date
 in HQ Payment Terms), then this Discount Rate field is unavailable for editing.

##  Discount Offered

 For Customer sales only.
 The total amount of discount offered for early payment on this ticket. Default is the [discount basis](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/ms-hauler-time-sheet-entry-form/field-definitions-ms-hauler-time-sheet-entry-form#ID-0001b78f--en) x [discount rate](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/ms-hauler-time-sheet-entry-form/field-definitions-ms-hauler-time-sheet-entry-form#ID-0001b79c--en).
The default may be overridden. In this case, the [tax discount](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/ms-hauler-time-sheet-entry-form/field-definitions-ms-hauler-time-sheet-entry-form#ID-0001b7b8--en) will be recalculated, but discount basis and discount rate will not be recalculated.
Note: If the Payment Terms selected in AR Customers have no
 Discount Date (i.e., None is selected for Discount Date
 in HQ Payment Terms), then this Discount Offered field is unavailable for editing.

##  Tax Discount

 For Customer sales only. Use only when the
 Allow TaxDisc on
 Invoices & Receipts checkbox in AR Company Parameters is checked.
 The total amount of sales tax that will be credited off the customer’s payment if the discount offered is taken. Default is the tax rate x discount offered.
Note: If the Payment Terms selected in AR Customers have no
 Discount Date (i.e., None is selected for Discount Date
 in HQ Payment Terms), then this Tax Discount field is unavailable for editing.

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
Specify the tax code to use for calculating
 taxes on payments to the haul vendor. Initially defaults the tax code specified for haul
 charges (in the Tax
 Code field above). May be overridden.

## Haul Pay Tax Amt

Enabled for Australia and Canada only (i.e.
 the Default
 Country in HQ Company Setup is AU or CA); used only when Hauler Type is
 set to Haul Vendor.
Specify the total amount of tax to apply to the haul vendor payment or accept the default calculation (pay total x tax rate).
Note: The default calculation may be overridden; it will not affect the vendor payment amount.
