---
title: "Generate & Process Agreement Billings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/generate--process-agreement-billings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/generate--process-agreement-billings"
---

# Generate & Process Agreement Billings

Agreement billings are generated automatically based on the billing schedules defined for the agreement in SM Agreement Billing Schedules.

- Before you begin creating invoices, you must assign a receivable type in one of the following locations: SM Company Parameters, AR Customers (for the Bill To customer), or AR Company Parameters.The system assigns the receivable type during batch processing. The receivable type associated with each invoice determines the General Ledger accounts updated during processing.

- If you have periodic services defined on the agreement that are flagged for separate billing, you must set up billing schedules for the applicable services (using [SM Service](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form), Billing Schedule tab). Once you define your billing schedules, you can then use SM Agreement Billings Due to identify agreements due for billing and then initiate an invoice session for selected agreements.

 Once you create an invoice session, you can use SM Agreement Invoice Review to edit, preview, and process the invoice(s). The following steps will guide you through this process.

1. From the main menu, open the SM Agreement Billings Due form.

1. In the Search Criteria section, enter the Customer and/or Agreement Type by which to filter agreements due for billing, or leave one or both blank to include all customers and/or agreement types.

1. In the Due Within the Next ___ Days field, enter the number of days by which to filter agreements.

1. Click Search. The system refreshes the grid to display only those agreements that meet the search criteria.

1. Select the agreements you want billed in this session by either manually checking the Create box for each applicable agreement in the grid or by clicking the Check All button.Note: You can manually deselect agreements you do not want billed once you click the Check All button.

1. Click Launch Invoice Review. The system generates invoices for selected agreements and displays the SM Agreement Invoice Review form.

1. The header fields default values based on the customer's setup (in AR Customers). You should not need to change these values; however, with the exception of the Seq field, you can change the default values as needed. For more information about these fields, see the F1 help.

1. Preview the invoices.You can click Preview (to the right of the Invoice Summary Level field to preview the selected invoice or click Preview All (bottom of screen) to preview all invoices in the session.

1. Process the invoices.

1. Click Process. The AR Batch Process form displays

1. Click Validate. The system validates the information and generates the applicable batch reports.

1. Review and print batch reports (recommended).

1. In the Posting Date field, enter the date to which invoices are to be posted. Initially defaults to the current date.

1. Click Post to initiate the posting process. The system will process each batch entry and make all the necessary transaction updates. In addition, each invoice is updated to a status of Invoiced (from Pending) and any related work completed lines are updated with a status of Billed

1. [Edit the Recipients list for invoice delivery (optional)](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/edit-the-recipients-list-for-sm-invoices).

1. [Add attachments for invoice delivery via email (optional).](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/addselect-attachments-for-sm-invoice-delivery)

1. Click the Deliver button.Note: If you are not ready to deliver the invoice, you can do so later via the [SM Invoices](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoices-form) form.

 Once you process an invoice, it is available for payment in AR Cash Receipts. You can reprint invoices at any time using the custom reports you chose for each invoice, the SM Agreement Invoice report (if no custom report was used), or the AR Invoice report (this option only available for processed invoices).
