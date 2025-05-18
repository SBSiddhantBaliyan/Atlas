# Atlas
game designed primarly for students for knowledge of geographical locations 



# 🌍 Atlas Game (Geography Word Chain)

This is a command-line game where the player and AI take turns naming geographic locations. Each new location must start with the last letter of the previous one.

---

## 🎮 How to Play

- The game randomly starts with a geographic location.
- You must enter a valid **continent, country, state, or district** name.
- Your entry must:
  - Start with the **last letter** of the previous name.
  - Not be already used.
  - Be present in the dataset.
- The AI will respond with the next valid location.
- The game continues until one of you runs out of valid entries!

---

## 💡 Example

```
My start: Brazil  
Your turn (start with 'L'):  
Lucknow  
My turn: West Bengal  
Your turn (start with 'L'):  
```

---

## 🧠 Features

- Turn-based user vs AI gameplay  
- Checks for:
  - Starting letter correctness  
  - Duplicate entries  
  - Invalid or unknown names  
- Clean game loop logic  
- Easily extendable for new features

---

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/atlas-game.git
cd atlas-game
```

2. Run the game:

```bash
python main.py
```

---

## 📂 Files

- `main.py`: The core game logic  
- `locations.py`: Contains the dataset of valid locations (as a Python set)

---

## ✅ To Do

- Add scoring system  
- Add categories (show if it's a country, state, etc.)  
- Expand dataset (full world coverage)  
- Add GUI or web interface  

---

## 📄 License

MIT License
