---
title: "About the IN Adjustment Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/transfersadjustments/about-the-in-adjustment-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/transfersadjustments/about-the-in-adjustment-entry-form"
---

# About the IN Adjustment Entry Form

Use this form to adjust current Inventory levels and/or their
 values.
Adjustments are generally made to compensate for theft, incorrect postings, or write-offs. Adjustments for discrepancies found during physical counts can also be entered here, though typically they will be entered directly in [IN Physical Count Worksheet ](/en/vista/vista/job-resources/inventory/monthly-reconciliation/in-physical-count-worksheet-form). This form can also be used to expense materials that are not accounted for in production, transfers, sales, or other posting, directly to a GL account.
You can adjust units only (setting Total Cost to
 0.00), total cost only (setting Units to 0.00), or both units and total
 cost. Changes to Unit Cost only will have no impact. If adjusting both units
 and total cost, the Unit Cost used to calculate the Total Cost is determined
 by the Cost Method specified for the location (i.e., if the Cost Method is
 Avg Unit Cost, the Unit Cost will be the material’s Avg Unit Cost as defined
 in Location Materials). The Cost Method is defined in IN Company Parameters,
 but may be overridden by location (IN Locations) or by location/category (IN
 Location Category Override).
Adjustments made here will update the Average Unit
 Cost and On Hand amounts appropriately (in IN Location Materials). Average
 Unit Cost will not be updated for expense entries where the default GL
 Account has been overwritten unless the GL account is equal to the
 material’s Inventory Adjustment account (in IN Locations).
Note: The Unit Cost and EM fields are only available when the Allow Unit Cost Overrides checkbox is selected in IN Company Parameters.
[About Posting Adjustments in General Ledger](/en/vista/vista/job-resources/inventory/transfersadjustments/about-posting-adjustments-in-general-ledger#concept-711--en__concept-711)
