---
title: "PM Create & Send Data Sources Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form"
---

# PM Create & Send Data Sources Form

Use this form to create data sources.
Data sources define the relationship between the tables used to send merge information to the Word templates. They must be set up here before they can be referenced on a template.
Generally, you will only use this form if you want to pull information from custom tables (i.e. user-defined tables created via User Database). Vista™ comes with all document objects that are required for the standard template types. These document objects are identified by a “Standard Document Object” label (in red) to the right of the object name, and cannot be edited or deleted.

- Template Type - When setting up document objects, you must first specify the template type. Template types are predefined and refer to the type of templates available when using PM Create and Send. There are [eight standard template types](/en/vista/vista/project-management/create-and-send/template-types#reference-8869--en__reference-8869).

-  Document Object - Although there are no limitations on how you name your document objects, you typically will want to name them so they identify the information you are trying to pull. For example, if you are going to be using the "Subcontract with Items" template, and you want to include subcontract item detail (such as phase and cost type), your document object might be "Subcontract Item".

-  Linked Object - Linked objects establish the relationship between the document object and the object table (i.e., how you are going to join the document object with the object table). You cannot create linked objects; they must already exist in the Document Objects table for the specified template type. So, using the example above for the "Subcontract Item" document object, the linked object would be "Subcontract Header". This 'link' will provide the association between the subcontract item and the subcontract.

-  Object Table - This is the actual table from which the information you want will be pulled. You can only use valid Vistasoftware tables or custom tables (i.e., udXXXX). In our example, the object table would be "PMSL" (PM Subcontract Detail) because this is where subcontract items and their associated detail (phase, cost type, etc.) are stored.

-  Alias - The Alias identifies the object table. Although it will default a value based on the template type and existing alias values, you do have the option to assign your own value. However, it must be a value that is unique for the template type. You can use the F4 lookup to review the aliases already in use for the template type. You will also note that when you specify the linked object for the document object, the 'linked alias' (i.e., the alias assigned to the linked object) displays to the right. You will need this 'alias' in addition to the alias assigned to the object table when creating the join clause.

-  Join Clause - The join clause defines the relationship between the document object's table and the linked object's table when creating the query statement for the template type. For more information, see [Join Clause](/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form/field-definitions-create-and-send-data-sources-form#task-9934--en__task-9934).

[](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form)PM Create & Send Templates
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
