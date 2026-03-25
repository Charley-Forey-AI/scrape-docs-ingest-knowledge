---
title: "Field Definitions: PO Item Distribution Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-item-distribution-form/field-definitions-po-item-distribution-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-item-distribution-form/field-definitions-po-item-distribution-form"
---

# Field Definitions: PO Item Distribution Form

The following is a list of field descriptions for the PO Item
 Distribution form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## PO

Enter a PO number or press F4 to select one from a list.
This is the purchase order that you would like to view/maintain the PO item lines on.

## PO Item

Enter a PO item number or press F4 to select
 an item from a list.
Only items associated with the purchase order
 selected in the PO field will display in the list.

## JC Month

Use this field to select which month and year the committed costs are posted to in the Job Cost module. This field will be applied to any PO item lines that you create or modify in the lower portion of the form.
By default this field will populate with the current month and year.

## Description

This field is display only.
This field displays the description of the purchase order item.
If you want to change this value, pull the PO
 into a batch using the [PO Purchase Order Entry ](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form) form and modify the PO item.

## Material

This field is display only.
This field displays the material associated
 with the PO item. Materials are created and maintained using the [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) form.
If you want to change this value, you can pull
 the PO into a batch using the [PO Purchase Order Entry ](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form) form and then modify the PO
 item.

## UM

The UM field on the PO Item Distribution, PO/Item Grid / Info tabs.

This display-only field shows the unit of measure associated with the PO item.
If you want to change this value, you can pull the PO into a batch (via PO Purchase Order Entry) and then modify the PO item.

## Units

This field is display only.
This field displays the units associated with the PO item.
If you want to change this value, you can pull the PO into a batch using the [PO Purchase Order Entry ](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form) form and then modify the PO item.

## Unit Cost

This field is display only.
This field displays the unit cost associated with the PO item.
If you want to change this value, you can pull the PO into a batch using the [PO Purchase Order Entry ](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form) form and then modify the PO item.

## ECM

This field is display only.
This field displays the quantity that the unit
 cost represents.

- E - Per each

- C - Per hundred

- M - Per thousand

If you want to change this value, you can pull the PO into a batch using the [PO Purchase Order Entry ](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form) form and then modify the PO item.

## Total

This field is display only.
This field displays the PO item total.

- If the PO item is a lump sum, this field will
 display the lump sum amount.

- If the PO item is units based, it will calculate
 using the following formula:
Units X
(Unit Cost / ECM) =
Total

If you want to change this value, you can pull the PO into a batch using the [PO Purchase Order Entry ](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form) form and then modify the PO item.

## Line

You cannot change PO item line 1. This line
 calculates based on the other distribution lines on the PO item.
Enter a "+" in this field or, to create a new
 PO item line, click the New
 Record icon when the cursor is in the lower portion of the form.

## Type

The Type drop-down on the PO Item Distribution form, lines Grid / Info tabs.

Use this field to select the type of PO line item that you would like to create. This field is only enabled when creating new PO item lines.

- 1-Job – Select to order materials for a job. Multiple jobs may be on the same PO and do not have to match the job specified in the PO header. Job item lines interface with the JC module to update committed costs and units to specific job/phase/cost type combinations.

- 2-Inventory – Select to order materials that you stock in your inventory. This type of PO item line interfaces with the IN module to automatically track items on order and those that have been received but not yet posted as payable in the AP module.

- 3-Expense – Select to order materials that are not for a job, inventory, work order, or equipment - for example office supplies and office equipment. If using the EM module, you should use this type for actual equipment purchases. This type of purchase order only interfaces with the AP and GL modules, and does not generate any committed costs.

- 4-Equipment – Select to order items used with equipment - for example operating costs such as parts, oil, and fuel, and repair costs. Assigning EM module cost types and cost codes allows you to track these costs for each piece of equipment. Entries for this type of PO do not directly update EM. This occurs when the invoice is posted in AP.

