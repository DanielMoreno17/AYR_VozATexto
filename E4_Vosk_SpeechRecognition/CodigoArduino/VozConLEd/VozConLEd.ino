#define LED_MOV_DERECHA 2
#define LED_MOV_IZQUIERDA 3
#define LED_AVANZAR 4
#define LED_REVERSA 5
#define LED_PRENDER_APAGAR 6

void setup() {
    pinMode(LED_MOV_DERECHA, OUTPUT);
    pinMode(LED_MOV_IZQUIERDA, OUTPUT);
    pinMode(LED_AVANZAR, OUTPUT);
    pinMode(LED_REVERSA, OUTPUT);
    pinMode(LED_PRENDER_APAGAR, OUTPUT);
    
    Serial.begin(9600); // Comunicación con Python
}

void loop() {
    if (Serial.available() > 0) {
        String comando = Serial.readStringUntil('\n');
        comando.trim();

        if (comando == "mover derecha") {
            digitalWrite(LED_MOV_DERECHA, 1);
            delay(1000); 
            digitalWrite(LED_MOV_DERECHA, 0);
        } 
        else if (comando == "mover izquierda") {
            digitalWrite(LED_MOV_IZQUIERDA, 1);
            delay(1000);
            digitalWrite(LED_MOV_IZQUIERDA, 0);
        } 
        else if (comando == "avanzar") {
            digitalWrite(LED_AVANZAR, 1);
            delay(1000);
            digitalWrite(LED_AVANZAR, 0);
        } 
        else if (comando == "reversa") {
            digitalWrite(LED_REVERSA, 1);
            delay(1000);
            digitalWrite(LED_REVERSA, 0);
        } 
        else if (comando == "prender cocina" || comando == "apagar cocina") {
            digitalWrite(LED_PRENDER_APAGAR, 1);
            delay(1000);
            digitalWrite(LED_PRENDER_APAGAR, 0);
        }
    }
}
