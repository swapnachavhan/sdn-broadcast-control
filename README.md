# 📡 SDN Broadcast Traffic Control

## Student Details

* Name: Swapna Chavhan
* USN: (Add your USN here)
* Course: Computer Networks Lab

---

## Problem Statement

Control excessive broadcast traffic in the network using Software Defined Networking (SDN).

---

## Objective

* Detect broadcast packets in the network
* Limit unnecessary flooding
* Apply selective forwarding rules
* Improve network performance

---

## Tools Used

* Mininet
* POX Controller
* Python 3.8
* Ubuntu Virtual Machine

---

## Description

In traditional networks, broadcast packets are sent to all devices which causes flooding and network congestion.
In this project, an SDN controller (POX) is used to detect broadcast packets and block them, reducing unnecessary traffic.

---

##  Steps to Run

### 1. Start POX Controller

cd ~/pox
python3.8 pox.py log.level --INFO openflow.of_01 broadcast_control

### 2. Run Mininet (in new terminal)

sudo mn -c
sudo mn --controller=remote --topo tree,depth=2

### 3. Test Connectivity

pingall

---

## Output

* All hosts are connected successfully
* Result shows 0% packet loss
* Broadcast packets are detected and blocked

---

## Screenshots

<img width="1052" height="627" alt="image" src="https://github.com/user-attachments/assets/ba4f9a1a-e33d-4d82-aa96-4374484eaa84" />


<img width="816" height="565" alt="image" src="https://github.com/user-attachments/assets/cfb67ca3-864d-445b-bd2b-05314ee009a1" />


---
## Conclusion

This project demonstrates how SDN can be used to control broadcast traffic and improve network efficiency by reducing unnecessary packet flooding.
