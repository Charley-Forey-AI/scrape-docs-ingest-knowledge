---
title: "Field Definitions: MS Haul Ticket Add-Ons Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-ticket-add-ons-form/field-definitions-ms-haul-ticket-add-ons-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-ticket-add-ons-form/field-definitions-ms-haul-ticket-add-ons-form"
---

# Field Definitions: MS Haul Ticket Add-Ons Form

The following is a list of field descriptions for the MS Haul
 Ticket Add-Ons form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq #

Enter N, NEW, or + to create a new entry, or enter the
 batch sequence number of an existing entry to display.

##  From Loc

 Specify the 'sales' location from the existing ticket. This must be a valid IN Location.

##  Ticket #

 Specify the ticket number for this add-on haul charge. The entry must be an existing ticket number. Press F4 for a list of existing ticket numbers for the sales location.

## Orig MS Trans

Specify the transaction number of the ticket for this add-on haul charge.
Note: If the original ticket specified a piece of equipment with attachments, and the attachments are flagged for revenue posting (EM Equipment), there will be a transaction for the primary piece of equipment, as well as transactions for each attachment. You will generally want to select the transaction for the primary piece of equipment.

##  Haul Code

 Specify the haul code to use for this add-on haul charge. The entry must be a valid haul code (from MS Haul Codes).

##  Start

 Enter the start time in 24-hour format. If the haul code is hourly based, the system uses this time in conjunction with the Stop time to determine the haul basis default.

## Stop

Enter the stop time in 24-hour format. If the haul code is hourly based, the system uses this time in conjunction with the Start time to determine the haul basis default.
Note: If the stop time is less than the start time, stop time is assumed to be on the following day. So, if start time is 17:00 (5:00 p.m.), and the stop time is 02:00 (2:00 a.m.), the total hours will be 9.

##  Hours

 This field initially defaults the total number of hours, based on the start and stop times. You can override this field, but the Start and Stop fields will not update.

##  Zone

 Enter the haul zone for this haul, up to 10 characters. This value may be used to determine haul and pay rates.
 If a quote exists for the purchaser, and a haul zone is defined on the quote for the sales location, that haul zone will default here.

##  Haul Phase

 For Job sales only.
 Enter the phase for expensing the add-on haul charge. This field initially defaults the haul phase from the associated ticket.

##  Haul CT

 For Job sales only.
 Enter the cost type for expensing the add-on haul charge. This field initially defaults the haul cost type from the associated ticket.

## Haul Basis

Specify the basis for the add-on haul charge. If the specified haul code is hourly based, this field will default a value based on the Start and Stop times. Otherwise, enter the haul basis manually, up to 8 digits and 3 decimals.
Note: If haul charges are based on values entered with the
 revenue or pay code (i.e., Use EM Revenue/Hauler Pay Amounts box is
 checked in MS Haul Codes), this field automatically defaults the revenue or pay basis and
 will be disabled.

## Haul Rate

Enter the rate to calculate the add-on haul charge.
If an active quote exists for the purchaser, and an override rate has been defined for the specified haul code (matching information set up on ticket), haul rate will default from the quote. Otherwise, the haul rate will default from MS Haul Codes.
Note: If haul charges are based on values entered with the
 revenue or pay code (i.e., Use EM Revenue/Hauler Pay Amounts box is
 checked in MS Haul Codes), this field automatically defaults the revenue or pay rate and
 will be disabled.

## Haul Charge

Enter the total add-on haul charge for this transaction. Initially defaults a value based on the haul basis x the haul rate or the minimum amount specified for the haul code (in MS Quotes or MS Haul Codes) if the haul basis is greater than 0.00 and the calculated haul charge is less than the minimum amount. Overriding the default will cause the system to recalculate the haul rate.
Note: If haul charges are based on values entered with the
 revenue or pay code (i.e., Use EM Revenue/Hauler Pay Amounts box is
 checked in MS Haul Codes), this field automatically defaults the revenue or pay basis and
 will be disabled.

## Rev Code

Used only when the Hauler Type
 specified on the original ticket is E-Equipment.
Specify the revenue code (from EM Revenue Codes) for this add-on haul charge (optional). This is the revenue code to which equipment usage will be posted, and by which equipment revenue will be calculated. Defaults the revenue code assigned to the equipment in EM Equipment.

## Rev Basis

Used only when the Hauler Type
 specified on the original ticket is E-Equipment.
Enter the basis on which to calculate equipment revenue. Defaults a value based on the revenue basis defined for the revenue code in EM Revenue Codes.

- If the revenue basis is Hour, defaults a value based
 on the posted hours divided by the revenue code’s hours/time unit. For example, if
 the Hours/Time Unit is 8.00 and 12 hours were posted, the revenue basis
 would be 1.5.

- If the revenue basis is Units, defaults as 0.00.

- If revenue charges are based on values entered with
 the haul code (i.e., the Based on MS Haul Charge box is
 checked in EM Revenue Codes), this field automatically defaults the haul basis and is
 disabled.

