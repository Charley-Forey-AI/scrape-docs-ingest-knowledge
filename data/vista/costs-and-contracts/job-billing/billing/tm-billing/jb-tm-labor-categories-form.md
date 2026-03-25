---
title: "JB T&M Labor Categories Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-labor-categories-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-labor-categories-form"
---

# JB T&M Labor Categories Form

Use this form to set up labor categories for T&M billings.
Labor categories group specific labor information (payroll detail) together by class/craft, determining how labor details print on invoices. If you will use labor rates instead of actual costs for T&M billing, you must set up labor categories.
Setting up labor categories consists of two steps: creating a name and description for the category and then determining what payroll detail should be included in the category. Enter the name and description for the category in the Labor Category and Description fields. Use the Assignments tab to define payroll detail for the category.
The system uses labor class and craft information to define what payroll detail should be grouped into a category. When setting up labor categories, determine what craft and class information should be combined together on the invoice.
When assigning crafts and classes to a labor category (Assignments tab), use the ‘Restrict by Craft’ and ‘Restrict by Class’ options to control the selection of payroll detail by craft and class. You can elect to include all crafts and classes on a billing, specify individual classes for a craft or crafts for a class, or group all classes of a craft or crafts of a class together. When initializing billings, the system will include only job cost details that match the specified craft and class restriction.
The following list describes the available restriction options in the order in which they are applied during initialization:

- To restrict by both craft and class, check the Restrict by Craft and Restrict by Class boxes and specify the craft and class by which to restrict billings.

- To restrict crafts, but not classes, select the Restrict by Craft checkbox and leave the Restrict by Class box unchecked. Specify the craft to restrict by in the Craft field.

- To restrict by class, but not by craft, leave the Restrict by Craft box unchecked and select the Restrict by Class checkbox. Specify the class to restrict by in the Class field.

- To include all crafts and classes, leave both the Restrict By Craft and Restrict by Class checkboxes unchecked.
Note: Leaving both options unchecked is not recommended when using multiple billing rates.

The following example illustrates four labor categories made up from Payroll craft/class combinations set up in PR Craft Classes.
A. All Classes for the Craft of CARP will be pulled for the invoice (AP80, FORE, and JRNY)
B. All Crafts with a Class of JRNY will be pulled for the invoice (CARP, OPER)
C. Only the Craft of CARP and CCclass of JRNY will be pulled for the invoice
D. All Classes for all Crafts will be pulled for the invoice (AP80, FORE, JRNY for Craft of CARP and   FORE, GR01, JRNY for Craft of OPER)
