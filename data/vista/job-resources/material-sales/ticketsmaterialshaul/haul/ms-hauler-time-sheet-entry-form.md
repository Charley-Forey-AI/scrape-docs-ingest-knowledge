---
title: "MS Hauler Time Sheet Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/ms-hauler-time-sheet-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/ms-hauler-time-sheet-entry-form"
---

# MS Hauler Time Sheet Entry Form

Use the MS Hauler Time Sheet Entry form to record the daily activity of either your own equipment or the independent haul vendors used to deliver materials.
Entry of haul information in this form is similar to that of the MS Ticket Entry, with the exception that material units, unit price, and material total information is not included.
Typically, this form is most useful if you frequently deal with hourly-based haul charges, payment rates, and/or equipment revenue, and use some form of hauler sheet to track and enter haul charges after you post material tickets. If haul information is normally included with the material tickets (that is, haul charges, payment rates, and equipment revenue are unit based), then you may not need to use this form.
Note: If you are posting hours and the revenue code is unit-based, both work units and time units are updated to the EM Revenue Detail table (EMRD). If the revenue code is hourly based, only time units (hours) are updated to EMRD.

All of the information entered here is available for updates to Job Cost (hauling expense posted to jobs) and Equipment Management (equipment revenue from usage), as well as Accounts Receivable (haul charges posted to customers), and Accounts Payable (hauler payments), just as if it were posted in MS Ticket Entry.
It is expected that tickets uploaded from a scale package or manually entered in the system will generally be posted prior to the hauler's time sheet. This allows you to verify tickets as you make entries here (Tickets button to the right of the header). For more information, [Ticket Verification](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/ticket-verification).
The Remove From Haul Sheet Entry section in MS Company Parameters (Haul Sheets tab) determines what fields will display on the hauler time sheet entry screen. When the box is checked for an option, all corresponding fields are removed from the time sheet entry screen.

## Taxes

Taxes are calculated for haul charges if the haul code is designated as subject to sales tax (US) or value added tax (Australia and Canada) and the Haul Tax Option is set to 1-Taxable Using Haul Vendor or 2-Always Taxable in MS Quotes (if quote exists for purchaser), or in AR Customers, JC Job Mater/PM Projects, or IN Locations (if no quote exists for purchaser).
Note: If you override the tax basis, the system recalculates the tax amount accordingly; however, if you override the tax amount, the system will not recalculate the tax basis.

You can also calculate taxes on haul payments to a vendor when entering time sheets. If the Default Country in HQ Company Setup is AU (Australia) or CA (Canada), the screen displays additional fields to allow entering the haul pay tax type, code, and payment amount. The haul pay tax amount (tax rate x pay total) will be included when processing haul payments in MS Haul Payment Worksheet.
Note: If you prefer, you can enter haul charges and haul pay tax information in MS Ticket Entry.

## Equipment Attachments

If you enter haul information for your own equipment and the equipment used to haul the materials has an attachment, you can post haul revenue to the attachment. The attachment must be flagged to receive posted revenue in EM Equipment (Comp/Attach tab). Then, when you enter a time sheet that references the equipment associated with the attachment, the system creates a separate sequence for the attachment with just the revenue amounts. Although the sequence is created upon validation of the time sheet, it is not displayed until the form is refreshed (Records menu).
Note: You have the option to base your equipment revenue on haul charges or have haul charges based on the equipment revenue. These options are controlled by haul code and/or revenue code setup options. For more detailed information, see [About Linking Equipment Revenue to Haul Charges](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets/about-linking-equipment-revenue-to-haul-charges).

If you calculate haul charges based on revenue and you are using equipment with attachments, you can have the revenue posted to the attachment passed through as a charge to the job, customer, or purchasing inventory location along with the equipment. To accomplish this, you must flag the attachment to receive revenue when posting revenue to the primary piece of equipment (in EM Equipment, Comp/Attach tab). In addition, any revenue codes you will use when entering haul charges for the primary piece of equipment must also be set up for the attachment (in EM Revenue Rates by Equipment and/or EM Revenue Rates by Category). When you enter revenue-based haul charges for the equipment, the system automatically calculates haul charges for the attachment as well, based on the attachment's revenue values.

Related information

- [About the MS Haul Add Transaction Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-haul-add-transaction-form)

- [About the MS Hauler Time Sheet Tickets Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/about-the-ms-hauler-time-sheet-tickets-form)
