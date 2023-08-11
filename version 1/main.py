import random
from datetime import datetime, timezone, timedelta

class AstrologyDice:
    def __init__(self, dice_faces):
        self.dice_faces = dice_faces

    def roll(self, user_input):
        current_time = datetime.now(timezone.utc) + timedelta(hours=8)  # Adjusted for UTC+8
        timestamp = current_time.timestamp()

        random.seed(int(timestamp * 1e8) + user_input)  # Seed with timestamp and user input
        random_index = random.random() * len(self.dice_faces)

        selected_index = int(random_index) % len(self.dice_faces)
        return self.dice_faces[selected_index]

# Define symbols for each astrology component
zodiac_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
houses = ["1st House", "2nd House", "3rd House", "4th House", "5th House", "6th House", "7th House", "8th House", "9th House", "10th House", "11th House", "12th House"]

# Explanations for each zodiac sign
zodiac_explanations = {
    "Aries": "Energetic, courageous, and impulsive. Aries individuals are known for their drive and determination, always eager to take on new challenges.",
    "Taurus": "Practical, reliable, and sensual. Taurus individuals value stability and comfort, often enjoying the finer things in life.",
    "Gemini": "Adaptable, curious, and witty. Geminis are communicative and social, often having a wide range of interests and being skilled at making connections.",
    "Cancer": "Nurturing, empathetic, and intuitive. Cancers are known for their emotional depth and strong connections to their families and home.",
    "Leo": "Confident, charismatic, and creative. Leos love to be the center of attention and are often associated with leadership and self-expression.",
    "Virgo": "Analytical, practical, and detail-oriented. Virgos are focused on organization and perfection, often seeking to improve themselves and their surroundings.",
    "Libra": "Charming, diplomatic, and balanced. Libras are known for their desire for harmony and fairness, often seeking to create peace in their relationships.",
    "Scorpio": "Intense, intuitive, and passionate. Scorpios have a powerful and mysterious nature, often driven by their emotions and deep connections.",
    "Sagittarius": "Optimistic, adventurous, and philosophical. Sagittarians love to explore and expand their horizons, often seeking deeper meanings in life.",
    "Capricorn": "Practical, disciplined, and ambitious. Capricorns are focused on achieving their goals and are often associated with hard work and determination.",
    "Aquarius": "Innovative, independent, and humanitarian. Aquarians are known for their unique ideas and desire to make the world a better place.",
    "Pisces": "Compassionate, imaginative, and intuitive. Pisces individuals are often dreamers with a strong connection to their emotions and the spiritual realm."
}

# Explanations for each planet
planet_explanations = {
    "Sun": "Represents self-expression and identity. The Sun is the core of a person's character and vitality, reflecting their essence and purpose in life.",
    "Moon": "Represents emotions and inner feelings. The Moon influences a person's emotional landscape, reflecting their subconscious and instincts.",
    "Mercury": "Represents communication and intellect. Mercury influences how a person thinks, communicates, and processes information.",
    "Venus": "Represents love and beauty. Venus governs relationships, aesthetics, and one's values, reflecting how a person seeks harmony and connection.",
    "Mars": "Represents energy and passion. Mars influences one's drive, courage, and assertiveness, reflecting how a person takes action and pursues goals.",
    "Jupiter": "Represents expansion and growth. Jupiter is associated with luck, abundance, and philosophical exploration, reflecting how a person seeks expansion.",
    "Saturn": "Represents responsibility and discipline. Saturn influences structure, limitations, and life lessons, reflecting how a person deals with challenges.",
    "Uranus": "Represents innovation and change. Uranus governs uniqueness, rebellion, and sudden insights, reflecting how a person embraces change.",
    "Neptune": "Represents spirituality and illusion. Neptune influences dreams, intuition, and imagination, reflecting how a person connects to the unseen.",
    "Pluto": "Represents transformation and regeneration. Pluto governs deep changes, power dynamics, and rebirth, reflecting how a person evolves and transforms."
}

# Explanations for each house
house_explanations = {
    "1st House": "Represents self-image and personality. The 1st House reflects how a person presents themselves to the world and their overall identity.",
    "2nd House": "Represents resources and values. The 2nd House governs finances, possessions, and personal values, reflecting how a person values stability.",
    "3rd House": "Represents communication and learning. The 3rd House influences communication, short trips, and learning experiences, reflecting how a person gathers information.",
    "4th House": "Represents home and family. The 4th House governs one's roots, family life, and emotional foundation, reflecting how a person finds security.",
    "5th House": "Represents creativity and pleasure. The 5th House influences self-expression, romance, and leisure activities, reflecting how a person seeks joy.",
    "6th House": "Represents work and health. The 6th House governs daily routines, health, and service, reflecting how a person approaches responsibilities.",
    "7th House": "Represents partnerships and relationships. The 7th House influences one-on-one connections, partnerships, and marriage, reflecting how a person relates to others.",
    "8th House": "Represents transformation and shared resources. The 8th House governs deep changes, shared resources, and intimate connections, reflecting how a person handles transformation.",
    "9th House": "Represents higher learning and exploration. The 9th House influences travel, philosophy, and seeking truth, reflecting how a person expands their horizons.",
    "10th House": "Represents career and public image. The 10th House governs one's public life, reputation, and career, reflecting how a person is perceived by the world.",
    "11th House": "Represents social groups and aspirations. The 11th House influences friendships, groups, and ideals, reflecting how a person connects to society.",
    "12th House": "Represents spirituality and subconscious. The 12th House governs hidden matters, spirituality, and inner reflection, reflecting how a person connects to the unseen."
}

# Create instances of AstrologyDice for each component
zodiac_dice = AstrologyDice(zodiac_signs)
planet_dice = AstrologyDice(planets)
house_dice = AstrologyDice(houses)

# Get user input (you can replace this with any input method you prefer)
user_input = int(input("Enter a random number: "))

# Roll the dice for each component with user input
rolled_sign = zodiac_dice.roll(user_input)
rolled_planet = planet_dice.roll(user_input)
rolled_house = house_dice.roll(user_input)

# Print the result along with explanations
print("Zodiac Sign:", rolled_sign)


print("Planet:", rolled_planet)


print("House:", rolled_house)
print('\n')

print("Zodiac Sign Meaning:", zodiac_explanations.get(rolled_sign, "No meaning available."))
print("Planet Meaning:", planet_explanations.get(rolled_planet, "No meaning available."))
print("House Meaning:", house_explanations.get(rolled_house, "No meaning available."))