- 5-EM Work Order – Select to order items needed to complete work orders set up in the EM module. Entries for this type of PO do not directly update EM. This occurs when the invoice is posted in AP.

- 6-SM Work Order - Select to purchase materials for service work orders (set up in the SM module). Entries of this type will auto-generate a work completed purchase line for the work order (in SM Work Orders, Work Completed tab), and add the purchase order to the Purchase Orders grid in SM Work Orders.

## JC / IN / EM Company

Enter a company or press F4 to select one from a list.
The type of company that you can select varies
 depending on the type of PO item line that you are creating. For example if Job is selected
 in the Type field, use this field to select the Job Cost module company that is
 associated with the PO item line.

## Job

Enter a job or press F4 to select a job from a list. This is the job associated with the PO item line.
Depending on how the Job Cost module is set up, you might not be able to select a soft or hard-closed job. The status of a job displays in the lookup form when you select it using F4. The
 Allow Posting to Soft-Closed Jobs
 and
 Allow Posting to Hard Closed Jobs
 boxes on the Info tab of [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) determine if you can post to hard or soft closed jobs.

## Phase

Enter
 a phase or press F4 to select one from a list.
Note: If the Phases on this job are locked box on the
 Info tab of [JC Jobs ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) is checked, the selected phase must be set up on
 the job using [JC Job Phases ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form).

## Equipment

Enter the equipment that you are purchasing the material for or press F4 to select it from a list.
This field only applies to equipment type PO item lines.
Equipment is created and maintained using the [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form) form.

## Component Type

Enter the type of component you would like to
 add to the PO item line or press F4 to select one from a list. This field is used in
 conjunction with the
 Component
 field, and is used to add an equipment component to the PO item line.
Component types are created and maintained using the [EM Component Types ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-component-types-form) form, and they are assigned to components using the
 Component Type
 field on the Components/Attachments tab of [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form).
Once a component type is selected in this
 field, you can select a component of that type using the
 Component
 field.
This field only applies to equipment type PO
 item lines.

## Component

Enter a component or press F4 to select one
 from a list. The selected component must be set up as a component of the equipment selected
 in the Equipment field.
Components are created and maintained using the [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form) form, and they are associated with equipment using the Components /Attachments tab.
This field only applies to equipment type PO
 item lines.

## Cost Code

Enter a cost code or press F4 to select one from a list.
Cost codes are created and maintained using the [EM Cost Codes ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-cost-codes-form) form.
If this is an Equipment line and you selected
 a component in the Component field, this field populates with the default cost code set up on
 the component type using the [EM Component Types ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-component-types-form) form.

## Cost Type

Cost Type field in the PO Item Distribution form.

Enter a cost type or press F4 to select one from a list.
If this is a job type PO item line, select a
 job cost type. Use the JC Cost Types form to create and maintain Job Cost Types.
Note: If the Phases on this job are
 locked checkbox is selected on the Info tab of the
 JC Jobs form, you must set up the cost type for the selected phase in the
 JV Job Phases form. If the Phases on this job are
 locked checkbox is not selected, you must specify a
 valid cost type for the phase in the JC Phases form.
If this is an equipment or EM Work Order type
 PO item line, select an equipment cost type. Use the EM Cost Types form to create and maintain Equipment cost types.

## Location

Enter the IN module inventory location that you are purchasing the
 specified material from or press F4 to select it from a list.
Locations are created and maintained in the
 Inventory module using [IN Locations ](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form).
Materials are assigned to locations using [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form).

## SM Co

This field only displays when 6-SM Work Order
 is selected in the Type field.
Enter the SM company that the purchase order
 item applies to or press F4 to select it from a list. This is the
 SM company where the SM work order was set up.

## SM WO

The SM WO field on the PO Item Distribution form, lines Grid / Info tabs.

This field only displays when the line type is 6-SM Work Order.
Enter the SM work order for this PO line or press F4 to select from a list of valid work orders. This is the work order for which you are purchasing the material.

