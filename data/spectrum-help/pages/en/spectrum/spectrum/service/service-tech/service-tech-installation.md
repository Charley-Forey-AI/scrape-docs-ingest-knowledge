---
title: "Service Tech Installation | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-tech/service-tech-installation"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/service/service-tech/service-tech-installation"
---

# Service Tech Installation

Use this screen to define Service Tech settings and selection options.
On this screen you can do the following, and more.

- Set up clock-in/clock-out dispatch statuses

- select a Crystal finished work order form

- decide whether to roll up technician's labor hours

- choose which dispatch status codes to exclude from reportingNote: Fields on this screen apply to Field Tech dashboard apps, Service Tech, and the Service Tech Mobile app. The field descriptions below specify requirements by product.

Field/ButtonDescription
Default dispatch status settings Important: These settings apply only to the Service Tech Mobile app, and are required in order for the auto status to work.
If you have access to the Dispatch Status Maintenance screen, you can add or edit dispatch status codes from the Dispatch Statuses window.
Clock-inSelect a default dispatch status code to be assigned when technicians clock in on a work order.Note: To add or edit dispatch status codes, go to Dispatch Status Maintenance > Dispatch Statuses.

Clock-out - assignments incompleteSelect a default dispatch status code to be assigned when a assignment isn't finished at the moment the technician clock-outs on a work order.
Clock-out - assignments completeSelect a default dispatch status code to be assigned when technicians clock out on a work order and all assignments are complete.
New work orderSelect a default work order status to be assigned when technicians generate a new work order for the current site or job.
Paid by credit cardSelect a default dispatch status code to be assigned when a work order is paid via credit card using the mobile app.Note: Your selection must be one of the status codes whose checkbox is selected in the Excluded status codes list.

Finished work order form
Custom Crystal report form?Select this checkbox to use a custom finished work order form, and then Select Form to choose the custom report.
Default e-mail bodyEnter any text you want included in the body of each email when the Finished Work Order form is sent to the customer.
Signature line textEnter the text that should appear on the signature capture widget in Service Tech and on the Finished Work Order Form.
Service Tech 'From e-mail'Enter the customer's email address for delivery of completed Work Order Forms.
Excluded status codesWork orders with any dispatch status whose checkbox is selected in this grid do not appear in the My Open Work Orders and My Other Work Orders dashboard apps, and are not accessible in the Service Tech Mobile app.
Hours adjustment at clock-outChoose whether to round technician labor hours up to the next quarter hour, half hour, or no rounding.
Log location when clock in or out?
Log location when sign finish work order form?
Select these checkboxes to log the technician's location at each event.
Payment collection
Enable mobile payment collection?
Select to enable field technicians to collect credit card payments using their mobile device.
Account IDEnter the Account ID that Stripe issued when you set up your account. It is formatted as acct_, followed by a string of alphanumeric characters.
