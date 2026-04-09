# EmailSpoof PoC

This is a simple **Proof of Concept (PoC)** for email spoofing.

> **Disclaimer**: This project is for educational and ethical testing purposes only. Unauthorized use is illegal.

## Usage

### 1. Initialize Postfix
The Postfix service must be running to handle mail transfer.

![image](https://github.com/user-attachments/assets/73233020-509d-45a6-9642-f0127971e614)

### 2. Help Menu
Use the `-h` flag to see the available options and required parameters.

![image](https://github.com/user-attachments/assets/96595eda-9335-4217-bf7d-07d037b62eb8)

### 3. Target Setup
For this PoC, a temporary email service is used to verify the receipt of the spoofed message.

![image](https://github.com/user-attachments/assets/f89083d5-5d2a-4fc1-a903-b4c15159bd87)

### 4. Sending the Email
Execute the script with the destination and source parameters.

![image](https://github.com/user-attachments/assets/3d5de164-74f5-4aa8-bdd4-cb3467f0c061)

### 5. Verification
The email is delivered to the target address displaying the spoofed metadata.

![image](https://github.com/user-attachments/assets/3ab90ec2-b94d-4c1e-b86b-b203c78293d1)
