# OpenModelica Desktop App using PyQt6

## 📌 Overview

This project is a desktop application built using **Python (PyQt6)** that allows users to execute an OpenModelica simulation model (`TwoConnectedTanks`) by providing runtime parameters.

The application provides a simple GUI where users can:

* Select the executable file generated from OpenModelica
* Enter start time and stop time
* Run the simulation with a single click

---

## ⚙️ Technologies Used

* Python 3.11
* PyQt6
* OpenModelica
* Windows OS

---

## 📂 Project Structure

```
OpenModelica_Project/
│
├── app/
│   └── main.py
│
├── model/
│   ├── TwoConnectedTanks.exe
│   ├── *.dll
│   ├── *.mat
│   ├── *.bin
│   └── other dependency files
│
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Install Dependencies

```
pip install -r requirements.txt
```

### 2. Run Application

```
py -3.11 app/main.py
```

---

## 🖥️ Usage

1. Click **Browse** and select:

   ```
   model/TwoConnectedTanks.exe
   ```

2. Enter:

   ```
   Start Time: 0  
   Stop Time: 3
   ```

3. Click **Run Simulation**

---

## ✅ Validation Condition

```
0 ≤ start time < stop time < 5
```

---

## ⚠️ Notes

- Some warnings (e.g., division by zero or override messages) may appear in the terminal due to model behavior and do not affect application execution.
- The application successfully executes the simulation executable with user-defined parameters.
- All required `.dll` files must be present in the same directory as the `.exe`.
- Executable and dependency files are excluded due to size. The project demonstrates GUI-based execution of OpenModelica simulations.

---

## 🎯 Features

* User-friendly GUI
* File selection dialog
* Input validation
* Subprocess execution with parameters
* Error handling

---

## 👨‍💻 Author

**Sakshi Chandravanshi**
