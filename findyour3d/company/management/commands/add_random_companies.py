import random

from django.core.management.base import BaseCommand

from findyour3d.company.models import Company
from findyour3d.users.models import User

names = ["Joanna", "Alexandria", "Morgan", "Jared", "Titus", "Ember", "Iris", "Ryan", "Amir", "Paisley", "Christian",
         "Mya", "Legend", "Arthur", "Asher", "Dalton", "Aiden", "Shane", "Isaac", "Kash", "Harrison", "Axel",
         "Marshall", "Jaxson", "Leila", "Daniela", "Cayden", "Kelsey", "Charlie", "Brooks", "Sawyer", "Abigail", "Luna",
         "Avery", "Harper", "Collin", "Maria", "Ivy", "Elizabeth", "Maximiliano", "Lilly", "Eleanor", "Elise", "Ayla",
         "Carmen", "Max", "Sienna", "Brianna", "Jason", "Genevieve", "Aubree", "Noah", "Kingston", "Emerson", "Jasmine",
         "Dean", "Erick", "Abel", "Mark", "Mariana", "Natalia", "Rylan", "Conner", "Eliana", "Andrew", "Elias",
         "Cecilia", "Briella", "Lorenzo", "Brady", "Kai", "Annabelle", "Dallas", "Holden", "Piper", "Bryson",
         "Adrianna", "Phoebe", "Nathan", "Benjamin", "Preston", "Aaron", "Grant", "Lydia", "Gracelynn", "Jordan",
         "Cash", "Savannah", "Aden", "Kyrie", "Abraham", "Mckenna", "Victoria", "Major", "Malik", "Violet", "Victor",
         "Chloe", "Ashlynn", "Jace", "Wesley", "Paige", "Allison", "Samuel", "Veronica", "Garrett", "Maddox", "Rosalie",
         "Raelynn", "Silas", "Mikayla", "Ximena", "Arabella", "Kameron", "Hazel", "Roman", "Ethan", "Beckett",
         "Barrett", "Chelsea", "Alayna", "Travis", "London", "Alexander", "Tyson", "Raymond", "Brian", "Bennett",
         "Delilah", "Nicholas", "Lucy", "Gia", "Allen", "Muhammad", "Jeremiah", "Rowan", "June", "Maddison", "George",
         "Journee", "Anastasia", "Aubrey", "Kaylee", "Alan", "Isla", "Rowan", "Hector", "Hayden", "Londyn", "Alexandra",
         "Maximus", "Alejandro", "Alison", "Erin", "Esther", "Aurora", "Annie", "Thomas", "Alex", "Jessica", "Daphne",
         "Jay", "Beau", "Christina", "Elle", "Mackenzie", "Richard", "Mateo", "Vera", "Jake", "Desmond", "Audrey",
         "Derek", "Danielle", "Isaiah", "Kathryn", "River", "Mckinley", "Miguel", "Jennifer", "Luis", "Delaney", "John",
         "Walker", "Kiara", "Colt", "Arielle", "Dante", "Sophia", "Angel", "Penelope", "Claire", "Jesse", "Logan",
         "Jack", "Olive", "Declan", "Ashley", "Heaven", "Madeline", "Tucker", "Anthony", "Peyton", "Emersyn", "Melanie",
         "Joseph", "Parker", "Jesus", "Fernando", "Lana", "Maverick", "Rhett", "Rory", "Eric", "Gunnar", "Owen",
         "Adriel", "Aria", "Cristian", "Brody", "Aylin", "Mila", "Kayleigh", "Rachel", "Caroline", "Gabriel", "Andrea",
         "Tessa", "Nina", "Nora", "Rebecca", "Liliana", "Killian", "Ashton", "Tobias", "Landon", "Elliott", "Kendall",
         "Cesar", "Emma", "Amira", "Tristan", "Brooke", "Reed", "Juliana", "Pablo", "Ryder", "Madilyn", "Everly",
         "Timothy", "Josiah", "Katelyn", "Kimberly", "Dakota", "Jordan", "Ella", "Jensen", "Lane", "Gabriela", "Leland",
         "Skyler", "Drew", "Camden", "Dominic", "Graham", "Alana", "Solomon", "Gunner", "Grayson", "Caiden", "Adan",
         "Reid", "Roberto", "Giovanni", "Stella", "Raelyn", "Francisco", "Diego", "Ashlyn", "Alexis", "Cheyenne",
         "Troy", "Serenity", "Thiago", "Elliot", "Jonathan", "Finn", "Drake", "Jada", "Frank", "Hailey", "Fatima",
         "Paul", "Makenna", "Nehemiah", "Emily", "Remington", "Emanuel", "Josue", "Naomi", "Lauren", "Charles",
         "Michelle", "Ava", "Camilla", "Addilyn", "Jose", "Scarlet", "Jade", "Reagan", "Levi", "Edwin", "Ricardo",
         "Marcus", "Eloise", "Quinn", "Austin", "Cohen", "Ian", "Aspen", "Jax", "Brandon", "Daisy", "Hope", "Isabelle",
         "Micah", "Damien", "Valeria", "Skye", "Michael", "Jayden", "Brielle", "Charlee", "Izabella", "Henry", "Aliyah",
         "Kamden", "Myles", "Braylon", "Arianna", "Kennedy", "Jocelyn", "Joshua", "Emiliano", "Kason", "Lola", "Shawn",
         "Brynn", "Bentley", "Jaxon", "Jase", "Evangeline", "Miriam", "Gage", "Riley", "Jeremy", "Julia", "Sydney",
         "Emilia", "Erik", "Maya", "Daleyza", "Kaleb", "Beckham", "Christopher", "Bradley", "Rylee", "Eduardo",
         "Gianna", "Connor", "Addison", "Brayden", "Braxton", "Liam", "Faith", "Cassidy", "Elaina", "Judah", "Talia",
         "Zoe", "Elliana", "Josephine", "King", "Gracie", "Trevor", "Jeffrey", "Alexa", "Kayla", "Jasper", "Eden",
         "Marley", "Trinity", "Zayden", "Diana", "Griffin", "Alyssa", "Emmett", "Dylan", "Tanner", "Jane", "Nadia",
         "Ryker", "Jayceon", "Ayden", "Edward", "Martin", "Julianna", "Camille", "Sadie", "Bailey", "Brooklyn",
         "Nicolas", "Gemma", "David", "Iker", "Alivia", "Anna", "Megan", "Charlotte", "Genesis", "Natalie", "Miranda",
         "Nicole", "Journey", "Seth", "Stephanie", "Catalina", "Brendan", "Karter", "Jaiden", "Melissa", "Alessandra",
         "Finley", "Clara", "Jenna", "Kaydence", "Javier", "Ezekiel", "Chance", "Fiona", "Nova", "Israel", "Sean",
         "Ruben", "Patrick", "Noelle", "Kate", "Lyric", "Valentina", "Adam", "Isabel", "Vivienne", "Greyson", "River",
         "Hudson", "Amy", "Aaliyah", "Lucia", "Xavier", "Jameson", "Jaden", "Trenton", "Kylee", "Lilliana", "Hannah",
         "Parker", "Sarah", "Mallory", "Caden", "Harley", "Kenzie", "Derrick", "Leo", "Matteo", "Haley", "Kellan",
         "Antonio", "Lilah", "Esteban", "Sebastian", "Jayce", "Juan", "Milo", "Omar", "Jackson", "Selena", "Riley",
         "Kayden", "Peter", "Orion", "Lena", "Daniella", "Porter", "Waylon", "Sergio", "Dawson", "Bianca", "Leonel",
         "Corbin", "Leon", "Kamila", "Blakely", "Cali", "Madeleine", "Nyla", "Knox", "Adalyn", "Allie", "Chase",
         "Fabian", "Jett", "Catherine", "Andre", "Lillian", "Luke", "Cora", "Dominick", "Carter", "Paislee", "Jayla",
         "Nathaniel", "Ruby", "Autumn", "Joaquin", "Amari", "Marco", "Clayton", "Kira", "Kyle", "Vanessa", "Tyler",
         "Quinn", "Jacob", "Cameron", "Katherine", "Dylan", "Camryn", "Angelina", "Amber", "Valerie", "Felix", "Cooper",
         "Sabrina", "Adaline", "Johnathan", "Bella", "Ellie", "Evan", "Kinsley", "Destiny", "Leslie", "Maci", "Amaya",
         "Ryleigh", "Mariah", "Harmony", "Paxton", "Karson", "Gabriella", "Cole", "Ali", "Carson", "Pedro", "Emilio",
         "Daniel", "Kinley", "Maxwell", "Mary", "Emmanuel", "Isabella", "Kennedi", "Xander", "Laura", "Kevin", "Daxton",
         "Luca", "Kaiden", "Alondra", "Julian", "Summer", "Callie", "Lexi", "Alice", "Georgia", "Madelyn", "Vivian",
         "Leilani", "Kaitlyn", "Keegan", "Alexis", "Jordyn", "Juliette", "Bryan", "Zander", "Ariana", "Ruth", "Peyton",
         "Kylie", "Kyleigh", "Logan", "Cruz", "Prince", "Messiah", "Romeo", "Matthew", "Finley", "Spencer", "Ada",
         "Stephen", "Sophie", "Avery", "Steven", "Weston", "Adalynn", "Rose", "Lincoln", "Elena", "Easton", "Dakota",
         "Ronan", "Heidi", "Lukas", "Alaina", "Zaiden", "Santiago", "Cadence", "Donovan", "Maggie", "Amelia", "Rylie",
         "Lucille", "Gabrielle", "Gracelyn", "Hadley", "Calvin", "Averie", "Phoenix", "Taylor", "Juliet", "Molly",
         "Everett", "Joel", "Adrian", "Sloane", "Gael", "Presley", "Oscar", "Julius", "Eli", "Skyler", "Rafael",
         "Adelynn", "Kendra", "Laila", "Simon", "Edgar", "Gideon", "Cody", "Zoey", "Shelby", "James", "Emery", "Jaylen",
         "Johnny", "Esmeralda", "Grady", "Ivan", "Sara", "Giselle", "Ariel", "Melody", "Angel", "Katie", "Kendrick",
         "Malia", "Grace", "Zane", "Mason", "Kade", "Athena", "Blake", "Hayden", "Nash", "Eliza", "Adelyn", "Eva",
         "Lyla", "Margaret", "Alexia", "Wyatt", "Paris", "Robert", "Nolan", "Khloe", "Kyla", "Arya", "Louis", "Alina",
         "Gavin", "Justin", "Madison", "Layla", "Aidan", "Archer", "Sawyer", "Vincent", "Evelyn", "Kenneth", "Samantha",
         "Nevaeh", "Brynlee", "Gregory", "Theodore", "Adelaide", "Raegan", "August", "Lila", "Miles", "Andres",
         "Brooklynn", "Jude", "Sage", "Zion", "Abram", "Colton", "Devin", "Zachary", "Makayla", "Felicity", "Caleb",
         "Aniyah", "Sofia", "Oliver", "Teagan", "Alicia", "Keira", "Landen", "Angelo", "Amanda", "Camila", "Elsie",
         "Adeline", "Reese", "Lia", "Elijah", "Amina", "Angela", "Ainsley", "Noel", "Leah", "Manuel", "Skylar", "Norah",
         "Enzo", "Mario", "Jorge", "Leonardo", "Haven", "Allyson", "Makenzie", "Annabella", "Kaden", "Kamryn", "Damian",
         "Walter", "Payton", "Amiyah", "Anderson", "Carly", "Jonah", "Malachi", "Bryce", "Atticus", "Adriana", "Clark",
         "Scarlett", "Emerson", "Kali", "Carlos", "Colin", "Andy", "Hunter", "Mia", "Lily", "Josie", "Charlie", "Ana",
         "Lucas", "William", "Willow", "Jacqueline", "Mckenzie", "Kyler", "Brantley", "Cade", "Myla", "Olivia",
         "Ezra", ]


