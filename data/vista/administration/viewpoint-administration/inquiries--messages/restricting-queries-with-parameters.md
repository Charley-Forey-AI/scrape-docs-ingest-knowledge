---
title: "Restricting Queries with Parameters | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/inquiries--messages/restricting-queries-with-parameters"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/inquiries--messages/restricting-queries-with-parameters"
---

# Restricting Queries with Parameters

Use the Parameters tab of VA Inquiries to define parameter restrictions for records that the query returns.
Parameters act as placeholders. The parameter restrictions instruct the system on what data to display.

1. Create the query. For example, if you want to pull a company’s name and address from the HQ Company Parameters (HQCO) table, you might create the following query (and enter it in the Query Text field on the Info tab): Select Name as [Name], Address as [Address], City as [City] From HQCO Where HQCO=@company. In this example, the Where clause contains the @company parameter. When using this query, the system replaces the parameter with the value/restriction you define on the Parameters tab.

1. Enter a name for the parameter in the Parameter Name field on the Parameters tab of VA Inquiries. Using the above example, you would enter @company.

1.  If you want to use a predefined datatype, select the datatype (the data's format) in the Datatype field,. If you do not want to use a predefined datatype, leave this field blank. In the above example, you might specify the bHQCo datatype.

1. Determine if the restriction is based on a current system setting (e.g., active company, current date, etc.) or a specific value.

1. To base the restriction on a current system setting, select the setting from the Default Type drop-down list. In the above example, you could select 5-Active Company.The system automatically defaults the appropriate value in the Value field. To base the restriction on a specific value, leave the Default Type field blank and enter a value in the Value field. Using the example above, if you wanted the parameter to return all companies with a number less than 100, you would enter <100 in the Value field.

1. If you want users to be able to change the parameter for the Grid section of their Dashboard Work Center, check the Visible box. When users access the Grid section and select the Parameters tab, all parameters with the Visible box checked will display for that query. Note: When allowing users the ability to adjust parameter restrictions, make sure that the users understand how the parameter works and what restriction options are available. [More](/en/vista/vista/system-tools/work-centers/about-the-dashboard-work-center)

1. If you did not select a predefined datatype in step 3, enter the input details.

1. Select the input
 type from the Input Type drop-down.


1. Enter the length of the input in the Input Length field.

1. If you selected a numeric input type, select the [precision](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form/field-definitions-va-inquiries-form#ID-00048f79--en) from the Precision drop-down.

1. Optional: Enter a lookup that the parameter should use in the Lookup field. Press F4 to see a list of valid lookups.

1. Make sure a Where clause that specifies the parameter exists in the Query Text field on the Info tab.
