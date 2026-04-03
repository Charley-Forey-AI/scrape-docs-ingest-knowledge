---
title: "List of Tables Affected by the Assign Cost Centers by Department Utility | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/assign-cost-centers-by-department/list-of-tables-affected-by-the-assign-cost-centers-by-department-utility"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/assign-cost-centers-by-department/list-of-tables-affected-by-the-assign-cost-centers-by-department-utility"
---

# List of Tables Affected by the Assign Cost Centers by Department Utility

Review this list of the tables that are impacted when you run the Assign Cost Centers by Department utility.
Table
Company Code Basis
GL Code Column Basis

GL_BALANCE_MC
Company_Code
GL_Account

^GL_DETAIL_MC
Company_Code
GL_Account

GL_BUDGET_MC
Company_Code
GL_Account

GL_RECUR_JE_DETAIL_MC
Company_Code
GL_Account

CR_GL_HISTORY_MC
Company_Code
GL_Account

CR_HIST_INVOICE_MC
Company_Code
GL_Code

CR_CASH_RECEIPT_GL_HIST_MC
Company_Code
GL_Account

CR_INVOICE_HEADER_MC
Company_Code
AR_GL_Account

CR_INVOICE_DETAIL_MC
Company_Code
GL_Account

CR_OPEN_ITEM_MC
Company_Code

CR_RECURRING_INVOICE_HDR_MC
Company_Code
AR_GL_Account

CR_RECURRING_INVOICE_DET_MC
Company_Code
GL_Account

EC_GL_WORK_HISTORY_MC
+Equipment_Company_Code
GL_Account

EC_RECUR_TRAN_DETAIL_MC
+Company_Code_2
GL_Debit_Account

EC_RECUR_TRAN_DETAIL_MC
Company_Code
GL_Credit_Account

HR_ACCRUAL_HISTORY_MC
Company_Code
Accrual_Debit_Account

IN_INVOICE_HEADER_MC
Company_Code
AR_GL_Account

OE_ORDER_HEADER_MC
Company_Code
AR_GL_Account

OE_QUOTE_HEADER_MC
Company_Code
*See note below

PR_GL_HISTORY_MC
+Alt_Company_Code
GL_Account

PO_PURCHASE_ORDER_DETAIL_MC
Company_Code
GL_Account

PO_PROPOSED_PO_DETAIL_MC
Company_Code
GL_Account

PO_BLANKET_ITEMS_MC
Company_Code
GL_Account

VN_GL_DISTRIBUTION_HEADER_MC
Company_Code
AR_GL_Account

VN_GL_DISTRIBUTION_DETAIL_MC
+Company_Code_2
GL_Distribution_Account

VN_GL_HISTORY_MC
+Company_Code_2
GL_Account

VN_INVOICE_APPROVAL_HDR_MC
Company_Code
AR_GL_Account

VN_INVOICE_APPROVAL_DET_MC
+Company_Code_2
Distribution_GL_Account

VN_OPEN_ITEMS_MC
Company_Code

VN_RECUR_INVOICE_HEADER_MC
Company_Code
**See note below

VN_RECUR_INVOICE_DETAIL_MC
Company_Code
Distribution_GL_Account

VN_SUB_BLL_BELOW_LINE_HDR_MC
Company_Code
AR_GL_Account

VN_SUB_BILLING_OTHER_DET_MC
+Company_Code_2
Distribution_GL_Account

WO_HEADER_MC
Company_Code
***See note below

^ The G/L detail table (GL_DETAIL_MC) contains two cost center columns. This update will populate 'Cost_Center' (not 'Matching_Cost_Center')
+ If the alternate company code is blank, the software checks the transaction's Company_Code (key). If it is the current company, the software assigns the specified cost center, otherwise the cost center column will be blank.
* The Order Processing quote table (OE_QUOTE_HEADER_MC) does not contain the A/R G/L account. The software determines the cost center based on the G/L department of the A/R G/L account code stored in Accounts Receivable Installation.
** The Accounts Payable recurring header table (VN_RECUR_INVOICE_HEADER_MC) does not contain the A/P G/L account. The software determines the cost center based on the G/L department of the A/P G/L account code stored in Accounts Payable Installation.
*** The Work Order Header Table (WO_HEADER_MC) does not contain a G/L account. Instead, the utility will set the cost center based on the Material Sales G/L Account (Material_Sales_GL) stored in the WO_GL_DEPARTMENT_MC table for the assigned department code. The update will read the Work Order header to identify the WO_GL_Department code assigned to the work order, and then set the Cost center in the WO_HEADER_MC table based on that G/L account (if the cost center is blank in the Work Order Header Table).
