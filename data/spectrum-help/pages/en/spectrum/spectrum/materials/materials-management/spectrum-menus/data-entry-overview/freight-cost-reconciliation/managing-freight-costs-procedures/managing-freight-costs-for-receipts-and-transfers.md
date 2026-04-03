---
title: "Managing Freight Costs For Receipts and Transfers | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/freight-cost-reconciliation/managing-freight-costs-procedures/managing-freight-costs-for-receipts-and-transfers"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/freight-cost-reconciliation/managing-freight-costs-procedures/managing-freight-costs-for-receipts-and-transfers"
---

# Managing Freight Costs For Receipts and Transfers

Use the Managing Freight Costs for
 receipts and transfers procedure when managing freight costs for jobs. The following procedure
 is comprised of two parts: Part A describes how to add scale tickets, which should be done at
 regular intervals as a part of your scale data entry process and Part B describes how to
 reconcile hauler invoices as they arrive.
Before continuing with this procedure, make sure the necessary standard and special default hauler rates are set up in Spectrum.
[Setting Up Hauler Rates (Special vs. Standard)](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/freight-cost-reconciliation/managing-freight-costs-procedures/setting-up-hauler-rates-special-vs.-standard)

## Part A – Recording the Scale Ticket

1. On the Site Map screen, click
 Materials Management > Data Entry > Scale Ticket
 Transactions.

1. Enter a unique Batch code for the batch
 of tickets being entered and press Enter.

1. Click the Add button.

1. In the New/Edit Scale Ticket window,
 enter the Plant code for the ticket location or press
 F4 to select a plant code.

1. Complete the Ticket portion of the
 window. At the Type field, select either
 Receipt or Transfer.

1. Once you have completed the Ticket
 section, the User-Defined Fields windows displays. Complete
 the window as needed, and click OK.

1. The Haul Info window displays. If hauler
 information has been completed in Hauler File Maintenance or
 Job Material Contract Maintenance, freight rate information
 will default. Complete this window for the selected ticket.Note: If special hauler information was designated for the
 selected receipt or transfer, this hauler rate will default. If special pricing
 was not specified, then the standard rate for the selected hauler will
 default.

1. In the detail portion of the screen,
 enter the item(s) hauled for the ticket. Press F4 at the
 Item field to select a valid item code.

1. Repeat step 8 for each additional item hauled on the ticket.
 Once you have completed the ticket, click OK.

1. OPTIONAL: If your company is adding additional hourly
 freight information, click the Frt Hours button and complete
 the Freight Hours Entry screen.

## Completing the Freight Hours Entry screen

1. Click the Update button and complete the
 Scale Ticket Journal screen. Preview the report.

1. The Scale Ticket Update screen displays.
 Once you have verified that information is correct on the report, select the
 Proceed with update checkbox and click
 OK.

## Part B – Reconciling the Invoice in Freight Cost Reconciliation

The Freight Cost Reconciliation screen serves two
 purposes. The first is to adjust or reconcile the freight charged on a ticket-by-ticket
 basis. The second is to group tickets and to create an A/P invoice (after you receive
 the vendor invoice).
This procedure is performed at the time the hauler requests payment. When you receive hauler invoices, compare the amounts being billed with those entered in Spectrum. In most cases, charges should be the same, but there will be charges that need to be reconciled to match the hauler's requested amount. In the event that there is a large discrepancy between the amounts due, then further investigation of the differences may be necessary. If their amount differs from what your company has on file and you accept their amount, then this is recorded here. Additionally, quantities and rates can be changed here as needed.

1. On the Site Map screen, click
 Materials Management > Data Entry > Freight Cost
 Reconciliation.

1. At the Vendor code field, enter the
 vendor code for whom you are reconciling freight costs or press
 F4 to select a vendor code.

1. At the Invoice no field, enter the
 invoice number for the invoice you are reconciling or press F4
 to select an invoice number.

1. At the Invoice date field, the last date
 of the current payment processing cycle displays. Press Enter
 to accept this date or enter a different date.

1. In the detail portion of the screen,
 locate the tickets that are included on the invoice being reconciled and select the
 checkbox in the Include column that corresponds to each of
 these tickets.

1. Make any necessary changes to the ticket in the Rate
 type, Quantity, or Rate
 fields for each ticket.Note: As changes are made to quantity or
 rates on a ticket, Spectrum will automatically calculate the new ticket amount in
 the Charge column. Additionally, if at any time you want to
 view ticket or item detail for a ticket, place the cursor anywhere in the ticket's
 line and click the Ticket or Items
 buttons, respectively.

1. Once you've reconciled all of the tickets for the invoice and
 made any necessary adjustments, click OK twice.

1. Click the Update button.

1. In the Freight Cost Journal / Update
 screen, complete the Selections fields and click
 Preview. Review the reconciliation report for
 accuracy.

1. In the Freight Cost Update screen,
 select Yes, proceed with update and click
 OK.
Once the update is run, Spectrum will create A/P invoices for
 any freight costs listed on the report (except for those tickets with a zero
 balance).

## Optional Part C – Reconciling Freight Hours

The Freight Hours Reconciliation screen is used when
 reconciling the hours for tickets where the "grouping" of tickets for invoicing is of no
 concern. This screen is designed specifically for reconciling the quantity (hours or
 tonnage) on a ticket.

1. On the Site Map screen, click
 Materials Management > Data Entry > Freight Cost
 Reconciliation.

1. Click the Hours button.

1. At the Batch code field, enter the
 batch code you are using to reconcile freight costs or press
 F4 to select a batch code.

1. At the Truck code field, enter the
 truck code for the tickets your are reconciling or press F4
 to select a truck code.

1. Complete the From date and
 To date fields, press F4 to
 select a date using the Date Change window, or press
 Enter to select the default at each field.Note: The From date field defaults to
 blank to include all tickets for the selected truck code; the To
 date field defaults to the current processing date.

1. In the detail portion of the screen,
 locate the tickets that are included on the invoice being reconciled and select
 the checkbox in the Include column that corresponds to each
 of these tickets.

1. Make any necessary changes to the ticket in the
 Freight hours, Rate type, and
 Freight Quantity fields for each ticket.Note: The Freight Quantity field is
 applicable only if Ton is selected in the
 Rate type column.

1. Once you've reconciled all of the tickets for the batch and
 made any necessary adjustments, click OK twice.

1. On the Freight Hours Reconciliation
 Print screen, select the type of tickets you want to preview and
 click Preview.Note: If you select to
 print by Batch, the Additional
 Selections window will display when you print the report
 prompting you for a batch code.
