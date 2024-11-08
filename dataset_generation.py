import random
import json

# Labels
labels = ["Book Search", "Order Status", "Review Submission", "Store Policy Enquiry"]

# Sample messages for each label
book_search_examples = [
    "I'm looking for the book 'The Catcher in the Rye'.",
    "Can you find me books by J.K. Rowling?",
    "I want to read something similar to '1984'.",
    "Do you have 'To Kill a Mockingbird' in stock?",
    "Can you recommend some books on science fiction?",
    "Where can I find 'The Lord of the Rings'?",
    "Tell me more about the book 'Pride and Prejudice'.",
    "Is there a book by George Orwell?",
    "Can you suggest books like 'Harry Potter'?",
    "I'm searching for a book titled 'War and Peace'.",
    "Can you help me find 'The Hobbit'?",
    "I'm looking for books by George R.R. Martin.",
    "Do you have 'Brave New World' in hardcover?",
    "I need to find books related to machine learning.",
    "Is there a book similar to 'The Alchemist'?",
    "Find me some bestsellers in the fiction category.",
    "Where can I find 'Sapiens: A Brief History of Humankind'?",
    "Can you recommend a good fantasy book?",
    "Do you sell 'The Da Vinci Code' by Dan Brown?",
    "I'm searching for a book titled 'The Picture of Dorian Gray'.",
    "Is there a biography of Albert Einstein?",
    "I want to buy 'Thinking, Fast and Slow'.",
    "Do you stock any books by Stephen King?",
    "Can you show me books that are available in the thriller genre?",
    "Please find me a list of popular science books."
]

order_status_examples = [
    "Can you check the status of my order #A123BC?",
    "Where is my order #B456DF? It’s been a week.",
    "I want to track my order #C789GH.",
    "Can you tell me when my order #D012IJ will arrive?",
    "Is my order #E345KL delayed?",
    "I haven’t received my package yet. Order #F678MN.",
    "How long does it take for delivery? My order is #G901OP.",
    "My order #H234QR hasn’t been shipped yet.",
    "I need to know the status of my order #J567ST.",
    "When will my order #K890UV be dispatched?",
    "What is the current status of my order #L901WX?",
    "How can I track my order #M234YZ?",
    "When will my order #N567AB arrive?",
    "I want an update on my order #O890CD.",
    "Can you check if my order #P123EF has shipped?",
    "What’s the delivery time for order #Q456GH?",
    "I haven’t received order #R789IJ yet.",
    "My order #S012KL is still showing pending. Why?",
    "Where is my order #T345MN?",
    "Can you tell me the expected delivery date for my order #U678OP?",
    "My package hasn’t arrived yet. Order number is #V901QR.",
    "Can I change the delivery address for order #W234ST?",
    "Has my order #X567UV been dispatched?",
    "Order #Y890WX seems delayed. Can you help?",
    "Please provide a status update for order #Z123YZ."
]

review_submission_examples = [
    "I loved 'The Great Gatsby'. Here's my review: A masterpiece!",
    "This is my review of '1984': It’s hauntingly relevant.",
    "I'd like to submit a review for 'Pride and Prejudice': Brilliant!",
    "Here’s my feedback for 'The Catcher in the Rye': Very relatable.",
    "Review for 'To Kill a Mockingbird': A timeless classic.",
    "My thoughts on 'War and Peace': A bit too long but amazing.",
    "Submitting a review for 'Harry Potter': Magical!",
    "I'd like to give a 5-star rating for 'The Lord of the Rings'.",
    "This is my review of 'Moby Dick': A thrilling adventure.",
    "Let me review 'A Tale of Two Cities': Emotional and powerful.",
    "Here's my review of 'The Shining': It’s chillingly good!",
    "I didn’t enjoy 'The Road'. Here's my review: Too bleak for my taste.",
    "This is my review for '1984': It's a timeless piece of literature.",
    "Review for 'The Catcher in the Rye': I found it overrated.",
    "I loved 'The Alchemist'. Here’s my review: Inspiring and profound.",
    "Submitting a 3-star review for 'The Great Gatsby': It's okay.",
    "Review for 'To Kill a Mockingbird': A must-read for everyone.",
    "Here’s my 5-star rating for 'The Lord of the Rings': Simply epic!",
    "This is my feedback on 'Moby Dick': It’s a classic but quite slow.",
    "Let me submit my thoughts on 'Pride and Prejudice': A true masterpiece.",
    "I'd give 'War and Peace' a 4-star rating: It’s long but worth it.",
    "Review of 'Harry Potter': Best book series ever!",
    "Let me submit a 2-star review for 'Dracula': Not what I expected.",
    "Review for 'A Tale of Two Cities': A beautiful narrative of love and sacrifice.",
    "I'm submitting a review for 'Frankenstein': A great take on humanity."
]

store_policy_enquiry_examples = [
    "What’s your return policy?",
    "How can I get a refund?",
    "What is your shipping policy?",
    "Do you offer free returns?",
    "How long do I have to return a book?",
    "Is there a refund option for damaged books?",
    "Can you explain the return process?",
    "Is there any charge for shipping?",
    "How soon can I get my money back on a return?",
    "What are the conditions for refunds?",
    "What is your policy on late returns?",
    "Can I return a book if it’s damaged?",
    "How long does shipping usually take?",
    "What are the conditions for a full refund?",
    "Is there a fee for returning a book?",
    "What’s your policy on international shipping?",
    "Can I cancel my order after it's shipped?",
    "How do I return an ebook?",
    "Is it possible to exchange a book instead of returning it?",
    "Do you offer refunds on digital purchases?",
    "What is your return policy for pre-owned books?",
    "Are there any shipping charges for orders over $50?",
    "Can I return a book without a receipt?",
    "How do I check the shipping status of my order?",
    "Are there restrictions on returning discounted books?"
]

# Create dataset
dataset = []

for message in book_search_examples:
    dataset.append({"message": message, "label": "Book Search"})

for message in order_status_examples:
    dataset.append({"message": message, "label": "Order Status"})

for message in review_submission_examples:
    dataset.append({"message": message, "label": "Review Submission"})

for message in store_policy_enquiry_examples:
    dataset.append({"message": message, "label": "Store Policy Enquiry"})

# Shuffle dataset for randomness
random.shuffle(dataset)

# Save to a JSON file
with open('synthetic_chatbot_training_data.json', 'w') as f:
    json.dump(dataset, f, indent=4)

print("Synthetic dataset generated and saved to 'synthetic_chatbot_training_data.json'")
