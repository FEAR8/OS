// Sketch: Hello.ino
int const LED = 13;

void setup() { 
  pinMode(LED, OUTPUT);  // Corregido "pinmode" a "pinMode"
  Serial.begin(9600);    // Baudios
  digitalWrite(LED, LOW); // Corregido "digital.Write" a "digitalWrite"
  Serial.print("Hola");  // Añadido el punto y coma que faltaba
}

void loop() {
  // Código dentro del loop (si lo necesitas)
}
