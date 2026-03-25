---
title: "Field Definitions: Create and Send Data Sources Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form/field-definitions-create-and-send-data-sources-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form/field-definitions-create-and-send-data-sources-form"
---

# Field Definitions: Create and Send Data Sources Form

The following is a list of field descriptions for the PM
 Create and Send Data Sources form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Template Type

 Press F4 to select the type of data source that
 you want to create. For example select PCO if you are creating a pending change
 order data source.
RFQs
There are two options that relate to RFQs:

- REQQUOTE - Select this option if
 you are creating a data source that you want to use with the enhanced PM Request For
 Quote form that was created in the 6.7.0 release.

- RFQ - Select this option if you are
 creating a data source that you want to use with the legacy PM Request For Quote -
 6.6 form.

Related Information
[](/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form)PM Create & Send Data Sources
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview

##  Document Object

 Enter
 the document object name, up to 30 characters. This can be any name; however, you might
 consider using a name that easily identifies the table from which you want to extract
 information or the information you are trying to extract. For example, if you are trying to
 extract information located in the JC Jobs, your document object name might be "Job
 Master".
Note: Viewpoint provides all document objects that are
 required for the standard template types. These document objects are identified by a
 “Standard Document Object” label (in red) to the right of the object name, and cannot be
 edited or deleted.

[](/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form)PM Create & Send Data Sources
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview

##  Object Table

 Required.
 Specify the table from which to pull the information. Must be a valid Vista table or user-defined table (i.e. udXXXX). Press F4 for a list of valid tables.

[](/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form)PM Create & Send Data Sources
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview

##  Linked Object

 Required.
 Specify a valid linked object for this document object. Press F4 for a list of valid objects for the template type.
 This linked object will establish the relationship between the document object and the object table specified below (i.e. how you are going to join the document object with the object table).

[](/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form)PM Create & Send Data Sources
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview

## Join Clause

The join clause defines the relationship between the document object's table and the
 linked object's table when creating the query statement for the template type.
In other words, it determines how the tables
 will associate records with each other by specifying a unique set of values that exist
 in both tables.
For example:
Template Type:
Submit

Document Object:
Contract Master

Linked Object:
Job Master (Linked
 Alias: b)

Object Table:
JCCM

Alias:
c

The object table for the Linked Object, Job Master,
 is JCJM (as defined when Job Master was set up as a document object). In order to
 establish a relationship between JCJM and JCCM to obtain the information we want, we
 need to create the following join clause (using the Alias to identify each table):
c.JCCo=b.JCCo and c.Contract=b.Contract
After you have defined document objects
 here, you can assign them to document templates to define the merge fields for your
 documents (IN Document Templates).

## Alias

Required.
Enter up to 2 letters to identify the object table. Defaults a sequential value based on the template type and existing aliases.
The 'alias' must be unique for the template type. Press F4 to review the aliases already in use for the template type. You will typically want to select the next sequential letter available.
Note:This alias, as well as the alias shown above for the 'linked object', will be used when creating the join clause.

[](/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form)PM Create & Send Data Sources
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview

##  Joins

 Display only.
 This section is displayed when you access the Joins tab, and shows all of the joins defined for this document object. Joins are based on the information entered for the document object on the Info tab.

[](/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form)PM Create & Send Data Sources
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
