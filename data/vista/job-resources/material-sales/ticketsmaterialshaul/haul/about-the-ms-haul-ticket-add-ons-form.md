---
title: "About the MS Haul Ticket Add-Ons Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-ticket-add-ons-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-ticket-add-ons-form"
---

# About the MS Haul Ticket Add-Ons Form

Use this form to enter add-on haul charges to existing ticket transactions. Although add-on charges are typically "wait time" charges, you can enter any type of additional haul charges.
Note: You can only enter add-ons for tickets with a Haul Type
 of H-Haul Vendor or E-Equipment.
To enter add-on haul charges, specify the selling from location, the ticket for entering the additional haul charges, and the transaction to which the charges apply. Once you enter this information, the Original Ticket Information section displays details about the ticket transaction, including the 'purchaser' (i.e. customer, job, location), the material information (UM, units, unit price, total), the equipment or haul vendor used to haul the material, and the original haul charge information (i.e. haul code, rate, and haul charge).
Use the Info tab to enter the add-on charges. Entry of haul information in this form is similar to that of MS Ticket Entry and MS Hauler Time Sheet Entry. Specify a haul code, the start and stop time, and haul zone (if applicable). The haul basis, rate, and charge default based on the specified haul code. If the haul code is hourly based, the system uses the start and stop times to determine the haul basis. Otherwise, you must enter the haul basis manually. The haul rate is determined using the standard hierarchy; that is, if the haul code exists on a quote for the purchaser, the system uses the quote haul rate. If you did not specify a rate on the quote, the system uses the standard rate defined for the haul code (in MS Haul Codes). If haul charges are based on values entered with the revenue or payment code, the haul basis, rate, and charge values will default from the revenue or pay basis, rate, and charge. For more information, see Related Topics below.

- Entering Revenue/Payment Information - Depending on whether you used your own
 equipment or an outside haul vendor (determined by the original ticket), you
 will also need to enter revenue or payment information for the add-on haul
 charge. If revenue or payment values are based on values entered with the haul
 code (determined by the revenue or pay code), the system disables the basis,
 rate, and amount fields and they will automatically default the revenue or
 payment values.

- Posting Haul Revenue to Attachments - If the equipment used to haul the
 materials has an attachment, and you flagged the attachment to receive posted
 revenue, the system creates a separate sequence for the attachment during add-on
 validation. Although the system creates the sequence upon validation, it will
 not display in the detail grid until the form refreshes. Once you have finished
 entering add-on haul charges, process the batch as normal. Entries made in this
 form will not modify the original transaction. New transactions are created
 using the location, ticket number, sales date, material, etc. (from the original
 transaction), with material quantities and dollars set to 0.00.

- Posting Add-Ons Charges to Attachments - If you are calculating haul add-ons
 based on revenue, and you are using equipment with attachments, you can have the
 revenue posted to the attachment passed through as an expense to the job,
 customer, or purchasing inventory location along with the equipment. In order to
 accomplish this, flag the attachment to receive revenue when posting revenue to
 the primary piece of equipment (in EM Equipment, Comp/Attach tab). In addition,
 any revenue codes you will use when entering haul add-ons for the primary piece
 of equipment must also be set up for the attachment (in EM Revenue Rates by
 Equipment and/or EM Revenue Rates by Category). When entering revenue-based haul
 add-ons for the equipment, the system automatically calculates haul add-ons for
 the attachment, based on the attachment's revenue values.

- Making Changes to Posted Haul Add-Ons - You can only use this form to enter and
 process haul-related add-on charges—it does not allow for changes or deletions
 to add-ons once they post. If you need to change or delete a haul add-on
 transaction, you can do so using MS Ticket Entry. Just pull in the desired
 transaction, make the necessary changes (or flag it for deletion), then process
 the batch as normal.

Related information

- [Haul Charges](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/haul-charges)

- [About the MS Haul Codes Form](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-haul-codes-form)

- [About Posting Taxes](/en/vista/vista/job-resources/material-sales/about-posting-taxes)
