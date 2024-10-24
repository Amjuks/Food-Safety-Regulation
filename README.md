# Food Safety Analysis Application

Welcome to the Food Safety Analysis Application! This project was developed during the Craft-N-Code hackathon organized by **IIIT-Bhubaneswar**. Our application allows users to upload images of food items and receive a comprehensive safety report based on current food safety regulations.

## Features

- **Image Upload**: Users can easily upload images of food items.
- **Safety Analysis**: The application processes the image and provides a detailed safety report.
- **User-Friendly Interface**: Designed with usability in mind for a seamless experience.

## Technologies Used

- **Django**
- **OpenAI API**
- **HTML/CSS**
- **JavaScript**

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Amjuks/Food-Safety-Regulation.git
   cd food-safety-analysis
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Use `venv\Scripts\activate` on Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the Application**:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

6. **Access**: Open `http://127.0.0.1:8000` in your browser.

## Contributers
- @Amjuks
- @aaradhyasaxena0606
- @Shubhang-Kuber
- @thinbearr

## License

This project is licensed under the MIT License.

---

Thank you for using our application! Happy coding!
