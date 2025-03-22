
# Welcome to the **Cash Flow Minimizer System** README!!

## **Deployment Link**: [Live website](http://13.127.192.36/)

This system is designed to minimize the **number of transactions** among multiple banks spread across different corners of the world. These banks often use **different modes of payment**, and a **world bank** with access to all payment modes acts as an intermediary for banks that have no common mode of payment. The system optimizes the transaction process and ensures smooth, efficient fund transfers.

---

## **How to Use?**

The system is completely **menu-driven** and is implemented in **C++**. Once the application is executed, the system will guide you step-by-step and generate the optimized transactions as the final output.

### **Steps to Execute the Application**:
1. Run the C++ Application from the command line.
2. Follow the on-screen instructions to input the required data.
3. The system will process the inputs and display the optimized cash flow between banks.

### **Example Execution**:

Below is a screenshot of the example execution process:

![image](https://user-images.githubusercontent.com/54183085/110011598-a33f9280-7d45-11eb-9499-a2868924cefd.png)

---

## **File Format Details**

The system expects input data in the form of text files. Below is the format for the input files:

### **1.txt** (Bank Information)

- The first line contains the number of banks.
- Each subsequent line contains:
  - Bank name.
  - Number of payment modes.
  - The list of payment modes for that bank.

## txt files will be as in this format
1.txt\
6-no of banks\
bank-noof payment modes-type of modeo of payment\
B 3 1 2 3\
C 2 1 2\
D 1 2\
E 2 1 3\
F 1 3\

2.txt\
9-no of transactions\
debt cred amt\
G B 30\
G D 10\
F B 10\
F C 30\
F D 10\
F E 10\
B C 40\
C D 20\
D E 50\

## **System Workflow**

The system minimizes the number of transactions by consolidating them through a world bank. Banks with different payment modes use the world bank to facilitate transactions. The world bank ensures efficient fund transfers between banks with no common payment modes.

Below is a visual representation of the system workflow:

![Workflow Diagram](https://github.com/user-attachments/assets/401e5dce-82da-429e-b5ba-51c8685ad7cc)

---

## **User Interface**

The system features a **clean and modern user interface** with **hover effects** and **glass card effects** that provide an intuitive experience for users. The UI has been designed with attention to detail, creating an interactive environment for users to efficiently navigate through the application.

### **Key Features**:
- **Attractive Hover Effects**: Elements on the screen respond to user interaction with smooth hover effects.
- **Glass Card Design**: Glassmorphism is used to create modern, visually appealing UI cards that display information in a clear, stylish manner.

---

## **Deployment**

This system is deployed using **Gunicorn** and **Nginx**, ensuring robust and efficient server performance. Below is a brief overview of the deployment stack:

- **Gunicorn**: Used as a WSGI HTTP server to serve the C++ application in production.
- **Nginx**: Acts as a reverse proxy server that distributes requests and handles static content delivery, ensuring scalability and high availability.

---

We hope this README provides you with a comprehensive overview of the **Cash Flow Minimizer System**. For any further questions or support, feel free to reach out!

Enjoy optimizing transactions!
