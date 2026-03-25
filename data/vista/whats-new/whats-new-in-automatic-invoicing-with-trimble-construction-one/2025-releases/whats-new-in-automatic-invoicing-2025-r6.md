---
title: "What's New in Automatic Invoicing 2025 R6 | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-automatic-invoicing-with-trimble-construction-one/2025-releases/whats-new-in-automatic-invoicing-2025-r6"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-automatic-invoicing-with-trimble-construction-one/2025-releases/whats-new-in-automatic-invoicing-2025-r6"
---

# What's New in Automatic Invoicing 2025 R6

This release adds several quality of life enhancements to
 Automatic Invoicing as
 well as a temporary fix for a known issue with PO number field length.

## Move an Invoice to Another Batch

You can now change which batch an invoice is assigned to when processing an invoice.
 For more information, see [Process Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/automatic-invoicing-for-trimble-construction-one-users/process-invoices).

## Thumbnail Resizer Feature

You can now change the default thumbnail size when preparing an invoice. For more
 information, see [Prepare Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/automatic-invoicing-for-trimble-construction-one-users/prepare-invoices).

## Export .csv Reports

You can now easily export processing or completed invoices as a .csv file in Trimble Construction One.
For more information, see [Export Invoice Data](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/automatic-invoicing-for-trimble-construction-one-users/export-invoice-data).

## Custom Date Ranges for Inbox & Completed Pages

Automatic Invoicing has a new date
 picker that includes the ability to add custom date range on the Inbox and Completed
 page. It also allows you to select dates outside of the currently selected
 month.

## Hotfix for PO Number Field Length

Since the previous release, a hotfix has been applied to
 mitigate a mismatch between PO Number field lengths in Vista AP Unapproved Invoice Entry (10
 characters) and PO Purchase Order entry (30 characters).
With this hotfix, Automatic Invoicing will:

1. Remove any Purchase Orders with numbers longer
 than 10 characters from both manual and automatic selection.

1. Remove the Purchase Order number when a user
 selects Retry All Errored on the Completed page.

If you previously had invoices that did not send to Vista
 due to a String or binary data would be truncated error,
 please go to the Completed page and select Retry All Errored
 on the affected batches. The invoices should send to Vista correctly, but the PO Number will
 remain blank.
When the length mismatch issue in Vista is resolved, we will revert this
 change.
