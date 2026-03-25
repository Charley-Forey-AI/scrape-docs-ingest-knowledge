---
title: "Create a Stored Procedure Success Message | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/create-a-stored-procedure-success-message"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons/create-a-stored-procedure-success-message"
---

# Create a Stored Procedure Success Message

When setting up a custom button that triggers a stored procedure, you can set up the stored procedure to return a success or failure message without raising an exception from the stored procedure, triggering a stack trace error.
Note: This is only an outline of
 the process. These steps do not give a detailed description and assume that you know
 how to write stored procedures and launch them using a custom button.

1. Add a parameter to a
 stored procedure named @ReturnMessage that is an output
 parameter.

1. Code the stored procedure to set the return message. If the message should not display, set it up as an empty string.

1. Code the stored procedure to return an integer to determine whether the message is a success message (0) or failure message (any number greater than 0).

1. When setting up the custom button in the [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form), add the return message parameter to the Parameters tab.

Related information

- [Set Parameters for Custom Form Buttons](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-parameters-for-custom-form-buttons)

- [VA Custom Form Buttons Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-form-buttons-form)
