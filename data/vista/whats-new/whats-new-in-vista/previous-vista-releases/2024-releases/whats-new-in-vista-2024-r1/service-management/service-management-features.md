---
title: "Service Management Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/service-management/service-management-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/service-management/service-management-features"
---

# Service Management Features

Vista 2024 R1 delivers on user-requested Service Management enhancements, fixes, and other improvements.

## Enhanced Tax Handling for Service Management

Improved tax handling in Service Management now allows you to pay or accrue taxes when purchasing materials for a work order and then, if applicable, also apply taxes when billing the work order.
As part of this enhanced functionality, a new Tax Option field was added to the SM Call Types form. This new field allows you specify how to handle taxes for work completed lines. Available options are:

- N - Not Taxable

- P - Taxable at Purchase Only

- B - Taxable at Billing Only

- M - Taxable at Purchase/Markup at Billing

- F - Full Tax at Purchase and Billing

In addition, a Tax Option Override field was added to the following forms:

- SM Agreements

- SM Service

- SM Work Order Quotes

- SM Work Orders

For SM Agreements and SM Work Order Quotes, this field defaults as blank. You will only enter a value if you want to override the Tax Option selected for the Call Type assigned to the agreement service or quote scope.
For SM Service, this field defaults based on the option you selected for the related agreement. You may override the default as needed.
 For manually entered work orders, this field defaults as blank. For work orders scopes generated from an agreement service or work order quote, this field defaults the Tax Option Override specified for the agreement service or work order quote scope (respectively). You may override the defaulted value on the work order scope as needed.
