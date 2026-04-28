📸 Wally
------------------------------------------------------------------------

A lightweight image sharing web application built with Django where users can sign up, upload images, and interact with posts from other users.

Users can create posts, like images, and manage their own content through their profile.

🚀 Features
--------------------------

🔐 User Authentication
---------------------------

Sign up

Login / Logout

🖼 Image Posts

Upload images

View posts from other users

Image feed

❤️ Like System
----------------

Users can like posts from other users

👤 User Profiles

View your uploaded posts

Manage your content

✏️ Post Management
-------------------

Update posts

Delete posts

🗄 Lightweight Database

Uses SQLite for simple and fast development

🛠 Tech Stack
-------------

Backend: Django

Database: SQLite

Frontend: HTML, CSS, Django Templates

Authentication: Django Auth System


⚙️ Installation
----------------
1. Clone the repository
git clone https://github.com/rawatog/wally.git
cd wally
2. Create a virtual environment
python -m venv venv

Activate it:

Linux / Mac
-----------

source venv/bin/activate

Windows
-------

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run migrations
python manage.py migrate
5. Start the development server
python manage.py runserver

Open your browser:

http://127.0.0.1:8000

📖 Usage
--------------------------

Create an account

Upload images as posts

Browse images posted by other users

Like posts you enjoy

Manage your own posts from your profile

