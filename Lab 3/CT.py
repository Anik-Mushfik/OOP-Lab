# a
class Message:
    def __init__(self, sender, recipient, content, timestamp):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = timestamp
# b
    def display_message(self):
        print(f"From:{self.sender}, To:{self.recipient}, Content:{self.content}, Sent at:{self.timestamp}")

    def update_message(self, new_content, new_time):
        self.content = new_content
        self.timestamp = new_time

    def __str__(self):
        return f"Sender: {self.sender} \nRecipient: {self.recipient} \nContent: {self.content} \nTime Stamp: {self.timestamp}"


# c
chat_1 = Message("Alice", "Bob", "Hello, how are you?", "12:30, 23/12/24")
# d
chat_1.display_message()
chat_1.update_message("Hello, Alice, how are you?", "12:30, 22/12/24")
chat_1.display_message()

# e
print(chat_1)