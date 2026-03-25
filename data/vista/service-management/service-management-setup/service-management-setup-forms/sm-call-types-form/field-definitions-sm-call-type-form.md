---
title: "Field Definitions: SM Call Type Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-call-types-form/field-definitions-sm-call-type-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-call-types-form/field-definitions-sm-call-type-form"
---

# Field Definitions: SM Call Type Form

The following is a list of field descriptions for the SM Call
 Type form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Call Type

The Call Type field on the SM Call Types form.
Enter a number or code, up to 10 characters, to identify this call type. Call types represent the types of work you perform when making service calls. Some examples of call types might be:
Type
Description

AHService
After Hours Service

COMMain
Commercial Maintenance

RESMain
Residential Maintenance

HVACRepair
HVAC Repairs

WARR
Warranty Work

## Description

The Description field on the SM Call Types form.
Enter a description to identify this call type, up to 60 characters.

## SM Call Type Category

The Call Type Category field on the SM Call Types form, Info tab.
Enter a call type category. Press F4 for the SM Call Type Category Lookup form. Press F5 to connect to the SM Call Type Category form.

## Track WIP

The Track WIP checkbox on the SM Call Type form.
Select this checkbox to track WIP account updates for this call type when capturing and billing work completed for a work order. When entering and saving work completed lines referencing this call type, the system will update the Cost WIP account specified for the work completed line. When you bill the line, the system updates the Revenue WIP account, unless the scope is closed, in which case it updates the Revenue account instead. Once you close the scope, the system will transfer costs and revenue from the WIP accounts to the Cost and Revenue accounts, respectively.
Do not select this checkbox if you are not tracking WIP for this call type. When entering and saving work completed lines referencing this call type, the system will update the Cost account specified for the work completed line; billing the work completed line will update the specified Revenue account. The Cost WIP and Revenue WIP accounts will not be used.

## Active

The Active checkbox on the SM Call Types form.
Select this checkbox to activate this call type. Once activated, it will be available for selection when assigning call types to service centers (in SM Service Centers), divisions (in SM Divisions), and/or work orders (in SM Work Orders), and will be included in call type lookups.
Do not select this box if you are not ready to activate this call type. Call type will not be available for selection when assigning call types to service centers, divisions, or work orders, and will not be included in call type lookups.

## Prevent Scope Auto Close when Billing

Prevent Scope Auto Close when Billing checkbox on the SM Call Types form, Info tab.

Select this checkbox to prevent scopes with this call type from automatically closing when fully billed. When you fully bill the work order scope, the system leaves the work order scope open, even if you selected the Auto Close Work Order on Final Bill checkbox in SM Company Parameters. You will need to manually close the work order scope.
If you leave this checkbox unselected and you selected the Auto Close Work Order on Final Bill checkbox in SM Company Parameters, upon fully billing work order scopes with this call type, the system will auto-close the work order scope.
Note: If the Auto Close Work Order on Final Bill checkbox is not selected in SM Company Parameters, you must manually close work order scopes, no matter how you set this checkbox.

## Matl Tax Override

The Matl Tax Override drop-down on the SM Call Types
 form.

Select the tax type override default for agreement services, work order quote scopes, and work order scopes that reference this call type.
The option selected here is used to determine the Tax Type default when entering taxable material-related work completed for a work order (those with a material SM Cost Type).

- Blank – Use the standard tax type defaulting behavior. For taxable material-related work completed lines, the tax type defaults as Sales. For non-taxable material-related work completed lines, the tax type defaults as blank.

- N - No Tax – Default the tax type as "blank" for material-related work completed lines.

- S - Sales Tax Only – Default the tax type for taxable material-related work completed lines as Sales (US) or VAT (AU/CA).

- U - Use Tax Only (US companies only) – Default the tax type as Use for taxable material-related work completed lines.

## Tax Option

The Tax Option drop-down on the SM Call Types
 form.

Select the default taxability option for this call type. The option you select
 here determines whether a work completed line associated with this call type
 is taxable, and if so, when to apply the tax defaults.
You can override the tax option at the agreement, agreement service, work order
 quote, or work order scope level. If you do not specify an override option,
 the system uses the tax option specified for the call type associated with
 the work order scope.

- N - Not Taxable - Do not apply taxes at the time of purchase or billing. The cost and billing tax types and tax codes default as blank, regardless of whether the SM cost type specified for the work completed line is taxable. You may override the defaults as needed.

- P - Taxable at Purchase Only - Apply taxes at the time of purchase only. If the cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope and the Cost Tax Code defaults from the service site or service center depending on the Tax Source defined for the work order scope. The billing tax type and billing tax code default as blank. If the cost type is not taxable or no cost type is specified, all tax fields default as blank. You may override as needed.

- B - Taxable at Billing Only - Apply taxes at the time of billing only. If the line's cost type is taxable, the billing tax type and billing tax code default to the Tax Type and Tax Code specified for the work order scope. The Cost Tax Type and Cost Tax Code default as blank. If the cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.

- M - Taxable at Purchase/Markup at Billing - Apply taxes at the time of purchase and also apply taxes to the markup amount at the time of billing. If the line's cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope and the Cost Tax Code defaults from the service site or service center depending on the Tax Source defined for the work order scope. The billing tax type and tax code default to the Tax Type and Tax Code specified for the work order scope; however, the tax basis defaults the markup amount only. If the line's cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.Note: For taxable purchases, the bill tax basis is reduced by the amount that was previously taxed at the time costs were recorded. If you did not capture taxes when recording costs, there is no credit to apply to the transaction at billing; therefore, the bill tax basis is calculated using the full billing subtotal, not just the markup.

- F - Full Tax at Purchase and Billing - Apply tax fully at time of purchase and at time of billing. If the line's cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope, and the Cost Tax Code defaults from the service site or service center, depending on the Tax Source defined for the work order scope. The billing tax type and billing tax code default to the Tax Type and Tax Code specified for the work order scope, and the tax basis defaults the full billable amount. If the line's cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.
