---
title: "About the EM Departments Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-departments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-departments-form"
---

# About the EM Departments Form

Use this form to set up departments and define the General Ledger accounts to which equipment revenue (usage) and costs should be posted.
Each piece of equipment (set up in EM Equipment) must be assigned to a department in order to determine where to post that equipment’s revenue and costs.
Note: All GL accounts defined for a department must be assigned a Sub Ledger Code of ‘E-Equipment’ or 'null' (blank) in GL Chart of Accounts.

- How Many Departments Do I Need? - You can set up as many departments as needed based on your company’s accounting needs. However, if all equipment revenue and expenses are posted to a single set of GL accounts, then you need only set up one department.

- Where are the accounts used? - Departments are assigned to equipment in EM Equipment. Whenever you post usage or costs to a piece of equipment, the system finds the correct revenue or cost GL account from this department file. In some forms, such as EM Cost Adjustments, EM Usage Posting, and AP Transaction Entry, you can override the default accounts, provided the appropriate ‘Allow GL Accounts Override’ option is checked in EM Company Parameters. In other situations where equipment revenue or costs are updated, the GL update is completely automatic.Note: You can ‘turn off’ any of the GL updates that occur when posting equipment revenue or costs by setting the appropriate General Ledger Update option in EM Company Parameters to ‘No Update’.

- Cost Types Tab - The Cost Types tab allows you to assign GL accounts to each of the cost types that apply to the selected department. These accounts will be used when costs are posted to the equipment for the selected cost types. You may have separate GL accounts for each cost type or you may assign the same GL account to more than one cost type.Note: GL accounts assigned here must be an account type of either ‘E-Expense’ or ‘A-Asset’ (in GL Chart of Accounts).

- Cost Codes Tab - If you require a finer level of GL breakdown, you can set up GL account overrides by cost code. Any posting to that cost code (regardless of the cost type) goes to the override account. For example, you use four cost types: Labor, Parts, Subcontract, and Miscellaneous. Each of them is given an expense GL account. However, you want certain ownership expenses, such as depreciation and insurance, to be broken out into their own accounts. You would set up cost codes for those items (in EM Cost Codes) and then assign the override GL accounts to those cost codes here. You can then post your depreciation and insurance costs to the miscellaneous cost type, and the system will use the override accounts instead of the miscellaneous account.

- Earnings Types tab - This tab allows you to assign GL accounts to each of the earnings types used when posting mechanics' timecards. Typically, this is done when certain types of earnings need to be posted to separate GL accounts, rather than following the labor cost type's GL account.

- Liability Type Tab - This tab allows you to assign GL accounts to each of the liability types used when posting mechanics' timecards. Typically, you will use this feature when certain liabilities need to be posted to different GL accounts. For example, you would set up accounts here if you want the portion of burden expense to go to an account other than the one assigned to the corresponding cost type.

- Revenue Breakdown Codes Tab - Use this tab to assign GL accounts to revenue breakdown codes. When posting equipment usage, these accounts will be used in place of the specified revenue code's GL account. If you do not want these accounts used for a specific revenue code, make sure you assign a GL account to that revenue code.

- Revenue Codes Tab - This tab allows you to assign GL accounts to each of the revenue codes used when posting equipment usage. If you do not assign GL accounts here, usage will be posted to the GL accounts for the assigned revenue breakdown codes.

- Workflow Tab - This tab only applies if you have the Workflow module and use the Process Workflow feature. The workflow processes added to this tab will override the workflow processes set up on the Workflow tab of the EM Company Parameters form, and the Workflow tab of the HQ Company Setup form - for example any process set up on a specific department will override the more generic processes set up at the module and application level. For more information, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

- Roles Tab - This tab only applies if you have the Workflow module and use the Process Workflow feature. Use this tab to assign a user to a specific role. The following rules apply when adding roles/users:


- Users can only be associated with a role that they have been set up with in HQ Roles.

- Users can be assigned to more than one role.

- Roles can be used more than once.

Related information

- [About the EM Equipment Form](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form)
