---
title: "Audit Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-batch-process-form/audit-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-batch-process-form/audit-reports"
---

# Audit Reports

The following audit lists are available when processing Service Management batches. If an option is disabled, it means that particular list is not available for the current batch. Additionally, only lists with the checkbox marked can be previewed or printed.
Available audit reports:

- Batch List - The audit report
 available will depend on the type of transactions in the batch.

- SM Miscellaneous Batch List -
 This report prints when posting miscellaneous work completed transactions (Source of
 SMLedgerUp). Entries in the batch are sorted by work order and scope. Information
 shown will depend on the GL Usage Interface level defined in SM Company Parameters.

- SM Equipment Usage Batch List
 - This report prints when posting equipment work completed transactions (Source of
 SMEquipUse). Entries in the batch are sorted by work order and scope. Information
 shown will depend on the GL Usage Interface level defined in EM Company Parameters,
 and may include the date, equipment, work unit of measure and units, time unit of
 measure and units, revenue rate, and amount.

- SM Inventory Usage Batch List
 - This report prints when posting transactions for work completed inventory (type
 4-Inventory). Entries in the batch are sorted by work order and scope. Information
 shown will depend on the GL Adjustment Interface level defined in IN Company
 Parameters, and may include the date, IN company and location, material and
 description, UM, quantity, unit cost, total cost, and stock cost

- Distribution Report - Prints the SM GL Distribution List for the current batch, showing the general ledger distributions for each affected GL account.

- Error Report - Lists the sequence number and the error message for any entries where errors were found in the validation process. You must correct the errors before you can post the batch.

Note: Users who have access to batch processing forms do not
 automatically have access to the related audit reports. It is recommended that if they will
 be processing batches, you give them access to the related audit reports using VA Report
 Security. If users do not have access, they will receive an error message when trying to
 preview/print those reports to which they do not have access. In addition, if you have
 checked the Attach
 Batch Report to HQ Batch Control box in SM Company Parameters, restricted
 access to one or more audit reports will prevent the user from posting the batch.
