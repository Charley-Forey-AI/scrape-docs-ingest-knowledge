---
title: "About the EM Miles By State/ EM Kilometers by State/EM Kilometers by Province Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-miles-by-state-em-kilometers-by-stateem-kilometers-by-province-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-miles-by-state-em-kilometers-by-stateem-kilometers-by-province-form"
---

# About the EM Miles By State/ EM Kilometers by State/EM Kilometers by Province Form

Use this form to post mileage by state/province.
Posting mileage is useful for creating IFTA
 (International Fuel Tax Agreement) reports or other required state/province reports. You
 can access this form from the EM Programs menu or by selecting File  >  Miles by
 State from [EM Meter
 Readings ](/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-meter-readings-form) or [EM Fuel
 Posting ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form).
The title of this form differs depending on the
 Default
 Country specified in HQ Company Setup. Titles are as follows:

- United States - EM Miles by State

- Australia - EM Kilometres by State

- Canada - EM Kilometres by Province

Note: This is a stand-alone form; that is, it pulls information
 from and updates itself (via the EMSM and EMSD tables). Therefore, when entering a new
 record, the Begin Odo field will default the End Odo reading from the 'miles by
 state' posting, rather than the current odometer reading from EM Equipment (EMEM). If
 you have replaced the odometer, it is suggested that you post a single entry to bring
 the Begin Odo current with the last reading taken before the meter was replaced. Then
 post another entry to manually reset the Begin Odo reading to whatever the new meter was
 at the time of replacement and the End Odo to the meter's current reading.

## Header

Use the header section to specify the equipment for which you are posting mileage,
 the reading date, and the equipment’s beginning and ending odometer readings. The
 system uses the odometer readings to determine the Total Miles (displayed above
 header) posted to the equipment for the current transaction.

## Info

This section allows you to enter the
 individual usage transactions. In addition to the usage date, you specify the state
 to which the mileage applies, the miles driven with a full load, the miles driven
 unloaded, and the miles driven off road (section of road not considered a main
 highway or thoroughfare, such as a logging road). If the state for which you are
 posting mileage does not require a breakdown of loaded vs. unloaded miles, you can
 enter both loaded and unloaded mileage in the ‘Loaded’ field.
When entering the mileage for each line
 (loaded, unloaded, and off-road), you will note that the ‘Undistributed’ value
 (above the line section) reflects all previously entered lines. Initially, this
 amount will default the Total Miles for the equipment. As you enter and save each
 line, the combined total of loaded, unloaded, and off-road mileage for that line is
 subtracted from 'Undistributed' amount, with the result being the number of miles
 that have yet to be distributed (accounted for). You can enter as many lines as
 necessary to distribute the total mileage. When you are ready to post the batch, if
 the ‘Undistributed’ amount does not equal 0.00, a message displays indicating that
 there are undistributed or over-distributed miles left in the batch. You have the
 option to ‘cancel’ the operation and return to the batch to correct the error
 (recommended) or to continue processing the batch. If you click ‘Cancel’, the EM
 Batch Warnings window displays, providing a list of the sequences in the batch that
 are out of balance. Information shown includes the equipment, total miles, and
 undistributed amount.
Once you have entered the mileage for
 all applicable equipment, you can post the batch (EM Batch Process) as normal. Since
 the system only uses this information for reporting purposes, mileage entered here
 will not update equipment odometers.

Related information

- [About the EM Meter Readings Form](/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-meter-readings-form)
