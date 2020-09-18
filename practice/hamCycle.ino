/*
Problems: 
-Ham decides to run the other direction 
*/

int ham = 7;
unsigned long time;
//Calculating the circumference of the wheel (11.43cm times pi)
float circ = 3.14 * 11.43; 

// Variables will change:
int counter = 0;   // counter for the number of button presses
int buttonState = 0;         // current state of the button
int lastButtonState = 0;     // previous state of the button

void setup() {
  Serial.begin(9600);
  pinMode(ham, INPUT);
  time = millis();
}

void loop() {
  // read the pushbutton input pin:
  buttonState = digitalRead(ham);

  // compare the buttonState to its previous state
  if (buttonState != lastButtonState) {
    // if the state has changed, increment the counter
    if (buttonState == HIGH) {
      // if the current state is HIGH then the button
      // wend from off to on:
      counter++;
      Serial.println(counter);
    }
  } 
  // save the current state as the last state,
  //for next time through the loop
  lastButtonState = buttonState;
  delay(1); // Delay a little bit to avoid bouncing
    
}
