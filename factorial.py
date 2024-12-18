# Ζητάει από το χρήστη να εισάγει έναν αριθμό για να υπολογίσει το παραγοντικό του
num = int(input("Εισάγετε έναν αριθμό για να υπολογίσετε το παραγοντικό του:"))

# Ελέγξτε αν ο αριθμός είναι αρνητικός
if num < 0:
    # Εκτύπωση μηνύματος αν ο αριθμός είναι αρνητικός
    print("Το παραγοντικό δεν ορίζεται για αρνητικούς αριθμούς")
# Ελέγξτε αν ο αριθμός είναι 0
elif num == 0:
    # Εκτύπωση μηνύματος αν ο αριθμός είναι 0
    print("Το παραγοντικό του 0 είναι 1")
else:
    # Ορισμός της μεταβλητής result στο 1
    result = 1
    # Βρόχος από το 1 έως τον εισαγόμενο αριθμό (συμπεριλαμβανομένου)
    for i in range(1, num + 1):
        # Πολλαπλασιάστε το αποτέλεσμα με τον τρέχοντα αριθμό
        result *= i
    # Εκτύπωση του αποτελέσματος(παραγοντικό) του αριθμού2
    print("Το παραγοντικό του", num, "είναι:", result)