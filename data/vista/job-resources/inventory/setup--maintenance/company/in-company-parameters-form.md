---
title: "IN Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form"
---

# IN Company Parameters Form

Use this form to set up the various control options for each Inventory company before you begin processing in the Inventory module.
The options you select on this form affect the way the Inventory forms work and how other modules such as General Ledger and Job Cost interact with this module. Security access to this form should be restricted to only the system administrator(s).
Set up the following information in these forms in
 Headquarters (HQ) module:

- HQ Company Setup – You must
 first create each company record that you use in the IN Company Parameters
 form.

- HQ Units of Measure – Set up the
 units of measure to use as you sell and buy materials. Units of measure must
 be set up in this form before conversion and unit price information can be
 modified for materials in HQ Materials.

- HQ Material Categories – Set up
 the different categories that you assign materials to in Inventory.

- HQ Materials – Set up all
 materials that you use throughout the software. Make sure you check the
 Stocked option for each material that you will stock and track in Inventory.
 If you do not check this option, the material cannot be used in
 Inventory.

Once you set up your company options, they are rarely changed. Changing an option may affect processing or stored information, so consider your changes carefully before you make them. If you want to change a setup option but are unsure of its affect on existing
 data in the system, contact Viewpoint Support to discuss implications.

## Auto-generating Material Order Numbers

You can have the system automatically generate material order number by selecting the Auto Generate MO#s checkbox (Info
 tab). Auto-generated material order numbers are based on the number specified in the
 Last Used
 MO# field. You must assign this number initially when setting up an
 Inventory company, but once processing begins, this number is updated each time a
 material order is entered (IN Material Order Entry). If you manually override a material
 order number, the system does not update the Last Used MO# field.
If you are using the Project Management module,
 consider how material order numbers are generated in the PM Company Parameters form. If
 the P-Project/Sequence option is selected in the MO Number Type drop-down, you should
 refrain from having IN automatically assign material order numbers. However, if the
 Auto-Number option is selected, you can use Inventory's 'auto-generate' feature.

## Workflow tab

If you have the Workflow module and are using the Process Workflow feature, you can use the Workflow tab to define which workflows apply to the entire company. The workflow processes set up here override the workflow processes set up using the Workflow tab on the HQ Company Setup form.Note: You can also set up company-level workflow processes using the Assigned Companies tab on the [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process) form.

Note: You can override the workflows defined at the company level by location in IN Locations.

For more information about the workflow process and hierarchy, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

Related information

- [About Pricing Options](/en/vista/vista/job-resources/inventory/setup--maintenance/company/about-pricing-options)

- [About the IN Monthly Reconciliation Form](/en/vista/vista/job-resources/inventory/monthly-reconciliation/about-the-in-monthly-reconciliation-form)
