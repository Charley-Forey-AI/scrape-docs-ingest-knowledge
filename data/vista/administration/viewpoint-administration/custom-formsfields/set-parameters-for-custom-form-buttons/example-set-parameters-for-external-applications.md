---
title: "Example: Set Parameters for External Applications | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-external-applications"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/example-set-parameters-for-external-applications"
---

# Example: Set Parameters for External Applications

This example discusses creating a button on PM Contracts to open a third-party estimating application and pass parameters for the login name and password.
For a button that opens an external application, you want to pass parameters to this application and should understand the types of parameters that the application will accept. The way in which you configure parameters depends on the application that you are passing information to. The external application must have some way of receiving and processing parameters.

1. On the Info tab in VA Custom Form Buttons, create the custom form button. Make sure to specify PM Contracts as the form you are placing the button on, and the third-party application in the Action field.

1. On the Parameters tab, in the Parameter ID field, enter a + to create a new entry and have the system automatically assign the next available ID number.

1. Enter the name of the third-party application’s login field in the Name field.

1. Select 0-Fixed Value from the Default Type dropdown.

1. In the Default Value field, enter the login name to pass to the third-party application.

1. Repeat steps 4 – 6 to create a parameter for the password.

1. Save the record.

1. Open PM Contracts and reposition the button, as necessary.

1. Select the custom button. The system opens the third-party application with the login and password fields populated with the default values you specified on the Parameters tab.
