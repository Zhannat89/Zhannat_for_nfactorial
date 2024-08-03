class Movie:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Ticket:
    def __init__(self, user, movie):
        self.user = user
        self.movie = movie


class CinemaTicketSystem:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.tickets = {}
        self.next_movie_id = 1
        self.next_user_id = 1
        self.next_ticket_id = 1

    def addMovie(self, title):
        movie_id = self.next_movie_id
        self.movies[movie_id] = Movie(title)
        self.next_movie_id += 1
        return movie_id

    def addUser(self, name):
        user_id = self.next_user_id
        self.users[user_id] = User(name)
        self.next_user_id += 1
        return user_id

    def buyTicket(self, user_id, movie_id):
        if user_id in self.users and movie_id in self.movies:
            ticket = Ticket(self.users[user_id], self.movies[movie_id])
            ticket_id = self.next_ticket_id
            self.tickets[ticket_id] = ticket
            self.next_ticket_id += 1
            return ticket_id
        return None  # Return None if user or movie doesn't exist

    def cancelTicket(self, ticket_id):
        if ticket_id in self.tickets:
            del self.tickets[ticket_id]
            return True
        return False

    def showAllMovies(self):
        print("Available Movies:")
        for movie_id, movie in self.movies.items():
            print(f"{movie_id}. {movie}")

    def showAllBoughtTickets(self):
        print("Bought Tickets:")
        if not self.tickets:
            print("No tickets have been purchased.")
            return
        for ticket_id, ticket in self.tickets.items():
            print(f"Ticket ID: {ticket_id}, User: {ticket.user}, Movie: {ticket.movie}")


# Example usage
if __name__ == "__main__":
    cinemaSystem = CinemaTicketSystem()

    # Initial setup: adding movies
    movieId1 = cinemaSystem.addMovie("Inception")
    movieId2 = cinemaSystem.addMovie("The Matrix")
    movieId3 = cinemaSystem.addMovie("Interstellar")
    movieId4 = cinemaSystem.addMovie("The Godfather")

    # Show all movies after adding new ones
    cinemaSystem.showAllMovies()
    
    # Initial setup: adding users
    userId1 = cinemaSystem.addUser("Alice")
    userId2 = cinemaSystem.addUser("Bob")
    userId3 = cinemaSystem.addUser("Nurlan")
    userId4 = cinemaSystem.addUser("Diana")

    # Buying tickets
    ticketId1 = cinemaSystem.buyTicket(userId1, movieId1)  # Alice buys a ticket for Inception
    ticketId2 = cinemaSystem.buyTicket(userId2, movieId2)  # Bob buys a ticket for The Matrix
    ticketId3 = cinemaSystem.buyTicket(userId3, movieId3)  # Nurlan buys a ticket for Interstellar
    
    # Show all bought tickets
    cinemaSystem.showAllBoughtTickets()

   # Canceling a ticket
    print(cinemaSystem.cancelTicket(ticketId3))  # Returns True, ticket canceled
    print(cinemaSystem.cancelTicket(999))  # Returns False, ticket with such an ID not found

    # Show ticket cancellation confirmation
    print("Tickets after cancellations:")
    for ticket_id, ticket in cinemaSystem.tickets.items():
        print(f"Ticket #{ticket_id}: {ticket.user} - {ticket.movie}")