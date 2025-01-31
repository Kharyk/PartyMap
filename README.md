# PartyMap

## Database Schema
This repository contains a database schema for a music event platform. The schema is represented as a diagram.

### Entities:

Schedule: Stores information about the schedule of the event.
Event: Stores information about the event itself.
Tickets: Stores information about the tickets for the event.
Place: Stores information about the location of the event.
Organization: Stores information about the organization hosting the event.
Artist: Stores information about the artists performing at the event.
Group: Stores information about the groups of artists performing at the event.

### Relationships:

The event has a one-to-many relationship with Tickets.
The event has a one-to-many relationship with Artist.
The event has a one-to-many relationship with the Group.
Event has a one-to-one relationship with Place.
The event has a one-to-one relationship with the Organization.
The artist has a one-to-many relationship with the Group.


### Data Types:

bigint: Large integer value.
int: Integer value.
DateTime: Date and time value.
text: Text string.

### Purpose:

This schema can be used to store and manage information about music events, including event details, tickets, location, organizers, artists, and groups.

### Future Improvements:

Add a User table to store information about event attendees.
Add a Review table to allow users to rate and review events.
Add a Payment table to track payments for tickets.
Add a Social Media table to store links to the event's social media accounts.

### Usage:

This schema can be used to create a database for an event platform.

### Status:

Development

![image](https://github.com/user-attachments/assets/d1d35416-586f-40a0-a163-b9b94442e20c)

