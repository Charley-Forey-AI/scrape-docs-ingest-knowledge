---
title: "PO Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form"
---

# PO Company Parameters Form

Use this form to set up PO companies for processing purchase orders and requisitions.

When you set up a PO company, it is important that you understand the effects of all choices for each setup option, as they can affect processing in the Purchase Order module. It is recommended that you restrict this form so only the System Administrator has access to it.
You generally won't need to make changes to this form after the initial setup; however, if you do need to make changes later, please use caution, as modifying these options may affect processing or stored data. If you're unsure how a change will affect existing data, please contact ViewpointSupport before proceeding.
Note: Each PO company that you set up must have a corresponding Accounts Payable company with the same number.

## Audit Options

Audit options allow you to track changes to selected data. For each PO company you set up, you can track purchase order information and requisition information. For more information about purchase order and requisition audit options, see the F1 Help.

## Interface Levels

 Interface Levels are are displayed in the Update GL/Sub-Ledgers on Receipt section. With the exception of the GL Expense Interface option, PO interface levels are set via the PO Receipt Expense Initialize form (accessed by selecting File > Initialize Expenses on Receipt). For more information about these settings, see [Set or Change PO Interface Levels](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/set-or-change-po-interface-levels)

## Requisition Approval Options

The PO module enables you to assign reviewers to requisitions, enabling an approval process. If you want to enforce the approval process, you can have the system enforce the approval process for both quote and purchase lines.

## Close Exceptions

The PO Close JC Exceptions and PO Close SM Exceptions tabs list the JC cost types and SM Cost Types (respectively) that will be excluded from auto-closing of purchase orders. These tabs are only enabled for entry if you have selected the Auto Close Purchase Orders on Final Invoice checkbox (Info tab). For more information, see [Auto Close Purchase Orders on Final Invoice](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form/field-definitions-po-company-parameters-form#concept-9016--en).
