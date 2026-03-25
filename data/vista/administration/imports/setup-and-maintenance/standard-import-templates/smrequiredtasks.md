---
title: "SMRequiredTasks | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/smrequiredtasks"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/smrequiredtasks"
---

# SMRequiredTasks

This is a direct import (i.e., data is uploaded directly to the data table) that allows for inserting new records and updating existing ones.
However, because required tasks can be set up for work orders, agreement services, work order quotes, and class maintenance tasks, this import requires a "parent type" to identify the table to which the record should be linked. Parent types are identified as follows:
Record Type
Parent Type

Work Orders
7

Agreement Services
9

Work Order Quotes
11

Class Maintenance Tasks
14

There are two methods by which you can designate the parent type for an import:

- Template Detail (Recommended) - If you regularly
 import required tasks for each of the record types indicated above, you can
 create a template for each type and then set the appropriate parent type for
 each template. For example, if you import required tasks for work order quotes,
 you could set up a template called "ReqTaskQuotes". Then in the Template Detail,
 you would set the User Default Value for the
 Parent Type Identifier (#200) to 11.

- Text File - Add a column for the parent type to your text file and supply the parent type for each applicable record. Then in the Template Detail, specify the column location. If your data format is Delimited, this will be the Record Column number. If your data format is Fixed Width, this will be the Beginning Position/Ending Position numbers.
