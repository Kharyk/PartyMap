# PartyMap

##Database Schema
This repository contains a database schema for a music event platform. The schema is represented as a diagram.

###Entities:

Schedule: Stores information about the schedule of the event.
Evant: Stores information about the event itself.
Tickets: Stores information about the tickets for the event.
Place: Stores information about the location of the event.
Organization: Stores information about the organization hosting the event.
Artist: Stores information about the artists performing at the event.
Group: Stores information about the groups of artists performing at the event.

###Relationships:

Evant has a one-to-many relationship with Tickets.
Evant has a one-to-many relationship with Artist.
Evant has a one-to-many relationship with Group.
Evant has a one-to-one relationship with Place.
Evant has a one-to-one relationship with Organization.
Artist has a one-to-many relationship with Group.


###Data Types:

bigint: Large integer value.
int: Integer value.
datetime: Date and time value.
text: Text string.

###Purpose:

This schema can be used to store and manage information about music events, including event details, tickets, location, organizers, artists, and groups.

###Future Improvements:

Add a User table to store information about event attendees.
Add a Review table to allow users to rate and review events.
Add a Payment table to track payments for tickets.
Add a Social Media table to store links to the event's social media accounts.

###Usage:

This schema can be used to create a database for an event platform.

###Status:

Development

![Screenshot 2025-01-31 23 32 29](https://github.com/user-attachments/assets/b7816dfd-f7a3-4a84-9e29-0f2ae1dd45d6)