Note: The Tax Option Override selected for each work order scope is used to determine taxability for Misc, Inventory, and Purchase work completed lines associated with the work order scope. For a complete description of the Tax Option Override options, see [Tax Option Override](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#concept-nef25hfx--en).

Additional changes made for the new tax handling functionality include:
New Tax Fields for Work CompletedFor Miscellaneous, Inventory, and Purchase work completed lines, additional tax fields were added to the work completed grid. These tax fields allow you to enter cost tax for Misc and Inventory transactions, as well as display cost tax information from Accounts Payable and Purchase Orders.

- Cost Tax Type

- Cost Tax Code

- Cost Tax Basis

- Cost Tax Amt

These new fields were also added to the Cost section on the Info tab for the SM Work Completed Misc, SM Work Completed Inventory, and SM Work Completed Purchase forms, as well as to the Grid tab for each form.
For Misc lines, these fields are enabled only if you are manually entering miscellaneous work completed lines in the Work Completed grid in SM Work Orders or in the SM Work Completed Misc form. For Misc work completed lines generated from AP Transaction Entry (type 8-SM Work Order), these fields are populated from the AP invoice line and are disabled in both the grid and the form. Changes to cost tax information for AP-generated miscellaneous lines must be handled in AP Transaction Entry.
Note: For Misc lines entered in SM (via the Work Completed grid or the SM Work Completed Misc form), only tax types 1-Sales and 2-Use are allowed. Tax type 3-VAT is only valid for Misc lines generated from an AP invoice.

For Inventory lines, these fields are enabled and populated based on the Material Tax Override and Tax Option Override values. You may override the default values as needed.
For Purchase lines, these fields are disabled in both the grid and the SM Work Completed Purchase form. If you need to update the tax information, you must do so using either SM Purchase Order Entry or PO Purchase Order Entry.
For information about defaulting for the Cost Tax fields, refer to the F1 Help.
New AP History tab in SM Work Completed PurchaseYou can now view the AP information for work completed purchase lines on SM work orders using the new AP History tab on the SM Work Completed Purchase form. This display-only tab shows you the transaction detail for AP invoices posted to SM-related purchase orders in AP Transaction Entry. The detail shown on this tab includes (but is not limited to) the PO number, related AP transaction and invoice line, AP reference number, invoice amounts, and tax information.
This tab is display only and is populated once you post the AP transaction (via AP Batch Process).
Billing Tax for Work Completed LinesThe tax fields on the Work Completed grid in SM Work Orders, as well as those displayed in the related Work Completed forms, are now reserved for billing purposes only.
 For clarity, the labels for the tax fields in the Work Completed grid (shown after the Bill Amount field) were changed to:

- Bill Tax Type

- Bill Tax Code

- Bill Tax Basis

- Bill Tax Amt

In addition, the original tax fields in the SM Work Completed Misc, SM Work Completed Inventory, and SM Work Completed Purchase forms were moved into the Billable group box and the grid columns relabeled to match the labels in the work completed grid.
The system uses the Tax Option Override defined for the work order scope to determine the billing taxability of work completed lines, along with the Tax Type and Tax Code defined for the work order scope. If the Tax Option Override is blank for the work order scope, the system uses the Tax Option defined for the scope's Call Type.
As part of these changes, the 2-Use tax option was removed from the Bill Tax Type field for all line types, since use tax is not applicable for billing.
Updates to SM and GL for AP Use TaxWhen you post a transaction to an SM work order in AP Transaction Entry, if the transaction includes Use tax, the system now correctly updates Service Management and General Ledger.
Use tax values from an AP transaction will appear in the Cost Tax Type, Cost Tax Code, Cost Tax Basis, and Cost Tax Amt fields of the generated work completed miscellaneous line, regardless of how you have set the Material Tax Override option for the associated work order scope. These values cannot be changed.
Note: For an accounting of the General Ledger updates, see the batch reports when processing the AP transaction via AP Batch Process.

Tax Type/Tax Code Fields Now Available for T&M Work Order ScopesWhen entering a T&M work order scope, you now have access to the Tax Type and Tax Code fields (previously only available for Flat Price scopes). In addition, these fields are now enclosed in a Billing Tax Info group box for better clarity.
The Tax Type defaults to 1-Sales for U.S. companies and to 3-VAT for Australian and Canadian companies. The Tax Code defaults from the service site or service center, depending on the Tax Source selected for the work order scope. Defaults may be overridden as needed.
In addition, for Flat Price scopes, changed the label for the Tax Amount field to Est. Billable Tax.
Job Work Orders
The Tax Type and Tax Code fields remain unavailable for Job work order scopes, as tax information comes from the job specified for the work order. The Tax Source field (which was previously displayed but disabled) has been removed, as it is not used for job work orders.
Matl Tax Override / Tax Option Defaults for Agreements/ServicesWhen you amend or renew an agreement, the Matl Tax Override and Tax Option Override values are now copied to the new revision for both the agreement and the agreement services. You may override the values if needed.
If you change the Matl Tax Override and/or Tax Option Override value(s) for an existing agreement with one or more agreement services, when you save the record, the system displays a message asking if you want to update existing agreement services to the new value(s). If you select Yes, the system updates the value(s) for all agreement services to match the new value(s) entered for the agreement. However, if you update the agreement value to blank, when the services are updated, the system defaults the value(s) from the call type associated with each service. If you select No, the system leaves the existing value(s) intact for each agreement service.
Work Completed Grid RelabelingSeveral of the fields in the Work Completed grid in SM Work Orders have been relabeled to be more consistent with their related Work Completed forms. The fields affected by this change are as follows:
Old LabelNew LabelLine Type
Actual CostTotal Actual CostAll
Actual QuantityInvoiced UnitsPurchase
Total BillableBill SubtotalAll
Billable ECMBill ECMInventory, Purchase
Billable HrsBill HrsLabor
Billable QtyBill QtyMisc
Billable RateBill RateAll
Billable UMBill UMInventory, Purchase
Pretax CostCost SubtotalMisc (material-related), Inventory, Purchase lines
Proj CostTotal Projected CostLabor, Purchase
TotalTotal BillableAll
UMCost UMInventory, Purchase

Note: Some of these fields may be hidden intentionally by Viewpoint or by your company (via the F3 Properties form). If a field is not displaying, use the Show in Grid checkbox in the F3 Properties form (User Overrides or System Overrides tabs) to have them display in the grid.

Updated SM Work Completed Misc, Inventory, and Purchase FormsIn conjunction with the changes in this release that separates cost tax from billing tax, the Cost and Billable sections on the SM Work Completed Misc, SM Work Completed Inventory, and SM Work Completed Purchase forms have been updated to provide a more consistent look and support a more intuitive data flow.
In addition to adding Cost Tax fields to the Cost section and Grid tab for each of these forms, the Tax group box was removed and the existing tax fields moved into the Billable section.
Additional changes to these forms are as follows:
SM Work Completed Misc

- In the Cost group box:

- Renamed the Pretax field to Subtotal. For transactions created in AP, this amount is the sum of the Misc Amt and Gross amount. This amount does not include use tax for lines coming from AP or lines entered directly in the Work Completed grid.

- Added a Unit Cost field.

- Moved the Rate field lower in the group box and disabled it.

- Added a display-only Total field (bottom of group box).

- In the Billable group box:

- Renamed the (billable) Total field to Subtotal.

- Enabled the Tax Amount field for editing.

- Added a display-only Total field (bottom of group box).

SM Work Completed Inventory

- In the Cost group box:

- Renamed the Rate field to Cost Rate and moved it and the related cost ECM field lower in the group box; both the Cost Rate and ECM fields are now disabled.

- Added Unit Cost and unit cost ECM fields.

- Renamed the Pretax field to Subtotal.

- In the Billable group box:

-  Renamed the Total field to Subtotal.

- Added a display-only Total field.

SM Work Completed Purchase

- In the Cost group box

- Renamed the Projected Cost group box to Projected Cost from Purchase Order

- Added Unit Cost and unit cost EMC fields

- Renamed the Total field to Subtotal

- The Rate and rate ECM fields were moved lower in the group box

- In the Billable group box

- Renamed the Total field to Subtotal

- Added a display-only Total field

- Enabled the Tax Amount field

- Other Changes

- Renamed the Actual Cost group box to Actual Cost from Accounts Payable

- Moved the Received group box after the Projected Cost from Purchase Order group box

- Renamed the Quantity field in the Actual Cost from Accounts Payable group box to Invoiced Units

- On the Grid tab, several column names were relabeled to match the changes made on the Info tab. In addition, some columns were repositioned for a better work flow.

## Updates to Legacy Data

In conjunction with all of the changes made for the SM Tax Handling feature, existing work completed lines, work order scopes, and work order quote scopes require updating. Therefore, during installation of Vista 2024 R1, the installation process will run a procedure to update these existing records. The following briefly describes these updates.Work Completed Lines (Type 3-Misc, 4-Inv, and 5-Purchase)For existing work completed lines with a Tax Type of 1-Sales or 3-VAT, the system populates the Bill Tax Type, Bill Tax Code, Bill Tax Basis, and Bill Tax Amount fields with the legacy tax values (tax type, tax code, tax basis, and tax amount). For work completed lines with a Tax Type of 2-Use, the system populates the new Cost Tax Type, Cost Tax Code, Cost Tax Basis, and Cost Tax Amount fields with the legacy tax values and sets the legacy tax fields, now the Bill Tax fields, to null (blank).
For the new Cost UC and Cost Subtotal fields, the system updates existing work completed records as follows:

- If the tax type is 1-Sales or 3-VAT, the Cost Subtotal field is set equal to the legacy Cost Total value, including tax (if the Cost Total included tax).If the work completed line is unit-based, the system sets the Cost UC field to a value that includes tax, if the legacy Cost Total included tax. Additionally the Cost Rate field (display only) is updated to include tax if the legacy Cost Total included tax.

- If the Tax Type is 2-Use, the system populates the Cost Subtotal field with the legacy Cost Total value, less tax (if the Cost Total included tax).If the work completed line is unit-based, the system sets the Cost UC field to a value that excludes tax (if the legacy Cost Total included tax). In addition, the Cost Rate field is updated to include tax, if the legacy Cost Total included tax.

Work Order Scopes (Customer work orders only)For work order scopes with a Price Method of Time & Materials, the system sets the new Tax Type and Tax Code fields for existing records based on the scope's Tax Source (service site or service center).
 The Tax Code defaults from the service site or service center (depending on the Tax Source). If the tax code is not a VAT code, the Tax Type is set to 1-Sales. If the tax code is a VAT code, the Tax Type is set to 3-VAT. If the service site or service center Tax Code is blank, the scope Tax Type and Tax Code default as blank. You may override the defaults as needed.
Work Order Quote ScopesFor work order quote scopes with a Price Method of Time & Materials, the system sets the new Tax Type and Tax Code fields for existing records based on the quote scope's Tax Source (service site or service center).The Tax Code defaults from the service site or service center (depending on the Tax Source). If the tax code is not a VAT code, the Tax Type is set to 1-Sales. If the tax code is a VAT code, the Tax Type is set to 3-VAT. If the service site or service center Tax Code is blank, the scope Tax Type and Tax Code default as blank. You may override the defaults as needed.

## Disabled Use Tax Variance Feature

With the extensive changes made to tax handling for SM Work Orders, the Use Tax Variance feature in SM is no longer a valid option for capturing tax variance on work completed lines. Therefore, the Use Tax Variance checkbox in SM Company Parameters has been removed.
You can still capture tax variance manually on AP invoices (SM and PO) and via the Work Completed grid or SM Work Completed Misc form. For more information, see the [Enter Tax Variance for Work Completed](/en/vista/vista/service-management/work-orders/enter-tax-variance-for-work-completed) article.

## 'Refresh' Control Options Added for Dispatch Boards

You now have the ability to control whether dispatch boards are updated when saving work orders and/or work order scopes.
To implement this functionality, the following checkboxes were added to the SM Dispatch Board Setup form:

- Refresh Board on Work Order Save - When this checkbox is selected, the system will update the selected dispatch board (when open) each time a work order is saved.

- Refresh Board on Scope Save - When this checkbox is selected, the system will update the selected dispatch board (when open) each time a work order scope is saved.

If you have large amounts of data on your system and/or use custom queries on your dispatch board, it is recommended that you do not select either of these checkboxes, as they may potentially cause performance issues when saving work orders and work order scopes.

## Improved F4 Lookup in SM Service Centers

When using the F4 Lookup from the Service Center field in SM Service Centers, you now have two lookup options:

- SM Service Center (Active) - This is the default lookup, which shows only the active service centers.

- SM Service Centers (All) - This lookup shows both active and inactive service centers.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
