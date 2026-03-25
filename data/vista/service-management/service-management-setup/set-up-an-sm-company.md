---
title: "Set Up an SM Company | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company"
---

# Set Up an SM Company

You must set up each of the companies in which you will be creating work orders, capturing work completed, and generating invoices for billable work.

Each SM company you set up here must first be set up in the Headquarters (HQ) module.
For each Service Management company that you set up, you must define the various control options for processing transactions (such as default companies, audit options, invoice print options, etc), as well as the GL interface level and the email settings used for invoice delivery.

1. From the main menu, select Service Management > Programs > SM Company Parameters.

1. In the SM Co field, enter a valid HQ company or press F4 to select from a list of valid companies.

1. In the Default Companies section, enter the default GL, AR, AP, PR, IN, EM, and JC companies updated when processing transactions in this company. For more information, see the F1 help for these fields.

1. If you want to automatically create and process cost posting batches when entering work completed on a work order, select the Auto Post New Work Completed checkbox. If this checkbox is not selected, you must manually create and process cost posting batches for new work completed lines (in SM Work Order Cost Posting).

1. If you want batch audit reports saved and attached to the batch record when a batch is posted, select the Attach Batch Reports to HQ Batch Control checkbox (highly recommended). Since most SM batches are processed behind the scenes (without exposing the batch process form), this is the only way to access the batch reports

1. If you want the system to automatically add standard charges to agreement work orders when defined for the customer or service site, select the Apply Standard Charges to Agreement Work Orders checkbox.If this checkbox is not selected, you must manually add standard charges to agreement work orders. For more information see the [F1](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#ID-00042859--en) help.

1. If you want to auto-default agreement numbers on manually entered customer work order scopes for service sites included in Spot Coverage on a single active agreement (in SM Agreements, Spot Coverage tab), select the Default Agreement number on Work Order Scopes checkbox.If this checkbox is not selected, the Agreement field in SM Work Orders will always default as blank.

1. Select the Use Review Process checkbox to activate the SM billing review process for Work Order Billing.

1. Select the Auto Close Work Order on Final Bill checkbox to have the WO billing process close the work order when fully billed.

1. Select the Auto Delete Open Trips to automatically delete open trips when closing work orders on final billing or from the work order close form.

1. Select the Use Closest Open Month checkbox to use the closest open month for closing entries when closing work orders on final billing of from the Work Order Close form.

1. In the Credit Hold Use Closest Open Monthdrop down list, select for soft or hard credit hold:

- S - Soft Credit Hold - (default) Select this option to alert users that they are on credit hold

- H - Hard Credit Hold - Select this option to prohibit users on credit hold from creating new work orders

1. In the Revenue Recognition drop down list, select how to recognize revenue:

- B - As Billed - (default) select this option to have revenue recognized as it is billed

- C - As Costs Incurred - select this option to have revenue recognized as costs are incurred

1. In the Next Work Order Number field, enter the number with which to begin auto-numbering work orders. The system automatically updates this number each time you add a new work order using auto-numbering.If left blank, work orders are auto-assigned based on the highest existing number in the system.

1. In the Minimum WO Quote ID field, enter the number with which to begin auto-numbering work order quotes. The system automatically updates this number each time you add a new work order quote.If left blank, work order quote numbering will begin with '0'.

1. In the Default Trip Duration field, enter the number of hours to use as a default when creating trips in SM Dispatch Board using the drag and drop functionality.If you leave this field blank, the default duration will be 1 hour.

1. In the Default Receivable Type field, enter the receivable type to use when billing work orders and agreements for this SM company. Press F4 to select from a list of valid receivable types.

1. In the Default WO Invoice Report field, enter the default custom invoice report to use when printing work order invoices or press F4 to select from a list of valid custom reports.Leave this field blank to have the system use the standard SM Invoice report.

1. In the Def. Agreement Inv. Report field, enter the default custom invoice report to use when printing agreement invoices or press F4 to select from a list of valid custom reports.If you want to use the standard SM Agreement Invoice report or if you are not using the Agreements feature, leave this field blank.

1. In the Audit Options section, select the checkbox for each item you want audited when making additions, changes, and deletions in related forms. For information about the forms affected for each audit option, see the [F1 help](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#ID-00042904--en).

1. In the Default Invoice Print Options section, the Work Order Invoices and Agreement Invoices checkboxes default as selected. Leave the checkboxes selected if you want invoices printed automatically when posting invoice batches.

1. Select the Default Use Tax on Purchases checkbox to default use tax on material-related miscellaneous and purchase work completed lines when posting AP invoices or purchase orders. For more information about setting this checkbox, see [Default Use Tax on Purchases](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#ID-000428bb--en).

1. If you are using the Tasking feature for agreements, set the [Agreement Sync Options](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#ID-00042933--en) as applicable. For more information about the Tasking feature, see [Equipment Tasking](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking).

1. If you are using the WO Invoice Desc. Options feature to specify what SM company fields from related work orders, work order scope, trips and work completed lines will automatically be included in the SM Work Order Invoice description, see [Setting Company Defaults for Auto-Population of SM Work Order Invoice
 Description](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/setting-company-defaults-for-auto-population-of-sm-work-order-invoice-description).

1. [Set the interface options.](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/set-the-interface-options-for-an-sm-company)

1. [Set up the email parameters for invoice delivery](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/define-email-settings-for-invoice-delivery).

Related information

- [SM Company Parameters Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form)

- [HQ Company Setup Form](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)
