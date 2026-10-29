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