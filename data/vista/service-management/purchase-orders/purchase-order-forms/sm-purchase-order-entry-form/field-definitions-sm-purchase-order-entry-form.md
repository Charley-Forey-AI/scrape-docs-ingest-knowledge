---
title: "Field Definitions: SM Purchase Order Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form"
---

# Field Definitions: SM Purchase Order Entry Form

The following is a list of field descriptions for the SM
 Purchase Order Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## PO #

Enter a purchase order number, up to 30 characters. Initially defaults as follows:

- If the Automatically Generate PO #'s box
 is checked in PO Company Parameters, this field defaults a PO number based on the
 Last Used
 PO # field in PO Company Parameters.

- If the Automatically Generate PO #'s box
 is not checked in PO Company Parameters, this field defaults as null.

Note: When manually entering a purchase order number, the system will verify that the number has not been used before. If it has, a message displays indicating that the PO # already exists. You will need to enter a number that has not been used before the record can be added.

## Vendor

Enter the vendor (from AP Vendors) that is supplying the merchandise
 on this purchase order or leave blank if you do not yet know the vendor.

-  If you know who the vendor is for this purchase order, but do not know the vendor number, you can enter the vendor's sort name and the system will default the vendor number for you.

- If you enter a non-compliant vendor, the header displays a red warning in the header section of the form.

- You can change vendors on existing POs until you apply invoices.

## Description

The Description field on the SM Purchase Order Entry form, header Info
 tab.
Enter a description of this purchase order, up to 60 characters. This description corresponds to the description in the purchase order header (in PO Purchase Order Entry).

## Order Date

