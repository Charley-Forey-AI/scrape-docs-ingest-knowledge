---
title: "Determining Import Defaults | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/determining-import-defaults"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/determining-import-defaults"
---

# Determining Import Defaults

When creating an import template in IM Template, you can set import defaults for each field. Import defaults allow you to default specific values for blank values in the data file, or override values in the data file. You can define two default types for a template. User defaults allow you to specify a value to use as a default, while the Viewpoint default sets the import to use the Viewpoint system default for the field.
Setting User Defaults
To set a user default value, enter the value in the User Default Value field for the applicable record. During the import process (IM Import), the system will use this for all blank values for all instances of this field in the data file. If a value already exists in the data file, the import process will not use the user default value.
To override the data file’s value, regardless if there is an existing value or not, enter the value for the record in the User Default Value field and check the Overwrite Import Value box. During the import process, the system will use the user default value for all instances of this field in the data file.
If you want the template to be more flexible in defaulting data, select the Prompt on Import box and do not specify a user default. During the import process, the system displays the [IM User Input Detail](/en/vista/vista/administration/imports/processing/about-the-im-user-input-detail-form) form, where you can specify a value for the current import. When you enter a value in the IM User Input Detail form, the specified value becomes the imported value.
Note: Because the value you specify on the IM User Input Detail form becomes the imported value, it can be overridden if you specify a user default value in the User Default Value field (or you check the Use Viewpoint Default box) and check the Overwrite Import Value box.
Setting Viewpoint Defaults
To set the field to use the Viewpoint default, check the Use Viewpoint Default box. During the import process (IM Import), the system will use the Viewpoint default for all blank values for all instances of this field in the data file. If a value already exists in the data file, it will remain unchanged.
To override the data file’s value, regardless if there is an existing value or not, check both the Use Viewpoint Default and the Overwrite Import Value boxes.
Note: If you have entered a value in the User Default Value field, and have checked both the Use Viewpoint Default and the Overwrite Import Value boxes, the system will use the Viewpoint default.
The following table displays the import result based on various template settings.
User Default Value
Overwrite Import Value
Use Viewpoint Default
Importing Value
Import Result

(blank)
Not checked
Not checked
(blank)
Nothing imported

(blank)
Not checked
Not checked
2
Value from import file (2)

XYZ
Not checked
Not checked
2
Value from import file (2)

XYZ
Not checked
Not checked
(blank)
User default value (XYZ)

XYZ
Checked
Not checked
2
User default value (XYZ)

(blank)
Not checked
Checked
2
Value from import file (2)

(blank)
Not checked
Checked
(blank)
Viewpoint default value

XYZ
Checked
Checked
2
Viewpoint default value

(blank)
Checked
Checked
2
Viewpoint default value

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [Create an Import Template](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template)

- [Set Import Template Detail](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail)

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)

- [About the IM User Input Detail Form](/en/vista/vista/administration/imports/processing/about-the-im-user-input-detail-form)