- If haul charges are revenue based, the haul basis will default from this value. In addition, if the equipment has attachments, and the attachment is flagged to receive revenue (in EM Equipment, Comp/Attach tab), the system will automatically calculate revenue and haul charges for the attachment as well.

## Rev Rate

Used only when the Hauler Type
 specified on the original ticket is E-Equipment.
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

## Rev Total

Used only when the Hauler Type
 specified on the original ticket is E-Equipment.
This field defaults the total revenue for this
 piece of equipment (revenue basis x revenue rate). You may override this amount if you have
 checked the Allow
 Rate Change box in EM Company Parameters (Usage tab) and the Allow Posting
 Override box in EM Revenue Rates by Category or EM Revenue Rates by
 Equipment. Overriding this amount will cause the system to recalculate the revenue
 rate.

- If revenue charges are based on values entered with
 the haul code (i.e., you have checked the Based on MS Haul Charge box in EM
 Revenue Codes), this field automatically defaults the haul total and is disabled,
 regardless of whether you specified to allow rate changes and posting overrides.

- If haul charges are revenue based, the haul total will default from this value. In addition, if the equipment has attachments, and the attachment is flagged to receive revenue (in EM Equipment, Comp/Attach tab), the system will automatically calculate revenue and haul charges for the attachment as well.

## Tax Type

Specify the tax type for this transaction. Initially defaults from the specified ticket; may be overridden.

- 1-Sales

- 2-Use

- 3-VAT (Value Added Tax)

## Tax Code

Specify the tax code to use for calculating
 taxes for this add-on haul charge. The tax code initially defaults from the original ticket
 transaction (specified above); however, if no tax code was specified on the ticket, the tax
 code defaults based on the Tax Option specified in MS Company
 Parameters as follows.

- 0-No Tax – Tax code defaults as 'null'; must be entered manually for taxable items.

- 1-Sales Location – Defaults the sales location's tax
 code (from IN Locations)

- 2-Sale Type / Purchaser – Defaults the purchaser's
 tax code (from AR Customers, JC Jobs, or IN Locations). If an override tax code
 exists for the purchaser on a quote, the override tax code is used.

- 3-Sale Type / Purchaser / Sales Location – Defaults
 the purchaser's tax code (from AR Customers, JC Jobs, or IN Locations) or the sales
 location's tax code (if no tax code assigned to purchaser). If an override tax code
 exists for the purchaser on a quote, the override tax code is used.

- 4-Delivery– If materials are delivered, defaults the tax code based on the sales type and purchaser. If materials are not delivered, tax code defaults from sales location.

Note: Entering a value here does not guarantee automatic calculation of taxes. Taxes will only be calculated for haul charges that are flagged as taxable.

##  Tax Basis

 Enter the basis on which to calculate taxes for this add-on haul charge. If haul charge is taxable, defaults the haul charge amount. If not taxable, defaults as 0.00.

##  Tax Amount

 Enter the total amount of tax for this add-on haul charge. Initially defaults calculation of tax basis x tax rate. If the tax type is ‘Sales’ or ‘VAT’, this amount will print on the invoice. If tax type is ‘Use’, this amount will be accrued and paid later to the appropriate taxing authority.

##  Pay Code

 Used only when Hauler Type is ‘Haul Vendor’.Optional
 Specify the pay code (from MS Pay Codes) that will be used to determine the haul vendor’s payment. Defaults the pay code assigned to the vendor/truck in MS Vendor Trucks.

## Pay Basis

Used only when the Hauler Type
 specified on the original ticket is H-Haul Vendor.
Enter the basis on which to calculate the haul vendor’s payment. Defaults a value based on the pay rate basis defined for the pay code (in MS Pay Codes). If pay rate basis is:

- Per Unit, Units/Mile, Units/Hour, or Per Load – Defaults as 0.00 (as there are no material units or loads specified).

- Hourly– Defaults the posted hours.

- Percent of Haul Charge – Defaults the posted haul charge.

## Pay Rate

Used only when the Hauler Type
 specified on the original ticket is H-Haul Vendor.
Specify the rate per haul unit that will be paid to the haul vendor for this add-on haul charge. Defaults the pay rate as follows:

- If a quote exists, uses the pay rate defined on the quote.

- If no override pay rate defined or no quote exists, uses the standard pay rate defined in MS Pay Codes.

Note: If you change the pay code or pay total for this entry, this rate will be recalculated.

## Pay Total

Used only when the Hauler Type
 specified on the original ticket is H-Haul Vendor.
Enter the total amount to pay the haul vendor for this add-on haul charge. Initially defaults an amount based on the pay basis x pay rate or the minimum payment amount specified for the pay code (in MS Quotes or MS Pay Codes) if the pay basis is greater than 0.00 and the calculated payment amount is less than the minimum payment amount. Overriding the default will cause the system to recalculate the pay rate.
