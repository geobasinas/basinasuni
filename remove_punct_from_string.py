## Πρόγραμμα που αφαιρεί από μια πρόταση τα σημεία στίξης

# Ορίζουμε τα σημεία στίξης που θέλουμε να αφαιρέσουμε από την πρόταση
shmeia_stijhw = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Ζητάμε από τον χρήστη να εισάγει μια πρόταση που περιέχει σημεία στίξης
protash = input("Δώσε μία πρόταση που να περιέχει σημεία στίξης: ")

# Ελέγχουμε κάθε χαρακτήρα της πρότασης
for shm in protash:
# Αν ο χαρακτήρας είναι σημείο στίξης, το αφαιρούμε από την πρόταση
    if shm in shmeia_stijhw:
        protash = protash.replace(shm, "")

# Εμφανίζουμε την νέα πρόταση χωρίς τα σημεία στίξης
print("Η νέα πρόταση χωρίς σημεία στίξης είναι: ", protash)


# Εναλλακτικά, μπορούμε να χρησιμοποιήσουμε την παρακάτω λύση
# new_protash = ""
# for char in protash:
    # if char not in shmeia_stijhw:
        # new_protash += char

# Εμφανίζουμε την νέα πρόταση χωρίς τα σημεία στίξης
# print("Η νέα πρόταση χωρίς σημεία στίξης είναι: ", new_protash)