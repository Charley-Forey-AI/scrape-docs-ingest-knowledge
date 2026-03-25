---
title: "Updates to GL | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/updates-to-gl"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/updates-to-gl"
---

# Updates to GL

When you capture work completed for an SM work order and process invoices for customer
 billing, the system updates information to the related module (where applicable) and General
 Ledger.
The updates to General Ledger are controlled
 by the interface settings defined in SM Company Parameters and the GL Interface levels
 defined in the related modules.

- To interface work completed data to related modules, you must check the appropriate
 interface boxes on the Interfaces tab. Interface options include EM, IN, JC, PR, and
 JC.Note: If you are using the Purchase Order module (PO), the system
 automatically updates PO when you post a PO batch using SM Purchase Order Entry.
 Therefore, no interface setting is required.

- For updates to General Ledger, you must define the interface levels in the related
 modules (based on work completed line type) as follows:

- Equipment / Miscellaneous / Inventory — The [GL Usage Interface](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#ID-0004296a--en) level in SM Company Parameters must be Summary or Detail.

- Labor — You must select the [Interface PR to GL](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form/field-definitions-pr-company-parameters-form#ID-00035878--en) checkbox in PR Company Parameters. When PR Ledger Update is run, a
 summarized entry is posted to GL for each applicable account.

- Purchase — You must set the [GL Expense Interface Level](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipt-expense-initialize-form/field-definitions-po-receipt-expense-initialize-form#ID-0002fd3c--en) to Summary or Detail in PO Receipt Expense Initialize (accessed by selecting
 File > Initialize Expenses on Receipt in PO Company Parameters).

Note: If the work completed lines are for a job-related work order, then in
 addition to the settings discussed above, the JC interface flag must be
 checked to update the costs to JC. The GL accounts updated will come from JC
 Departments based on the phase/cost type specified on the work order.

When you capture work completed, the system
 updates the related module and creates entries in General Ledger. When this update occurs,
 the GL accounts affected depend on the work completed line type, the department assigned to
 the service center on the work order, and the offset accounts defined for the related
 module.
The system will also update General Ledger
 when you post invoices as follows:

- Customer Work Orders - An additional GL update occurs when the work completed line
 is invoiced via SM Invoice Review. When you post an invoice batch, the system creates
 GL entries using the Revenue account or Revenue WIP account (if tracking WIP) defined
 for the work completed line, with offsetting entries to the Revenue GL account
 defined for the receivable type in AR Receivable Types.

- Flat Price Work Orders - The update to GL occurs when you bill the work order scope,
 rather than work completed lines. Work completed lines are not billable, as they are
 included in the flat price amount. You will generally only enter work completed for
 flat price scopes if you need to capture the related costs. In this case, updates to
 GL will occur for the incurred costs, but no additional revenue updates will
 occur.

- Job-related Work Orders - Billing is handled via Job Billing or Accounts Receivable
 (if not using Job Billing). The system will perform the standard GL updates defined
 for those modules.

If you track WIP for call types, the system
 performs one additional update to GL upon completing a scope. The amount posted to the Cost
 WIP account will be moved to the Cost account defined for the line type, and the amount
 posted (during invoicing) to the Revenue WIP account will be moved to the Revenue account
 defined for the line type.

Related concepts

- [GL Updates: Work Completed](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed)

- [GL Updates: Flat Price Work Orders](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-flat-price-work-orders)

Related tasks

- [Set the Interface Options for an SM
 Company](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/set-the-interface-options-for-an-sm-company)
