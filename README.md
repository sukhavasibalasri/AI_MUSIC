# **🎵 CoverComposer – AI-Powered Music & Album Cover Generator**

## **🔍 Mood-Based Music Recommendation and AI Album Cover Creation**

CoverComposer is an AI-powered web application that combines **facial emotion detection**, **mood-based music recommendation**, **AI-generated album artwork**, and **user personalization** into a single interactive platform.

The system analyzes user emotions through facial expressions or manual mood selection and recommends suitable music tracks while simultaneously generating unique album cover artwork using Generative AI.


## **🚀 Project Overview**

CoverComposer provides a personalized entertainment experience through Artificial Intelligence.

### **Key Features**

✅ User Registration & Login Authentication

✅ Facial Emotion Detection using Face API.js

✅ Manual Mood Selection

✅ Mood-Based Music Recommendation

✅ AI-Powered Album Cover Generation

✅ Listening History Management

✅ Artwork Gallery Storage

✅ User Session Management

✅ Responsive User Interface

✅ Personalized User Experience

## **🧠 Technologies Used**

| Category             | Technology               |
| -------------------- | ------------------------ |
| Programming Language | Python                   |
| Backend Framework    | Flask                    |
| Frontend             | HTML, CSS, JavaScript    |
| Database             | SQLite                   |
| AI Image Generation  | Google Gemini AI         |
| Emotion Detection    | Face API.js              |
| Authentication       | Flask Sessions           |
| Server               | Flask Development Server |

## **📂 Project Structure**

```text
CoverComposer/
│
├── backend/
│   ├── audio_generator.py
│   ├── cover_generator.py
│   ├── database.py
│   ├── database.db
│   └── server.py
│
├── frontend/
   ├── covers/
   ├── models/
   ├── songs/
   ├── auth.js
   ├── firebase.js
   ├── script.js
   ├── style.css
   ├── index.html
   ├── login.html
   └── welcome.html

```
## 🎯 Features Explained

### 1️⃣ User Authentication

Users can securely register and log in to access personalized features.

#### Functions

* User Registration
* Login Validation
* Session Management
* Secure Account Access


### 2️⃣ Mood Detection

The system detects emotions using webcam-based facial expression analysis.

#### Supported Emotions

* Happy 😊
* Sad 😔
* Calm 😌
* Energetic ⚡
* Neutral 😐
* Surprise 😲
* Fear 😨

### 3️⃣ Music Recommendation Engine

Based on the detected or selected mood, the system recommends suitable music tracks.

#### **Features**

* Mood Mapping
* Personalized Recommendations
* Music Playback
* Enhanced Listening Experience

### **4️⃣ AI Album Cover Generation**

Google Gemini AI generates unique album cover artwork based on the user's mood and music theme.

#### **Features**

* Mood-Based Prompt Generation
* AI Artwork Creation
* Creative Album Covers
* Real-Time Generation


### **5️⃣ History Management**

The application stores user activity for future reference.

#### Stored Information

* Selected Moods
* Recommended Music
* Generated Covers
* Date and Time Records

### **6️⃣ Art Gallery**

Users can revisit previously generated album covers.

#### **Features**

* Artwork Storage
* Gallery Display
* Cover Retrieval
* User Collections


## **⚙️ Application Workflow**

### Step 1

User logs into the application.

### Step 2

User selects a mood manually or enables webcam emotion detection.

### Step 3

Face API.js analyzes facial expressions and predicts the user's emotion.

### Step 4

The detected mood is sent to the Flask backend.

### Step 5

The Music Recommendation Engine suggests suitable songs.

### Step 6

Google Gemini AI generates a personalized album cover.

### Step 7

Results are displayed on the dashboard.

### Step 8

Listening history and generated artwork are stored in SQLite.

### Step 9

Users can revisit their content through the History and Gallery sections.


## **🗄️ Database Design**

### User Table

Stores:

* User ID
* Username
* Password

### History Table

Stores:

* Selected Mood
* Recommended Music
* Generated Cover
* Timestamp

### Gallery Table

Stores:

* Generated Artwork
* User Records
* Cover Metadata

---

## 🪜 Installation Guide

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/covercomposer.git
cd covercomposer
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

pip install -r requirements.txt

### Step 5: Run Application

bash
python app.py

### Step 6: Open Browser

http://127.0.0.1:5000

## 💡 Future Enhancements

* Add more moods and music genres
* Improve recommendation accuracy
* Cloud deployment support
* Advanced AI-generated artwork styles
* User profile customization
* Playlist creation and sharing
* Voice emotion recognition
* Mobile application support

## 👩‍💻 Author

### Sukhavasi Balasri

Fourth-Year Engineering Student

Passionate about Artificial Intelligence, Web Development, and Creative AI Applications.

📧 Email: [sukhavasibalasri@gmail.com](mailto:sukhavasibalasri@gmail.com)

🌐 GitHub: https://github.com/sukhavasibalasri

## 🏁 Conclusion

CoverComposer demonstrates how Artificial Intelligence can enhance digital entertainment by combining facial emotion recognition, mood-based music recommendation, and AI-generated album artwork into a single intelligent platform.

The project showcases the practical integration of Flask, Face API.js, SQLite, and Google Gemini AI to deliver a personalized and engaging user experience.

⭐ If you like this project, please give it a star on GitHub!
