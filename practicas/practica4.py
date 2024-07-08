# Codigo de Arduino en Python con Tinkercad

# int Pin_A = 2;  
# int Pin_B = 3;  
# int Pin_C = 4;  
# int Pin_D = 5;  
# int Pin_E = 6;  
# int Pin_F = 7;  
# int Pin_G = 8;  

# const byte numeros[10][7] = {
#   {1, 1, 1, 1, 1, 1, 0}, // 0
#   {0, 1, 1, 0, 0, 0, 0}, // 1
#   {1, 1, 0, 1, 1, 0, 1}, // 2
#   {1, 1, 1, 1, 0, 0, 1}, // 3
#   {0, 1, 1, 0, 0, 1, 1}, // 4
#   {1, 0, 1, 1, 0, 1, 1}, // 5
#   {1, 0, 1, 1, 1, 1, 1}, // 6
#   {1, 1, 1, 0, 0, 0, 0}, // 7
#   {1, 1, 1, 1, 1, 1, 1}, // 8
#   {1, 1, 1, 1, 0, 1, 1}  // 9
# };

# int a = 5;
# int m = 32;
# int x = 25;

# void setup() {
#     pinMode(Pin_A, OUTPUT);  
#     pinMode(Pin_B, OUTPUT); 
#     pinMode(Pin_C, OUTPUT); 
#     pinMode(Pin_D, OUTPUT); 
#     pinMode(Pin_E, OUTPUT); 
#     pinMode(Pin_F, OUTPUT); 
#     pinMode(Pin_G, OUTPUT);  
# }

# void loop() {
#   int randomNumber = generateRandomNumber(); // Genera un número aleatorio
#   mostrarNumero(randomNumber % 10); // Muestra sólo el último dígito del número aleatorio generado
#   delay(1000); // Espera 1 segundo antes de generar el siguiente número
# }

# int generateRandomNumber() {
#   x = (a * x) % m; //
#     return x;
# }

# void mostrarNumero(int num) {
#     digitalWrite(Pin_A, numeros[num][0]);
#     digitalWrite(Pin_B, numeros[num][1]);
#     digitalWrite(Pin_C, numeros[num][2]);
#     digitalWrite(Pin_D, numeros[num][3]);
#     digitalWrite(Pin_E, numeros[num][4]);
#     digitalWrite(Pin_F, numeros[num][5]);
#     digitalWrite(Pin_G, numeros[num][6]);
# }