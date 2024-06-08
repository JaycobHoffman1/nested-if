# Task 1: Code Correction
'''
Buggy Code
-----------------------------------------------
attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
'''

# Corrected Code
print('Task 1: Code Correction')

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"

print(venue)


# Task 2: Venue Selection
print('Task 2: Venue Selection')

attendees = int(input("Enter number of attendees: "))

if attendees > 100:
    venue, audio_visual = "large hall", "complex audio system"
else:
    venue, audio_visual = "conference room", "projector"

print(f'The venue should be a {venue} and the audio/visual system should be a {audio_visual}.')


# Task 3: Catering Choices
print('Task 3: Catering Choices')

is_vegetarian = input('Do you prefer is_vegetarian food? (yes/no): ')

print('We recommend Veggie Delight Caterers.' if is_vegetarian == 'yes' else 'We recommend Gourmet Meals Caterers.')