class Command(BaseCommand):
    help = 'Adding packs of fake companies. and fake news! Sad! (c)'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, nargs='*', default=1)

    def handle(self, *args, **options):
        number = options['number']
        if isinstance(number, list):
            number = number[0]

        count_ = 0

        def get_name():
            return random.choice(names)

        def get_username(n):
            return '{}_{}'.format(n, random.randint(1, 9999))

        def get_email(u):
            return '{}@example.com'.format(u)

        for i in range(number):

            name = get_name()
            last_name = get_name()
            username = get_username(name)
            email = get_email(username)
            user_type = 2

            user = User.objects.create(username=username,
                                       name=name,
                                       user_type=user_type,
                                       email=email,
                                       is_active=True)
            user.set_password('1234567a')
            user.save()

            display_name = '{} {} LLC'.format(name, last_name)
            address_line_1 = 'USA, {}, NY'.format(random.randint(1, 9999))
            address_line_2 = '{} str, {}'.format(get_name(), random.randint(1, 9999))
            full_name = '{} {}'.format(name, last_name)
            phone = '+1{}'.format(get_name(), random.randint(1, 99999999))
            ideal_customer = random.randint(0, 2)
            is_cad_assistance = random.randint(0, 1)
            budget = random.randint(0, 4)
            material = random.randint(0, 19)
            top_printing_processes = [str(random.randint(0, 8)), str(random.randint(0, 8)), str(random.randint(0, 8))]
            d = "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium" \
                          " voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint " \
                          "occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt " \
                          "mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et " \
                          "expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque " \
                          "nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas " \
                          "assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis " \
                          "debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et " \
                          "molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut " \
                          "reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus " \
                          "asperiores repellat"
            lst_d = d.split(' ')
            random.shuffle(lst_d)
            description = ' '.join(lst_d)

            consideration = random.randint(0, 1)

            Company.objects.create(
                name=name,
                display_name=display_name,
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                full_name=full_name,
                email=email,
                phone=phone,
                ideal_customer=ideal_customer,
                is_cad_assistance=is_cad_assistance,
                budget=budget,
                material=material,
                top_printing_processes=top_printing_processes,
                description=description,
                basic_material=material,
                consideration=consideration,
                user=user,)
            count_ += 1
        print('Added: {}'.format(count_))
