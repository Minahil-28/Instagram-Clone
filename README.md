

\# Ministagram



\*\*An Instagram-inspired social networking platform built to demonstrate real-world Data Structures \& Algorithms\*\*





\---



\## Overview



Ministagram is a fully functional desktop social media application that mirrors core Instagram features — but with every underlying mechanism built from scratch using fundamental data structures. No shortcuts, no built-in sort functions, no black-box libraries for logic. Every feed sort, every search, every undo action runs through a hand-implemented algorithm.



The goal was to answer a question that most CS courses leave abstract: \*how do real platforms like Instagram actually manage millions of users, posts, and interactions at scale?\* This project answers that concretely.



\---



\## Features



| Feature | Implementation |

|---|---|

| User registration \& login | Doubly Linked List (user store) + SHA-256 password hashing |

| Post creation \& feed | Queue (FIFO post management) + MD5-generated post IDs |

| Trending feed | Quick Sort by like count — O(n log n) |

| Latest feed | Merge Sort by timestamp — O(n log n) |

| Friends feed | Filtered queue + sorted by timestamp |

| Comments | Stack (LIFO — newest comment on top) |

| Undo mechanism | Stack — reverses likes, deletes, and other actions |

| Friend requests \& notifications | Hash Table (username → notification queue) |

| Keyword search | Custom keyword search — O(n×m) |

| Profile management | Input validation (email, name, DOB) with descriptive error messages |

| Data persistence | JSON-formatted flat file storage (users.txt, posts.txt, notifications.txt) |

| Dark/light theme | Toggle between deep dark mode and clean light mode |



\---



\## Data Structures Used



All data structures are implemented from scratch — no imports of Python's `collections` or sorting builtins for core logic.



\*\*Doubly Linked List\*\* — user management. O(1) insertion at head/tail, bidirectional traversal.



\*\*Queue\*\* — post feed. FIFO ordering matches chronological post flow. New posts enqueue at rear.



\*\*Stack\*\* — comments (newest first) and undo history. LIFO behavior handles both naturally.



\*\*Priority Queue\*\* — notification system. Different notification types (friend requests, likes, comments) carry different priority weights.



\*\*Hash Table (dict)\*\* — O(1) username lookup, notification mapping, post ID indexing.



\---



\## Algorithms Implemented



\### Sorting

\- \*\*Bubble Sort\*\* — educational baseline, O(n²)

\- \*\*Insertion Sort\*\* — small list optimization, O(n²)

\- \*\*Selection Sort\*\* — comparison demonstration, O(n²)

\- \*\*Quick Sort\*\* — trending feed (sort by likes), O(n log n) average

\- \*\*Merge Sort\*\* — latest feed (sort by timestamp), O(n log n) guaranteed



\### Searching

\- \*\*Linear Search\*\* — unsorted collections, O(n)

\- \*\*Binary Search\*\* — sorted collections, O(log n)

\- \*\*Keyword Search\*\* — post/user content search, O(n×m)

\- \*\*Quick Select\*\* — k-th element selection, O(n) average



\---



\## Architecture



```

Ministagram

├── Application Layer     → CustomTkinter GUI

├── Business Logic Layer  → Data Manager \& Operations

├── Data Structure Layer  → Linked List, Queue, Stack, Priority Queue

└── Persistence Layer     → users.txt | posts.txt | notifications.txt

```



\---



\## Tech Stack



\- \*\*Language:\*\* Python

\- \*\*GUI:\*\* CustomTkinter (glassmorphism-style UI — no external UI libraries)

\- \*\*Storage:\*\* JSON flat files

\- \*\*Hashing:\*\* MD5 (post IDs), SHA-256 (passwords)

\- \*\*Architecture:\*\* Threaded operations to keep UI responsive during I/O



\---



\## Getting Started



```bash

\# Clone the repository

git clone https://github.com/Minahil-28/Ministagram.git

cd Ministagram



\# Install dependencies

pip install customtkinter pillow



\# Run the app

python main.py

```



\---



\## Screenshots



| Splash \& Login | Dashboard Feed |

|---|---|

| Instagram-style splash screen with animated loading dots | Sidebar navigation with Trending / Latest / Friends feed tabs |



| Profile | Notifications |

|---|---|

| Post grid, friends list, sort options (Newest / Oldest / Popular) | Real-time notifications with accept/decline for friend requests |



\---



This project was built to demonstrate that DSA isn't theoretical — every data structure taught in class maps directly to something a real application does. Ministagram makes that mapping explicit.



\---





Built by \[Minahil Mehmood](https://www.linkedin.com/in/minahil-mehmood-9aa205328) · UET Lahore