- If you select a work order that is closed, a warning displays and you will be unable to save the record. You must either reopen the selected work order (in SM Work Orders) or enter a different (open) work order.

- If you specify a job-related work order and the job associated with the work order is soft or hard-closed, the system allows the entry only if you allow posting to closed jobs (flags in JC Company Parameters). If you do not allow posting to closed jobs, you will be unable to save the record.

## SM Scope Seq

The SM Scope Seq field on the PO Item Distribution form, lines Grid / Info tabs.

This field only displays if the line type is 6-SM Work Order.
Enter the work order scope for this PO line or press F4 to select from a list of valid scopes for the specified work order.
Note: If you select a scope that has been closed, a warning displays and you will be unable to save the record. You must either reopen the scope in SM Work Orders or select an open scope.

## SM Cost Type

The SM Cost Type field on the PO Item Distribution form, lines Grid / Info tabs.

This field only displays when the line type is 6-SM Work Order.
Enter the SM cost type for this PO line or press F4 to select from a list of valid SM cost types.
The system uses the cost type category for this cost type, along with the department associated with the service center for the work order, to determine the GL account defaults for the resulting work completed purchase line (in SM Work Orders, Work Completed tab).
If you do not specify a cost type here, the system uses the material cost type category to determine the GL accounts to use based on the service center's department.
Note: If you are posting taxes to the purchase order item, entry of an SM Cost Type is required to ensure proper tax distribution. If you do not enter an SM Cost Type, an error is displayed and you will be unable to save the record.

## JC Co

This field only displays when 6-SM Work Order
 is selected in the Type field and the specified SM work order is job-related.
Display only, the Job Cost company associated with the SM work order.

## Job

This field only displays when 6-SM Work Order
 is selected in the Type field and the specified SM work order is job-related.
Display only, the job specified for the SM
 work order (in SM Work Orders).

## Phase

This field only displays when 6-SM Work Order
 is selected in the
 Type

 field and the specified SM work order is job-related.
The system only enables this field if you
 specify a work order scope that is not assigned a phase (in SM Work Orders).
Enter the phase (from JC Job Phases) to which
 this purchase order item applies. Press
 F4
 for a list of valid job phases.

- If you specify a work order scope that is assigned a phase, this field defaults the scope phase and cannot be changed.

- Phases entered on a PO item for an SM work order
 must be set up for the job in JC Job Phases, regardless of whether phases on the job
 are locked. If you need to add a phase "on the fly", you can do so by pressing

 F5
 to access JC Job Phases. Once you add the phase to the job and exit JC
 Job Phases, you can enter the phase here.

## CT

This field only displays when 6-SM Work Order
 is selected in the
 Type

 field and the specified SM work order is job-related.
Enter a valid phase cost type or press
 F4
 to select one from a list.
Note: Cost types entered on a PO item for an SM work order
 must be set up for the job phase in JC Job Phases, regardless of whether phases on the job
 are locked. If you need to add a cost type to the phase "on the fly", you can do so by
 pressing
 F5
 to access JC Job Phases. Once you add the cost type to the job phase and
 exit JC Job Phases, you can enter the cost type here.

## GL Company

Enter the GL company for the PO item line or press F4 to select it from a list. GL companies are created and maintained using the [GL Company Parameters ](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-company-parameters-form) form.
This field is enabled only for 3-Expense line types.
For remaining line types, this field is display only and defaults the GL company as follows:

- 1-Job - Defaults the GL company assigned to the JC company in JC Company Parameters.

- 2-Inventory - Defaults the GL company assigned to the IN Company in IN Company Parameters.

- 4-Equipment / 5-EM Work Order - Defaults the GL company assigned to the EM company in EM Company Parameters.

- 6-SM Word Order - Defaults the GL company assigned to the SM company in SM Company Parameters.

## GL Account

