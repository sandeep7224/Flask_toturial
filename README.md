# FastAPI Patient Management System

## Overview
This project is a FastAPI-based application designed to manage patient records. It provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on patient data stored in a JSON file (`patients.json`). The application also calculates the Body Mass Index (BMI) and provides a health verdict for each patient based on their BMI.

---

## Features

1. **View All Patients**: Retrieve all patient records.
2. **View a Specific Patient**: Retrieve details of a specific patient by their ID.
3. **Add a New Patient**: Add a new patient to the database.
4. **Update Patient Information**: Update details of an existing patient.
5. **Delete a Patient**: Remove a patient from the database.
6. **BMI Calculation**: Automatically calculates BMI and provides a health verdict (e.g., Underweight, Normal, Obese).

---

## File Structure

- **main.py**: Contains the FastAPI application and endpoint logic.
- **patients.json**: Stores patient data in JSON format.
- **README.md**: Documentation for the project.

---

## How to Run

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

3. Open your browser and navigate to:
   - API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Swagger UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Dependencies

- **FastAPI**: Web framework for building APIs.
- **Pydantic**: Data validation and settings management.
- **Uvicorn**: ASGI server for running FastAPI applications.

---

## License
This project is licensed under the MIT License.
