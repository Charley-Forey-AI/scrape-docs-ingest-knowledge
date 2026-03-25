---
title: "About Entering Haul Charges with Tickets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets"
---

# About Entering Haul Charges with Tickets

If you have haul charges associated with sales of materials to customers, jobs, and inventory, you can enter them with tickets in MS Ticket Entry.
 You might typically use MS Ticket Entry to enter unit-based haul charges and MS Hauler Time Sheet Entry for hourly-based haul charges; however, you can enter all haul charges with tickets if you prefer.
When entering haul charges, you must specify whether you are posting haul charges to your own equipment or to an outside haul vendor and enter the associated vehicle information.
You can also enter start and stop times, mileage, number of loads, and/or gross and tare weights. If you are using weight to determine the material units sold, enter the weight information. If you are not using weights to calculate material units, the system will use the loads and vehicle capacity information to calculate the material units sold. For detailed information on the calculation of material units, see [Material Units](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/material-units).

- Using a Haul Vendor - If entering haul charges for a haul vendor, the screen displays additional fields for entry of payment information. This includes the pay code, pay basis, pay rate, and pay total. The system uses this Pay code information when initializing vendor payments in MS Haul Payment Worksheet.

- If you defined a minimum payment amount for the pay code (in MS Pay Codes or MS Quotes), that amount defaults as the pay total when the pay basis is greater than 0.00 and the calculated payment amount is less than the minimum amount.

- If you elected to remove vendor payment information from the ticket entry screen (in MS Company Parameters, Ticket Entry tab), the vendor payment fields will not display in MS Ticket Entry. However, if you have assigned pay codes to vendor trucks in MS Vendor Trucks, a pay code will default for the transaction and a payment amount calculated based on the pay code and pay rate.

- Haul Charge Taxes - Taxes are calculated for haul charges if the haul code is designated as subject to sales tax (US) or value added tax (Australia and Canada) and the Haul Tax Option is set to 1-Taxable Using Haul Vendor or 2-Always Taxable in MS Quotes if quote exists for purchaser, or in AR Customers, JC Job Mater/PM Projects, or IN Locations if no quote exists for purchaser. If you are not applying taxes to the material specified on the ticket, the tax Basis and Total fields represent the tax values for haul charges. However, if you are applying taxes to the material, the tax Basis and Total fields represent both the material and haul tax values.Note: You can override the tax basis or tax amount if necessary. If you override the tax basis, the system will recalculate the tax amount accordingly; however, if you override the tax amount, the system will not recalculate the tax basis.

- Haul Payment Taxes (Australia and Canada) - You have the ability to calculate taxes on haul payments to a vendor when entering tickets. If the Default Country in HQ Company Setup is AU (Australia) or CA (Canada), the screen displays additional fields to allow entering the haul pay tax type, code, and payment amount. The haul pay tax amount (tax rate x pay total) is included when processing haul payments in MS Haul Payment Worksheet.Note: If you prefer to use MS Hauler Time Sheet Entry for entering haul charges, you can enter haul pay tax information there instead.

- Using Your Own Equipment - If you are posting haul charges to your own equipment, the form displays additional fields for entering revenue information. These fields will not display if you selected the EM Revenue Info checkbox in MS Company Parameters (Remove From Ticket Entry section). A revenue code still defaults for the transaction if you assigned one to the specified equipment, and a revenue amount calculates based on the revenue code and rate. The system posts equipment usage and revenue to the equipment in EM if you have set the Equipment Revenue interface level to Summary or Detail in MS Company Parameters (Ticket Updates tab).Note: If the revenue code is hourly based, only time units (hours) are updated to EM Revenue Detail (EMRD). However, if you are posting hours and the revenue code is unit-based, the system updates both work units and time units to EMRD.

- Posting Haul Revenue to Attachments - If the equipment used to haul the materials has an attachment, and you flagged the attachment to receive posted revenue, then the system creates a separate sequence for the attachment when the ticket is validated. Although the sequence is created upon validation, it will not display in the Batch Detail grid until the form is exited and re-entered. You can do this quickly by selecting the Batch Process option in the File menu, then canceling out of the form.

Once you have invoiced tickets with haul charges in Accounts Payable (via MS Haul Payment Worksheet), it is recommended that you do not edit them. However, if you must edit the tickets, limited edits are allowed. For more information, see [About Editing and Deleting Tickets](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-editing-and-deleting-tickets).

Related information

- [About the MS Ticket Entry Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form)

- [About Posting Haul Charges to Attachments](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets/about-posting-haul-charges-to-attachments)

- [Base Haul Charges on Revenue or Pay Code](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets/base-haul-charges-on-revenue-or-pay-code)

- [Base Revenue on Haul Charges](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets/base-revenue-on-haul-charges)

- [About Linking Equipment Revenue to Haul Charges](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets/about-linking-equipment-revenue-to-haul-charges)