Enter the GL account to charge for this purchase order item line.
 The system uses this account as the default account in AP Transaction Entry - the
 PO module does not update GL.
The default for this field depends on the
 value in the
 Type
 field.

- 1-Job – Defaults from the [JC Departments ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-departments-form) form, and based on
 the phase or cost type on the PO item line. You can override this
 default if the Allow GL Account Override
 when Posting Costs box in [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) is checked.
 If the default is blank, the system allows entry, but disables the
 field when you save the record.

- 2-Inventory – For this type, this field defaults
 from [IN Locations ](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form). You can override this default if you
 checked the Allow GL Account Overrides box in [IN Company Parameters ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form). If the default is blank, the
 system allows entry, but disables the field when you save the record.

- 3-Expense – Defaults from the AP Vendors. You can
 override the default as necessary.

- 4-Equipment & 5-EM Work Order – For these types,
 the field defaults from the EM Department file, based on cost type, and cost code (if
 applicable). You can override this default if you checked the Allow GL Account
 Override box in [EM Company Parameters ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form); otherwise, the system
 disables the field. If the default is blank, the system allows entry, but disables
 the field when you save the record.

- 6-SM Work Order - Defaults the WIP account from the
 SM department assigned to the service center or division specified on the SM work
 order. The system determines the default as follows:

1. If you specified a division on the work order scope
 and an alternate department is assigned to the division, the system will first
 look for an override WIP account for parts based on the call type assigned to
 the work order scope. If an override account is found for the call type, it
 will default here.

1.  If no override WIP account is found for the call
 type, the system will use the standard WIP account for parts defined at the
 department level (in SM Departments, Info tab).

1.  If no alternate department is assigned to the
 division, the system will then use the department assigned to the service
 center to determine the default WIP account using the same process defined in
 steps 1 & 2 above.

## Required Date

Enter the date that this PO item line is required. By default this field will populate with the current date.

## Pay Category

Enter a pay category or press F4 to select one from a list. Pay categories are created and maintained using [AP Pay Category ](/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/ap-pay-typescategories-forms/ap-pay-category-form).
This field defaults a pay category based on
 the following:

- If you have set up a standard or user pay category
 override in F3 Properties (not recommended), defaults the F3 pay category.

- If no F3 override exists, defaults the pay category
 specified for the current user in VA User Profile.

- If no override pay category is specified for the
 user, defaults the pay category defined in AP Company Parameters.

