void setup() {
    pinMode(13, OUTPUT);
    Serial.begin(9600);
    Serial.println("$XXXX|YYYY|ZZZZ\\n");
}

void loop() {
    int x = analogRead(0);
    int y = analogRead(1);
    int z = analogRead(2);

    digitalWrite(13, HIGH);
    Serial.print("$");
    Serial.print((x * 5 / 1024.0) - 1.66);
    Serial.print("|");
    Serial.print((y * 5 / 1024.0) - 1.65);
    Serial.print("|");
    Serial.println((z * 5 / 1024.0) - 2.04);
    digitalWrite(13, LOW);
    delay(10);
}