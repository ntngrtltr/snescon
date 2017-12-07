int dataClock = D5; //yellow
int latch = D6; //orange
int data = D7; //red

void setup(){
  Serial.begin(115200);
  
  pinMode(dataClock, OUTPUT);
  pinMode(latch, OUTPUT);
  pinMode(data, INPUT);

  
}

void loop(){
  if(Serial.read() == -1){
    return;
  }
  unsigned short buttonState = 0;
  
  digitalWrite(dataClock, HIGH);

  digitalWrite(latch, HIGH);
  delayMicroseconds(12);
  digitalWrite(latch, LOW);

  for(int i = 0; i < 16; i++){  
  
    int bitValue = pow(2, i);
    
    digitalWrite(dataClock, LOW);
    int value = digitalRead(data);

    if(value){
      buttonState = buttonState | bitValue;
    }

    delayMicroseconds(6);
    digitalWrite(dataClock, HIGH);

  }

  byte buff[2] = {buttonState >> 8, buttonState & 0x00FF};
  Serial.write(buff, 2);

  
}
