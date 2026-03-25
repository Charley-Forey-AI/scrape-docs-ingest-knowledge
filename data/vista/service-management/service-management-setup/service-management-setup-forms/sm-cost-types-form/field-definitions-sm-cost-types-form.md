---
title: "Field Definitions: SM Cost Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-cost-types-form/field-definitions-sm-cost-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-cost-types-form/field-definitions-sm-cost-types-form"
---

# Field Definitions: SM Cost Types Form

The following is a list of field descriptions for the SM Cost
 Types form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## SM Cost Type

The SM Cost Type field on the SM Cost Types form

Enter a number (0-32,767) to identify this cost type.

## Description

The Description field on the SM Cost Types form.

Enter a description of this cost type, up to 60 characters, that identifies a type of cost associated with SM work orders.

## SM Cost Type Category

The SM Cost Type Category drop-down on the SM Cost Types form.

Specify the cost type category that applies to this SM cost type. The cost type category identifies the type of costs being captured when the cost type is used on a work completed line (in SM Work Orders).

- L-Labor

- E-Equipment

- M-Material

- O-Other

- S-Subcontracts

Note: When entering work completed lines (in SM Work Orders), the work completed line type determines the category of cost type you can assign. For example, if the work completed line type is Labor, the cost type's category must be Labor. However, this does not apply to Misc or Purchase work completed lines; you can assign any cost type to these lines, regardless of category.

## JC Cost Type

The JC Cost Type field on the SM Cost Types form.

Enter the JC cost type (from JC Cost Types) to use as a default when referencing this SM cost type on work completed lines for a job work order. The system will use this cost type, in conjunction with the phase specified for the work order sequence, to post the costs to Job Cost (via the JC Cost Detail table).
Note: For work completed labor lines, the system will ony use this cost type if the labor code specified for the work completed line is not assigned a JC cost type.
For work completed purchase lines, the system ignores this cost type and instead, uses the JC Cost Type specified for the PO item; edits only allowed via SM PO Purchase Order Entry or PO Purchase Order Entry.

### Locked Phases vs. Non-Locked Phases

You can assign any valid cost type here; however, when adding work completed lines to a job work order, the system validates the cost type for the scope phase as follows:

- If the Phases on this job are locked checkbox is selected for the job in JC Jobs, the cost type must be set up in JC Job Phases for the phase specified on the work order sequence; otherwise, the system displays a warning and will not allow you to save the work completed record until you specify a valid job/phase cost type.

- If the Phases on this job are locked checkbox is not selected for the job in JC Jobs, the cost type must be set up in JC Job Phases or JC Phases for the phase specified on the work order sequence; otherwise, the system displays a warning and will not allow you to save the work completed record until you specify a valid phase cost type.

## Taxable for Sales or Use

The Taxable for Sales or Use checkbox on the SM Cost Types form.

Select this checkbox if this cost type is taxable.
Note: If this is a material-related cost type (that is, the cost type category is M-Material), selecting this checkbox enables the Material Taxability field.

Leave this checkbox unselected if this cost type is not taxable.

## Material Taxability

The Material Taxability drop-down on the SM Cost Types form.
This field only displays for SM cost types with a Material cost type category and is only enabled when you select the Taxable for sales or use checkbox.
Select the taxability option for work completed lines using this material-related SM cost type:

- Blank – Select this option to use the standard tax type defaulting behavior.

- S - Sales Tax Only – Select this option to allow only Sales tax.

- U - Use Tax Only (US companies only) – Select to only allow Use tax.

- B - Both Sales and Use Tax – Select to allow either Sales or Use tax.
