# 💬 ChatApp Django (WebSocket Real-Time Chat)

A real-time chat application built with Django Channels and Redis. It enables WebSocket-based communication between users in chat rooms without authentication.

---

## ✨ Features

- ⚡ Real-time messaging using WebSockets  
- 🏠 Dynamic room-based chat system  
- 🔁 Redis-backed channel layer  
- 🧩 Async-ready scalable architecture (ASGI)  
- 👤 Anonymous chat (no login required)  
- 🌐 Multiple users in same room chat instantly  

---

## 🛠 Tech Stack

- Django  
- Django Channels  
- Redis  
- WebSockets (ASGI)

---

## 📁 Project Structure

```
justchat/
├── chat/
│   ├── consumers.py
│   ├── routing.py
│   ├── urls.py
|   |── views.py
│   └── templates/chat/
|        |── index.html
|        └── room.html
├── justchat/
│   ├── settings.py
│   ├── asgi.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone repo
```
git clone https://github.com/Bilal-2099/chatapp_django.git
cd chatapp_django
```

### 2. Create virtual environment
```
python -m venv venv
```

Activate:
```
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run Redis
```
redis-server
```

### 5. Migrate database
```
python manage.py migrate
```

### 6. Run server
```
python manage.py runserver
```

---

## 🖥 Usage

Open in browser:

```
http://127.0.0.1:8000/chat/<room_name>/
```

Example:
```
http://127.0.0.1:8000/chat/lobby/
```

Open same room in multiple tabs to chat in real time.

---

## 🔄 How it works

- User joins a chat room
- Django Channels opens WebSocket connection
- Messages go through Redis channel layer
- All users in same room receive messages instantly

---

## 🚀 Future improvements

- Save chat history in database  
- Improve frontend UI  

---

## 📚 References

https://channels.readthedocs.io/en/latest/tutorial/index.html  
https://redis.io/docs/latest/

---
