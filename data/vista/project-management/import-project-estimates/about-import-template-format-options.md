---
title: "About Import Template Format Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-import-template-format-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-import-template-format-options"
---

# About Import Template Format Options

For each template you set up, you must define the import routine and data format options.
The following is a list of routines currently provided with Vista™:

- Bid2Win (Bid2Win Estimating)

- Estimating (Viewpoint Estimating) 

- Generic (User Defined File Layout)

- HCSSHeavy (HCSS Heavy Bid)

- HardDollar (HardDollar Estimating)

- MEP Estimating (Viewpoint MEP Estimating) 

- Timberline (Timberline Precision Estimating)

- Accubid Estimating (Trimble MEP Estimating)

- Autobid Estimating (Trimble MEP Estimating)

- WinEst (Trimble GC Estimator)

- Quest (Trimble Estimating)

Each routine identifies the file format used when importing data from the specified third-party estimating package. For all routines except the Generic routine, the file format is predefined and cannot be changed. The Generic routine allows you to specify whether to use the Delimited or Fixed format (XML is not currently being used) and depending on the file format, the delimiter or column positions to use. You will typically use the Generic routine for importing data from spreadsheets and other third-party estimating packages that are not compatible with the specific packages indicated above, rather are designed to work with a standard layout. For more information, see [CSV (Generic) Layout](/en/vista/vista/project-management/import-project-estimates/csv-generic-layout)
In addition to the import routine, you also have the option to specify a user routine. User routines allow for additional functions (not included in the standard import routine) to be run at the end of the import process.
If you are adding a template that is an override to a standard template (used when establishing overrides for specific areas of work), check the ‘override template’ option, then indicate the standard template to which the override template is linked. The import process will look for cross-references on the override template first, and then look at the standard template for cross-references. For example, you set up a template using the HCSSHeavy import routine that references commonly used phase codes and cost types. However, you have a different set of phase codes/cost types that you use when doing bridgework. Therefore, you set up an override template that references the different set of phase/cost types, and link the template to the HCSSHeavy template.