- If no default pay category is defined for the
 company, default will be null. (In this case, the pay type will default from AP
 Company Parameters based on the line's type.)

Note: The pay category specified here will override any
 defaults set by F3, VA User Profile, or AP Company Parameters when the purchase order is
 invoiced in AP Transaction Entry.
This field is enabled only if you are using
 pay categories and entering pay types on purchase orders.
Note: Pay categories are used if the Using Payable
 Category box on [AP Company Parameters ](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form) is checked, and the Specify Pay Type during PO
 entry box is checked on [PO
 Company Parameters ](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form).

## Pay Type

 Enter a pay type or press F4 to select one from a list. Payable types are created and maintained using [AP Payable Types ](/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/ap-pay-typescategories-forms/ap-payable-types-form).
This field will populate with a default value
 based on the following:

- If you are using pay categories (Use Payable
 Category box checked in [AP Company Parameters ](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)), this field will default the
 pay type from this line's pay category based on the line type: Job - Uses the Job pay
 type. Inventory, Expense, Equipment, and EM Work Order - Uses the Expense pay type.
 SM Work Order - Uses the SM Work Order pay type. The default may be overridden;
 however, the pay type must be either assigned to the specified pay category (in AP
 Pay Category) or an 'unassigned' pay type (a pay type that has not been restricted to
 a pay category in AP Payable Types).

- If you are not using pay categories, default will be
 the standard pay type from AP Company based on the line type. May be overridden.

Note: The pay type specified here will override any defaults
 set by F3, VA User Profile, or AP Company Parameters when the purchase order is invoiced in
 AP Transaction Entry.
This field is only enabled if the Specify Pay Type during PO
 Entry box is checked in PO Company Parameters.

## Units

Enter the units that apply to this PO item line.

## Tax Type

The Tax Type field on the PO Item Distribution form, line Grid / Info tabs.

Select the tax type for this PO item line.

- 1-Sales – Tax amounts are payable to the vendor and are added to the purchase order total. This tax amount is directly charged to GL.

- 2-Use - Tax amounts are accrued and paid at a later date to the appropriate State or Local taxing authority. Calculated tax amounts do not affect the gross or net balance due to the vendor. Instead, the transaction's gross and tax amounts are charged to a GL account with an offsetting liability account as defined in HQ Tax Codes. Use the AP Tax Report to obtain an itemization of use tax amounts.

- 3-VAT (Value Added Tax) – This tax applies to Australian and Canadian companies. It is paid on goods and services at each stage of production or distribution, and is based on the value added at each stage. This tax is tracked in GL and reduces the payment to a taxing authority through an Input Tax Credit (ITC). This tax is not directly expensed. Use the AP Value Added Tax Report to obtain an itemization of VAT amounts.

### SM Work Order Lines

For purchase order items with a line type of 6-SM Work
 Order, this field defaults based on the SM Cost Type entered for the
 purchase order item, and the Matl Tax Override and Tax Option Override options
 selected on the associated work order scope. You may override the defaults as
 needed.
The following table describes the default behavior for SM-related
 purchase order line items.
SM Cost TypeMaterialTax Option OverrideMatl Tax OverrideDefault
Note: If the PO vendor
 is not assigned a tax code and the work order scope's tax source
 (service site or service center) is not assigned a tax code, all
 tax fields default as blank, but may be overridden.

Not TaxableBlankAllAllBlank
Not Taxable
Taxable
TaxableNot TaxableAllAllBlank
TaxableAllN - No TaxBlank
P - Taxable at Purchase Only,
 M - Taxable at Purchase/Markup at Billing, F - Full Tax at Purchase
 and BillingIf Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at Billing
 OnlyAllBlank
BlankP - Taxable at Purchase Only,
 M - Taxable at Purchase/Markup at Billing, F - Full Tax at Purchase
 and BillingIf Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at Billing
 OnlyAllBlank

## Tax Code

The Tax Code field on the PO Item Distribution form.

Entry in this field requires that you first enter a Tax Type.
Enter the tax code to use for this purchase order item or accept the defaulted value. Press F4 to select from a list of valid tax codes for the specified Tax Type.
This field defaults as follows:
Job LinesThe default for job lines is determined by the setting of the Base Tax On field in JC Jobs.

- J-Job - The tax code defaults from JC Jobs (Tax Code field). If no tax code is specified for the job, the default will be null.

- V-Vendor - The tax code defaults from AP Vendors (Tax Code field). If a tax code is not specified for the vendor, the default will be null.

- O-Vendor Override - The tax code defaults from AP Vendors. If a tax code is not specified for the vendor, the tax code will default from JC Jobs. You can override the default as necessary.

Inv / Exp / Equip / EM WO / SM WO LinesFor all non-job lines, the tax code defaults as follows:

- If you specified a Ship Location (PO header) and the ship location is assigned a tax code, that tax code defaults here.

- If the ship location is not assigned a tax code or you do not specify a ship location, this field defaults as follows:

- Inventory lines - Defaults the tax code specified for the inventory location. If no tax code is specified for the location, this field defaults as blank.

- Exp / Equip / EM Work Order lines - Defaults the tax code from AP Vendors for the vendor specified in the PO header. If a tax code is not assigned to the vendor, this field defaults as blank.

- SM Work Order lines - Defaults the tax code from AP Vendors for the vendor specified in the PO header. If a tax code is not assigned to the vendor, this field defaults based on the Tax Type.

- If the tax type is Sales or VAT, this field defaults the Tax Code assigned to the service site or service center, depending on the tax source specified for the work order scope.

- If the tax type is Use, this field defaults the Use Tax Code assigned to the service site or service center, depending on the scope's tax source. If no Use Tax Code is specified, it defaults the Tax Code specified for the tax source.

- If no tax codes (sales or use) are defined for the tax source, this field defaults as blank.

Note: If the SM work order is a job work order, the default behavior is the same as described above for Job Lines.

Intercompany TransactionsFor intercompany invoices, the tax code defaults as follows:

- If the tax type is Sales or VAT (Value Added Tax), the tax code defaults based on the Tax Group assigned to the AP Company.

- If the tax type is Use, the tax code defaults based on the Tax Group assigned to the 'posted to' company.

### Committed Costs (Job Lines)

If you post a job cost line (JC type) with tax, the system relieves committed costs from the phase/cost type in JC Cost Detail table for the tax amount as follows:

- If phase or cost type overrides do not exist for the tax code, the system uses the phase and cost type specified for the PO item.

- If phase and cost type overrides exist for the tax code, the system uses the tax code phase and cost type.

- If a phase override exists for the tax code, but a cost type override does not exist, the system uses the tax code phase and the cost type from the PO line.

- If a cost type override exists for the tax code, but a phase override does not exist, the system uses the phase from the PO line and the tax code cost type.Note: In all cases, the system updates JC with the tax rate amount. When you create an AP transaction for this PO item, the system relives the original tax rate amount from JC, but uses the current tax rate when creating an invoice.

### Redirect Phase/Cost Type

If this PO item is for a job (line type 1-Job) or a job-related SM work order (line type 6-SM Work Order) and the tax code is assigned a redirect phase and/or cost type (JC Tax Phase and/or JC Cost Type in HQ Tax Codes), the system validates the phase and/or cost type based on the Phases on this job are locked checkbox in JC Jobs.
If the Phases on this job are locked checkbox is selected and:

- The tax code specifies a redirect phase only, the phase must exist in JC Job Phases for the PO Item job (if a 1-Job line) or the work order job (if a 6-SM Work Order line).

- The tax code specifies both a redirect phase and cost type, the phase/cost type combination must exist for the specified job in JC Job Phases.

- The tax code specifies a redirect cost type only, the cost type must exist in JC Job Phases for the PO item phase (Job line) or the work order scope phase (SM Work Order line). For SM Work Order lines, if you have not assigned a phase to the work order scope, the cost type must exist for the PO item phase.

If the Phases on this job are locked checkbox is not selected and

- The tax code specifies a redirect phase only, the phase must exist in JC Job Phases or JC Phases for the PO Item job or the SM work order job.

- The tax code specifies both a redirect phase and cost type, the phase/cost type combination must exist for the specified job in JC Job Phases or JC Phases.

- The tax code specifies a redirect cost type only, the cost type must exist in JC Job Phases or JC Phases for the PO item phase (Job line) or the work order scope phase (SM Work Order line). For SM Work Order lines, if you have not assigned a phase to the work order scope, the cost type must exist for the PO item phase.

Note: If validation determines that the conditions indicated above do not exist, you will need to either use a different tax code or add the phase and/or cost type combination to JC Job Phases or JC Phases (depending on the "locked phases" flag) before you can post the batch.

## Work Order

Enter the work order that you are purchasing the material for or press F4 to select it from a list.
This field only displays when EM Work Order
 is selected in the Type field.
Work orders for equipment maintenance are
 created and maintained using the [EM Work Order Edit ](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form) form. You can open this form by
 pressing F5 in this field.

## Work Order Item

Enter the work order item that the PO item
 line applies to or press F4 to select it from a list.
This field only displays when EM Work Order
 is selected in the Type field.

## Notes

Enter notes on the PO item line.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.
