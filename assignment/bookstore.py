import pickle
import json
from difflib import get_close_matches
import re
import spacy
from dateutil import parser
from datetime import datetime

class Bookstore:
    def __init__(self):
        with open('pipeSVC.pkl', 'rb') as model_file:
            self.message_model = pickle.load(model_file)

        with open('pipeSVCPolicy.pkl', 'rb') as model_file:
            self.policy_model = pickle.load(model_file)

        self.book_list = self.book_data()
        self.date_list = self.book_and_date()
        self.nlp = spacy.load("en_core_web_sm")

    # User message classification Method
    def text_classification(self, message):
        prediction = self.message_model.predict([message])[0]
        if prediction == 'Book Search':
            return f"""{prediction} \n
                        {self.book_search(message)}"""
        if prediction == 'Order Status':
            return f"""{prediction} \n
                        {self.order_status(message)}"""
        if prediction == 'Review Submission':
            return f"""{prediction} \n
                        {self.user_review(message)}"""
        if prediction == 'Store Policy Enquiry':
            return f"""{prediction} \n
                        {self.store_policy(message)}"""
        else:
            return "I'm sorry, I don't understand that question."
    
    # Book Search Method
    def book_search(self, message):
        # Find the closest matches
        try:
            # Use regex to find potential date parts in the message
            date_match = re.search(r'\b(?:\d{1,2}(?:st|nd|rd|th)?\s+\w+\s+\d{4}|\w+\s+\d{1,2},?\s+\d{4}|\d{4}-\d{2}-\d{2}|\d{2}-\d{2}-\d{4})\b', message, re.IGNORECASE)
            if date_match:
                # Parse the date using dateutil
                date = parser.parse(date_match.group())
                # Format the date in YYYY-MM-DD
                formated_date = date.strftime('%Y-%m-%d')
                return self.find_closest_date(formated_date)
            else:
                matches = get_close_matches(message, self.book_list, n=1, cutoff=0.2)  # `n` is the max number of results, `cutoff` is match quality
                return matches[0] if matches else "Book not found"
                
        except Exception as e:
            return f"Error parsing date: {e}"
        
        
        
    
    # Order Status Method
    def order_status(self, message):
        pattern = r'\b[A-Z]\d{3}[A-Z]{2}\b'
        match = re.findall(pattern, message)
        return match[0] if match else "Order number not found"
    
    # User Review Method
    def user_review(self, message):
        doc = self.nlp(message)
        review_start = False
        review = []

        for token in doc:
            # Look for keywords that indicate the start of the review
            if token.text.lower() in {"review", "about", "for", ":"}:
                review_start = True
                continue
            
            if review_start:
                review.append(token.text)

        return " ".join(review).strip()
    
    # Store Policy Method
    def store_policy(self, message):
        return self.policy_model.predict([message])[0]
        
    
    # Helper Function
    def book_data(self):
        with open('books.json') as f:
            data = json.load(f)
            book_list = []
            for book in data:
                book_list.append(book['book_title'])

        return book_list
    
    # Helper Function
    def book_and_date(self):
        with open('books.json') as f:
            data = json.load(f)
            date_list = []
            for book in data:
                date_list.append({"book": book['book_title'], "date": book['published_date']})
        
        return date_list
    
    # Helper Function
    def find_closest_date(self, formated_date):
        try:
            # Parse the user's input date
            target_date = datetime.strptime(formated_date, '%Y-%m-%d')
            
            # Convert each date in date_list to datetime and calculate the absolute difference
            closest_date_tuple = min(
                self.date_list,
                key=lambda d: abs(datetime.strptime(d['date'], '%Y-%m-%d') - target_date)
            )
            
            # Return the closest date in YYYY-MM-DD format
            return closest_date_tuple['date'], closest_date_tuple['book']
        
        except Exception as e:
            return f"Error: {e}"