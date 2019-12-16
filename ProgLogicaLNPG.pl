/*Aritmética de Doar Sangue - Doador # Receptor*/

doa("A+", "A+").
doa("A+", "AB+").
doa("A-", "A+").
doa("A-", "A-").
doa("A-", "AB+").
doa("A-", "AB-").
doa("B+", "B+").
doa("B+", "AB+").
doa("B-", "B+").
doa("B-", "AB+").
doa("B-", "B-").
doa("B-", "AB-").
doa("O+", "O+").
doa("O+",  "A+").
doa("O+", "B+").
doa("O+", "AB+").
doa("O-", "TODOS").
doa("O-", "A+").
doa("O-", "A-").
doa("O-", "B+").
doa("O-", "B-").
doa("O-", "O+").
doa("O-", "O-").

pode(DOAR, RECEPTOR) :- doa(DOAR, RECEPTOR).
receber(RECEPTOR, X) :- doa(X, RECEPTOR).



