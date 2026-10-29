def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)

#------------ Test case for participant cost ---------------#
# Normal attendees
cost = participant_cost(30, 800, 200) ; print(cost)  # ___ Expected result ==> 30000

# Zero attendees 
cost = participant_cost(0, 800, 200) ; print(cost)        # ____ Expected reult ==> 0

""" HANDCOVER_NOTE
 Component: participant_cost
Returns: "attendes * (food_per_person + transport_per_person)" 
Tests: Normal attendees and zero attendees
Issue: none """

""" The second component calculates the event total cost for the attendees, which is the 
Participant_cost + venue cost"""
def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    cost = participant_cost(attendees, food_per_person, transport_per_person)
    return cost + venue_cost

# Testing the event total
# For normal attendees
# Inputs                        Expected result
attendees = 20                  # 30000 + 10000
food_per_person = 1000          # = 40000
transport_per_person = 500
venue_cost = 10000
total = event_total(attendees, food_per_person, transport_per_person, venue_cost)
print(total)

# For zero attendees
# Inputs                        Expected result
attendees = 0                   # 0 + 10000
food_per_person = 1000          # = 10000
transport_per_person = 500
venue_cost = 10000
total = event_total(attendees, food_per_person, transport_per_person, venue_cost)
print(total)

""" HANDCOVER_NOTE
 Component: event_total
Returns: Cost + venue 
Tests: Normal attendee cost plus venue
       Zero attendees with a non-zero venue

Issue: none """