The Order Date field on the SM Purchase Order Entry form, header Info tab.
Enter the date that this order was placed or accept the default (today's date).

## Prevent Auto Close

Prevent Auto Close checkbox on the Info tab header of the SM Purchase Order Entry form.

Select this checkbox to prevent the purchase order from being auto-closed on final invoice.

## Expected Date

The Expected Date field on the SM Purchase Order Entry form, header Info
 tab.
Enter the date that you expect to receive the
 items on this purchase order.

## Ordered By

The Ordered By field on the SM Purchase Order Entry form, header Info tab.
 Enter the name (or initials) of the person
 who placed the order.

## Hold Code

The Hold Code field on the SM Purchase Order Entry form, header Info tab.
Enter the hold code for this purchase order or
 press F4 to select from a list of valid hold codes. Specifying a hold code here
 automatically places AP transactions posted to this purchase order on payment hold.
Leave this field blank if no hold code applies to this purchase order.
Note: You cannot select a hold code set up for 'Retainage' in AP Company Parameters.

## Pay Terms

Specify the payment terms for this vendor/purchase order, or accept
 the default pay terms assigned to this vendor in AP Vendors.

## Cmpl Group

The Cmpl Group field on the SM Purchase Order Entry form, header Info tab.
Enter the compliance group (set up in [HQ Compliance Groups ](/en/vista/vista/administration/headquarters/compliance-setup/about-the-hq-compliance-groups-form)) for this purchase order or press F4 to select from a list of valid compliance groups. The compliance group is used to initialize compliance codes for this purchase order in PO Compliance Tracking. If you leave this field blank, compliance codes will need to be entered manually.
Note: If you change the compliance group for this purchase order after initialization has occurred, all compliance codes not already on the purchase order will be added when re-initialized.

## Ship Location

The Ship Location field on the SM Purchase Order Entry form, items Info
 tab.

The shipping location defines the default “Ship To” address, which will print on the Purchase Order Form.
Enter the shipping location or press F4 to select from a list of valid
 shipping locations.
The shipping location defines the default "ship to" address for the
 purchase order (shown on the Shipping Tab) and will print on the Purchase Order Form. You
 may override the address on the Shipping tab if needed.
Note: If a tax code is assigned to
 the ship location using PO Shipping Locations, it will be used as the tax code default and
 will override the standard tax code defaults.

## Shipping: Address

The Address fields on the SM Purchase Order Entry form, Shipping tab.
Use the following address fields to enter the shipping address for this SM purchase order. Initially defaults the address defined for the Ship Location specified on the Info tab. If no ship location is specified, these fields default as blank.

- Address

- Add'l Address

- City

- State

- Zip Code

- Country - Only required if the address exists outside the Default Country specified in HQ Company Parameters for the active company.

The address information entered here populates the address fields on the Shipping tab in PO Purchase Order entry, and will also print on the purchase order form.Note: If you enter an address here and then enter a Ship Location on the Info tab, the Ship Location address overwrites the address you entered here.

## Shipping: Attention

The Attention field on the SM Purchase Order Entry form, Shipping tab.

Use this field to add "attention" information to the ship to address. For example, "Joe Smith; Receiving".
 These instructions will populate the Attention field on the Shipping tab in PO Purchase Order, and will also print on the purchase order form.Note: If you change the shipping address using the Ship Location field on the Info tab, the information in this field is left intact.

## Shipping: Shipping Instructions

The Instructions field on the SM Purchase Order Entry form, Shipping tab.

Enter shipping instructions for this SM purchase order, up to 60 characters.
 These instructions will populate the Shipping Instructions field on the Shipping tab in PO Purchase Order, and will also print on the purchase order form.Note: If you change the shipping address using the Ship Location field on the Info tab, the information in this field is left intact.

## Notes

The Notes field or text box on forms throughout Vista
Enter any miscellaneous notes about this item. The space allowance is virtually unlimited.
Note: If you are accessing this field from a grid and you need additional space for your notes, double-click in the field to access the Grid Notes form.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field, right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard note to copy (or choose one from the F4 lookup) and select OK. The system inserts the selected note into the field.
Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

## Item

The Item field on the SM Purchase Order Entry form, items section.
Enter + or N to add a new purchase order item. The
 system automatically assigns the next available sequential number.

## Scope Seq

The Scope Seq field on the SM Purchase Order Entry form, items Info tab.

Enter the scope for this purchase order item
 or press F4 to select from a list of valid scopes for the specified work order.
Note: If you select a scope that
 has been closed, a warning displays and you will be unable to save the record. You must
 either reopen the scope in SM Work Orders or select an open scope.

### Job Work Orders

If this purchase order is for a job-related work order, once you enter the work order
 scope sequence, the screen displays the job and job description below the tax
 information. If you have already assigned a phase to the work order scope, the phase and
 phase description will also display.
If you have not assigned a phase to the work order scope, you will receive a message
 that the specified scope is missing a phase, and that you must enter a phase for the
 scope sequence before continuing.
Tip: You can add a phase to the work order scope
 without closing the SM Purchase Order Entry form. Just select the SM Work Order form
 (which should already be open), enter a phase on the applicable work order scope, and
 save the record. Then return to the SM Purchase Order Entry form and complete entry
 of your purchase order item.

## SM Cost Type

The SM Cost Type field on the SM Purchase Order Entry form, items Info
 tab.

Enter the SM cost type for this purchase order
 item or press F4 to select from a list of valid SM cost types.
Note: For purchase order items that include materials, if you do not specify a cost type here, the system uses the material cost type category to determine the GL accounts to use based on the service center's department.

The system uses the cost type category for
 this cost type, along with the department associated with the service center for the work
 order to determine the GL account defaults for the resulting work completed purchase
 line.
In addition, the SM Cost Type is used, in conjunction with other factors, to determine the
 taxability of the purchase order item. For more information, see the [Tax Type](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-00046861--en) and [Tax Code](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-00046877--en) F1 Help.
Note: If you are posting taxes to the purchase order item, entry of an SM Cost Type is required to ensure proper tax distribution. If you do not enter an SM Cost Type, an error is displayed and you will be unable to save the record.

## Material

The Material field on the SM Purchase Order Entry form, items Info tab.
Entry in this field is not required unless posting an Inventory
 transaction (type 2-Inv).
Enter the material for this purchase order
 item or press F4 to select from a list of valid HQ materials
 (non-Inventory lines) or IN Location materials (Inventory lines). The description, unit of
 measure, and standard unit cost default from HQ Materials.
Note: For non-Inventory lines only, you can
 enter any material, valid or non-valid. If you specify a non-valid material, the
 material description defaults as 'Not in material file' and the unit of measure defaults
 as EA.

If this purchase order item is not for a
 material, you may leave this field blank and use the Description field to identify the
 purchase.
If you enter a material that exists in PO Vendor Materials for the specified vendor/material group, the description will default from PO Vendor Materials. If multiple UMs exist for the vendor material, the system will default the description from the lowest UM in PO Vendor Materials.
Equipment LinesIf the material number exists in EM Equipment Parts, the
 system defaults the description and unit of measure from EM Equipment Parts, and
 the unit cost from HQ Materials.If the material number also
 exists in PO Vendor Materials, the description and unit of measure will default
 from EM Equipment Parts, but the unit cost will default from PO Vendor
 Materials.
EM Work Order LinesIf the material number exists in EM Work Order Parts or EM
 Equipment Parts, the description and unit of measure will default from EM Work
 Order Parts or EM Equipment Parts, respectively; however, the unit cost will
 default from HQ Materials.If the material number also exists
 in PO Vendor Materials, the system defaults the description and unit of measure
 from EM Work Order Parts or EM Equipment Parts; however, the unit cost defaults
 from PO Vendor Materials.
Note: If notes exist for the
 material in HQ Materials, you can add them to the notes for the purchase
 order item by selecting Copy
 Notes. Material notes are appended to any existing PO item
 notes. If no notes exist for the material, the Copy Notes button is
 disabled.

Note: This field is disabled once you distribute the PO item
 (in PO Item Distribution), receive the item (in PO Receipts Entry), or invoice the item (in
 AP Transaction Entry).

## Vendor Matl

Enter the vendor’s identification number for this material, if applicable. Initially defaults a value as follows:

- If you entered a valid HQ material in the Material
 field and a vendor material exists for the vendor/material group/HQ material in PO
 Vendor Materials, this field defaults the Vendor's Matl ID from PO Vendor Materials.

 If multiple entries exist for the vendor/material group/material (e.g. multiple UMs), this field will default the Vendor Matl ID from the entry matching the Purchase UM for the material in HQ Materials. If a match is not found, it will default the Vendor's Matl ID from the lowest UM (in PO Vendor Materials) for the vendor/material group/material.

- If you entered a non-valid material in the
 Material field, left the Material field blank, or entered a
 valid material, but no vendor material exists for the HQ material in PO Vendor
 Materials, this field defaults as null.

Note: Because the vendor’s material ID# is used as a cross-reference to the HQ material, you can enter this number if you do not know the HQ material number, and the HQ material number will be provided. This feature is only applicable to materials set up in PO Vendor Materials.
Note: This field will be disabled once you distribute the PO item (in PO Item Distribution), receive the PO item (in PO Receipts Entry), or invoice the item (in AP Transaction Entry).

## Description

The Desription field on the SM Purchase Order Entry form, items Info tab.
Enter a description of the purchase order item, up to 60 characters.
 Initially defaults a value as follows:

- If you entered a valid material in the Material
 field, defaults the material description from HQ Materials.

- If you entered a non-valid material in the
 Material field, this field defaults as 'Not in this material file.'

- If you entered a valid vendor material in the
 Vendor
 Matl field, defaults the description defined for the material in PO
 Vendor Materials.

- If you did not enter a material for this purchase
 order item, this field defaults as blank.

## Receiving

Check this box if you will be receiving this item in the PO module (PO Receipts Entry or PO Initialize Receipts). Click [here](/en/vista/vista/costs-and-contracts/purchase-order/receiving/about-receiving-purchase-orders) for an overview on receiving purchase orders in the PO module.
Do not check this box if you will be using AP Transaction Entry to receive this item. Received and Backordered quantities are updated as Invoiced.
Note: This field will be disabled once you distribute the PO item (in PO Item Distribution), receive the PO item (in PO Receipts Entry), or invoice the item (in AP Transaction Entry).

## Req Date

Enter the date this material is required.

## Pay Category

The Pay Category field on the SM Purchase Order Entry form, items Info
 tab.
This field is only enabled if the Using Payable
 Category checkbox is selected in AP Company Parameters (Pay
 Types/Discounts/ICR tab) and the Specify Pay Type during PO Entry checkbox
 is selected in PO Company Parameters.
Enter a valid pay category for this purchase
 order item or press F4 to select from a list of valid pay
 categories. The pay category specified here, along with the line type (Type field),
 determines the default pay type.
 Initially defaults the pay category as
 follows:

- Defaults the pay category assigned to the current
 user in VA User Profile.

- If a default pay category is not assigned to the
 user in VA User Profile, defaults the pay category defined in AP Company Parameters
 (in Payable
 Category Default field).

- If no default pay category is specified for the AP
 company, defaults as blank. If you leave blank, the pay type for this purchase order
 item defaults the SM Work Order pay type defined in AP Company Parameters.

## Pay Type

This field is only enabled if the Specify Pay Type during PO
 Entry box is checked in PO Company Parameters.
Enter the pay type for this purchase order item. Initially defaults the pay type as follows:

- If a pay category is assigned to this purchase order item, defaults the SM Work Order pay type assigned to the specified pay category.

- If a pay category is assigned to this purchase order item, but no SM Work Order pay type is defined for the pay category, this field defaults as null.

- If you did not enter a pay category for this
 purchase order item or if you are not using pay categories (i.e., the Using Payable
 Category box is unchecked in AP Company Parameters), this field
 defaults the standard SM Work Order pay type from AP Company Parameters.

If no SM Work Order pay type is specified in AP Company Parameters, this field defaults as null.

## UM

The UM field on the SM Purchase Order Entry form, items Info tab.

Enter a valid unit of measure for this purchase order item or accept the
 defaulted value.
Defaults are as follows:

- If you entered a valid material in the Material field, this field defaults
 the Purchase UM from HQ Materials.

- If you specified a non-valid material, this field defaults as EA.

- If overrides exist for the specified material/vendor in PO Vendor Materials (POVM),
 defaults the vendor material UM matching the Purchase UM in HQ Materials; if no match
 is found, defaults the lowest UM for the vendor/material group/material.

Note: This field will be disabled
 once you distribute the PO item (in PO Item Distribution), receive the PO item (in PO
 Receipts Entry), or invoice the item (in AP Transaction Entry).

## Units

The Units field on the SM Purchase Order Entry form, items Info tab.

This field is disabled if the UM is LS (lump sum)
Enter the number of units being purchased of this item or leave at 0.00 if this is a blanket (standing) PO.

- If UM is not LS and you leave the units at 0.00 (blanket PO), the Total must also be 0.00.

-  If you modify the original units/cost for a PO (regular or standing) after units have already been received, and it will cause the backordered units/cost to go negative, a warning is displayed; however, the entry is allowed.
Note: This field is disabled once a purchase order item is
 distributed (via PO Item Distribution) or if you apply a change order against the
 purchase order item (in PO Change Order Entry).

## UC

The UC field on the SM Purchase Order Entry form, items Info tab.
Enter the unit cost for this PO item or accept
 the defaulted value.
Initially defaults a unit cost as follows:

- If you entered a valid HQ material and the material's Purchase
 UM is equal to the Standard UM, defaults the standard unit cost defined in HQ
 Materials.

- If the Purchase UM is not equal to the Standard UM, defaults the
 unit cost defined on the Additional Units of Measure tab (in HQ Materials) for the
 Purchase UM.

- If pricing overrides exist in PO Category Discounts or PO Vendor
 Materials, defaults the unit cost as defined in the Category / Vendor Pricing
 Overrides section below.

- If you entered a non-valid material or did not enter a material,
 the unit cost defaults as 0.00.

Note: If the Purchase UM is not equal to the Standard UM,
 but the Purchase UM is not defined on the Additional Units of Measure tab, you will receive
 a message that the UM is not set up for the material, and you will be unable to save the
 record unless you either change the UM or set up the UM on the Additional Units of Measure
 tab in HQ Materials.

### Category / Vendor Pricing Overrides

If you have set up vendor pricing overrides in either PO Category
 Discounts or PO Vendor Materials, the system uses the overrides to default the unit cost
 for purchase order items.

- If a discount exists for the vendor and material category in PO Category
 Discounts, the system applies the discount to the standard unit price in HQ
 Materials to determine the default unit cost.

- If an override exists for the vendor/material group/material/UM in PO Vendor
 Materials, the unit cost defaults based on the specified Cost Option (Standard
 Unit Cost, Vendor's Unit Cost, Standard Book Price less discount, or Vendor's Book
 Price less discount).

- If overrides exist for the vendor/material in both PO Category Discounts and PO
 Vendor Materials, the unit cost is pulled from PO Vendor Materials.

- If the unit of measure is other than LS, and you enter a zero unit cost, the
 total cost must be zero. In addition, you will need to invoice the items to ensure
 that JCCD (Cost Detail) and POIT (PO Items) are in balance before you close the
 PO.

Note: If the unit of measure is other than LS and you enter a
 zero unit cost, the total cost must be zero. In addition, you will need to invoice
 the PO items to ensure that JCCD (Cost Detail) and POIT (PO Items) are in balance
 before you close the PO.

The system disables this field if any of the following conditions
 exist:

- The UM for the purchase order item is LS (Lump Sum)

- You distribute the purchase order item in PO Item
 Distribution

- The total costs are not equal

- You receive the purchase order item in PO Receipts Entry

- You invoice the purchase order item in AP Transaction
 Entry

- You selected to "Initialize Receipt Expenses" in PO Company
 Parameters

## ECM

 The ECM drop-down on the SM Purchase Order Entry form, items Info tab.

This field is disabled if the UM is LS (Lump
 Sum).
Specify which quantity the unit cost
 represents or accept the default.

- E - Per Each

- C - Per Hundred

- M - Per Thousand

This field is also disabled if any of the following conditions exist:

- You distribute the purchase order item in PO Item Distribution

- The total costs are not equal

- You receive the purchase order item in PO Receipts Entry

- You invoice the purchase order item in AP Transaction Entry

- You selected to 'initialize receipt expenses' in PO Company
 Parameters (File > Initialize Expenses on Receipt)

If you change this value, the system automatically updates the Total for the purchase order item. In addition, if you have already posted the purchase order, the system also updates the related cost and billing values on the work completed purchase line (Cost Subtotal, Cost Tax Basis, Cost Tax Amt, Bill Rate, etc.).

## Total

If the unit of measure is LS (Lump Sum), enter the total cost for this purchase order item.
If the UM is not Lump Sum, this field defaults an amount based on Units x (Unit Cost / ECM). Accept the default total or enter the new total. If you override the default, the unit cost will be recalculated.
 If you entered zero units and/or unit cost, the total cost must also be zero.
Note: This field is disabled if any of the following conditions exist:

- The UM for the purchase order item is not LS (Lump Sum)

- You distribute the purchase order item in PO Item Distribution

- You selected to "Initialize Receipt Expenses" in PO Company Parameters

## Tax Type

The Tax Type field on the SM Purchase Order Entry form, Items section, Info tab.

Required if specifying a tax code.
Note: Entry of an SM Cost Type is required if posting taxes to this purchase order item.

Select the tax type for this purchase order item or accept the defaulted value.

- 1-Sales – Tax amounts are payable to the vendor and are added to the purchase order total. This tax amount is directly charged to GL.

- 2-Use – Tax amounts are accrued and will be paid at a later date to the appropriate State or Local taxing authority. Calculated tax amounts do not affect the gross or net balance due to the vendor. Instead, the transaction's gross amount and tax amount is charged to GL account with an offsetting liability account as defined in HQ Tax Codes. Use the AP Tax Report to obtain an itemization of use tax amounts.

- 3-VAT – (Value Added Tax) - This tax applies to Australian and Canadian companies. It is paid on goods and services at each stage of production or distribution, and is based on the value added at each stage. This tax is tracked in GL and reduces the payment to a taxing authority through an Input Tax Credit (ITC). This tax is not directly expensed. Use the AP Value Added Tax Report to obtain an itemization of VAT amounts.

This field defaults based on the SM Cost Type entered for the purchase order item, and the Matl Tax Override and Tax Option Override options selected on the associated work order scope. You may override the defaults as needed.
The following table describes the default behavior for SM purchase order items.
SM Cost TypeMaterialTax Option OverrideMatl Tax OverrideDefault
Note: If the PO vendor is not assigned a tax code and the work order scope's tax source (service site or service center) is not assigned a tax code, all tax fields default as blank, but may be overridden.

Not TaxableBlankAllAllBlank
Not Taxable
Taxable
TaxableNot TaxableAllAllBlank
TaxableAllN - No TaxBlank
P - Taxable at Purchase Only, M - Taxable at Purchase/Markup at Billing, F - Full Tax at Purchase and BillingIf Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at Billing OnlyAllBlank
BlankP - Taxable at Purchase Only, M - Taxable at Purchase/Markup at Billing, F - Full Tax at Purchase and BillingIf Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at Billing OnlyAllBlank

Note: Once you save the PO and close the form, the system generates work completed purchase lines (in SM Work Orders) for each purchase order item. The tax type selected here displays in the Cost Tax Type field for the generated work completed purchase line.

Note: This field is disabled once you distribute the PO item (in PO Item Distribution), receive the PO item (in PO Receipts Entry), or invoice the item (in AP Transaction Entry).

## Tax Code

The Tax Code field on the SM Purchase Order Entry form, Items section, Info tab.

Entry in this field requires that you first enter a Tax Type.
If you are posting taxes to this purchase order item, specify a valid tax code (HQ Tax Codes) or accept the default. Must be a valid tax code for the specified tax type.
Note: Entry of an SM Cost Type is required if posting taxes to this purchase order item.

The system defaults the tax code as follows:

- If you specified a Ship Location (PO header) and the ship location is assigned a tax code, that tax code defaults here.

- If the ship location is not assigned a tax code or you do not specify a ship location, this field defaults the tax code from AP Vendors for the vendor specified in the PO header.

- If a tax code is not assigned to the vendor, this field defaults based on the Tax Type.

- If the tax type is Sales or VAT, this field defaults the Tax Code assigned to the work order's service site or service center, depending on the tax source specified for the work order scope.

- If the tax type is Use, this field defaults the Use Tax Code assigned to the service site or service center, depending on the scope's tax source. If no Use Tax Code is specified, it defaults the Tax Code specified for the tax source.

- If no tax codes (sales or use) are defined for the tax source, this field defaults as blank.

The tax code entered here displays in the Cost Tax Code field for the generated work completed purchase line (in SM Work Orders).

### Job Work Orders

The tax code default for job-related work orders is determined by the setting of the Base Tax On field in JC Jobs. Options are as follows:

- J-Job - The tax code defaults from JC Jobs ( Tax Code field). If no tax code is specified for the job, the default will be null.

- V-Vendor - The tax code defaults from AP Vendors ( Tax Code field). If a tax code is not specified for the vendor, the default will be null.

- O-Vendor Override - The tax code defaults from AP Vendors. If a tax code is not specified for the vendor, the tax code will default from JC Jobs. You can override the default as necessary.

### Intercompany Transactions

For intercompany transactions, the tax code defaults as follows:

- If the tax type is Sales or VAT (Value Added Tax), the tax code defaults based on the Tax Group assigned to the AP Company.

- If the tax type is Use, the tax code defaults based on the Tax Group assigned to the 'posted to' company.

### Redirect Phase/Cost Type

If the purchase order is for a job work order and the tax code for the purchase order line is assigned a redirect phase and/or cost type (in HQ Tax Codes), the system validates the phase and/or cost type based on the Phases on this job are locked checkbox in JC Jobs. Validation is as follows:

- Phases Locked - If the Phases on this job are locked checkbox is selected and the tax code specifies a redirect phase only, the phase must exist in JC Job Phases for the job specified on the work order. If the tax code specifies both a redirect phase and cost type, the phase/cost type combination must exist for the job in JC Job Phases. If the tax code specifies a redirect cost type only, the cost type must exist for the work order scope phase in JC Job Phases.

- Phases Not Locked - If the Phases on this job are locked checkbox is not selected and the tax code specifies a redirect phase only, the phase must exist for the job in JC Job Phases or JC Phases. If the tax code specifies both a redirect phase and cost type, the phase/cost type combination must exist for the job in JC Job Phases or JC Phases. If the tax code specifies a redirect cost type only, the cost type must exist for the work order scope phase in JC Job Phases or JC Phases.

## Phase

This field only displays if this purchase order is associated with a job work order.
 Display only, the phase assigned to the specified scope sequence.

## JC Cost Type

Required.
This field only displays if this purchase order is associated with a job work order.
Enter the JC cost type (from JC Cost Types)
 for this purchase order item or press F4 to select from a list of valid cost
 types for the phase or job phase. The cost type specified here defaults as the JC Cost Type
 on the work completed purchase line generated (during the batch process) for this PO
 item.
This field defaults as follows:

- If you specified an SM Cost Type for this purchase order item, this field defaults the JC Cost Type assigned to the SM cost type (in SM Cost Types).

-  If no JC cost type is assigned to the SM cost type or you did not assign an SM cost type to the PO item, this field defaults the Matl CT assigned to the material in HQ Materials.

-  If no Matl CT is specified in HQ Materials, this field defaults as blank.

If the job specified for the work order is locked (that is, the
 Phases on this job are locked
 checkbox is selected in JC Jobs), the cost type specified here must be set up for the
 job/phase in JC Job Phases. If the cost type is not set up for the job phase, you can add
 it by pressing F5 from this field
 to access JC Job Phases. Once you exit JC Job Phases, you can enter the cost type here.
If the job is not locked (that is, the Phases on this job are locked checkbox is
 not selected in JC Jobs), you can use any cost type defined for the phase in JC Job Phases
 or JC Phases.
Note: The system assigns the cost type
 specified here to the work completed purchase line generated (during the batch process)
 from this PO item. You can only make changes to the cost type at the PO item level here
 or in the PO Purchase Order Entry form; you cannot change the cost type at the work
 completed purchase line level.

Note: This field is disabled once
 you distribute the PO item (in PO Item Distribution), receive the PO item (in PO
 Receipts Entry), or invoice the item (in AP Transaction Entry).

## Job

The field on the SM Purchase Order Entry form, items Info tab.
This display-only field only appears if this
 purchase order is associated with a job work order.
Shows the job associated with the work order
 for this purchase order item.
