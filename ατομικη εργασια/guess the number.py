from flask import Flask, render_template, request
import random, datetime
app = Flask(__name__)
results_file = 'results.txt' # αρχειο στο οποίο αποθηκευονται τα αποτελέσματα
generated_number = random.randint(-100, 100) # ο τυχαιος αριθμός που πρεπει να βρουμε
current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") # Ημερομηνίας και ωρα η οποια παιξαμε το παιχνιδι, αναγραφεται στο αρχειο των αποτελεσματων 
results = []
@app.route('/', methods=["GET", "POST"]) # δημιουργια συνδεσμου η οποια θα μας οδηγει στο παιχνίδι 
def guessinggame():
    message = "" # εισάγει την εννοια των μυνηματων στον κώδικα
    
    if request.method == "POST":
        try:
            user_guess = int(request.form["guess"]) # ζηταμε απο τον χρηστη να εισάγει τον αριθμο για να χρησιμοποιηθει αργότερα στον κωδικα
            
            if user_guess > 100 or user_guess < -100:
                message = "Οι αριθμοί οποίοι εισάγεις, πρέπει να είναι μεταξύ του -100 και του 100"
            elif generated_number >= 0 and user_guess < 0:
                message = "Ο αριθμός που ψάχνεις δεν είναι αρνητικός"
            elif generated_number <= 0 and user_guess > 0:
                message = "Ο αριθμός που ψάχνεις δεν είναι θετικός"
            elif user_guess < generated_number:
                if generated_number - user_guess <= 10:
                    message = "Πλησιάζεις, ο αριθμός που ψάχνεις είναι λίγο μεγαλύτερος"
                else:
                    message = "Ο αριθμός που ψάχνεις είναι μεγαλύτερος"
            elif user_guess > generated_number:
                if user_guess - generated_number <= 10:
                    message = "Πλησιάζεις, ο αριθμός που ψάχνεις είναι λίγο μικρότερος"
                else:
                    message = "Ο αριθμός που ψάχνεις είναι μικρότερος"
            else:
                message = f"Συγχαρητήρια! Βρήκες τον σωστό αριθμό {generated_number}!"
                with open(results_file, 'a') as file: # ανοίγει το αρχειο των αποτελεσμάτων και γράφει αυτο που του υποδικνύουμε 
                    file.write(f"Μάντεψες τον αριθμό {generated_number} σωστά! Ήταν {current_time}\n")
                
        except ValueError: # σε περιπτωση που ο αριθμος δεν ειναι ακέραιος, ή που ο χρήστης καταλαθος πατησει καποιο πληκτρο, αναγραφεται το παρακατω μυνημα
            message = "Παρακαλώ εισάγετε έναν έγκυρο αριθμό."

    return render_template("guess_the_number.html", message=message) # χρησιμοποιει τα template και τα μυνηματα που γράφουμε, στον σύνδεσμο που δημιουργειται

if __name__ == '__main__':
    app.run(debug=True)